---
title: "qualcomm_Qwen3.5-0.8B · Hugging Face"
source: "Drive_sync/Original_Corpora/___Lex-Novi-Æxentis-Copiæ/--•📱📎_GITHUB_📂💻~/#REPO.s/qualcomm_Qwen3.5-0.8B · Hugging Face.pdf"
cleaned: 2026-10-08
converter: "pymupdf get_text via tools/clean.py normalize_markdown"
tags:
  - pdf-conversion
---

Search models, datasets, users...
qualcomm/Qwen3.5-0.8B
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
like
1.09k
Follow
Qualcomm
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


Qwen3.5 is the latest multilingual language model series from Alibaba Cloud with
improved reasoning and instruction-following capabilities over Qwen3.
This is based on the implementation of Qwen3.5-0.8B found here. This repository
contains pre-exported model files optimized for Qualcomm® devices. You can use the
Qualcomm® AI Hub Models library to export with custom configurations. More details
on model performance across various devices, can be found here.
Qualcomm AI Hub Models uses Qualcomm AI Hub Workbench to compile, profile, and
evaluate this model. Sign up to run these models on a hosted Qualcomm® device.
Follow the GenieX quickstart to install GenieX and deploy the model on a target device.
There are two ways to deploy this model on your device:
Qwen3.5-0.8B: Optimized for Qualcomm Devices
Deploying Qwen3.5-0.8B on-device
Getting Started


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
For more device-specific assets and performance metrics, visit Qwen3.5-0.8B on
Qualcomm® AI Hub.
Use the Qualcomm® AI Hub Models Python library to compile and export the model
with your own:
Custom weights (e.g., fine-tuned checkpoints)
Custom input shapes
Target device and runtime configurations
This option is ideal if you need to customize the model beyond the default
configuration provided here.
See our repository for Qwen3.5-0.8B on GitHub for usage instructions.
Model Type: Model_use_case.text_generation
Model Stats:
Model architecture: Transformer with GQA and SwiGLU
Supported languages: 100+ languages and dialects
Option 1: Download Pre-Exported Models
Option 2: Export with Custom Configurations
Model Details


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
Time To F
(range, s
Qwen3.5-
0.8B
GENIEX_LLAMACPP
q4_0
Snapdragon®
8 Elite Gen 5
Mobile
512
62.131097
0.23427574
-
0.93710299
Qwen3.5-
0.8B
GENIEX_LLAMACPP
q4_0
Snapdragon®
8 Elite Gen 5
Mobile
512
50.763998
0.27429675
Qwen3.5-
0.8B
GENIEX_LLAMACPP
q4_0
Snapdragon®
8 Elite Gen 5
Mobile
512
35.869292
0.11880325
Qwen3.5-
0.8B
GENIEX_LLAMACPP
q4_0
Snapdragon®
8 Elite Gen 5
Mobile
4096
59.414176
0.36005078
11.521625
Qwen3.5-
0.8B
GENIEX_LLAMACPP
q4_0
Snapdragon®
8 Elite Gen 5
Mobile
4096
56.679703
0.39175446
12.536143
Qwen3.5-
0.8B
GENIEX_LLAMACPP
q4_0
Snapdragon®
8 Elite Gen 5
Mobile
4096
41.909392
0.11803384
3.777083
Qwen3.5-
0.8B
GENIEX_LLAMACPP
q4_0
Snapdragon®
8 Elite Mobile
512
72.950102
0.26924750
-
Performance Summary


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
Time To F
(range, s
1.07699000
Qwen3.5-
0.8B
GENIEX_LLAMACPP
q4_0
Snapdragon®
8 Elite Mobile
512
62.441461
0.26454675
Qwen3.5-
0.8B
GENIEX_LLAMACPP
q4_0
Snapdragon®
8 Elite Mobile
512
37.52486
0.1532055 -
Qwen3.5-
0.8B
GENIEX_LLAMACPP
q4_0
Snapdragon®
8 Elite Mobile
4096
49.751244
0.42967528
13.749609
Qwen3.5-
0.8B
GENIEX_LLAMACPP
q4_0
Snapdragon®
8 Elite Mobile
4096
48.911714
0.43504246
13.921359
Qwen3.5-
0.8B
GENIEX_LLAMACPP
q4_0
Snapdragon®
8 Elite Mobile
4096
35.893754
0.15914856
5.092754
Qwen3.5-
0.8B
GENIEX_LLAMACPP
q4_0
Snapdragon®
X2 Elite
512
88.774407
0.09157649
-
0.36630599
Qwen3.5-
0.8B
GENIEX_LLAMACPP
q4_0
Snapdragon®
X2 Elite
512
87.673154
0.0942735 -
Qwen3.5-
0.8B
GENIEX_LLAMACPP
q4_0
Snapdragon®
X2 Elite
512
40.640275
0.1113045 -
Qwen3.5-
0.8B
GENIEX_LLAMACPP
q4_0
Snapdragon®
X2 Elite
4096
81.095293
0.12939821
-
4.14074300
Qwen3.5-
0.8B
GENIEX_LLAMACPP
q4_0
Snapdragon®
X2 Elite
4096
80.304757
0.14290928
4.573097
Qwen3.5-
0.8B
GENIEX_LLAMACPP
q4_0
Snapdragon®
X2 Elite
4096
39.613582
0.11075478
-


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
Time To F
(range, s
3.54415299
Qwen3.5-
0.8B
GENIEX_LLAMACPP
q4_0
Snapdragon®
X Elite
512
64.713531
0.12653075
Qwen3.5-
0.8B
GENIEX_LLAMACPP
q4_0
Snapdragon®
X Elite
512
63.044187
0.12997225
Qwen3.5-
0.8B
GENIEX_LLAMACPP
q4_0
Snapdragon®
X Elite
512
29.988464
0.2527895 -
Qwen3.5-
0.8B
GENIEX_LLAMACPP
q4_0
Snapdragon®
X Elite
4096
51.537779
0.21393696
6.845983
Qwen3.5-
0.8B
GENIEX_LLAMACPP
q4_0
Snapdragon®
X Elite
4096
48.821458
0.23768365
7.605877
Qwen3.5-
0.8B
GENIEX_LLAMACPP
q4_0
Snapdragon®
X Elite
4096
28.38794
0.25720621
8.230599
Qwen3.5-
0.8B
GENIEX_LLAMACPP
q4_0
Qualcomm®
Dragonwing™
IQ-9075
512
49.130392
0.36298 - 1.
Qwen3.5-
0.8B
GENIEX_LLAMACPP
q4_0
Qualcomm®
Dragonwing™
IQ-9075
512
50.150451
0.36064100
-
1.44256400
Qwen3.5-
0.8B
GENIEX_LLAMACPP
q4_0
Qualcomm®
Dragonwing™
IQ-9075
512
14.985471
0.33844025
Qwen3.5-
0.8B
GENIEX_LLAMACPP
q4_0
Qualcomm®
Dragonwing™
IQ-X7181
512
64.713531
0.12653075


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
Time To F
(range, s
Qwen3.5-
0.8B
GENIEX_LLAMACPP
q4_0
Qualcomm®
Dragonwing™
IQ-X7181
512
63.044187
0.12997225
Qwen3.5-
0.8B
GENIEX_LLAMACPP
q4_0
Qualcomm®
Dragonwing™
IQ-X7181
512
29.988464
0.2527895 -
Qwen3.5-
0.8B
GENIEX_LLAMACPP
q4_0
Qualcomm®
Dragonwing™
Q-8750
512
72.950102
0.26924750
-
1.07699000
Qwen3.5-
0.8B
GENIEX_LLAMACPP
q4_0
Qualcomm®
Dragonwing™
Q-8750
512
62.441461
0.26454675
Qwen3.5-
0.8B
GENIEX_LLAMACPP
q4_0
Qualcomm®
Dragonwing™
Q-8750
512
37.52486
0.1532055 -
Qwen3.5-
0.8B
GENIEX_LLAMACPP
q4_0
Qualcomm®
Dragonwing™
IQ-9075
4096
38.271652
0.46651725
14.928552
Qwen3.5-
0.8B
GENIEX_LLAMACPP
q4_0
Qualcomm®
Dragonwing™
IQ-9075
4096
39.346842
0.46202675
14.784856
Qwen3.5-
0.8B
GENIEX_LLAMACPP
q4_0
Qualcomm®
Dragonwing™
IQ-9075
4096
14.03834
0.33502103
-
10.7206730
Qwen3.5-
0.8B
GENIEX_LLAMACPP
q4_0
Qualcomm®
Dragonwing™
IQ-X7181
4096
51.537779
0.21393696
6.845983


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
Time To F
(range, s
Qwen3.5-
0.8B
GENIEX_LLAMACPP
q4_0
Qualcomm®
Dragonwing™
IQ-X7181
4096
48.821458
0.23768365
7.605877
Qwen3.5-
0.8B
GENIEX_LLAMACPP
q4_0
Qualcomm®
Dragonwing™
IQ-X7181
4096
28.38794
0.25720621
8.230599
Qwen3.5-
0.8B
GENIEX_LLAMACPP
q4_0
Qualcomm®
Dragonwing™
Q-8750
4096
49.751244
0.42967528
13.749609
Qwen3.5-
0.8B
GENIEX_LLAMACPP
q4_0
Qualcomm®
Dragonwing™
Q-8750
4096
48.911714
0.43504246
13.921359
Qwen3.5-
0.8B
GENIEX_LLAMACPP
q4_0
Qualcomm®
Dragonwing™
Q-8750
4096
35.893754
0.15914856
5.092754
The license for the original implementation of Qwen3.5-0.8B can be found here.
Qwen3.5: Towards Native Multimodal Agents
Source Model Implementation
License
References
Community


Join our AI Hub Slack community to collaborate, post questions and learn more
about on-device AI.
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
