---
title: "Google cloud API hooks guide through termux."
source: "Drive_sync/Original_Corpora/___Lex-Novi-Æxentis-Copiæ (1)/--•🖥️_TERMUX_[__ ]_main./Google cloud API hooks guide through termux..pdf"
cleaned: 2026-10-08
converter: "pymupdf get_text via tools/clean.py normalize_markdown"
tags:
  - pdf-conversion
---

I know exactly the nightmare you are talking about. Google Cloud’s IAM (Identity and Access
Management) console is a labyrinth designed for massive enterprise IT departments, not a solo
developer building an edge-agent. If you try to click through the web UI to figure out service
accounts, permissions, and API scopes, you will absolutely lose 4 hours of your life.
We are going to bypass the web interface completely for the hard stuff. We’ll do the bare
minimum in the browser to claim your $1,000 credits, and then we will use the terminal (Cloud
Shell) to force-enable everything instantly.
Here is your ground-zero, zero-friction setup guide.
Step 1: Find the Money
Do not go to Google AI Studio. Do not go to Google Developers. Go straight to the Google
Cloud Console.
1.​ Open an incognito window (to prevent your personal Google accounts from crossing
wires) and log in to the account that received the credits.
2.​ Go directly to console.cloud.google.com/billing.
3.​ You should see your $1,000 credit listed under a "Billing Account." If it asks you to set one
up, do it, and the credits should apply automatically.
Step 2: Create the Project (The Container)
Everything in GCP lives inside a "Project." We need to make one and attach it to your free
money.
1.​ At the top left of the console, click the drop-down (it probably says "Select a project").
2.​ Click New Project.
3.​ Name it something obvious like agent-knowledge-pipeline.
4.​ Under "Billing Account," make sure the one with your $1,000 credit is selected. Click
Create.
Step 3: Bypass the UI and Enable APIs via Cloud Shell
This is where people get stuck clicking through menus. We aren't doing that.
1.​ At the top right of the Google Cloud website, look for an icon that looks like a little
terminal prompt (>_). Hovering over it says Activate Cloud Shell. Click it.
2.​ A terminal will pop up at the bottom of your browser. This terminal already has owner
permissions for your project.
3.​ Run this exact command to ensure the shell is hooked to your new project (replace
your-project-id with the actual ID, which you can see in the project dropdown):​
Bash​
gcloud config set project your-project-id​

4.​ Now, run this single command to instantly enable Vertex AI, Document AI, and Google
Cloud Storage. No clicking required:​
Bash​
gcloud services enable aiplatform.googleapis.com storage.googleapis.com
documentai.googleapis.com​



Step 4: Hooking Termux to the Cloud
Now you have a cloud environment with the APIs turned on and the credits attached. You need
to give your Snapdragon tablet the keys so it can upload the PDFs and trigger the batch jobs.
Inside your Termux terminal on your tablet, run these commands:
1.​ Install the Google Cloud CLI:​
Bash​
pkg install python​
pip install google-cloud-cli​

2.​ Log in and authenticate your tablet:​
Bash​
gcloud auth application-default login​
​
(This will spit out a URL. Copy it, open it in your tablet's browser, sign in with your Google
account, and hit allow. This bypasses the need to create messy "Service Account JSON
keys" because it authenticates you as the owner.)
3.​ Tell Termux which project to use:​
Bash​
gcloud config set project your-project-id​

That’s it. You are out of the permissions nightmare. Your tablet now has a direct, authenticated
pipeline to your $1,000 Vertex AI credits, and you didn't have to configure a single IAM role.
