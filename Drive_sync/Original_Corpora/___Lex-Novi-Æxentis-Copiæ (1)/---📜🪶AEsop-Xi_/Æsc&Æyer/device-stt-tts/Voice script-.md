SRT/TTS SCRIPT

rm -f ~/vad_test.wav

echo "Recording up to 15s... speak now, pause when done"

termux-microphone-record -f ~/vad_test.wav -l 15

sleep 16

echo "Transcribing in proot..."

proot-distro login debian -- bash -c "cd /root/models &&
~/venv/bin/python3 \<\< 'PYEOF'

import sherpa_onnx

import numpy as np

import wave

vad_model = sherpa_onnx.VoiceActivityDetector(

sherpa_onnx.VadModelConfig(

silero_vad=sherpa_onnx.SileroVadModelConfig(model='silero-vad/silero_vad.onnx'),

sample_rate=16000,

),

buffer_size_in_seconds=30,

)

recognizer = sherpa_onnx.OfflineRecognizer.from_moonshine(

preprocessor='sherpa-onnx-moonshine-base-en-int8/preprocess.onnx',

encoder='sherpa-onnx-moonshine-base-en-int8/encode.int8.onnx',

uncached_decoder='sherpa-onnx-moonshine-base-en-int8/uncached_decode.int8.onnx',

cached_decoder='sherpa-onnx-moonshine-base-en-int8/cached_decode.int8.onnx',

tokens='sherpa-onnx-moonshine-base-en-int8/tokens.txt',

)

with wave.open('/data/data/com.termux/files/home/vad_test.wav', 'rb') as
f:

frames = f.readframes(f.getnframes())

samples = np.frombuffer(frames, dtype=np.int16).astype(np.float32) /
32768.0

window = 512

for i in range(0, len(samples), window):

vad_model.accept_waveform(samples\[i:i+window\])

while not vad_model.empty():

seg = vad_model.front

vad_model.pop()

stream = recognizer.create_stream()

stream.accept_waveform(seg.samples)

recognizer.decode_stream(stream)

print('TRANSCRIBED:', stream.result.text)

PYEOF

“

proot-distro login debian -- bash -c "~/venv/bin/pip install numpy”
