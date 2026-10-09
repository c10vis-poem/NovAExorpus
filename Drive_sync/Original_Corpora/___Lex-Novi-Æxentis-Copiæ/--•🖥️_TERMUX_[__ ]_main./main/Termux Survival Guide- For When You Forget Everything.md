# Termux Survival Guide: For When You Forget Everything

## 1. What is "Base Camp" and where am I?

- When Termux opens, you see `~ $`. The `~` is "Home" base.
- Lost or "file not found" errors: type `cd ~` to teleport back to the start.

## 2. How to talk to your files (Storage)

Termux starts in a locked box. To see actual Android files (Downloads, Photos), unlock it once:

1. Type: `termux-setup-storage`
2. Press Enter.
3. A popup asks for permission — tap Allow.
4. Get to downloads with: `cd ~/storage/downloads`

## 3. The "Copy & Paste" Safety Drill

1. Highlight & copy any code from your notes app.
2. Go to Termux, long-press on the black screen.
3. Tap Paste.
4. Important: press Enter to actually run the command.

## 4. What if "Nothing Happens"?

If you paste a command, hit Enter, and the terminal just shows a new blank line with a `$` — it worked. "No news is good news": the computer did exactly what you asked without complaining.

## 5. Essential Commands to Remember

- `ls` — lists files in the current folder ("show me what's in here").
- `pwd` — tells you exactly where you are standing (the full file path).
- `source ~/.bashrc` — the "refresh" button; if pasted keys/settings don't seem to work, run this to force the computer to wake up and use the new settings.

## 6. Where to find your keys & setup

Check other saved notes: "Termux Master Launcher & Setup Prompter" (heavy lifting), "Adding API Keys to Termux Environment" (connecting to Google).

## Termux Master Launcher & Setup Prompter

### 1. Safe Initialization (Run First When Lost)

If commands are failing or files aren't found:

```bash
cd ~ && pwd && ls
```

Expected safe output: `/data/data/com.termux/files/home`

### 2. Environment Refresh & Activation

After pasting any keys or hooks into the profile, force Termux to lock them in immediately without restarting the app:

```bash
source ~/.bashrc
```

### 3. Core Setup Verification Checks

Verify master keys and agents are properly attached to the background environment:

```bash
echo $GOOGLE_CLOUD_PROJECT
# Expected: main-catwalk-492516

echo $GOOGLE_APPLICATION_CREDENTIALS
# Expected: /data/data/com.termux/files/home/vertex-key.json
```

### 4. Copy / Paste Safety Drill

1. Highlight & copy the text block from the notes app.
2. Go to Termux, long-press anywhere on the black terminal screen.
3. Select Paste from the popup menu.
4. If a command runs silently and shows a new blank line with a `$`, it succeeded — do not expect a confirmation message.

## Recommended Termux AI Agents and CLIs

1. **Open Interpreter** — translates plain English instructions into actual terminal commands executed locally. Ideal for file system management and automation. Install: `pip install open-interpreter`. Launch: `interpreter`.
2. **Aider** — autonomous terminal-based pair programmer that directly edits local code files and handles git commits automatically. Install: `pip install aider-chat`. Run `aider` inside any coding project folder to co-author scripts.
3. **Fabric** — command-line prompting platform for advanced text extraction, video summarizing, and heavy structural text formatting. Usage example: `cat article.txt | fabric --pattern extract_wisdom`.

## Termux Web Scraping and Markdown Merging

### 1. Core Jina Scraping Command

Pull any web article into Termux as clean text without website layout junk:

```bash
curl [jina-reader-url] > article.md
```

### 2. Merging Multiple Markdown Files

Combine an entire folder of individual articles/notes into a single mega-document (e.g. for NotebookLM source limits):

```bash
cat *.md > Project_Master.md
```

### 3. Automated Web Reader Hook (`vagent_read`)

Add to the environment to pass a URL straight to the AI voice agent:

```bash
echo 'vagent_read() {
  URL=$1
  echo "Reading article..."
  CONTENT=$(curl -s "$URL")
  echo "$CONTENT" | claude -p "Analyze this article content and give me the best outside-the-box engineering ideas" | tee /dev/tty | termux-tts-speak
}' >> ~/.bashrc
source ~/.bashrc
```

Trigger with the keyboard microphone and say: `vagent_read [url]`.
