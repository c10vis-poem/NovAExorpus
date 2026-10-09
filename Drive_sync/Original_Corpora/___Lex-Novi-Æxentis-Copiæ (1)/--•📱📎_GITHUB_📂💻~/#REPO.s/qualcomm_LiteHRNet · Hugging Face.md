---
title: "qualcomm_LiteHRNet · Hugging Face"
source: "Drive_sync/Original_Corpora/___Lex-Novi-Æxentis-Copiæ (1)/--•📱📎_GITHUB_📂💻~/#REPO.s/qualcomm_LiteHRNet · Hugging Face.pdf"
cleaned: 2026-10-08
converter: "pymupdf get_text via tools/clean.py normalize_markdown"
tags:
  - pdf-conversion
---

Search models, datasets, users...
qualcomm/LiteHRNet
15
Keypoint Detection
PyTorch
android
Model card
Files
Community
like
1.09k
Follow
Qualcomm
arxiv:2104.06403
License: other
xet
Copy to bucket
NEW
Downloads last month
-
Downloads are not tracked for this model. How to track
Inference Providers
Keypoint Detection
This model isn't deployed by any Inference Provider.
🙋Ask for provider support
Paper for qualcomm/LiteHRNet
Lite-HRNet: A Lightweight High-Resolution Network
Paper • 2104.06403 • Published Apr 13, 2021
NEW


LiteHRNet is a machine learning model that detects human pose and returns a location
and confidence for each of 17 joints.
This is based on the implementation of LiteHRNet found here. This repository contains
pre-exported model files optimized for Qualcomm® devices. You can use the
Qualcomm® AI Hub Models library to export with custom configurations. More details
on model performance across various devices, can be found here.
Qualcomm AI Hub Models uses Qualcomm AI Hub Workbench to compile, profile, and
evaluate this model. Sign up to run these models on a hosted Qualcomm® device.
There are two ways to deploy this model on your device:
LiteHRNet: Optimized for Qualcomm Devices
Getting Started
Option 1: Download Pre-Exported Models


Below are pre-exported model assets ready for deployment.
Runtime
Precision
Chipset
SDK Versions
Download
ONNX
float
Universal
QAIRT 2.45, ONNX Runtime 1.27.1
Download
QNN_DLC
float
Universal
QAIRT 2.45
Download
TFLITE
float
Universal
QAIRT 2.45
Download
For more device-specific assets and performance metrics, visit LiteHRNet on
Qualcomm® AI Hub.
Use the Qualcomm® AI Hub Models Python library to compile and export the model
with your own:
Custom weights (e.g., fine-tuned checkpoints)
Custom input shapes
Target device and runtime configurations
This option is ideal if you need to customize the model beyond the default
configuration provided here.
See our repository for LiteHRNet on GitHub for usage instructions.
Model Type: Model_use_case.pose_estimation
Model Stats:
Input resolution: 256x192
Option 2: Export with Custom Configurations
Model Details


Number of parameters: 1.11M
Model size (float): 4.49 MB
Model
Runtime
Precision
Chipset
Inference
Time (ms)
Peak
Memory
Range
(MB)
Primary
Compute
Unit
LiteHRNet
ONNX
float
Snapdragon® X2
Elite
2.842 ms
2 - 2 MB
NPU
LiteHRNet
ONNX
float
Snapdragon® X
Elite
5.61 ms
5 - 5 MB
NPU
LiteHRNet
ONNX
float
Snapdragon® 8
Gen 3 Mobile
3.063 ms
0 - 121 MB
NPU
LiteHRNet
ONNX
float
Snapdragon® 8
Gen 1 Mobile
6.228 ms
1 - 120 MB
NPU
LiteHRNet
ONNX
float
Qualcomm®
Dragonwing™
QCS8550 (Proxy)
5.338 ms
0 - 123 MB
NPU
LiteHRNet
ONNX
float
Qualcomm®
QCS8450
6.228 ms
1 - 120 MB
NPU
LiteHRNet
ONNX
float
Qualcomm®
Dragonwing™ IQ-
9075
5.679 ms
1 - 4 MB
NPU
LiteHRNet
ONNX
float
Qualcomm®
Dragonwing™ IQ-
X7181
5.61 ms
5 - 5 MB
NPU
LiteHRNet
ONNX
float
Qualcomm®
Dragonwing™ Q-
2.835 ms
0 - 95 MB
NPU
Performance Summary


Model
Runtime
Precision
Chipset
Inference
Time (ms)
Peak
Memory
Range
(MB)
Primary
Compute
Unit
8750
LiteHRNet
ONNX
float
Snapdragon® 8
Elite Mobile
2.835 ms
0 - 95 MB
NPU
LiteHRNet
ONNX
float
Snapdragon® 8
Elite Gen 5
Mobile
2.738 ms
0 - 96 MB
NPU
LiteHRNet
QNN_DLC
float
Snapdragon® X2
Elite
1.23 ms
1 - 1 MB
NPU
LiteHRNet
QNN_DLC
float
Snapdragon® X
Elite
2.365 ms
1 - 1 MB
NPU
LiteHRNet
QNN_DLC
float
Snapdragon® 8
Gen 3 Mobile
1.346 ms
0 - 105 MB
NPU
LiteHRNet
QNN_DLC
float
Snapdragon® 8
Gen 1 Mobile
2.859 ms
0 - 103 MB
NPU
LiteHRNet
QNN_DLC
float
Qualcomm®
Dragonwing™
QCS8275
4.96 ms
1 - 78 MB
NPU
LiteHRNet
QNN_DLC
float
Qualcomm®
Dragonwing™
QCS8550 (Proxy)
2.062 ms
1 - 2 MB
NPU
LiteHRNet
QNN_DLC
float
Qualcomm®
SA8775P
2.651 ms
1 - 80 MB
NPU
LiteHRNet
QNN_DLC
float
Qualcomm®
SA8650P
2.651 ms
1 - 80 MB
NPU
LiteHRNet
QNN_DLC
float
Qualcomm®
SA8255P
2.651 ms
1 - 80 MB
NPU


Model
Runtime
Precision
Chipset
Inference
Time (ms)
Peak
Memory
Range
(MB)
Primary
Compute
Unit
LiteHRNet
QNN_DLC
float
Qualcomm®
QCS8450
2.859 ms
0 - 103 MB
NPU
LiteHRNet
QNN_DLC
float
Qualcomm®
Dragonwing™ IQ-
9075
3.237 ms
3 - 5 MB
NPU
LiteHRNet
QNN_DLC
float
Qualcomm®
Dragonwing™ IQ-
X7181
2.365 ms
1 - 1 MB
NPU
LiteHRNet
QNN_DLC
float
Qualcomm®
Dragonwing™ Q-
8750
1.023 ms
0 - 83 MB
NPU
LiteHRNet
QNN_DLC
float
Qualcomm®
SA7255P
4.96 ms
1 - 78 MB
NPU
LiteHRNet
QNN_DLC
float
Qualcomm®
SA8295P
3.427 ms
0 - 81 MB
NPU
LiteHRNet
QNN_DLC
float
Snapdragon® 8
Elite Mobile
1.023 ms
0 - 83 MB
NPU
LiteHRNet
QNN_DLC
float
Snapdragon® 8
Elite Gen 5
Mobile
0.875 ms
1 - 82 MB
NPU
LiteHRNet
TFLITE
float
Snapdragon® 8
Gen 3 Mobile
2.635 ms
0 - 150 MB
NPU
LiteHRNet
TFLITE
float
Snapdragon® 8
Gen 1 Mobile
5.227 ms
0 - 137 MB
NPU


Model
Runtime
Precision
Chipset
Inference
Time (ms)
Peak
Memory
Range
(MB)
Primary
Compute
Unit
LiteHRNet
TFLITE
float
Qualcomm®
Dragonwing™
QCS8275
8.495 ms
0 - 115 MB
NPU
LiteHRNet
TFLITE
float
Qualcomm®
Dragonwing™
QCS8550 (Proxy)
4.158 ms
0 - 2 MB
NPU
LiteHRNet
TFLITE
float
Qualcomm®
SA8775P
5.116 ms
0 - 114 MB
NPU
LiteHRNet
TFLITE
float
Qualcomm®
SA8650P
5.116 ms
0 - 114 MB
NPU
LiteHRNet
TFLITE
float
Qualcomm®
SA8255P
5.116 ms
0 - 114 MB
NPU
LiteHRNet
TFLITE
float
Qualcomm®
QCS8450
5.227 ms
0 - 137 MB
NPU
LiteHRNet
TFLITE
float
Qualcomm®
Dragonwing™ IQ-
9075
4.702 ms
0 - 10 MB
NPU
LiteHRNet
TFLITE
float
Qualcomm®
Dragonwing™ Q-
8750
2.196 ms
0 - 117 MB
NPU
LiteHRNet
TFLITE
float
Qualcomm®
SA7255P
8.495 ms
0 - 115 MB
NPU
LiteHRNet
TFLITE
float
Qualcomm®
SA8295P
6.207 ms
0 - 112 MB
NPU
LiteHRNet
TFLITE
float
Snapdragon® 8
Elite Mobile
2.196 ms
0 - 117 MB
NPU


Model
Runtime
Precision
Chipset
Inference
Time (ms)
Peak
Memory
Range
(MB)
Primary
Compute
Unit
LiteHRNet
TFLITE
float
Snapdragon® 8
Elite Gen 5
Mobile
2.014 ms
0 - 111 MB
NPU
The license for the original implementation of LiteHRNet can be found here.
Lite-HRNet: A Lightweight High-Resolution Network
Source Model Implementation
Join our AI Hub Slack community to collaborate, post questions and learn more
about on-device AI.
For questions or feedback please reach out to us.
License
References
Community


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
