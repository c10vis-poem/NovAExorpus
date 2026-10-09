---
title: "gcloud storage command"
source: "Drive_sync/Original_Corpora/__NovÆxorpus(NÆX)/4-UNIVERSAL_MEMORY_(16-files)/gcloud storage command.pdf"
cleaned: 2026-10-08
converter: "pymupdf get_text via tools/clean.py normalize_markdown"
tags:
  - pdf-conversion
---

Because you installed the modern google-cloud-cli, we are going to use the gcloud storage
command. It replaced the older gsutil tool and is significantly faster at parallel uploads, which is
exactly what you want when pushing heavy PDFs from a tablet.
Here are the exact commands to get your data into the cloud.
1. Create the Storage Bucket
There is one major catch with Google Cloud Storage: bucket names must be globally unique
across the entire internet. You cannot just name it my-pdfs. The easiest way to guarantee a
unique name is to slap your Project ID on the end of it.
Run this command to create the bucket. For the location flag, us-west1 (Oregon) will give you
the fastest upload speeds from Washington.



Bash
gcloud storage buckets create gs://raw-docs-YOUR-PROJECT-ID --location=us-west1​

(Replace YOUR-PROJECT-ID with the actual ID you set up in the last step).
2. Upload Your PDFs
Assuming you have all your Qualcomm specs, Unsloth docs, and repo manuals sitting in a
specific Termux directory (e.g., ~/docs/pdfs/), you use the recursive copy command to blast the
entire folder up to the cloud at once.



Bash
gcloud storage cp -r ~/path/to/your/pdf/folder/* gs://raw-docs-YOUR-PROJECT-ID/​

●​ The -r flag tells it to look recursively inside any subfolders you might have organized them
into.
●​ The * grabs every file in that directory.
3. Verify the Upload
Once the upload finishes, run a quick list command to make sure the cloud bucket actually
sees all your files:





Bash
gcloud storage ls gs://raw-docs-YOUR-PROJECT-ID/​

If you see your list of PDFs spit back out in the terminal, your cold storage layer is officially live
in the cloud. Your Snapdragon 8 Elite is completely free of the storage and processing burden
of those raw files.
