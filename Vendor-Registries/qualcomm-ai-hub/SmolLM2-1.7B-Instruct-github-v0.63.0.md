<!-- Converted from ai-hub-models_src_qai_hub_models_models_smollm2_1_7b_it_README.md at v0.63.0 · qualcomm_ai-hub-models.pdf — 4 pages -->

## Page 1

qualcomm ai-hub-models
Code Issues Pull requests 8 Agents Actions Security and quality Insights
v0.63.0
ai-hub-models / src / qai_ hub_ models / models / smollm2_ 1_ 7b_ it / README.md
Akshaya Nagarajan (… [TETRAAI-425] Fix and Update Scorecard Run for SmolLM2-1.7B-Instruct …
671590e · last week
116 lines (90 loc) · 5.39 KB
Preview Code Blame Raw
## SmolLM2-1.7B-Instruct: Compact language
## model capable of solving a wide range of tasks
## while being lightweight
A 1.7B parameter instruction-tuned variant of SmolLM2, fine-tuned for conversational and instruction-following tasks, optimized for efficient on-device inference on Qualcomm Snapdragon platforms.
This is based on the implementation of SmolLM2-1.7B-Instruct found here. This repository contains scripts for optimized on-device export suitable to run on Qualcomm® devices. More details on model performance across various devices, can be found here.
Qualcomm AI Hub Models uses Qualcomm AI Hub Workbench to compile, profile, and evaluate this model. Sign up to run these models on a hosted Qualcomm® device.
### Quick Start
Use our lightweight command-line interface to inspect and download SmolLM2-1.7B-Instruct:
pip install qai_hub_models_cli # (the CLI is also available with the qai-hub-
# Inspect the model and list the available download options

---

## Page 2

qai-hub-models info SmolLM2-1.7B-Instruct
# Print performance and accuracy metrics qai-hub-models perf SmolLM2-1.7B-Instruct qai-hub-models numerics SmolLM2-1.7B-Instruct
# Download a ready-to-deploy asset qai-hub-models fetch SmolLM2-1.7B-Instruct --runtime geniex_qairt --precision
See the CLI README for the full list of commands and filters.
## Deploying SmolLM2-1.7B-Instruct on-device
Follow the GenieX quickstart to install GenieX and deploy the model on a target device.
See the LLM-on-Genie tutorial to run with the Genie runtime. Note: Genie support will be deprecated soon.
## Setup
## 1. Install the package
Install the base package, then use the qai-hub-models CLI to install this recipe's
dependencies:
# NOTE: 3.10 <= PYTHON_VERSION < 3.14 is supported. pip install qai-hub-models qai-hub-models install smollm2_1_7b_it
## 2. Configure Qualcomm® AI Hub Workbench
Account -> Settings -> API Token .
With this API token, you can configure your client to run models on the cloud hosted devices.
qai-hub configure --api_token API_TOKEN
Navigate to docs for more information.

---

## Page 3

## Run CLI Demo
Run the following simple CLI demo to verify the model is working end to end:
qai-hub-models demo smollm2_1_7b_it
More details on the CLI tool can be found with the --help option. See demo.py for sample
usage of the model including pre/post processing scripts. Please refer to our general instructions on using models for more usage instructions.
## Export for on-device deployment
To run the model on Qualcomm® devices, you must export the model for use with an edge runtime such as TensorFlow Lite, ONNX Runtime, or Qualcomm AI Engine Direct. Export the pre-quantized model (published on AI Hub) for on-device deployment:
qai-hub-models export smollm2_1_7b_it --checkpoint DEFAULT_W4A16
--checkpoint also accepts DEFAULT (the model's default precision).
Optionally, quantize your own variant first and export the resulting checkpoint:
python -m qai_hub_models.models.smollm2_1_7b_it.quantize --precision w4a16 --qai-hub-models export smollm2_1_7b_it --checkpoint ./quantized_checkpoint
Additional options are documented with the --help option.
## License
The license for the original implementation of SmolLM2-1.7B-Instruct can be found here.
## References
SmolLM2: When Smol Goes Big -- Data-Centric Training of a Small Language Model
Source Model Implementation
## Community

---

## Page 4

Join our AI Hub Slack community to collaborate, post questions and learn more about on-device AI.
For questions or feedback please reach out to us.
### Usage and Limitations
This model may not be used for or in connection with any of the following applications:
Accessing essential private and public services and benefits;
Administration of justice and democratic processes;
Assessing or recognizing the emotional state of a person;
Biometric and biometrics-based systems, including categorization of persons based on sensitive characteristics;
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