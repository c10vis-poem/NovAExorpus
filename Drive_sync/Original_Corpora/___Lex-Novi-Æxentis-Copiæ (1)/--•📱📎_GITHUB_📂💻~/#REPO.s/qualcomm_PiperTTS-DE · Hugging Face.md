---
title: "qualcomm_PiperTTS-DE · Hugging Face"
source: "Drive_sync/Original_Corpora/___Lex-Novi-Æxentis-Copiæ (1)/--•📱📎_GITHUB_📂💻~/#REPO.s/qualcomm_PiperTTS-DE · Hugging Face.pdf"
cleaned: 2026-10-08
converter: "pymupdf get_text via tools/clean.py normalize_markdown"
tags:
  - pdf-conversion
---

Search models, datasets, users...
qualcomm/PiperTTS-DE
0
Text-to-Audio
PyTorch
real_time
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
Text-to-Audio
This model isn't deployed by any Inference Provider.
🙋Ask for provider support
Edit model card
Inference Providers
NEW


PiperTTS is a high-quality multi-lingual text-to-speech library.
This is based on the implementation of PiperTTS-DE found here. This repository
contains pre-exported model files optimized for Qualcomm® devices. You can use the
Qualcomm® AI Hub Models library to export with custom configurations. More details
on model performance across various devices, can be found here.
Qualcomm AI Hub Models uses Qualcomm AI Hub Workbench to compile, profile, and
evaluate this model. Sign up to run these models on a hosted Qualcomm® device.
There are two ways to deploy this model on your device:
Below are pre-exported model assets ready for deployment.
PiperTTS-DE: Optimized for Qualcomm Devices
Getting Started
Option 1: Download Pre-Exported Models


Runtime
Precision
Chipset
SDK
Versions
Download
VOICE_AI
float
Snapdragon® X2 Elite
QAIRT 2.45
Download
VOICE_AI
float
Snapdragon® X Elite
QAIRT 2.45
Download
VOICE_AI
float
Snapdragon® 8 Gen 3 Mobile
QAIRT 2.45
Download
VOICE_AI
float
Snapdragon® 8 Gen 1 Mobile
QAIRT 2.45
Download
VOICE_AI
float
Qualcomm® Dragonwing™ QCS8550
(Proxy)
QAIRT 2.45
Download
VOICE_AI
float
Qualcomm® SA8775P
QAIRT 2.45
Download
VOICE_AI
float
Qualcomm® Dragonwing™ IQ-9075
QAIRT 2.45
Download
VOICE_AI
float
Qualcomm® SA7255P
QAIRT 2.45
Download
VOICE_AI
float
Qualcomm® SA8295P
QAIRT 2.45
Download
VOICE_AI
float
Snapdragon® 8 Elite Mobile
QAIRT 2.45
Download
VOICE_AI
float
Snapdragon® 8 Elite Gen 5 Mobile
QAIRT 2.45
Download
For more device-specific assets and performance metrics, visit PiperTTS-DE on
Qualcomm® AI Hub.
Use the Qualcomm® AI Hub Models Python library to compile and export the model
with your own:
Custom weights (e.g., fine-tuned checkpoints)
Custom input shapes
Target device and runtime configurations
Option 2: Export with Custom Configurations


This option is ideal if you need to customize the model beyond the default
configuration provided here.
See our repository for PiperTTS-DE on GitHub for usage instructions.
Model Type: Model_use_case.audio_generation
Model Stats:
Model checkpoint: rhasspy/piper-checkpoints
Max decoded sequence length: 64 tokens
Number of parameters (encoder): 7.51M
Model size (encoder) (float): 28.7 MB
Number of parameters (sdp): 1.04K
Model size (sdp) (float): 6.61 KB
Number of parameters (flow): 7.39M
Model size (flow) (float): 28.2 MB
Number of parameters (decoder): 1.66M
Model size (decoder) (float): 6.37 MB
Number of parameters (t5_encoder): 15.1M
Model size (t5_encoder) (float): 57.5 MB
Number of parameters (t5_decoder): 5.72M
Model size (t5_decoder) (float): 21.8 MB
Model Details
Performance Summary


Model
Runtime
Precision
Chipset
Inference
Time
(ms)
Peak
Memory
Range
(MB)
Primary
Compute
Unit
charsiu_decoder
VOICE_AI
float
Snapdragon®
X2 Elite
0.34 ms
1 - 1 MB
NPU
charsiu_decoder
VOICE_AI
float
Snapdragon®
X Elite
0.411 ms
1 - 1 MB
NPU
charsiu_decoder
VOICE_AI
float
Snapdragon®
8 Gen 3 Mobile
0.309 ms
0 - 8 MB
NPU
charsiu_decoder
VOICE_AI
float
Snapdragon®
8 Gen 1 Mobile
0.573 ms
1 - 10 MB
NPU
charsiu_decoder
VOICE_AI
float
Qualcomm®
Dragonwing™
QCS8275
0.997 ms
0 - 9 MB
NPU
charsiu_decoder
VOICE_AI
float
Qualcomm®
Dragonwing™
QCS8550
(Proxy)
0.399 ms
0 - 3 MB
NPU
charsiu_decoder
VOICE_AI
float
Qualcomm®
SA8775P
0.653 ms
0 - 10 MB
NPU
charsiu_decoder
VOICE_AI
float
Qualcomm®
SA8650P
0.653 ms
0 - 10 MB
NPU
charsiu_decoder
VOICE_AI
float
Qualcomm®
SA8255P
0.653 ms
0 - 10 MB
NPU
charsiu_decoder
VOICE_AI
float
Qualcomm®
QCS8450
0.573 ms
1 - 10 MB
NPU
charsiu_decoder
VOICE_AI
float
Qualcomm®
Dragonwing™
0.52 ms
1 - 3 MB
NPU


Model
Runtime
Precision
Chipset
Inference
Time
(ms)
Peak
Memory
Range
(MB)
Primary
Compute
Unit
IQ-9075
charsiu_decoder
VOICE_AI
float
Qualcomm®
Dragonwing™
IQ-X7181
0.411 ms
1 - 1 MB
NPU
charsiu_decoder
VOICE_AI
float
Qualcomm®
Dragonwing™
Q-8750
0.28 ms
0 - 13 MB
NPU
charsiu_decoder
VOICE_AI
float
Qualcomm®
SA7255P
0.997 ms
0 - 9 MB
NPU
charsiu_decoder
VOICE_AI
float
Qualcomm®
SA8295P
0.802 ms
0 - 6 MB
NPU
charsiu_decoder
VOICE_AI
float
Snapdragon®
8 Elite Mobile
0.28 ms
0 - 13 MB
NPU
charsiu_decoder
VOICE_AI
float
Snapdragon®
8 Elite Gen 5
Mobile
0.261 ms
0 - 10 MB
NPU
charsiu_encoder
VOICE_AI
float
Snapdragon®
X2 Elite
0.67 ms
0 - 0 MB
NPU
charsiu_encoder
VOICE_AI
float
Snapdragon®
X Elite
1.062 ms
0 - 0 MB
NPU
charsiu_encoder
VOICE_AI
float
Snapdragon®
8 Gen 3 Mobile
0.637 ms
0 - 8 MB
NPU
charsiu_encoder
VOICE_AI
float
Snapdragon®
8 Gen 1 Mobile
1.344 ms
0 - 9 MB
NPU
charsiu_encoder
VOICE_AI
float
Qualcomm®
Dragonwing™
2.791 ms
0 - 9 MB
NPU


Model
Runtime
Precision
Chipset
Inference
Time
(ms)
Peak
Memory
Range
(MB)
Primary
Compute
Unit
QCS8275
charsiu_encoder
VOICE_AI
float
Qualcomm®
Dragonwing™
QCS8550
(Proxy)
0.873 ms
0 - 1 MB
NPU
charsiu_encoder
VOICE_AI
float
Qualcomm®
SA8775P
1.265 ms
0 - 10 MB
NPU
charsiu_encoder
VOICE_AI
float
Qualcomm®
SA8650P
1.265 ms
0 - 10 MB
NPU
charsiu_encoder
VOICE_AI
float
Qualcomm®
SA8255P
1.265 ms
0 - 10 MB
NPU
charsiu_encoder
VOICE_AI
float
Qualcomm®
QCS8450
1.344 ms
0 - 9 MB
NPU
charsiu_encoder
VOICE_AI
float
Qualcomm®
Dragonwing™
IQ-9075
1.12 ms
0 - 2 MB
NPU
charsiu_encoder
VOICE_AI
float
Qualcomm®
Dragonwing™
IQ-X7181
1.062 ms
0 - 0 MB
NPU
charsiu_encoder
VOICE_AI
float
Qualcomm®
Dragonwing™
Q-8750
0.527 ms
0 - 13 MB
NPU
charsiu_encoder
VOICE_AI
float
Qualcomm®
SA7255P
2.791 ms
0 - 9 MB
NPU
charsiu_encoder
VOICE_AI
float
Qualcomm®
SA8295P
1.74 ms
0 - 6 MB
NPU


Model
Runtime
Precision
Chipset
Inference
Time
(ms)
Peak
Memory
Range
(MB)
Primary
Compute
Unit
charsiu_encoder
VOICE_AI
float
Snapdragon®
8 Elite Mobile
0.527 ms
0 - 13 MB
NPU
charsiu_encoder
VOICE_AI
float
Snapdragon®
8 Elite Gen 5
Mobile
0.489 ms
0 - 9 MB
NPU
decoder
VOICE_AI
float
Snapdragon®
X2 Elite
1.741 ms
0 - 0 MB
NPU
decoder
VOICE_AI
float
Snapdragon®
X Elite
3.071 ms
0 - 0 MB
NPU
decoder
VOICE_AI
float
Snapdragon®
8 Gen 3 Mobile
2.201 ms
0 - 8 MB
NPU
decoder
VOICE_AI
float
Snapdragon®
8 Gen 1 Mobile
4.395 ms
0 - 9 MB
NPU
decoder
VOICE_AI
float
Qualcomm®
Dragonwing™
QCS8275
8.069 ms
0 - 9 MB
NPU
decoder
VOICE_AI
float
Qualcomm®
Dragonwing™
QCS8550
(Proxy)
3.02 ms
0 - 1 MB
NPU
decoder
VOICE_AI
float
Qualcomm®
SA8775P
3.49 ms
0 - 10 MB
NPU
decoder
VOICE_AI
float
Qualcomm®
SA8650P
3.49 ms
0 - 10 MB
NPU
decoder
VOICE_AI
float
Qualcomm®
SA8255P
3.49 ms
0 - 10 MB
NPU


Model
Runtime
Precision
Chipset
Inference
Time
(ms)
Peak
Memory
Range
(MB)
Primary
Compute
Unit
decoder
VOICE_AI
float
Qualcomm®
QCS8450
4.395 ms
0 - 9 MB
NPU
decoder
VOICE_AI
float
Qualcomm®
Dragonwing™
IQ-9075
3.33 ms
0 - 2 MB
NPU
decoder
VOICE_AI
float
Qualcomm®
Dragonwing™
IQ-X7181
3.071 ms
0 - 0 MB
NPU
decoder
VOICE_AI
float
Qualcomm®
Dragonwing™
Q-8750
1.897 ms
0 - 12 MB
NPU
decoder
VOICE_AI
float
Qualcomm®
SA7255P
8.069 ms
0 - 9 MB
NPU
decoder
VOICE_AI
float
Qualcomm®
SA8295P
3.945 ms
0 - 6 MB
NPU
decoder
VOICE_AI
float
Snapdragon®
8 Elite Mobile
1.897 ms
0 - 12 MB
NPU
decoder
VOICE_AI
float
Snapdragon®
8 Elite Gen 5
Mobile
1.827 ms
0 - 8 MB
NPU
encoder
VOICE_AI
float
Snapdragon®
X2 Elite
18.626 ms
0 - 0 MB
NPU
encoder
VOICE_AI
float
Snapdragon®
X Elite
29.667 ms
0 - 0 MB
NPU
encoder
VOICE_AI
float
Snapdragon®
8 Gen 3 Mobile
23.636 ms
0 - 7 MB
NPU


Model
Runtime
Precision
Chipset
Inference
Time
(ms)
Peak
Memory
Range
(MB)
Primary
Compute
Unit
encoder
VOICE_AI
float
Snapdragon®
8 Gen 1 Mobile
38.309 ms
1 - 10 MB
NPU
encoder
VOICE_AI
float
Qualcomm®
Dragonwing™
QCS8275
46.989 ms
0 - 10 MB
NPU
encoder
VOICE_AI
float
Qualcomm®
Dragonwing™
QCS8550
(Proxy)
30.389 ms
0 - 2 MB
NPU
encoder
VOICE_AI
float
Qualcomm®
SA8775P
33.088 ms
0 - 10 MB
NPU
encoder
VOICE_AI
float
Qualcomm®
SA8650P
33.088 ms
0 - 10 MB
NPU
encoder
VOICE_AI
float
Qualcomm®
SA8255P
33.088 ms
0 - 10 MB
NPU
encoder
VOICE_AI
float
Qualcomm®
QCS8450
38.309 ms
1 - 10 MB
NPU
encoder
VOICE_AI
float
Qualcomm®
Dragonwing™
IQ-9075
32.283 ms
2 - 5 MB
NPU
encoder
VOICE_AI
float
Qualcomm®
Dragonwing™
IQ-X7181
29.667 ms
0 - 0 MB
NPU
encoder
VOICE_AI
float
Qualcomm®
Dragonwing™
Q-8750
18.973 ms
0 - 8 MB
NPU


Model
Runtime
Precision
Chipset
Inference
Time
(ms)
Peak
Memory
Range
(MB)
Primary
Compute
Unit
encoder
VOICE_AI
float
Qualcomm®
SA7255P
46.989 ms
0 - 10 MB
NPU
encoder
VOICE_AI
float
Qualcomm®
SA8295P
35.241 ms
0 - 6 MB
NPU
encoder
VOICE_AI
float
Snapdragon®
8 Elite Mobile
18.973 ms
0 - 8 MB
NPU
encoder
VOICE_AI
float
Snapdragon®
8 Elite Gen 5
Mobile
17.116 ms
0 - 9 MB
NPU
flow
VOICE_AI
float
Snapdragon®
X2 Elite
9.679 ms
4 - 4 MB
NPU
flow
VOICE_AI
float
Snapdragon®
X Elite
15.874 ms
4 - 4 MB
NPU
flow
VOICE_AI
float
Snapdragon®
8 Gen 3 Mobile
11.076 ms
4 - 12 MB
NPU
flow
VOICE_AI
float
Snapdragon®
8 Gen 1 Mobile
18.261 ms
4 - 13 MB
NPU
flow
VOICE_AI
float
Qualcomm®
Dragonwing™
QCS8275
39.518 ms
1 - 10 MB
NPU
flow
VOICE_AI
float
Qualcomm®
Dragonwing™
QCS8550
(Proxy)
15.032 ms
4 - 5 MB
NPU
flow
VOICE_AI
float
Qualcomm®
SA8775P
17.273 ms
1 - 10 MB
NPU


Model
Runtime
Precision
Chipset
Inference
Time
(ms)
Peak
Memory
Range
(MB)
Primary
Compute
Unit
flow
VOICE_AI
float
Qualcomm®
SA8650P
17.273 ms
1 - 10 MB
NPU
flow
VOICE_AI
float
Qualcomm®
SA8255P
17.273 ms
1 - 10 MB
NPU
flow
VOICE_AI
float
Qualcomm®
QCS8450
18.261 ms
4 - 13 MB
NPU
flow
VOICE_AI
float
Qualcomm®
Dragonwing™
IQ-9075
17.415 ms
4 - 10 MB
NPU
flow
VOICE_AI
float
Qualcomm®
Dragonwing™
IQ-X7181
15.874 ms
4 - 4 MB
NPU
flow
VOICE_AI
float
Qualcomm®
Dragonwing™
Q-8750
8.942 ms
1 - 10 MB
NPU
flow
VOICE_AI
float
Qualcomm®
SA7255P
39.518 ms
1 - 10 MB
NPU
flow
VOICE_AI
float
Qualcomm®
SA8295P
18.898 ms
0 - 6 MB
NPU
flow
VOICE_AI
float
Snapdragon®
8 Elite Mobile
8.942 ms
1 - 10 MB
NPU
flow
VOICE_AI
float
Snapdragon®
8 Elite Gen 5
Mobile
8.975 ms
3 - 11 MB
NPU
sdp
VOICE_AI
float
Snapdragon®
X2 Elite
7.147 ms
0 - 0 MB
NPU


Model
Runtime
Precision
Chipset
Inference
Time
(ms)
Peak
Memory
Range
(MB)
Primary
Compute
Unit
sdp
VOICE_AI
float
Snapdragon®
X Elite
11.333 ms
0 - 0 MB
NPU
sdp
VOICE_AI
float
Snapdragon®
8 Gen 3 Mobile
7.696 ms
0 - 8 MB
NPU
sdp
VOICE_AI
float
Snapdragon®
8 Gen 1 Mobile
11.179 ms
0 - 10 MB
NPU
sdp
VOICE_AI
float
Qualcomm®
Dragonwing™
QCS8275
20.547 ms
0 - 9 MB
NPU
sdp
VOICE_AI
float
Qualcomm®
Dragonwing™
QCS8550
(Proxy)
10.414 ms
0 - 2 MB
NPU
sdp
VOICE_AI
float
Qualcomm®
SA8775P
11.102 ms
0 - 10 MB
NPU
sdp
VOICE_AI
float
Qualcomm®
SA8650P
11.102 ms
0 - 10 MB
NPU
sdp
VOICE_AI
float
Qualcomm®
SA8255P
11.102 ms
0 - 10 MB
NPU
sdp
VOICE_AI
float
Qualcomm®
QCS8450
11.179 ms
0 - 10 MB
NPU
sdp
VOICE_AI
float
Qualcomm®
Dragonwing™
IQ-9075
11.25 ms
2 - 4 MB
NPU


Model
Runtime
Precision
Chipset
Inference
Time
(ms)
Peak
Memory
Range
(MB)
Primary
Compute
Unit
sdp
VOICE_AI
float
Qualcomm®
Dragonwing™
IQ-X7181
11.333 ms
0 - 0 MB
NPU
sdp
VOICE_AI
float
Qualcomm®
Dragonwing™
Q-8750
6.956 ms
0 - 10 MB
NPU
sdp
VOICE_AI
float
Qualcomm®
SA7255P
20.547 ms
0 - 9 MB
NPU
sdp
VOICE_AI
float
Qualcomm®
SA8295P
12.668 ms
0 - 6 MB
NPU
sdp
VOICE_AI
float
Snapdragon®
8 Elite Mobile
6.956 ms
0 - 10 MB
NPU
sdp
VOICE_AI
float
Snapdragon®
8 Elite Gen 5
Mobile
6.608 ms
0 - 9 MB
NPU
The license for the original implementation of PiperTTS-DE can be found here.
PiperTTS High-quality Multi-lingual Multi-accent Text-to-Speech
Source Model Implementation
License
References
Community


Join our AI Hub Slack community to collaborate, post questions and learn more
about on-device AI.
For questions or feedback please reach out to us.
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
