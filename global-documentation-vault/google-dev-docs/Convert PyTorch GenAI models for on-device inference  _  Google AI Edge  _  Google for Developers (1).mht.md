# Convert PyTorch GenAI models for on-device inference  _  Google AI Edge  _  Google for Developers (1)

The [LiteRT Torch Generative API](https://github.com/google-ai-edge/litert-torch/tree/main/litert_torch/generative/) is a
high-performance library designed for authoring and converting
transformer-based PyTorch models into the LiteRT/LiteRT-LM format. This
enables developers to seamlessly deploy generative AI models, specifically
Large Language Models (LLMs), for on-device text and image generation
with ease.

The Torch Generative API supports model conversion for CPU, GPU and NPU.
By pairing Torch Generative API with [LiteRT-LM](https://github.com/google-ai-edge/LiteRT-LM), you can build
responsive, privacy-focused applications that run generative models entirely
on-device.

## Convert from Hugging Face Transformer Library

The LiteRT Torch [Hugging Face Export](https://github.com/google-ai-edge/litert-torch/tree/main/litert_torch/generative/export_hf) extension provides a
 streamlined pathway to convert generative AI models directly from the
[Hugging Face Transformers Library](https://huggingface.co/docs/transformers/en/index) into the
[LiteRT-LM](https://github.com/google-ai-edge/LiteRT-LM) format. Compared to
 [LiteRT Torch Generative APIs](https://github.com/google-ai-edge/litert-torch/tree/main/litert_torch/generative/) that provide you
 pytorch building blocks to build and optimize custom models, this tool handles
the complexities of downloading weights, translating PyTorch
 model architectures, and applying optimization techniques like graph
 optimizations and quantization in a single workflow. It outputs a .litertlm
 file, which is optimized for on-device inference on CPU, GPU and NPU using the
 [LiteRT-LM](https://github.com/google-ai-edge/LiteRT-LM) runtime.

### Prerequisites

Before using the export extension, ensure you have the following setup:

- Install [LiteRT Torch Python package](https://github.com/google-ai-edge/litert-torch). The Hugging Face Export extension is built directly into the`litert-torch`package.
- (Optional) For NPU compilation, install LiteRT NPU SDK extensions using
`pip install ai-edge-litert[npu-sdk]`. Fore more details, you can follow[LiteRT NPU AOT Compilation Colab](https://github.com/google-ai-edge/litert-samples/blob/main/compiled_model_api/colab/LiteRT_AOT_Compilation_Tutorial.ipynb).
- Hugging Face environment is set up if you intend to load from Hugging Face
hub directly. The export_hf tool uses the standard transformers authentication
mechanisms like `HF_TOKEN`or CLI. See example:

To download gated models (such as Gemma or Llama), you must authenticate with Hugging Face using either the CLI or an environment variable:

```
# Set your Hugging Face token as an environment variable
export HF_TOKEN="your_hugging_face_token"
# Or use the Hugging Face CLI login
hf auth login
```
### Basic Usage

You can use `export_hf` using the command line or the Python API. The tool will
 automatically download the model from Hugging Face or load the model from local
path provided, trace it, apply default optimizations, and convert it to
 a `.litertlm` file compatible for CPU and GPU inference.

#### Command Line Interface (CLI)

Use the `litert-torch export_hf` command. You need to provide the Hugging Face
 model ID and the chosen output directory.

```
litert-torch export_hf \
  --model=google/gemma-3-270m-it \
  --output_dir=/tmp/gemma3-270m-it-litertlm
```
For exporting a local or custom model, you can also pass the path to the safetensor checkpoint:

```
litert-torch export_hf \
  --model=/path/to/safetensor/dir \
  --output_dir=/my_custom_litertlm
```
#### Python API

For integration into Python scripts or notebooks, import the `export` module
 from `litert_torch.generative.export_hf`.

```
from litert_torch.generative.export_hf import export
export.export(
    model='google/gemma-3-270m-it',
    output_dir='/tmp/gemma3-270m-it-litertlm',
)
```
### On-device deployment with LiteRT-LM 

Once you have successfully exported your model to a `.litertlm` file, you can
 deploy it directly on-device using LiteRT-LM for high-performance execution on
  both CPU and GPU. See details on [how to use the LiteRT-LM API](https://ai.google.dev/edge/litert/next/litert_lm_npu). For
  NPU acceleration, refer to [NPU AOT compilation guide](https://developers.google.com/edge/litert/conversion/pytorch/genai#npu-aot-compilation).

### Supported Architectures

The `export_hf` tool verifies the following Transformers model architectures.
This can be verified by checking the `model_type` field in `config.json`.

- **Gemma 3**(- `Gemma3ForCausalLM`)
- **Gemma 3n**(- `Gemma3nForCausalLM`)
- **Gemma 4**(- `Gemma4ForCausalLM`)
- **Llama**(- `LlamaForCausalLM`)
- **Mistral**(- `MistralForCausalLM`)
- **Qwen 2/2.5**(- `Qwen2ForCausalLM`)
- **Qwen 3**(- `Qwen3ForCausalLM`)
- **SmolLM 3**(- `SmolLM3ForCausalLM`)

### Advanced settings

While you can explore the advanced options available in the extension flags, the follows are some common knobs you can try.

#### Vision Language Models

For supported models, you can set `--task=image_text_to_text` and
`--export_vision_encoder` to load and export the vision encoder model.

Supported architectures:

- **Gemma 3**(- `Gemma3ForConditionalGeneration`)
- **Gemma 4**(- `Gemma4ForConditionalGeneration`)

#### Quantization Configuration

Generative AI models are often too large to run efficiently on edge devices
 without optimization. By default, `export_hf` applies the `dynamic_wi8_afp32`
  quantization recipe using [AI Edge Quantizer](https://github.com/google-ai-edge/ai-edge-quantizer),
  which quantizes weights to per-channel INT8 while keeping activations in FP32.

You can override this default behavior using the `--quantization_recipe` flag
 (or the `quantization_recipe` parameter in Python).
 You can provide the name of a built-in recipe from
 [AI Edge Quantizer](https://github.com/google-ai-edge/ai-edge-quantizer) or specify the path to a custom JSON
recipe.

**Example:**

```
litert-torch export_hf \
  --model=google/gemma-3-270m-it \
  --output_dir=/tmp/gemma3-270m-it-litertlm \
  --quantization_recipe=/path/to/my/quantization_recipe.json
```
#### Jinja Template Override

The jinja template coming with the transformers model might not be compatible
with LiteRT-LM (e.g. Gemma4 models), you can set `use_jinja_template` flag to
`False` or use `jinja_chat_template_override` option to override the template.

**Example:**

```
 litert-torch export_hf \
   --model=google/gemma-4-E2B-it \
  --output_dir=/tmp/gemma4_2b_litertlm \
  --externalize_embedder \
  --jinja_chat_template_override=litert-community/gemma-4-E2B-it-litert-lm
```
### NPU AOT Compilation

In addition to CPU and GPU, you can also target supported NPU accelerators when exporting your models by providing the NPU specific options.

#### Google Tensor

Prerequisites: Follow [Google Tensor SDK](https://developers.google.com/edge/litert/next/tensor-sdk) page
 for the development environment setup.

To export LLMs targeting Google Tensor TPUs, follow the example for the additional flags required for TPU compilation.

**Example:**

```
litert-torch export-hf \
  --model=google/gemma-3-270m-it \
  --output_dir=/tmp/gemma3-270m-google-tensor-g5 \
  --split_cache \
  --externalize_embedder \
  --prefill_lengths=128, \
  --cache_length=1280 \
  --quantization_recipe="weight_only_wi8_afp32"
  --aot_backend=GOOGLE \
  --aot_soc_model=Tensor_G5 \
  --aot_compilation_config_dict='{"google_tensor_enable_large_model_support": True}'
```
For more information, see [Compile models with Google Tensor SDK](https://developers.google.com/edge/litert/next/compilation-flags).

#### Qualcomm AI Runtime:

Prerequisites: Follow [LiteRT Qualcomm Integration](https://ai.google.dev/edge/litert/next/qualcomm) for SDK
setup instructions and supported devices.

**Example:**

```
litert-torch export-hf \
  --model=google/gemma-3-270m-it \
  --output_dir=/tmp/gemma3-270m-google-tensor-g5 \
  --split_cache \
  --externalize_embedder \
  --quantization_recipe='' \
  --aot_backend=qualcomm \
  --aot_soc_model=SM8750
```
#### MediaTek NeuroPilot:  

Prerequisites: Follow [LiteRT MediaTek Integration](https://ai.google.dev/edge/litert/next/mediatek) for SDK
setup instructions and supported devices.

**Example:**

```
litert-torch export-hf \
  --model=google/gemma-3-270m-it \
  --output_dir=/tmp/gemma3-270m-google-tensor-g5 \
  --split_cache \
  --externalize_embedder \
  --aot_backend=mediatek \
  --aot_soc_model=MT8189
```
#### Intel OpenVINO 

Prerequisites: Follow [LiteRT Intel OpenVINO Integration](https://ai.google.dev/edge/litert/next/intel) for SDK
setup instructions and supported devices.

**Example:**

```
litert-torch export-hf \
  --model=google/gemma-3-270m-it \
  --output_dir=/tmp/gemma3-270m-google-tensor-g5 \
  --split_cache \
  --externalize_embedder \
  --aot_backend=intel_openvino \
  --aot_soc_model=PTL
```
## Re-author and Convert using LiteRT Torch Generative API 

LiteRT Torch Generative API also provides building blocks to build and optimize
 custom PyTorch models, including but not limited to normalizer layers,
 attentions and other basic modules. If your model is not covered by
 the LiteRT Torch [Hugging Face Export](https://github.com/google-ai-edge/litert-torch/tree/main/litert_torch/generative/export_hf) extension, you can build your
 own models to be compatible with LiteRT and LiteRT-LM.

There are model [examples](https://github.com/google-ai-edge/litert-torch/tree/main/litert_torch/generative/examples) including LLMs, diffusion models and
ASR models. Feel free to check those out and deploy your own model.

For more information, see the
[Generative Torch API GitHub repo](https://github.com/google-ai-edge/litert-torch/tree/main/litert_torch/generative/).