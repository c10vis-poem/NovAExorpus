# Run LLMs using LiteRT-LM  _  Google AI Edge  _  Google for Developers

Introducing Google AI Edge Portal (https://ai.google.dev/edge/ai-edge-portal): Benchmark Edge AI at scale. Sign-
up
(https://docs.google.com/forms/d/e/1FAIpQLSfTcGPycQve8TLAsfH46pBlXBZe9FrgJAClwbF7DeL1LgVn4Q/viewf
orm)
to request access during private preview.
Run LLMs using LiteRT-LM
LiteRT-LM is a cross-platform library designed to efficiently run language model pipelines on a wide
range of devices, from mobile phones to embedded systems. It provides developers with the tools to
create and deploy sophisticated language model workflows, now with seamless NPU integration.
Run LLMs on CPU and GPU
See LiteRT-LM GitHub repo (https://github.com/google-ai-edge/LiteRT-LM) for detailed instructions on
cross-platform development and CPU/GPU hardware acceleration.
Run LLMs on NPU
Neural Processing Units (NPUs) offer specialized hardware blocks optimized for deep learning
workloads. They are increasingly available in modern systems on a chip (SoCs), especially on mobile
devices. Their high-performing nature makes them a great fit for running LLM inference.
NPU Vendors
LiteRT-LM supports running LLMs using NPU acceleration with the following vendors. Choose the
instructions depending on which vendor you would like to try:
Google Tensor (#tensor)
Qualcomm AI Engine Direct (#qualcomm)
MediaTek NeuroPilot (#mediatek)
Intel OpenVino (#intel)
content_copy arrow_drop_down


Quick Start
To get started, first follow the Prerequisites
(https://github.com/google-ai-edge/LiteRT-LM?tab=readme-ov-file#prerequisites) instructions to set up the
environment and the repository.
Also, to be able to interact with your Android device, make sure you've properly installed Android
Debug Bridge (https://developer.android.com/tools/adb) and have a connected device that can be
accessed using adb.
For more details instructions, checkout the Quick Start
(https://github.com/google-ai-edge/LiteRT-LM?tab=readme-ov-file#quick-start) section in the LiteRT-LM
(https://github.com/google-ai-edge/LiteRT-LM) repository and find more information about the
litert_lm_main command line demo
(https://github.com/google-ai-edge/LiteRT-LM?tab=readme-ov-file#command-line-demo-usage-).
Google Tensor
Follow these steps to run LLMs on Google Tensor:
Step 1: Download the .litertlm model
Step 2: Build the LiteRT-LM runtime / libraries
Step 3: Run the model on device
Qualcomm AI Engine Direct
The steps to run the LLMs on Qualcomm NPU are as the following:
Step 1: Download the .litertlm model
Step 2: Download and extract the QAIRT libraries
Step 3: Build the LiteRT-LM runtime / libraries
Step 4: Run the model on device
MediaTek NeuroPilot
The steps to run the LLMs on MediaTek NPU are as the following:


Step 1: Download the .litertlm model
Step 2: Build the LiteRT-LM runtime / libraries
Step 3: Run the model on device
Intel OpenVino
Run using the C++ executable
The steps to run the LLMs on Intel NPU are as the following:
Step 1: Download the .litertlm model
Step 2: Build the LiteRT-LM runtime and LiteRT Intel Dispatch library
Step 3: Run the model on device
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License
(https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the Apache 2.0 License
(https://www.apache.org/licenses/LICENSE-2.0). For details, see the Google Developers Site Policies
(https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2026-06-12 UTC.
