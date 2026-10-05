# c10vis-poem／reasoning-bank

Watch
0
Apache License 2.0
Contributing
0 stars
0 forks
0 watching
1 branch
0 tags
Activity
Public repository · Forked from google-research/reasoning-bank
1 Branch
0 Tags
Go to file
Go to file
Add file
Code
This branch is up to date with google-research/reasoning-bank:main .
Contribute
Sync fork
junyann Update BibTeX
ed80611 · 2 months ago
SWE-Bench
Initial commit for ReasoningBank OSS…
5 months ago
WebArena
Clean webarena_patch and expand .gi…
3 months ago
assets
Initial commit for ReasoningBank OSS…
5 months ago
third_party
Clean webarena_patch and expand .gi…
3 months ago
.gitignore
Clean webarena_patch and expand .gi…
3 months ago
.python-version
Update autoeval and memory inductio…
3 months ago
CONTRIBUTING.md
Initial commit for ReasoningBank OSS…
5 months ago
LICENSE
Initial commit for ReasoningBank OSS…
5 months ago
README.md
Update BibTeX
2 months ago
main.py
Update autoeval and memory inductio…
3 months ago
pyproject.toml
Update autoeval and memory inductio…
3 months ago
uv.lock
Update autoeval and memory inductio…
3 months ago
c10vis-poem
reasoning-bank
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
T
ReasoningBank: Scaling Agent Self-Evolving with
Reasoning Memory
README
Contributing
License


We introduce ReasoningBank, a memory mechanism for agents that learns from both successful and failed
trajectories, with reasoning stored as memory content.
Building upon this memory formulation, we propose memory-aware test-time scaling, which leverages the
bidirectional synergy between memory and test-time scaling, establishing experience-driven memory as another
scaling dimension for agent systems.
We release code for SWE-Bench (software engineering) and WebArena (web-browsing), as in corresponding
directories.
Before we start, please install required packages by running pip install -r requirements.txt .
Currently we support three model families:
GPT: To use GPT models ( gpt-3.5-turbo , gpt-4 , gpt-4o ), you need to set your OpenAI API key as an
environment variable:
Gemini & Claude: To use Gemini models ( gemini-2.5-flash , gemini-2.5-pro ) or Claude ( claude-3-7-
sonnet@20250219 ) on Vertex AI, you need to configure Google Cloud authentication.
i. Install the Google Cloud CLI and log in to set up Application Default Credentials (ADC):
📜 Overview
📂 Code Setup
0. LLM Configuration
export OPENAI_API_KEY="your-openai-api-key"


ii. Set your project and location as environment variables, as they are required by clients like the one for
Claude on Vertex AI:
Make sure to correctly install browsergym following the official documentation.
The next step is to download and config docker environment for WebArena. Please refer to this tutorial, executing
the scripts follow the numerical order of file names. Before executing, make sure to config the address of each
website in corresponding scripts as instructed correspondingly.
WebArena/agents/ : implementation for web agents integrating with browsergym
WebArena/autoeval/ : llm-as-a-judge for obtaining correctness signal for trajectories
WebArena/config_files/ : data processing for webarena tasks
WebArena/prompt/ : instructions used across the implementation
Download raw test files from here and put it to config_files . The repo also vendors a patched copy at
third_party/webarena/test.raw.json with shopping-split annotation corrections; use either one.
Run generate_config_files.py to process raw test data to config files as input.
The repo ships a patched webarena/ harness at third_party/webarena/ (corrected shopping annotations,
wishlist eval fix, fill('','') guard, retry_with_force=True clicks) to make environment and corresponding
evaluation more robust and stable. Prepend it to PYTHONPATH so it shadows the pip-installed
browsergym.webarena :
webarena is a namespace package, so no code edits are required — every webarena.* submodule resolves to
the vendored copy.
Run directly with ReasoningBank: bash run.sh , config model , output_dir , and website , and memory_mode
accordingly.
To run with scaling setting, please refer to pipeline_scaling.py and induce_scaling.py .
gcloud auth application-default login
export GOOGLE_CLOUD_PROJECT="your-project-id"
export GOOGLE_CLOUD_LOCATION="your-region"
export GOOGLE_GENAI_USE_VERTEXAI="True"
1. WebArena
Docker Configuration
Directory Structure
Data preprocessing
Use the vendored webarena tree
export PYTHONPATH="$(pwd)/third_party:$PYTHONPATH"
Run the code


We built upon mini-swe-agent. First, install it from source by pip install -e . under the directory of
./third_party This will install the dependencies as specified in pyproject.toml .
The script SWE-Bench/run.sh provides direct running command, which will generate result files in the output
directory. Before running, make sure the configuration for VertexAI is properly configured as instructed in run.sh .
For evaluation, please refer to sb-cli command in the official documentation.
We adopt code from the following code repositories. We sincerely appreciate these great work/codebases:
Agent-workflow-memory
webarena
mini-swe-agent
If you find this work useful, please kindly cite our paper:
This is not an officially supported Google product. This project is not eligible for the Google Open Source Software
Vulnerability Rewards Program.
This project is intended for demonstration purposes only It is not intended for use in a production environment
Releases
No releases published
Create a new release
Packages
No packages published
Publish your first package
Contributors
2. SWE-Bench
Acknowledgement
📚 Citation
@inproceedings{
  ouyang2026reasoningbank,
  title={ReasoningBank: Scaling Agent Self-Evolving with Reasoning Memory},
  author={Siru Ouyang and Jun Yan and I-Hung Hsu and Yanfei Chen and Ke Jiang and Zifeng 
Wang and Rujun Han and Long Le and Samira Daruki and Xiangru Tang and Vishy Tirumalashetty 
and George Lee and Mahsan Rofouei and Hangfei Lin and Jiawei Han and Chen-Yu Lee and Tomas 
Pfister},
  booktitle={The Fourteenth International Conference on Learning Representations},
  year={2026},
  url={https://openreview.net/forum?id=jL7fwchScm}
}
Disclaimer


No contributors
Languages
Python 98.9%
Shell 1.1%
Suggested workflows
Based on your tech stack
SLSA Generic generator
Generate SLSA3 provenance for your existing release workflows
By Open Source Security Foundation (OpenSSF)
Configure
Django
Build and Test a Django Project
By GitHub Actions
Configure
Pylint
Lint a Python application with pylint.
By GitHub Actions
Configure
More workflows
