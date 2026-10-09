---
title: "qualcomm_Phi-4-Mini-Instruct · Hugging Face"
source: "Drive_sync/Original_Corpora/___Lex-Novi-Æxentis-Copiæ (1)/--•📱📎_GITHUB_📂💻~/#REPO.s/qualcomm_Phi-4-Mini-Instruct · Hugging Face.pdf"
cleaned: 2026-10-08
converter: "pymupdf get_text via tools/clean.py normalize_markdown"
tags:
  - pdf-conversion
---

Search models, datasets, users...
qualcomm/Phi-4-Mini-Instruct
0
Text Generation
PyTorch
llm
generative_ai
android
Model card
Files
Community
like
1.09k
Follow
Qualcomm
arxiv:2412.08905
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
Paper for qualcomm/Phi-4-Mini-Instruct
Phi-4 Technical Report
Paper • 2412.08905 • Published Dec 12, 2024 •
124
Edit model card
Inference Providers
NEW


Phi-4-mini-instruct is a lightweight open model built upon synthetic data and filtered
publicly available websites - with a focus on high-quality, reasoning dense data.
This is based on the implementation of Phi-4-Mini-Instruct found here. This repository
contains pre-exported model files optimized for Qualcomm® devices. You can use the
Qualcomm® AI Hub Models library to export with custom configurations. More details
on model performance across various devices, can be found here.
Qualcomm AI Hub Models uses Qualcomm AI Hub Workbench to compile, profile, and
evaluate this model. Sign up to run these models on a hosted Qualcomm® device.
Follow the GenieX quickstart to install GenieX and deploy the model on a target device.
There are two ways to deploy this model on your device:
Phi-4-Mini-Instruct: Optimized for Qualcomm Devices
Deploying Phi-4-Mini-Instruct on-device
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
For more device-specific assets and performance metrics, visit Phi-4-Mini-Instruct on
Qualcomm® AI Hub.
Use the Qualcomm® AI Hub Models Python library to compile and export the model
with your own:
Custom weights (e.g., fine-tuned checkpoints)
Custom input shapes
Target device and runtime configurations
This option is ideal if you need to customize the model beyond the default
configuration provided here.
See our repository for Phi-4-Mini-Instruct on GitHub for usage instructions.
Model Type: Model_use_case.text_generation
Model Stats:
Number of parameters: 3.8B
Option 1: Download Pre-Exported Models
Option 2: Export with Custom Configurations
Model Details


TTFT: Time To First Token is the time it takes to generate the first response token.
This is expressed as a range because it varies based on the length of the prompt.
The lower bound is for a short prompt (up to 128 tokens, i.e., one iteration of the
prompt processor) and the upper bound is for a prompt using the full context
length (4096 tokens).
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
Time To Firs
(range, se
Phi-4-
Mini-
Instruct
GENIEX_LLAMACPP
q4_0
Snapdragon®
8 Elite Gen 5
Mobile
512
23.272858
0.92645325 -
Phi-4-
Mini-
Instruct
GENIEX_LLAMACPP
q4_0
Snapdragon®
8 Elite Gen 5
Mobile
512
22.664968
1.03434575 -
Phi-4-
Mini-
Instruct
GENIEX_LLAMACPP
q4_0
Snapdragon®
8 Elite Gen 5
Mobile
512
19.242405
0.1765904999
-
0.7063619999
Phi-4-
Mini-
Instruct
GENIEX_LLAMACPP
q4_0
Snapdragon®
8 Elite Gen 5
Mobile
4096
12.621046
2.2515993749
- 72.05117999
Phi-4-
Mini-
Instruct
GENIEX_LLAMACPP
q4_0
Snapdragon®
8 Elite Gen 5
Mobile
4096
12.03971
2.4794271875
79.34167
Phi-4-
Mini-
GENIEX_LLAMACPP
q4_0
Snapdragon®
8 Elite Gen 5
4096
11.220493
0.3603361562
11.530757
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
Time To Firs
(range, se
Instruct
Mobile
Phi-4-
Mini-
Instruct
GENIEX_LLAMACPP
q4_0
Snapdragon®
8 Elite Mobile
512
24.055461
0.9468802500
-
3.7875210000
Phi-4-
Mini-
Instruct
GENIEX_LLAMACPP
q4_0
Snapdragon®
8 Elite Mobile
512
23.939526
0.95809125 -
Phi-4-
Mini-
Instruct
GENIEX_LLAMACPP
q4_0
Snapdragon®
8 Elite Mobile
512
19.557942
0.1830165 - 0
Phi-4-
Mini-
Instruct
GENIEX_LLAMACPP
q4_0
Snapdragon®
8 Elite Mobile
4096
13.965758
1.9402748437
62.088795
Phi-4-
Mini-
Instruct
GENIEX_LLAMACPP
q4_0
Snapdragon®
8 Elite Mobile
4096
8.177678
2.3551633124
- 75.36522599
Phi-4-
Mini-
Instruct
GENIEX_LLAMACPP
q4_0
Snapdragon®
8 Elite Mobile
4096
13.116693
0.3528676874
-
11.291765999
Phi-4-
Mini-
Instruct
GENIEX_LLAMACPP
q4_0
Snapdragon®
X2 Elite
512
33.714527
0.2476775000
-
0.9907100000
Phi-4-
Mini-
Instruct
GENIEX_LLAMACPP
q4_0
Snapdragon®
X2 Elite
512
33.35471
0.248513 - 0.9


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
Time To Firs
(range, se
Phi-4-
Mini-
Instruct
GENIEX_LLAMACPP
q4_0
Snapdragon®
X2 Elite
512
22.484254
0.12369325 -
Phi-4-
Mini-
Instruct
GENIEX_LLAMACPP
q4_0
Snapdragon®
X2 Elite
4096
24.554353
0.4478984687
14.332751
Phi-4-
Mini-
Instruct
GENIEX_LLAMACPP
q4_0
Snapdragon®
X2 Elite
4096
24.309187
0.4479129375
14.333214
Phi-4-
Mini-
Instruct
GENIEX_LLAMACPP
q4_0
Snapdragon®
X2 Elite
4096
15.507219
0.1938458437
6.203067
Phi-4-
Mini-
Instruct
GENIEX_LLAMACPP
q4_0
Snapdragon®
X Elite
512
27.988389
0.40832025 -
Phi-4-
Mini-
Instruct
GENIEX_LLAMACPP
q4_0
Snapdragon®
X Elite
512
27.143556
0.46132475 -
Phi-4-
Mini-
Instruct
GENIEX_LLAMACPP
q4_0
Snapdragon®
X Elite
512
16.042448
0.25184725 -
Phi-4-
Mini-
Instruct
GENIEX_LLAMACPP
q4_0
Snapdragon®
X Elite
4096
15.617096
0.913791375
29.241324
Phi-4-
Mini-
Instruct
GENIEX_LLAMACPP
q4_0
Snapdragon®
X Elite
4096
16.000366
0.9590768749
-
30.690459999


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
Time To Firs
(range, se
Phi-4-
Mini-
Instruct
GENIEX_LLAMACPP
q4_0
Snapdragon®
X Elite
4096
9.673267
0.4117405312
13.175697
Phi-4-
Mini-
Instruct
GENIEX_LLAMACPP
q4_0
Qualcomm®
Dragonwing™
IQ-X7181
512
27.988389
0.40832025 -
Phi-4-
Mini-
Instruct
GENIEX_LLAMACPP
q4_0
Qualcomm®
Dragonwing™
IQ-X7181
512
27.143556
0.46132475 -
Phi-4-
Mini-
Instruct
GENIEX_LLAMACPP
q4_0
Qualcomm®
Dragonwing™
IQ-X7181
512
16.042448
0.25184725 -
Phi-4-
Mini-
Instruct
GENIEX_LLAMACPP
q4_0
Qualcomm®
Dragonwing™
Q-8750
512
24.055461
0.9468802500
-
3.7875210000
Phi-4-
Mini-
Instruct
GENIEX_LLAMACPP
q4_0
Qualcomm®
Dragonwing™
Q-8750
512
23.939526
0.95809125 -
Phi-4-
Mini-
Instruct
GENIEX_LLAMACPP
q4_0
Qualcomm®
Dragonwing™
Q-8750
512
19.557942
0.1830165 - 0
Phi-4-
Mini-
Instruct
GENIEX_LLAMACPP
q4_0
Qualcomm®
Dragonwing™
IQ-9075
4096
13.1
1.9971918880
- 63.91014
Phi-4-
Mini-
Instruct
GENIEX_LLAMACPP
q4_0
Qualcomm®
Dragonwing™
IQ-9075
4096
3.0
2.471042471
79.073359


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
Time To Firs
(range, se
Phi-4-
Mini-
Instruct
GENIEX_LLAMACPP
q4_0
Qualcomm®
Dragonwing™
IQ-9075
4096
10.0
0.4413793099
- 14.124138
Phi-4-
Mini-
Instruct
GENIEX_LLAMACPP
q4_0
Qualcomm®
Dragonwing™
IQ-X7181
4096
15.617096
0.913791375
29.241324
Phi-4-
Mini-
Instruct
GENIEX_LLAMACPP
q4_0
Qualcomm®
Dragonwing™
IQ-X7181
4096
16.000366
0.9590768749
-
30.690459999
Phi-4-
Mini-
Instruct
GENIEX_LLAMACPP
q4_0
Qualcomm®
Dragonwing™
IQ-X7181
4096
9.673267
0.4117405312
13.175697
Phi-4-
Mini-
Instruct
GENIEX_LLAMACPP
q4_0
Qualcomm®
Dragonwing™
Q-8750
4096
13.965758
1.9402748437
62.088795
Phi-4-
Mini-
Instruct
GENIEX_LLAMACPP
q4_0
Qualcomm®
Dragonwing™
Q-8750
4096
8.177678
2.3551633124
- 75.36522599
Phi-4-
Mini-
Instruct
GENIEX_LLAMACPP
q4_0
Qualcomm®
Dragonwing™
Q-8750
4096
13.116693
0.3528676874
-
11.291765999
The license for the original implementation of Phi-4-Mini-Instruct can be found
here.
License


Phi-4 Technical Report
Source Model Implementation
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
References
Community
Usage and Limitations


Recommender systems of social media platforms;
Scraping of facial images (from the internet or otherwise); and/or
Subliminal manipulation
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
