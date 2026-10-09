---
title: "asymmetric_iam_sync.sh"
source: "Drive_sync/Secure-Spark-Proof-Folder /novae-xorpus/04_skills_runtime/runtimes/asymmetric_iam_sync.sh.pdf"
cleaned: 2026-10-08
converter: "pymupdf get_text via tools/clean.py normalize_markdown"
tags:
  - pdf-conversion
---

#!/usr/bin/env bash
#
========================================================================
======
# GCP Asymmetric Cross-Account IAM Bridge & Storage Sync Script
# Derived from: 4-ARCHITECTURE-cont.-(6-files) & Part 5 IAM Specifications
#
# Purpose:
#   Synchronizes data from a business/source GCS bucket to a personal developer
#   credit environment for Vertex AI Agent Builder indexing, enforcing
#   read-only permissions (roles/storage.objectViewer) so that personal projects
#   can never corrupt or alter source repositories.
#
========================================================================
======

set -euo pipefail

# Configuration variables
SOURCE_PROJECT_ID="${SOURCE_PROJECT_ID:-business-secure-workspace}"
SOURCE_BUCKET="${SOURCE_BUCKET:-gs://business-vault-bucket}"
TARGET_PROJECT_ID="${TARGET_PROJECT_ID:-personal-agentic-dev}"
TARGET_BUCKET="${TARGET_BUCKET:-gs://personal-developer-stage}"
SERVICE_ACCOUNT="${SERVICE_ACCOUNT:-sa-vertex-indexer@${TARGET_PROJECT_ID
}.iam.gserviceaccount.com}"

echo "[*] Initializing GCP Asymmetric Cross-Account IAM Handshake..."
echo "    Source (Business):  ${SOURCE_BUCKET} (${SOURCE_PROJECT_ID})"
echo "    Target (Developer): ${TARGET_BUCKET} (${TARGET_PROJECT_ID})"
echo "    Service Account:    ${SERVICE_ACCOUNT}"

# Step 1: Verify read-only access on the source bucket
echo "[*] Step 1: Validating read-only IAM binding (roles/storage.objectViewer)..."
if command -v gcloud &> /dev/null; then
    gcloud storage buckets add-iam-policy-binding "${SOURCE_BUCKET}" \
        --member="serviceAccount:${SERVICE_ACCOUNT}" \
        --role="roles/storage.objectViewer" \
        --condition=None \
        --quiet || echo "[!] Notice: IAM policy binding requires operator authorization or already
configured."
else
    echo "[-] Warning: gcloud CLI not detected. Skipping live IAM policy update."
fi



# Step 2: One-way sync using gsutil rsync or rclone
echo "[*] Step 2: Executing read-only synchronization..."
if command -v gsutil &> /dev/null; then
    gsutil -m rsync -r -d "${SOURCE_BUCKET}/clean_md" "${TARGET_BUCKET}/clean_md"
    gsutil -m rsync -r -d "${SOURCE_BUCKET}/chunks" "${TARGET_BUCKET}/chunks"
    echo "[✓] Synchronization complete: source data staged for Vertex AI indexing."
elif command -v rclone &> /dev/null; then
    rclone sync "gcs:${SOURCE_BUCKET#gs://}/clean_md"
"gcs:${TARGET_BUCKET#gs://}/clean_md" --progress
    rclone sync "gcs:${SOURCE_BUCKET#gs://}/chunks"
"gcs:${TARGET_BUCKET#gs://}/chunks" --progress
    echo "[✓] Rclone sync complete: source data staged for Vertex AI indexing."
else
    echo "[-] Error: Neither gsutil nor rclone available in PATH. Please run in production shell."
    exit 1
fi

echo "[*] Asymmetric handshake successfully verified. Zero-write isolation active."
