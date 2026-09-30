# Unsloth Studio Installation - Unsloth Documentation

1
New
🦥Introducing Unsloth Studio
Unsloth Studio Installation
Learn how to install Unsloth Studio on your local device.
Unsloth Studio works on Windows, Linux, WSL and MacOS. You
should use the same installation process on every device, although
the system requirements may differ by device.
Windows
MacOS
Linux & WSL
Docker
Developer Install
• Mac: Like CPU - Chat + Data Recipes works for now. MLX
training now works!
• CPU: Unsloth still works without a GPU, but for Chat + Data
Recipes.
• Training: Works on NVIDIA, Intel, AMD GPUs and Mac devices
Copy
This site uses cookies to deliver its
service and to analyze traffic. By browsing
this site, you accept the privacy policy.
Accept
Reject


2
Launch the terminal from Mac, then install Unsloth by entering
the command below.
Unsloth will start setting up the environment and installing the
required packages as shown below. Type Y and Press Enter
when asked if you want to allow Unsloth to start now. This will
start Unsloth on your local 8888 port.
If you chose not to start Unsloth during the installation process,
you can always start the Unsloth app using unsloth studio -p 8888
. If you would like to have your Unsloth instance accessible by
clients outside of your PC/computer, add -H 0.0.0.0 to the 
unsloth studio command.
Quickstart
MacOS
Windows
Linux, WSL
Step 1: Setup Unsloth
curl -fsSL https://unsloth.ai/install.sh | sh
This site uses cookies to deliver its
service and to analyze traffic. By browsing
this site, you accept the privacy policy.


3
Open your browser of choice and go to the http://127.0.0.1:8888
URL. If this is your first time installing Unsloth, you will be
prompted to create a new password. After, the Unsloth app
should now open on the Chat Page as shown below.
Launch Unsloth securely with HTTPS and Cloudflare. Unsloth
now provides a secure way to launch Unsloth over HTTPS
through a free Cloudflare tunnel. Use the below (works in
Windows, Mac & Linux):
You can start training and running models immediately. You can
view our more detailed step-by-step guide to get started below:
Get Started
To update Unsloth Studio use the same commands as install:
macOS, WSL, Linux:
Step 2: Start Unsloth
unsloth studio --secure
Update Unsloth Studio
This site uses cookies to deliver its
service and to analyze traffic. By browsing
this site, you accept the privacy policy.


4
Windows (PowerShell):
Unsloth Studio works directly on Windows without WSL. To train
models, make sure your system satisfies these requirements:
Requirements
• Windows 10 or Windows 11 (64-bit)
• NVIDIA GPU with drivers installed
• App Installer (includes winget ): here
• Git: winget install --id Git.Git -e --source winget
• Python: version 3.11 up to, but not including, 3.14
• Work inside a Python environment such as uv, venv, or 
conda/mamba
Unsloth Studio works on Mac devices for Chat and training and all
features. You can run MLX models with Unsloth.
• macOS 12 Monterey or newer (Intel or Apple Silicon)
curl -fsSL https://unsloth.ai/install.sh | sh
irm https://unsloth.ai/install.ps1 | iex
System Requirements
 Windows
 MacOS
This site uses cookies to deliver its
service and to analyze traffic. By browsing
this site, you accept the privacy policy.


5
• Work inside a Python environment such as uv, venv, or 
conda/mamba
• Ubuntu 20.04+ or similar distro (64-bit)
• NVIDIA GPU with drivers installed
• CUDA toolkit (12.4+ recommended, 12.8+ for blackwell)
• Git: sudo apt install git
• Python: version 3.11 up to, but not including, 3.14
• Work inside a Python environment such as uv, venv, or 
conda/mamba
Our Docker image now works for Unsloth! We're working on Mac
compatibility.
• Pull our latest Unsloth container image: docker pull
unsloth/unsloth
• Run the container via:
For more information, see here .
 Linux & WSL
 Docker
docker run -d -e JUPYTER_PASSWORD="mypassword" \
-p 8888:8888 -p 8000:8000 -p 2222:22 \
-v $(pwd)/work:/workspace/work \
--gpus all \
unsloth/unsloth
This site uses cookies to deliver its
service and to analyze traffic. By browsing
this site, you accept the privacy policy.


6
• Access your studio instance at http://localhost:8000 or external
ip address http://external_ip_address:8000/
Unsloth Studio supports CPU devices for Chat for GGUF models
and Data Recipes (Export coming very soon)
• Same as the ones mentioned above for Linux (except for
NVIDIA GPU drivers) and MacOS.
To install into an isolated location (its own virtual env, auth/ , 
studio.db , cache and llama.cpp build), set UNSLOTH_STUDIO_HOME
and pass it again at launch:
 CPU only
Developer / Nightly Installations
(Advanced)
Main Repo Install
macOS, Linux, WSL developer installs:
git clone https://github.com/unslothai/unsloth
cd unsloth
./install.sh --local
unsloth studio -p 8888
UNSLOTH_STUDIO_HOME="$PWD/.studio" ./install.sh --local
UNSLOTH_STUDIO_HOME="$PWD/.studio" unsloth studio -p 8888
This site uses cookies to deliver its
service and to analyze traffic. By browsing
this site, you accept the privacy policy.


7
Then to update :
To install into an isolated location (its own virtual env, auth/ , 
studio.db , cache and llama.cpp build), set UNSLOTH_STUDIO_HOME
and pass it again at launch:
Then to update :
By default unsloth studio binds to 127.0.0.1 (this machine only). To
reach it from another device, pick one of:
cd unsloth && git pull
./install.sh --local
unsloth studio -p 8888
Windows PowerShell developer installs:
git clone https://github.com/unslothai/unsloth.git
cd unsloth
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\install.ps1 --local
unsloth studio -p 8888
$env:UNSLOTH_STUDIO_HOME="$PWD\.studio"; .\install.ps1 --local
$env:UNSLOTH_STUDIO_HOME="$PWD\.studio"; unsloth studio -p 8888
cd unsloth; git pull
.\install.ps1 --local
unsloth studio -p 8888
Remote access: --secure (HTTPS tunnel) vs raw
port
This site uses cookies to deliver its
service and to analyze traffic. By browsing
this site, you accept the privacy policy.


8
•
--secure (recommended): serve only through a free Cloudflare
HTTPS link. Unsloth stays bound to localhost and the tunnel
provides the public URL; it fails closed (does not start) if the
tunnel can't come up, so the raw port is never exposed.
•
-H 0.0.0.0 : bind the raw port on all network interfaces, reachable
from anywhere on the network. Only use this on a trusted
network.
Server-side tools (web search, Python and terminal code execution)
run as your user and are on by default. Anyone who can reach the
server with the API key can run code on this machine, so keep your
API key private and pass --disable-tools when exposing Unsloth.
Installer options can be passed as environment variables. On
macOS, Linux and WSL place the variable after the pipe so the shell
passes it to sh ; on Windows set it with $env: before piping to iex .
Skip PyTorch (GGUF-only mode):
Pin the Python version:
unsloth studio --secure -p 8888
unsloth studio -H 0.0.0.0 -p 8888
Advanced Launch methods
curl -fsSL https://unsloth.ai/install.sh | UNSLOTH_NO_TORCH=1 sh
$env:UNSLOTH_NO_TORCH=1; irm https://unsloth.ai/install.ps1 | iex
This site uses cookies to deliver its
service and to analyze traffic. By browsing
this site, you accept the privacy policy.


9
Install to a custom location with UNSLOTH_STUDIO_HOME :
Cap Unsloth's native CPU thread pools on high-core hosts: 
UNSLOTH_CPU_THREADS=8 unsloth studio -p 8888 .
The recommended way to fully remove Unsloth Studio is the
matching uninstall script for your OS. It stops any running servers,
removes the install dir, the launcher data dir, the desktop shortcut,
and any platform-specific entries (macOS .app bundle + Launch
Services on Mac; Start Menu, HKCU\Software\Unsloth registry key
and user PATH entries on Windows):
•
MacOS, WSL, Linux:
•
Windows (PowerShell):
curl -fsSL https://unsloth.ai/install.sh | UNSLOTH_PYTHON=3.12 sh
$env:UNSLOTH_PYTHON='3.12'; irm https://unsloth.ai/install.ps1 | iex
curl -fsSL https://unsloth.ai/install.sh |
UNSLOTH_STUDIO_HOME=/abs/path sh
$env:UNSLOTH_STUDIO_HOME='C:\path'; irm
https://unsloth.ai/install.ps1 | iex
Uninstall
curl -fsSL
https://raw.githubusercontent.com/unslothai/unsloth/main/scripts/unin
stall.sh | sh
This site uses cookies to deliver its
service and to analyze traffic. By browsing
this site, you accept the privacy policy.


10
If you only want to drop the install dir and keep the
launcher/shortcut for a later reinstall, you can instead run rm -rf
~/.unsloth/studio (Mac/Linux/WSL) or Remove-Item -Recurse -Force
"$HOME\.unsloth\studio" (Windows). The model cache at 
~/.cache/huggingface is not touched by any of these.
If you prefer to remove only specific parts:
1. Remove app only (keeps history, chats, checkpoints, and exports
intact):
• macOS, WSL, Linux: rm -rf ~/.unsloth/studio/unsloth_studio
• Windows (PowerShell): Remove-Item -Recurse -Force
"$HOME\.unsloth\studio\unsloth_studio"
2. Remove Unsloth entirely (keeps other Unsloth tools intact):
• macOS, WSL, Linux: rm -rf ~/.unsloth/studio
• Windows (PowerShell): Remove-Item -Recurse -Force
"$HOME\.unsloth\studio"
3. Remove everything Unsloth-related:
• macOS, WSL, Linux: rm -rf ~/.unsloth
• Windows (PowerShell): Remove-Item -Recurse -Force
"$HOME\.unsloth"
irm
https://raw.githubusercontent.com/unslothai/unsloth/main/scripts/unin
stall.ps1 | iex
Manual uninstall
This site uses cookies to deliver its
service and to analyze traffic. By browsing
this site, you accept the privacy policy.


11
Note: Step 3 deletes everything in history, chats, model checkpoints,
and exports. This cannot be undone.
4. Remove shortcuts and symlinks:
macOS:
Linux:
WSL / Windows (PowerShell):
5. Remove the CLI command:
• macOS, Linux, WSL: rm -f ~/.local/bin/unsloth
• Windows (PowerShell): The installer added the venv's Scripts
directory to your User PATH. To remove it, open Settings →
System → About → Advanced system settings → Environment
Variables, find Path under User variables, and remove the entry
pointing to .unsloth\studio\...\Scripts .
Note: Steps 1-5 dont touch your downloaded HF model files. See
Deleting cached HF model files below if you want to reclaim that
space.
rm -rf ~/Applications/Unsloth\ Studio.app ~/Desktop/Unsloth\ Studio
rm -f ~/.local/share/applications/unsloth-studio.desktop
~/Desktop/unsloth-studio.desktop
Remove-Item -Force "$HOME\Desktop\Unsloth Studio.lnk"
Remove-Item -Force "$env:APPDATA\Microsoft\Windows\Start
Menu\Programs\Unsloth Studio.lnk"
This site uses cookies to deliver its
service and to analyze traffic. By browsing
this site, you accept the privacy policy.


12
You can delete old model files either from the bin icon in model
search or by removing the relevant cached model folder from the
default Hugging Face cache directory. By default, Hugging Face
uses ~/.cache/huggingface/hub/ on macOS/Linux/WSL and 
C:\Users\<username>\.cache\huggingface\hub\ on Windows.
• MacOS, Linux, WSL: ~/.cache/huggingface/hub/
• Windows: %USERPROFILE%\.cache\huggingface\hub\
If HF_HUB_CACHE or HF_HOME is set, use that location instead. On
Linux and WSL, XDG_CACHE_HOME can also change the default
cache root.
Apr 1 update: You can now
select an existing folder for
Unsloth to detect from.
Mar 27 update: Unsloth Studio
now automatically detects
older / pre-existing models 
downloaded from Hugging
Face, LM Studio etc.
Deleting cached HF model files
Using old / existing GGUF models
This site uses cookies to deliver its
service and to analyze traffic. By browsing
this site, you accept the privacy policy.


13
Manual instructions: Unsloth Studio detects models downloaded to
your Hugging Face Hub cache 
(C:\Users{your_username}.cache\huggingface\hub) . If you have GGUF
models downloaded through LM Studio, note that these are stored
in C:\Users{your_username}.cache\lm-studio\models OR
C:\Users{your_username}\lm-studio\models . Sometimes when they
are not visible, you will need to move or copy those .gguf files into
your Hugging Face Hub cache directory (or another path accessible
to llama.cpp) for Unsloth Studio to load them.
After fine-tuning a model or adapter in Unsloth, you can export it to
GGUF and run local inference with llama.cpp directly in Unsloth
Chat. Unsloth Studio is powered by llama.cpp and Hugging Face.
We’ve created a free Google Colab notebook so you can explore
all of Unsloth’s features on Colab’s T4 GPUs. You can train and run
most models up to 22B parameters, and switch to a larger GPU for
bigger models. Just Click 'Run all' and the UI should pop up after
installation.
 Google Colab notebook
This site uses cookies to deliver its
service and to analyze traffic. By browsing
this site, you accept the privacy policy.


14
Once installation is complete,
scroll to Start Unsloth Studio
and click Open Unsloth Studio
in the white box shown on the
left:
Scroll further down, to see the
actual UI.
Sometimes the Unsloth link may return an error. This happens
because you might have disabled cookies or you're using an
adblocker or Mozilla. You can still access the UI by scrolling below
the button.
Google Colab also expects you to stay on the Colab page; if it
detects inactivity, it may shut down the GPU session.
Google Colab
colab.research.goo
gle.com
This site uses cookies to deliver its
service and to analyze traffic. By browsing
this site, you accept the privacy policy.


15
Previous
Studio Chat
Next
Data Recipes
Last updated 5 days ago
Was this helpful?
Troubleshooting
Search
Problem
Fix
Python version error
sudo apt install python3.12 python3.12-venv
version 3.11 up to, but not including, 3.14
nvidia-smi not found
Install NVIDIA drivers from
https://www.nvidia.com/Download/index.as
px
nvcc not found (CUDA)
sudo apt install nvidia-cuda-toolkit or add 
/usr/local/cuda/bin to PATH
llama-server build failed
Non-fatal, Unsloth still works, GGUF
inference won't be available. Install cmake
and re-run setup to fix.
cmake not found
sudo apt install cmake
git not found
sudo apt install git
Build failed
Delete ~/.unsloth/llama.cpp and re-run setup
This site uses cookies to deliver its
service and to analyze traffic. By browsing
this site, you accept the privacy policy.


16
Community
Reddit r/unsloth
Twitter (X)
LinkedIn
Resources
Tutorials
Docker
Hugging Face
Company
Unsloth Studio
Contact
Events
© Unsloth, 2026
This site uses cookies to deliver its
service and to analyze traffic. By browsing
this site, you accept the privacy policy.
