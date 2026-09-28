# Android Install - Qualcomm® AI Hub GenieX

Android (Kotlin)
Android Install
Add the GenieX SDK to an Android Studio project so your app can pull weights from Hugging
Face / Qualcomm AI Hub and run them on the Hexagon NPU, Adreno GPU, or CPU compute
units — all in Kotlin.
Try the sample app first
See GenieX running on Android before you write any code. The reference chat app — with
model picker, resumable downloads, and VLM support — lives in qualcomm/ai-hub-apps .
Clone it, open it in Android Studio, and hit Run ▶.
Pick a model from the dropdown and choose NPU, GPU, or CPU on load. Tap the image button
for VLMs. Stay on Wi-Fi for the first download.
No phone? See 
.
Prerequisites
Get the GenieX Chat sample app
Build the reference chat app from source — follow the README to clone, build, and run
it.
Android Studio 
 or newer.
Testing without a physical device
Hedgehog (2023.1.1)
Android (Kotlin)
Android Install
Qualcomm® AI Hub GenieX


Add the SDK to your app
minSdk = 27 (Android 8.1) in your app module.
A phone running Snapdragon 8 Elite ( SM8750 ) or Snapdragon 8 Elite Gen 5 ( SM8850 )
— see 
.
Enable Maven Central
In settings.gradle.kts (or your top-level build.gradle.kts for older projects):
1
Add the dependency
In your app module’s build.gradle.kts :
The artifact ships native arm64-v8a libraries — no NDK or CMake on your side.
2
Declare permissions
The SDK pulls weights at runtime. In AndroidManifest.xml :
3
Supported platforms
Qualcomm® AI Hub GenieX


Linux (Docker) Install
Quickstart
Powered by
Next, head to the 
 to download and run your first model.
Was this page helpful?
Yes
No
For VLMs that load images from the gallery, also declare READ_EXTERNAL_STORAGE (or
scoped media permissions on Android 13+).
Sync Gradle
Click Sync Now in Android Studio.
4
Quickstart
Qualcomm® AI Hub GenieX
