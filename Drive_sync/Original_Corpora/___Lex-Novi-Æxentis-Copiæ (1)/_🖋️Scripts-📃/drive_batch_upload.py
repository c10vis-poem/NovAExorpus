#!/usr/bin/env python3
"""
Recursive directory mirror to Google Drive with concurrent uploads,
MD5 deduplication, and folder caching.
"""

import os
import sys
import time
import math
import hashlib
import argparse
import mimetypes
import threading
from collections import Counter
from concurrent.futures import ThreadPoolExecutor, as_completed

try:
    from google.auth.transport.requests import Request
    from google.oauth2.credentials import Credentials
    from google.oauth2 import service_account
    from google_auth_oauthlib.flow import InstalledAppFlow
    from googleapiclient.discovery import build
    from googleapiclient.http import MediaFileUpload
    from googleapiclient.errors import HttpError
except ImportError:
    pass

SCOPES = ["https://www.googleapis.com/auth/drive"]
DEFAULT_WORKERS = 6
DEFAULT_CHUNK_SIZE_MB = 8
MAX_RETRIES = 5

_thread_local = threading.local()

def get_drive_service(creds):
    """Returns a thread-safe Google Drive API service instance."""
    if not hasattr(_thread_local, "service"):
        _thread_local.service = build("drive", "v3", credentials=creds, cache_discovery=False)
    return _thread_local.service

def authenticate(credentials_path="credentials.json", token_path="token.json", service_account_path=None):
    """
    Handles authentication using either OAuth2 client secrets or a Service Account JSON.
    Saves and refreshes token.json automatically.
    """
    if service_account_path and os.path.exists(service_account_path):
        return service_account.Credentials.from_service_account_file(
            service_account_path, scopes=SCOPES
        )

    creds = None
    if os.path.exists(token_path):
        creds = Credentials.from_authorized_user_file(token_path, SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            if not os.path.exists(credentials_path):
                raise FileNotFoundError(
                    f"Authentication file '{credentials_path}' not found.\n"
                    f"Please download your client_secrets OAuth JSON from Google Cloud Console "
                    f"and save it as '{credentials_path}', or provide --service-account."
                )
            flow = InstalledAppFlow.from_client_secrets_file(credentials_path, SCOPES)
            try:
                creds = flow.run_local_server(port=0)
            except Exception:
                creds = flow.run_console()

        with open(token_path, "w") as token_file:
            token_file.write(creds.to_json())

    return creds

def sha256_or_md5_of(path):
    """Calculates MD5 hash of local file in 1MB chunks to match Drive md5Checksum."""
    h = hashlib.md5()
    try:
        with open(path, "rb") as f:
            for chunk in iter(lambda: f.read(1024 * 1024), b""):
                h.update(chunk)
        return h.hexdigest()
    except OSError:
        return None

def human_size(bytes_val):
    """Converts bytes to human readable format."""
    if not bytes_val:
        return "0 B"
    units = ["B", "KB", "MB", "GB", "TB"]
    i = int(math.floor(math.log(bytes_val, 1024)))
    p = math.pow(1024, i)
    s = round(bytes_val / p, 2)
    return f"{s} {units[i]}"

class DriveFolderManager:
    """Manages folder tree traversal and folder creation on Drive with caching."""
    def __init__(self, creds, root_parent_id="root"):
        self.creds = creds
        self.root_parent_id = root_parent_id
        self.folder_cache = {"": root_parent_id}
        self.folder_contents_cache = {}  # folder_id -> {filename: {"id": id, "md5": md5}}
        self.lock = threading.Lock()

    def get_remote_folder_contents(self, folder_id):
        """Lists files inside a Drive folder and indexes them by name."""
        with self.lock:
            if folder_id in self.folder_contents_cache:
                return self.folder_contents_cache[folder_id]

        service = get_drive_service(self.creds)
        files_by_name = {}
        page_token = None
        query = f"'{folder_id}' in parents and mimeType != 'application/vnd.google-apps.folder' and trashed = false"

        while True:
            resp = service.files().list(
                q=query,
                fields="nextPageToken, files(id, name, md5Checksum, size)",
                pageToken=page_token,
                pageSize=1000
            ).execute()

            for item in resp.get("files", []):
                files_by_name[item["name"]] = {
                    "id": item["id"],
                    "md5": item.get("md5Checksum"),
                    "size": int(item.get("size", 0))
                }

            page_token = resp.get("nextPageToken")
            if not page_token:
                break

        with self.lock:
            self.folder_contents_cache[folder_id] = files_by_name
        return files_by_name

    def ensure_remote_dir(self, rel_dir):
        """Recursively ensures that the remote folder structure exists on Drive."""
        rel_dir = rel_dir.strip(os.sep).replace("\\", "/")
        with self.lock:
            if rel_dir in self.folder_cache:
                return self.folder_cache[rel_dir]

        parts = rel_dir.split("/") if rel_dir else []
        current_rel = ""
        current_parent_id = self.root_parent_id

        for part in parts:
            current_rel = f"{current_rel}/{part}".strip("/")
            with self.lock:
                if current_rel in self.folder_cache:
                    current_parent_id = self.folder_cache[current_rel]
                    continue

            service = get_drive_service(self.creds)
            escaped_name = part.replace("'", "\\'")
            query = f"'{current_parent_id}' in parents and name = '{escaped_name}' and mimeType = 'application/vnd.google-apps.folder' and trashed = false"
            
            resp = service.files().list(q=query, fields="files(id, name)", pageSize=10).execute()
            items = resp.get("files", [])

            if items:
                folder_id = items[0]["id"]
            else:
                folder_metadata = {
                    "name": part,
                    "mimeType": "application/vnd.google-apps.folder",
                    "parents": [current_parent_id]
                }
                folder = service.files().create(body=folder_metadata, fields="id").execute()
                folder_id = folder["id"]

            with self.lock:
                self.folder_cache[current_rel] = folder_id
            current_parent_id = folder_id

        return current_parent_id

def upload_single_file(file_info, creds, folder_manager, chunk_size_bytes, dry_run=False):
    """Uploads or updates a single file with resumable streaming and retry logic."""
    local_path = file_info["local_path"]
    rel_path = file_info["rel_path"]
    rel_dir = file_info["rel_dir"]
    filename = file_info["filename"]
    size = file_info["size"]

    if dry_run:
        return {"status": "DRY_RUN", "rel_path": rel_path, "size": size}

    service = get_drive_service(creds)
    parent_folder_id = folder_manager.ensure_remote_dir(rel_dir)
    remote_contents = folder_manager.get_remote_folder_contents(parent_folder_id)

    local_md5 = sha256_or_md5_of(local_path)
    existing = remote_contents.get(filename)

    if existing and existing.get("md5") and local_md5 and existing["md5"].lower() == local_md5.lower():
        return {"status": "SKIPPED_IDENTICAL", "rel_path": rel_path, "size": size}

    mime_type, _ = mimetypes.guess_type(local_path)
    if not mime_type:
        mime_type = "application/octet-stream"

    resumable = size > (5 * 1024 * 1024)
    media = MediaFileUpload(
        local_path,
        mimetype=mime_type,
        chunksize=chunk_size_bytes if resumable else -1,
        resumable=resumable
    )

    for attempt in range(1, MAX_RETRIES + 1):
        try:
            if existing:
                file_id = existing["id"]
                req = service.files().update(fileId=file_id, media_body=media, fields="id, md5Checksum, size")
            else:
                file_metadata = {
                    "name": filename,
                    "parents": [parent_folder_id]
                }
                req = service.files().create(body=file_metadata, media_body=media, fields="id, md5Checksum, size")

            response = None
            if resumable:
                while response is None:
                    _, response = req.next_chunk()
            else:
                response = req.execute()

            with folder_manager.lock:
                remote_contents[filename] = {
                    "id": response["id"],
                    "md5": response.get("md5Checksum"),
                    "size": int(response.get("size", size))
                }

            action = "UPDATED" if existing else "UPLOADED"
            return {"status": action, "rel_path": rel_path, "size": size}

        except (HttpError, OSError) as exc:
            if attempt == MAX_RETRIES:
                return {"status": "FAILED", "rel_path": rel_path, "error": str(exc), "size": size}
            time.sleep(2 ** attempt)

def scan_local_directory(src_root):
    """Discovers all files in the source directory."""
    files_to_upload = []
    total_bytes = 0
    for dirpath, _, filenames in os.walk(src_root):
        for fn in filenames:
            full_path = os.path.join(dirpath, fn)
            rel_path = os.path.relpath(full_path, src_root)
            rel_dir = os.path.dirname(rel_path)
            try:
                st = os.stat(full_path)
                size = st.st_size
            except OSError:
                continue

            files_to_upload.append({
                "local_path": full_path,
                "rel_path": rel_path,
                "rel_dir": rel_dir,
                "filename": fn,
                "size": size
            })
            total_bytes += size

    return files_to_upload, total_bytes

def batch_upload(src_root, parent_id="root", workers=DEFAULT_WORKERS, chunk_size_mb=DEFAULT_CHUNK_SIZE_MB,
                 creds_path="credentials.json", token_path="token.json", service_account_path=None, dry_run=False):
    """Executes the high-speed batch upload operation."""
    print(f"Scanning source directory: {src_root} ...")
    files, total_bytes = scan_local_directory(src_root)
    print(f"Found {len(files)} files ({human_size(total_bytes)}).")

    if not files:
        print("No files found to process.")
        return Counter()

    print("Authenticating with Google Drive API...")
    creds = authenticate(creds_path, token_path, service_account_path)
    folder_manager = DriveFolderManager(creds, root_parent_id=parent_id)

    chunk_size_bytes = chunk_size_mb * 1024 * 1024
    stats = Counter()
    start_time = time.time()
    uploaded_bytes = 0

    print(f"\nStarting concurrent transfer with {workers} worker threads...\n")

    with ThreadPoolExecutor(max_workers=workers) as executor:
        futures = {
            executor.submit(upload_single_file, f, creds, folder_manager, chunk_size_bytes, dry_run): f
            for f in files
        }

        for future in as_completed(futures):
            res = future.result()
            status = res["status"]
            rel_path = res["rel_path"]
            size_str = human_size(res.get("size", 0))

            if status in ("UPLOADED", "UPDATED"):
                stats["uploaded"] += 1
                uploaded_bytes += res.get("size", 0)
                print(f"[{status:8s}] {size_str:>9s} | {rel_path}")
            elif status == "SKIPPED_IDENTICAL":
                stats["skipped_identical"] += 1
                print(f"[SKIP-MD5] {size_str:>9s} | {rel_path}")
            elif status == "DRY_RUN":
                stats["dry_run"] += 1
                print(f"[DRY-RUN ] {size_str:>9s} | {rel_path}")
            else:
                stats["failed"] += 1
                err = res.get("error", "Unknown")[:60]
                print(f"[FAILED  ] {size_str:>9s} | {rel_path} -> {err}")

    elapsed = max(time.time() - start_time, 0.001)
    rate = (uploaded_bytes / (1024 * 1024)) / elapsed

    print("\n" + "=" * 50)
    print("                TRANSFER SUMMARY")
    print("=" * 50)
    print(f"Total files scanned  : {len(files)}")
    print(f"Files uploaded/synced: {stats['uploaded']}")
    print(f"Identical skipped    : {stats['skipped_identical']}")
    print(f"Failed               : {stats['failed']}")
    print(f"Transferred volume   : {human_size(uploaded_bytes)}")
    print(f"Time elapsed         : {elapsed:.2f}s ({rate:.2f} MB/s)")
    print("=" * 50 + "\n")

    return stats

def main():
    parser = argparse.ArgumentParser(
        description="Fast recursive batch folder uploader to Google Drive with deduplication."
    )
    parser.add_argument("source", help="Path to local folder to upload")
    parser.add_argument("--parent-id", default="root", help="Google Drive target folder ID (default: 'root')")
    parser.add_argument("--workers", type=int, default=DEFAULT_WORKERS, help=f"Concurrent threads (default: {DEFAULT_WORKERS})")
    parser.add_argument("--chunk-size", type=int, default=DEFAULT_CHUNK_SIZE_MB, help=f"Resumable chunk size in MB (default: {DEFAULT_CHUNK_SIZE_MB})")
    parser.add_argument("--credentials", default="credentials.json", help="Path to client credentials JSON")
    parser.add_argument("--token", default="token.json", help="Path to cached token JSON")
    parser.add_argument("--service-account", default=None, help="Optional path to service account JSON")
    parser.add_argument("--dry-run", action="store_true", help="Simulate upload without transferring files")

    args = parser.parse_args()

    if not os.path.exists(args.source):
        print(f"Error: source path '{args.source}' does not exist.", file=sys.stderr)
        sys.exit(1)

    batch_upload(
        src_root=args.source,
        parent_id=args.parent_id,
        workers=args.workers,
        chunk_size_mb=args.chunk_size,
        creds_path=args.credentials,
        token_path=args.token,
        service_account_path=args.service_account,
        dry_run=args.dry_run
    )

if __name__ == "__main__":
    main()
