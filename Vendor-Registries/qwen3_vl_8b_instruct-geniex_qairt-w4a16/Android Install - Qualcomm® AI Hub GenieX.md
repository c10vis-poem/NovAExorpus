<!-- Converted from Android Install - Qualcomm® AI Hub GenieX.pdf — 3 pages -->

## Page 1

Qualcomm® AI Hub GenieX
Android (Kotlin) Android Install
Android (Kotlin)
## Android Install
Add the GenieX SDK to an Android Studio project so your app can pull weights from Hugging
Face / Qualcomm AI Hub and run them on the Hexagon NPU, Adreno GPU, or CPU compute
units — all in Kotlin.
## Try the sample app first
See GenieX running on Android before you write any code. The reference chat app — with
model picker, resumable downloads, and VLM support — lives in qualcomm/ai-hub-apps .
Clone it, open it in Android Studio, and hit Run ▶.
Get the GenieX Chat sample app Build the reference chat app from source — follow the README to clone, build, and run it.
Pick a model from the dropdown and choose NPU, GPU, or CPU on load. Tap the image button
for VLMs. Stay on Wi-Fi for the first download.
No phone? See Testing without a physical device.
## Prerequisites
Android Studio Hedgehog (2023.1.1) or newer.

---

## Page 2

Qualcomm® AI Hub GenieX A phone running Snapdragon 8 Elite ( SM8750 ) or Snapdragon 8 Elite Gen 5 ( SM8850 )
— see Supported platforms.
### Add the SDK to your app
Enable Maven Central
In settings.gradle.kts (or your top-level build.gradle.kts for older projects):
Add the dependency
In your app module’s build.gradle.kts :
The artifact ships native arm64-v8a libraries — no NDK or CMake on your side.
Declare permissions
The SDK pulls weights at runtime. In AndroidManifest.xml :

---

## Page 3

Qualcomm® AI Hub GenieX
For VLMs that load images from the gallery, also declare READ_
scoped media permissions on Android 13+).
Sync Gradle
Click Sync Now in Android Studio.
Next, head to the Quickstart to download and run your first model.
Was this page helpful? Yes No
Linux (Docker) Install
Powered by
_STORAGE (or
Quickstart
EXTERNAL