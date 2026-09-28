# c10vis-poem／android-reverse-engineering-skill: Claude Code skill to support Android app's reverse engineering

Watch
0
Claude Code skill to support Android app's reverse engineering
Apache License 2.0
0 stars
0 forks
0 watching
1 branch
0 tags
Activity
Public repository · Forked from SimoneAvogadro/android-reverse-engineering-skill
1 Branch
0 Tags
Go to file
Go to file
Add file
Code
This branch is up to date with SimoneAvogadro/android-reverse-engineering-skill:master .
Contribute
Sync fork
SimoneAvogadro chore: bump plugin version to 1.5.0
e8dde9d · last month
.claude-plugin
chore: bump plugin version to 1.5.0
last month
plugins/android-reverse-engineering
chore: bump plugin version to 1.5.0
last month
.gitattributes
ADDED: .gitattributes for better WSL/Windo…
5 months ago
LICENSE
Fix GitHub username in all repository URLs …
5 months ago
README.md
docs: document PR SimoneAvogadro#16 fe…
last month
License
License Apache-2.0
Apache-2.0
Stars
Stars
6.6k
6.6k
last commit
last commit june
june
A Claude Code skill that decompiles Android APK/XAPK/JAR/AAR files and extracts the HTTP APIs used by the app — Retrofit endpoints,
OkHttp calls, hardcoded URLs, authentication patterns — so you can document and reproduce them without the original source code.
First-class Kotlin support: modern Android apps are Kotlin/KMP, heavily obfuscated with R8. This skill recovers the original Kotlin class
names from metadata R8 cannot strip, and extracts APIs from Ktor, Apollo (GraphQL) and Koin — not just the classic Retrofit/OkHttp
stack. See Kotlin name recovery below.
Windows / PowerShell support (experimental): The *.ps1 scripts alongside the bash ones are a recent community contribution, still
being stabilised. For any issues please open an issue on this repository (not on the contributors' upstream forks): the PowerShell scripts
are maintained here by @SimoneAvogadro.
What it does
Requirements
Installation
Usage
Repository Structure
References
Acknowledgments
Disclaimer
c10vis-poem
android-reverse-engineering-skill
Code
Pull requests
Agents
Actions
Projects
Wiki
Security and quality
Insights
Settings
Fork
0
m…
T
Android Reverse Engineering & API Extraction — Claude Code skill
Table of Contents
README
License


License
Capability
Description
Fingerprint first
(Phase 0)
Triage an APK/XAPK in seconds — detect the framework (Flutter / React Native / Cordova / Xamarin / native-Kotlin),
HTTP stack, obfuscation level and native libs before spending time on a full decompile
Decompile
APK, XAPK, JAR, and AAR files using jadx and Fernflower/Vineflower (single engine or side-by-side comparison)
Recover Kotlin
names
Rebuild original *Repository / *ViewModel / *UseCase class names from R8-obfuscated binaries using Kotlin
metadata that R8 cannot strip
Extract APIs
Retrofit, OkHttp, Volley and modern Kotlin/KMP stacks: Ktor, Apollo (GraphQL), Koin DI — endpoints, hardcoded
URLs, auth headers, tokens and HMAC request-signing schemes
Trace call flows
From Activities/Fragments through ViewModels and repositories down to HTTP calls
Analyze structure
Manifest, packages, architecture patterns
Handle
obfuscation
R8-resistant path/URL extraction plus strategies for navigating ProGuard/R8 output
Required:
Java JDK 17+
jadx (CLI)
Optional (recommended):
Vineflower or Fernflower — better output on complex Java code
dex2jar — needed to use Fernflower on APK/DEX files
See plugins/android-reverse-engineering/skills/android-reverse-engineering/references/setup-guide.md for detailed installation
instructions.
Inside Claude Code, run:
The skill will be permanently available in all future sessions.
Then in Claude Code:
What it does
Requirements
Installation
From GitHub (recommended)
/plugin marketplace add SimoneAvogadro/android-reverse-engineering-skill
/plugin install android-reverse-engineering@android-reverse-engineering-skill
From a local clone
git clone https://github.com/SimoneAvogadro/android-reverse-engineering-skill.git
/plugin marketplace add /path/to/android-reverse-engineering-skill
/plugin install android-reverse-engineering@android-reverse-engineering-skill


This runs the full workflow: dependency check, decompilation, and initial structure analysis.
The skill activates on phrases like:
"Decompile this APK"
"Reverse engineer this Android app"
"Extract API endpoints from this app"
"Follow the call flow from LoginActivity"
"Analyze this AAR library"
The scripts can also be used standalone:
Most real-world Kotlin/KMP apps ship through R8, so the decompiled classes come out as a.b.c . R8 renames the JVM symbols but cannot
strip the Kotlin metadata strings — the Kotlin runtime (reflection, coroutines) needs the original fully-qualified names at runtime. This skill
mines those @DebugMetadata / @Metadata annotations to rebuild an obfuscated → real class-name map. On a typical app it recovers
~100 % of the *Repository / *ViewModel / *UseCase / *Impl classes you actually want to read.
Usage
Slash command
/decompile path/to/app.apk
Natural language
Manual scripts
# Check dependencies
bash plugins/android-reverse-engineering/skills/android-reverse-engineering/scripts/check-deps.sh
# Install a missing dependency (auto-detects OS and package manager)
bash plugins/android-reverse-engineering/skills/android-reverse-engineering/scripts/install-dep.sh jadx
bash plugins/android-reverse-engineering/skills/android-reverse-engineering/scripts/install-dep.sh vineflower
# Fingerprint an APK/XAPK BEFORE decompiling (Phase 0 triage):
# framework, HTTP stack, obfuscation level, native libs, notable SDKs
bash plugins/android-reverse-engineering/skills/android-reverse-engineering/scripts/fingerprint.sh app.apk
# Decompile APK with jadx (default)
bash plugins/android-reverse-engineering/skills/android-reverse-engineering/scripts/decompile.sh app.apk
# Decompile XAPK (auto-extracts and decompiles each APK inside)
bash plugins/android-reverse-engineering/skills/android-reverse-engineering/scripts/decompile.sh app-bundle.xapk
# Decompile with Fernflower
bash plugins/android-reverse-engineering/skills/android-reverse-engineering/scripts/decompile.sh --engine fernflower 
# Run both engines and compare
bash plugins/android-reverse-engineering/skills/android-reverse-engineering/scripts/decompile.sh --engine both --deob
# Find API calls — defaults to a full scan across every supported stack
bash plugins/android-reverse-engineering/skills/android-reverse-engineering/scripts/find-api-calls.sh output/sources/
bash plugins/android-reverse-engineering/skills/android-reverse-engineering/scripts/find-api-calls.sh output/sources/
bash plugins/android-reverse-engineering/skills/android-reverse-engineering/scripts/find-api-calls.sh output/sources/
# Modern Kotlin/KMP stacks and obfuscation-resistant extraction
bash plugins/android-reverse-engineering/skills/android-reverse-engineering/scripts/find-api-calls.sh output/sources/
bash plugins/android-reverse-engineering/skills/android-reverse-engineering/scripts/find-api-calls.sh output/sources/
bash plugins/android-reverse-engineering/skills/android-reverse-engineering/scripts/find-api-calls.sh output/sources/
Kotlin name recovery (R8 deobfuscation)
# 1. Build the mapping from the decompiled sources
bash plugins/android-reverse-engineering/skills/android-reverse-engineering/scripts/recover-kotlin-names.sh output/so


jadx — Dex to Java decompiler
Fernflower — JetBrains analytical decompiler
Vineflower — Fernflower community fork
dex2jar — DEX to JAR converter
apktool — Android resource decoder
Thanks to the contributors who have shaped this skill:
@tajchert — Phase 0 fingerprinting, R8-resistant Kotlin name recovery ( recover-kotlin-names.sh , lookup-name.sh ), and Ktor / Apollo /
Koin / HMAC extraction patterns (#16)
@philjn — Native Windows / PowerShell support ( check-deps.ps1 , install-dep.ps1 , decompile.ps1 , find-api-calls.ps1 ) and
split/bundled APK detection in decompile.sh (#8)
@txhno — Migration to the maintained ThexXTURBOXx/dex2jar fork (#12)
@muqiao215 — Decompile partial-success handling, Fernflower timeout safeguard, intermediate-artifact directory (#10)
#    → output/names/mapping.tsv, mapping.json, by_package/
# 2. Query it: resolve an obfuscated name, search by real name, or grep
#    the sources with each hit annotated with its recovered class name
bash plugins/android-reverse-engineering/skills/android-reverse-engineering/scripts/lookup-name.sh output/names/ Logi
bash plugins/android-reverse-engineering/skills/android-reverse-engineering/scripts/lookup-name.sh output/names/ -o a
bash plugins/android-reverse-engineering/skills/android-reverse-engineering/scripts/lookup-name.sh output/names/ --gr
Repository Structure
android-reverse-engineering-skill/
├── .claude-plugin/
│   └── marketplace.json                    # Marketplace catalog
├── plugins/
│   └── android-reverse-engineering/
│       ├── .claude-plugin/
│       │   └── plugin.json                 # Plugin manifest
│       ├── skills/
│       │   └── android-reverse-engineering/
│       │       ├── SKILL.md                # Core workflow (Phase 0–5)
│       │       ├── references/
│       │       │   ├── setup-guide.md
│       │       │   ├── jadx-usage.md
│       │       │   ├── fernflower-usage.md
│       │       │   ├── api-extraction-patterns.md
│       │       │   ├── kotlin-name-recovery.md
│       │       │   ├── third_party_hosts.txt   # denylist for first/third-party bucketing
│       │       │   └── call-flow-analysis.md
│       │       └── scripts/
│       │           ├── check-deps.sh       # Bash
│       │           ├── check-deps.ps1      # PowerShell
│       │           ├── install-dep.sh
│       │           ├── install-dep.ps1
│       │           ├── decompile.sh
│       │           ├── decompile.ps1
│       │           ├── fingerprint.sh          # Phase 0 — pre-decompile triage
│       │           ├── recover-kotlin-names.sh # R8 → real Kotlin class names
│       │           ├── lookup-name.sh          # query the recovered name map
│       │           ├── find-api-calls.sh
│       │           └── find-api-calls.ps1
│       └── commands/
│           └── decompile.md                # /decompile slash command
├── LICENSE
└── README.md
References
Acknowledgments


@kevinaimonster — Chinese localization ( SKILL.md discovery keywords) (#4)
This plugin is provided strictly for lawful purposes, including but not limited to:
Security research and authorized penetration testing
Interoperability analysis permitted under applicable law (e.g., EU Directive 2009/24/EC, US DMCA §1201(f))
Malware analysis and incident response
Educational use and CTF competitions
You are solely responsible for ensuring that your use of this tool complies with all applicable laws, regulations, and terms of service.
Unauthorized reverse engineering of software you do not own or do not have permission to analyze may violate intellectual property laws and
computer fraud statutes in your jurisdiction.
The authors disclaim any liability for misuse of this tool.
Releases
No releases published
Create a new release
Packages
No packages published
Publish your first package
Contributors
No contributors
Languages
Shell 51.4%
PowerShell 48.6%
Disclaimer
