# Mer0vin8ian／Gemma-4-E4B-it · Hugging Face

Search models, datasets, users...
Mer0vin8ian/Gemma-4-E4B-it 
0
Text Generation
PyTorch
llm
vlm
generative_ai
android
Model card
Files
Community
Settings
like
License: other
xet
Copy to bucket
NEW
Downloads last month
-
Downloads are not tracked for this model. How to track
Text Generation
This model isn't deployed by any Inference Provider.
🙋Ask for provider support
Edit model card
Inference Providers
NEW
SSH
cURL
Clone this model repository
HTTPS
# Make sure git-xet is installed (https://hf.co/docs/hub/git-xet)
curl -sSfL https://hf.co/git-xet/install.sh | sh
git clone git@hf.co:Mer0vin8ian/Gemma-4-E4B-it
# If you want to clone without large files - just their pointers
GIT_LFS_SKIP_SMUDGE=1 git clone git@hf.co:Mer0vin8ian/Gemma-4-E4B-it
Homebrew
uv
uvx
# Make sure the hf CLI is installed
curl -LsSf https://hf.co/cli/install.sh | bash
# Download the model
hf download Mer0vin8ian/Gemma-4-E4B-it


Gemma is a family of open models built by Google DeepMind. Gemma 4 models are
multimodal, handling text and image input (with audio supported on small models)
and generating text output. This release includes open-weights models in both pre-
trained and instruction-tuned variants. Gemma 4 features a context window of up to
256K tokens and maintains multilingual support in over 140 languages.
This is based on the implementation of Gemma-4-E4B-it found here. This repository
contains pre-exported model files optimized for Qualcomm® devices. You can use the
Qualcomm® AI Hub Models library to export with custom configurations. More details
on model performance across various devices, can be found here.
Qualcomm AI Hub Models uses Qualcomm AI Hub Workbench to compile, profile, and
evaluate this model. Sign up to run these models on a hosted Qualcomm® device.
Follow the GenieX quickstart to install GenieX and deploy the model on a target device.
Gemma-4-E4B-it: Optimized for Qualcomm Devices
Deploying Gemma-4-E4B-it on-device
Clone this model repository
# Make sure git-xet is installed (https://hf.co/docs/hub/git-xet)
curl -sSfL https://hf.co/git-xet/install.sh | sh
git clone git@hf.co:Mer0vin8ian/Gemma-4-E4B-it
# If you want to clone without large files - just their pointers
GIT_LFS_SKIP_SMUDGE=1 git clone git@hf.co:Mer0vin8ian/Gemma-4-E4B-it
# Make sure the hf CLI is installed
curl -LsSf https://hf.co/cli/install.sh | bash
# Download the model
hf download Mer0vin8ian/Gemma-4-E4B-it


There are two ways to deploy this model on your device:
Below are pre-exported model assets ready for deployment.
Runtime
Precision
Chipset
SDK Versions
Download
GENIEX_LLAMACPP
q4_0
Universal
Download
For more device-specific assets and performance metrics, visit Gemma-4-E4B-it on
Qualcomm® AI Hub.
Use the Qualcomm® AI Hub Models Python library to compile and export the model
with your own:
Custom weights (e.g., fine-tuned checkpoints)
Custom input shapes
Target device and runtime configurations
This option is ideal if you need to customize the model beyond the default
configuration provided here.
See our repository for Gemma-4-E4B-it on GitHub for usage instructions.
Model Type: Model_use_case.text_generation
Getting Started
Option 1: Download Pre-Exported Models
Option 2: Export with Custom Configurations
Model Details
Clone this model repository
# Make sure git-xet is installed (https://hf.co/docs/hub/git-xet)
curl -sSfL https://hf.co/git-xet/install.sh | sh
git clone git@hf.co:Mer0vin8ian/Gemma-4-E4B-it
# If you want to clone without large files - just their pointers
GIT_LFS_SKIP_SMUDGE=1 git clone git@hf.co:Mer0vin8ian/Gemma-4-E4B-it
# Make sure the hf CLI is installed
curl -LsSf https://hf.co/cli/install.sh | bash
# Download the model
hf download Mer0vin8ian/Gemma-4-E4B-it


Model Stats:
Model architecture: Mixture-of-Experts (MoE) Transformer with Per-Layer Expert
Selection and selective routing.
Supported languages: Multilingual (trained on 140+ languages)
TTFT: Time To First Token is the time it takes to generate the first response token.
This is expressed as a range because it varies based on the length of the prompt.
Response Rate: Rate of response generation after the first response token.
Model
Runtime
Precision
Chipset
Context
Length
Response
Rate
(tokens
per
second)
Time To Fir
(range, se
Gemma-
4-E4B-it
GENIEX_LLAMACPP
q4_0
Snapdragon®
8 Elite Gen 5
Mobile
512
17.905892
1.12984925 
Gemma-
4-E4B-it
GENIEX_LLAMACPP
q4_0
Snapdragon®
8 Elite Gen 5
Mobile
512
17.771069
1.246530749
- 4.98612299
Gemma-
4-E4B-it
GENIEX_LLAMACPP
q4_0
Snapdragon®
8 Elite Gen 5
Mobile
512
16.824563
0.195887 - 0
Gemma-
4-E4B-it
GENIEX_LLAMACPP
q4_0
Snapdragon®
8 Elite Gen 5
Mobile
4096
13.347809
2.223176625
- 71.1416520
Gemma-
4-E4B-it
GENIEX_LLAMACPP
q4_0
Snapdragon®
8 Elite Gen 5
Mobile
4096
11.701253
2.24031025 
71.689928
Performance Summary
Clone this model repository
# Make sure git-xet is installed (https://hf.co/docs/hub/git-xet)
curl -sSfL https://hf.co/git-xet/install.sh | sh
git clone git@hf.co:Mer0vin8ian/Gemma-4-E4B-it
# If you want to clone without large files - just their pointers
GIT_LFS_SKIP_SMUDGE=1 git clone git@hf.co:Mer0vin8ian/Gemma-4-E4B-it
# Make sure the hf CLI is installed
curl -LsSf https://hf.co/cli/install.sh | bash
# Download the model
hf download Mer0vin8ian/Gemma-4-E4B-it


Model
Runtime
Precision
Chipset
Context
Length
Response
Rate
(tokens
per
second)
Time To Fir
(range, se
Gemma-
4-E4B-it
GENIEX_LLAMACPP
q4_0
Snapdragon®
8 Elite Gen 5
Mobile
4096
13.26779
0.265452468
8.494479
Gemma-
4-E4B-it
GENIEX_LLAMACPP
q4_0
Snapdragon®
8 Elite Mobile
512
17.234032
1.26287975 
Gemma-
4-E4B-it
GENIEX_LLAMACPP
q4_0
Snapdragon®
8 Elite Mobile
512
16.777481
1.35680775 
Gemma-
4-E4B-it
GENIEX_LLAMACPP
q4_0
Snapdragon®
8 Elite Mobile
512
16.021655
0.1988185 - 
Gemma-
4-E4B-it
GENIEX_LLAMACPP
q4_0
Snapdragon®
8 Elite Mobile
4096
12.238845
2.369586437
75.826766
Gemma-
4-E4B-it
GENIEX_LLAMACPP
q4_0
Snapdragon®
8 Elite Mobile
4096
12.105188
2.424854968
77.595359
Gemma-
4-E4B-it
GENIEX_LLAMACPP
q4_0
Snapdragon®
8 Elite Mobile
4096
12.358648
0.299681656
9.589813
Gemma-
4-E4B-it
GENIEX_LLAMACPP
q4_0
Snapdragon®
X2 Elite
512
23.827865
0.680427249
-
2.721708999
Gemma-
4-E4B-it
GENIEX_LLAMACPP
q4_0
Snapdragon®
X2 Elite
512
25.136049
0.729007 - 2
Gemma-
4-E4B-it
GENIEX_LLAMACPP
q4_0
Snapdragon®
X2 Elite
512
20.846358
0.146913000
-
0.587652000
Gemma-
4-E4B-it
GENIEX_LLAMACPP
q4_0
Snapdragon®
X2 Elite
4096
12.013094
1.250677468
40.021679
Clone this model repository
# Make sure git-xet is installed (https://hf.co/docs/hub/git-xet)
curl -sSfL https://hf.co/git-xet/install.sh | sh
git clone git@hf.co:Mer0vin8ian/Gemma-4-E4B-it
# If you want to clone without large files - just their pointers
GIT_LFS_SKIP_SMUDGE=1 git clone git@hf.co:Mer0vin8ian/Gemma-4-E4B-it
# Make sure the hf CLI is installed
curl -LsSf https://hf.co/cli/install.sh | bash
# Download the model
hf download Mer0vin8ian/Gemma-4-E4B-it


Model
Runtime
Precision
Chipset
Context
Length
Response
Rate
(tokens
per
second)
Time To Fir
(range, se
Gemma-
4-E4B-it
GENIEX_LLAMACPP
q4_0
Snapdragon®
X2 Elite
4096
13.238633
1.140750406
36.504013
Gemma-
4-E4B-it
GENIEX_LLAMACPP
q4_0
Snapdragon®
X2 Elite
4096
17.911474
0.193840781
-
6.202904999
Gemma-
4-E4B-it
GENIEX_LLAMACPP
q4_0
Snapdragon®
X Elite
512
20.525636
0.53967775 
Gemma-
4-E4B-it
GENIEX_LLAMACPP
q4_0
Snapdragon®
X Elite
512
19.702914
0.6135875 - 
Gemma-
4-E4B-it
GENIEX_LLAMACPP
q4_0
Snapdragon®
X Elite
512
11.882264
0.35202125 
Gemma-
4-E4B-it
GENIEX_LLAMACPP
q4_0
Snapdragon®
X Elite
4096
11.823266
0.803188843
25.702043
Gemma-
4-E4B-it
GENIEX_LLAMACPP
q4_0
Snapdragon®
X Elite
4096
8.192524
0.932555093
29.841763
Gemma-
4-E4B-it
GENIEX_LLAMACPP
q4_0
Snapdragon®
X Elite
4096
10.034623
0.464178062
14.853698
Gemma-
4-E4B-it
GENIEX_LLAMACPP
q4_0
Qualcomm®
Dragonwing™
IQ-9075
512
13.439978
1.7480915 - 
Gemma-
4-E4B-it
GENIEX_LLAMACPP
q4_0
Qualcomm®
Dragonwing™
IQ-9075
512
13.431804
1.75437625 
Clone this model repository
# Make sure git-xet is installed (https://hf.co/docs/hub/git-xet)
curl -sSfL https://hf.co/git-xet/install.sh | sh
git clone git@hf.co:Mer0vin8ian/Gemma-4-E4B-it
# If you want to clone without large files - just their pointers
GIT_LFS_SKIP_SMUDGE=1 git clone git@hf.co:Mer0vin8ian/Gemma-4-E4B-it
# Make sure the hf CLI is installed
curl -LsSf https://hf.co/cli/install.sh | bash
# Download the model
hf download Mer0vin8ian/Gemma-4-E4B-it


Model
Runtime
Precision
Chipset
Context
Length
Response
Rate
(tokens
per
second)
Time To Fir
(range, se
Gemma-
4-E4B-it
GENIEX_LLAMACPP
q4_0
Qualcomm®
Dragonwing™
IQ-9075
512
8.859328
0.3919085 - 
Gemma-
4-E4B-it
GENIEX_LLAMACPP
q4_0
Qualcomm®
Dragonwing™
IQ-9075
4096
10.071341
2.126688531
- 68.0540329
Gemma-
4-E4B-it
GENIEX_LLAMACPP
q4_0
Qualcomm®
Dragonwing™
IQ-9075
4096
10.054127
2.094956437
67.038606
Gemma-
4-E4B-it
GENIEX_LLAMACPP
q4_0
Qualcomm®
Dragonwing™
IQ-9075
4096
7.626485
0.500706562
16.02261
The license for the original implementation of Gemma-4-E4B-it can be found here.
Gemma 4
Source Model Implementation
Join our AI Hub Slack community to collaborate, post questions and learn more
about on-device AI.
License
References
Community
Clone this model repository
# Make sure git-xet is installed (https://hf.co/docs/hub/git-xet)
curl -sSfL https://hf.co/git-xet/install.sh | sh
git clone git@hf.co:Mer0vin8ian/Gemma-4-E4B-it
# If you want to clone without large files - just their pointers
GIT_LFS_SKIP_SMUDGE=1 git clone git@hf.co:Mer0vin8ian/Gemma-4-E4B-it
# Make sure the hf CLI is installed
curl -LsSf https://hf.co/cli/install.sh | bash
# Download the model
hf download Mer0vin8ian/Gemma-4-E4B-it


For questions or feedback please reach out to us.
This model may not be used for or in connection with any of the following applications:
Accessing essential private and public services and benefits;
Administration of justice and democratic processes;
Assessing or recognizing the emotional state of a person;
Biometric and biometrics-based systems, including categorization of persons
based on sensitive characteristics;
Education and vocational training;
Employment and workers management;
Exploitation of the vulnerabilities of persons resulting in harmful behavior;
General purpose social scoring;
Law enforcement;
Management and operation of critical infrastructure;
Migration, asylum and border control management;
Predictive policing;
Real-time remote biometric identification in public spaces;
Recommender systems of social media platforms;
Scraping of facial images (from the internet or otherwise); and/or
Subliminal manipulation
Usage and Limitations
Clone this model repository
# Make sure git-xet is installed (https://hf.co/docs/hub/git-xet)
curl -sSfL https://hf.co/git-xet/install.sh | sh
git clone git@hf.co:Mer0vin8ian/Gemma-4-E4B-it
# If you want to clone without large files - just their pointers
GIT_LFS_SKIP_SMUDGE=1 git clone git@hf.co:Mer0vin8ian/Gemma-4-E4B-it
# Make sure the hf CLI is installed
curl -LsSf https://hf.co/cli/install.sh | bash
# Download the model
hf download Mer0vin8ian/Gemma-4-E4B-it


Company
TOS
Privacy
About
Careers
Website
Models
Datasets
Spaces
Pricing
Docs
System theme
Clone this model repository
# Make sure git-xet is installed (https://hf.co/docs/hub/git-xet)
curl -sSfL https://hf.co/git-xet/install.sh | sh
git clone git@hf.co:Mer0vin8ian/Gemma-4-E4B-it
# If you want to clone without large files - just their pointers
GIT_LFS_SKIP_SMUDGE=1 git clone git@hf.co:Mer0vin8ian/Gemma-4-E4B-it
# Make sure the hf CLI is installed
curl -LsSf https://hf.co/cli/install.sh | bash
# Download the model
hf download Mer0vin8ian/Gemma-4-E4B-it
