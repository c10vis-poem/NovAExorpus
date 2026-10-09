---
title: "export_drive_docs.js"
source: "Drive_sync/Secure-Spark-Proof-Folder /raw_database/spark_recommendations/03_ALTERNATIVES_PROPOSAL_V1/tools/export_drive_docs.js.pdf"
cleaned: 2026-10-08
converter: "pymupdf get_text via tools/clean.py normalize_markdown"
tags:
  - pdf-conversion
---

/**
 * Automated Google Drive Document Exporter (Markdown & JSONL Only)
 * Watches a designated source folder and exports Google Docs directly
 * into clean Markdown (.md) and structured raw-text records (.jsonl).
 */

const SOURCE_FOLDER_ID = "YOUR_SOURCE_FOLDER_ID";
const DESTINATION_FOLDER_ID = "YOUR_DESTINATION_FOLDER_ID";

function exportGoogleDocsToMarkdown() {
  const srcFolder = DriveApp.getFolderById(SOURCE_FOLDER_ID);
  const destFolder = DriveApp.getFolderById(DESTINATION_FOLDER_ID);
  const files = srcFolder.getFilesByType(MimeType.GOOGLE_DOCS);

  while (files.hasNext()) {
    const doc = files.next();
    const docId = doc.getId();
    const baseName = doc.getName();

    // 1. Export as Clean Markdown (.md) via Google's native markdown endpoint
    const exportUrl =
`https://docs.google.com/feeds/download/documents/export/Export?exportFormat=markdown&i
d=${docId}`;
    const response = UrlFetchApp.fetch(exportUrl, {
      headers: { Authorization: 'Bearer ' + ScriptApp.getOAuthToken() },
      muteHttpExceptions: true
    });

    if (response.getResponseCode() === 200) {
      const existingMd = destFolder.getFilesByName(baseName + ".md");
      if (existingMd.hasNext()) {
        existingMd.next().setContent(response.getBlob().getDataAsString());
      } else {
        destFolder.createFile(response.getBlob()).setName(baseName + ".md");
      }
    }

    // 2. Export as Machine-Readable JSONL (.jsonl)
    const docText = DocumentApp.openById(docId).getBody().getText();
    const jsonlRecord = JSON.stringify({
      file_name: baseName,
      source_id: docId,
      exported_at: new Date().toISOString(),


      text: docText
    }) + "\n";

    const existingJsonl = destFolder.getFilesByName(baseName + ".jsonl");
    if (existingJsonl.hasNext()) {
      existingJsonl.next().setContent(jsonlRecord);
    } else {
      destFolder.createFile(baseName + ".jsonl", jsonlRecord, MimeType.PLAIN_TEXT);
    }
  }
}
