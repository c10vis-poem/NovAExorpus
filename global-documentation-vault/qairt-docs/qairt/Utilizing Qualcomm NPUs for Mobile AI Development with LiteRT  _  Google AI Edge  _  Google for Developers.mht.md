# Utilizing Qualcomm NPUs for Mobile AI Development with LiteRT  _  Google AI Edge  _  Google for Developers

As mobile AI models grow, LiteRT developers need to maximize performance. NPUs are increasingly crucial for on-device AI offering lower latency, higher throughput, and reduced power consumption compared to CPUs and GPUs. Leveraging Qualcomm® NPUs via the Qualcomm AI Engine Direct Delegate significantly improves mobile AI app performance on Snapdragon devices. In collaboration with Qualcomm, the Google AI Edge team will demonstrate integrating this delegate into Android apps, highlighting performance gains over traditional processors and showing how to get started.

## Qualcomm AI Engine Direct Delegate

The Qualcomm AI Engine Direct Delegate enables users to run LiteRT models using the Qualcomm AI Stack. Using the Qualcomm AI Engine Direct Delegate is essential to running inference on the NPU for your LiteRT model on-device. Supported devices include:

- Snapdragon 8 Gen 1 (SM8450)
- Snapdragon 8 Gen 2 (SM8550)
- Snapdragon 8 Gen 3 (SM8650)
- Snapdragon 8 Elite (SM8750)
- [and more](https://docs.qualcomm.com/bundle/publicresource/topics/80-63442-50/overview.html)

Applications on these devices will benefit from the Qualcomm AI Stack by targeting the NPU which provides the best performance for AI models.

## How to leverage the NPU using Qualcomm AI Engine Direct Delegate

First, download the Qualcomm AI Engine Direct Delegate available on [Maven
Central](https://central.sonatype.com/artifact/com.qualcomm.qti/qnn-litert-delegate).
To [set up the
delegate](https://docs.qualcomm.com/bundle/publicresource/topics/80-63442-50/TfLite-Delegate_setup.html#android-java-application)
in an Android Java Application, the following dependencies are needed:

```
dependencies {
 implementation 'com.qualcomm.qti:qnn-runtime:2.34.0'
 implementation 'com.qualcomm.qti:qnn-litert-delegate:2.34.0' }
```
To use the delegate:

```
try {
  // Created default Options
  QnnDelegate.Options options = new QnnDelegate.Options();
  // Set the backend and library path
  options.setBackendType(QnnDelegate.Options.BackendType.HTP_BACKEND);
  options.setSkelLibraryDir(activity.getApplicationInfo().nativeLibraryDir);
  // Create the Delegate instance.
  qnnDelegate = new QnnDelegate(options);
  tfliteOptions.addDelegate(qnnDelegate);
}
catch (UnsupportedOperationException e) {
  // Delegate creation failed
}
tfliteInterpreter = new Interpreter(tfliteModel, tfliteOptions);
```
To see an example of an Android app that uses the QNN Delegate for LiteRT, see
the Qualcomm AI Hub [Android Sample
Apps](https://github.com/quic/ai-hub-apps/tree/main/apps/android).

## Performance Benefits

On devices with Snapdragon SOCs with the Qualcomm® Hexagon Tensor Processor,
most models perform significantly faster compared to GPU and CPU. The HTP is
also a more power-efficient processor for neural network computation.
MobileNetv2, an open-source model, pre-optimized as part of [AI Hub
Models](https://aihub.qualcomm.com/models/mobilenet_v2) was used as a sample for
this performance analysis.

| Device | NPU (QNN Delegate for HTP) | GPU (GPUv2) | CPU (XNNPACK) | 
|---|---|---|---|
| Samsung S25 | 0.3ms | 1.8ms | 2.8ms | 
| Samsung S24 | 0.4ms | 2.3ms | 3.6ms | 
| Samsung S23 | 0.6ms | 2.7ms | 4.1ms | 

| Device | NPU (QNN Delegate for HTP) | GPU (GPUv2) | CPU (XNNPACK) | 
|---|---|---|---|
| Samsung S25 | 24.9ms | 43ms | 481.7ms | 
| Samsung S24 | 29.8ms | 52.6ms | 621.4ms | 
| Samsung S23 | 43.7ms | 68.2ms | 871.1ms | 

Snapdragon and Qualcomm branded products are products of Qualcomm Technologies, Inc. and/or its subsidiaries.

## What's Next

Stay tuned for more exciting updates on leveraging NPUs seamlessly for AI
application development with [LiteRT Next](https://developers.google.com/edge/litert/next/overview)!