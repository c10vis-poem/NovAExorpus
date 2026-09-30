# c10vis-poem／silero-vad: Silero VAD: pre-trained enterprise-grade Voice Activity Detector

Watch
0
Silero VAD: pre-trained enterprise-grade Voice Activity Detector
MIT License
Code of conduct
0 stars
0 forks
0 watching
1 branch
0 tags
Activity
Public repository · Forked from snakers4/silero-vad
1 Branch
0 Tags
Go to file
Go to file
Add file
Code
This branch is up to date with snakers4/silero-vad:master .
Contribute
Sync fork
adamnsandle Merge pull request snakers4#784 from AliOsm/add-vectorized-offline-on…
76e3dc4 · 2 weeks ago
.github
Update test.yml
5 months ago
datasets
Update README.md
2 years ago
examples
Add offline ONNX sequence export ex…
2 weeks ago
files
Delete files/real_time_example.mp4
2 years ago
src/silero_vad
add openvino model
27 days ago
tests
replace mp3 test file with valid
last month
tuning
Update utils.py
9 months ago
CITATION.cff
Create CITATION.cff
last year
CODE_OF_CONDUCT.md
Mv folder
6 years ago
LICENSE
Add License
6 years ago
README.md
Add offline ONNX sequence export ex…
2 weeks ago
hubconf.py
add just 16k model
2 years ago
pyproject.toml
Update pyproject.toml
last month
silero-vad.ipynb
add pip examples to collab
2 years ago
c10vis-poem
silero-vad
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
README
Code of conduct
License


E M A I L
T E L E G R A M
L I C E N S E
M I T
D O W N L O A D S
R A T E L I M I T E D B Y U P S T R E A M S E R V I C E
Open in Colab
Open in Colab
Test Package
Test Package
passing
passing
pypi
pypi v6.2.1
v6.2.1
python
python 3.8 | 3.9 | 3.10 | 3.11 | 3.12 | 3.13 | 3.14 | 3.15
3.8 | 3.9 | 3.10 | 3.11 | 3.12 | 3.13 | 3.14 | 3.15
Silero VAD - pre-trained enterprise-grade Voice Activity Detector (also see our STT models).
Real Time Example
Silero VAD


Dependencies
Using pip: pip install silero-vad
Using torch.hub:
Stellar accuracy
Silero VAD has excellent results on speech detection tasks.
Fast
One audio chunk (30+ ms) takes less than 1ms to be processed on a single CPU thread. Using batching or
GPU can also improve performance considerably. Under certain conditions ONNX may even run up to 4-5x
faster.
Lightweight
JIT model is around two megabytes in size.
General
Fast start
from silero_vad import load_silero_vad, read_audio, get_speech_timestamps
model = load_silero_vad()
wav = read_audio('path_to_audio_file')
speech_timestamps = get_speech_timestamps(
  wav,
  model,
  return_seconds=True,  # Return speech timestamps in seconds (default is samples)
)
import torch
torch.set_num_threads(1)
model, utils = torch.hub.load(repo_or_dir='snakers4/silero-vad', model='silero_vad')
(get_speech_timestamps, _, read_audio, _, _) = utils
wav = read_audio('path_to_audio_file')
speech_timestamps = get_speech_timestamps(
  wav,
  model,
  return_seconds=True,  # Return speech timestamps in seconds (default is samples)
)
Key Features


Silero VAD was trained on huge corpora that include over 6000 languages and it performs well on audios from
different domains with various background noise and quality levels.
Flexible sampling rate
Silero VAD supports 8000 Hz and 16000 Hz sampling rates.
Highly Portable
Silero VAD reaps benefits from the rich ecosystems built around PyTorch and ONNX running everywhere
where these runtimes are available.
No Strings Attached
Published under permissive license (MIT) Silero VAD has zero strings attached - no telemetry, no keys, no
registration, no built-in expiration, no keys or vendor lock.
Voice activity detection for IOT / edge / mobile use cases
Data cleaning and preparation, voice detection in general
Telephony and call-center automation, voice bots
Voice interfaces
Examples and Dependencies
Quality Metrics
Performance Metrics
Versions and Available Models
Further reading
FAQ
Try our models, create an issue, start a discussion, join our telegram chat, email us, read our news.
Please see our wiki for relevant information and email us directly.
Citations
Typical Use Cases
Links
Get In Touch


Example of VAD ONNX Runtime model usage in C++
Example of VAD ExecuTorch model usage in C++
Voice activity detection for the browser using ONNX Runtime Web
Rust, Rust (wavekat-vad), Go, Java, C++, C# and other community examples
OpenVINO conversion guidelines
Releases
No releases published
Create a new release
Packages
No packages published
Publish your first package
Contributors
No contributors
Languages
Python 89.1%
Jupyter Notebook 10.9%
Suggested workflows
Based on your tech stack
Python package
Create and test a Python package on multiple Python versions.
By GitHub Actions
Configure
@misc{Silero VAD,
  author = {Silero Team},
  title = {Silero VAD: pre-trained enterprise-grade Voice Activity Detector (VAD), Number 
Detector and Language Classifier},
  year = {2024},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/snakers4/silero-vad}},
  commit = {insert_some_commit_here},
  email = {hello@silero.ai}
}
Examples and VAD-based Community Apps


Django
Build and Test a Django Project
By GitHub Actions
Configure
Publish Python Package
Publish a Python Package to PyPI on release.
By GitHub Actions
Configure
More workflows
