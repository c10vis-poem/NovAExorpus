---
source: gcp-cross-account-handshake (Markor)
type: pdf
cleaned: 2026-09-11
cleaner: tools/clean.py (mutool)
---

🌌 GCP CROSS-ACCOUNT SECURE DATA HANDSHAKE
PROTOCOL

Subsystem: Cloud-to-Edge Data Ingestion & Credit-Funded RAG Auditing

Version: 1.0.0 (Production Blueprint)

1. THE ARCHITECTURAL PLAN: DIVISION OF LABORS

To protect your intellectual property behind strict corporate/business workspace walls while absorbing
100% of the heavy query, indexing, and token-processing costs via your personal account’s $1,000
Vertex AI Agent Builder credit pool, the system uses an asymmetric, cross-organizational IAM
handshake.

┌──────────────────────────────────────┐

┌──────────────────────────────────────┐
│  BUSINESS / CONTRACTOR RESOURCE TIER │          │      PERSONAL
DEVELOPER CREDIT TIER  │
│  (Holds Secure GCS Bucket / Raw IP)  │          │      (Houses Vertex AI

/ Cloud Run)  │
├──────────────────────────────────────┤
├──────────────────────────────────────┤
│                                      │          │

│
│   gs://business-secure-vault-bucket  │          │   Grounded Generation
API (Agent)    │
│                  │                   │          │                  ▲
│

│                  │                   │          │                  │
│
│                  ▼                   │          │                  │
│

│        [Storage Object Viewer]       │          │          [Data Store
Index]          │
│                  │                   │          │                  ▲
│

│
└───────────────────┼──────────┼──────────────────┘
│
│                     (Grant Read-Only │          │ (Vertex AI Discovery
Engine SA)      │


Core Design Principles:

1. No Data Relocation (Zero-Copy): Raw data files never physically duplicate or migrate into your
personal developer environment. They remain inside the business or contractor’s encrypted
storage vault, maintaining 100% local IP ownership.
2. Compute-Credit Redirection: The personal-tier project initiates and manages the indexing,
semantic search, and grounding executions. This ensures that every billing token represents an
application application SKU charge that is absorbed by your personal $1,000 credit pool rather
than hitting business or personal debit cards.
3. Instant Access Severance: If a contractor contract ends or employee clearance is revoked, the
business administrator simply removes the Service Account member from the bucket’s Access
Control List (ACL). Access is terminated instantly at the cloud boundary, leaving the consumer
project with empty indexes.

2. THE ROUTE MAP & PRINCIPALS

Credit-Consumer Project (Personal Account):

Role: Executes the RAG pipelines, schedules nightly logs analysis, and hosts the Cloud Run
gateway.
Service Account: service-PERSONAL_PROJECT_NUMBER@gcp-sa-
discoveryengine.iam.gserviceaccount.com (This is Google’s Discovery Engine system
identity used to crawl storage paths).
IP-Owner Project (Business Account or Contractor):

Role: Holds the source files, raw code repository logs, and operational specifications.
Resource: gs://business-secure-vault-bucket/ (Standard Google Cloud Storage bucket).
The Connection Gate:

Role: roles/storage.objectViewer (Read-only object access; blocks writing, deleting, or
credential modifications).

3. THE HANDOFF BluePrint DOCUMENT (Step-by-Step)

Phase 1: Retrieve Your Personal Project Number

1. Log into the Google Cloud Console using your personal account (holding the credits).
2. Ensure you have selected your active developer project.
3. On the Home Dashboard, look at the Project Info card and copy the Project Number (e.g.,
8589934592).

Phase 2: Assemble Your Service Account Identifier

Construct the email identifier for your personal Vertex AI system agent using your copied Project
Number:

service-PERSONAL_PROJECT_NUMBER@gcp-sa-discoveryengine.iam.gserviceaccount.com

│                        Permissions)  │          │
│
└──────────────────────────────────────┘

└──────────────────────────────────────┘


Phase 3: Business Bucket Configuration (To be executed by the Business Admin)

The owner of the sensitive files must grant your personal service account read-only access to their
bucket:

1. Open the Google Cloud Console using the Business Workspace account.
2. Navigate to Cloud Storage > Buckets and click on your secure bucket (gs://business-secure-
vault-bucket).
3. Select the Permissions tab and click Grant Access (or Add Principal).
4. Paste the Service Account email created in Phase 2 into the New Principals field.
5. In the Select a Role menu, choose Cloud Storage > Storage Object Viewer
(roles/storage.objectViewer).
6. Click Save.

Phase 4: Create the Data Store in Your Personal Vertex AI Suite

Now, connect the secure bucket directly to your credit-funded Agent Builder:

1. Return to your Personal Account GCP Console.
2. Navigate to Vertex AI Agent Builder > Data Stores.
3. Click Create Data Store and choose Cloud Storage.
4. In the Cloud Storage path field, enter the direct address of the business bucket:
gs://business-secure-vault-bucket/
5. Choose Unstructured documents (if parsing PDFs, text files, or Markdown notes) and select
Continuous import to allow real-time changes to stream directly into your local cache indices.
6. Click Create. Your Vertex AI agent can now safely parse and ground its responses using your
business’s proprietary manuals without copying them!

4. THE AUTOMATED HANDOFF BOOTSTRAP SCRIPT

Save this script as gcp_cross_account_handshake.sh and make it executable with chmod +x
gcp_cross_account_handshake.sh . You can run it inside your Termux shell or local CLI environment to
automate the setup process using Google Cloud SDK ( gcloud ).

#!/usr/bin/env bash
#
==========================================================================

====
# AESOP XI: CROSS-ACCOUNT RESOURCE INGESTION & CREDIT HARNESS
# Script ID: AX-GCP-CROSS-ACCOUNT-HANDSHAKE-BOOTSTRAP
#

==========================================================================
====
set -euo pipefail


# Style definitions for clean terminal telemetry output
RED='\033[0;31m'
GREEN='\033[0;32m'
CYAN='\033[0;36m'


YELLOW='\033[1;33m'
NC='\033[0m' # No Color


clear
echo -e
"\${CYAN}=================================================================
==============="

echo -e "🌌 [GCP CROSS-ACCOUNT HANDSHAKE] Initializing Sovereign
Connection Pipeline..."
echo -e
"=========================================================================

=======\${NC}"

# Ensure gcloud CLI is installed
if ! command -v gcloud &> /dev/null; then

    echo -e "\${RED}❌ ERROR: Google Cloud SDK (gcloud) is not installed
in this shell.\${NC}"
    echo -e "👉 Install it via: pkg install google-cloud-sdk (or follow
your OS guide)."
    exit 1

fi

# Step 1: Identify Consumer (Personal Account) Project
echo -e "\n\${YELLOW}🔑 [STEP 1/3] Fetching Personal Credit-Consumer

Project Details...\${NC}"
read -p "Enter your PERSONAL GCP Project ID (where the \\$1k credits
live): " PERSONAL_PROJECT_ID


# Verify active project setup
echo -e "Checking configuration status for project:
\${CYAN}\$PERSONAL_PROJECT_ID\${NC}..."
if ! gcloud config set project "\$PERSONAL_PROJECT_ID" &> /dev/null; then

    echo -e "\${RED}❌ ERROR: Project ID invalid or not authenticated via
gcloud CLI.\${NC}"
    echo -e "👉 Please run 'gcloud auth login' and try again."
    exit 1
fi


# Extract the literal Project Number
PROJECT_NUMBER=\$(gcloud projects list --
filter="projectId=\$PERSONAL_PROJECT_ID" --format="value(projectNumber)")

if [ -z "\$PROJECT_NUMBER" ]; then
    echo -e "\${RED}❌ ERROR: Failed to retrieve project number for


\$PERSONAL_PROJECT_ID.\${NC}"
    exit 1
fi


SERVICE_ACCOUNT="service-\${PROJECT_NUMBER}@gcp-sa-
discoveryengine.iam.gserviceaccount.com"
echo -e "\${GREEN}✅ Success: Personal Project Number verified:

\$PROJECT_NUMBER\${NC}"
echo -e "Your Personal Vertex AI Service Account is:
\${CYAN}\$SERVICE_ACCOUNT\${NC}"


# Step 2: Configure Business/Contractor Bucket Access
echo -e "\n\${YELLOW}📁 [STEP 2/3] Configuring Read-Only Access on
Business Resource Bucket...\${NC}"
read -p "Enter the secure GCS Bucket Name (e.g. business-secure-vault-

bucket): " BUCKET_NAME
# Trim gs:// prefix if entered by the user
BUCKET_NAME=\${BUCKET_NAME#gs://}

echo -e "\nTo establish the secure access bridge, choose an execution

strategy:"
echo -e "1) \${CYAN}Execute Now:\${NC} Run the IAM update directly
(Requires being currently logged into gcloud with Business admin
credentials)."

echo -e "2) \${CYAN}Generate Handoff Block:\${NC} Output a pre-formatted
CLI code block you can copy and email to your business admin /
contractor."
read -p "Select option [1 or 2]: " EXEC_MODE


if [ "\$EXEC_MODE" == "1" ]; then
    echo -e "\nApplying policy binding on GCS target bucket:
\${YELLOW}gs://\$BUCKET_NAME\${NC}..."

    if gcloud storage buckets add-iam-policy-binding "gs://\$BUCKET_NAME"
\
        --member="serviceAccount:\$SERVICE_ACCOUNT" \
        --role="roles/storage.objectViewer" &> /dev/null; then
        echo -e "\${GREEN}🎉 SUCCESS: Secure cross-account permission

bridge established successfully!\${NC}"
    else
        echo -e "\${RED}❌ ACCESS DENIED: Failed to modify bucket
permissions.\${NC}"

        echo -e "👉 You may need to use Option 2 and have the Business
Administrator run the command."


    fi
else
    echo -e "\n\${CYAN}---------------------------------------------------

-----------------------------"
    echo -e "📋 BUSINESS ADMIN CODES (EMAIL TO CONTRACTOR OR RUN ON
WORKSPACE CONSOLE)"
    echo -e "-------------------------------------------------------------

-------------------\${NC}"
    echo -e "Copy and execute this exact command block to grant read-only
RAG access:"
    echo -e "\n\${YELLOW}gcloud storage buckets add-iam-policy-binding

gs://\${BUCKET_NAME} \\"
    echo -e "  --member=\"serviceAccount:\${SERVICE_ACCOUNT}\" \\"
    echo -e "  --role=\"roles/storage.objectViewer\"\${NC}"
    echo -e "\n\${CYAN}Alternative Legacy Utility Command:\${NC}"

    echo -e "\${YELLOW}gsutil iam ch
serviceAccount:\${SERVICE_ACCOUNT}:objectViewer
gs://\${BUCKET_NAME}\${NC}"
    echo -e "\${CYAN}-----------------------------------------------------
---------------------------\${NC}"

fi

# Step 3: Guidelines for finalization
echo -e "\n\${YELLOW}⚡ [STEP 3/3] Finalizing Data Store

Creation...\${NC}"
echo -e "1. Go to your \${CYAN}Personal Vertex AI Agent Builder\${NC}
console."
echo -e "2. Create a new \${CYAN}Data Store\${NC} using \${YELLOW}Cloud

Storage\${NC}."
echo -e "3. Point the connection directly to:
\${GREEN}gs://\$BUCKET_NAME/\${NC}"
echo -e "4. Your Vertex AI system is now fully authorized to crawl, parse,

and index your business's files!"
echo -e
"\${CYAN}=================================================================
===============\${NC}"
