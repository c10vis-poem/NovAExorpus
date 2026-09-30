# LiteRT CompiledModel Kotlin API  _  Google AI Edge  _  Google for Developers

The LiteRT `CompiledModel` API is available in Kotlin, offering Android
developers a seamless, accelerator-first experience with high-level APIs. For an
example, see the [Image segmentation Kotlin App](https://github.com/google-ai-edge/litert-samples/tree/main/compiled_model_api/image_segmentation).

The following guide shows the basic CPU inference of the `CompiledModel` Kotlin
API. See guide on [GPU acceleration](https://developers.google.com/edge/litert/next/gpu) and [NPU acceleration](https://developers.google.com/edge/litert/next/npu) for
advanced acceleration features.

## Add Maven package

Add the LiteRT Maven package to your Android project:

```
dependencies {
  ...
  implementation `com.google.ai.edge.litert:litert:2.1.0`
}
```
## Basic inference

### Create `Compiled`Model 

Initialize the runtime with a model and your choice of hardware acceleration:

```
val  model =
  CompiledModel.create(
    context.assets,
    "mymodel.tflite",
    CompiledModel.Options(Accelerator.CPU),
    env,
  )
```
### Create Input and Output Buffers

Create the necessary data structures (buffers) to hold the input data that you will feed into the model for inference, and the output data that the model produces after running inference.

```
val inputBuffers = model.createInputBuffers()
val outputBuffers = model.createOutputBuffers()
```
If you are using CPU memory, fill the inputs by writing data directly into the first input buffer.

```
inputBuffers[0].writeFloat(FloatArray(data_size) { data_value /* your data */ })
```
### Invoke the model

Providing the input and output buffers, run the model.

```
model.run(inputBuffers, outputBuffers)
```
### Retrieve Outputs

Retrieve outputs by directly reading the model output from memory.

```
val outputFloatArray = outputBuffers[0].readFloat()
```
## Use `Tensor`Buffer 

LiteRT provides built-in support for I/O buffer interoperability, using the
Tensor Buffer API (`TensorBuffer`) to handle the flow of data into and out of
the `CompiledModel`. The Tensor Buffer API provides the ability to write
(`Write<T>()`) and read (`Read<T>()`), and lock buffers.

For a more complete view of how the Tensor Buffer API is implemented, see the
source code at
[TensorBuffer.kt](https://github.com/google-ai-edge/LiteRT/blob/main/litert/kotlin/src/main/kotlin/com/google/ai/edge/litert/TensorBuffer.kt).