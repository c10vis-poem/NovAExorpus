**Termux Survival Guide: For When You Forget Everything**

# Termux Survival Guide: For When You Forget Everything

1\. What is "Base Camp" and where am I?

• When you open Termux, you see \`~ \$\`.

• The \`~\` is your "Home" base.

• If you ever feel lost or get "file not found" errors, just type: \`cd
~\` (This teleports you back to the start).

2\. How to talk to your files (Storage)

Termux starts in a locked box. To see your actual Android files
(Downloads, Photos), you must unlock it once:

1\. Type: \`termux-setup-storage\`

2\. Press Enter.

3\. A popup will ask for permission—**tap Allow.**

4\. Now you can get to your downloads by typing: \`cd
~/storage/downloads\`

3\. The "Copy & Paste" Safety Drill

1\. **Highlight & Copy** any code from your Keep notes.

2\. Go to Termux and **long-press** on the black screen.

3\. Tap **Paste**.

4\. **Important:** Press the **Enter** key on your keyboard to actually
run the command.

4\. What if "Nothing Happens"?

If you paste a command, hit Enter, and the terminal just shows a new
blank line with a \`\$\`—**it worked!**

• In terminal-speak, "no news is good news." The computer did exactly
what you asked without complaining.

5\. Essential Commands to Remember

• \`ls\` : Lists the files in your current folder (like "Show me what's
in here").

• \`pwd\` : Tells you exactly where you are standing (the full file
path).

• \`source ~/.bashrc\` : The "Refresh" button. If you ever paste keys or
settings and they don't seem to work, run this to force the computer to
"wake up" and use the new settings.

6\. Where to find your keys & setup

Always check your other Keep notes:

• **"Termux Master Launcher & Setup Prompter"** (for the heavy lifting).

• **"Adding API Keys to Termux Environment"** (for connecting to
Google).

**Termux Master Launcher & Setup Prompter**

# Termux Master Launcher & Setup Prompter

## 1. Safe Initialization (Run First When Lost)

If commands are failing or files aren't found, copy-paste this line to
reset back to base camp, verify your path, and see your files:

\`\`\`

cd ~ && pwd && ls

\`\`\`

*Expected safe output:* \`/data/data/com.termux/files/home\`

## 2. Environment Refresh & Activation

After pasting any keys or hooks into your profile, run this to force
Termux to lock them in immediately without restarting the app:

\`\`\`

source ~/.bashrc

\`\`\`

## 3. Core Setup Verification Checks

Run these commands to verify that your master keys and agents are
properly attached to the background environment:

• Check Google Cloud Project ID:

\`\`\`

echo \$GOOGLE_CLOUD_PROJECT

\`\`\`

*Expected:* \`main-catwalk-492516\`

• Check Passkey JSON Path:

\`\`\`

echo \$GOOGLE_APPLICATION_CREDENTIALS

\`\`\`

*Expected:* \`/data/data/com.termux/files/home/vertex-key.json\`

## 4. Copy / Paste Safety Drill

1\. **Highlight & Copy** the text block from Google Keep.

2\. Go to Termux, **long-press** anywhere on the black terminal screen.

3\. Select **Paste** from the popup menu.

4\. If a command runs silently and shows a new blank line with a \`\$\`,
**it succeeded.** Do not expect a confirmation message.

**Recommended Termux AI Agents and CLIs**

## Recommended Termux AI Agents and CLIs

## 1. Open Interpreter

Translates plain English instructions into actual terminal commands
executed locally on your system. Ideal for file system management and
automation. Installation Command: pip install open-interpreter Usage:
Type **interpreter** to launch the environment.

## 2. Aider

An autonomous terminal-based pair programmer that directly edits local
code files and automatically handles git commits. Installation Command:
pip install aider-chat Usage: Run **aider** inside any coding project
folder to begin co-authoring scripts.

## 3. Fabric

A command-line prompting platform optimized for advanced text
extraction, video summarizing, and heavy structural text formatting.
Installation: Follow the official setup guide via pip or go. Usage
Example: cat article.txt \| fabric --pattern extract_wisdom

**Termux Web Scraping and Markdown Merging**

## Termux Web Scraping and Markdown Merging

## 1. Core Jina Scraping Command

To pull any web article into Termux as clean text without website layout
junk: curl \[suspicious link removed\] \>
[<u>article.md</u>](http://article.md)

## 2. Merging Multiple Markdown Files

To combine an entire folder of individual articles or notes into a
single mega-document for NotebookLM source limits: cat \*.md \>
Project_Master.md

## 3. Automated Web Reader Hook (vagent_read)

Add this to your environment to pass a URL straight to your AI voice
agent: echo 'vagent_read() { URL=\$1 echo "Reading article..."
CONTENT=\$(curl -s "\[suspicious link removed\]") echo "\$CONTENT" \|
claude -p "Analyze this article content and give me the best
outside-the-box engineering ideas" \| tee /dev/tty \| termux-tts-speak
}' \>\> ~/.bashrc source ~/.bashrc

## How to Use the Automated Script

Just trigger your keyboard microphone and say: vagent_read \[suspicious
link removed\]

**Android Native Voice Agent Stack**

# Android Native Voice Agent Stack

1\. The Core Environment Exports

Run these commands to permanently inject your Vertex JSON key and Google
Cloud settings into the background of Termux:

\`\`\`

echo 'export GOOGLE_CLOUD_PROJECT="main-catwalk-492516"' \>\> ~/.bashrc

echo 'export
GOOGLE_APPLICATION_CREDENTIALS="/data/data/com.termux/files/home/vertex-key.json"'
\>\> ~/.bashrc

source ~/.bashrc

\`\`\`

2\. High-Quality, Lowest-Latency TTS Setup

Instead of cloud APIs, turn Sherpa-ONNX into your system-wide voice
engine:

• Install the pre-compiled **Sherpa-ONNX Android APK** (which includes
optimized offline VITS/Piper neural models).

• Open your tablet's global settings: **Settings \> Accessibility \>
Text-to-Speech**.

• Change the **Preferred Engine** from Google to **Sherpa-ONNX**.

• Open Termux and install the Termux API toolset to bridge the audio:

\`\`\`

pkg install termux-api -y

\`\`\`

3\. Creating the Voice Agent (\`vagent\`) Terminal Hook

Run this block to create a permanent command that runs your AI, displays
the text, and instantly speaks it out loud using your hardware's offline
speech engine:

\`\`\`

echo 'vagent() {

    claude "\$@" \| tee /dev/tty \| termux-tts-speak

}' \>\> ~/.bashrc

source ~/.bashrc

\`\`\`

4\. Direct Voice Input Configuration

• Set **FUTO Voice Input** as your active system keyboard.

• Open Termux, type \`vagent\`, tap the microphone icon on the FUTO
keyboard, and speak your command natively without any background
recording scripts.

**Post RazrPi agent build\> Tasks Management, Projects Architecture**

[<u>https://docs.google.com/document/d/1ugle-WYKmLJcI2B9I4qEEp8UxbMiuDssusybhflnr4E/edit?usp=drivesdk</u>](https://docs.google.com/document/d/1ugle-WYKmLJcI2B9I4qEEp8UxbMiuDssusybhflnr4E/edit?usp=drivesdk)

**RazrPi Build docs**

[<u>https://claude.ai/share/5a55524b-2032-4a16-a2f2-5253a7eeab9a</u>](https://claude.ai/share/5a55524b-2032-4a16-a2f2-5253a7eeab9a)
