---
title: "TERMUX-APP-STORE"
source: "Drive_sync/Original_Corpora/___Lex-Novi-Æxentis-Copiæ (1)/--•🖥️_TERMUX_[__ ]_main./•🛠️-Assets-🧰_termux./TERMUX-APP-STORE.pdf"
cleaned: 2026-10-08
converter: "pymupdf get_text via tools/clean.py normalize_markdown"
tags:
  - pdf-conversion
---

Watch
0
TUI & CLI package manager for Termux on Android. Browse, build, and install community tools from source and binary source — offline, SHA256-
verified, no root. Like AUR but for Termux.
MIT License
djunekz.github.io/termux-app-store/
Code of conduct
Contributing
Security policy
0 stars
0 forks
0 watching
1 branch
0 tags
Activity
Public repository · Forked from djunekz/termux-app-store
1 Branch
0 Tags
Go to file
Go to file
Add file
Code
This branch is up to date with djunekz/termux-app-store:master .
Contribute
Sync fork
Termux App Store chore: update index.json
a1a7992 · 17 hours ago
.assets
Upload gif from termux
4 months ago
.circleci
Update fixed
5 months ago
.github
Update actions/attest-build-provenance dig…
yesterday
ci
Added fixed floating sources packages
last month
packages
termux-sync bump version 1.2.3 to 1.2.4
2 weeks ago
template
Added template index.json
3 months ago
termux_app_store
Bump version 0.4.1 to 0.4.5
2 weeks ago
tests
Update fixed
5 months ago
tools
chore: update index.json
17 hours ago
.codecov.yml
Update .codecov.yml
6 months ago
ARCHITECTURE.md
Update formatting and headings in ARCHIT…
4 months ago
BINARY_DISCLAIMER.md
Remove emoji from section headers in discl…
4 months ago
CHANGELOG.md
Fix script-injection vulnerabilities in workflo…
last week
CODE_OF_CONDUCT.md
Update: docs CODE_OF_CONDUCT.md
6 months ago
CONTRIBUTING.md
Update formatting and headings in CONTRI…
4 months ago
DISCLAIMER.md
Remove emojis from DISCLAIMER.md secti…
4 months ago
FAQ.md
Upload docs and license
7 months ago
GOVERNANCE.md
Standardize headings in GOVERNANCE.md
4 months ago
HOW_TO_UPLOAD.md
Revise package upload instructions for clarity
4 months ago
INSTALL.md
Refactor INSTALL.md for improved readabili…
4 months ago
termux-app-store-poem
Code
Pull requests
Agents
More
Fork
0
m…
T


LICENSE
Update LICENSE
6 months ago
MANIFEST.in
Added manifest for pypi
4 months ago
PRIVACY.md
Refactor section headers in PRIVACY.md
4 months ago
README.ch.md
Revise README with new interface screens…
3 months ago
README.id.md
Update badge links in README.id.md
2 weeks ago
README.in.md
Update information readme
3 months ago
README.jp.md
Update information readme
3 months ago
README.md
Update star history section with responsive i…
2 weeks ago
README.th.md
Update information readme
3 months ago
README.vi.md
Update information readme
3 months ago
SECURITY.md
Revise security policy and reporting guidelin…
3 months ago
SUPPORT.md
Added: docs SUPPORT.md
6 months ago
TROUBLESHOOTING.md
Upload docs and license
7 months ago
build-package.sh
Improve warnings and fix minor formatting i…
2 weeks ago
build-tester.py
Fixed bug
3 months ago
doctor.py
Use shlex.quote for command safety in doct…
2 weeks ago
guidebook.py
Update cls function to use subprocess for te…
2 weeks ago
install-repo.py
Chore: update new interface and information
4 months ago
install.sh
Chore: update fixed installer
3 months ago
pkg-scaffold.py
Refactor version retrieval logic in pkg-scaffo…
last month
pyproject.toml
Bump version 0.4.1 to 0.4.5
2 weeks ago
pytest.ini
Update fixed
5 months ago
tasctl
Chore: update fixed installer
3 months ago
termux-build
Chore: update with create-index
3 months ago
uninstall.sh
Update fixed bug
6 months ago


The first offline-first, binary-safe TUI package manager built natively for Termux on Android.
Read in: 🇮🇩 Bahasa Indonesia | 🇹🇭 ภาษาไทย | 🇯🇵 日本語 | 🇨🇳 中文 | 🇻🇳 Tiếng Việt | 🇮🇳 हिन्दी
CI
CI
passing
passing
codecov
codecov
100%
100%
pypi
pypi v0.4.5
v0.4.5
release
release
Termux-App-Store v0.4.5
Termux-App-Store v0.4.5
downloads
downloads 942
942
License
License MIT
MIT
stars
stars
96
96
forks
forks
16
16
issues
issues open
open
pull requests
pull requests 0 open
0 open
Community
Community Ready
Ready
Offline-first • Binary-safe • Source-based • Termux-native • Android Terminal Install and manage Termux packages — pre-built binaries or
source builds — no root, no account, no telemetry.
Termux App Store ( termux-app-store ) is a TUI (Terminal User Interface) and CLI package manager built with Python (Textual) that lets
Termux users on Android browse, install, and manage tools/packages directly on-device — no account, no telemetry, no cloud dependency, no
root required.
Starting from v0.4.0, Termux App Store supports a fast install engine: packages are downloaded as pre-built .deb binaries from a mirror poo
(GitHub Pages, Cloudflare CDN, jsDelivr), with local .deb caching (TTL 7 days) and per-arch SHA256 verification. Source builds remain
available via fix-install for full control.
It works as an alternative package manager for Termux, letting you install community tools using verified build.sh scripts — similar in spirit
to the AUR (Arch User Repository) but designed specifically for Termux on Android.
How is this different from termux-packages or TUR (Termux User Repository)?
termux-packages is the official Termux repo — maintained by the core team, requires PR approval, and only accepts widely-used
tools.
TUR is a curated extension, still requires contributor review.
Termux App Store — TUI & CLI Package Manager for Termux
What is Termux App Store?
README
Code of conduct
More


Termux App Store is fully community-driven: anyone can submit a build.sh , packages are distributed as pre-built .deb or source
builds, and there is no centralized approval gate. Think of it as a personal + community package layer on top of Termux.
Important
Termux App Store is not a hidden auto-installer. All installs — binary or source — run locally, transparently, and under full user control.
User
Use Case
Termux Users
Fast binary installs or full source-build control
Developers
Distribute tools via pre-built .deb or source packaging
Reviewers & Auditors
Review and validate build scripts
Maintainers
Manage multiple Termux packages at once
Who Is It For?
Screenshots
Tui Interface


TUI Main Interface
TUI Install Interface
Menu Palette
TUI main menu
Package install process
Command palette
TUI User-friendly with full touchscreen support
Other tools support
CLI Install Interface
CLI View Interface
tasctl and termux-build
Package install process
CLI help, list and show
CLI Interface
GuideBook


List menu
Menu about
Menu how to upload
GuideBook main menu
Information termux-app-store
Guide how to upload
GuideBook is a information, run: python guidebook.py
Record termux-app-store TUI, CLI, Other tool tasctl , termux-build , guidebook.py
Screenrecord


Available on PyPI — searchable and indexed, easy to discover.
Simple (recommended if memory is limited)
With git clone (downloads full repository)
After install, run:
Quick Install and Uninstall
Option 1 (Recommended)
pkg install python
pip install termux-app-store
Option 2 (Manual)
curl -fsSL https://raw.githubusercontent.com/djunekz/termux-app-store/master/tasctl | bash -s install
git clone --single-branch --branch master https://github.com/djunekz/termux-app-store
cd termux-app-store
bash install.sh
termux-app-store        # Open interactive TUI
termux-app-store -h     # Show CLI help
tas                     # Shorthand for termux-app-store
Uninstall
pip uninstall termux-app-store
# or
./tasctl uninstall
Usage
TUI — Interactive Interface
termux-app-store
# or shorthand:
tas
CLI — Direct Commands
termux-app-store list                     # List all packages
termux-app-store show <package>           # Show package details
termux-app-store install <package>        # Fast install (pre-built .deb)
termux-app-store install pkg1 pkg2 pkg3   # Multi-package install
termux-app-store fix-install <package>    # Force source build (bypass fast install)
termux-app-store search <query>           # Search packages by name or description
termux-app-store update                   # Check for available updates
termux-app-store upgrade                  # Upgrade all packages
termux-app-store upgrade <package>        # Upgrade a specific package
termux-app-store uninstall <package>      # Uninstall a package
termux-app-store mirrors                  # Check mirror status
termux-app-store cache info               # Show binary cache info
termux-app-store cache clear              # Clear binary cache


Package Browser (TUI) Browse packages from the packages/ folder
interactively with keyboard & touchscreen navigation.
Fast Install Engine Downloads pre-built .deb from mirror pool —
GitHub Pages, Cloudflare CDN, jsDelivr — with automatic fallback.
Binary Cache Local .deb cache with 7-day TTL and per-arch SHA256
verification. Cached packages install instantly.
Smart Build Validator Detects unsupported Termux dependencies with
automatic status badges.
Real-time Search & Filter Search packages by name or
description — search / find CLI commands included.
Multi-package Install/Uninstall Install or remove several
packages in one command with a summary output.
One-Click Manage Install / update / uninstall Termux App
Store itself via ./tasctl .
Privacy-First No account, no tracking, no telemetry — fully
offline after mirror sync.
Badge
Description
NEW
Newly added package (< 7 days)
UPDATE
A newer version is available
INSTALLED
Installed version is up-to-date
UNSUPPORTED
Dependency not available in Termux
If fast install fails, use fix-install <package> to force a full source build via build-package.sh .
Every package in Termux App Store is defined by a single build.sh file — similar to how PKGBUILD works in Arch Linux, but adapted for
Termux on Android.
Every package must have a build.sh file:
termux-app-store version                  # Check latest version
termux-app-store help                     # Full help
Features
Package Status Badges
How Fast Install Works (v0.4.0+)
termux-app-store install <package>
        │
        ▼
  Check local .deb cache (TTL 7 days)
        │ cache HIT          │ cache MISS
        ▼                    ▼
  Verify SHA256        Try mirrors in order:
  (per arch)           1. GitHub Pages (primary)
        │              2. Cloudflare CDN
        ▼              3. jsDelivr CDN
  dpkg -i              4. Raw GitHub (fallback)
                             │
                             ▼
                       Download .deb
                       Verify SHA256 (sha256_by_arch)
                       Cache locally
                       dpkg -i
Adding a Package
packages/<tool-name>/build.sh


Note
See the full template in template/build.sh or run: ./termux-build template
Note
When naming, do not use spaces — use - . Example: my-tool-name
termux-build is a validation and reviewer helper tool — not an auto-upload or auto-publish tool.
Note
termux-build only reads and validates — it does not modify files or upload to GitHub.
tasctl is the controller for the termux-app-store system.
Minimal build.sh Template
TERMUX_PKG_HOMEPAGE=""
TERMUX_PKG_DESCRIPTION=""
TERMUX_PKG_LICENSE=""
TERMUX_PKG_MAINTAINER="@your-github-username"
TERMUX_PKG_VERSION=""
TERMUX_PKG_SRCURL=""
TERMUX_PKG_SHA256=""
Adding a Package using termux-build
cd termux-app-store
./termux-build create your-tool-name
# or auto-create from a GitHub URL:
./termux-build init https://github.com/user/repo
termux-build — Build & Validation Tool
./termux-build create <package>      # Create package for distribution
./termux-build init <url-repo>       # Auto-create and build package from GitHub URL
./termux-build lint <package>        # Lint a build script
./termux-build check-pr <package>    # Check PR readiness
./termux-build doctor                # Diagnose environment
./termux-build suggest <package>     # Get improvement suggestions
./termux-build explain <package>     # Detailed package explanation
./termux-build template              # Generate build.sh template
./termux-build guide                 # Contribution guide
tasctl — Termux App Store Controller
./tasctl install       # Install Termux App Store (latest)
./tasctl update        # Update to latest version
./tasctl uninstall     # Remove Termux App Store
./tasctl doctor        # Diagnose environment
./tasctl self-update   # Update tasctl itself
./tasctl help          # Show help
guidebook — All Information About Termux App Store
python guidebook.py


Note
guidebook currently supports two languages: English and Bahasa Indonesia.
Full guide: HOW_TO_UPLOAD.md
Full details: ARCHITECTURE.md
Security
Privacy
No extra permissions required
No account or registration
No network ports opened
No analytics or tracking
No background services running
No telemetry of any kind
Builds only run on explicit user command
Offline-first by design
SHA256 verification on all .deb downloads
Binary source is transparent and auditable
Full details: SECURITY.md | PRIVACY.md | DISCLAIMER.md | BINARY_DISCLAIMER.md
How to Distribute Your Package to the Termux Community
# 1. Fork this repo
# 2. Add your package folder:
mkdir packages/your-tool-name
# 3. Create build.sh from the template or with termux-build:
./termux-build create your-tool-name
# or from a GitHub URL:
./termux-build init https://github.com/you/your-repo
# 4. Validate with termux-build:
./termux-build lint packages/your-tool-name
# 5. Submit a Pull Request
Architecture
termux-app-store/
├── packages/              # All packages directory
│   └── <tool-name>/
│       └── build.sh       # Metadata & build script
├── template/
│   └── build.sh           # Package template
├── core/
│   ├── binary_core.py     # BinaryCache — local .deb cache + mirror download
│   ├── mirrors.py         # MirrorManager — mirror pool registry
│   ├── package.py         # Package dataclass
│   └── validator.py       # PackageValidator
├── utils/
│   └── installer.py       # install_from_binary / install_from_source helpers
├── tools/
│   └── mirrors.json       # Mirror registry (GitHub Pages, Cloudflare, jsDelivr, raw GitHub)
├── fast_install.py        # Fast install engine (.deb download + cache + SHA256 verify)
├── tasctl                 # TAS installer/updater/uninstaller
├── termux-build           # Validation & review tool
└── install.sh             # Main installer
Security & Privacy


All contributions are welcome!
How to Contribute
Description
Add a package
Submit a new tool package
Report a bug
Open an issue on GitHub
Send a PR
Code or documentation improvements
Review PRs
Help validate others' contributions
Security audit
Review build script security
Improve docs
Clarify or translate documentation
Full guide: CONTRIBUTING.md
Document
Description
FAQ
Frequently asked questions
TROUBLESHOOTING
Solutions to common problems
HOW TO UPLOAD
How to upload your tool
CONTRIBUTING
Contribution guide
SUPPORT
How to get support
BINARY_DISCLAIMER
Notes on binary distribution
"Local first. Control over convenience. Transparency over magic."
Termux App Store is built for users who want to:
Fully understand what runs on their device
Control builds and sources directly
Avoid vendor lock-in and cloud dependency
Share tools openly with the Termux community
This project is licensed under the MIT License — see LICENSE for details.
Djunekz — Independent & Official Developer
G I T H U B
D J U N E K Z
Releases
Contributing
Help & Documentation
Philosophy
License
Maintainer


No releases published
Create a new release
Packages
No packages published
Publish your first package
Contributors
No contributors
Languages
Python 57.6%
Shell 42.4%
Suggested workflows
Based on your tech stack
Django
Build and Test a Django Project
By GitHub Actions
Configure
Publish Python Package
Publish a Python Package to PyPI on release.
By GitHub Actions
Configure
SLSA Generic generator
Generate SLSA3 provenance for your existing release workflows
By Open Source Security Foundation (OpenSSF)
Configure
More workflows
