#!/usr/bin/env bash
# ==========================================================================
# AESOP XI: CROSS-ACCOUNT RESOURCE INGESTION & CREDIT HARNESS
# Script ID: AX-GCP-CROSS-ACCOUNT-HANDSHAKE-BOOTSTRAP
# ==========================================================================
set -euo pipefail

# Style definitions for clean terminal telemetry output
RED='\033[0;31m'
GREEN='\033[0;32m'
CYAN='\033[0;36m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

clear
echo -e "${CYAN}=================================================================================${NC}"
echo -e "🌌 [GCP CROSS-ACCOUNT HANDSHAKE] Initializing Sovereign Connection Pipeline..."
echo -e "=================================================================================${NC}"

# Ensure gcloud CLI is installed
if ! command -v gcloud &> /dev/null; then
    echo -e "${RED}❌ ERROR: Google Cloud SDK (gcloud) is not installed in this shell.${NC}"
    echo -e "👉 Install it via: pkg install google-cloud-sdk (or follow your OS guide)."
    exit 1
fi

# Step 1: Identify Consumer (Personal Account) Project
echo -e "\n${YELLOW}🔑 [STEP 1/3] Fetching Personal Credit-Consumer Project Details...${NC}"
read -p "Enter your PERSONAL GCP Project ID (where the \$1k credits live): " PERSONAL_PROJECT_ID

# Verify active project setup
echo -e "Checking configuration status for project: ${CYAN}$PERSONAL_PROJECT_ID${NC}..."
if ! gcloud config set project "$PERSONAL_PROJECT_ID" &> /dev/null; then
    echo -e "${RED}❌ ERROR: Project ID invalid or not authenticated via gcloud CLI.${NC}"
    echo -e "👉 Please run 'gcloud auth login' and try again."
    exit 1
fi

# Extract the literal Project Number
PROJECT_NUMBER=$(gcloud projects list --filter="projectId=$PERSONAL_PROJECT_ID" --format="value(projectNumber)")
if [ -z "$PROJECT_NUMBER" ]; then
    echo -e "${RED}❌ ERROR: Failed to retrieve project number for $PERSONAL_PROJECT_ID.${NC}"
    exit 1
fi

SERVICE_ACCOUNT="service-${PROJECT_NUMBER}@gcp-sa-discoveryengine.iam.gserviceaccount.com"
echo -e "${GREEN}✅ Success: Personal Project Number verified: $PROJECT_NUMBER${NC}"
echo -e "Your Personal Vertex AI Service Account is: ${CYAN}$SERVICE_ACCOUNT${NC}"

# Step 2: Configure Business/Contractor Bucket Access
echo -e "\n${YELLOW}📁 [STEP 2/3] Configuring Read-Only Access on Business Resource Bucket...${NC}"
read -p "Enter the secure GCS Bucket Name (e.g. business-secure-vault-bucket): " BUCKET_NAME
# Trim gs:// prefix if entered by the user
BUCKET_NAME=${BUCKET_NAME#gs://}

echo -e "\nTo establish the secure access bridge, choose an execution strategy:"
echo -e "1) ${CYAN}Execute Now:${NC} Run the IAM update directly (Requires being currently logged into gcloud with Business admin credentials)."
echo -e "2) ${CYAN}Generate Handoff Block:${NC} Output a pre-formatted CLI code block you can copy and email to your business admin / contractor."
read -p "Select option [1 or 2]: " EXEC_MODE

if [ "$EXEC_MODE" == "1" ]; then
    echo -e "\nApplying policy binding on GCS target bucket: ${YELLOW}gs://$BUCKET_NAME${NC}..."
    if gcloud storage buckets add-iam-policy-binding "gs://$BUCKET_NAME" \
        --member="serviceAccount:$SERVICE_ACCOUNT" \
        --role="roles/storage.objectViewer" &> /dev/null; then
        echo -e "${GREEN}🎉 SUCCESS: Secure cross-account permission bridge established successfully!${NC}"
    else
        echo -e "${RED}❌ ACCESS DENIED: Failed to modify bucket permissions.${NC}"
        echo -e "👉 You may need to use Option 2 and have the Business Administrator run the command."
    fi
else
    echo -e "\n${CYAN}---------------------------------------------------------------------------------${NC}"
    echo -e "📋 BUSINESS ADMIN CODES (EMAIL TO CONTRACTOR OR RUN ON WORKSPACE CONSOLE)"
    echo -e "${CYAN}---------------------------------------------------------------------------------${NC}"
    echo -e "Copy and execute this exact command block to grant read-only RAG access:"
    echo -e "\n${YELLOW}gcloud storage buckets add-iam-policy-binding gs://${BUCKET_NAME} \\"
    echo -e "    --member=\"serviceAccount:${SERVICE_ACCOUNT}\" \\"
    echo -e "    --role=\"roles/storage.objectViewer\"${NC}"
    echo -e "\n${CYAN}Alternative Legacy Utility Command:${NC}"
    echo -e "${YELLOW}gsutil iam ch serviceAccount:${SERVICE_ACCOUNT}:objectViewer gs://${BUCKET_NAME}${NC}"
    echo -e "${CYAN}---------------------------------------------------------------------------------${NC}"
fi

# Step 3: Guidelines for finalization
echo -e "\n${YELLOW}⚡ [STEP 3/3] Finalizing Data Store Creation...${NC}"
echo -e "1. Go to your ${CYAN}Personal Vertex AI Agent Builder${NC} console."
echo -e "2. Create a new ${CYAN}Data Store${NC} using ${YELLOW}Cloud Storage${NC}."
echo -e "3. Point the connection directly to: ${GREEN}gs://$BUCKET_NAME/${NC}"
echo -e "4. Your Vertex AI system is now fully authorized to crawl, parse, and index your business's files!"
echo -e "${CYAN}=================================================================================${NC}"
