---
title: "Master Menu Script_"
source: "Drive_sync/Original_Corpora/__NovÆxorpus(NÆX)/3-FILES-MGMT16-SCRIPTS-(16-files)/Master Menu Script_.pdf"
cleaned: 2026-10-08
converter: "pymupdf get_text via tools/clean.py normalize_markdown"
tags:
  - pdf-conversion
---

A master wrapper script is a simple control panel for your phone’s terminal.
Instead of remembering and typing multiple commands like python log_builder.py,
./sync_and_grep.sh, or rclone sync, you just run one single file. It opens a text-based menu on
your screen where you type a number (1, 2, 3, or 4) to instantly launch whichever task you
need.
Here is the exact code to create this master control panel directly on your phone.
Step 1: Create the Master Menu Script
Open your mobile terminal and run this exact block to build the script:

cat << 'EOF' > agent_panel.sh​
#!/bin/bash​
​
while true; do​
    clear​
    echo "========================================="​
    echo "   📱 MOBILE AGENT WORKSPACE MANAGER    "​
    echo "========================================="​
    echo "1) 🔄 Sync Files From Google Drive"​
    echo "2) 📝 Create New JSONL Log Entry"​
    echo "3) 🔍 Grip/Grep Workspace Files"​
    echo "4) 🚪 Exit"​
    echo "========================================="​
    read -p "Choose an option [1-4]: " choice​
​
    case $choice in​
        1)​
            echo ""​
            echo "🔄 Pulling latest .md, .jsonl, and skills.md
files..."​
            rclone sync gdrive:Your_GDrive_Folder_Name
~/AgentWorkspace​
            read -p "Press Enter to continue..." temp​
            ;;​
        2)​
            echo ""​
            python log_builder.py​
            read -p "Press Enter to continue..." temp​
            ;;​
        3)​
            echo ""​


            read -p "🔍 What keyword do you want to grip? " keyword​
            echo "-----------------------------------------"​
            grep -rn "$keyword" ~/AgentWorkspace/​
            echo "-----------------------------------------"​
            read -p "Press Enter to continue..." temp​
            ;;​
        4)​
            echo "Goodbye!"​
            exit 0​
            ;;​
        *)​
            echo "Invalid option. Please pick 1-4."​
            sleep 2​
            ;;​
    esac​
done​
EOF​
​
chmod +x agent_panel.sh​

Step 2: How to Run It on Your Phone
Anytime you open your mobile terminal app, you now just type this single command:

./agent_panel.sh​

What Happens Next
Your screen will turn into a clean, simple menu.
●​ Pressing 1 completely automates downloading your updated Google Drive documents.
●​ Pressing 2 jumps straight into your text prompts to log field notes.
●​ Pressing 3 runs your search engine across your entire folder layout using the rules
defined in your skills.md.
Do you want to add an option to this menu that pushes your newly created logs back up to
Google Drive, or are you ready to test out the menu as it is?
