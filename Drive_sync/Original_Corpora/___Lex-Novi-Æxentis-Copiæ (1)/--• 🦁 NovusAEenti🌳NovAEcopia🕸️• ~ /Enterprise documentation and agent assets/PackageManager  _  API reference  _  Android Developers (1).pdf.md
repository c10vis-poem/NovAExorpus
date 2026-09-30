# PackageManager  _  API reference  _  Android Developers (1)

Added in API level 1 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
r
PackageManager
Kotlin (https://developer.android.com/reference/kotlin/android/content/pm/PackageManager) | Java
public abstract class PackageManager
extends Object (https://developer.android.com/reference/java/lang/Object)
java.lang.Object (https://developer.android.com/reference/java/lang/Object)
  ↳android.content.pm.PackageManager
MockPackageManager
 (https://developer.android.com/reference/android/test/mock/MockPackageManager)
This class was dep
a mocking framew
 (https://github.co
tests should be wr
Testing Support Li
 (https://develope
support-library)
.
Class for retrieving various kinds of information related to the application packages that are
currently installed on the device. You can find this class through Context.getPackageManager
(https://developer.android.com/reference/android/content/Context#getPackageManager()).
Note: If your app targets Android 11 (API level 30) or higher, the methods in this class each return a filtered
list of apps. Learn more about how to manage package visibility
(https://developer.android.com/training/basics/intents/package-visibility).
con
Known direct subclasses
MockPackageManager (https://developer.android.com/reference/android/test/mock/MockPackageMan


Summary
Nested classes
class
PackageManager.ApplicationInfoFlags
 (https://developer.android.com/reference/android/content/pm/PackageM
Specific flags used for retrieving application info. 
class
PackageManager.ComponentEnabledSetting
 (https://developer.android.com/reference/android/content/pm/PackageM
The class containing the enabled setting of a package component. 
class
PackageManager.ComponentInfoFlags
 (https://developer.android.com/reference/android/content/pm/PackageM
Specific flags used for retrieving component info. 
class
PackageManager.NameNotFoundException
 (https://developer.android.com/reference/android/content/pm/PackageM
This exception is thrown when a given package, application, or component
interface
PackageManager.OnChecksumsReadyListener
 (https://developer.android.com/reference/android/content/pm/PackageM
Listener that gets notified when checksums are available. 
class
PackageManager.PackageInfoFlags
 (https://developer.android.com/reference/android/content/pm/PackageM
Specific flags used for retrieving package info. 
class
PackageManager.Property
 (https://developer.android.com/reference/android/content/pm/PackageM
A property value set within the manifest. 


class
PackageManager.ResolveInfoFlags
 (https://developer.android.com/reference/android/content/pm/PackageM
Specific flags used for retrieving resolve info. 
Constants
int
CERT_INPUT_RAW_X509 (https://developer.and
Certificate input bytes: the input bytes represent a
int
CERT_INPUT_SHA256 (https://developer.android
Certificate input bytes: the input bytes represent t
int
COMPONENT_ENABLED_STATE_DEFAULT (https
Flag for setApplicationEnabledSetting(S
setComponentEnabledSetting(Component
 (https://developer.android.com/reference/andro
specified in its manifest).
int
COMPONENT_ENABLED_STATE_DISABLED (http
Flag for setApplicationEnabledSetting(S
setComponentEnabledSetting(Component
 (https://developer.android.com/reference/andro
regardless of what it has specified in its manifest
int
COMPONENT_ENABLED_STATE_DISABLED_UNT
Flag for setApplicationEnabledSetting(S
application should be considered, until the point w
int
COMPONENT_ENABLED_STATE_DISABLED_USE
Flag for setApplicationEnabledSetting(S
has explicitly disabled the application, regardless


int
COMPONENT_ENABLED_STATE_ENABLED (https
Flag for setApplicationEnabledSetting(S
setComponentEnabledSetting(Component
 (https://developer.android.com/reference/andro
regardless of what it has specified in its manifest
int
DELETE_ARCHIVE (https://developer.android.co
Flag parameter for PackageInstaller.unins
 (https://developer.android.com/reference/andro
int
DONT_KILL_APP (https://developer.android.com
Flag parameter for setComponentEnabledSet
 (https://developer.android.com/reference/andro
component.
String
(https://developer.android.com/reference/java/lang/String)
EXTRA_VERIFICATION_ID (https://developer.a
Extra field name for the ID of a package pending 
String
(https://developer.android.com/reference/java/lang/String)
EXTRA_VERIFICATION_RESULT (https://develo
Extra field name for the result of a verification, eit
 (https://developer.android.com/reference/andro
String
(https://developer.android.com/reference/java/lang/String)
FEATURE_ACTIVITIES_ON_SECONDARY_DISP
Feature for getSystemAvailableFeatures(
 (https://developer.android.com/reference/andro
String
(https://developer.android.com/reference/java/lang/String)
FEATURE_APP_WIDGETS (https://developer.and
Feature for getSystemAvailableFeatures(
 (https://developer.android.com/reference/andro


String
(https://developer.android.com/reference/java/lang/String)
FEATURE_AUDIO_LOW_LATENCY (https://develo
Feature for getSystemAvailableFeatures(
 (https://developer.android.com/reference/andro
sound input or output.
String
(https://developer.android.com/reference/java/lang/String)
FEATURE_AUDIO_OUTPUT (https://developer.an
Feature for getSystemAvailableFeatures(
 (https://developer.android.com/reference/andro
Document (CDD) section 7.8 Audio (https://sourc
String
(https://developer.android.com/reference/java/lang/String)
FEATURE_AUDIO_PRO (https://developer.android
Feature for getSystemAvailableFeatures(
 (https://developer.android.com/reference/andro
String
(https://developer.android.com/reference/java/lang/String)
FEATURE_AUDIO_SPATIAL_HEADTRACKING_L
Feature for getSystemAvailableFeatures(
 (https://developer.android.com/reference/andro
criteria for the feature.
String
(https://developer.android.com/reference/java/lang/String)
FEATURE_AUTOFILL (https://developer.android.
Feature for getSystemAvailableFeatures(
 (https://developer.android.com/reference/andro
providers (https://developer.android.com/refe
String
(https://developer.android.com/reference/java/lang/String)
FEATURE_AUTOMOTIVE (https://developer.andro
Feature for getSystemAvailableFeatures(
 (https://developer.android.com/reference/andro
String
(https://developer.android.com/reference/java/lang/String)
FEATURE_BACKUP (https://developer.android.co
Feature for getSystemAvailableFeatures(
 (https://developer.android.com/reference/andro
String
(https://developer.android.com/reference/java/lang/String)
FEATURE_BLUETOOTH (https://developer.android


Feature for getSystemAvailableFeatures(
 (https://developer.android.com/reference/andro
String
(https://developer.android.com/reference/java/lang/String)
FEATURE_BLUETOOTH_LE (https://developer.an
Feature for getSystemAvailableFeatures(
 (https://developer.android.com/reference/andro
String
(https://developer.android.com/reference/java/lang/String)
FEATURE_BLUETOOTH_LE_CHANNEL_SOUNDIN
Feature for getSystemAvailableFeatures(
 (https://developer.android.com/reference/andro
String
(https://developer.android.com/reference/java/lang/String)
FEATURE_CAMERA (https://developer.android.co
Feature for getSystemAvailableFeatures(
 (https://developer.android.com/reference/andro
String
(https://developer.android.com/reference/java/lang/String)
FEATURE_CAMERA_ANY (https://developer.andro
Feature for getSystemAvailableFeatures(
 (https://developer.android.com/reference/andro
 (https://developer.android.com/reference/andro
String
(https://developer.android.com/reference/java/lang/String)
FEATURE_CAMERA_AR (https://developer.android
Feature for getSystemAvailableFeatures(
 (https://developer.android.com/reference/andro
 (https://developer.android.com/reference/andro
String
(https://developer.android.com/reference/java/lang/String)
FEATURE_CAMERA_AUTOFOCUS (https://develop
Feature for getSystemAvailableFeatures(
 (https://developer.android.com/reference/andro
String
(https://developer.android.com/reference/java/lang/String)
FEATURE_CAMERA_CAPABILITY_MANUAL_POS
Feature for getSystemAvailableFeatures(
 (https://developer.android.com/reference/andro
 (https://developer.android.com/reference/andro


String
(https://developer.android.com/reference/java/lang/String)
FEATURE_CAMERA_CAPABILITY_MANUAL_SEN
Feature for getSystemAvailableFeatures(
 (https://developer.android.com/reference/andro
 (https://developer.android.com/reference/andro
String
(https://developer.android.com/reference/java/lang/String)
FEATURE_CAMERA_CAPABILITY_RAW (https://d
Feature for getSystemAvailableFeatures(
 (https://developer.android.com/reference/andro
 (https://developer.android.com/reference/andro
String
(https://developer.android.com/reference/java/lang/String)
FEATURE_CAMERA_CONCURRENT (https://develo
Feature for getSystemAvailableFeatures(
 (https://developer.android.com/reference/andro
CameraManager.getConcurrentCameraIds
String
(https://developer.android.com/reference/java/lang/String)
FEATURE_CAMERA_EXTERNAL (https://develope
Feature for getSystemAvailableFeatures(
 (https://developer.android.com/reference/andro
String
(https://developer.android.com/reference/java/lang/String)
FEATURE_CAMERA_FLASH (https://developer.an
Feature for getSystemAvailableFeatures(
 (https://developer.android.com/reference/andro
String
(https://developer.android.com/reference/java/lang/String)
FEATURE_CAMERA_FRONT (https://developer.an
Feature for getSystemAvailableFeatures(
 (https://developer.android.com/reference/andro
String
(https://developer.android.com/reference/java/lang/String)
FEATURE_CAMERA_LEVEL_FULL (https://develo
Feature for getSystemAvailableFeatures(
 (https://developer.android.com/reference/andro
 (https://developer.android.com/reference/andro
String
(https://developer.android.com/reference/java/lang/String)
FEATURE_CANT_SAVE_STATE (https://develope


Feature for getSystemAvailableFeatures(
 (https://developer.android.com/reference/andro
 (https://developer.android.com/reference/andro
String
(https://developer.android.com/reference/java/lang/String)
FEATURE_COMPANION_DEVICE_SETUP (https://
Feature for getSystemAvailableFeatures(
 (https://developer.android.com/reference/andro
 (https://developer.android.com/reference/andro
with devices via CompanionDeviceManager (h
String
(https://developer.android.com/reference/java/lang/String)
FEATURE_CONNECTION_SERVICE (https://deve
This constant was deprecated in API level 33. use 
String
(https://developer.android.com/reference/java/lang/String)
FEATURE_CONSUMER_IR (https://developer.and
Feature for getSystemAvailableFeatures(
 (https://developer.android.com/reference/andro
String
(https://developer.android.com/reference/java/lang/String)
FEATURE_CONTROLS (https://developer.android.
Feature for getSystemAvailableFeatures(
 (https://developer.android.com/reference/andro
applications.
String
(https://developer.android.com/reference/java/lang/String)
FEATURE_CREDENTIALS (https://developer.and
Feature for getSystemAvailableFeatures(
 (https://developer.android.com/reference/andro
String
(https://developer.android.com/reference/java/lang/String)
FEATURE_DEVICE_ADMIN (https://developer.an
Feature for getSystemAvailableFeatures(
 (https://developer.android.com/reference/andro
String
(https://developer.android.com/reference/java/lang/String)
FEATURE_DEVICE_ID_ATTESTATION (https://d
Feature for getSystemAvailableFeatures(
 (https://developer.android.com/reference/andro


String
(https://developer.android.com/reference/java/lang/String)
FEATURE_DEVICE_LOCK (https://developer.and
Feature for getSystemAvailableFeatures(
 (https://developer.android.com/reference/andro
String
(https://developer.android.com/reference/java/lang/String)
FEATURE_EMBEDDED (https://developer.android.
Feature for getSystemAvailableFeatures(
 (https://developer.android.com/reference/andro
String
(https://developer.android.com/reference/java/lang/String)
FEATURE_ETHERNET (https://developer.android.
Feature for getSystemAvailableFeatures(
 (https://developer.android.com/reference/andro
String
(https://developer.android.com/reference/java/lang/String)
FEATURE_EXPANDED_PICTURE_IN_PICTURE (
Feature for getSystemAvailableFeatures(
 (https://developer.android.com/reference/andro
String
(https://developer.android.com/reference/java/lang/String)
FEATURE_FACE (https://developer.android.com/
Feature for getSystemAvailableFeatures(
 (https://developer.android.com/reference/andro
String
(https://developer.android.com/reference/java/lang/String)
FEATURE_FAKETOUCH (https://developer.android
Feature for getSystemAvailableFeatures(
 (https://developer.android.com/reference/andro
String
(https://developer.android.com/reference/java/lang/String)
FEATURE_FAKETOUCH_MULTITOUCH_DISTINC
Feature for getSystemAvailableFeatures(
 (https://developer.android.com/reference/andro
distinct tracking of two or more fingers.
String
(https://developer.android.com/reference/java/lang/String)
FEATURE_FAKETOUCH_MULTITOUCH_JAZZHAN
Feature for getSystemAvailableFeatures(
 (https://developer.android.com/reference/andro
tracking a hand of fingers (5 or more fingers) fully


String
(https://developer.android.com/reference/java/lang/String)
FEATURE_FINGERPRINT (https://developer.and
Feature for getSystemAvailableFeatures(
 (https://developer.android.com/reference/andro
String
(https://developer.android.com/reference/java/lang/String)
FEATURE_FREEFORM_WINDOW_MANAGEMENT (h
Feature for getSystemAvailableFeatures(
 (https://developer.android.com/reference/andro
String
(https://developer.android.com/reference/java/lang/String)
FEATURE_GAMEPAD (https://developer.android.c
Feature for getSystemAvailableFeatures(
 (https://developer.android.com/reference/andro
compatible game controller in the box.
String
(https://developer.android.com/reference/java/lang/String)
FEATURE_HARDWARE_KEYSTORE (https://develo
Feature for getSystemAvailableFeatures(
 (https://developer.android.com/reference/andro
execution environment.
String
(https://developer.android.com/reference/java/lang/String)
FEATURE_HIFI_SENSORS (https://developer.an
Feature for getSystemAvailableFeatures(
 (https://developer.android.com/reference/andro
String
(https://developer.android.com/reference/java/lang/String)
FEATURE_HOME_SCREEN (https://developer.and
Feature for getSystemAvailableFeatures(
 (https://developer.android.com/reference/andro
String
(https://developer.android.com/reference/java/lang/String)
FEATURE_IDENTITY_CREDENTIAL_HARDWARE
Feature for getSystemAvailableFeatures(
 (https://developer.android.com/reference/andro
 (https://developer.android.com/reference/andro
String
(https://developer.android.com/reference/java/lang/String)
FEATURE_IDENTITY_CREDENTIAL_HARDWARE
Feature for getSystemAvailableFeatures(
 (https://developer.android.com/reference/andro


 (https://developer.android.com/reference/andro
String
(https://developer.android.com/reference/java/lang/String)
FEATURE_INPUT_METHODS (https://developer.a
Feature for getSystemAvailableFeatures(
 (https://developer.android.com/reference/andro
 (https://developer.android.com/reference/andro
String
(https://developer.android.com/reference/java/lang/String)
FEATURE_IPSEC_TUNNELS (https://developer.a
Feature for getSystemAvailableFeatures(
 (https://developer.android.com/reference/andro
String
(https://developer.android.com/reference/java/lang/String)
FEATURE_IPSEC_TUNNEL_MIGRATION (https://
Feature for getSystemAvailableFeatures(
 (https://developer.android.com/reference/andro
addresses.
String
(https://developer.android.com/reference/java/lang/String)
FEATURE_IRIS (https://developer.android.com/
Feature for getSystemAvailableFeatures(
 (https://developer.android.com/reference/andro
String
(https://developer.android.com/reference/java/lang/String)
FEATURE_KEYSTORE_APP_ATTEST_KEY (https
Feature for getSystemAvailableFeatures(
 (https://developer.android.com/reference/andro
String
(https://developer.android.com/reference/java/lang/String)
FEATURE_KEYSTORE_LIMITED_USE_KEY (http
Feature for getSystemAvailableFeatures(
 (https://developer.android.com/reference/andro
count (including count equals to 1).
String
(https://developer.android.com/reference/java/lang/String)
FEATURE_KEYSTORE_SINGLE_USE_KEY (https
Feature for getSystemAvailableFeatures(
 (https://developer.android.com/reference/andro
count equals to 1.


String
(https://developer.android.com/reference/java/lang/String)
FEATURE_LEANBACK (https://developer.android.
Feature for getSystemAvailableFeatures(
 (https://developer.android.com/reference/andro
String
(https://developer.android.com/reference/java/lang/String)
FEATURE_LEANBACK_ONLY (https://developer.a
Feature for getSystemAvailableFeatures(
 (https://developer.android.com/reference/andro
String
(https://developer.android.com/reference/java/lang/String)
FEATURE_LIVE_TV (https://developer.android.c
Feature for getSystemAvailableFeatures(
 (https://developer.android.com/reference/andro
TvInputService (https://developer.android.co
String
(https://developer.android.com/reference/java/lang/String)
FEATURE_LIVE_WALLPAPER (https://developer.
Feature for getSystemAvailableFeatures(
 (https://developer.android.com/reference/andro
String
(https://developer.android.com/reference/java/lang/String)
FEATURE_LOCATION (https://developer.android.
Feature for getSystemAvailableFeatures(
 (https://developer.android.com/reference/andro
String
(https://developer.android.com/reference/java/lang/String)
FEATURE_LOCATION_GPS (https://developer.an
Feature for getSystemAvailableFeatures(
 (https://developer.android.com/reference/andro
String
(https://developer.android.com/reference/java/lang/String)
FEATURE_LOCATION_NETWORK (https://develop
Feature for getSystemAvailableFeatures(
 (https://developer.android.com/reference/andro
String
(https://developer.android.com/reference/java/lang/String)
FEATURE_MANAGED_USERS (https://developer.a
Feature for getSystemAvailableFeatures(
 (https://developer.android.com/reference/andro
 (https://developer.android.com/reference/andro


String
(https://developer.android.com/reference/java/lang/String)
FEATURE_MICROPHONE (https://developer.andro
Feature for getSystemAvailableFeatures(
 (https://developer.android.com/reference/andro
String
(https://developer.android.com/reference/java/lang/String)
FEATURE_MIDI (https://developer.android.com/
Feature for getSystemAvailableFeatures(
 (https://developer.android.com/reference/andro
String
(https://developer.android.com/reference/java/lang/String)
FEATURE_NEURAL_PROCESSING_UNIT (https://
Feature for getSystemAvailableFeatures(
 (https://developer.android.com/reference/andro
String
(https://developer.android.com/reference/java/lang/String)
FEATURE_NFC (https://developer.android.com/re
Feature for getSystemAvailableFeatures(
 (https://developer.android.com/reference/andro
String
(https://developer.android.com/reference/java/lang/String)
FEATURE_NFC_BEAM (https://developer.android.
Feature for getSystemAvailableFeatures(
 (https://developer.android.com/reference/andro
String
(https://developer.android.com/reference/java/lang/String)
FEATURE_NFC_HOST_CARD_EMULATION (https
Feature for getSystemAvailableFeatures(
 (https://developer.android.com/reference/andro
String
(https://developer.android.com/reference/java/lang/String)
FEATURE_NFC_HOST_CARD_EMULATION_NFCF
Feature for getSystemAvailableFeatures(
 (https://developer.android.com/reference/andro
String
(https://developer.android.com/reference/java/lang/String)
FEATURE_NFC_OFF_HOST_CARD_EMULATION_
Feature for getSystemAvailableFeatures(
 (https://developer.android.com/reference/andro


String
(https://developer.android.com/reference/java/lang/String)
FEATURE_NFC_OFF_HOST_CARD_EMULATION_
Feature for getSystemAvailableFeatures(
 (https://developer.android.com/reference/andro
String
(https://developer.android.com/reference/java/lang/String)
FEATURE_OPENGLES_DEQP_LEVEL (https://dev
Feature for getSystemAvailableFeatures(
 (https://developer.android.com/reference/andro
the OpenGLES dEQP test suite associated with th
String
(https://developer.android.com/reference/java/lang/String)
FEATURE_OPENGLES_EXTENSION_PACK (https
Feature for getSystemAvailableFeatures(
 (https://developer.android.com/reference/andro
 (http://www.khronos.org/registry/gles/extension
String
(https://developer.android.com/reference/java/lang/String)
FEATURE_PC (https://developer.android.com/ref
Feature for getSystemAvailableFeatures(
 (https://developer.android.com/reference/andro
String
(https://developer.android.com/reference/java/lang/String)
FEATURE_PICTURE_IN_PICTURE (https://deve
Feature for getSystemAvailableFeatures(
 (https://developer.android.com/reference/andro
String
(https://developer.android.com/reference/java/lang/String)
FEATURE_PRINTING (https://developer.android.
Feature for getSystemAvailableFeatures(
 (https://developer.android.com/reference/andro
String
(https://developer.android.com/reference/java/lang/String)
FEATURE_RAM_LOW (https://developer.android.c
Feature for getSystemAvailableFeatures(
 (https://developer.android.com/reference/andro
 (https://developer.android.com/reference/andro
String
(https://developer.android.com/reference/java/lang/String)
FEATURE_RAM_NORMAL (https://developer.andro
Feature for getSystemAvailableFeatures(
 (https://developer.android.com/reference/andro


 (https://developer.android.com/reference/andro
String
(https://developer.android.com/reference/java/lang/String)
FEATURE_SCREEN_LANDSCAPE (https://develop
Feature for getSystemAvailableFeatures(
 (https://developer.android.com/reference/andro
String
(https://developer.android.com/reference/java/lang/String)
FEATURE_SCREEN_PORTRAIT (https://develope
Feature for getSystemAvailableFeatures(
 (https://developer.android.com/reference/andro
String
(https://developer.android.com/reference/java/lang/String)
FEATURE_SECURELY_REMOVES_USERS (https://
Feature for getSystemAvailableFeatures(
 (https://developer.android.com/reference/andro
String
(https://developer.android.com/reference/java/lang/String)
FEATURE_SECURE_LOCK_SCREEN (https://deve
Feature for getSystemAvailableFeatures(
 (https://developer.android.com/reference/andro
password as defined in Android CDD
String
(https://developer.android.com/reference/java/lang/String)
FEATURE_SECURITY_MODEL_COMPATIBLE (htt
Feature for getSystemAvailableFeatures(
 (https://developer.android.com/reference/andro
String
(https://developer.android.com/reference/java/lang/String)
FEATURE_SENSOR_ACCELEROMETER (https://de
Feature for getSystemAvailableFeatures(
 (https://developer.android.com/reference/andro
String
(https://developer.android.com/reference/java/lang/String)
FEATURE_SENSOR_ACCELEROMETER_LIMITED
Feature for getSystemAvailableFeatures(
 (https://developer.android.com/reference/andro


String
(https://developer.android.com/reference/java/lang/String)
FEATURE_SENSOR_ACCELEROMETER_LIMITED
Feature for getSystemAvailableFeatures(
 (https://developer.android.com/reference/andro
String
(https://developer.android.com/reference/java/lang/String)
FEATURE_SENSOR_AMBIENT_TEMPERATURE (h
Feature for getSystemAvailableFeatures(
 (https://developer.android.com/reference/andro
String
(https://developer.android.com/reference/java/lang/String)
FEATURE_SENSOR_BAROMETER (https://develop
Feature for getSystemAvailableFeatures(
 (https://developer.android.com/reference/andro
String
(https://developer.android.com/reference/java/lang/String)
FEATURE_SENSOR_COMPASS (https://developer.
Feature for getSystemAvailableFeatures(
 (https://developer.android.com/reference/andro
String
(https://developer.android.com/reference/java/lang/String)
FEATURE_SENSOR_DYNAMIC_HEAD_TRACKER (
Feature for getSystemAvailableFeatures(
 (https://developer.android.com/reference/andro
String
(https://developer.android.com/reference/java/lang/String)
FEATURE_SENSOR_GYROSCOPE (https://develop
Feature for getSystemAvailableFeatures(
 (https://developer.android.com/reference/andro
String
(https://developer.android.com/reference/java/lang/String)
FEATURE_SENSOR_GYROSCOPE_LIMITED_AXE
Feature for getSystemAvailableFeatures(
 (https://developer.android.com/reference/andro
String
(https://developer.android.com/reference/java/lang/String)
FEATURE_SENSOR_GYROSCOPE_LIMITED_AXE
Feature for getSystemAvailableFeatures(
 (https://developer.android.com/reference/andro


String
(https://developer.android.com/reference/java/lang/String)
FEATURE_SENSOR_HEADING (https://developer.
Feature for getSystemAvailableFeatures(
 (https://developer.android.com/reference/andro
String
(https://developer.android.com/reference/java/lang/String)
FEATURE_SENSOR_HEART_RATE (https://develo
Feature for getSystemAvailableFeatures(
 (https://developer.android.com/reference/andro
String
(https://developer.android.com/reference/java/lang/String)
FEATURE_SENSOR_HEART_RATE_ECG (https://d
Feature for getSystemAvailableFeatures(
 (https://developer.android.com/reference/andro
String
(https://developer.android.com/reference/java/lang/String)
FEATURE_SENSOR_HINGE_ANGLE (https://deve
Feature for getSystemAvailableFeatures(
 (https://developer.android.com/reference/andro
String
(https://developer.android.com/reference/java/lang/String)
FEATURE_SENSOR_LIGHT (https://developer.an
Feature for getSystemAvailableFeatures(
 (https://developer.android.com/reference/andro
String
(https://developer.android.com/reference/java/lang/String)
FEATURE_SENSOR_PROXIMITY (https://develop
Feature for getSystemAvailableFeatures(
 (https://developer.android.com/reference/andro
String
(https://developer.android.com/reference/java/lang/String)
FEATURE_SENSOR_RELATIVE_HUMIDITY (http
Feature for getSystemAvailableFeatures(
 (https://developer.android.com/reference/andro
String
(https://developer.android.com/reference/java/lang/String)
FEATURE_SENSOR_STEP_COUNTER (https://dev
Feature for getSystemAvailableFeatures(
 (https://developer.android.com/reference/andro


String
(https://developer.android.com/reference/java/lang/String)
FEATURE_SENSOR_STEP_DETECTOR (https://de
Feature for getSystemAvailableFeatures(
 (https://developer.android.com/reference/andro
String
(https://developer.android.com/reference/java/lang/String)
FEATURE_SE_OMAPI_ESE (https://developer.an
Feature for getSystemAvailableFeatures(
 (https://developer.android.com/reference/andro
String
(https://developer.android.com/reference/java/lang/String)
FEATURE_SE_OMAPI_SD (https://developer.and
Feature for getSystemAvailableFeatures(
 (https://developer.android.com/reference/andro
String
(https://developer.android.com/reference/java/lang/String)
FEATURE_SE_OMAPI_UICC (https://developer.a
Feature for getSystemAvailableFeatures(
 (https://developer.android.com/reference/andro
String
(https://developer.android.com/reference/java/lang/String)
FEATURE_SIP (https://developer.android.com/re
Feature for getSystemAvailableFeatures(
 (https://developer.android.com/reference/andro
String
(https://developer.android.com/reference/java/lang/String)
FEATURE_SIP_VOIP (https://developer.android.
Feature for getSystemAvailableFeatures(
 (https://developer.android.com/reference/andro
String
(https://developer.android.com/reference/java/lang/String)
FEATURE_STRONGBOX_KEYSTORE (https://deve
Feature for getSystemAvailableFeatures(
 (https://developer.android.com/reference/andro
 (https://developer.android.com/reference/andro
secure processor referred to as StrongBox (https
String
(https://developer.android.com/reference/java/lang/String)
FEATURE_TELECOM (https://developer.android.c
Feature for getSystemAvailableFeatures(
 (https://developer.android.com/reference/andro


String
(https://developer.android.com/reference/java/lang/String)
FEATURE_TELEPHONY (https://developer.android
Feature for getSystemAvailableFeatures(
 (https://developer.android.com/reference/andro
String
(https://developer.android.com/reference/java/lang/String)
FEATURE_TELEPHONY_CALLING (https://develo
Feature for getSystemAvailableFeatures(
 (https://developer.android.com/reference/andro
String
(https://developer.android.com/reference/java/lang/String)
FEATURE_TELEPHONY_CDMA (https://developer.
Feature for getSystemAvailableFeatures(
 (https://developer.android.com/reference/andro
String
(https://developer.android.com/reference/java/lang/String)
FEATURE_TELEPHONY_DATA (https://developer.
Feature for getSystemAvailableFeatures(
 (https://developer.android.com/reference/andro
String
(https://developer.android.com/reference/java/lang/String)
FEATURE_TELEPHONY_EUICC (https://develope
Feature for getSystemAvailableFeatures(
 (https://developer.android.com/reference/andro
String
(https://developer.android.com/reference/java/lang/String)
FEATURE_TELEPHONY_EUICC_MEP (https://dev
Feature for getSystemAvailableFeatures(
 (https://developer.android.com/reference/andro
String
(https://developer.android.com/reference/java/lang/String)
FEATURE_TELEPHONY_GSM (https://developer.a
Feature for getSystemAvailableFeatures(
 (https://developer.android.com/reference/andro
String
(https://developer.android.com/reference/java/lang/String)
FEATURE_TELEPHONY_IMS (https://developer.a
Feature for getSystemAvailableFeatures(
 (https://developer.android.com/reference/andro


String
(https://developer.android.com/reference/java/lang/String)
FEATURE_TELEPHONY_MBMS (https://developer.
Feature for getSystemAvailableFeatures(
 (https://developer.android.com/reference/andro
String
(https://developer.android.com/reference/java/lang/String)
FEATURE_TELEPHONY_MESSAGING (https://dev
Feature for getSystemAvailableFeatures(
 (https://developer.android.com/reference/andro
String
(https://developer.android.com/reference/java/lang/String)
FEATURE_TELEPHONY_RADIO_ACCESS (https://
Feature for getSystemAvailableFeatures(
 (https://developer.android.com/reference/andro
String
(https://developer.android.com/reference/java/lang/String)
FEATURE_TELEPHONY_SUBSCRIPTION (https://
Feature for getSystemAvailableFeatures(
 (https://developer.android.com/reference/andro
String
(https://developer.android.com/reference/java/lang/String)
FEATURE_TELEVISION (https://developer.andro
This constant was deprecated in API level 21. use 
String
(https://developer.android.com/reference/java/lang/String)
FEATURE_THREAD_NETWORK (https://developer.
Feature for getSystemAvailableFeatures(
 (https://developer.android.com/reference/andro
networking protocol.
String
(https://developer.android.com/reference/java/lang/String)
FEATURE_TOUCHSCREEN (https://developer.and
Feature for getSystemAvailableFeatures(
 (https://developer.android.com/reference/andro
String
(https://developer.android.com/reference/java/lang/String)
FEATURE_TOUCHSCREEN_MULTITOUCH (https://
Feature for getSystemAvailableFeatures(
 (https://developer.android.com/reference/andro


String
(https://developer.android.com/reference/java/lang/String)
FEATURE_TOUCHSCREEN_MULTITOUCH_DISTI
Feature for getSystemAvailableFeatures(
 (https://developer.android.com/reference/andro
String
(https://developer.android.com/reference/java/lang/String)
FEATURE_TOUCHSCREEN_MULTITOUCH_JAZZH
Feature for getSystemAvailableFeatures(
 (https://developer.android.com/reference/andro
simultaneous independent pointers.
String
(https://developer.android.com/reference/java/lang/String)
FEATURE_USB_ACCESSORY (https://developer.a
Feature for getSystemAvailableFeatures(
 (https://developer.android.com/reference/andro
String
(https://developer.android.com/reference/java/lang/String)
FEATURE_USB_HOST (https://developer.android.
Feature for getSystemAvailableFeatures(
 (https://developer.android.com/reference/andro
String
(https://developer.android.com/reference/java/lang/String)
FEATURE_UWB (https://developer.android.com/re
Feature for getSystemAvailableFeatures(
 (https://developer.android.com/reference/andro
String
(https://developer.android.com/reference/java/lang/String)
FEATURE_VERIFIED_BOOT (https://developer.a
Feature for getSystemAvailableFeatures(
 (https://developer.android.com/reference/andro
String
(https://developer.android.com/reference/java/lang/String)
FEATURE_VR_HEADTRACKING (https://develope
Feature for getSystemAvailableFeatures(
 (https://developer.android.com/reference/andro
String
(https://developer.android.com/reference/java/lang/String)
FEATURE_VR_MODE (https://developer.android.c
This constant was deprecated in API level 28. use 


String
(https://developer.android.com/reference/java/lang/String)
FEATURE_VR_MODE_HIGH_PERFORMANCE (http
Feature for getSystemAvailableFeatures(
 (https://developer.android.com/reference/andro
rendering of notifications, disables most monocu
String
(https://developer.android.com/reference/java/lang/String)
FEATURE_VULKAN_DEQP_LEVEL (https://develo
Feature for getSystemAvailableFeatures(
 (https://developer.android.com/reference/andro
the Vulkan dEQP test suite associated with that d
String
(https://developer.android.com/reference/java/lang/String)
FEATURE_VULKAN_HARDWARE_COMPUTE (https
Feature for getSystemAvailableFeatures(
 (https://developer.android.com/reference/andro
the Vulkan native API will enumerate at least one
String
(https://developer.android.com/reference/java/lang/String)
FEATURE_VULKAN_HARDWARE_LEVEL (https://d
Feature for getSystemAvailableFeatures(
 (https://developer.android.com/reference/andro
the Vulkan native API will enumerate at least one
String
(https://developer.android.com/reference/java/lang/String)
FEATURE_VULKAN_HARDWARE_VERSION (https
Feature for getSystemAvailableFeatures(
 (https://developer.android.com/reference/andro
the feature version will indicate the highest VkPh
 (https://developer.android.com/reference/andro
String
(https://developer.android.com/reference/java/lang/String)
FEATURE_WALLET_LOCATION_BASED_SUGGES
Feature for getSystemAvailableFeatures(
 (https://developer.android.com/reference/andro
app.
String
(https://developer.android.com/reference/java/lang/String)
FEATURE_WATCH (https://developer.android.com
Feature for getSystemAvailableFeatures(
 (https://developer.android.com/reference/andro


String
(https://developer.android.com/reference/java/lang/String)
FEATURE_WEBVIEW (https://developer.android.c
Feature for getSystemAvailableFeatures(
 (https://developer.android.com/reference/andro
String
(https://developer.android.com/reference/java/lang/String)
FEATURE_WIFI (https://developer.android.com/
Feature for getSystemAvailableFeatures(
 (https://developer.android.com/reference/andro
String
(https://developer.android.com/reference/java/lang/String)
FEATURE_WIFI_AWARE (https://developer.andro
Feature for getSystemAvailableFeatures(
 (https://developer.android.com/reference/andro
String
(https://developer.android.com/reference/java/lang/String)
FEATURE_WIFI_DIRECT (https://developer.and
Feature for getSystemAvailableFeatures(
 (https://developer.android.com/reference/andro
String
(https://developer.android.com/reference/java/lang/String)
FEATURE_WIFI_PASSPOINT (https://developer.
Feature for getSystemAvailableFeatures(
 (https://developer.android.com/reference/andro
 (https://developer.android.com/reference/andro
String
(https://developer.android.com/reference/java/lang/String)
FEATURE_WIFI_RTT (https://developer.android.
Feature for getSystemAvailableFeatures(
 (https://developer.android.com/reference/andro
String
(https://developer.android.com/reference/java/lang/String)
FEATURE_WINDOW_MAGNIFICATION (https://de
Feature for getSystemAvailableFeatures(
 (https://developer.android.com/reference/andro
int
FLAG_PERMISSION_WHITELIST_INSTALLER (
Permission whitelist flag: permissions whitelisted


int
FLAG_PERMISSION_WHITELIST_SYSTEM (http
Permission whitelist flag: permissions whitelisted
int
FLAG_PERMISSION_WHITELIST_UPGRADE (htt
Permission whitelist flag: permissions whitelisted
int
GET_ACTIVITIES (https://developer.android.co
PackageInfo (https://developer.android.com/re
 (https://developer.android.com/reference/andro
int
GET_ATTRIBUTIONS (https://developer.android.
This constant was deprecated in API level 34. Use 
Operations with this flag may cause unintended re
long
GET_ATTRIBUTIONS_LONG (https://developer.a
PackageInfo (https://developer.android.com/re
int
GET_CONFIGURATIONS (https://developer.andro
PackageInfo (https://developer.android.com/re
 (https://developer.android.com/reference/andro
 (https://developer.android.com/reference/andro
int
GET_DISABLED_COMPONENTS (https://develope
This constant was deprecated in API level 24. repla
int
GET_DISABLED_UNTIL_USED_COMPONENTS (h
This constant was deprecated in API level 24. repla
 (https://developer.android.com/reference/andro
int
GET_GIDS (https://developer.android.com/refere
PackageInfo (https://developer.android.com/re
an application.


int
GET_INSTRUMENTATION (https://developer.and
PackageInfo (https://developer.android.com/re
 (https://developer.android.com/reference/andro
int
GET_INTENT_FILTERS (https://developer.andro
This constant was deprecated in API level 31. The 
int
GET_META_DATA (https://developer.android.com
ComponentInfo (https://developer.android.com
 (https://developer.android.com/reference/andro
int
GET_PERMISSIONS (https://developer.android.c
PackageInfo (https://developer.android.com/re
 (https://developer.android.com/reference/andro
int
GET_PROVIDERS (https://developer.android.com
PackageInfo (https://developer.android.com/re
 (https://developer.android.com/reference/andro
int
GET_RECEIVERS (https://developer.android.com
PackageInfo (https://developer.android.com/re
 (https://developer.android.com/reference/andro
int
GET_RESOLVED_FILTER (https://developer.and
ResolveInfo (https://developer.android.com/re
 (https://developer.android.com/reference/andro
int
GET_SERVICES (https://developer.android.com/
PackageInfo (https://developer.android.com/re
 (https://developer.android.com/reference/andro
int
GET_SHARED_LIBRARY_FILES (https://develop


ApplicationInfo (https://developer.android.c
 (https://developer.android.com/reference/andro
int
GET_SIGNATURES (https://developer.android.co
This constant was deprecated in API level 28. use 
int
GET_SIGNING_CERTIFICATES (https://develop
PackageInfo (https://developer.android.com/re
int
GET_UNINSTALLED_PACKAGES (https://develop
This constant was deprecated in API level 24. repla
int
GET_URI_PERMISSION_PATTERNS (https://dev
ProviderInfo (https://developer.android.com/
 (https://developer.android.com/reference/andro
int
INSTALL_REASON_DEVICE_RESTORE (https://d
Code indicating that this package was installed a
int
INSTALL_REASON_DEVICE_SETUP (https://dev
Code indicating that this package was installed a
int
INSTALL_REASON_POLICY (https://developer.a
Code indicating that this package was installed d
int
INSTALL_REASON_UNKNOWN (https://developer.
Code indicating that the reason for installing this
int
INSTALL_REASON_USER (https://developer.and
Code indicating that the package installation was


int
INSTALL_SCENARIO_BULK (https://developer.a
Installation scenario indicating a bulk operation w
int
INSTALL_SCENARIO_BULK_SECONDARY (https
Installation scenario indicating a bulk operation t
int
INSTALL_SCENARIO_DEFAULT (https://develop
A value to indicate the lack of CUJ information, d
int
INSTALL_SCENARIO_FAST (https://developer.a
Installation scenario providing the fastest "install
int
MATCH_ALL (https://developer.android.com/refe
Querying flag: if set and if the platform is doing a
int
MATCH_APEX (https://developer.android.com/ref
PackageInfo (https://developer.android.com/re
long
MATCH_ARCHIVED_PACKAGES (https://develope
Flag parameter to also retrieve some information
int
MATCH_DEFAULT_ONLY (https://developer.andro
Resolution and querying flag: if set, only filters th
int
MATCH_DIRECT_BOOT_AUTO (https://developer.
Querying flag: automatically match components 
int
MATCH_DIRECT_BOOT_AWARE (https://develope
Querying flag: match components which are direc


int
MATCH_DIRECT_BOOT_UNAWARE (https://develo
Querying flag: match components which are direc
int
MATCH_DISABLED_COMPONENTS (https://develo
PackageInfo (https://developer.android.com/re
int
MATCH_DISABLED_UNTIL_USED_COMPONENTS
PackageInfo (https://developer.android.com/re
 (https://developer.android.com/reference/andro
int
MATCH_SYSTEM_ONLY (https://developer.android
Querying flag: include only components from app
int
MATCH_UNINSTALLED_PACKAGES (https://deve
Flag parameter to retrieve some information abo
long
MAXIMUM_VERIFICATION_TIMEOUT (https://de
Can be used as the millisecondsToDelay arg
 (https://developer.android.com/reference/andro
int
PERMISSION_DENIED (https://developer.android
Permission check result: this is returned by chec
the permission has not been granted to the given
int
PERMISSION_GRANTED (https://developer.andro
Permission check result: this is returned by chec
the permission has been granted to the given pac
String
(https://developer.android.com/reference/java/lang/String)
PROPERTY_COMPAT_OVERRIDE_LANDSCAPE_T
Application level PackageManager .Property
compatibility treatment that rotates camera outp


String
(https://developer.android.com/reference/java/lang/String)
PROPERTY_MEDIA_CAPABILITIES (https://dev
<application> level PackageManager.Propert
file For example: <application> <property android
String
(https://developer.android.com/reference/java/lang/String)
PROPERTY_NATIVE_SERVICE_FUNCTION_NAM
Service level PackageManager.Property (http
service.
String
(https://developer.android.com/reference/java/lang/String)
PROPERTY_NATIVE_SERVICE_LIBRARY_NAME
Service level PackageManager.Property (http
hosts the service.
String
(https://developer.android.com/reference/java/lang/String)
PROPERTY_SELF_CERTIFIED_NETWORK_CAPA
<application> level PackageManager.Propert
network capabilities used by the application.
String
(https://developer.android.com/reference/java/lang/String)
PROPERTY_SPECIAL_USE_FGS_SUBTYPE (http
<service> level PackageManager.Property (h
ServiceInfo.FOREGROUND_SERVICE_TYPE_
String
(https://developer.android.com/reference/java/lang/String)
PROPERTY_USE_RESTRICTED_BACKUP_MODE (
<application> level PackageManager.Propert
it's started for backup and restore operations.
int
SIGNATURE_FIRST_NOT_SIGNED (https://deve
Signature check result: this is returned by check
second is.
int
SIGNATURE_MATCH (https://developer.android.c
Signature check result: this is returned by check
match.


int
SIGNATURE_NEITHER_SIGNED (https://develop
Signature check result: this is returned by check
int
SIGNATURE_NO_MATCH (https://developer.andro
Signature check result: this is returned by check
match.
int
SIGNATURE_SECOND_NOT_SIGNED (https://dev
Signature check result: this is returned by check
the first is.
int
SIGNATURE_UNKNOWN_PACKAGE (https://develo
Signature check result: this is returned by check
int
SYNCHRONOUS (https://developer.android.com/re
Flag parameter for setComponentEnabledSet
 (https://developer.android.com/reference/andro
serialised to disk after the component state has b
int
VERIFICATION_ALLOW (https://developer.andro
Used as the verificationCode argument for 
the calling package verifier allows the installation
int
VERIFICATION_REJECT (https://developer.and
Used as the verificationCode argument for 
calling package verifier does not vote to allow the
int
VERSION_CODE_HIGHEST (https://developer.an
Constant for specifying the highest installed pack


Fields
public static final List
(https://developer.android.com/reference/java/util/List)<Certificate
(https://developer.android.com/reference/java/security/cert/Certificate)
>
TRUST_ALL
 (https://developer.android.com/refe
Trust any Installer to provide checks
public static final List
(https://developer.android.com/reference/java/util/List)<Certificate
(https://developer.android.com/reference/java/security/cert/Certificate)
>
TRUST_NONE
 (https://developer.android.com/refe
Don't trust any Installer to provide ch
Public constructors
PackageManager
(https://developer.android.com/reference/android/content/pm/PackageManager#PackageManager())()
This constructor is deprecated. Do not instantiate or subclass - obtain an instance from
Context.getPackageManager
(https://developer.android.com/reference/android/content/Context#getPackageManager())
Public methods
abstract void
addPackageToP
This method was 
ResolveInfoFl
 (https://develope
see RoleManage
abstract boolean
addPermission
Add a new dynam
abstract boolean
addPermission


Like addPermis
return quicker an
abstract void
addPreferredA
 (https://develope
 (https://develope
This method was 
ResolveInfoFl
 (https://develope
see RoleManage
boolean
addWhiteliste
packageName, 
Adds a whiteliste
boolean
canPackageQue
 (https://develope
Returns true if t
boolean[]
canPackageQue
 (https://develope
Same as canPac
abstract boolean
canRequestPac
Checks whether t
abstract String[] (https://developer.android.com/reference/java/lang/String)
canonicalToCu
Map from a pack
abstract int
checkPermissi
 (https://develope
Check whether a 
abstract int
checkSignatur
 (https://develope


Compare the sign
abstract int
checkSignatur
Like checkSign
abstract void
clearInstantA
Clears the instan
abstract void
clearPackageP
This method was 
ResolveInfoFl
 (https://develope
see RoleManage
abstract String[] (https://developer.android.com/reference/java/lang/String)
currentToCano
Map from the cur
abstract void
extendVerific
Allows a package
timeout occurs.
abstract Drawable
(https://developer.android.com/reference/android/graphics/drawable/Drawable)
getActivityBa
Retrieve the bann
abstract Drawable
(https://developer.android.com/reference/android/graphics/drawable/Drawable)
getActivityBa
Retrieve the bann
abstract Drawable
(https://developer.android.com/reference/android/graphics/drawable/Drawable)
getActivityIc
Retrieve the icon 


abstract Drawable
(https://developer.android.com/reference/android/graphics/drawable/Drawable)
getActivityIc
Retrieve the icon 
abstract ActivityInfo
(https://developer.android.com/reference/android/content/pm/ActivityInfo)
getActivityIn
flags)
Retrieve all of the
ActivityInfo
(https://developer.android.com/reference/android/content/pm/ActivityInfo)
getActivityIn
 (https://develope
See getActivit
abstract Drawable
(https://developer.android.com/reference/android/graphics/drawable/Drawable)
getActivityLo
Retrieve the logo 
abstract Drawable
(https://developer.android.com/reference/android/graphics/drawable/Drawable)
getActivityLo
Retrieve the logo 
abstract List (https://developer.android.com/reference/java/util/List)<Permission
GroupInfo
(https://developer.android.com/reference/android/content/pm/PermissionGroupInfo)>
getAllPermiss
Retrieve all of the
int
getAppUidForP
Maps a Private C
abstract Drawable
(https://developer.android.com/reference/android/graphics/drawable/Drawable)
getApplicatio
Retrieve the bann
abstract Drawable
(https://developer.android.com/reference/android/graphics/drawable/Drawable)
getApplicatio
Retrieve the bann


abstract int
getApplicatio
Return the enable
abstract Drawable
(https://developer.android.com/reference/android/graphics/drawable/Drawable)
getApplicatio
Retrieve the icon 
abstract Drawable
(https://developer.android.com/reference/android/graphics/drawable/Drawable)
getApplicatio
Retrieve the icon 
ApplicationInfo
(https://developer.android.com/reference/android/content/pm/ApplicationInfo)
getApplicatio
packageName, 
See getApplica
abstract ApplicationInfo
(https://developer.android.com/reference/android/content/pm/ApplicationInfo)
getApplicatio
Retrieve all of the
abstract CharSequence
(https://developer.android.com/reference/java/lang/CharSequence)
getApplicatio
Return the label t
abstract Drawable
(https://developer.android.com/reference/android/graphics/drawable/Drawable)
getApplicatio
Retrieve the logo 
abstract Drawable
(https://developer.android.com/reference/android/graphics/drawable/Drawable)
getApplicatio
Retrieve the logo 
ArchivedPackageInfo
(https://developer.android.com/reference/android/content/pm/ArchivedPackageInfo)
getArchivedPa
Return archived p
CharSequence (https://developer.android.com/reference/java/lang/CharSequence)
getBackground
Gets the localized


abstract ChangedPackages
(https://developer.android.com/reference/android/content/pm/ChangedPackages)
getChangedPac
Returns the name
abstract int
getComponentE
 (https://develope
Return the enable
abstract Drawable
(https://developer.android.com/reference/android/graphics/drawable/Drawable)
getDefaultAct
Return the generi
abstract Drawable
(https://developer.android.com/reference/android/graphics/drawable/Drawable)
getDrawable (h
ApplicationIn
Retrieve an image
void
getGroupOfPla
 (https://develope
 (https://develope
Get the platform-
InstallSourceInfo
(https://developer.android.com/reference/android/content/pm/InstallSourceInfo)
getInstallSou
Retrieves informa
abstract List (https://developer.android.com/reference/java/util/List)<Application
Info (https://developer.android.com/reference/android/content/pm/ApplicationInfo)>
getInstalledA
Return a List of a
List (https://developer.android.com/reference/java/util/List)<ApplicationInfo
(https://developer.android.com/reference/android/content/pm/ApplicationInfo)>
getInstalledA
 (https://develope
See getInstal
List (https://developer.android.com/reference/java/util/List)<ModuleInfo
(https://developer.android.com/reference/android/content/pm/ModuleInfo)>
getInstalledM
Return a List of a


abstract List (https://developer.android.com/reference/java/util/List)<PackageInfo
(https://developer.android.com/reference/android/content/pm/PackageInfo)>
getInstalledP
Return a List of a
List (https://developer.android.com/reference/java/util/List)<PackageInfo
(https://developer.android.com/reference/android/content/pm/PackageInfo)>
getInstalledP
 (https://develope
See getInstal
abstract String (https://developer.android.com/reference/java/lang/String)
getInstallerP
This method was 
abstract byte[]
getInstantApp
Gets the instant a
abstract int
getInstantApp
Gets the maximu
abstract InstrumentationInfo
(https://developer.android.com/reference/android/content/pm/InstrumentationInfo)
getInstrument
className, in
Retrieve all of the
abstract Intent (https://developer.android.com/reference/android/content/Intent)
getLaunchInte
Returns a "good" 
IntentSender (https://developer.android.com/reference/android/content/IntentSender)
getLaunchInte
Returns an Inte
abstract Intent (https://developer.android.com/reference/android/content/Intent)
getLeanbackLa
Return a "good" in


Set (https://developer.android.com/reference/java/util/Set)<String
(https://developer.android.com/reference/java/lang/String)>
getMimeGroup
Gets all MIME typ
ModuleInfo (https://developer.android.com/reference/android/content/pm/ModuleInfo) getModuleInfo
Retrieve informat
abstract String (https://developer.android.com/reference/java/lang/String)
getNameForUid
Retrieve the offic
PackageInfo
(https://developer.android.com/reference/android/content/pm/PackageInfo)
getPackageArc
Retrieve overall in
 (https://develope
PackageInfo
(https://developer.android.com/reference/android/content/pm/PackageInfo)
getPackageArc
 (https://develope
See getPackage
abstract int[]
getPackageGid
Return an array o
abstract int[]
getPackageGid
Return an array o
int[]
getPackageGid
Name, Package
See getPackage
abstract PackageInfo
(https://developer.android.com/reference/android/content/pm/PackageInfo)
getPackageInf
Retrieve overall in


PackageInfo
(https://developer.android.com/reference/android/content/pm/PackageInfo)
getPackageInf
Name, Package
See getPackage
PackageInfo
(https://developer.android.com/reference/android/content/pm/PackageInfo)
getPackageInf
 (https://develope
See getPackage
abstract PackageInfo
(https://developer.android.com/reference/android/content/pm/PackageInfo)
getPackageInf
versionedPack
Retrieve overall in
abstract PackageInstaller
(https://developer.android.com/reference/android/content/pm/PackageInstaller)
getPackageIns
Return interface t
int
getPackageUid
Name, Package
See getPackage
abstract int
getPackageUid
Return the UID as
abstract String[] (https://developer.android.com/reference/java/lang/String)
getPackagesFo
Retrieve the nam
abstract List (https://developer.android.com/reference/java/util/List)<PackageInfo
(https://developer.android.com/reference/android/content/pm/PackageInfo)>
getPackagesHo
flags)
Return a List of a
List (https://developer.android.com/reference/java/util/List)<PackageInfo
(https://developer.android.com/reference/android/content/pm/PackageInfo)>
getPackagesHo
 (https://develope
See getPackage


abstract PermissionGroupInfo
(https://developer.android.com/reference/android/content/pm/PermissionGroupInfo)
getPermission
Retrieve all of the
abstract PermissionInfo
(https://developer.android.com/reference/android/content/pm/PermissionInfo)
getPermission
Retrieve all of the
void
getPlatformPe
 (https://develope
 (https://develope
 (https://develope
Get the platform-
abstract int
getPreferredA
 (https://develope
 (https://develope
This method was 
ResolveInfoFl
 (https://develope
see RoleManage
abstract List (https://developer.android.com/reference/java/util/List)<PackageInfo
(https://developer.android.com/reference/android/content/pm/PackageInfo)>
getPreferredP
This method was 
ResolveInfoFl
 (https://develope
see RoleManage
PackageManager.Property
(https://developer.android.com/reference/android/content/pm/PackageManager.Property)
getProperty (h
 (https://develope
Returns the prope
PackageManager.Property
(https://developer.android.com/reference/android/content/pm/PackageManager.Property)
getProperty (h
 (https://develope
Returns the prope


abstract ProviderInfo
(https://developer.android.com/reference/android/content/pm/ProviderInfo)
getProviderIn
flags)
Retrieve all of the
ProviderInfo
(https://developer.android.com/reference/android/content/pm/ProviderInfo)
getProviderIn
 (https://develope
See getProvide
abstract ActivityInfo
(https://developer.android.com/reference/android/content/pm/ActivityInfo)
getReceiverIn
int flags)
Retrieve all of the
ActivityInfo
(https://developer.android.com/reference/android/content/pm/ActivityInfo)
getReceiverIn
 (https://develope
See getReceive
abstract Resources
(https://developer.android.com/reference/android/content/res/Resources)
getResourcesF
activityName)
Retrieve the reso
abstract Resources
(https://developer.android.com/reference/android/content/res/Resources)
getResourcesF
 (https://develope
Retrieve the reso
abstract Resources
(https://developer.android.com/reference/android/content/res/Resources)
getResourcesF
Retrieve the reso
Resources (https://developer.android.com/reference/android/content/res/Resources)
getResourcesF
 (https://develope
Retrieve the reso
ServiceInfo (https://developer.android.com/reference/android/content/pm/ServiceInfo) getServiceInf
 (https://develope


See getService
abstract ServiceInfo
(https://developer.android.com/reference/android/content/pm/ServiceInfo)
getServiceInf
flags)
Retrieve all of the
List (https://developer.android.com/reference/java/util/List)<SharedLibraryInfo
(https://developer.android.com/reference/android/content/pm/SharedLibraryInfo)>
getSharedLibr
 (https://develope
See getShared
abstract List (https://developer.android.com/reference/java/util/List)<Shared
LibraryInfo
(https://developer.android.com/reference/android/content/pm/SharedLibraryInfo)>
getSharedLibr
Get a list of share
Bundle (https://developer.android.com/reference/android/os/Bundle)
getSuspendedP
Returns a Bundl
boolean
getSyntheticA
Return whether a
abstract FeatureInfo[]
(https://developer.android.com/reference/android/content/pm/FeatureInfo)
getSystemAvai
Get a list of featu
abstract String[] (https://developer.android.com/reference/java/lang/String)
getSystemShar
Get a list of share
int
getTargetSdkV
abstract CharSequence
(https://developer.android.com/reference/java/lang/CharSequence)
getText (https:/
ApplicationIn
Retrieve text from


abstract Drawable
(https://developer.android.com/reference/android/graphics/drawable/Drawable)
getUserBadged
 (https://develope
int badgeDens
If the target user 
abstract Drawable
(https://developer.android.com/reference/android/graphics/drawable/Drawable)
getUserBadged
 (https://develope
If the target user 
abstract CharSequence
(https://developer.android.com/reference/java/lang/CharSequence)
getUserBadged
UserHandle (ht
If the target user 
static SigningInfo
(https://developer.android.com/reference/android/content/pm/SigningInfo)
getVerifiedSi
Version)
Verifies and retur
Set (https://developer.android.com/reference/java/util/Set)<String
(https://developer.android.com/reference/java/lang/String)>
getWhiteliste
int whitelist
Gets the restricte
abstract XmlResourceParser
(https://developer.android.com/reference/android/content/res/XmlResourceParser)
getXml (https://
ApplicationIn
Retrieve an XML 
boolean
hasSigningCer
Searches the set 
boolean
hasSigningCer
certificate, 
Searches the set 


abstract boolean
hasSystemFeat
Check whether th
abstract boolean
hasSystemFeat
Check whether th
boolean
isAppArchivab
Returns true if an
boolean
isAutoRevokeW
Checks whether a
boolean
isAutoRevokeW
Note: In retrospe
boolean
isDefaultAppl
drawable)
Returns if the pro
boolean
isDeviceUpgra
Returns true if the
abstract boolean
isInstantApp
Gets whether this
abstract boolean
isInstantApp
Gets whether the
boolean
isPackageStop
Query if an app is


boolean
isPackageSusp
Query if an app is
boolean
isPackageSusp
Apps can query t
abstract boolean
isPermissionR
 (https://develope
Checks whether a
abstract boolean
isSafeMode (ht
Return whether th
<T> T
parseAndroidM
 (https://develope
Function)
Retrieve AndroidM
<T> T
parseAndroidM
 (https://develope
 (https://develope
Similar to parse
descriptor instea
List (https://developer.android.com/reference/java/util/List)<PackageManager.
Property
(https://developer.android.com/reference/android/content/pm/PackageManager.Property)
>
queryActivity
Returns the prope
List (https://developer.android.com/reference/java/util/List)<PackageManager.
Property
(https://developer.android.com/reference/android/content/pm/PackageManager.Property)
>
queryApplicat
Returns the prope


List (https://developer.android.com/reference/java/util/List)<ResolveInfo
(https://developer.android.com/reference/android/content/pm/ResolveInfo)>
queryBroadcas
 (https://develope
See queryBroad
abstract List (https://developer.android.com/reference/java/util/List)<ResolveInfo
(https://developer.android.com/reference/android/content/pm/ResolveInfo)>
queryBroadcas
Retrieve all receiv
abstract List (https://developer.android.com/reference/java/util/List)<Provider
Info (https://developer.android.com/reference/android/content/pm/ProviderInfo)>
queryContentP
flags)
Retrieve content 
List (https://developer.android.com/reference/java/util/List)<ProviderInfo
(https://developer.android.com/reference/android/content/pm/ProviderInfo)>
queryContentP
 (https://develope
See queryConte
abstract List (https://developer.android.com/reference/java/util/List)
<InstrumentationInfo
(https://developer.android.com/reference/android/content/pm/InstrumentationInfo)>
queryInstrume
Retrieve informat
List (https://developer.android.com/reference/java/util/List)<ResolveInfo
(https://developer.android.com/reference/android/content/pm/ResolveInfo)>
queryIntentAc
 (https://develope
See queryInten
abstract List (https://developer.android.com/reference/java/util/List)<ResolveInfo
(https://developer.android.com/reference/android/content/pm/ResolveInfo)>
queryIntentAc
Retrieve all activi
abstract List (https://developer.android.com/reference/java/util/List)<ResolveInfo
(https://developer.android.com/reference/android/content/pm/ResolveInfo)>
queryIntentAc
 (https://develope
flags)
Retrieve a set of 
List (https://developer.android.com/reference/java/util/List)<ResolveInfo
(https://developer.android.com/reference/android/content/pm/ResolveInfo)>
queryIntentAc
 (https://develope


(ComponentNam
 (https://develope
See queryInten
 (https://develope
List (https://developer.android.com/reference/java/util/List)<ResolveInfo
(https://developer.android.com/reference/android/content/pm/ResolveInfo)>
queryIntentCo
 (https://develope
See queryInten
abstract List (https://developer.android.com/reference/java/util/List)<ResolveInfo
(https://developer.android.com/reference/android/content/pm/ResolveInfo)>
queryIntentCo
flags)
Retrieve all provid
abstract List (https://developer.android.com/reference/java/util/List)<ResolveInfo
(https://developer.android.com/reference/android/content/pm/ResolveInfo)>
queryIntentSe
Retrieve all servic
List (https://developer.android.com/reference/java/util/List)<ResolveInfo
(https://developer.android.com/reference/android/content/pm/ResolveInfo)>
queryIntentSe
 (https://develope
See queryInten
abstract List (https://developer.android.com/reference/java/util/List)<Permission
Info (https://developer.android.com/reference/android/content/pm/PermissionInfo)>
queryPermissi
Query for all of th
List (https://developer.android.com/reference/java/util/List)<PackageManager.
Property
(https://developer.android.com/reference/android/content/pm/PackageManager.Property)
>
queryProvider
Returns the prope
List (https://developer.android.com/reference/java/util/List)<PackageManager.
Property
(https://developer.android.com/reference/android/content/pm/PackageManager.Property)
>
queryReceiver
Returns the prope


List (https://developer.android.com/reference/java/util/List)<PackageManager.
Property
(https://developer.android.com/reference/android/content/pm/PackageManager.Property)
>
queryServiceP
Returns the prope
void
relinquishUpd
Attempt to relinq
abstract void
removePackage
This method was 
ResolveInfoFl
 (https://develope
see RoleManage
abstract void
removePermiss
Removes a perm
boolean
removeWhiteli
 (https://develope
Removes a white
void
requestChecks
 (https://develope
 (https://develope
> trustedInst
Requests the che
ResolveInfo
(https://developer.android.com/reference/android/content/pm/ResolveInfo)
resolveActivi
intent, Packa
See resolveAct
abstract ResolveInfo
(https://developer.android.com/reference/android/content/pm/ResolveInfo)
resolveActivi
Determine the be


ProviderInfo
(https://developer.android.com/reference/android/content/pm/ProviderInfo)
resolveConten
 (https://develope
See resolveCon
abstract ProviderInfo
(https://developer.android.com/reference/android/content/pm/ProviderInfo)
resolveConten
Find a single con
abstract ResolveInfo
(https://developer.android.com/reference/android/content/pm/ResolveInfo)
resolveServic
Determine the be
ResolveInfo
(https://developer.android.com/reference/android/content/pm/ResolveInfo)
resolveServic
intent, Packa
See resolveSe
abstract void
setApplicatio
Hint)
Provide a hint of 
abstract void
setApplicatio
State, int fl
Set the enabled s
boolean
setAutoRevoke
whitelisted)
Marks an applica
abstract void
setComponentE
 (https://develope
Set the enabled s
void
setComponentE
 (https://develope


Set the enabled s
abstract void
setInstallerP
 (https://develope
Change the insta
void
setMimeGroup
 (https://develope
Sets MIME group
abstract void
updateInstant
Updates the insta
abstract void
verifyPending
Allows a package
Inherited methods
Object (https://developer.android.com/reference/java/lang/Object)
clone (https://developer.an
Creates and returns a copy o
boolean
equals
 (https://developer.android.c
(Object (https://developer
Indicates whether some oth
void
finalize (https://develope
Called by the garbage collec
there are no more references
final Class (https://developer.android.com/reference/java/lang/Class)<?>getClass (https://develope
From class java.lang.Object (https://developer.android.com/reference/java/lang/Object)


Returns the runtime class of
int
hashCode (https://develope
()
Returns a hash code value fo
final void
notify (https://developer.a
Wakes up a single thread tha
final void
notifyAll (https://develop
()
Wakes up all threads that ar
String (https://developer.android.com/reference/java/lang/String)
toString (https://develope
Returns a string representat
final void
wait (https://developer.and
(long timeoutMillis, 
Causes the current thread to
interrupted, or until a certain
final void
wait (https://developer.and
timeoutMillis)
Causes the current thread to
interrupted, or until a certain
final void
wait (https://developer.and
Causes the current thread to
interrupted.
Constants


Added in API level 28 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Added in API level 28 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Added in API level 1 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
CERT_INPUT_RAW_X509
Certificate input bytes: the input bytes represent an encoded X.509 Certificate which could be
generated using an CertificateFactory
Constant Value: 0 (0x00000000)
CERT_INPUT_SHA256
Certificate input bytes: the input bytes represent the SHA256 output of an encoded X.509
Certificate.
Constant Value: 1 (0x00000001)
COMPONENT_ENABLED_STATE_DEFAULT
Flag for setApplicationEnabledSetting(String,int,int)
(https://developer.android.com/reference/android/content/pm/PackageManager#setApplicationEnabledSe
tting(java.lang.String,%20int,%20int))
and setComponentEnabledSetting(ComponentName,int,int)
public static final int CERT_INPUT_RAW_X509
public static final int CERT_INPUT_SHA256
public static final int COMPONENT_ENABLED_STATE_DEFAULT


Added in API level 1 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Added in API level 18 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
(https://developer.android.com/reference/android/content/pm/PackageManager#setComponentEnabledSe
tting(android.content.ComponentName,%20int,%20int))
: This component or application is in its default enabled state (as specified in its manifest).
Explicitly setting the component state to this value restores it's enabled state to whatever is set
in the manifest.
Constant Value: 0 (0x00000000)
COMPONENT_ENABLED_STATE_DISABLED
Flag for setApplicationEnabledSetting(String,int,int)
(https://developer.android.com/reference/android/content/pm/PackageManager#setApplicationEnabledSe
tting(java.lang.String,%20int,%20int))
and setComponentEnabledSetting(ComponentName,int,int)
(https://developer.android.com/reference/android/content/pm/PackageManager#setComponentEnabledSe
tting(android.content.ComponentName,%20int,%20int))
: This component or application has been explicitly disabled, regardless of what it has specified
in its manifest.
Constant Value: 2 (0x00000002)
COMPONENT_ENABLED_STATE_DISABLED_UNTIL_USED
Flag for setApplicationEnabledSetting(String,int,int)
(https://developer.android.com/reference/android/content/pm/PackageManager#setApplicationEnabledSe
tting(java.lang.String,%20int,%20int))
public static final int COMPONENT_ENABLED_STATE_DISABLED
public static final int COMPONENT_ENABLED_STATE_DISABLED_UNTIL_USED


Added in API level 14 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Added in API level 1 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
only: This application should be considered, until the point where the user actually wants to use
it. This means that it will not normally show up to the user (such as in the launcher), but various
parts of the user interface can use GET_DISABLED_UNTIL_USED_COMPONENTS
(https://developer.android.com/reference/android/content/pm/PackageManager#GET_DISABLED_UNTIL_U
SED_COMPONENTS)
to still see it and allow the user to select it (as for example an IME, device admin, etc). Such
code, once the user has selected the app, should at that point also make it enabled. This option
currently can not be used with setComponentEnabledSetting(ComponentName,int,int)
(https://developer.android.com/reference/android/content/pm/PackageManager#setComponentEnabledSe
tting(android.content.ComponentName,%20int,%20int))
.
Constant Value: 4 (0x00000004)
COMPONENT_ENABLED_STATE_DISABLED_USER
Flag for setApplicationEnabledSetting(String,int,int)
(https://developer.android.com/reference/android/content/pm/PackageManager#setApplicationEnabledSe
tting(java.lang.String,%20int,%20int))
only: The user has explicitly disabled the application, regardless of what it has specified in its
manifest. Because this is due to the user's request, they may re-enable it if desired through the
appropriate system UI. This option currently cannot be used with
setComponentEnabledSetting(ComponentName,int,int)
(https://developer.android.com/reference/android/content/pm/PackageManager#setComponentEnabledSe
tting(android.content.ComponentName,%20int,%20int))
.
Constant Value: 3 (0x00000003)
COMPONENT_ENABLED_STATE_ENABLED
public static final int COMPONENT_ENABLED_STATE_DISABLED_USER


Added in API level 35 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Added in API level 1 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Flag for setApplicationEnabledSetting(String,int,int)
(https://developer.android.com/reference/android/content/pm/PackageManager#setApplicationEnabledSe
tting(java.lang.String,%20int,%20int))
and setComponentEnabledSetting(ComponentName,int,int)
(https://developer.android.com/reference/android/content/pm/PackageManager#setComponentEnabledSe
tting(android.content.ComponentName,%20int,%20int))
: This component or application has been explictily enabled, regardless of what it has specified
in its manifest.
Constant Value: 1 (0x00000001)
DELETE_ARCHIVE
Flag parameter for PackageInstaller.uninstall(VersionedPackage,int,IntentSender)
(https://developer.android.com/reference/android/content/pm/PackageInstaller#uninstall(android.content.
pm.VersionedPackage,%20int,%20android.content.IntentSender))
to indicate that the deletion is an archival. This flag is only for internal usage as part of
PackageInstaller.requestArchive
(https://developer.android.com/reference/android/content/pm/PackageInstaller#requestArchive(java.lang.
String,%20android.content.IntentSender))
.
Constant Value: 16 (0x00000010)
DONT_KILL_APP
public static final int COMPONENT_ENABLED_STATE_ENABLED
public static final int DELETE_ARCHIVE


Added in API level 14 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Added in API level 17 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Flag parameter for setComponentEnabledSetting(android.content.ComponentName, int,
int)
(https://developer.android.com/reference/android/content/pm/PackageManager#setComponentEnabledSe
tting(android.content.ComponentName,%20int,%20int))
to indicate that you don't want to kill the app containing the component. Be careful when you
set this since changing component states can make the containing application's behavior
unpredictable.
Constant Value: 1 (0x00000001)
EXTRA_VERIFICATION_ID
Extra field name for the ID of a package pending verification. Passed to a package verifier and
is used to call back to PackageManager.verifyPendingInstall(int,int)
(https://developer.android.com/reference/android/content/pm/PackageManager#verifyPendingInstall(int,%
20int))
Constant Value: "android.content.pm.extra.VERIFICATION_ID"
EXTRA_VERIFICATION_RESULT
public static final int DONT_KILL_APP
public static final String (https://developer.android.com/reference/java/lang/String) EXTRA_VER
public static final String (https://developer.android.com/reference/java/lang/String) EXTRA_VER


Added in API level 26 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Added in API level 18 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Extra field name for the result of a verification, either VERIFICATION_ALLOW
(https://developer.android.com/reference/android/content/pm/PackageManager#VERIFICATION_ALLOW),
or VERIFICATION_REJECT
(https://developer.android.com/reference/android/content/pm/PackageManager#VERIFICATION_REJECT).
Passed to package verifiers after a package is verified.
Constant Value: "android.content.pm.extra.VERIFICATION_RESULT"
FEATURE_ACTIVITIES_ON_SECONDARY_DISPLAYS
Feature for getSystemAvailableFeatures()
(https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatu
res())
and hasSystemFeature(String)
(https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.l
ang.String))
: The device supports running activities on secondary displays. Displays here refers to both
physical and virtual displays. Disabling this feature can impact support for application
projection use-cases and support for virtual devices on the device.
Constant Value: "android.software.activities_on_secondary_displays"
FEATURE_APP_WIDGETS
public static final String (https://developer.android.com/reference/java/lang/String) FEATURE_A
public static final String (https://developer.android.com/reference/java/lang/String) FEATURE_A


Added in API level 9 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Added in API level 21 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Feature for getSystemAvailableFeatures()
(https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatu
res())
and hasSystemFeature(String)
(https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.l
ang.String))
: The device supports app widgets.
Constant Value: "android.software.app_widgets"
FEATURE_AUDIO_LOW_LATENCY
Feature for getSystemAvailableFeatures()
(https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatu
res())
and hasSystemFeature(String)
(https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.l
ang.String))
: The device's audio pipeline is low-latency, more suitable for audio applications sensitive to
delays or lag in sound input or output.
Constant Value: "android.hardware.audio.low_latency"
FEATURE_AUDIO_OUTPUT
public static final String (https://developer.android.com/reference/java/lang/String) FEATURE_A
public static final String (https://developer.android.com/reference/java/lang/String) FEATURE_A


Added in API level 23 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Added in API level 36 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Feature for getSystemAvailableFeatures()
(https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatu
res())
and hasSystemFeature(String)
(https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.l
ang.String))
: The device includes at least one form of audio output, as defined in the Android Compatibility
Definition Document (CDD) section 7.8 Audio
(https://source.android.com/compatibility/android-cdd#7_8_audio).
Constant Value: "android.hardware.audio.output"
FEATURE_AUDIO_PRO
Feature for getSystemAvailableFeatures()
(https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatu
res())
and hasSystemFeature(String)
(https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.l
ang.String))
: The device has professional audio level of functionality and performance.
Constant Value: "android.hardware.audio.pro"
FEATURE_AUDIO_SPATIAL_HEADTRACKING_LOW_LATENCY
public static final String (https://developer.android.com/reference/java/lang/String) FEATURE_A
public static final String (https://developer.android.com/reference/java/lang/String) FEATURE_A


Added in API level 26 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Added in API level 23 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Feature for getSystemAvailableFeatures()
(https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatu
res())
and hasSystemFeature(String)
(https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.l
ang.String))
which indicates whether head tracking for spatial audio operates with low-latency, as defined
by the CDD criteria for the feature.
Constant Value: "android.hardware.audio.spatial.headtracking.low_latency"
FEATURE_AUTOFILL
Feature for getSystemAvailableFeatures()
(https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatu
res())
and hasSystemFeature(String)
(https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.l
ang.String))
: The device supports autofill of user credentials, addresses, credit cards, etc via integration
with autofill providers
(https://developer.android.com/reference/android/service/autofill/AutofillService).
Constant Value: "android.software.autofill"
FEATURE_AUTOMOTIVE
public static final String (https://developer.android.com/reference/java/lang/String) FEATURE_A
public static final String (https://developer.android.com/reference/java/lang/String) FEATURE_A


Added in API level 20 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Added in API level 8 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Feature for getSystemAvailableFeatures()
(https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatu
res())
and hasSystemFeature(String)
(https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.l
ang.String))
: This is a device dedicated to showing UI on a vehicle headunit. A headunit here is defined to
be inside a vehicle that may or may not be moving. A headunit uses either a primary display in
the center console and/or additional displays in the instrument cluster or elsewhere in the
vehicle. Headunit display(s) have limited size and resolution. The user will likely be focused on
driving so limiting driver distraction is a primary concern. User input can be a variety of hard
buttons, touch, rotary controllers and even mouse- like interfaces.
Constant Value: "android.hardware.type.automotive"
FEATURE_BACKUP
Feature for getSystemAvailableFeatures()
(https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatu
res())
and hasSystemFeature(String)
(https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.l
ang.String))
: The device can perform backup and restore operations on installed applications.
Constant Value: "android.software.backup"
FEATURE_BLUETOOTH
public static final String (https://developer.android.com/reference/java/lang/String) FEATURE_B


Added in API level 18 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Added in API level 36 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Feature for getSystemAvailableFeatures()
(https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatu
res())
and hasSystemFeature(String)
(https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.l
ang.String))
: The device is capable of communicating with other devices via Bluetooth.
Constant Value: "android.hardware.bluetooth"
FEATURE_BLUETOOTH_LE
Feature for getSystemAvailableFeatures()
(https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatu
res())
and hasSystemFeature(String)
(https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.l
ang.String))
: The device is capable of communicating with other devices via Bluetooth Low Energy radio.
Constant Value: "android.hardware.bluetooth_le"
FEATURE_BLUETOOTH_LE_CHANNEL_SOUNDING
public static final String (https://developer.android.com/reference/java/lang/String) FEATURE_B
public static final String (https://developer.android.com/reference/java/lang/String) FEATURE_B


Added in API level 7 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Added in API level 17 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Feature for getSystemAvailableFeatures()
(https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatu
res())
and hasSystemFeature(String)
(https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.l
ang.String))
: The device is capable of ranging with other devices using channel sounding via Bluetooth Low
Energy radio.
Constant Value: "android.hardware.bluetooth_le.channel_sounding"
FEATURE_CAMERA
Feature for getSystemAvailableFeatures()
(https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatu
res())
and hasSystemFeature(String)
(https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.l
ang.String))
: The device has a camera facing away from the screen.
Constant Value: "android.hardware.camera"
FEATURE_CAMERA_ANY
public static final String (https://developer.android.com/reference/java/lang/String) FEATURE_B
public static final String (https://developer.android.com/reference/java/lang/String) FEATURE_C


Added in API level 28 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Feature for getSystemAvailableFeatures()
(https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatu
res())
and hasSystemFeature(String)
(https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.l
ang.String))
: The device has at least one camera pointing in some direction, or can support an external or a
virtual (https://developer.android.com/reference/android/companion/virtual/VirtualDevice) camera
being connected to it.
Constant Value: "android.hardware.camera.any"
FEATURE_CAMERA_AR
Feature for getSystemAvailableFeatures()
(https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatu
res())
and hasSystemFeature(String)
(https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.l
ang.String))
: At least one of the cameras on the device supports the MOTION_TRACKING
(https://developer.android.com/reference/android/hardware/camera2/CameraMetadata#REQUEST_AVAILA
BLE_CAPABILITIES_MOTION_TRACKING)
capability level.
Constant Value: "android.hardware.camera.ar"
public static final String (https://developer.android.com/reference/java/lang/String) FEATURE_C
public static final String (https://developer.android.com/reference/java/lang/String) FEATURE_C


Added in API level 7 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Added in API level 21 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
FEATURE_CAMERA_AUTOFOCUS
Feature for getSystemAvailableFeatures()
(https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatu
res())
and hasSystemFeature(String)
(https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.l
ang.String))
: The device's camera supports auto-focus.
Constant Value: "android.hardware.camera.autofocus"
FEATURE_CAMERA_CAPABILITY_MANUAL_POST_PROCESSING
Feature for getSystemAvailableFeatures()
(https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatu
res())
and hasSystemFeature(String)
(https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.l
ang.String))
: At least one of the cameras on the device supports the manual post-processing
(https://developer.android.com/reference/android/hardware/camera2/CameraMetadata#REQUEST_AVAILA
BLE_CAPABILITIES_MANUAL_POST_PROCESSING)
capability level.
Constant Value: "android.hardware.camera.capability.manual_post_processing"
public static final String (https://developer.android.com/reference/java/lang/String) FEATURE_C
public static final String (https://developer.android.com/reference/java/lang/String) FEATURE_C


Added in API level 21 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Added in API level 21 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
FEATURE_CAMERA_CAPABILITY_MANUAL_SENSOR
Feature for getSystemAvailableFeatures()
(https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatu
res())
and hasSystemFeature(String)
(https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.l
ang.String))
: At least one of the cameras on the device supports the manual sensor
(https://developer.android.com/reference/android/hardware/camera2/CameraMetadata#REQUEST_AVAILA
BLE_CAPABILITIES_MANUAL_SENSOR)
capability level.
Constant Value: "android.hardware.camera.capability.manual_sensor"
FEATURE_CAMERA_CAPABILITY_RAW
Feature for getSystemAvailableFeatures()
(https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatu
res())
and hasSystemFeature(String)
(https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.l
ang.String))
: At least one of the cameras on the device supports the RAW
(https://developer.android.com/reference/android/hardware/camera2/CameraMetadata#REQUEST_AVAILA
BLE_CAPABILITIES_RAW)
capability level.
public static final String (https://developer.android.com/reference/java/lang/String) FEATURE_C
public static final String (https://developer.android.com/reference/java/lang/String) FEATURE_C


Added in API level 30 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Constant Value: "android.hardware.camera.capability.raw"
FEATURE_CAMERA_CONCURRENT
Feature for getSystemAvailableFeatures()
(https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatu
res())
and hasSystemFeature(String)
(https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.l
ang.String))
: The device's main front and back cameras can stream concurrently as described in
CameraManager.getConcurrentCameraIds()
(https://developer.android.com/reference/android/hardware/camera2/CameraManager#getConcurrentCam
eraIds())
.
While CameraManager.getConcurrentCameraIds()
(https://developer.android.com/reference/android/hardware/camera2/CameraManager#getConcurrentCam
eraIds())
and associated APIs are only available on API level 30 or newer, this feature flag may be
advertised by devices on API levels below 30. If present on such a device, the same guarantees
hold: The main front and main back camera can be used at the same time, with guaranteed
stream configurations as defined in the table for concurrent streaming at
CameraDevice.createCaptureSession(android.hardware.camera2.params.SessionConf
iguration)
(https://developer.android.com/reference/android/hardware/camera2/CameraDevice#createCaptureSessio
n(android.hardware.camera2.params.SessionConfiguration))
.
Constant Value: "android.hardware.camera.concurrent"
public static final String (https://developer.android.com/reference/java/lang/String) FEATURE_C


Added in API level 20 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Added in API level 7 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Added in API level 9 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
FEATURE_CAMERA_EXTERNAL
Feature for getSystemAvailableFeatures()
(https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatu
res())
and hasSystemFeature(String)
(https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.l
ang.String))
: The device can support having an external camera connected to it. The external camera may
not always be connected or available to applications to use.
Constant Value: "android.hardware.camera.external"
FEATURE_CAMERA_FLASH
Feature for getSystemAvailableFeatures()
(https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatu
res())
and hasSystemFeature(String)
(https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.l
ang.String))
: The device's camera supports flash.
Constant Value: "android.hardware.camera.flash"
FEATURE_CAMERA_FRONT
public static final String (https://developer.android.com/reference/java/lang/String) FEATURE_C
public static final String (https://developer.android.com/reference/java/lang/String) FEATURE_C


Added in API level 21 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Added in API level 28 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Feature for getSystemAvailableFeatures()
(https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatu
res())
and hasSystemFeature(String)
(https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.l
ang.String))
: The device has a front facing camera.
Constant Value: "android.hardware.camera.front"
FEATURE_CAMERA_LEVEL_FULL
Feature for getSystemAvailableFeatures()
(https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatu
res())
and hasSystemFeature(String)
(https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.l
ang.String))
: At least one of the cameras on the device supports the full hardware
(https://developer.android.com/reference/android/hardware/camera2/CameraCharacteristics#INFO_SUPP
ORTED_HARDWARE_LEVEL)
capability level.
Constant Value: "android.hardware.camera.level.full"
FEATURE_CANT_SAVE_STATE
public static final String (https://developer.android.com/reference/java/lang/String) FEATURE_C
public static final String (https://developer.android.com/reference/java/lang/String) FEATURE_C


Added in API level 26 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Feature for getSystemAvailableFeatures()
(https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatu
res())
and hasSystemFeature(String)
(https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.l
ang.String))
: The device supports the R.attr.cantSaveState
(https://developer.android.com/reference/android/R.attr#cantSaveState) API.
Constant Value: "android.software.cant_save_state"
FEATURE_COMPANION_DEVICE_SETUP
Feature for getSystemAvailableFeatures()
(https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatu
res())
and hasSystemFeature(String)
(https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.l
ang.String))
: The device supports associating
(https://developer.android.com/reference/android/companion/CompanionDeviceManager#associate(andro
id.companion.AssociationRequest,%20android.companion.CompanionDeviceManager.Callback,%20android.
os.Handler))
with devices via CompanionDeviceManager
(https://developer.android.com/reference/android/companion/CompanionDeviceManager).
Constant Value: "android.software.companion_device_setup"
public static final String (https://developer.android.com/reference/java/lang/String) FEATURE_C
public static final String (https://developer.android.com/reference/java/lang/String) FEATURE_C


Added in API level 21 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Deprecated in API level 33
(https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
or
Added in API level 19 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
FEATURE_CONNECTION_SERVICE
This constant was deprecated in API level 33.
use FEATURE_TELECOM
(https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_TELECOM)
instead.
Feature for getSystemAvailableFeatures()
(https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatu
res())
and hasSystemFeature(String)
(https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.l
ang.String))
: The Connection Service API is enabled on the device.
Constant Value: "android.software.connectionservice"
FEATURE_CONSUMER_IR
Feature for getSystemAvailableFeatures()
(https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatu
res())
and hasSystemFeature(String)
public static final String (https://developer.android.com/reference/java/lang/String) FEATURE_C
public static final String (https://developer.android.com/reference/java/lang/String) FEATURE_C


Added in API level 30 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Added in API level 34 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
(https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.l
ang.String))
: The device is capable of communicating with consumer IR devices.
Constant Value: "android.hardware.consumerir"
FEATURE_CONTROLS
Feature for getSystemAvailableFeatures()
(https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatu
res())
and hasSystemFeature(String)
(https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.l
ang.String))
: The device supports a system interface for the user to select and bind device control services
provided by applications.
See also:
ControlsProviderService
(https://developer.android.com/reference/android/service/controls/ControlsProviderService)
Constant Value: "android.software.controls"
FEATURE_CREDENTIALS
public static final String (https://developer.android.com/reference/java/lang/String) FEATURE_C
public static final String (https://developer.android.com/reference/java/lang/String) FEATURE_C


Added in API level 19 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Added in API level 37 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Feature for getSystemAvailableFeatures()
(https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatu
res())
and hasSystemFeature(String)
(https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.l
ang.String))
: The device supports retrieval of user credentials, via integration with credential providers.
Constant Value: "android.software.credentials"
FEATURE_DEVICE_ADMIN
Feature for getSystemAvailableFeatures()
(https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatu
res())
and hasSystemFeature(String)
(https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.l
ang.String))
: The device supports device policy enforcement via device admins.
Constant Value: "android.software.device_admin"
FEATURE_DEVICE_ID_ATTESTATION
Feature for getSystemAvailableFeatures()
(https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatu
res())
public static final String (https://developer.android.com/reference/java/lang/String) FEATURE_D
public static final String (https://developer.android.com/reference/java/lang/String) FEATURE_D


Added in API level 34 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Added in API level 26 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
and hasSystemFeature(String)
(https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.l
ang.String))
: The device has a KeyMint (or Keymaster) implementation that supports device ID attestation.
See the public documentation
(https://source.android.com/docs/security/features/keystore/attestation#id-attestation) for more
information about device ID attestation.
See also:
DevicePolicyManager.isDeviceIdAttestationSupported
(https://developer.android.com/reference/android/app/admin/DevicePolicyManager#isDeviceIdAttestation
Supported())
Constant Value: "android.software.device_id_attestation"
FEATURE_DEVICE_LOCK
Feature for getSystemAvailableFeatures()
(https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatu
res())
and hasSystemFeature(String)
(https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.l
ang.String))
: The device supports locking (for example, by a financing provider in case of a missed
payment).
Constant Value: "android.software.device_lock"
FEATURE_EMBEDDED
public static final String (https://developer.android.com/reference/java/lang/String) FEATURE_D


Added in API level 24 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Added in API level 33 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Feature for getSystemAvailableFeatures()
(https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatu
res())
and hasSystemFeature(String)
(https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.l
ang.String))
: This is a device for IoT and may not have an UI. An embedded device is defined as a full stack
Android device with or without a display and no user-installable apps.
Constant Value: "android.hardware.type.embedded"
FEATURE_ETHERNET
Feature for getSystemAvailableFeatures()
(https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatu
res())
and hasSystemFeature(String)
(https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.l
ang.String))
: This device supports ethernet.
Constant Value: "android.hardware.ethernet"
FEATURE_EXPANDED_PICTURE_IN_PICTURE
public static final String (https://developer.android.com/reference/java/lang/String) FEATURE_E
public static final String (https://developer.android.com/reference/java/lang/String) FEATURE_E


Added in API level 29 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Feature for getSystemAvailableFeatures()
(https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatu
res())
and hasSystemFeature(String)
(https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.l
ang.String))
: The device supports expanded picture-in-picture multi-window mode.
See also:
PictureInPictureParams.Builder.setExpandedAspectRatio(Rational)
(https://developer.android.com/reference/android/app/PictureInPictureParams.Builder#setExpandedAspec
tRatio(android.util.Rational))
Constant Value: "android.software.expanded_picture_in_picture"
FEATURE_FACE
Feature for getSystemAvailableFeatures()
(https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatu
res())
and hasSystemFeature(String)
(https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.l
ang.String))
: The device has biometric hardware to perform face authentication.
Constant Value: "android.hardware.biometrics.face"
public static final String (https://developer.android.com/reference/java/lang/String) FEATURE_E
public static final String (https://developer.android.com/reference/java/lang/String) FEATURE_F


Added in API level 11 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Added in API level 13 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
FEATURE_FAKETOUCH
Feature for getSystemAvailableFeatures()
(https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatu
res())
and hasSystemFeature(String)
(https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.l
ang.String))
: The device does not have a touch screen, but does support touch emulation for basic events.
For instance, the device might use a mouse or remote control to drive a cursor, and emulate
basic touch pointer events like down, up, drag, etc. All devices that support
android.hardware.touchscreen or a sub-feature are presumed to also support faketouch.
Constant Value: "android.hardware.faketouch"
FEATURE_FAKETOUCH_MULTITOUCH_DISTINCT
Feature for getSystemAvailableFeatures()
(https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatu
res())
and hasSystemFeature(String)
(https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.l
ang.String))
: The device does not have a touch screen, but does support touch emulation for basic events
that supports distinct tracking of two or more fingers. This is an extension of
FEATURE_FAKETOUCH
(https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_FAKETOUCH)
public static final String (https://developer.android.com/reference/java/lang/String) FEATURE_F
public static final String (https://developer.android.com/reference/java/lang/String) FEATURE_F


Added in API level 13 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
for input devices with this capability. Note that unlike a distinct multitouch screen as defined by
FEATURE_TOUCHSCREEN_MULTITOUCH_DISTINCT
(https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_TOUCHSCREE
N_MULTITOUCH_DISTINCT)
, these kinds of input devices will not actually provide full two-finger gestures since the input is
being transformed to cursor movement on the screen. That is, single finger gestures will move
a cursor; two-finger swipes will result in single-finger touch events; other two-finger gestures
will result in the corresponding two-finger touch event.
Constant Value: "android.hardware.faketouch.multitouch.distinct"
FEATURE_FAKETOUCH_MULTITOUCH_JAZZHAND
Feature for getSystemAvailableFeatures()
(https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatu
res())
and hasSystemFeature(String)
(https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.l
ang.String))
: The device does not have a touch screen, but does support touch emulation for basic events
that supports tracking a hand of fingers (5 or more fingers) fully independently. This is an
extension of FEATURE_FAKETOUCH
(https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_FAKETOUCH)
for input devices with this capability. Note that unlike a multitouch screen as defined by
FEATURE_TOUCHSCREEN_MULTITOUCH_JAZZHAND
(https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_TOUCHSCREE
N_MULTITOUCH_JAZZHAND)
, not all two finger gestures can be detected due to the limitations described for
FEATURE_FAKETOUCH_MULTITOUCH_DISTINCT
(https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_FAKETOUCH_
MULTITOUCH_DISTINCT)
.
public static final String (https://developer.android.com/reference/java/lang/String) FEATURE_F


Added in API level 23 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Added in API level 24 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Constant Value: "android.hardware.faketouch.multitouch.jazzhand"
FEATURE_FINGERPRINT
Feature for getSystemAvailableFeatures()
(https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatu
res())
and hasSystemFeature(String)
(https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.l
ang.String))
: The device has biometric hardware to detect a fingerprint.
Constant Value: "android.hardware.fingerprint"
FEATURE_FREEFORM_WINDOW_MANAGEMENT
Feature for getSystemAvailableFeatures()
(https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatu
res())
and hasSystemFeature(String)
(https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.l
ang.String))
: The device supports freeform window management. Windows have title bars and can be
moved and resized.
Constant Value: "android.software.freeform_window_management"
public static final String (https://developer.android.com/reference/java/lang/String) FEATURE_F
public static final String (https://developer.android.com/reference/java/lang/String) FEATURE_F


Added in API level 21 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Added in API level 31 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
FEATURE_GAMEPAD
Feature for getSystemAvailableFeatures()
(https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatu
res())
and hasSystemFeature(String)
(https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.l
ang.String))
: The device has all of the inputs necessary to be considered a compatible game controller, or
includes a compatible game controller in the box.
Constant Value: "android.hardware.gamepad"
FEATURE_HARDWARE_KEYSTORE
Feature for getSystemAvailableFeatures()
(https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatu
res())
and hasSystemFeature(String,int)
(https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.l
ang.String,%20int))
: If this feature is supported, the device implements the Android Keystore backed by an isolated
execution environment. The version indicates which features are implemented in the isolated
execution environment:
500: Hardware support for ML-DSA signature generation.
400: Inclusion of module information (via tag MODULE_HASH) in the attestation record.
public static final String (https://developer.android.com/reference/java/lang/String) FEATURE_G
public static final String (https://developer.android.com/reference/java/lang/String) FEATURE_H


300: Ability to include a second IMEI in the ID attestation record, see
DevicePolicyManager.ID_TYPE_IMEI
 (https://developer.android.com/reference/android/app/admin/DevicePolicyManager#ID_TYPE_IMEI).
200: Hardware support for Curve 25519 (including both Ed25519 signature generation
and X25519 key agreement).
100: Hardware support for ECDH (see KeyAgreement
 (https://developer.android.com/reference/javax/crypto/KeyAgreement)) and support for app-
generated attestation keys (see
android.security.keystore.KeyGenParameterSpec.Builder.setAttestKeyAlias(S
tring)
 (https://developer.android.com/reference/android/security/keystore/KeyGenParameterSpec.Builder#
setAttestKeyAlias(java.lang.String))
).
41: Hardware enforcement of device-unlocked keys (see
KeyGenParameterSpec.Builder.setUnlockedDeviceRequired(boolean)
 (https://developer.android.com/reference/android/security/keystore/KeyGenParameterSpec.Builder#
setUnlockedDeviceRequired(boolean))
).
40: Support for wrapped key import (see WrappedKeyEntry
 (https://developer.android.com/reference/android/security/keystore/WrappedKeyEntry)), optional
support for ID attestation (see
KeyGenParameterSpec.Builder.setDevicePropertiesAttestationIncluded(boolea
n)
 (https://developer.android.com/reference/android/security/keystore/KeyGenParameterSpec.Builder#
setDevicePropertiesAttestationIncluded(boolean))
), attestation (see
KeyGenParameterSpec.Builder.setAttestationChallenge(byte[])
 (https://developer.android.com/reference/android/security/keystore/KeyGenParameterSpec.Builder#
setAttestationChallenge(byte[]))
), AES, HMAC, ECDSA and RSA support where the secret or private key never leaves
secure hardware, and support for requiring user authentication before a key can be used.
This feature version is guaranteed to be set for all devices launching with Android 12 and may
be set on devices launching with an earlier version. If the feature version is set, it will at least
have the value 40. If it's not set the device may have a version of hardware-backed keystore but
it may not support all features listed above.
Constant Value: "android.hardware.hardware_keystore"


Added in API level 23 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Added in API level 18 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Added in API level 31 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
FEATURE_HIFI_SENSORS
Feature for getSystemAvailableFeatures()
(https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatu
res())
and hasSystemFeature(String)
(https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.l
ang.String))
: The device supports high fidelity sensor processing capabilities.
Constant Value: "android.hardware.sensor.hifi_sensors"
FEATURE_HOME_SCREEN
Feature for getSystemAvailableFeatures()
(https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatu
res())
and hasSystemFeature(String)
(https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.l
ang.String))
: The device supports a home screen that is replaceable by third party applications.
Constant Value: "android.software.home_screen"
FEATURE_IDENTITY_CREDENTIAL_HARDWARE
public static final String (https://developer.android.com/reference/java/lang/String) FEATURE_H
public static final String (https://developer.android.com/reference/java/lang/String) FEATURE_H


Added in API level 31 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Feature for getSystemAvailableFeatures()
(https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatu
res())
and hasSystemFeature(String,int)
(https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.l
ang.String,%20int))
: If this feature is supported, the device supports IdentityCredentialStore
(https://developer.android.com/reference/android/security/identity/IdentityCredentialStore) implemented
in secure hardware at the given feature version.
Known feature versions include:
202009: corresponds to the features included in the Identity Credential API shipped in
Android 11.
202101: corresponds to the features included in the Identity Credential API shipped in
Android 12.
202201: corresponds to the features included in the Identity Credential API shipped in
Android 13.
Constant Value: "android.hardware.identity_credential"
FEATURE_IDENTITY_CREDENTIAL_HARDWARE_DIRECT_ACCESS
Feature for getSystemAvailableFeatures()
(https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatu
res())
and hasSystemFeature(String,int)
public static final String (https://developer.android.com/reference/java/lang/String) FEATURE_I
public static final String (https://developer.android.com/reference/java/lang/String) FEATURE_I


Added in API level 18 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Added in API level 29 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
(https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.l
ang.String,%20int))
: If this feature is supported, the device supports IdentityCredentialStore
(https://developer.android.com/reference/android/security/identity/IdentityCredentialStore) implemented
in secure hardware with direct access at the given feature version. See
FEATURE_IDENTITY_CREDENTIAL_HARDWARE
(https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_IDENTITY_CRE
DENTIAL_HARDWARE)
for known feature versions.
Constant Value: "android.hardware.identity_credential_direct_access"
FEATURE_INPUT_METHODS
Feature for getSystemAvailableFeatures()
(https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatu
res())
and hasSystemFeature(String)
(https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.l
ang.String))
: The device supports adding new input methods implemented with the InputMethodService
(https://developer.android.com/reference/android/inputmethodservice/InputMethodService) API.
Constant Value: "android.software.input_methods"
FEATURE_IPSEC_TUNNELS
public static final String (https://developer.android.com/reference/java/lang/String) FEATURE_I
public static final String (https://developer.android.com/reference/java/lang/String) FEATURE_I


Added in API level 34 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Added in API level 29 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Feature for getSystemAvailableFeatures()
(https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatu
res())
and hasSystemFeature(String)
(https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.l
ang.String))
: The device has the requisite kernel support for multinetworking-capable IPsec tunnels.
This feature implies that the device supports XFRM Interfaces (CONFIG_XFRM_INTERFACE), or
VTIs with kernel patches allowing updates of output/set mark via UPDSA.
Constant Value: "android.software.ipsec_tunnels"
FEATURE_IPSEC_TUNNEL_MIGRATION
Feature for getSystemAvailableFeatures()
(https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatu
res())
and hasSystemFeature(String)
(https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.l
ang.String))
: The device has the requisite kernel support for migrating IPsec tunnels to new
source/destination addresses.
This feature implies that the device supports XFRM Migration (CONFIG_XFRM_MIGRATE) and
has the kernel fixes to support cross-address-family IPsec tunnel migration
Constant Value: "android.software.ipsec_tunnel_migration"
FEATURE_IRIS
public static final String (https://developer.android.com/reference/java/lang/String) FEATURE_I


Added in API level 31 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Added in API level 31 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Feature for getSystemAvailableFeatures()
(https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatu
res())
and hasSystemFeature(String)
(https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.l
ang.String))
: The device has biometric hardware to perform iris authentication.
Constant Value: "android.hardware.biometrics.iris"
FEATURE_KEYSTORE_APP_ATTEST_KEY
Feature for getSystemAvailableFeatures()
(https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatu
res())
and hasSystemFeature(String)
(https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.l
ang.String))
: The device has a Keystore implementation that can create application-specific attestation
keys. See KeyGenParameterSpec.Builder.setAttestKeyAlias(String)
(https://developer.android.com/reference/android/security/keystore/KeyGenParameterSpec.Builder#setAtt
estKeyAlias(java.lang.String))
.
Constant Value: "android.hardware.keystore.app_attest_key"
FEATURE_KEYSTORE_LIMITED_USE_KEY
public static final String (https://developer.android.com/reference/java/lang/String) FEATURE_I
public static final String (https://developer.android.com/reference/java/lang/String) FEATURE_K


Added in API level 31 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Added in API level 21 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Feature for getSystemAvailableFeatures()
(https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatu
res())
and hasSystemFeature(String)
(https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.l
ang.String))
: The device has a Keystore implementation that can enforce limited use key in hardware with
any max usage count (including count equals to 1).
Constant Value: "android.hardware.keystore.limited_use_key"
FEATURE_KEYSTORE_SINGLE_USE_KEY
Feature for getSystemAvailableFeatures()
(https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatu
res())
and hasSystemFeature(String)
(https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.l
ang.String))
: The device has a Keystore implementation that can only enforce limited use key in hardware
with max usage count equals to 1.
Constant Value: "android.hardware.keystore.single_use_key"
FEATURE_LEANBACK
public static final String (https://developer.android.com/reference/java/lang/String) FEATURE_K
public static final String (https://developer.android.com/reference/java/lang/String) FEATURE_K


Added in API level 26 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Added in API level 21 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Feature for getSystemAvailableFeatures()
(https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatu
res())
and hasSystemFeature(String)
(https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.l
ang.String))
: The device supports leanback UI. This is typically used in a living room television experience,
but is a software feature unlike FEATURE_TELEVISION
(https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_TELEVISION).
Devices running with this feature will use resources associated with the "television" UI mode.
Constant Value: "android.software.leanback"
FEATURE_LEANBACK_ONLY
Feature for getSystemAvailableFeatures()
(https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatu
res())
and hasSystemFeature(String)
(https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.l
ang.String))
: The device supports only leanback UI. Only applications designed for this experience should
be run, though this is not enforced by the system.
Constant Value: "android.software.leanback_only"
FEATURE_LIVE_TV
public static final String (https://developer.android.com/reference/java/lang/String) FEATURE_L
public static final String (https://developer.android.com/reference/java/lang/String) FEATURE_L


Added in API level 7 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Added in API level 8 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Feature for getSystemAvailableFeatures()
(https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatu
res())
and hasSystemFeature(String)
(https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.l
ang.String))
: The device supports live TV and can display contents from TV inputs implemented with the
TvInputService (https://developer.android.com/reference/android/media/tv/TvInputService) API.
Constant Value: "android.software.live_tv"
FEATURE_LIVE_WALLPAPER
Feature for getSystemAvailableFeatures()
(https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatu
res())
and hasSystemFeature(String)
(https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.l
ang.String))
: The device supports live wallpapers.
Constant Value: "android.software.live_wallpaper"
FEATURE_LOCATION
public static final String (https://developer.android.com/reference/java/lang/String) FEATURE_L
public static final String (https://developer.android.com/reference/java/lang/String) FEATURE_L


Added in API level 8 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Added in API level 8 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Feature for getSystemAvailableFeatures()
(https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatu
res())
and hasSystemFeature(String)
(https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.l
ang.String))
: The device supports one or more methods of reporting current location.
Constant Value: "android.hardware.location"
FEATURE_LOCATION_GPS
Feature for getSystemAvailableFeatures()
(https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatu
res())
and hasSystemFeature(String)
(https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.l
ang.String))
: The device has a Global Positioning System receiver and can report precise location.
Constant Value: "android.hardware.location.gps"
FEATURE_LOCATION_NETWORK
public static final String (https://developer.android.com/reference/java/lang/String) FEATURE_L
public static final String (https://developer.android.com/reference/java/lang/String) FEATURE_L


Added in API level 21 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Added in API level 8 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Feature for getSystemAvailableFeatures()
(https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatu
res())
and hasSystemFeature(String)
(https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.l
ang.String))
: The device can report location with coarse accuracy using a network-based geolocation
system.
Constant Value: "android.hardware.location.network"
FEATURE_MANAGED_USERS
Feature for getSystemAvailableFeatures()
(https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatu
res())
and hasSystemFeature(String)
(https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.l
ang.String))
: The device supports creating secondary users and managed profiles via
DevicePolicyManager
(https://developer.android.com/reference/android/app/admin/DevicePolicyManager).
Constant Value: "android.software.managed_users"
FEATURE_MICROPHONE
public static final String (https://developer.android.com/reference/java/lang/String) FEATURE_L
public static final String (https://developer.android.com/reference/java/lang/String) FEATURE_M


Added in API level 23 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Added in API level 37 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Feature for getSystemAvailableFeatures()
(https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatu
res())
and hasSystemFeature(String)
(https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.l
ang.String))
: The device can record audio via a microphone.
Constant Value: "android.hardware.microphone"
FEATURE_MIDI
Feature for getSystemAvailableFeatures()
(https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatu
res())
and hasSystemFeature(String)
(https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.l
ang.String))
: The device has a full implementation of the android.media.midi.* APIs.
Constant Value: "android.software.midi"
FEATURE_NEURAL_PROCESSING_UNIT
public static final String (https://developer.android.com/reference/java/lang/String) FEATURE_M
public static final String (https://developer.android.com/reference/java/lang/String) FEATURE_M


Added in API level 9 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Added in API level 29 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Feature for getSystemAvailableFeatures()
(https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatu
res())
and hasSystemFeature(String)
(https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.l
ang.String))
: This device has a NPU (Neural Processing Unit) or similar hardware for accelerating AI
workloads.
Constant Value: "android.hardware.npu"
FEATURE_NFC
Feature for getSystemAvailableFeatures()
(https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatu
res())
and hasSystemFeature(String)
(https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.l
ang.String))
: The device can communicate using Near-Field Communications (NFC), acting as a reader.
Constant Value: "android.hardware.nfc"
FEATURE_NFC_BEAM
public static final String (https://developer.android.com/reference/java/lang/String) FEATURE_N
public static final String (https://developer.android.com/reference/java/lang/String) FEATURE_N


Added in API level 19 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Added in API level 24 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Feature for getSystemAvailableFeatures()
(https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatu
res())
and hasSystemFeature(String)
(https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.l
ang.String))
: The Beam API is enabled on the device.
Constant Value: "android.sofware.nfc.beam"
FEATURE_NFC_HOST_CARD_EMULATION
Feature for getSystemAvailableFeatures()
(https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatu
res())
and hasSystemFeature(String)
(https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.l
ang.String))
: The device supports host- based NFC card emulation.
Constant Value: "android.hardware.nfc.hce"
FEATURE_NFC_HOST_CARD_EMULATION_NFCF
public static final String (https://developer.android.com/reference/java/lang/String) FEATURE_N
public static final String (https://developer.android.com/reference/java/lang/String) FEATURE_N


Added in API level 29 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Added in API level 29 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Feature for getSystemAvailableFeatures()
(https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatu
res())
and hasSystemFeature(String)
(https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.l
ang.String))
: The device supports host- based NFC-F card emulation.
Constant Value: "android.hardware.nfc.hcef"
FEATURE_NFC_OFF_HOST_CARD_EMULATION_ESE
Feature for getSystemAvailableFeatures()
(https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatu
res())
and hasSystemFeature(String)
(https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.l
ang.String))
: The device supports eSE- based NFC card emulation.
Constant Value: "android.hardware.nfc.ese"
FEATURE_NFC_OFF_HOST_CARD_EMULATION_UICC
public static final String (https://developer.android.com/reference/java/lang/String) FEATURE_N
public static final String (https://developer.android.com/reference/java/lang/String) FEATURE_N


Added in API level 31 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Feature for getSystemAvailableFeatures()
(https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatu
res())
and hasSystemFeature(String)
(https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.l
ang.String))
: The device supports uicc- based NFC card emulation.
Constant Value: "android.hardware.nfc.uicc"
FEATURE_OPENGLES_DEQP_LEVEL
Feature for getSystemAvailableFeatures()
(https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatu
res())
and hasSystemFeature(String,int)
(https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.l
ang.String,%20int))
: If this feature is supported, the feature version specifies a date such that the device is known
to pass the OpenGLES dEQP test suite associated with that date. The date is encoded as
follows:
Year in bits 31-16
Month in bits 15-8
Day in bits 7-0
Example: 2021-03-01 is encoded as 0x07E50301, and would indicate that the device passes
the OpenGL ES dEQP test suite version that was current on 2021-03-01.
public static final String (https://developer.android.com/reference/java/lang/String) FEATURE_N
public static final String (https://developer.android.com/reference/java/lang/String) FEATURE_O


Added in API level 21 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Added in API level 27 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Constant Value: "android.software.opengles.deqp.level"
FEATURE_OPENGLES_EXTENSION_PACK
Feature for getSystemAvailableFeatures()
(https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatu
res())
and hasSystemFeature(String)
(https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.l
ang.String))
: The device supports the OpenGL ES Android Extension Pack
(http://www.khronos.org/registry/gles/extensions/ANDROID/ANDROID_extension_pack_es31a.txt).
Constant Value: "android.hardware.opengles.aep"
FEATURE_PC
Feature for getSystemAvailableFeatures()
(https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatu
res())
and hasSystemFeature(String)
(https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.l
ang.String))
: This is a device dedicated to be primarily used with keyboard, mouse or touchpad. This
includes traditional desktop computers, laptops and variants such as convertibles or
detachables. Due to the larger screen, the device will most likely use the
public static final String (https://developer.android.com/reference/java/lang/String) FEATURE_O
public static final String (https://developer.android.com/reference/java/lang/String) FEATURE_P


Added in API level 24 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Added in API level 20 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
FEATURE_FREEFORM_WINDOW_MANAGEMENT
(https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_FREEFORM_WI
NDOW_MANAGEMENT)
feature as well.
Constant Value: "android.hardware.type.pc"
FEATURE_PICTURE_IN_PICTURE
Feature for getSystemAvailableFeatures()
(https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatu
res())
and hasSystemFeature(String)
(https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.l
ang.String))
: The device supports picture-in-picture multi-window mode.
Constant Value: "android.software.picture_in_picture"
FEATURE_PRINTING
Feature for getSystemAvailableFeatures()
(https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatu
res())
and hasSystemFeature(String)
public static final String (https://developer.android.com/reference/java/lang/String) FEATURE_P
public static final String (https://developer.android.com/reference/java/lang/String) FEATURE_P


Added in API level 27 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Added in API level 27 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
(https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.l
ang.String))
: The device supports printing.
Constant Value: "android.software.print"
FEATURE_RAM_LOW
Feature for getSystemAvailableFeatures()
(https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatu
res())
and hasSystemFeature(String)
(https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.l
ang.String))
: The device's ActivityManager.isLowRamDevice()
(https://developer.android.com/reference/android/app/ActivityManager#isLowRamDevice()) method
returns true.
Constant Value: "android.hardware.ram.low"
FEATURE_RAM_NORMAL
Feature for getSystemAvailableFeatures()
(https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatu
res())
and hasSystemFeature(String)
public static final String (https://developer.android.com/reference/java/lang/String) FEATURE_R
public static final String (https://developer.android.com/reference/java/lang/String) FEATURE_R


Added in API level 13 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Added in API level 13 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
(https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.l
ang.String))
: The device's ActivityManager.isLowRamDevice()
(https://developer.android.com/reference/android/app/ActivityManager#isLowRamDevice()) method
returns false.
Constant Value: "android.hardware.ram.normal"
FEATURE_SCREEN_LANDSCAPE
Feature for getSystemAvailableFeatures()
(https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatu
res())
and hasSystemFeature(String)
(https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.l
ang.String))
: The device supports landscape orientation screens. For backwards compatibility, you can
assume that if neither this nor FEATURE_SCREEN_PORTRAIT
(https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_SCREEN_PORT
RAIT)
is set then the device supports both portrait and landscape.
Constant Value: "android.hardware.screen.landscape"
FEATURE_SCREEN_PORTRAIT
public static final String (https://developer.android.com/reference/java/lang/String) FEATURE_S
public static final String (https://developer.android.com/reference/java/lang/String) FEATURE_S


Added in API level 21 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Added in API level 29 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Feature for getSystemAvailableFeatures()
(https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatu
res())
and hasSystemFeature(String)
(https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.l
ang.String))
: The device supports portrait orientation screens. For backwards compatibility, you can
assume that if neither this nor FEATURE_SCREEN_LANDSCAPE
(https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_SCREEN_LAND
SCAPE)
is set then the device supports both portrait and landscape.
Constant Value: "android.hardware.screen.portrait"
FEATURE_SECURELY_REMOVES_USERS
Feature for getSystemAvailableFeatures()
(https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatu
res())
and hasSystemFeature(String)
(https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.l
ang.String))
: The device supports secure removal of users. When a user is deleted the data associated with
that user is securely deleted and no longer available.
Constant Value: "android.software.securely_removes_users"
FEATURE_SECURE_LOCK_SCREEN
public static final String (https://developer.android.com/reference/java/lang/String) FEATURE_S


Added in API level 31 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Added in API level 8 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Feature for getSystemAvailableFeatures()
(https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatu
res())
and hasSystemFeature(String)
(https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.l
ang.String))
: The device has a secure implementation of keyguard, meaning the device supports PIN,
pattern and password as defined in Android CDD
Constant Value: "android.software.secure_lock_screen"
FEATURE_SECURITY_MODEL_COMPATIBLE
Feature for getSystemAvailableFeatures()
(https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatu
res())
and hasSystemFeature(String)
(https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.l
ang.String))
: The device is compatible with Android's security model.
See sections 2 and 9 in the Android CDD (https://source.android.com/compatibility/android-cdd) for
more details.
Constant Value: "android.hardware.security.model.compatible"
FEATURE_SENSOR_ACCELEROMETER
public static final String (https://developer.android.com/reference/java/lang/String) FEATURE_S
public static final String (https://developer.android.com/reference/java/lang/String) FEATURE_S


Added in API level 33 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Added in API level 33 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Feature for getSystemAvailableFeatures()
(https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatu
res())
and hasSystemFeature(String)
(https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.l
ang.String))
: The device includes an accelerometer.
Constant Value: "android.hardware.sensor.accelerometer"
FEATURE_SENSOR_ACCELEROMETER_LIMITED_AXES
Feature for getSystemAvailableFeatures()
(https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatu
res())
and hasSystemFeature(String)
(https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.l
ang.String))
: The device includes a limited axes accelerometer.
Constant Value: "android.hardware.sensor.accelerometer_limited_axes"
FEATURE_SENSOR_ACCELEROMETER_LIMITED_AXES_UNCALIBRATED
public static final String (https://developer.android.com/reference/java/lang/String) FEATURE_S
public static final String (https://developer.android.com/reference/java/lang/String) FEATURE_S


Added in API level 21 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Added in API level 9 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Feature for getSystemAvailableFeatures()
(https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatu
res())
and hasSystemFeature(String)
(https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.l
ang.String))
: The device includes an uncalibrated limited axes accelerometer.
Constant Value: "android.hardware.sensor.accelerometer_limited_axes_uncalibrated"
FEATURE_SENSOR_AMBIENT_TEMPERATURE
Feature for getSystemAvailableFeatures()
(https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatu
res())
and hasSystemFeature(String)
(https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.l
ang.String))
: The device includes an ambient temperature sensor.
Constant Value: "android.hardware.sensor.ambient_temperature"
FEATURE_SENSOR_BAROMETER
public static final String (https://developer.android.com/reference/java/lang/String) FEATURE_S
public static final String (https://developer.android.com/reference/java/lang/String) FEATURE_S


Added in API level 8 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Added in API level 33 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Feature for getSystemAvailableFeatures()
(https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatu
res())
and hasSystemFeature(String)
(https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.l
ang.String))
: The device includes a barometer (air pressure sensor.)
Constant Value: "android.hardware.sensor.barometer"
FEATURE_SENSOR_COMPASS
Feature for getSystemAvailableFeatures()
(https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatu
res())
and hasSystemFeature(String)
(https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.l
ang.String))
: The device includes a magnetometer (compass).
Constant Value: "android.hardware.sensor.compass"
FEATURE_SENSOR_DYNAMIC_HEAD_TRACKER
public static final String (https://developer.android.com/reference/java/lang/String) FEATURE_S
public static final String (https://developer.android.com/reference/java/lang/String) FEATURE_S


Added in API level 9 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Added in API level 33 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Feature for getSystemAvailableFeatures()
(https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatu
res())
and hasSystemFeature(String)
(https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.l
ang.String))
: The device supports exposing head tracker sensors from peripheral devices via the dynamic
sensors API.
Constant Value: "android.hardware.sensor.dynamic.head_tracker"
FEATURE_SENSOR_GYROSCOPE
Feature for getSystemAvailableFeatures()
(https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatu
res())
and hasSystemFeature(String)
(https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.l
ang.String))
: The device includes a gyroscope.
Constant Value: "android.hardware.sensor.gyroscope"
FEATURE_SENSOR_GYROSCOPE_LIMITED_AXES
public static final String (https://developer.android.com/reference/java/lang/String) FEATURE_S
public static final String (https://developer.android.com/reference/java/lang/String) FEATURE_S


Added in API level 33 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Added in API level 33 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Feature for getSystemAvailableFeatures()
(https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatu
res())
and hasSystemFeature(String)
(https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.l
ang.String))
: The device includes a limited axes gyroscope.
Constant Value: "android.hardware.sensor.gyroscope_limited_axes"
FEATURE_SENSOR_GYROSCOPE_LIMITED_AXES_UNCALIBRATED
Feature for getSystemAvailableFeatures()
(https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatu
res())
and hasSystemFeature(String)
(https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.l
ang.String))
: The device includes an uncalibrated limited axes gyroscope.
Constant Value: "android.hardware.sensor.gyroscope_limited_axes_uncalibrated"
FEATURE_SENSOR_HEADING
public static final String (https://developer.android.com/reference/java/lang/String) FEATURE_S
public static final String (https://developer.android.com/reference/java/lang/String) FEATURE_S


Added in API level 20 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Added in API level 21 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Feature for getSystemAvailableFeatures()
(https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatu
res())
and hasSystemFeature(String)
(https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.l
ang.String))
: The device includes a heading sensor.
Constant Value: "android.hardware.sensor.heading"
FEATURE_SENSOR_HEART_RATE
Feature for getSystemAvailableFeatures()
(https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatu
res())
and hasSystemFeature(String)
(https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.l
ang.String))
: The device includes a heart rate monitor.
Constant Value: "android.hardware.sensor.heartrate"
FEATURE_SENSOR_HEART_RATE_ECG
public static final String (https://developer.android.com/reference/java/lang/String) FEATURE_S
public static final String (https://developer.android.com/reference/java/lang/String) FEATURE_S


Added in API level 30 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Added in API level 7 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Feature for getSystemAvailableFeatures()
(https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatu
res())
and hasSystemFeature(String)
(https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.l
ang.String))
: The heart rate sensor on this device is an Electrocardiogram.
Constant Value: "android.hardware.sensor.heartrate.ecg"
FEATURE_SENSOR_HINGE_ANGLE
Feature for getSystemAvailableFeatures()
(https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatu
res())
and hasSystemFeature(String)
(https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.l
ang.String))
: The device includes a hinge angle sensor.
Constant Value: "android.hardware.sensor.hinge_angle"
FEATURE_SENSOR_LIGHT
public static final String (https://developer.android.com/reference/java/lang/String) FEATURE_S
public static final String (https://developer.android.com/reference/java/lang/String) FEATURE_S


Added in API level 7 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Added in API level 21 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Feature for getSystemAvailableFeatures()
(https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatu
res())
and hasSystemFeature(String)
(https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.l
ang.String))
: The device includes a light sensor.
Constant Value: "android.hardware.sensor.light"
FEATURE_SENSOR_PROXIMITY
Feature for getSystemAvailableFeatures()
(https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatu
res())
and hasSystemFeature(String)
(https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.l
ang.String))
: The device includes a proximity sensor.
Constant Value: "android.hardware.sensor.proximity"
FEATURE_SENSOR_RELATIVE_HUMIDITY
public static final String (https://developer.android.com/reference/java/lang/String) FEATURE_S
public static final String (https://developer.android.com/reference/java/lang/String) FEATURE_S


Added in API level 19 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Added in API level 19 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Feature for getSystemAvailableFeatures()
(https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatu
res())
and hasSystemFeature(String)
(https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.l
ang.String))
: The device includes a relative humidity sensor.
Constant Value: "android.hardware.sensor.relative_humidity"
FEATURE_SENSOR_STEP_COUNTER
Feature for getSystemAvailableFeatures()
(https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatu
res())
and hasSystemFeature(String)
(https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.l
ang.String))
: The device includes a hardware step counter.
Constant Value: "android.hardware.sensor.stepcounter"
FEATURE_SENSOR_STEP_DETECTOR
public static final String (https://developer.android.com/reference/java/lang/String) FEATURE_S
public static final String (https://developer.android.com/reference/java/lang/String) FEATURE_S


Added in API level 30 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Added in API level 30 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Feature for getSystemAvailableFeatures()
(https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatu
res())
and hasSystemFeature(String)
(https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.l
ang.String))
: The device includes a hardware step detector.
Constant Value: "android.hardware.sensor.stepdetector"
FEATURE_SE_OMAPI_ESE
Feature for getSystemAvailableFeatures()
(https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatu
res())
and hasSystemFeature(String)
(https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.l
ang.String))
: The device supports Open Mobile API capable eSE-based secure elements.
Constant Value: "android.hardware.se.omapi.ese"
FEATURE_SE_OMAPI_SD
public static final String (https://developer.android.com/reference/java/lang/String) FEATURE_S
public static final String (https://developer.android.com/reference/java/lang/String) FEATURE_S


Added in API level 30 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Added in API level 9 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Feature for getSystemAvailableFeatures()
(https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatu
res())
and hasSystemFeature(String)
(https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.l
ang.String))
: The device supports Open Mobile API capable SD-based secure elements.
Constant Value: "android.hardware.se.omapi.sd"
FEATURE_SE_OMAPI_UICC
Feature for getSystemAvailableFeatures()
(https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatu
res())
and hasSystemFeature(String)
(https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.l
ang.String))
: The device supports Open Mobile API capable UICC-based secure elements.
Constant Value: "android.hardware.se.omapi.uicc"
FEATURE_SIP
public static final String (https://developer.android.com/reference/java/lang/String) FEATURE_S
public static final String (https://developer.android.com/reference/java/lang/String) FEATURE_S


Added in API level 9 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Added in API level 28 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Feature for getSystemAvailableFeatures()
(https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatu
res())
and hasSystemFeature(String)
(https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.l
ang.String))
: The SIP API is enabled on the device.
Constant Value: "android.software.sip"
FEATURE_SIP_VOIP
Feature for getSystemAvailableFeatures()
(https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatu
res())
and hasSystemFeature(String)
(https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.l
ang.String))
: The device supports SIP-based VOIP.
Constant Value: "android.software.sip.voip"
FEATURE_STRONGBOX_KEYSTORE
public static final String (https://developer.android.com/reference/java/lang/String) FEATURE_S
public static final String (https://developer.android.com/reference/java/lang/String) FEATURE_S


Feature for getSystemAvailableFeatures()
(https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatu
res())
, hasSystemFeature(String)
(https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.l
ang.String))
, and hasSystemFeature(String,int)
(https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.l
ang.String,%20int))
: If this feature is supported, the device implements the Android Keystore backed by a
dedicated secure processor referred to as StrongBox
(https://source.android.com/security/best-practices/hardware#strongbox-keymaster). If this feature has
a version, the version number indicates which features are implemented in StrongBox:
400: Inclusion of module information (via tag MODULE_HASH) in the attestation record.
300: Ability to include a second IMEI in the ID attestation record, see
DevicePolicyManager.ID_TYPE_IMEI
 (https://developer.android.com/reference/android/app/admin/DevicePolicyManager#ID_TYPE_IMEI).
200: No new features for StrongBox (the Android Keystore environment backed by an
isolated execution environment has gained support for Curve 25519 in this version, but
the implementation backed by a dedicated secure processor is not expected to
implement it).
100: Hardware support for ECDH (see KeyAgreement
 (https://developer.android.com/reference/javax/crypto/KeyAgreement)) and support for app-
generated attestation keys (see
android.security.keystore.KeyGenParameterSpec.Builder.setAttestKeyAlias(S
tring)
 (https://developer.android.com/reference/android/security/keystore/KeyGenParameterSpec.Builder#
setAttestKeyAlias(java.lang.String))
).
41: Hardware enforcement of device-unlocked keys (see
KeyGenParameterSpec.Builder.setUnlockedDeviceRequired(boolean)
public static final String (https://developer.android.com/reference/java/lang/String) FEATURE_S


Added in API level 33 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
 (https://developer.android.com/reference/android/security/keystore/KeyGenParameterSpec.Builder#
setUnlockedDeviceRequired(boolean))
).
40: Support for wrapped key import (see WrappedKeyEntry
 (https://developer.android.com/reference/android/security/keystore/WrappedKeyEntry)), optional
support for ID attestation (see
KeyGenParameterSpec.Builder.setDevicePropertiesAttestationIncluded(boolea
n)
 (https://developer.android.com/reference/android/security/keystore/KeyGenParameterSpec.Builder#
setDevicePropertiesAttestationIncluded(boolean))
), attestation (see
KeyGenParameterSpec.Builder.setAttestationChallenge(byte[])
 (https://developer.android.com/reference/android/security/keystore/KeyGenParameterSpec.Builder#
setAttestationChallenge(byte[]))
), AES, HMAC, ECDSA and RSA support where the secret or private key never leaves
secure hardware, and support for requiring user authentication before a key can be used.
If a device has StrongBox, this feature version number is guaranteed to be set for all devices
launching with Android 12 and may be set on devices launching with an earlier version. If the
feature version is set, it will at least have the value 40. If it's not set the device may have
StrongBox but it may not support all features listed above.
Constant Value: "android.hardware.strongbox_keystore"
FEATURE_TELECOM
Feature for getSystemAvailableFeatures()
(https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatu
res())
and hasSystemFeature(String)
(https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.l
ang.String))
: The device supports Telecom Service APIs.
public static final String (https://developer.android.com/reference/java/lang/String) FEATURE_T


Added in API level 7 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Added in API level 33 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Constant Value: "android.software.telecom"
FEATURE_TELEPHONY
Feature for getSystemAvailableFeatures()
(https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatu
res())
and hasSystemFeature(String)
(https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.l
ang.String))
: The device has a telephony radio with data communication support.
Constant Value: "android.hardware.telephony"
FEATURE_TELEPHONY_CALLING
Feature for getSystemAvailableFeatures()
(https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatu
res())
and hasSystemFeature(String)
(https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.l
ang.String))
: The device supports Telephony APIs for calling service.
This feature should only be defined if FEATURE_TELEPHONY_RADIO_ACCESS
(https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_TELEPHONY_R
ADIO_ACCESS)
public static final String (https://developer.android.com/reference/java/lang/String) FEATURE_T
public static final String (https://developer.android.com/reference/java/lang/String) FEATURE_T


Added in API level 7 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Added in API level 33 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
, FEATURE_TELEPHONY_SUBSCRIPTION
(https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_TELEPHONY_S
UBSCRIPTION)
, and FEATURE_TELECOM
(https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_TELECOM)
have been defined.
Constant Value: "android.hardware.telephony.calling"
FEATURE_TELEPHONY_CDMA
Feature for getSystemAvailableFeatures()
(https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatu
res())
and hasSystemFeature(String)
(https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.l
ang.String))
: The device has a CDMA telephony stack.
This feature should only be defined if FEATURE_TELEPHONY
(https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_TELEPHONY)
has been defined.
Constant Value: "android.hardware.telephony.cdma"
FEATURE_TELEPHONY_DATA
public static final String (https://developer.android.com/reference/java/lang/String) FEATURE_T
public static final String (https://developer.android.com/reference/java/lang/String) FEATURE_T


Added in API level 28 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Feature for getSystemAvailableFeatures()
(https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatu
res())
and hasSystemFeature(String)
(https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.l
ang.String))
: The device supports Telephony APIs for data service.
This feature should only be defined if both FEATURE_TELEPHONY_SUBSCRIPTION
(https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_TELEPHONY_S
UBSCRIPTION)
and FEATURE_TELEPHONY_RADIO_ACCESS
(https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_TELEPHONY_R
ADIO_ACCESS)
have been defined.
Constant Value: "android.hardware.telephony.data"
FEATURE_TELEPHONY_EUICC
Feature for getSystemAvailableFeatures()
(https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatu
res())
and hasSystemFeature(String)
(https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.l
ang.String))
: The device supports embedded subscriptions on eUICCs. This feature should only be defined
if FEATURE_TELEPHONY_SUBSCRIPTION
(https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_TELEPHONY_S
UBSCRIPTION)
has been defined.
Constant Value: "android.hardware.telephony.euicc"
public static final String (https://developer.android.com/reference/java/lang/String) FEATURE_T


Added in API level 33 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Added in API level 7 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
FEATURE_TELEPHONY_EUICC_MEP
Feature for getSystemAvailableFeatures()
(https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatu
res())
and hasSystemFeature(String)
(https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.l
ang.String))
: The device supports multiple enabled profiles on eUICCs.
Devices declaring this feature must have an implementation of the UiccCardInfo.getPorts
(https://developer.android.com/reference/android/telephony/UiccCardInfo#getPorts()),
UiccCardInfo.isMultipleEnabledProfilesSupported
(https://developer.android.com/reference/android/telephony/UiccCardInfo#isMultipleEnabledProfilesSuppo
rted())
and (with portIndex)
(https://developer.android.com/reference/android/telephony/euicc/EuiccManager#switchToSubscription(in
t,%20android.app.PendingIntent))
. This feature should only be defined if FEATURE_TELEPHONY_EUICC
(https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_TELEPHONY_E
UICC)
have been defined.
Constant Value: "android.hardware.telephony.euicc.mep"
FEATURE_TELEPHONY_GSM
public static final String (https://developer.android.com/reference/java/lang/String) FEATURE_T
public static final String (https://developer.android.com/reference/java/lang/String) FEATURE_T


Added in API level 29 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Added in API level 28 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Feature for getSystemAvailableFeatures()
(https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatu
res())
and hasSystemFeature(String)
(https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.l
ang.String))
: The device has a GSM telephony stack.
This feature should only be defined if FEATURE_TELEPHONY
(https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_TELEPHONY)
has been defined.
Constant Value: "android.hardware.telephony.gsm"
FEATURE_TELEPHONY_IMS
Feature for getSystemAvailableFeatures()
(https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatu
res())
and hasSystemFeature(String)
(https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.l
ang.String))
: The device supports attaching to IMS implementations using the ImsService API in telephony.
This feature should only be defined if FEATURE_TELEPHONY_DATA
(https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_TELEPHONY_D
ATA)
has been defined.
Constant Value: "android.hardware.telephony.ims"
FEATURE_TELEPHONY_MBMS
public static final String (https://developer.android.com/reference/java/lang/String) FEATURE_T


Added in API level 33 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Feature for getSystemAvailableFeatures()
(https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatu
res())
and hasSystemFeature(String)
(https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.l
ang.String))
: The device supports cell-broadcast reception using the MBMS APIs.
This feature should only be defined if both FEATURE_TELEPHONY_SUBSCRIPTION
(https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_TELEPHONY_S
UBSCRIPTION)
and FEATURE_TELEPHONY_RADIO_ACCESS
(https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_TELEPHONY_R
ADIO_ACCESS)
have been defined.
Constant Value: "android.hardware.telephony.mbms"
FEATURE_TELEPHONY_MESSAGING
Feature for getSystemAvailableFeatures()
(https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatu
res())
and hasSystemFeature(String)
(https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.l
ang.String))
: The device supports Telephony APIs for SMS and MMS.
public static final String (https://developer.android.com/reference/java/lang/String) FEATURE_T
public static final String (https://developer.android.com/reference/java/lang/String) FEATURE_T


Added in API level 33 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Added in API level 33 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
This feature should only be defined if both FEATURE_TELEPHONY_SUBSCRIPTION
(https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_TELEPHONY_S
UBSCRIPTION)
and FEATURE_TELEPHONY_RADIO_ACCESS
(https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_TELEPHONY_R
ADIO_ACCESS)
have been defined.
Constant Value: "android.hardware.telephony.messaging"
FEATURE_TELEPHONY_RADIO_ACCESS
Feature for getSystemAvailableFeatures()
(https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatu
res())
and hasSystemFeature(String)
(https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.l
ang.String))
: The device supports Telephony APIs for the radio access.
This feature should only be defined if FEATURE_TELEPHONY
(https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_TELEPHONY)
has been defined.
Constant Value: "android.hardware.telephony.radio.access"
FEATURE_TELEPHONY_SUBSCRIPTION
public static final String (https://developer.android.com/reference/java/lang/String) FEATURE_T
public static final String (https://developer.android.com/reference/java/lang/String) FEATURE_T


Added in API level 16 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Deprecated in API level 21
(https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
or
Feature for getSystemAvailableFeatures()
(https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatu
res())
and hasSystemFeature(String)
(https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.l
ang.String))
: The device supports Telephony APIs for the subscription.
This feature should only be defined if FEATURE_TELEPHONY
(https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_TELEPHONY)
has been defined.
Constant Value: "android.hardware.telephony.subscription"
FEATURE_TELEVISION
This constant was deprecated in API level 21.
use FEATURE_LEANBACK
(https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_LEANBACK)
instead.
Feature for getSystemAvailableFeatures()
(https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatu
res())
and hasSystemFeature(String)
(https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.l
ang.String))
: This is a device dedicated to showing UI on a television. Television here is defined to be a
typical living room television experience: displayed on a big screen, where the user is sitting far
away from it, and the dominant form of input will be something like a DPAD, not through touch
or mouse.
public static final String (https://developer.android.com/reference/java/lang/String) FEATURE_T


Added in API level 36 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Added in API level 8 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Constant Value: "android.hardware.type.television"
FEATURE_THREAD_NETWORK
Feature for getSystemAvailableFeatures()
(https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatu
res())
and hasSystemFeature(String)
(https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.l
ang.String))
: The device is capable of communicating with other devices via Thread
(https://www.threadgroup.org/) networking protocol.
Constant Value: "android.hardware.thread_network"
FEATURE_TOUCHSCREEN
Feature for getSystemAvailableFeatures()
(https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatu
res())
and hasSystemFeature(String)
(https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.l
ang.String))
: The device's display has a touch screen.
Constant Value: "android.hardware.touchscreen"
public static final String (https://developer.android.com/reference/java/lang/String) FEATURE_T
public static final String (https://developer.android.com/reference/java/lang/String) FEATURE_T


Added in API level 7 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Added in API level 8 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Added in API level 9 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
FEATURE_TOUCHSCREEN_MULTITOUCH
Feature for getSystemAvailableFeatures()
(https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatu
res())
and hasSystemFeature(String)
(https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.l
ang.String))
: The device's touch screen supports multitouch sufficient for basic two-finger gesture
detection.
Constant Value: "android.hardware.touchscreen.multitouch"
FEATURE_TOUCHSCREEN_MULTITOUCH_DISTINCT
Feature for getSystemAvailableFeatures()
(https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatu
res())
and hasSystemFeature(String)
(https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.l
ang.String))
: The device's touch screen is capable of tracking two or more fingers fully independently.
Constant Value: "android.hardware.touchscreen.multitouch.distinct"
FEATURE_TOUCHSCREEN_MULTITOUCH_JAZZHAND
public static final String (https://developer.android.com/reference/java/lang/String) FEATURE_T
public static final String (https://developer.android.com/reference/java/lang/String) FEATURE_T


Added in API level 12 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Added in API level 12 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Feature for getSystemAvailableFeatures()
(https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatu
res())
and hasSystemFeature(String)
(https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.l
ang.String))
: The device's touch screen is capable of tracking a full hand of fingers fully independently --
that is, 5 or more simultaneous independent pointers.
Constant Value: "android.hardware.touchscreen.multitouch.jazzhand"
FEATURE_USB_ACCESSORY
Feature for getSystemAvailableFeatures()
(https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatu
res())
and hasSystemFeature(String)
(https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.l
ang.String))
: The device supports connecting to USB accessories.
Constant Value: "android.hardware.usb.accessory"
FEATURE_USB_HOST
public static final String (https://developer.android.com/reference/java/lang/String) FEATURE_T
public static final String (https://developer.android.com/reference/java/lang/String) FEATURE_U


Added in API level 34 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Added in API level 21 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Feature for getSystemAvailableFeatures()
(https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatu
res())
and hasSystemFeature(String)
(https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.l
ang.String))
: The device supports connecting to USB devices as the USB host.
Constant Value: "android.hardware.usb.host"
FEATURE_UWB
Feature for getSystemAvailableFeatures()
(https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatu
res())
and hasSystemFeature(String)
(https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.l
ang.String))
: The device is capable of communicating with other devices via ultra wideband.
Constant Value: "android.hardware.uwb"
FEATURE_VERIFIED_BOOT
public static final String (https://developer.android.com/reference/java/lang/String) FEATURE_U
public static final String (https://developer.android.com/reference/java/lang/String) FEATURE_U


Added in API level 26 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Added in API level 24 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Deprecated in API level 28
(https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Feature for getSystemAvailableFeatures()
(https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatu
res())
and hasSystemFeature(String)
(https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.l
ang.String))
: The device supports verified boot.
Constant Value: "android.software.verified_boot"
FEATURE_VR_HEADTRACKING
Feature for getSystemAvailableFeatures()
(https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatu
res())
and hasSystemFeature(String)
(https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.l
ang.String))
: The device implements headtracking suitable for a VR device.
Constant Value: "android.hardware.vr.headtracking"
FEATURE_VR_MODE
public static final String (https://developer.android.com/reference/java/lang/String) FEATURE_V
public static final String (https://developer.android.com/reference/java/lang/String) FEATURE_V


or
Added in API level 24 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
This constant was deprecated in API level 28.
use FEATURE_VR_MODE_HIGH_PERFORMANCE
(https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_VR_MODE_HIG
H_PERFORMANCE)
instead.
Feature for getSystemAvailableFeatures()
(https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatu
res())
and hasSystemFeature(String)
(https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.l
ang.String))
: The device implements an optimized mode for virtual reality (VR) applications that handles
stereoscopic rendering of notifications, and disables most monocular system UI components
while a VR application has user focus. Devices declaring this feature must include an
application implementing a VrListenerService
(https://developer.android.com/reference/android/service/vr/VrListenerService) that can be targeted by
VR applications via Activity.setVrModeEnabled(boolean, ComponentName)
(https://developer.android.com/reference/android/app/Activity#setVrModeEnabled(boolean,%20android.co
ntent.ComponentName))
.
Constant Value: "android.software.vr.mode"
FEATURE_VR_MODE_HIGH_PERFORMANCE
public static final String (https://developer.android.com/reference/java/lang/String) FEATURE_V
public static final String (https://developer.android.com/reference/java/lang/String) FEATURE_V


Added in API level 30 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Feature for getSystemAvailableFeatures()
(https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatu
res())
and hasSystemFeature(String)
(https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.l
ang.String))
: The device implements an optimized mode for virtual reality (VR) applications that handles
stereoscopic rendering of notifications, disables most monocular system UI components while
a VR application has user focus and meets extra CDD requirements to provide a high-quality VR
experience. Devices declaring this feature must include an application implementing a
VrListenerService (https://developer.android.com/reference/android/service/vr/VrListenerService)
that can be targeted by VR applications via Activity.setVrModeEnabled(boolean,
ComponentName)
(https://developer.android.com/reference/android/app/Activity#setVrModeEnabled(boolean,%20android.co
ntent.ComponentName))
. and must meet CDD requirements to provide a high-quality VR experience.
Constant Value: "android.hardware.vr.high_performance"
FEATURE_VULKAN_DEQP_LEVEL
Feature for getSystemAvailableFeatures()
(https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatu
res())
and hasSystemFeature(String,int)
(https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.l
ang.String,%20int))
: If this feature is supported, the feature version specifies a date such that the device is known
to pass the Vulkan dEQP test suite associated with that date. The date is encoded as follows:
Year in bits 31-16
Month in bits 15-8
public static final String (https://developer.android.com/reference/java/lang/String) FEATURE_V


Added in API level 26 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Added in API level 24 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Day in bits 7-0
Example: 2019-03-01 is encoded as 0x07E30301, and would indicate that the device passes
the Vulkan dEQP test suite version that was current on 2019-03-01.
Constant Value: "android.software.vulkan.deqp.level"
FEATURE_VULKAN_HARDWARE_COMPUTE
Feature for getSystemAvailableFeatures()
(https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatu
res())
and hasSystemFeature(String,int)
(https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.l
ang.String,%20int))
: If this feature is supported, the Vulkan implementation on this device is hardware accelerated,
and the Vulkan native API will enumerate at least one VkPhysicalDevice, and the feature
version will indicate what level of optional compute features that device supports beyond the
Vulkan 1.0 requirements.
Compute level 0 indicates:
The VK_KHR_variable_pointers extension and
VkPhysicalDeviceVariablePointerFeaturesKHR::variablePointers feature are
supported.
VkPhysicalDeviceLimits::maxPerStageDescriptorStorageBuffers is at least 16.
Constant Value: "android.hardware.vulkan.compute"
FEATURE_VULKAN_HARDWARE_LEVEL
public static final String (https://developer.android.com/reference/java/lang/String) FEATURE_V


Feature for getSystemAvailableFeatures()
(https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatu
res())
and hasSystemFeature(String,int)
(https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.l
ang.String,%20int))
: If this feature is supported, the Vulkan implementation on this device is hardware accelerated,
and the Vulkan native API will enumerate at least one VkPhysicalDevice, and the feature
version will indicate what level of optional hardware features limits it supports.
Level 0 includes the base Vulkan requirements as well as:
VkPhysicalDeviceFeatures::textureCompressionETC2
Level 1 additionally includes:
VkPhysicalDeviceFeatures::fullDrawIndexUint32
VkPhysicalDeviceFeatures::imageCubeArray
VkPhysicalDeviceFeatures::independentBlend
VkPhysicalDeviceFeatures::geometryShader
VkPhysicalDeviceFeatures::tessellationShader
VkPhysicalDeviceFeatures::sampleRateShading
VkPhysicalDeviceFeatures::textureCompressionASTC_LDR
VkPhysicalDeviceFeatures::fragmentStoresAndAtomics
VkPhysicalDeviceFeatures::shaderImageGatherExtended
VkPhysicalDeviceFeatures::shaderUniformBufferArrayDynamicIndexing
VkPhysicalDeviceFeatures::shaderSampledImageArrayDynamicIndexing
Constant Value: "android.hardware.vulkan.level"
public static final String (https://developer.android.com/reference/java/lang/String) FEATURE_V


Added in API level 24 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
FEATURE_VULKAN_HARDWARE_VERSION
Feature for getSystemAvailableFeatures()
(https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatu
res())
and hasSystemFeature(String,int)
(https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.l
ang.String,%20int))
: If this feature is supported, the Vulkan implementation on this device is hardware accelerated,
and the feature version will indicate the highest VkPhysicalDeviceProperties::apiVersion
supported by the physical devices that support the hardware level indicated by
FEATURE_VULKAN_HARDWARE_LEVEL
(https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_VULKAN_HAR
DWARE_LEVEL)
. The feature version uses the same encoding as Vulkan version numbers:
Major version number in bits 31-22
Minor version number in bits 21-12
Patch version number in bits 11-0
A version of 1.1.0 or higher also indicates:
The VK_ANDROID_external_memory_android_hardware_buffer extension is
supported.
SYNC_FD external semaphore and fence handles are supported.
VkPhysicalDeviceSamplerYcbcrConversionFeatures::samplerYcbcrConversion is
supported.
A subset of devices that support Vulkan 1.1 do so via software emulation. For more
information, see Vulkan Design Guidelines
(https://developer.android.com/ndk/guides/graphics/design-notes).
Constant Value: "android.hardware.vulkan.version"
public static final String (https://developer.android.com/reference/java/lang/String) FEATURE_V


Added in API level 34 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Added in API level 20 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
FEATURE_WALLET_LOCATION_BASED_SUGGESTIONS
Feature for getSystemAvailableFeatures()
(https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatu
res())
and hasSystemFeature(String)
(https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.l
ang.String))
: The device supports showing location-based suggestions for wallet cards provided by the
default payment app.
Constant Value: "android.software.wallet_location_based_suggestions"
FEATURE_WATCH
Feature for getSystemAvailableFeatures()
(https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatu
res())
and hasSystemFeature(String)
(https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.l
ang.String))
: This is a device dedicated to showing UI on a watch. A watch here is defined to be a device
worn on the body, perhaps on the wrist. The user is very close when interacting with the device.
Constant Value: "android.hardware.type.watch"
public static final String (https://developer.android.com/reference/java/lang/String) FEATURE_W
public static final String (https://developer.android.com/reference/java/lang/String) FEATURE_W


Added in API level 20 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Added in API level 8 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Added in API level 26 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
FEATURE_WEBVIEW
Feature for getSystemAvailableFeatures()
(https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatu
res())
and hasSystemFeature(String)
(https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.l
ang.String))
: The device has a full implementation of the android.webkit.* APIs. Devices lacking this feature
will not have a functioning WebView implementation.
Constant Value: "android.software.webview"
FEATURE_WIFI
Feature for getSystemAvailableFeatures()
(https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatu
res())
and hasSystemFeature(String)
(https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.l
ang.String))
: The device supports WiFi (802.11) networking.
Constant Value: "android.hardware.wifi"
FEATURE_WIFI_AWARE
public static final String (https://developer.android.com/reference/java/lang/String) FEATURE_W
public static final String (https://developer.android.com/reference/java/lang/String) FEATURE_W


Added in API level 14 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Added in API level 27 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Feature for getSystemAvailableFeatures()
(https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatu
res())
and hasSystemFeature(String)
(https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.l
ang.String))
: The device supports Wi-Fi Aware.
Constant Value: "android.hardware.wifi.aware"
FEATURE_WIFI_DIRECT
Feature for getSystemAvailableFeatures()
(https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatu
res())
and hasSystemFeature(String)
(https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.l
ang.String))
: The device supports Wi-Fi Direct networking.
Constant Value: "android.hardware.wifi.direct"
FEATURE_WIFI_PASSPOINT
public static final String (https://developer.android.com/reference/java/lang/String) FEATURE_W
public static final String (https://developer.android.com/reference/java/lang/String) FEATURE_W


Added in API level 28 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Feature for getSystemAvailableFeatures()
(https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatu
res())
and hasSystemFeature(String)
(https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.l
ang.String))
: The device supports Wi-Fi Passpoint and all Passpoint related APIs in WifiManager
(https://developer.android.com/reference/android/net/wifi/WifiManager) are supported. Refer to
WifiManager.addOrUpdatePasspointConfiguration
(https://developer.android.com/reference/android/net/wifi/WifiManager#addOrUpdatePasspointConfigurati
on(android.net.wifi.hotspot2.PasspointConfiguration))
for more info.
Constant Value: "android.hardware.wifi.passpoint"
FEATURE_WIFI_RTT
Feature for getSystemAvailableFeatures()
(https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatu
res())
and hasSystemFeature(String)
(https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.l
ang.String))
: The device supports Wi-Fi RTT (IEEE 802.11mc).
Constant Value: "android.hardware.wifi.rtt"
public static final String (https://developer.android.com/reference/java/lang/String) FEATURE_W
public static final String (https://developer.android.com/reference/java/lang/String) FEATURE_W


Added in API level 33 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Added in API level 29 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
FEATURE_WINDOW_MAGNIFICATION
Feature for getSystemAvailableFeatures()
(https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatu
res())
and hasSystemFeature(String)
(https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.l
ang.String))
: The device supports window magnification.
See also:
MagnificationConfig.MAGNIFICATION_MODE_WINDOW
(https://developer.android.com/reference/android/accessibilityservice/MagnificationConfig#MAGNIFICATI
ON_MODE_WINDOW)
Constant Value: "android.software.window_magnification"
FLAG_PERMISSION_WHITELIST_INSTALLER
Permission whitelist flag: permissions whitelisted by the installer. Permissions can also be
whitelisted by the system, on upgrade, or on role grant.
Note: In retrospect it would have been preferred to use more inclusive terminology when
naming this API. Similar APIs added will refrain from using the term "whitelist".
Constant Value: 2 (0x00000002)
public static final String (https://developer.android.com/reference/java/lang/String) FEATURE_W
public static final int FLAG_PERMISSION_WHITELIST_INSTALLER


Added in API level 29 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Added in API level 29 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Added in API level 1 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
FLAG_PERMISSION_WHITELIST_SYSTEM
Permission whitelist flag: permissions whitelisted by the system. Permissions can also be
whitelisted by the installer, on upgrade, or on role grant.
Note: In retrospect it would have been preferred to use more inclusive terminology when
naming this API. Similar APIs added will refrain from using the term "whitelist".
Constant Value: 1 (0x00000001)
FLAG_PERMISSION_WHITELIST_UPGRADE
Permission whitelist flag: permissions whitelisted by the system when upgrading from an OS
version where the permission was not restricted to an OS version where the permission is
restricted. Permissions can also be whitelisted by the installer, the system, or on role grant.
Note: In retrospect it would have been preferred to use more inclusive terminology when
naming this API. Similar APIs added will refrain from using the term "whitelist".
Constant Value: 4 (0x00000004)
GET_ACTIVITIES
public static final int FLAG_PERMISSION_WHITELIST_SYSTEM
public static final int FLAG_PERMISSION_WHITELIST_UPGRADE
public static final int GET_ACTIVITIES


Added in API level 31 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Deprecated in API level 34
(https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
or
Added in API level 34 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
PackageInfo (https://developer.android.com/reference/android/content/pm/PackageInfo) flag: return
information about activities in the package in PackageInfo.activities
(https://developer.android.com/reference/android/content/pm/PackageInfo#activities).
Constant Value: 1 (0x00000001)
GET_ATTRIBUTIONS
This constant was deprecated in API level 34.
Use GET_ATTRIBUTIONS_LONG
(https://developer.android.com/reference/android/content/pm/PackageManager#GET_ATTRIBUTIONS_LO
NG)
to avoid unintended sign extension. Operations with this flag may cause unintended results and potential
RuntimeException (https://developer.android.com/reference/java/lang/RuntimeException).
Constant Value: -2147483648 (0x80000000)
GET_ATTRIBUTIONS_LONG
PackageInfo (https://developer.android.com/reference/android/content/pm/PackageInfo) flag: return
all attributions declared in the package manifest
Constant Value: 2147483648 (0x0000000080000000)
public static final int GET_ATTRIBUTIONS
public static final long GET_ATTRIBUTIONS_LONG


Added in API level 3 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Added in API level 1 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Deprecated in API level 24
(https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
or
Added in API level 18 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Deprecated in API level 24
GET_CONFIGURATIONS
PackageInfo (https://developer.android.com/reference/android/content/pm/PackageInfo) flag: return
information about hardware preferences in PackageInfo.configPreferences
(https://developer.android.com/reference/android/content/pm/PackageInfo#configPreferences), and
requested features in PackageInfo.reqFeatures
(https://developer.android.com/reference/android/content/pm/PackageInfo#reqFeatures) and
PackageInfo.featureGroups
(https://developer.android.com/reference/android/content/pm/PackageInfo#featureGroups).
Constant Value: 16384 (0x00004000)
GET_DISABLED_COMPONENTS
This constant was deprecated in API level 24.
replaced with MATCH_DISABLED_COMPONENTS
(https://developer.android.com/reference/android/content/pm/PackageManager#MATCH_DISABLED_COM
PONENTS)
Constant Value: 512 (0x00000200)
GET_DISABLED_UNTIL_USED_COMPONENTS
public static final int GET_CONFIGURATIONS
public static final int GET_DISABLED_COMPONENTS


(https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
or
Added in API level 1 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Added in API level 1 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
This constant was deprecated in API level 24.
replaced with MATCH_DISABLED_UNTIL_USED_COMPONENTS
(https://developer.android.com/reference/android/content/pm/PackageManager#MATCH_DISABLED_UNTI
L_USED_COMPONENTS)
.
Constant Value: 32768 (0x00008000)
GET_GIDS
PackageInfo (https://developer.android.com/reference/android/content/pm/PackageInfo) flag: return
the group ids (https://developer.android.com/reference/android/content/pm/PackageInfo#gids) that
are associated with an application. This applies for any API returning a PackageInfo class,
either directly or nested inside of another.
Constant Value: 256 (0x00000100)
GET_INSTRUMENTATION
public static final int GET_DISABLED_UNTIL_USED_COMPONENTS
public static final int GET_GIDS
public static final int GET_INSTRUMENTATION


Added in API level 1 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Deprecated in API level 31
(https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
or
Added in API level 1 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
PackageInfo (https://developer.android.com/reference/android/content/pm/PackageInfo) flag: return
information about instrumentation in the package in PackageInfo.instrumentation
(https://developer.android.com/reference/android/content/pm/PackageInfo#instrumentation).
Constant Value: 16 (0x00000010)
GET_INTENT_FILTERS
This constant was deprecated in API level 31.
The platform does not support getting IntentFilter
(https://developer.android.com/reference/android/content/IntentFilter)s for the package.
PackageInfo (https://developer.android.com/reference/android/content/pm/PackageInfo) flag: return
information about the intent filters supported by the activity.
Constant Value: 32 (0x00000020)
GET_META_DATA
ComponentInfo (https://developer.android.com/reference/android/content/pm/ComponentInfo) flag:
return the ComponentInfo.metaData
(https://developer.android.com/reference/android/content/pm/PackageItemInfo#metaData) data Bundle
public static final int GET_INTENT_FILTERS
public static final int GET_META_DATA


Added in API level 1 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Added in API level 1 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Added in API level 1 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
(https://developer.android.com/reference/android/os/Bundle)s that are associated with a component.
This applies for any API returning a ComponentInfo subclass.
Constant Value: 128 (0x00000080)
GET_PERMISSIONS
PackageInfo (https://developer.android.com/reference/android/content/pm/PackageInfo) flag: return
information about permissions in the package in PackageInfo.permissions
(https://developer.android.com/reference/android/content/pm/PackageInfo#permissions).
Constant Value: 4096 (0x00001000)
GET_PROVIDERS
PackageInfo (https://developer.android.com/reference/android/content/pm/PackageInfo) flag: return
information about content providers in the package in PackageInfo.providers
(https://developer.android.com/reference/android/content/pm/PackageInfo#providers).
Constant Value: 8 (0x00000008)
GET_RECEIVERS
public static final int GET_PERMISSIONS
public static final int GET_PROVIDERS


Added in API level 1 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Added in API level 1 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
PackageInfo (https://developer.android.com/reference/android/content/pm/PackageInfo) flag: return
information about intent receivers in the package in PackageInfo.receivers
(https://developer.android.com/reference/android/content/pm/PackageInfo#receivers).
Constant Value: 2 (0x00000002)
GET_RESOLVED_FILTER
ResolveInfo (https://developer.android.com/reference/android/content/pm/ResolveInfo) flag: return
the IntentFilter that was matched for a particular ResolveInfo in ResolveInfo.filter
(https://developer.android.com/reference/android/content/pm/ResolveInfo#filter).
Constant Value: 64 (0x00000040)
GET_SERVICES
PackageInfo (https://developer.android.com/reference/android/content/pm/PackageInfo) flag: return
information about services in the package in PackageInfo.services
(https://developer.android.com/reference/android/content/pm/PackageInfo#services).
Constant Value: 4 (0x00000004)
public static final int GET_RECEIVERS
public static final int GET_RESOLVED_FILTER
public static final int GET_SERVICES


Added in API level 1 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Added in API level 1 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Deprecated in API level 28
(https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
or
Added in API level 28 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
GET_SHARED_LIBRARY_FILES
ApplicationInfo (https://developer.android.com/reference/android/content/pm/ApplicationInfo) flag:
return the paths to the shared libraries
(https://developer.android.com/reference/android/content/pm/ApplicationInfo#sharedLibraryFiles) that
are associated with an application. This applies for any API returning an ApplicationInfo class,
either directly or nested inside of another.
Constant Value: 1024 (0x00000400)
GET_SIGNATURES
This constant was deprecated in API level 28.
use GET_SIGNING_CERTIFICATES instead
PackageInfo (https://developer.android.com/reference/android/content/pm/PackageInfo) flag: return
information about the signatures included in the package.
Constant Value: 64 (0x00000040)
GET_SIGNING_CERTIFICATES
public static final int GET_SHARED_LIBRARY_FILES
public static final int GET_SIGNATURES


Added in API level 3 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Deprecated in API level 24
(https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
or
Added in API level 1 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
PackageInfo (https://developer.android.com/reference/android/content/pm/PackageInfo) flag: return
the signing certificates associated with this package. Each entry is a signing certificate that the
package has proven it is authorized to use, usually a past signing certificate from which it has
rotated.
Constant Value: 134217728 (0x08000000)
GET_UNINSTALLED_PACKAGES
This constant was deprecated in API level 24.
replaced with MATCH_UNINSTALLED_PACKAGES
(https://developer.android.com/reference/android/content/pm/PackageManager#MATCH_UNINSTALLED_
PACKAGES)
Constant Value: 8192 (0x00002000)
GET_URI_PERMISSION_PATTERNS
public static final int GET_SIGNING_CERTIFICATES
public static final int GET_UNINSTALLED_PACKAGES
public static final int GET_URI_PERMISSION_PATTERNS


Added in API level 26 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Added in API level 26 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Added in API level 26 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
ProviderInfo (https://developer.android.com/reference/android/content/pm/ProviderInfo) flag: return
the URI permission patterns
(https://developer.android.com/reference/android/content/pm/ProviderInfo#uriPermissionPatterns) that
are associated with a content provider. This applies for any API returning a ProviderInfo class,
either directly or nested inside of another.
Constant Value: 2048 (0x00000800)
INSTALL_REASON_DEVICE_RESTORE
Code indicating that this package was installed as part of restoring from another device.
Constant Value: 2 (0x00000002)
INSTALL_REASON_DEVICE_SETUP
Code indicating that this package was installed as part of device setup.
Constant Value: 3 (0x00000003)
INSTALL_REASON_POLICY
public static final int INSTALL_REASON_DEVICE_RESTORE
public static final int INSTALL_REASON_DEVICE_SETUP


Added in API level 26 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Added in API level 26 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Added in API level 31 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Code indicating that this package was installed due to enterprise policy.
Constant Value: 1 (0x00000001)
INSTALL_REASON_UNKNOWN
Code indicating that the reason for installing this package is unknown.
Constant Value: 0 (0x00000000)
INSTALL_REASON_USER
Code indicating that the package installation was initiated by the user.
Constant Value: 4 (0x00000004)
INSTALL_SCENARIO_BULK
public static final int INSTALL_REASON_POLICY
public static final int INSTALL_REASON_UNKNOWN
public static final int INSTALL_REASON_USER


Added in API level 31 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Added in API level 31 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Installation scenario indicating a bulk operation with the desired result of a fully optimized
application. If the system is busy or resources are scarce the system will perform less work to
avoid impacting system health. Examples of bulk installation scenarios might include device
restore, background updates of multiple applications, or user-triggered updates for all
applications. The decision to use BULK or BULK_SECONDARY should be based on the desired
user experience. BULK_SECONDARY operations may take less time to complete but, when they
do, will produce less optimized applications. The device state (e.g. memory usage or battery
status) should not be considered when making this decision as those factors are taken into
account by the Package Manager when acting on the installation scenario.
Constant Value: 2 (0x00000002)
INSTALL_SCENARIO_BULK_SECONDARY
Installation scenario indicating a bulk operation that prioritizes minimal system health impact
over application optimization. The application may undergo additional optimization if the
system is idle and system resources are abundant. The more elements of a bulk operation that
are marked BULK_SECONDARY, the faster the entire bulk operation will be. See the comments
for INSTALL_SCENARIO_BULK for more information.
Constant Value: 3 (0x00000003)
INSTALL_SCENARIO_DEFAULT
public static final int INSTALL_SCENARIO_BULK
public static final int INSTALL_SCENARIO_BULK_SECONDARY


Added in API level 31 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Added in API level 23 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Added in API level 29 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
A value to indicate the lack of CUJ information, disabling all installation scenario logic.
Constant Value: 0 (0x00000000)
INSTALL_SCENARIO_FAST
Installation scenario providing the fastest "install button to launch" experience possible.
Constant Value: 1 (0x00000001)
MATCH_ALL
Querying flag: if set and if the platform is doing any filtering of the results, then the filtering will
not happen. This is a synonym for saying that all results should be returned.
This flag should be used with extreme care.
Constant Value: 131072 (0x00020000)
MATCH_APEX
public static final int INSTALL_SCENARIO_DEFAULT
public static final int INSTALL_SCENARIO_FAST
public static final int MATCH_ALL


Added in API level 35 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Added in API level 1 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
PackageInfo (https://developer.android.com/reference/android/content/pm/PackageInfo) flag: include
APEX packages that are currently installed. In APEX terminology, this corresponds to packages
that are currently active, i.e. mounted and available to other processes of the OS. In particular,
this flag alone will not match APEX files that are staged for activation at next reboot.
Constant Value: 1073741824 (0x40000000)
MATCH_ARCHIVED_PACKAGES
Flag parameter to also retrieve some information about archived packages. Packages can be
archived through PackageInstaller.requestArchive
(https://developer.android.com/reference/android/content/pm/PackageInstaller#requestArchive(java.lang.
String,%20android.content.IntentSender))
and do not have any APKs stored on the device, but do keep the data directory.
Note: Archived apps are a subset of apps returned by MATCH_UNINSTALLED_PACKAGES
(https://developer.android.com/reference/android/content/pm/PackageManager#MATCH_UNINSTALLED_
PACKAGES)
.
Note: this flag may cause less information about currently installed applications to be returned.
Note: use of this flag requires the android.permission.QUERY_ALL_PACKAGES permission to
see uninstalled packages.
Constant Value: 4294967296 (0x0000000100000000)
MATCH_DEFAULT_ONLY
public static final int MATCH_APEX
public static final long MATCH_ARCHIVED_PACKAGES


Added in API level 29 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Resolution and querying flag: if set, only filters that support the Intent.CATEGORY_DEFAULT
(https://developer.android.com/reference/android/content/Intent#CATEGORY_DEFAULT) will be
considered for matching. This is a synonym for including the CATEGORY_DEFAULT in your
supplied Intent.
Constant Value: 65536 (0x00010000)
MATCH_DIRECT_BOOT_AUTO
Querying flag: automatically match components based on their Direct Boot awareness and the
current user state.
Since the default behavior is to automatically apply the current user state, this is effectively a
sentinel value that doesn't change the output of any queries based on its presence or absence.
Instead, this value can be useful in conjunction with
StrictMode.VmPolicy.Builder.detectImplicitDirectBoot()
(https://developer.android.com/reference/android/os/StrictMode.VmPolicy.Builder#detectImplicitDirectBoo
t())
to detect when a caller is relying on implicit automatic matching, instead of confirming the
explicit behavior they want, using a combination of these flags:
MATCH_DIRECT_BOOT_AWARE
 (https://developer.android.com/reference/android/content/pm/PackageManager#MATCH_DIRECT_B
OOT_AWARE)
MATCH_DIRECT_BOOT_UNAWARE
 (https://developer.android.com/reference/android/content/pm/PackageManager#MATCH_DIRECT_B
OOT_UNAWARE)
public static final int MATCH_DEFAULT_ONLY
public static final int MATCH_DIRECT_BOOT_AUTO


Added in API level 24 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
MATCH_DIRECT_BOOT_AUTO
 (https://developer.android.com/reference/android/content/pm/PackageManager#MATCH_DIRECT_B
OOT_AUTO)
Constant Value: 268435456 (0x10000000)
MATCH_DIRECT_BOOT_AWARE
Querying flag: match components which are direct boot aware in the returned info, regardless
of the current user state.
When neither MATCH_DIRECT_BOOT_AWARE
(https://developer.android.com/reference/android/content/pm/PackageManager#MATCH_DIRECT_BOOT_
AWARE)
nor MATCH_DIRECT_BOOT_UNAWARE
(https://developer.android.com/reference/android/content/pm/PackageManager#MATCH_DIRECT_BOOT_
UNAWARE)
are specified, the default behavior is to match only runnable components based on the user
state. For example, when a user is started but credentials have not been presented yet, the user
is running "locked" and only MATCH_DIRECT_BOOT_AWARE
(https://developer.android.com/reference/android/content/pm/PackageManager#MATCH_DIRECT_BOOT_
AWARE)
components are returned. Once the user credentials have been presented, the user is running
"unlocked" and both MATCH_DIRECT_BOOT_AWARE
(https://developer.android.com/reference/android/content/pm/PackageManager#MATCH_DIRECT_BOOT_
AWARE)
and MATCH_DIRECT_BOOT_UNAWARE
(https://developer.android.com/reference/android/content/pm/PackageManager#MATCH_DIRECT_BOOT_
UNAWARE)
components are returned.
See also:
public static final int MATCH_DIRECT_BOOT_AWARE


Added in API level 24 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
UserManager.isUserUnlocked()
(https://developer.android.com/reference/android/os/UserManager#isUserUnlocked())
Constant Value: 524288 (0x00080000)
MATCH_DIRECT_BOOT_UNAWARE
Querying flag: match components which are direct boot unaware in the returned info,
regardless of the current user state.
When neither MATCH_DIRECT_BOOT_AWARE
(https://developer.android.com/reference/android/content/pm/PackageManager#MATCH_DIRECT_BOOT_
AWARE)
nor MATCH_DIRECT_BOOT_UNAWARE
(https://developer.android.com/reference/android/content/pm/PackageManager#MATCH_DIRECT_BOOT_
UNAWARE)
are specified, the default behavior is to match only runnable components based on the user
state. For example, when a user is started but credentials have not been presented yet, the user
is running "locked" and only MATCH_DIRECT_BOOT_AWARE
(https://developer.android.com/reference/android/content/pm/PackageManager#MATCH_DIRECT_BOOT_
AWARE)
components are returned. Once the user credentials have been presented, the user is running
"unlocked" and both MATCH_DIRECT_BOOT_AWARE
(https://developer.android.com/reference/android/content/pm/PackageManager#MATCH_DIRECT_BOOT_
AWARE)
and MATCH_DIRECT_BOOT_UNAWARE
(https://developer.android.com/reference/android/content/pm/PackageManager#MATCH_DIRECT_BOOT_
UNAWARE)
components are returned.
See also:
UserManager.isUserUnlocked()
(https://developer.android.com/reference/android/os/UserManager#isUserUnlocked())
public static final int MATCH_DIRECT_BOOT_UNAWARE


Added in API level 24 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Added in API level 24 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Added in API level 24 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Constant Value: 262144 (0x00040000)
MATCH_DISABLED_COMPONENTS
PackageInfo (https://developer.android.com/reference/android/content/pm/PackageInfo) flag: include
disabled components in the returned info.
Constant Value: 512 (0x00000200)
MATCH_DISABLED_UNTIL_USED_COMPONENTS
PackageInfo (https://developer.android.com/reference/android/content/pm/PackageInfo) flag: include
disabled components which are in that state only because of
COMPONENT_ENABLED_STATE_DISABLED_UNTIL_USED
(https://developer.android.com/reference/android/content/pm/PackageManager#COMPONENT_ENABLED
_STATE_DISABLED_UNTIL_USED)
in the returned info. Note that if you set this flag, applications that are in this disabled state will
be reported as enabled.
Constant Value: 32768 (0x00008000)
MATCH_SYSTEM_ONLY
public static final int MATCH_DISABLED_COMPONENTS
public static final int MATCH_DISABLED_UNTIL_USED_COMPONENTS


Added in API level 24 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Added in API level 17 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Querying flag: include only components from applications that are marked with
ApplicationInfo.FLAG_SYSTEM
(https://developer.android.com/reference/android/content/pm/ApplicationInfo#FLAG_SYSTEM).
Constant Value: 1048576 (0x00100000)
MATCH_UNINSTALLED_PACKAGES
Flag parameter to retrieve some information about all applications (even uninstalled ones)
which have data directories. This state could have resulted if applications have been deleted
with flag DELETE_KEEP_DATA with a possibility of being replaced or reinstalled in future.
Note: this flag may cause less information about currently installed applications to be returned.
Note: use of this flag requires the android.permission.QUERY_ALL_PACKAGES permission to
see uninstalled packages.
Constant Value: 8192 (0x00002000)
MAXIMUM_VERIFICATION_TIMEOUT
public static final int MATCH_SYSTEM_ONLY
public static final int MATCH_UNINSTALLED_PACKAGES
public static final long MAXIMUM_VERIFICATION_TIMEOUT


Added in API level 1 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Added in API level 1 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Can be used as the millisecondsToDelay argument for
PackageManager.extendVerificationTimeout
(https://developer.android.com/reference/android/content/pm/PackageManager#extendVerificationTimeo
ut(int,%20int,%20long))
. This is the maximum time PackageManager waits for the verification agent to return (in
milliseconds).
Constant Value: 3600000 (0x000000000036ee80)
PERMISSION_DENIED
Permission check result: this is returned by checkPermission(String, String)
(https://developer.android.com/reference/android/content/pm/PackageManager#checkPermission(java.la
ng.String,%20java.lang.String))
if the permission has not been granted to the given package.
Constant Value: -1 (0xffffffff)
PERMISSION_GRANTED
Permission check result: this is returned by checkPermission(String, String)
(https://developer.android.com/reference/android/content/pm/PackageManager#checkPermission(java.la
ng.String,%20java.lang.String))
if the permission has been granted to the given package.
Constant Value: 0 (0x00000000)
public static final int PERMISSION_DENIED
public static final int PERMISSION_GRANTED


Added in API level 34 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
PROPERTY_COMPAT_OVERRIDE_LANDSCAPE_TO_PORTRAIT
Application level PackageManager .Property
(https://developer.android.com/reference/android/content/pm/PackageManager.Property) for an app to
inform the system that the app can be opted-in or opted-out from the compatibility treatment
that rotates camera output by 90 degrees on landscape sensors on devices known to have
compatibility issues.
The treatment is disabled by default but device manufacturers can enable the treatment using
their discretion to improve camera compatibility. With this property set to false, the rotation
will not be applied. A value of true will ensure that rotation is applied, provided it is enabled for
the device. In most cases, if rotation is the desired behavior this property need not be set.
However, if your app experiences stretching or incorrect rotation on these devices, explicitly
setting this to true may resolve that behavior. Apps should set this to false if there is
confidence that the app handles CameraCharacteristics.SENSOR_ORIENTATION
(https://developer.android.com/reference/android/hardware/camera2/CameraCharacteristics#SENSOR_OR
IENTATION)
correctly. See the documentation for best practice.
(https://developer.android.com/training/camera2/camera-preview)
Syntax:
Constant Value:
"android.camera.PROPERTY_COMPAT_OVERRIDE_LANDSCAPE_TO_PORTRAIT"
public static final String (https://developer.android.com/reference/java/lang/String) PROPERTY_
<application>
  <property
    android:name="android.camera.PROPERTY_COMPAT_OVERRIDE_LANDSCAPE_TO_PORTRAIT
    android:value="true|false"/>
</application>


Added in API level 31 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Added in API level 37 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
PROPERTY_MEDIA_CAPABILITIES
<application> level PackageManager.Property
(https://developer.android.com/reference/android/content/pm/PackageManager.Property) tag specifying
the XML resource ID containing an application's media capabilities XML file For example:
<application> <property android:name="android.media.PROPERTY_MEDIA_CAPABILITIES"
android:resource="@xml/media_capabilities"> <application>
Constant Value: "android.media.PROPERTY_MEDIA_CAPABILITIES"
PROPERTY_NATIVE_SERVICE_FUNCTION_NAME
Service level PackageManager.Property
(https://developer.android.com/reference/android/content/pm/PackageManager.Property) tag for native
services specifying the symbol name of the entry point function for the service. If not specified,
the system executes ANativeService_onCreate.
Example:
public static final String (https://developer.android.com/reference/java/lang/String) PROPERTY_
public static final String (https://developer.android.com/reference/java/lang/String) PROPERTY_
 <service android:isolatedProcess="true"
                   android:nativeService="true">
   <property
     android:name="android.app.PROPERTY_NATIVE_SERVICE_FUNCTION_NAME"
     android:value="native_service_createService"/>


Added in API level 37 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Added in API level 34 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Constant Value: "android.app.PROPERTY_NATIVE_SERVICE_FUNCTION_NAME"
PROPERTY_NATIVE_SERVICE_LIBRARY_NAME
Service level PackageManager.Property
(https://developer.android.com/reference/android/content/pm/PackageManager.Property) tag for native
services specifying the name of the library to be loaded to the process that hosts the service. If
not specified, the system tries to load libmain.so.
Example:
Constant Value: "android.app.PROPERTY_NATIVE_SERVICE_LIBRARY_NAME"
PROPERTY_SELF_CERTIFIED_NETWORK_CAPABILITIES
</service>
public static final String (https://developer.android.com/reference/java/lang/String) PROPERTY_
<service android:isolatedProcess="true"
                  android:nativeService="true">
  <property
    android:name="android.app.PROPERTY_NATIVE_SERVICE_LIBRARY_NAME"
    android:value="libnativeservice.so"/>
</service>


Added in API level 34 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
<application> level PackageManager.Property
(https://developer.android.com/reference/android/content/pm/PackageManager.Property) tag specifying
the XML resource ID containing the declaration of the self-certified network capabilities used
by the application.
Starting from Android 14, usage of some network capabilities in
ConnectivityManager.requestNetwork(NetworkRequest, PendingIntent)
(https://developer.android.com/reference/android/net/ConnectivityManager#requestNetwork(android.net.N
etworkRequest,%20android.app.PendingIntent))
require the application to declare its usage of that particular capability in this resource. Only
some capabilities require a declaration. Please look up the specific capability you want to use
in NetworkCapabilities (https://developer.android.com/reference/android/net/NetworkCapabilities)
to see if it needs declaration in this property. For example: <application> <property
android:name="android.net.PROPERTY_SELF_CERTIFIED_NETWORK_CAPABILITIES"
android:resource="@xml/self_certified_network_capabilities"> <application>
The detail format of self_certified_network_capabilities.xml is described in NetworkRequest
(https://developer.android.com/reference/android/net/NetworkRequest)
Constant Value: "android.net.PROPERTY_SELF_CERTIFIED_NETWORK_CAPABILITIES"
PROPERTY_SPECIAL_USE_FGS_SUBTYPE
<service> level PackageManager.Property
(https://developer.android.com/reference/android/content/pm/PackageManager.Property) tag specifying
the actual use case of the service if it's foreground service with the type
ServiceInfo.FOREGROUND_SERVICE_TYPE_SPECIAL_USE
public static final String (https://developer.android.com/reference/java/lang/String) PROPERTY_
public static final String (https://developer.android.com/reference/java/lang/String) PROPERTY_


Added in API level 36 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
(https://developer.android.com/reference/android/content/pm/ServiceInfo#FOREGROUND_SERVICE_TYPE_
SPECIAL_USE)
.
For example: <service> <property
android:name="android.app.PROPERTY_SPECIAL_USE_FGS_SUBTYPE" android:value="foo"/>
</service>
Constant Value: "android.app.PROPERTY_SPECIAL_USE_FGS_SUBTYPE"
PROPERTY_USE_RESTRICTED_BACKUP_MODE
<application> level PackageManager.Property
(https://developer.android.com/reference/android/content/pm/PackageManager.Property) tag specifying
whether the app should be put into the "restricted" backup mode when it's started for backup
and restore operations.
See for information about restricted mode
(https://developer.android.com/identity/data/autobackup#ImplementingBackupAgent).
Starting with Android 16 apps may not be started in restricted mode based on this property.
Syntax:
public static final String (https://developer.android.com/reference/java/lang/String) PROPERTY_
<application>
  <property
    android:name="android.app.backup.PROPERTY_USE_RESTRICTED_BACKUP_MODE"
    android:value="true|false"/>
</application>


Added in API level 1 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Added in API level 1 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
If this property is set, the operating system will respect it for now (see Note below). If it's not
set, the behavior depends on the SDK level that the app is targeting. For apps targeting SDK
level Build.VERSION_CODES.VANILLA_ICE_CREAM
(https://developer.android.com/reference/android/os/Build.VERSION_CODES#VANILLA_ICE_CREAM) or
lower, the property defaults to true. For apps targeting SDK level
Build.VERSION_CODES.BAKLAVA
(https://developer.android.com/reference/android/os/Build.VERSION_CODES#BAKLAVA) or higher, the
operating system will make a decision dynamically.
Note: It's not recommended to set this property to true unless absolutely necessary. In a
future Android version, this property may be deprecated in favor of removing restricted mode
completely.
Constant Value: "android.app.backup.PROPERTY_USE_RESTRICTED_BACKUP_MODE"
SIGNATURE_FIRST_NOT_SIGNED
Signature check result: this is returned by checkSignatures(int, int)
(https://developer.android.com/reference/android/content/pm/PackageManager#checkSignatures(int,%20i
nt))
if the first package is not signed but the second is.
Constant Value: -1 (0xffffffff)
SIGNATURE_MATCH
public static final int SIGNATURE_FIRST_NOT_SIGNED
public static final int SIGNATURE_MATCH


Added in API level 1 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Added in API level 1 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Signature check result: this is returned by checkSignatures(int, int)
(https://developer.android.com/reference/android/content/pm/PackageManager#checkSignatures(int,%20i
nt))
if all signatures on the two packages match.
Constant Value: 0 (0x00000000)
SIGNATURE_NEITHER_SIGNED
Signature check result: this is returned by checkSignatures(int, int)
(https://developer.android.com/reference/android/content/pm/PackageManager#checkSignatures(int,%20i
nt))
if neither of the two packages is signed.
Constant Value: 1 (0x00000001)
SIGNATURE_NO_MATCH
Signature check result: this is returned by checkSignatures(int, int)
(https://developer.android.com/reference/android/content/pm/PackageManager#checkSignatures(int,%20i
nt))
if not all signatures on both packages match.
Constant Value: -3 (0xfffffffd)
public static final int SIGNATURE_NEITHER_SIGNED
public static final int SIGNATURE_NO_MATCH


Added in API level 1 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Added in API level 1 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Added in API level 30 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
SIGNATURE_SECOND_NOT_SIGNED
Signature check result: this is returned by checkSignatures(int, int)
(https://developer.android.com/reference/android/content/pm/PackageManager#checkSignatures(int,%20i
nt))
if the second package is not signed but the first is.
Constant Value: -2 (0xfffffffe)
SIGNATURE_UNKNOWN_PACKAGE
Signature check result: this is returned by checkSignatures(int, int)
(https://developer.android.com/reference/android/content/pm/PackageManager#checkSignatures(int,%20i
nt))
if either of the packages are not valid.
Constant Value: -4 (0xfffffffc)
SYNCHRONOUS
Flag parameter for setComponentEnabledSetting(android.content.ComponentName, int,
int)
public static final int SIGNATURE_SECOND_NOT_SIGNED
public static final int SIGNATURE_UNKNOWN_PACKAGE
public static final int SYNCHRONOUS


Added in API level 14 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Added in API level 14 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
(https://developer.android.com/reference/android/content/pm/PackageManager#setComponentEnabledSe
tting(android.content.ComponentName,%20int,%20int))
to indicate that the given user's package restrictions state will be serialised to disk after the
component state has been updated. Note that this is synchronous disk access, so calls using
this flag should be run on a background thread.
Constant Value: 2 (0x00000002)
VERIFICATION_ALLOW
Used as the verificationCode argument for PackageManager.verifyPendingInstall
(https://developer.android.com/reference/android/content/pm/PackageManager#verifyPendingInstall(int,%
20int))
to indicate that the calling package verifier allows the installation to proceed.
Constant Value: 1 (0x00000001)
VERIFICATION_REJECT
Used as the verificationCode argument for PackageManager.verifyPendingInstall
(https://developer.android.com/reference/android/content/pm/PackageManager#verifyPendingInstall(int,%
20int))
to indicate the calling package verifier does not vote to allow the installation to proceed.
Constant Value: -1 (0xffffffff)
public static final int VERIFICATION_ALLOW
public static final int VERIFICATION_REJECT


Added in API level 26 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Added in API level 31 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Added in API level 31 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
VERSION_CODE_HIGHEST
Constant for specifying the highest installed package version code.
Constant Value: -1 (0xffffffff)
Fields
TRUST_ALL
Trust any Installer to provide checksums for the package.
See also:
requestChecksums(String, boolean, int, List, OnChecksumsReadyListener)
(https://developer.android.com/reference/android/content/pm/PackageManager#requestChecksums(java.l
ang.String,%20boolean,%20int,%20java.util.List%3Cjava.security.cert.Certificate%3E,%20android.content.pm.
PackageManager.OnChecksumsReadyListener))
TRUST_NONE
public static final int VERSION_CODE_HIGHEST
public static final List (https://developer.android.com/reference/java/util/List)<Certificate (ht
public static final List (https://developer.android.com/reference/java/util/List)<Certificate (ht


Added in API level 1 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
or
Added in API level 1 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Deprecated in API level 15
(https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Don't trust any Installer to provide checksums for the package. This effectively disables
optimized Installer-enforced checksums.
See also:
requestChecksums(String, boolean, int, List, OnChecksumsReadyListener)
(https://developer.android.com/reference/android/content/pm/PackageManager#requestChecksums(java.l
ang.String,%20boolean,%20int,%20java.util.List%3Cjava.security.cert.Certificate%3E,%20android.content.pm.
PackageManager.OnChecksumsReadyListener))
Public constructors
PackageManager
This constructor is deprecated.
Do not instantiate or subclass - obtain an instance from Context.getPackageManager
(https://developer.android.com/reference/android/content/Context#getPackageManager())
Public methods
addPackageToPreferred
public PackageManager ()
public abstract void addPackageToPreferred (String (https://developer.android.com/referenc


or
Added in API level 1 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
This method was deprecated in API level 15.
This function no longer does anything. It is the platform's responsibility to assign preferred activities and this
cannot be modified directly. To determine the activities resolved by the platform, use
resolveActivity(Intent, ResolveInfoFlags)
(https://developer.android.com/reference/android/content/pm/PackageManager#resolveActivity(android.c
ontent.Intent,%20android.content.pm.PackageManager.ResolveInfoFlags))
or queryIntentActivities(Intent, ResolveInfoFlags)
(https://developer.android.com/reference/android/content/pm/PackageManager#queryIntentActivities(and
roid.content.Intent,%20android.content.pm.PackageManager.ResolveInfoFlags))
. To configure an app to be responsible for a particular role and to check current role holders, see
RoleManager (https://developer.android.com/reference/android/app/role/RoleManager).
Parameters
packageName
String: This value cannot be null.
addPermission
Add a new dynamic permission to the system. For this to work, your package must have
defined a permission tree through the <permission-tree>
(https://developer.android.com/reference/android/R.styleable#AndroidManifestPermissionTree) tag in its
manifest. A package can only add permissions to trees that were defined by either its own
package or another with the same user id; a permission is in a tree if it matches the name of
the permission tree + ".": for example, "com.foo.bar" is a member of the permission tree
"com.foo".
It is good to make your permission tree name descriptive, because you are taking possession
of that entire set of permission names. Thus, it must be under a domain you control, with a
public abstract boolean addPermission (PermissionInfo (https://developer.android.com/refer


Added in API level 8 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
suffix that will not match any normal permissions that may be declared in any applications that
are part of that domain.
New permissions must be added before any .apks are installed that use those permissions.
Permissions you add through this method are remembered across reboots of the device. If the
given permission already exists, the info you supply here will be used to update it.
Parameters
info
PermissionInfo: Description of the permission to be added.
This value cannot be null.
Returns
boolean
Returns true if a new permission was created, false if an existing one was
updated.
Throws
SecurityException
(https://developer.android.com/reference/java/lang/SecurityException)
if you are not allowed to add the
given permission name.
See also:
removePermission(String)
(https://developer.android.com/reference/android/content/pm/PackageManager#removePermission(java.l
ang.String))
addPermissionAsync


Added in API level 1 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Deprecated in API level 15
(https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Like addPermission(PermissionInfo)
(https://developer.android.com/reference/android/content/pm/PackageManager#addPermission(android.c
ontent.pm.PermissionInfo))
but asynchronously persists the package manager state after returning from the call, allowing
it to return quicker and batch a series of adds at the expense of no guarantee the added
permission will be retained if the device is rebooted before it is written.
Parameters
info
PermissionInfo: This value cannot be null.
Returns
boolean
addPreferredActivity
public abstract boolean addPermissionAsync (PermissionInfo (https://developer.android.com
public abstract void addPreferredActivity (IntentFilter (https://developer.android.com/re
               int match, 
               ComponentName[] (https://developer.android.com/reference/android/content/Compo
               ComponentName (https://developer.android.com/reference/android/content/Compone


orThis method was deprecated in API level 15.
This function no longer does anything. It is the platform's responsibility to assign preferred activities and this
cannot be modified directly. To determine the activities resolved by the platform, use
resolveActivity(Intent, ResolveInfoFlags)
(https://developer.android.com/reference/android/content/pm/PackageManager#resolveActivity(android.c
ontent.Intent,%20android.content.pm.PackageManager.ResolveInfoFlags))
or queryIntentActivities(Intent, ResolveInfoFlags)
(https://developer.android.com/reference/android/content/pm/PackageManager#queryIntentActivities(and
roid.content.Intent,%20android.content.pm.PackageManager.ResolveInfoFlags))
. To configure an app to be responsible for a particular role and to check current role holders, see
RoleManager (https://developer.android.com/reference/android/app/role/RoleManager).
Add a new preferred activity mapping to the system. This will be used to automatically select
the given activity component when Context.startActivity()
(https://developer.android.com/reference/android/content/Context#startActivity(android.content.Intent))
finds multiple matching activities and also matches the given filter.
Parameters
filter
IntentFilter: The set of intents under which this activity will be made
preferred.
This value cannot be null.
match
int: The IntentFilter match category that this preference applies to.
set
ComponentName: The set of activities that the user was picking from
when this preference was made.
This value may be null.
activity
ComponentName: The component name of the activity that is to be
preferred.
This value cannot be null.


Added in API level 29 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
addWhitelistedRestrictedPermission
Adds a whitelisted restricted permission for an app.
Permissions can be hard restricted which means that the app cannot hold them or soft
restricted where the app can hold the permission but in a weaker form. Whether a permission
is hard restricted
(https://developer.android.com/reference/android/content/pm/PermissionInfo#FLAG_HARD_RESTRICTED)
or soft restricted
(https://developer.android.com/reference/android/content/pm/PermissionInfo#FLAG_SOFT_RESTRICTED)
depends on the permission declaration. Whitelisting a hard restricted permission allows for the
to hold that permission and whitelisting a soft restricted permission allows the app to hold the
permission in its full, unrestricted form.
There are four whitelists:
1. one for cases where the system permission policy whitelists a permission This list
corresponds to the FLAG_PERMISSION_WHITELIST_SYSTEM
 (https://developer.android.com/reference/android/content/pm/PackageManager#FLAG_PERMISSIO
N_WHITELIST_SYSTEM)
flag. Can only be modified by pre-installed holders of a dedicated permission.
2. one for cases where the system whitelists the permission when upgrading from an OS
version in which the permission was not restricted to an OS version in which the
permission is restricted. This list corresponds to the
FLAG_PERMISSION_WHITELIST_UPGRADE
 (https://developer.android.com/reference/android/content/pm/PackageManager#FLAG_PERMISSIO
N_WHITELIST_UPGRADE)
flag. Can be modified by pre-installed holders of a dedicated permission. The installer on
record can only remove permissions from this whitelist.
3. one for cases where the installer of the package whitelists a permission. This list
corresponds to the FLAG_PERMISSION_WHITELIST_INSTALLER
public boolean addWhitelistedRestrictedPermission (String (https://developer.android.com
               String (https://developer.android.com/reference/java/lang/String) permName, 
               int whitelistFlags)


 (https://developer.android.com/reference/android/content/pm/PackageManager#FLAG_PERMISSIO
N_WHITELIST_INSTALLER)
flag. Can be modified by pre-installed holders of a dedicated permission or the installer
on record.
You need to specify the whitelists for which to set the whitelisted permissions which will clear
the previous whitelisted permissions and replace them with the provided ones.
Note: In retrospect it would have been preferred to use more inclusive terminology when
naming this API. Similar APIs added will refrain from using the term "whitelist".
Parameters
packageName
String: The app for which to get whitelisted permissions.
This value cannot be null.
permName
String: The whitelisted permission to add.
This value cannot be null.
whitelistFlags
int: The whitelists to which to add. Passing multiple flags updates all spe
Value is either 0 or a combination of the following:
FLAG_PERMISSION_WHITELIST_SYSTEM
 (https://developer.android.com/reference/android/content/pm/Packag
FLAG_PERMISSION_WHITELIST_INSTALLER
 (https://developer.android.com/reference/android/content/pm/Packag
FLAG_PERMISSION_WHITELIST_UPGRADE
 (https://developer.android.com/reference/android/content/pm/Packag
Returns
boolean
Whether the permission was added to the whitelist.


Added in API level 33 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Throws
SecurityException
(https://developer.android.com/reference/java/lang/SecurityException)
if you try to modify a whitelist that
you have no access to.
See also:
getWhitelistedRestrictedPermissions(String,int)
(https://developer.android.com/reference/android/content/pm/PackageManager#getWhitelistedRestricted
Permissions(java.lang.String,%20int))
removeWhitelistedRestrictedPermission(String,String,int)
(https://developer.android.com/reference/android/content/pm/PackageManager#removeWhitelistedRestri
ctedPermission(java.lang.String,%20java.lang.String,%20int))
FLAG_PERMISSION_WHITELIST_SYSTEM
(https://developer.android.com/reference/android/content/pm/PackageManager#FLAG_PERMISSION_WHI
TELIST_SYSTEM)
FLAG_PERMISSION_WHITELIST_UPGRADE
(https://developer.android.com/reference/android/content/pm/PackageManager#FLAG_PERMISSION_WHI
TELIST_UPGRADE)
FLAG_PERMISSION_WHITELIST_INSTALLER
(https://developer.android.com/reference/android/content/pm/PackageManager#FLAG_PERMISSION_WHI
TELIST_INSTALLER)
canPackageQuery
Returns true if the source package is able to query for details about the target package.
Applications that share details about other applications should use this API to determine if
those details should be withheld from callers that do not otherwise have visibility of them.
public boolean canPackageQuery (String (https://developer.android.com/reference/java/lang/Strin
               String (https://developer.android.com/reference/java/lang/String) targetPackage


Note: The caller must be able to query for details about the source and target package. A
NameNotFoundException
(https://developer.android.com/reference/android/content/pm/PackageManager.NameNotFoundException
)
is thrown if it isn't.
Parameters
sourcePackageName
String: The source package that would receive details about the target
package.
This value cannot be null.
targetPackageName
String: The target package whose details would be shared with the
source package.
This value cannot be null.
Returns
boolean
true if the source package is able to query for details about the target
package.
Throws
PackageManager.NameNotFoundException
(https://developer.android.com/reference/android/content/pm/PackageManager.NameNotFoundException)


Added in API level 34 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
canPackageQuery
Same as canPackageQuery(String,String)
(https://developer.android.com/reference/android/content/pm/PackageManager#canPackageQuery(java.la
ng.String,%20java.lang.String))
but accepts an array of target packages to be queried.
Parameters
sourcePackageName
String: The source package that would receive details about the target
package.
This value cannot be null.
targetPackageNames
String: An array of target packages whose details would be shared with
the source package.
This value cannot be null.
Returns
boolean[]
An array of booleans where each member specifies whether the source
package is able to query for details about the target package given by the
corresponding value at the same index in the array of target packages.
This value cannot be null.
Throws
public boolean[] canPackageQuery (String (https://developer.android.com/reference/java/lang/S
               String[] (https://developer.android.com/reference/java/lang/String) targetPacka


Added in API level 26 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
PackageManager.NameNotFoundException
(https://developer.android.com/reference/android/content/pm/PackageManager.NameNotFoundException)
canRequestPackageInstalls
Checks whether the calling package is allowed to request package installs through package
installer. Apps are encouraged to call this API before launching the package installer via intent
Intent.ACTION_INSTALL_PACKAGE
(https://developer.android.com/reference/android/content/Intent#ACTION_INSTALL_PACKAGE). Starting
from Android O, the user can explicitly choose what external sources they trust to install apps
on the device. If this API returns false, the install request will be blocked by the package
installer and a dialog will be shown to the user with an option to launch settings to change their
preference. An application must target Android O or higher and declare permission
Manifest.permission.REQUEST_INSTALL_PACKAGES
(https://developer.android.com/reference/android/Manifest.permission#REQUEST_INSTALL_PACKAGES)
in order to use this API.
Returns
boolean
true if the calling package is trusted by the user to request install
packages on the device, false otherwise.
See also:
Intent.ACTION_INSTALL_PACKAGE
(https://developer.android.com/reference/android/content/Intent#ACTION_INSTALL_PACKAGE)
public abstract boolean canRequestPackageInstalls ()


Added in API level 8 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Added in API level 1 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Settings.ACTION_MANAGE_UNKNOWN_APP_SOURCES
(https://developer.android.com/reference/android/provider/Settings#ACTION_MANAGE_UNKNOWN_APP_S
OURCES)
canonicalToCurrentPackageNames
Map from a packages canonical name to the current name in use on the device.
Parameters
packageNames
String: Array of new names to be mapped.
This value cannot be null.
Returns
String[]
(https://developer.android.com/reference/java/lang/String)
Returns an array of the same size as the original,
containing the current name for each package.
checkPermission
public abstract String[] (https://developer.android.com/reference/java/lang/String) canonicalTo
public abstract int checkPermission (String (https://developer.android.com/reference/java/lan
               String (https://developer.android.com/reference/java/lang/String) packageName)


Check whether a particular package has been granted a particular permission.
Note: This API returns the underlying permission state as-is and is mostly intended for
permission managing system apps. To perform an access check for a certain app, please use
the Context.checkPermission
(https://developer.android.com/reference/android/content/Context#checkPermission(java.lang.String,%20i
nt,%20int))
APIs instead.
Parameters
permName
String: The name of the permission you are checking for.
This value cannot be null.
packageName
String: The name of the package you are checking against.
This value cannot be null.
Returns
int
If the package has the permission, PERMISSION_GRANTED is returned. If i
PERMISSION_DENIED is returned.
Value is one of the following:
PERMISSION_GRANTED
 (https://developer.android.com/reference/android/content/pm/Packag
PERMISSION_DENIED
 (https://developer.android.com/reference/android/content/pm/Packag
See also:
PERMISSION_GRANTED
(https://developer.android.com/reference/android/content/pm/PackageManager#PERMISSION_GRANTED)


Added in API level 1 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
PERMISSION_DENIED
(https://developer.android.com/reference/android/content/pm/PackageManager#PERMISSION_DENIED)
checkSignatures
Compare the signatures of two packages to determine if the same signature appears in both of
them. If they do contain the same signature, then they are allowed special privileges when
working with each other: they can share the same user-id, run instrumentation against each
other, etc.
Parameters
packageName1
String: First package name whose signature will be compared.
This value cannot be null.
packageName2
String: Second package name whose signature will be compared.
This value cannot be null.
Returns
int
Returns an integer indicating whether all signatures on the two packages m
 (https://developer.android.com/reference/android/content/pm/PackageM
match or < 0 if there is not a match (SIGNATURE_NO_MATCH
 (https://developer.android.com/reference/android/content/pm/PackageM
SIGNATURE_UNKNOWN_PACKAGE
 (https://developer.android.com/reference/android/content/pm/PackageM
Value is one of the following:
public abstract int checkSignatures (String (https://developer.android.com/reference/java/lan
               String (https://developer.android.com/reference/java/lang/String) packageName2)


Added in API level 5 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
SIGNATURE_MATCH
 (https://developer.android.com/reference/android/content/pm/Packag
SIGNATURE_NEITHER_SIGNED
 (https://developer.android.com/reference/android/content/pm/Packag
SIGNATURE_FIRST_NOT_SIGNED
 (https://developer.android.com/reference/android/content/pm/Packag
SIGNATURE_SECOND_NOT_SIGNED
 (https://developer.android.com/reference/android/content/pm/Packag
SIGNATURE_NO_MATCH
 (https://developer.android.com/reference/android/content/pm/Packag
SIGNATURE_UNKNOWN_PACKAGE
 (https://developer.android.com/reference/android/content/pm/Packag
See also:
checkSignatures(int, int)
(https://developer.android.com/reference/android/content/pm/PackageManager#checkSignatures(int,%20i
nt))
checkSignatures
Like checkSignatures(String,String)
(https://developer.android.com/reference/android/content/pm/PackageManager#checkSignatures(java.lan
g.String,%20java.lang.String))
, but takes UIDs of the two packages to be checked. This can be useful, for example, when
doing the check in an IPC, where the UID is the only identity available. It is functionally identical
to determining the package associated with the UIDs and checking their signatures.
public abstract int checkSignatures (int uid1, 
               int uid2)


Parameters
uid1
int: First UID whose signature will be compared.
uid2
int: Second UID whose signature will be compared.
Returns
int
Returns an integer indicating whether all signatures on the two packages m
 (https://developer.android.com/reference/android/content/pm/PackageM
match or < 0 if there is not a match (SIGNATURE_NO_MATCH
 (https://developer.android.com/reference/android/content/pm/PackageM
SIGNATURE_UNKNOWN_PACKAGE
 (https://developer.android.com/reference/android/content/pm/PackageM
Value is one of the following:
SIGNATURE_MATCH
 (https://developer.android.com/reference/android/content/pm/Packag
SIGNATURE_NEITHER_SIGNED
 (https://developer.android.com/reference/android/content/pm/Packag
SIGNATURE_FIRST_NOT_SIGNED
 (https://developer.android.com/reference/android/content/pm/Packag
SIGNATURE_SECOND_NOT_SIGNED
 (https://developer.android.com/reference/android/content/pm/Packag
SIGNATURE_NO_MATCH
 (https://developer.android.com/reference/android/content/pm/Packag
SIGNATURE_UNKNOWN_PACKAGE
 (https://developer.android.com/reference/android/content/pm/Packag
See also:


Added in API level 26 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Added in API level 1 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Deprecated in API level 29
(https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
checkSignatures(String,String)
(https://developer.android.com/reference/android/content/pm/PackageManager#checkSignatures(java.lan
g.String,%20java.lang.String))
clearInstantAppCookie
Clears the instant application cookie for the calling app.
See also:
isInstantApp()
(https://developer.android.com/reference/android/content/pm/PackageManager#isInstantApp())
isInstantApp(String)
(https://developer.android.com/reference/android/content/pm/PackageManager#isInstantApp(java.lang.St
ring))
getInstantAppCookieMaxBytes()
(https://developer.android.com/reference/android/content/pm/PackageManager#getInstantAppCookieMax
Bytes())
getInstantAppCookie()
(https://developer.android.com/reference/android/content/pm/PackageManager#getInstantAppCookie())
clearInstantAppCookie()
(https://developer.android.com/reference/android/content/pm/PackageManager#clearInstantAppCookie())
clearPackagePreferredActivities
public abstract void clearInstantAppCookie ()
public abstract void clearPackagePreferredActivities (String (https://developer.android.


or
Added in API level 8 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
This method was deprecated in API level 29.
This function no longer does anything. It is the platform's responsibility to assign preferred activities and this
cannot be modified directly. To determine the activities resolved by the platform, use
resolveActivity(Intent, ResolveInfoFlags)
(https://developer.android.com/reference/android/content/pm/PackageManager#resolveActivity(android.c
ontent.Intent,%20android.content.pm.PackageManager.ResolveInfoFlags))
or queryIntentActivities(Intent, ResolveInfoFlags)
(https://developer.android.com/reference/android/content/pm/PackageManager#queryIntentActivities(and
roid.content.Intent,%20android.content.pm.PackageManager.ResolveInfoFlags))
. To configure an app to be responsible for a particular role and to check current role holders, see
RoleManager (https://developer.android.com/reference/android/app/role/RoleManager).
Remove all preferred activity mappings, previously added with
addPreferredActivity(IntentFilter, int, ComponentName, ComponentName)
(https://developer.android.com/reference/android/content/pm/PackageManager#addPreferredActivity(and
roid.content.IntentFilter,%20int,%20android.content.ComponentName[],%20android.content.ComponentNam
e))
, from the system whose activities are implemented in the given package name. An application
can only clear its own package(s).
Parameters
packageName
String: The name of the package whose preferred activity mappings are
to be removed.
This value cannot be null.
currentToCanonicalPackageNames
public abstract String[] (https://developer.android.com/reference/java/lang/String) currentToCa


Added in API level 17 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Map from the current package names in use on the device to whatever the current canonical
name of that package is.
Parameters
packageNames
String: Array of current names to be mapped.
This value cannot be null.
Returns
String[]
(https://developer.android.com/reference/java/lang/String)
Returns an array of the same size as the original,
containing the canonical name for each
package.
extendVerificationTimeout
Allows a package listening to the package verification broadcast
(https://developer.android.com/reference/android/content/Intent#ACTION_PACKAGE_NEEDS_VERIFICATIO
N)
to extend the default timeout for a response and declare what action to perform after the
timeout occurs. The response must include the verificationCodeAtTimeout which is one of
PackageManager.VERIFICATION_ALLOW
(https://developer.android.com/reference/android/content/pm/PackageManager#VERIFICATION_ALLOW)
or PackageManager.VERIFICATION_REJECT
(https://developer.android.com/reference/android/content/pm/PackageManager#VERIFICATION_REJECT).
This method can be called multiple times, but the total amount of time extension time will be
public abstract void extendVerificationTimeout (int id, 
               int verificationCodeAtTimeout, 
               long millisecondsToDelay)


limited to PackageManager.MAXIMUM_VERIFICATION_TIMEOUT
(https://developer.android.com/reference/android/content/pm/PackageManager#MAXIMUM_VERIFICATIO
N_TIMEOUT)
. If the method is called multiple times with different verificationCodeAtTimeout, then
previous verificationCodeAtTimeout will be ignored and only the latest one will take effect.
If this method is called after calling PackageManager.verifyPendingInstall
(https://developer.android.com/reference/android/content/pm/PackageManager#verifyPendingInstall(int,%
20int))
, it may nullify the result set by verifyPendingInstall.
Parameters
id
int: pending package identifier as passed via the PackageManager.EXT
 (https://developer.android.com/reference/android/content/pm/PackageM
extra.
verificationCodeAtTimeout int: either PackageManager.VERIFICATION_ALLOW
 (https://developer.android.com/reference/android/content/pm/PackageM
Manager.VERIFICATION_REJECT
 (https://developer.android.com/reference/android/content/pm/PackageM
verificationCodeAtTimeout is neither PackageManager.VERIFIC
 (https://developer.android.com/reference/android/content/pm/PackageM
Manager.VERIFICATION_REJECT
 (https://developer.android.com/reference/android/content/pm/PackageM
verificationCodeAtTimeout will default to PackageManager.VERI
 (https://developer.android.com/reference/android/content/pm/PackageM
millisecondsToDelay
long: the amount of time requested for the timeout. Must be positive and 
VERIFICATION_TIMEOUT
 (https://developer.android.com/reference/android/content/pm/PackageM
. If millisecondsToDelay is out of bounds, millisecondsToDelay w
namely, 0 or PackageManager.MAXIMUM_VERIFICATION_TIMEOUT
 (https://developer.android.com/reference/android/content/pm/PackageM
.


Added in API level 20 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Throws
SecurityException
(https://developer.android.com/reference/java/lang/SecurityException)
if the caller does not have the
PACKAGE_VERIFICATION_AGENT
permission.
getActivityBanner
Retrieve the banner associated with an activity. Given the full name of an activity, retrieves the
information about it and calls ComponentInfo.loadIcon()
(https://developer.android.com/reference/android/content/pm/PackageItemInfo#loadIcon(android.content.
pm.PackageManager))
to return its banner. If the activity cannot be found, NameNotFoundException is thrown.
Parameters
activityName
ComponentName: Name of the activity whose banner is to be retrieved.
This value cannot be null.
Returns
Drawable
(https://developer.android.com/reference/android/graphics/drawable/Drawable)
Returns the image of the ba
or null if the activity has no 
specified.
public abstract Drawable (https://developer.android.com/reference/android/graphics/drawable/Draw


Added in API level 20 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Throws
PackageManager.NameNotFoundException
(https://developer.android.com/reference/android/content/pm/PackageManager.NameNotFoundException)
See also:
getActivityBanner(Intent)
(https://developer.android.com/reference/android/content/pm/PackageManager#getActivityBanner(androi
d.content.Intent))
getActivityBanner
Retrieve the banner associated with an Intent. If intent.getClassName() is set, this simply
returns the result of getActivityBanner(intent.getClassName()). Otherwise it resolves the
intent's component and returns the banner associated with the resolved component. If
intent.getClassName() cannot be found or the Intent cannot be resolved to a component,
NameNotFoundException is thrown.
Parameters
intent
Intent: The intent for which you would like to retrieve a banner.
This value cannot be null.
Returns
public abstract Drawable (https://developer.android.com/reference/android/graphics/drawable/Draw


Added in API level 1 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Drawable
(https://developer.android.com/reference/android/graphics/drawable/Drawable)
Returns the image of the ba
or null if the activity has no 
specified.
Throws
PackageManager.NameNotFoundException
(https://developer.android.com/reference/android/content/pm/PackageManager.NameNotFoundException)
See also:
getActivityBanner(ComponentName)
(https://developer.android.com/reference/android/content/pm/PackageManager#getActivityBanner(androi
d.content.ComponentName))
getActivityIcon
Retrieve the icon associated with an Intent. If intent.getClassName() is set, this simply returns
the result of getActivityIcon(intent.getClassName()). Otherwise it resolves the intent's
component and returns the icon associated with the resolved component. If
intent.getClassName() cannot be found or the Intent cannot be resolved to a component,
NameNotFoundException is thrown.
Parameters
public abstract Drawable (https://developer.android.com/reference/android/graphics/drawable/Draw


Added in API level 1 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
intent
Intent: The intent for which you would like to retrieve an icon.
This value cannot be null.
Returns
Drawable
(https://developer.android.com/reference/android/graphics/drawable/Drawable)
Returns the image of the ico
the default activity icon if it 
not be found. Does not retu
Throws
PackageManager.NameNotFoundException
(https://developer.android.com/reference/android/content/pm/PackageManager.NameNotFoundException)
See also:
getActivityIcon(ComponentName)
(https://developer.android.com/reference/android/content/pm/PackageManager#getActivityIcon(android.c
ontent.ComponentName))
getActivityIcon
Retrieve the icon associated with an activity. Given the full name of an activity, retrieves the
information about it and calls ComponentInfo.loadIcon()
public abstract Drawable (https://developer.android.com/reference/android/graphics/drawable/Draw


Added in API level 1 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
(https://developer.android.com/reference/android/content/pm/PackageItemInfo#loadIcon(android.content.
pm.PackageManager))
to return its icon. If the activity cannot be found, NameNotFoundException is thrown.
Parameters
activityName
ComponentName: Name of the activity whose icon is to be retrieved.
This value cannot be null.
Returns
Drawable
(https://developer.android.com/reference/android/graphics/drawable/Drawable)
Returns the image of the ico
the default activity icon if it 
not be found. Does not retu
Throws
PackageManager.NameNotFoundException
(https://developer.android.com/reference/android/content/pm/PackageManager.NameNotFoundException)
See also:
getActivityIcon(Intent)
(https://developer.android.com/reference/android/content/pm/PackageManager#getActivityIcon(android.c
ontent.Intent))
getActivityInfo


Retrieve all of the information we know about a particular activity class. Use
getActivityInfo(ComponentName,ComponentInfoFlags)
(https://developer.android.com/reference/android/content/pm/PackageManager#getActivityInfo(android.c
ontent.ComponentName,%20android.content.pm.PackageManager.ComponentInfoFlags))
when long flags are needed.
Parameters
component
ComponentName: The full component name (i.e.
com.google.apps.contacts/com.google.apps.contacts. ContactsList) of
an Activity class.
This value cannot be null.
flags
int: Additional option flags to modify the data returned.
Returns
ActivityInfo
(https://developer.android.com/reference/android/content/pm/ActivityInfo)
An ActivityInfo
 (https://developer.android.com/
containing information about the
This value cannot be null.
Throws
public abstract ActivityInfo (https://developer.android.com/reference/android/content/pm/Activit
               int flags)


Added in API level 33 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
PackageManager.NameNotFoundException
(https://developer.android.com/reference/android/content/pm/PackageManager.NameNotFoundException)
getActivityInfo
See getActivityInfo(ComponentName,int)
(https://developer.android.com/reference/android/content/pm/PackageManager#getActivityInfo(android.c
ontent.ComponentName,%20int))
.
Parameters
component
ComponentName: This value cannot be null.
flags
PackageManager.ComponentInfoFlags: This value cannot be null.
Returns
ActivityInfo
(https://developer.android.com/reference/android/content/pm/ActivityInfo)
This value cannot be null.
Throws
public ActivityInfo (https://developer.android.com/reference/android/content/pm/ActivityInfo) getA
               PackageManager.ComponentInfoFlags (https://developer.android.com/reference/


Added in API level 9 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
PackageManager.NameNotFoundException
(https://developer.android.com/reference/android/content/pm/PackageManager.NameNotFoundException)
getActivityLogo
Retrieve the logo associated with an Intent. If intent.getClassName() is set, this simply returns
the result of getActivityLogo(intent.getClassName()). Otherwise it resolves the intent's
component and returns the logo associated with the resolved component. If
intent.getClassName() cannot be found or the Intent cannot be resolved to a component,
NameNotFoundException is thrown.
Parameters
intent
Intent: The intent for which you would like to retrieve a logo.
This value cannot be null.
Returns
Drawable
(https://developer.android.com/reference/android/graphics/drawable/Drawable)
Returns the image of the log
null if the activity has no log
specified.
Throws
public abstract Drawable (https://developer.android.com/reference/android/graphics/drawable/Draw


Added in API level 9 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
PackageManager.NameNotFoundException
(https://developer.android.com/reference/android/content/pm/PackageManager.NameNotFoundException)
See also:
getActivityLogo(ComponentName)
(https://developer.android.com/reference/android/content/pm/PackageManager#getActivityLogo(android.
content.ComponentName))
getActivityLogo
Retrieve the logo associated with an activity. Given the full name of an activity, retrieves the
information about it and calls ComponentInfo.loadLogo()
(https://developer.android.com/reference/android/content/pm/PackageItemInfo#loadLogo(android.content
.pm.PackageManager))
to return its logo. If the activity cannot be found, NameNotFoundException is thrown.
Parameters
activityName
ComponentName: Name of the activity whose logo is to be retrieved.
This value cannot be null.
Returns
public abstract Drawable (https://developer.android.com/reference/android/graphics/drawable/Draw


Added in API level 1 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Drawable
(https://developer.android.com/reference/android/graphics/drawable/Drawable)
Returns the image of the log
null if the activity has no log
specified.
Throws
PackageManager.NameNotFoundException
(https://developer.android.com/reference/android/content/pm/PackageManager.NameNotFoundException)
See also:
getActivityLogo(Intent)
(https://developer.android.com/reference/android/content/pm/PackageManager#getActivityLogo(android.
content.Intent))
getAllPermissionGroups
Retrieve all of the known permission groups in the system.
Parameters
flags
int: Additional option flags to modify the data returned.
Value is either 0 or
GET_META_DATA
 (https://developer.android.com/reference/android/content/pm/Packag
public abstract List (https://developer.android.com/reference/java/util/List)<PermissionGroupInf


Added in API level 37 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Added in API level 20 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Returns
List (https://developer.android.com/reference/java/util/List)<PermissionGroup
Info
(https://developer.android.com/reference/android/content/pm/PermissionGroupInfo)
>
Returns a list of Permi
 (https://developer.and
containing information
This value cannot be n
getAppUidForPrivateComputeCoreUid
Maps a Private Compute Core (PCC) UID to its corresponding application UID.
Parameters
pccUid
int: The PCC UID to map.
Returns
int
The corresponding application UID, or ERROR(Process.INVALID_UID/
java.lang.Process#INVALID_UID Process.INVALID_UID)
 (https://developer.android.com/) if the provided UID is not a valid PCC
UID or no mapping exists.
getApplicationBanner
public int getAppUidForPrivateComputeCoreUid (int pccUid)


Retrieve the banner associated with an application. Given the name of the application's
package, retrieves the information about it and calls getApplicationIcon() to return its banner. If
the application cannot be found, NameNotFoundException is thrown.
Parameters
packageName
String: Name of the package whose application banner is to be
retrieved.
This value cannot be null.
Returns
Drawable
(https://developer.android.com/reference/android/graphics/drawable/Drawable)
Returns the image of the ba
or null if the application has
banner specified.
Throws
PackageManager.NameNotFoundException
(https://developer.android.com/reference/android/content/pm/PackageManager.NameNotFoundException)
See also:
getApplicationBanner(ApplicationInfo)
(https://developer.android.com/reference/android/content/pm/PackageManager#getApplicationBanner(an
droid.content.pm.ApplicationInfo))
public abstract Drawable (https://developer.android.com/reference/android/graphics/drawable/Draw


Added in API level 20 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Added in API level 1 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
getApplicationBanner
Retrieve the banner associated with an application.
Parameters
info
ApplicationInfo: Information about application being queried.
This value cannot be null.
Returns
Drawable
(https://developer.android.com/reference/android/graphics/drawable/Drawable)
Returns the image of the ba
or null if the application has
banner specified.
See also:
getApplicationBanner(String)
(https://developer.android.com/reference/android/content/pm/PackageManager#getApplicationBanner(jav
a.lang.String))
getApplicationEnabledSetting
public abstract Drawable (https://developer.android.com/reference/android/graphics/drawable/Draw
public abstract int getApplicationEnabledSetting (String (https://developer.android.com/


Return the enabled setting for an application. This returns the last value set by
setApplicationEnabledSetting(String,int,int)
(https://developer.android.com/reference/android/content/pm/PackageManager#setApplicationEnabledSe
tting(java.lang.String,%20int,%20int))
; in most cases this value will be COMPONENT_ENABLED_STATE_DEFAULT
(https://developer.android.com/reference/android/content/pm/PackageManager#COMPONENT_ENABLED
_STATE_DEFAULT)
since the value originally specified in the manifest has not been modified.
Parameters
packageName
String: The package name of the application to retrieve.
This value cannot be null.
Returns
int
Returns the current enabled state for the application.
Value is one of the following:
COMPONENT_ENABLED_STATE_DEFAULT
 (https://developer.android.com/reference/android/content/pm/Packag
COMPONENT_ENABLED_STATE_ENABLED
 (https://developer.android.com/reference/android/content/pm/Packag
COMPONENT_ENABLED_STATE_DISABLED
 (https://developer.android.com/reference/android/content/pm/Packag
COMPONENT_ENABLED_STATE_DISABLED_USER
 (https://developer.android.com/reference/android/content/pm/Packag
COMPONENT_ENABLED_STATE_DISABLED_UNTIL_USED
 (https://developer.android.com/reference/android/content/pm/Packag
Throws


Added in API level 1 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
IllegalArgumentException
(https://developer.android.com/reference/java/lang/IllegalArgumentException)
if the named package does n
exist.
getApplicationIcon
Retrieve the icon associated with an application. If it has not defined an icon, the default app
icon is returned. Does not return null.
Parameters
info
ApplicationInfo: Information about application being queried.
This value cannot be null.
Returns
Drawable
(https://developer.android.com/reference/android/graphics/drawable/Drawable)
Returns the image of the ico
the default application icon
could not be found.
See also:
getApplicationIcon(String)
(https://developer.android.com/reference/android/content/pm/PackageManager#getApplicationIcon(java.l
ang.String))
public abstract Drawable (https://developer.android.com/reference/android/graphics/drawable/Draw


Added in API level 1 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
getApplicationIcon
Retrieve the icon associated with an application. Given the name of the application's package,
retrieves the information about it and calls getApplicationIcon() to return its icon. If the
application cannot be found, NameNotFoundException is thrown.
Parameters
packageName
String: Name of the package whose application icon is to be retrieved.
This value cannot be null.
Returns
Drawable
(https://developer.android.com/reference/android/graphics/drawable/Drawable)
Returns the image of the ico
the default application icon
could not be found. Does no
return null.
Throws
PackageManager.NameNotFoundException
(https://developer.android.com/reference/android/content/pm/PackageManager.NameNotFoundException)
See also:
public abstract Drawable (https://developer.android.com/reference/android/graphics/drawable/Draw


Added in API level 33 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
getApplicationIcon(ApplicationInfo)
(https://developer.android.com/reference/android/content/pm/PackageManager#getApplicationIcon(andro
id.content.pm.ApplicationInfo))
getApplicationInfo
See getApplicationInfo(String,int)
(https://developer.android.com/reference/android/content/pm/PackageManager#getApplicationInfo(java.l
ang.String,%20int))
.
Parameters
packageName
String: This value cannot be null.
flags
PackageManager.ApplicationInfoFlags: This value cannot be
null.
Returns
ApplicationInfo
(https://developer.android.com/reference/android/content/pm/ApplicationInfo)
This value cannot be null.
Throws
public ApplicationInfo (https://developer.android.com/reference/android/content/pm/ApplicationInfo
               PackageManager.ApplicationInfoFlags (https://developer.android.com/referen


Added in API level 1 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
PackageManager.NameNotFoundException
(https://developer.android.com/reference/android/content/pm/PackageManager.NameNotFoundException)
getApplicationInfo
Retrieve all of the information we know about a particular package/application. Use
getApplicationInfo(String,ApplicationInfoFlags)
(https://developer.android.com/reference/android/content/pm/PackageManager#getApplicationInfo(java.l
ang.String,%20android.content.pm.PackageManager.ApplicationInfoFlags))
when long flags are needed.
Parameters
packageName
String: The full name (i.e. com.google.apps.contacts) of an application.
This value cannot be null.
flags
int: Additional option flags to modify the data returned.
Returns
ApplicationInfo
(https://developer.android.com/reference/android/content/pm/ApplicationInfo)
An ApplicationInfo
 (https://developer.android.c
containing information abou
PACKAGES is set and if the p
applications, the application 
public abstract ApplicationInfo (https://developer.android.com/reference/android/content/pm/Ap
               int flags)


Added in API level 1 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
applications (which includes
data directory i.e. application
DATA flag set).
This value cannot be null.
Throws
PackageManager.NameNotFoundException
(https://developer.android.com/reference/android/content/pm/PackageManager.NameNotFoundException)
getApplicationLabel
Return the label to use for this application.
Parameters
info
ApplicationInfo: The ApplicationInfo
 (https://developer.android.com/reference/android/content/pm/Applicatio
of the application to get the label of.
This value cannot be null.
Returns
public abstract CharSequence (https://developer.android.com/reference/java/lang/CharSequence) g


Added in API level 9 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
CharSequence
(https://developer.android.com/reference/java/lang/CharSequence)
Returns a CharSequence
 (https://developer.android.com/referenc
containing the label associated with this
item does not have a label.
This value cannot be null.
getApplicationLogo
Retrieve the logo associated with an application. Given the name of the application's package,
retrieves the information about it and calls getApplicationLogo() to return its logo. If the
application cannot be found, NameNotFoundException is thrown.
Parameters
packageName
String: Name of the package whose application logo is to be retrieved.
This value cannot be null.
Returns
Drawable
(https://developer.android.com/reference/android/graphics/drawable/Drawable)
Returns the image of the log
null if no application logo ha
been specified.
public abstract Drawable (https://developer.android.com/reference/android/graphics/drawable/Draw


Added in API level 9 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Throws
PackageManager.NameNotFoundException
(https://developer.android.com/reference/android/content/pm/PackageManager.NameNotFoundException)
See also:
getApplicationLogo(ApplicationInfo)
(https://developer.android.com/reference/android/content/pm/PackageManager#getApplicationLogo(andr
oid.content.pm.ApplicationInfo))
getApplicationLogo
Retrieve the logo associated with an application. If it has not specified a logo, this method
returns null.
Parameters
info
ApplicationInfo: Information about application being queried.
This value cannot be null.
Returns
Drawable
(https://developer.android.com/reference/android/graphics/drawable/Drawable)
Returns the image of the log
null if no logo is specified b
public abstract Drawable (https://developer.android.com/reference/android/graphics/drawable/Draw


Added in API level 35 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
application.
See also:
getApplicationLogo(String)
(https://developer.android.com/reference/android/content/pm/PackageManager#getApplicationLogo(java.l
ang.String))
getArchivedPackage
Return archived package info for the package or null if the package is not installed.
Parameters
packageName
String: This value cannot be null.
Returns
ArchivedPackageInfo
(https://developer.android.com/reference/android/content/pm/ArchivedPackageInfo)
See also:
public ArchivedPackageInfo (https://developer.android.com/reference/android/content/pm/ArchivedP


Added in API level 30 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Added in API level 26 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
PackageInstaller.installPackageArchived
(https://developer.android.com/reference/android/content/pm/PackageInstaller#installPackageArchived(a
ndroid.content.pm.ArchivedPackageInfo,%20android.content.pm.PackageInstaller.SessionParams,%20andro
id.content.IntentSender))
getBackgroundPermissionOptionLabel
Gets the localized label that corresponds to the option in settings for granting background
access.
The intended use is for apps to reference this label in its instruction for users to grant a
background permission.
Returns
CharSequence
(https://developer.android.com/reference/java/lang/CharSequence)
the localized label that corresponds to
the settings option for granting
background access.
This value cannot be null.
getChangedPackages
public CharSequence (https://developer.android.com/reference/java/lang/CharSequence) getBackgro
public abstract ChangedPackages (https://developer.android.com/reference/android/content/pm/Ch


Added in API level 1 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Returns the names of the packages that have been changed [eg. added, removed or updated]
since the given sequence number.
If no packages have been changed, returns null.
The sequence number starts at 0 and is reset every boot.
Parameters
sequenceNumber
int: The first sequence number for which to retrieve package changes.
Value is 0 or greater
Returns
ChangedPackages
(https://developer.android.com/reference/android/content/pm/ChangedPackages)
See also:
Settings.Global.BOOT_COUNT
(https://developer.android.com/reference/android/provider/Settings.Global#BOOT_COUNT)
getComponentEnabledSetting
Return the enabled setting for a package component (activity, receiver, service, provider). This
returns the last value set by setComponentEnabledSetting(ComponentName,int,int)
public abstract int getComponentEnabledSetting (ComponentName (https://developer.android


Added in API level 1 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
(https://developer.android.com/reference/android/content/pm/PackageManager#setComponentEnabledSe
tting(android.content.ComponentName,%20int,%20int))
; in most cases this value will be COMPONENT_ENABLED_STATE_DEFAULT
(https://developer.android.com/reference/android/content/pm/PackageManager#COMPONENT_ENABLED
_STATE_DEFAULT)
since the value originally specified in the manifest has not been modified.
Parameters
componentName
ComponentName: The component to retrieve.
This value cannot be null.
Returns
int
Returns the current enabled state for the component.
Value is one of the following:
COMPONENT_ENABLED_STATE_DEFAULT
 (https://developer.android.com/reference/android/content/pm/Packag
COMPONENT_ENABLED_STATE_ENABLED
 (https://developer.android.com/reference/android/content/pm/Packag
COMPONENT_ENABLED_STATE_DISABLED
 (https://developer.android.com/reference/android/content/pm/Packag
COMPONENT_ENABLED_STATE_DISABLED_USER
 (https://developer.android.com/reference/android/content/pm/Packag
COMPONENT_ENABLED_STATE_DISABLED_UNTIL_USED
 (https://developer.android.com/reference/android/content/pm/Packag
getDefaultActivityIcon


Added in API level 1 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Return the generic icon for an activity that is used when no specific icon is defined.
Returns
Drawable
(https://developer.android.com/reference/android/graphics/drawable/Drawable)
Drawable Image of the icon
This value cannot be null.
getDrawable
Retrieve an image from a package. This is a low-level API used by the various package
manager info structures (such as ComponentInfo
(https://developer.android.com/reference/android/content/pm/ComponentInfo) to implement retrieval
of their associated icon.
Parameters
packageName
String: The name of the package that this icon is coming from. Cannot
be null.
public abstract Drawable (https://developer.android.com/reference/android/graphics/drawable/Draw
public abstract Drawable (https://developer.android.com/reference/android/graphics/drawable/Draw
               int resid, 
               ApplicationInfo (https://developer.android.com/reference/android/content/pm/Ap


Added in API level 31 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
resid
int: The resource identifier of the desired image. Cannot be 0.
appInfo
ApplicationInfo: Overall information about packageName. This may
be null, in which case the application information will be retrieved for you
if needed; if you already have this information around, it can be much
more efficient to supply it here.
Returns
Drawable
(https://developer.android.com/reference/android/graphics/drawable/Drawable)
Returns a Drawable holding
requested image. Returns n
an image could not be foun
any reason.
getGroupOfPlatformPermission
Get the platform-defined permission group of a particular permission, if the permission is a
platform-defined permission.
Parameters
permissionName
String: the permission whose group is desired.
This value cannot be null.
public void getGroupOfPlatformPermission (String (https://developer.android.com/reference/j
               Executor (https://developer.android.com/reference/java/util/concurrent/Executor) e
               Consumer (https://developer.android.com/reference/java/util/function/Consumer)<St


Added in API level 30 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
executor
Executor: the Executor
 (https://developer.android.com/reference/java/util/concurrent/Executor) 
invoke the callback.
This value cannot be null.
Callback and listener events are dispatched through this Executor
 (https://developer.android.com/reference/java/util/concurrent/Executor), 
easy way to control which thread is used. To dispatch events through the m
your application, you can use Context.getMainExecutor()
 (https://developer.android.com/reference/android/content/Context#getM
. Otherwise, provide an Executor
 (https://developer.android.com/reference/java/util/concurrent/Executor) t
dispatches to an appropriate thread.
callback
Consumer: the callback which will receive the name of the permission gro
permission belongs to, or null if it has no group, is not a platform-defined
or there was an exception
getInstallSourceInfo
Retrieves information about how a package was installed or updated.
If the calling application does not hold the INSTALL_PACKAGES permission then the result will
always return null from InstallSourceInfo.getOriginatingPackageName()
(https://developer.android.com/reference/android/content/pm/InstallSourceInfo#getOriginatingPackageNa
me())
.
If the package that requested the install has been uninstalled, then information about it will
only be returned from InstallSourceInfo.getInitiatingPackageName()
(https://developer.android.com/reference/android/content/pm/InstallSourceInfo#getInitiatingPackageNam
e())
public InstallSourceInfo (https://developer.android.com/reference/android/content/pm/InstallSourc


Added in API level 1 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
and InstallSourceInfo.getInitiatingPackageSigningInfo()
(https://developer.android.com/reference/android/content/pm/InstallSourceInfo#getInitiatingPackageSigni
ngInfo())
if the calling package is requesting its own install information and is not an instant app.
Parameters
packageName
String: The name of the package to query.
This value cannot be null.
Returns
InstallSourceInfo
(https://developer.android.com/reference/android/content/pm/InstallSourceInfo)
Throws
PackageManager.NameNotFoundException
(https://developer.android.com/reference/android/content/pm/PackageManager.NameNotFoundException)
getInstalledApplications
Return a List of all application packages that are installed for the current user. If flag
GET_UNINSTALLED_PACKAGES has been set, a list of all applications including those deleted
with DELETE_KEEP_DATA (partially installed apps with data directory) will be returned. Use
public abstract List (https://developer.android.com/reference/java/util/List)<ApplicationInfo (ht


Added in API level 33 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
getInstalledApplications(ApplicationInfoFlags)
(https://developer.android.com/reference/android/content/pm/PackageManager#getInstalledApplications(
android.content.pm.PackageManager.ApplicationInfoFlags))
when long flags are needed.
Parameters
flags
int: Additional option flags to modify the data returned.
Returns
List (https://developer.android.com/reference/java/util/List)<Application
Info
(https://developer.android.com/reference/android/content/pm/ApplicationInfo)
>
A List of ApplicationInfo obje
one for each installed applic
In the unlikely case there are
installed packages, an empty
is returned. If flag MATCH_
UNINSTALLED_PACKAGES i
the application information is
retrieved from the list of
uninstalled applications (whi
includes installed application
well as applications with dat
directory i.e. applications wh
had been deleted with DELET
KEEP_DATA flag set).
This value cannot be null.
getInstalledApplications
public List (https://developer.android.com/reference/java/util/List)<ApplicationInfo (https://develop


Added in API level 29 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
See getInstalledApplications(int)
(https://developer.android.com/reference/android/content/pm/PackageManager#getInstalledApplications(
int))
Parameters
flags
PackageManager.ApplicationInfoFlags: This value cannot be
null.
Returns
List (https://developer.android.com/reference/java/util/List)<Application
Info
(https://developer.android.com/reference/android/content/pm/ApplicationInfo)
>
This value cannot be null.
getInstalledModules
Return a List of all modules that are installed.
Parameters
flags
int: Additional option flags to modify the data returned.
Value is either 0 or
MATCH_ALL
 (https://developer.android.com/reference/android/content/pm/Packag
public List (https://developer.android.com/reference/java/util/List)<ModuleInfo (https://developer.and


Added in API level 1 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Returns
List (https://developer.android.com/reference/java/util/List)<Module
Info
(https://developer.android.com/reference/android/content/pm/ModuleInfo)
>
A List (https://developer.andro
Info
 (https://developer.android.com/
objects, one for each installed m
module. In the unlikely case ther
returned.
This value cannot be null.
getInstalledPackages
Return a List of all packages that are installed for the current user. Use
getInstalledPackages(PackageInfoFlags)
(https://developer.android.com/reference/android/content/pm/PackageManager#getInstalledPackages(an
droid.content.pm.PackageManager.PackageInfoFlags))
when long flags are needed.
Parameters
flags
int: Additional option flags to modify the data returned.
Returns
public abstract List (https://developer.android.com/reference/java/util/List)<PackageInfo (https://


Added in API level 33 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
List (https://developer.android.com/reference/java/util/List)<Package
Info
(https://developer.android.com/reference/android/content/pm/PackageInfo)
>
A List of PackageInfo objects, o
for each installed package,
containing information about th
package. In the unlikely case th
are no installed packages, an
empty list is returned. If flag
MATCH_UNINSTALLED_
PACKAGES is set, the package
information is retrieved from th
list of uninstalled applications
(which includes installed
applications as well as
applications with data directory
i.e. applications which had been
deleted with DELETE_KEEP_
DATA flag set).
This value cannot be null.
getInstalledPackages
See getInstalledPackages(int)
(https://developer.android.com/reference/android/content/pm/PackageManager#getInstalledPackages(int
))
.
Parameters
flags
PackageManager.PackageInfoFlags: This value cannot be null.
public List (https://developer.android.com/reference/java/util/List)<PackageInfo (https://developer.an


Added in API level 5 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Deprecated in API level 30
(https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
or
Returns
List (https://developer.android.com/reference/java/util/List)<Package
Info
(https://developer.android.com/reference/android/content/pm/PackageInfo)
>
This value cannot be null.
getInstallerPackageName
This method was deprecated in API level 30.
use getInstallSourceInfo(String)
(https://developer.android.com/reference/android/content/pm/PackageManager#getInstallSourceInfo(java
.lang.String))
instead
Retrieve the package name of the application that installed a package. This identifies which
market the package came from.
Parameters
packageName
String: The name of the package to query.
This value cannot be null.
public abstract String (https://developer.android.com/reference/java/lang/String) getInstallerP


Added in API level 26 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Returns
String
(https://developer.android.com/reference/java/lang/String)
This value may be null.
Throws
IllegalArgumentException
(https://developer.android.com/reference/java/lang/IllegalArgumentException)
if the given package name is 
installed
getInstantAppCookie
Gets the instant application cookie for this app. Non instant apps and apps that were instant
but were upgraded to normal apps can still access this API. For instant apps this cookie is
cached for some time after uninstall while for normal apps the cookie is deleted after the app
is uninstalled. The cookie is always present while the app is installed.
Returns
byte[]
The cookie.
This value cannot be null.
See also:
public abstract byte[] getInstantAppCookie ()


Added in API level 26 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
isInstantApp()
(https://developer.android.com/reference/android/content/pm/PackageManager#isInstantApp())
isInstantApp(String)
(https://developer.android.com/reference/android/content/pm/PackageManager#isInstantApp(java.lang.St
ring))
updateInstantAppCookie(byte[])
(https://developer.android.com/reference/android/content/pm/PackageManager#updateInstantAppCookie
(byte[]))
getInstantAppCookieMaxBytes()
(https://developer.android.com/reference/android/content/pm/PackageManager#getInstantAppCookieMax
Bytes())
clearInstantAppCookie()
(https://developer.android.com/reference/android/content/pm/PackageManager#clearInstantAppCookie())
getInstantAppCookieMaxBytes
Gets the maximum size in bytes of the cookie data an instant app can store on the device.
Returns
int
The max cookie size in bytes.
See also:
isInstantApp()
(https://developer.android.com/reference/android/content/pm/PackageManager#isInstantApp())
public abstract int getInstantAppCookieMaxBytes ()


Added in API level 1 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
isInstantApp(String)
(https://developer.android.com/reference/android/content/pm/PackageManager#isInstantApp(java.lang.St
ring))
updateInstantAppCookie(byte[])
(https://developer.android.com/reference/android/content/pm/PackageManager#updateInstantAppCookie
(byte[]))
getInstantAppCookie()
(https://developer.android.com/reference/android/content/pm/PackageManager#getInstantAppCookie())
clearInstantAppCookie()
(https://developer.android.com/reference/android/content/pm/PackageManager#clearInstantAppCookie())
getInstrumentationInfo
Retrieve all of the information we know about a particular instrumentation class.
Parameters
className
ComponentName: The full name (i.e. com.google.apps.contacts.Instrumen
class.
This value cannot be null.
flags
int: Additional option flags to modify the data returned.
Value is either 0 or
GET_META_DATA
 (https://developer.android.com/reference/android/content/pm/Packag
public abstract InstrumentationInfo (https://developer.android.com/reference/android/content/p
               int flags)


Added in API level 3 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Returns
InstrumentationInfo
(https://developer.android.com/reference/android/content/pm/InstrumentationInfo)
An Instrumentation
 (https://developer.andro
object containing inform
This value cannot be nu
Throws
PackageManager.NameNotFoundException
(https://developer.android.com/reference/android/content/pm/PackageManager.NameNotFoundException)
getLaunchIntentForPackage
Returns a "good" intent to launch a front-door activity in a package. This is used, for example, to
implement an "open" button when browsing through packages. The current implementation
looks first for a main activity in the category Intent.CATEGORY_INFO
(https://developer.android.com/reference/android/content/Intent#CATEGORY_INFO), and next for a main
activity in the category Intent.CATEGORY_LAUNCHER
(https://developer.android.com/reference/android/content/Intent#CATEGORY_LAUNCHER). Returns null
if neither are found.
Consider using getLaunchIntentSenderForPackage(String)
(https://developer.android.com/reference/android/content/pm/PackageManager#getLaunchIntentSenderF
orPackage(java.lang.String))
if the caller is not allowed to query for the packageName.
public abstract Intent (https://developer.android.com/reference/android/content/Intent) getLaunc


Added in API level 33 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Parameters
packageName
String: The name of the package to inspect.
This value cannot be null.
Returns
Intent
(https://developer.android.com/reference/android/content/Intent)
A fully-qualified Intent
 (https://developer.android.com/reference
that can be used to launch the main activit
Returns null if the package does not con
if packageName is not recognized.
See also:
getLaunchIntentSenderForPackage(String)
(https://developer.android.com/reference/android/content/pm/PackageManager#getLaunchIntentSenderF
orPackage(java.lang.String))
getLaunchIntentSenderForPackage
Returns an IntentSender (https://developer.android.com/reference/android/content/IntentSender)
that can be used to launch a front-door activity in a package. This is used, for example, to
implement an "open" button when browsing through packages. The current implementation is
the same with getLaunchIntentForPackage(String)
(https://developer.android.com/reference/android/content/pm/PackageManager#getLaunchIntentForPack
age(java.lang.String))
public IntentSender (https://developer.android.com/reference/android/content/IntentSender) getLau


Added in API level 21 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
. Instead of returning the Intent (https://developer.android.com/reference/android/content/Intent), it
returns the IntentSender (https://developer.android.com/reference/android/content/IntentSender)
which is not restricted by the package visibility.
The caller can invoke
IntentSender.sendIntent(Context,int,Intent,IntentSender.OnFinished,Handler)
(https://developer.android.com/reference/android/content/IntentSender#sendIntent(android.content.Conte
xt,%20int,%20android.content.Intent,%20android.content.IntentSender.OnFinished,%20android.os.Handler))
to launch the activity. An IntentSender.SendIntentException
(https://developer.android.com/reference/android/content/IntentSender.SendIntentException) is thrown if
the package does not contain such an activity, or if packageName is not recognized.
Parameters
packageName
String: The name of the package to inspect.
This value cannot be null.
Returns
IntentSender
(https://developer.android.com/reference/android/content/IntentSender)
Returns a IntentSender
 (https://developer.android.com/ref
to launch the activity.
This value cannot be null.
See also:
getLaunchIntentForPackage(String)
(https://developer.android.com/reference/android/content/pm/PackageManager#getLaunchIntentForPack
age(java.lang.String))
getLeanbackLaunchIntentForPackage


Added in API level 30 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Return a "good" intent to launch a front-door Leanback activity in a package, for use for
example to implement an "open" button when browsing through packages. The current
implementation will look for a main activity in the category
Intent.CATEGORY_LEANBACK_LAUNCHER
(https://developer.android.com/reference/android/content/Intent#CATEGORY_LEANBACK_LAUNCHER), or
return null if no main leanback activities are found.
Parameters
packageName
String: The name of the package to inspect.
This value cannot be null.
Returns
Intent
(https://developer.android.com/reference/android/content/Intent)
Returns either a fully-qualified Intent that
can be used to launch the main Leanback
activity in the package, or null if the
package does not contain such an
activity.
getMimeGroup
public abstract Intent (https://developer.android.com/reference/android/content/Intent) getLeanb
public Set (https://developer.android.com/reference/java/util/Set)<String (https://developer.android.co


Added in API level 29 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Gets all MIME types contained by MIME group. Libraries should use a reverse-DNS prefix
followed by a ':' character and library-specific group name to avoid namespace collisions, e.g.
"com.example:myFeature".
Parameters
mimeGroup
String: MIME group to retrieve.
This value cannot be null.
Returns
Set
(https://developer.android.com/reference/java/util/Set)
<String
(https://developer.android.com/reference/java/lang/String)
>
MIME types contained by the MIME group.
This value cannot be null.
Throws
IllegalArgumentException
(https://developer.android.com/reference/java/lang/IllegalArgumentException)
if the MIME group was not
declared in the manifest.
getModuleInfo
public ModuleInfo (https://developer.android.com/reference/android/content/pm/ModuleInfo) getMod
               int flags)


Added in API level 1 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Retrieve information for a particular module.
Parameters
packageName
String: The name of the module.
This value cannot be null.
flags
int: Additional option flags to modify the data returned.
Value is either 0 or
Returns
ModuleInfo
(https://developer.android.com/reference/android/content/pm/ModuleInfo)
A ModuleInfo
 (https://developer.android.com/
object containing information ab
This value cannot be null.
Throws
PackageManager.NameNotFoundException
(https://developer.android.com/reference/android/content/pm/PackageManager.NameNotFoundException)
getNameForUid
public abstract String (https://developer.android.com/reference/java/lang/String) getNameForUid


Added in API level 1 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Retrieve the official name associated with a uid. This name is guaranteed to never change,
though it is possible for the underlying uid to be changed. That is, if you are storing information
about uids in persistent storage, you should use the string returned by this function instead of
the raw uid.
Parameters
uid
int: The uid for which you would like to retrieve a name.
Returns
String
(https://developer.android.com/reference/java/lang/String)
Returns a unique name for the given uid, or null
if the uid is not currently assigned.
getPackageArchiveInfo
Retrieve overall information about an application package defined in a package archive file Use
getPackageArchiveInfo(String,PackageInfoFlags)
(https://developer.android.com/reference/android/content/pm/PackageManager#getPackageArchiveInfo(j
ava.lang.String,%20android.content.pm.PackageManager.PackageInfoFlags))
when long flags are needed.
Parameters
public PackageInfo (https://developer.android.com/reference/android/content/pm/PackageInfo) getP
               int flags)


Added in API level 33 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
archiveFilePath
String: The path to the archive file.
This value cannot be null.
flags
int: Additional option flags to modify the data returned.
Returns
PackageInfo
(https://developer.android.com/reference/android/content/pm/PackageInfo)
A PackageInfo object containin
information about the package
archive. If the package could no
be parsed, returns null.
getPackageArchiveInfo
See getPackageArchiveInfo(String,int)
(https://developer.android.com/reference/android/content/pm/PackageManager#getPackageArchiveInfo(j
ava.lang.String,%20int))
.
Parameters
archiveFilePath
String: This value cannot be null.
public PackageInfo (https://developer.android.com/reference/android/content/pm/PackageInfo) getP
               PackageManager.PackageInfoFlags (https://developer.android.com/reference/an


Added in API level 1 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
flags
PackageManager.PackageInfoFlags: This value cannot be null.
Returns
PackageInfo
(https://developer.android.com/reference/android/content/pm/PackageInfo)
This value may be null.
getPackageGids
Return an array of all of the POSIX secondary group IDs that have been assigned to the given
package.
Note that the same package may have different GIDs under different UserHandle
(https://developer.android.com/reference/android/os/UserHandle) on the same device.
Parameters
packageName
String: The full name (i.e. com.google.apps.contacts) of the desired
package.
This value cannot be null.
Returns
public abstract int[] getPackageGids (String (https://developer.android.com/reference/java/la


Added in API level 24 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
int[]
Returns an int array of the assigned GIDs, or null if there are none.
Throws
PackageManager.NameNotFoundException
(https://developer.android.com/reference/android/content/pm/PackageManager.NameNotFoundException)
getPackageGids
Return an array of all of the POSIX secondary group IDs that have been assigned to the given
package.
Note that the same package may have different GIDs under different UserHandle
(https://developer.android.com/reference/android/os/UserHandle) on the same device. Use
getPackageGids(String,PackageInfoFlags)
(https://developer.android.com/reference/android/content/pm/PackageManager#getPackageGids(java.lan
g.String,%20android.content.pm.PackageManager.PackageInfoFlags))
when long flags are needed.
Parameters
packageName
String: The full name (i.e. com.google.apps.contacts) of the desired
package.
This value cannot be null.
public abstract int[] getPackageGids (String (https://developer.android.com/reference/java/la
               int flags)


Added in API level 33 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
flags
int
Returns
int[]
Returns an int array of the assigned gids, or null if there are none.
Throws
PackageManager.NameNotFoundException
(https://developer.android.com/reference/android/content/pm/PackageManager.NameNotFoundException)
getPackageGids
See getPackageGids(String,int)
(https://developer.android.com/reference/android/content/pm/PackageManager#getPackageGids(java.lan
g.String,%20int))
.
Parameters
packageName
String: This value cannot be null.
public int[] getPackageGids (String (https://developer.android.com/reference/java/lang/String) 
               PackageManager.PackageInfoFlags (https://developer.android.com/reference/an


Added in API level 1 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
flags
PackageManager.PackageInfoFlags: This value cannot be null.
Returns
int[]
This value may be null.
Throws
PackageManager.NameNotFoundException
(https://developer.android.com/reference/android/content/pm/PackageManager.NameNotFoundException)
getPackageInfo
Retrieve overall information about an application package that is installed on the system. Use
getPackageInfo(String,PackageInfoFlags)
(https://developer.android.com/reference/android/content/pm/PackageManager#getPackageInfo(java.lang
.String,%20android.content.pm.PackageManager.PackageInfoFlags))
when long flags are needed.
Parameters
packageName
String: The full name (i.e. com.google.apps.contacts) of the desired
package.
public abstract PackageInfo (https://developer.android.com/reference/android/content/pm/Package
               int flags)


Added in API level 33 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
This value cannot be null.
flags
int: Additional option flags to modify the data returned.
Returns
PackageInfo
(https://developer.android.com/reference/android/content/pm/PackageInfo)
A PackageInfo object containin
information about the package
flag MATCH_UNINSTALLED_
PACKAGES is set and if the
package is not found in the list 
installed applications, the
package information is retrieve
from the list of uninstalled
applications (which includes
installed applications as well as
applications with data directory
i.e. applications which had bee
deleted with DELETE_KEEP_
DATA flag set).
Throws
PackageManager.NameNotFoundException
(https://developer.android.com/reference/android/content/pm/PackageManager.NameNotFoundException)
getPackageInfo
public PackageInfo (https://developer.android.com/reference/android/content/pm/PackageInfo) getP


Added in API level 33 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
See getPackageInfo(String,int)
(https://developer.android.com/reference/android/content/pm/PackageManager#getPackageInfo(java.lang
.String,%20int))
Parameters
packageName
String: This value cannot be null.
flags
PackageManager.PackageInfoFlags: This value cannot be null.
Returns
PackageInfo
(https://developer.android.com/reference/android/content/pm/PackageInfo)
This value cannot be null.
Throws
PackageManager.NameNotFoundException
(https://developer.android.com/reference/android/content/pm/PackageManager.NameNotFoundException)
getPackageInfo
               PackageManager.PackageInfoFlags (https://developer.android.com/reference/an
public PackageInfo (https://developer.android.com/reference/android/content/pm/PackageInfo) getP


Added in API level 26 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
See getPackageInfo(VersionedPackage,int)
(https://developer.android.com/reference/android/content/pm/PackageManager#getPackageInfo(android.
content.pm.VersionedPackage,%20int))
Parameters
versionedPackage
VersionedPackage: This value cannot be null.
flags
PackageManager.PackageInfoFlags: This value cannot be null.
Returns
PackageInfo
(https://developer.android.com/reference/android/content/pm/PackageInfo)
This value cannot be null.
Throws
PackageManager.NameNotFoundException
(https://developer.android.com/reference/android/content/pm/PackageManager.NameNotFoundException)
getPackageInfo
               PackageManager.PackageInfoFlags (https://developer.android.com/reference/an
public abstract PackageInfo (https://developer.android.com/reference/android/content/pm/Package


Retrieve overall information about an application package that is installed on the system. This
method can be used for retrieving information about packages for which multiple versions can
be installed at the time. Currently only packages hosting static shared libraries can have
multiple installed versions. The method can also be used to get info for a package that has a
single version installed by passing VERSION_CODE_HIGHEST
(https://developer.android.com/reference/android/content/pm/PackageManager#VERSION_CODE_HIGHES
T)
in the VersionedPackage
(https://developer.android.com/reference/android/content/pm/VersionedPackage) constructor. Use
getPackageInfo(VersionedPackage,PackageInfoFlags)
(https://developer.android.com/reference/android/content/pm/PackageManager#getPackageInfo(android.
content.pm.VersionedPackage,%20android.content.pm.PackageManager.PackageInfoFlags))
when long flags are needed.
Parameters
versionedPackage
VersionedPackage: The versioned package for which to query.
This value cannot be null.
flags
int: Additional option flags to modify the data returned.
Returns
PackageInfo
(https://developer.android.com/reference/android/content/pm/PackageInfo)
A PackageInfo object containin
information about the package
flag MATCH_UNINSTALLED_
PACKAGES is set and if the
package is not found in the list 
installed applications, the
package information is retrieve
from the list of uninstalled
applications (which includes
               int flags)


Added in API level 21 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Added in API level 33 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
installed applications as well as
applications with data directory
i.e. applications which had bee
deleted with DELETE_KEEP_
DATA flag set).
Throws
PackageManager.NameNotFoundException
(https://developer.android.com/reference/android/content/pm/PackageManager.NameNotFoundException)
getPackageInstaller
Return interface that offers the ability to install, upgrade, and remove applications on the
device.
Returns
PackageInstaller
(https://developer.android.com/reference/android/content/pm/PackageInstaller)
This value cannot be null
getPackageUid
public abstract PackageInstaller (https://developer.android.com/reference/android/content/pm/P


Added in API level 24 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
See getPackageUid(String,int)
(https://developer.android.com/reference/android/content/pm/PackageManager#getPackageUid(java.lang.
String,%20int))
.
Parameters
packageName
String: This value cannot be null.
flags
PackageManager.PackageInfoFlags: This value cannot be null.
Returns
int
Throws
PackageManager.NameNotFoundException
(https://developer.android.com/reference/android/content/pm/PackageManager.NameNotFoundException)
getPackageUid
public int getPackageUid (String (https://developer.android.com/reference/java/lang/String) pac
               PackageManager.PackageInfoFlags (https://developer.android.com/reference/an


Return the UID associated with the given package name.
Note that the same package will have different UIDs under different UserHandle
(https://developer.android.com/reference/android/os/UserHandle) on the same device. Use
getPackageUid(String,PackageInfoFlags)
(https://developer.android.com/reference/android/content/pm/PackageManager#getPackageUid(java.lang.
String,%20android.content.pm.PackageManager.PackageInfoFlags))
when long flags are needed.
Parameters
packageName
String: The full name (i.e. com.google.apps.contacts) of the desired
package.
This value cannot be null.
flags
int
Returns
int
Returns an integer UID who owns the given package name.
Throws
PackageManager.NameNotFoundException
(https://developer.android.com/reference/android/content/pm/PackageManager.NameNotFoundException)
public abstract int getPackageUid (String (https://developer.android.com/reference/java/lang/
               int flags)


Added in API level 1 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Added in API level 18 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
getPackagesForUid
Retrieve the names of all packages that are associated with a particular user id. In most cases,
this will be a single package name, the package that has been assigned that user id. Where
there are multiple packages sharing the same user id through the "sharedUserId" mechanism,
all packages with that id will be returned.
Parameters
uid
int: The user id for which you would like to retrieve the associated
packages.
Returns
String[]
(https://developer.android.com/reference/java/lang/String)
Returns an array of one or more packages
assigned to the user id, or null if there are no
known packages with the given id.
getPackagesHoldingPermissions
public abstract String[] (https://developer.android.com/reference/java/lang/String) getPackages
public abstract List (https://developer.android.com/reference/java/util/List)<PackageInfo (https://
               int flags)


Return a List of all installed packages that are currently holding any of the given permissions.
Use getPackagesHoldingPermissions(String[],PackageInfoFlags)
(https://developer.android.com/reference/android/content/pm/PackageManager#getPackagesHoldingPer
missions(java.lang.String[],%20android.content.pm.PackageManager.PackageInfoFlags))
when long flags are needed.
Parameters
permissions
String: This value cannot be null.
flags
int: Additional option flags to modify the data returned.
Returns
List (https://developer.android.com/reference/java/util/List)<Package
Info
(https://developer.android.com/reference/android/content/pm/PackageInfo)
>
A List of PackageInfo objects, o
for each installed package that
holds any of the permissions th
were provided, containing
information about the package.
no installed packages hold any 
the permissions, an empty list i
returned. If flag MATCH_
UNINSTALLED_PACKAGES is s
the package information is
retrieved from the list of
uninstalled applications (which
includes installed applications a
well as applications with data
directory i.e. applications which
had been deleted with DELETE_
KEEP_DATA flag set).
This value cannot be null.


Added in API level 33 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Added in API level 1 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
getPackagesHoldingPermissions
See getPackagesHoldingPermissions(String[],int)
(https://developer.android.com/reference/android/content/pm/PackageManager#getPackagesHoldingPer
missions(java.lang.String[],%20int))
.
Parameters
permissions
String: This value cannot be null.
flags
PackageManager.PackageInfoFlags: This value cannot be null.
Returns
List (https://developer.android.com/reference/java/util/List)<Package
Info
(https://developer.android.com/reference/android/content/pm/PackageInfo)
>
This value cannot be null.
getPermissionGroupInfo
public List (https://developer.android.com/reference/java/util/List)<PackageInfo (https://developer.an
               PackageManager.PackageInfoFlags (https://developer.android.com/reference/an
public abstract PermissionGroupInfo (https://developer.android.com/reference/android/content/p


Retrieve all of the information we know about a particular group of permissions.
Parameters
groupName
String: The fully qualified name (i.e. com.google.permission_group.APPS
interested in.
This value cannot be null.
flags
int: Additional option flags to modify the data returned.
Value is either 0 or
GET_META_DATA
 (https://developer.android.com/reference/android/content/pm/Packag
Returns
PermissionGroupInfo
(https://developer.android.com/reference/android/content/pm/PermissionGroupInfo)
Returns a Permissio
 (https://developer.and
containing information
This value cannot be n
Throws
PackageManager.NameNotFoundException
(https://developer.android.com/reference/android/content/pm/PackageManager.NameNotFoundException)
               int flags)


Added in API level 1 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
getPermissionInfo
Retrieve all of the information we know about a particular permission.
Parameters
permName
String: The fully qualified name (i.e. com.google.permission.LOGIN) of th
interested in.
This value cannot be null.
flags
int: Additional option flags to modify the data returned.
Value is either 0 or
GET_META_DATA
 (https://developer.android.com/reference/android/content/pm/Packag
Returns
PermissionInfo
(https://developer.android.com/reference/android/content/pm/PermissionInfo)
Returns a PermissionInfo
 (https://developer.android.c
containing information abou
Throws
public abstract PermissionInfo (https://developer.android.com/reference/android/content/pm/Perm
               int flags)


Added in API level 31 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
PackageManager.NameNotFoundException
(https://developer.android.com/reference/android/content/pm/PackageManager.NameNotFoundException)
getPlatformPermissionsForGroup
Get the platform-defined permissions which belong to a particular permission group.
Parameters
permissionGroupName
String: the permission group whose permissions are desired.
This value cannot be null.
executor
Executor: the Executor
 (https://developer.android.com/reference/java/util/concurrent/Executor) 
invoke the callback.
This value cannot be null.
Callback and listener events are dispatched through this Executor
 (https://developer.android.com/reference/java/util/concurrent/Executor), 
easy way to control which thread is used. To dispatch events through the m
your application, you can use Context.getMainExecutor()
 (https://developer.android.com/reference/android/content/Context#getM
. Otherwise, provide an Executor
 (https://developer.android.com/reference/java/util/concurrent/Executor) t
dispatches to an appropriate thread.
callback
Consumer: the callback which will receive a list of the platform-defined pe
the group, or empty if the group is not a valid platform-defined permission 
public void getPlatformPermissionsForGroup (String (https://developer.android.com/referenc
               Executor (https://developer.android.com/reference/java/util/concurrent/Executor) e
               Consumer (https://developer.android.com/reference/java/util/function/Consumer)<Li


Added in API level 1 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Deprecated in API level 29
(https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
or
was an exception.
This value cannot be null.
getPreferredActivities
This method was deprecated in API level 29.
This function no longer does anything. It is the platform's responsibility to assign preferred activities and this
cannot be modified directly. To determine the activities resolved by the platform, use
resolveActivity(Intent, ResolveInfoFlags)
(https://developer.android.com/reference/android/content/pm/PackageManager#resolveActivity(android.c
ontent.Intent,%20android.content.pm.PackageManager.ResolveInfoFlags))
or queryIntentActivities(Intent, ResolveInfoFlags)
(https://developer.android.com/reference/android/content/pm/PackageManager#queryIntentActivities(and
roid.content.Intent,%20android.content.pm.PackageManager.ResolveInfoFlags))
. To configure an app to be responsible for a particular role and to check current role holders, see
RoleManager (https://developer.android.com/reference/android/app/role/RoleManager).
Retrieve all preferred activities, previously added with
addPreferredActivity(IntentFilter, int, ComponentName, ComponentName)
(https://developer.android.com/reference/android/content/pm/PackageManager#addPreferredActivity(and
roid.content.IntentFilter,%20int,%20android.content.ComponentName[],%20android.content.ComponentNam
e))
, that are currently registered with the system.
Parameters
public abstract int getPreferredActivities (List (https://developer.android.com/reference/j
               List (https://developer.android.com/reference/java/util/List)<ComponentName (https
               String (https://developer.android.com/reference/java/lang/String) packageName)


Added in API level 1 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Deprecated in API level 29
(https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
or
outFilters
List: A required list in which to place the filters of all of the preferred
activities.
This value cannot be null.
outActivities
List: A required list in which to place the component names of all of the
preferred activities.
This value cannot be null.
packageName
String: An optional package in which you would like to limit the list. If
null, all activities will be returned; if non-null, only those activities in the
given package are returned.
Returns
int
Returns the total number of registered preferred activities (the number of
distinct IntentFilter records, not the number of unique activity
components) that were found.
getPreferredPackages
This method was deprecated in API level 29.
This function no longer does anything. It is the platform's responsibility to assign preferred activities and this
cannot be modified directly. To determine the activities resolved by the platform, use
resolveActivity(Intent, ResolveInfoFlags)
(https://developer.android.com/reference/android/content/pm/PackageManager#resolveActivity(android.c
ontent.Intent,%20android.content.pm.PackageManager.ResolveInfoFlags))
public abstract List (https://developer.android.com/reference/java/util/List)<PackageInfo (https://


Added in API level 31 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
or queryIntentActivities(Intent, ResolveInfoFlags)
(https://developer.android.com/reference/android/content/pm/PackageManager#queryIntentActivities(and
roid.content.Intent,%20android.content.pm.PackageManager.ResolveInfoFlags))
. To configure an app to be responsible for a particular role and to check current role holders, see
RoleManager (https://developer.android.com/reference/android/app/role/RoleManager).
Retrieve the list of all currently configured preferred packages. The first package on the list is
the most preferred, the last is the least preferred.
Parameters
flags
int: Additional option flags to modify the data returned.
Returns
List (https://developer.android.com/reference/java/util/List)<Package
Info
(https://developer.android.com/reference/android/content/pm/PackageInfo)
>
A List of PackageInfo objects, o
for each preferred application, i
order of preference.
This value cannot be null.
getProperty
Returns the property defined in the given package's <application> tag.
public PackageManager.Property (https://developer.android.com/reference/android/content/pm/Pac
               String (https://developer.android.com/reference/java/lang/String) packageName)


Added in API level 31 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Parameters
propertyName
String: This value cannot be null.
packageName
String: This value cannot be null.
Returns
PackageManager.Property
(https://developer.android.com/reference/android/content/pm/PackageManager.Property)
This value canno
Throws
PackageManager.NameNotFoundException
(https://developer.android.com/reference/android/content/pm/PackageManager.NameNotFoundException)
getProperty
Returns the property defined in the given component declaration.
public PackageManager.Property (https://developer.android.com/reference/android/content/pm/Pac
               ComponentName (https://developer.android.com/reference/android/content/Compone


Added in API level 9 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Parameters
propertyName
String: This value cannot be null.
component
ComponentName: This value cannot be null.
Returns
PackageManager.Property
(https://developer.android.com/reference/android/content/pm/PackageManager.Property)
This value canno
Throws
PackageManager.NameNotFoundException
(https://developer.android.com/reference/android/content/pm/PackageManager.NameNotFoundException)
getProviderInfo
Retrieve all of the information we know about a particular content provider class. Use
getProviderInfo(ComponentName,ComponentInfoFlags)
public abstract ProviderInfo (https://developer.android.com/reference/android/content/pm/Provid
               int flags)


Added in API level 33 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
(https://developer.android.com/reference/android/content/pm/PackageManager#getProviderInfo(android.
content.ComponentName,%20android.content.pm.PackageManager.ComponentInfoFlags))
when long flags are needed.
Parameters
component
ComponentName: The full component name (i.e.
com.google.providers.media/com.google.providers.media.
MediaProvider) of a ContentProvider class.
This value cannot be null.
flags
int: Additional option flags to modify the data returned.
Returns
ProviderInfo
(https://developer.android.com/reference/android/content/pm/ProviderInfo)
A ProviderInfo
 (https://developer.android.com
object containing information a
This value cannot be null.
Throws
PackageManager.NameNotFoundException
(https://developer.android.com/reference/android/content/pm/PackageManager.NameNotFoundException)
getProviderInfo


Added in API level 1 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
See getProviderInfo(ComponentName,int)
(https://developer.android.com/reference/android/content/pm/PackageManager#getProviderInfo(android.
content.ComponentName,%20int))
.
Parameters
component
ComponentName: This value cannot be null.
flags
PackageManager.ComponentInfoFlags: This value cannot be null.
Returns
ProviderInfo
(https://developer.android.com/reference/android/content/pm/ProviderInfo)
This value cannot be null.
Throws
PackageManager.NameNotFoundException
(https://developer.android.com/reference/android/content/pm/PackageManager.NameNotFoundException)
getReceiverInfo
public ProviderInfo (https://developer.android.com/reference/android/content/pm/ProviderInfo) get
               PackageManager.ComponentInfoFlags (https://developer.android.com/reference/


Retrieve all of the information we know about a particular receiver class. Use
getReceiverInfo(ComponentName,ComponentInfoFlags)
(https://developer.android.com/reference/android/content/pm/PackageManager#getReceiverInfo(android.
content.ComponentName,%20android.content.pm.PackageManager.ComponentInfoFlags))
when long flags are needed.
Parameters
component
ComponentName: The full component name (i.e.
com.google.apps.calendar/com.google.apps.calendar. CalendarAlarm) of
a Receiver class.
This value cannot be null.
flags
int: Additional option flags to modify the data returned.
Returns
ActivityInfo
(https://developer.android.com/reference/android/content/pm/ActivityInfo)
An ActivityInfo
 (https://developer.android.com/
containing information about the
This value cannot be null.
Throws
public abstract ActivityInfo (https://developer.android.com/reference/android/content/pm/Activit
               int flags)


Added in API level 33 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
PackageManager.NameNotFoundException
(https://developer.android.com/reference/android/content/pm/PackageManager.NameNotFoundException)
getReceiverInfo
See getReceiverInfo(ComponentName,int)
(https://developer.android.com/reference/android/content/pm/PackageManager#getReceiverInfo(android.
content.ComponentName,%20int))
.
Parameters
component
ComponentName: This value cannot be null.
flags
PackageManager.ComponentInfoFlags: This value cannot be null.
Returns
ActivityInfo
(https://developer.android.com/reference/android/content/pm/ActivityInfo)
This value cannot be null.
Throws
public ActivityInfo (https://developer.android.com/reference/android/content/pm/ActivityInfo) getR
               PackageManager.ComponentInfoFlags (https://developer.android.com/reference/


Added in API level 1 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
PackageManager.NameNotFoundException
(https://developer.android.com/reference/android/content/pm/PackageManager.NameNotFoundException)
getResourcesForActivity
Retrieve the resources associated with an activity. Given the full name of an activity, retrieves
the information about it and calls getResources() to return its application's resources. If the
activity cannot be found, NameNotFoundException is thrown.
Parameters
activityName
ComponentName: Name of the activity whose resources are to be
retrieved.
This value cannot be null.
Returns
Resources
(https://developer.android.com/reference/android/content/res/Resources)
Returns the application's
Resources.
This value cannot be null.
Throws
public abstract Resources (https://developer.android.com/reference/android/content/res/Resources


Added in API level 1 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
PackageManager.NameNotFoundException
(https://developer.android.com/reference/android/content/pm/PackageManager.NameNotFoundException)
See also:
getResourcesForApplication(ApplicationInfo)
(https://developer.android.com/reference/android/content/pm/PackageManager#getResourcesForApplicat
ion(android.content.pm.ApplicationInfo))
getResourcesForApplication
Retrieve the resources for an application. Throws NameNotFoundException if the package is
no longer installed.
Parameters
app
ApplicationInfo: Information about the desired application.
This value cannot be null.
Returns
Resources
(https://developer.android.com/reference/android/content/res/Resources)
Returns the application's
Resources.
This value cannot be null.
public abstract Resources (https://developer.android.com/reference/android/content/res/Resources


Added in API level 1 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Throws
PackageManager.NameNotFoundException
(https://developer.android.com/reference/android/content/pm/PackageManager.NameNotFoundException)
getResourcesForApplication
Retrieve the resources associated with an application. Given the full package name of an
application, retrieves the information about it and calls getResources() to return its
application's resources. If the appPackageName cannot be found, NameNotFoundException is
thrown.
Parameters
packageName
String: Package name of the application whose resources are to be
retrieved.
This value cannot be null.
Returns
Resources
(https://developer.android.com/reference/android/content/res/Resources)
Returns the application's
Resources.
This value cannot be null.
public abstract Resources (https://developer.android.com/reference/android/content/res/Resources


Added in API level 31 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Throws
PackageManager.NameNotFoundException
(https://developer.android.com/reference/android/content/pm/PackageManager.NameNotFoundException)
See also:
getResourcesForApplication(ApplicationInfo)
(https://developer.android.com/reference/android/content/pm/PackageManager#getResourcesForApplicat
ion(android.content.pm.ApplicationInfo))
getResourcesForApplication
Retrieve the resources for an application for the provided configuration.
Parameters
app
ApplicationInfo: Information about the desired application.
This value cannot be null.
configuration
Configuration: Overridden configuration when loading the Resources.
This value may be null.
public Resources (https://developer.android.com/reference/android/content/res/Resources) getResou
               Configuration (https://developer.android.com/reference/android/content/res/Confi


Added in API level 33 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Returns
Resources
(https://developer.android.com/reference/android/content/res/Resources)
Returns the application's
Resources.
This value cannot be null.
Throws
PackageManager.NameNotFoundException
(https://developer.android.com/reference/android/content/pm/PackageManager.NameNotFoundException)
getServiceInfo
See getServiceInfo(ComponentName,int)
(https://developer.android.com/reference/android/content/pm/PackageManager#getServiceInfo(android.c
ontent.ComponentName,%20int))
.
Parameters
component
ComponentName: This value cannot be null.
public ServiceInfo (https://developer.android.com/reference/android/content/pm/ServiceInfo) getSe
               PackageManager.ComponentInfoFlags (https://developer.android.com/reference/


Added in API level 1 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
flags
PackageManager.ComponentInfoFlags: This value cannot be null.
Returns
ServiceInfo
(https://developer.android.com/reference/android/content/pm/ServiceInfo)
This value cannot be null.
Throws
PackageManager.NameNotFoundException
(https://developer.android.com/reference/android/content/pm/PackageManager.NameNotFoundException)
getServiceInfo
Retrieve all of the information we know about a particular service class. Use
getServiceInfo(ComponentName,ComponentInfoFlags)
(https://developer.android.com/reference/android/content/pm/PackageManager#getServiceInfo(android.c
ontent.ComponentName,%20android.content.pm.PackageManager.ComponentInfoFlags))
when long flags are needed.
Parameters
public abstract ServiceInfo (https://developer.android.com/reference/android/content/pm/ServiceI
               int flags)


Added in API level 33 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
component
ComponentName: The full component name (i.e.
com.google.apps.media/com.google.apps.media. BackgroundPlayback)
of a Service class.
This value cannot be null.
flags
int: Additional option flags to modify the data returned.
Returns
ServiceInfo
(https://developer.android.com/reference/android/content/pm/ServiceInfo)
A ServiceInfo
 (https://developer.android.com/
object containing information ab
This value cannot be null.
Throws
PackageManager.NameNotFoundException
(https://developer.android.com/reference/android/content/pm/PackageManager.NameNotFoundException)
getSharedLibraries
See getSharedLibraries(int)
(https://developer.android.com/reference/android/content/pm/PackageManager#getSharedLibraries(int)).
public List (https://developer.android.com/reference/java/util/List)<SharedLibraryInfo (https://deve


Added in API level 26 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Parameters
flags
PackageManager.PackageInfoFlags: This value cannot be null.
Returns
List (https://developer.android.com/reference/java/util/List)<SharedLibrary
Info
(https://developer.android.com/reference/android/content/pm/SharedLibraryInfo)
>
This value cannot be null
getSharedLibraries
Get a list of shared libraries on the device. Use getSharedLibraries(PackageInfoFlags)
(https://developer.android.com/reference/android/content/pm/PackageManager#getSharedLibraries(andro
id.content.pm.PackageManager.PackageInfoFlags))
when long flags are needed.
Parameters
flags
int: To filter the libraries to return.
Returns
public abstract List (https://developer.android.com/reference/java/util/List)<SharedLibraryInfo 


Added in API level 28 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
List (https://developer.android.com/reference/java/util/List)<SharedLibrary
Info
(https://developer.android.com/reference/android/content/pm/SharedLibraryInfo)
>
The shared library list.
This value cannot be null
See also:
MATCH_UNINSTALLED_PACKAGES
(https://developer.android.com/reference/android/content/pm/PackageManager#MATCH_UNINSTALLED_
PACKAGES)
getSuspendedPackageAppExtras
Returns a Bundle (https://developer.android.com/reference/android/os/Bundle) of extras that was
meant to be sent to the calling app when it was suspended. An app with the permission
android.permission.SUSPEND_APPS can supply this to the system at the time of suspending
an app.
This is the same Bundle (https://developer.android.com/reference/android/os/Bundle) that is sent
along with the broadcast Intent.ACTION_MY_PACKAGE_SUSPENDED
(https://developer.android.com/reference/android/content/Intent#ACTION_MY_PACKAGE_SUSPENDED),
whenever the app is suspended. The contents of this Bundle
(https://developer.android.com/reference/android/os/Bundle) are a contract between the suspended
app and the suspending app.
Note: These extras are optional, so if no extras were supplied to the system, this method will
return null, even when the calling app has been suspended.
Returns
public Bundle (https://developer.android.com/reference/android/os/Bundle) getSuspendedPackageA


Added in API level 29 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Bundle
(https://developer.android.com/reference/android/os/Bundle)
A Bundle
 (https://developer.android.com/reference/and
containing the extras for the app, or null if th
currently suspended.
See also:
isPackageSuspended()
(https://developer.android.com/reference/android/content/pm/PackageManager#isPackageSuspended())
Intent.ACTION_MY_PACKAGE_UNSUSPENDED
(https://developer.android.com/reference/android/content/Intent#ACTION_MY_PACKAGE_UNSUSPENDED)
Intent.ACTION_MY_PACKAGE_SUSPENDED
(https://developer.android.com/reference/android/content/Intent#ACTION_MY_PACKAGE_SUSPENDED)
Intent.EXTRA_SUSPENDED_PACKAGE_EXTRAS
(https://developer.android.com/reference/android/content/Intent#EXTRA_SUSPENDED_PACKAGE_EXTRAS
)
getSyntheticAppDetailsActivityEnabled
Return whether a synthetic app details activity will be generated if the app has no enabled
launcher activity.
Parameters
packageName
String: The package name of the app.
This value cannot be null.
public boolean getSyntheticAppDetailsActivityEnabled (String (https://developer.android.


Added in API level 5 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Added in API level 3 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Returns
boolean
Returns the enabled state for the synthetic app details activity.
getSystemAvailableFeatures
Get a list of features that are available on the system.
Returns
FeatureInfo[]
(https://developer.android.com/reference/android/content/pm/FeatureInfo)
An array of FeatureInfo classes
describing the features that are
available on the system, or null i
there are none(!!).
getSystemSharedLibraryNames
Get a list of shared libraries that are available on the system.
public abstract FeatureInfo[] (https://developer.android.com/reference/android/content/pm/Featu
public abstract String[] (https://developer.android.com/reference/java/lang/String) getSystemSh


Added in API level 31 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Returns
String[]
(https://developer.android.com/reference/java/lang/String)
An array of shared library names that are
available on the system, or null if none are
installed.
getTargetSdkVersion
Parameters
packageName
String: This value cannot be null.
Returns
int
The target SDK version for the given package name.
Value is 0 or greater
Throws
PackageManager.NameNotFoundException
(https://developer.android.com/reference/android/content/pm/PackageManager.NameNotFoundException)
public int getTargetSdkVersion (String (https://developer.android.com/reference/java/lang/Strin


Added in API level 1 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
getText
Retrieve text from a package. This is a low-level API used by the various package manager info
structures (such as ComponentInfo
(https://developer.android.com/reference/android/content/pm/ComponentInfo) to implement retrieval
of their associated labels and other text.
Parameters
packageName
String: The name of the package that this text is coming from. Cannot
be null.
resid
int: The resource identifier of the desired text. Cannot be 0.
appInfo
ApplicationInfo: Overall information about packageName. This may
be null, in which case the application information will be retrieved for you
if needed; if you already have this information around, it can be much
more efficient to supply it here.
Returns
CharSequence
(https://developer.android.com/reference/java/lang/CharSequence)
Returns a CharSequence holding the
requested text. Returns null if the text
could not be found for any reason.
public abstract CharSequence (https://developer.android.com/reference/java/lang/CharSequence) g
               int resid, 
               ApplicationInfo (https://developer.android.com/reference/android/content/pm/Ap


Added in API level 21 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
getUserBadgedDrawableForDensity
If the target user is a managed profile of the calling user or the caller is itself a managed
profile, then this returns a badged copy of the given drawable allowing the user to distinguish it
from the original drawable. The caller can specify the location in the bounds of the drawable to
be badged where the badge should be applied as well as the density of the badge to be used.
If the original drawable is a BitmapDrawable and the backing bitmap is mutable as per
Bitmap.isMutable() (https://developer.android.com/reference/android/graphics/Bitmap#isMutable()),
the badging is performed in place and the original drawable is returned.
Parameters
drawable
Drawable: The drawable to badge.
This value cannot be null.
user
UserHandle: The target user.
This value cannot be null.
badgeLocation
Rect: Where in the bounds of the badged drawable to place the badge. If i
null, the badge is applied on top of the entire drawable being badged.
badgeDensity
int: The optional desired density for the badge as per DisplayMetrics
densityDpi
 (https://developer.android.com/reference/android/util/DisplayMetrics#de
. If it's not positive, the density of the display is used.
public abstract Drawable (https://developer.android.com/reference/android/graphics/drawable/Draw
               UserHandle (https://developer.android.com/reference/android/os/UserHandle) user
               Rect (https://developer.android.com/reference/android/graphics/Rect) badgeLocat
               int badgeDensity)


Added in API level 21 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Returns
Drawable
(https://developer.android.com/reference/android/graphics/drawable/Drawable)
A drawable that combines t
original drawable and a bad
determined by the system.
This value cannot be null.
getUserBadgedIcon
If the target user is a managed profile, then this returns a badged copy of the given icon to be
able to distinguish it from the original icon. For badging an arbitrary drawable use
getUserBadgedDrawableForDensity(android.graphics.drawable.Drawable,UserHandle
,android.graphics.Rect,int)
(https://developer.android.com/reference/android/content/pm/PackageManager#getUserBadgedDrawable
ForDensity(android.graphics.drawable.Drawable,%20android.os.UserHandle,%20android.graphics.Rect,%20in
t))
.
If the original drawable is a BitmapDrawable and the backing bitmap is mutable as per
Bitmap.isMutable() (https://developer.android.com/reference/android/graphics/Bitmap#isMutable()),
the badging is performed in place and the original drawable is returned.
Parameters
drawable
Drawable: The drawable to badge.
This value cannot be null.
public abstract Drawable (https://developer.android.com/reference/android/graphics/drawable/Draw
               UserHandle (https://developer.android.com/reference/android/os/UserHandle) user


Added in API level 21 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
user
UserHandle: The target user.
This value cannot be null.
Returns
Drawable
(https://developer.android.com/reference/android/graphics/drawable/Drawable)
A drawable that combines t
original icon and a badge as
determined by the system.
This value cannot be null.
getUserBadgedLabel
If the target user is a managed profile of the calling user or the caller is itself a managed
profile, then this returns a copy of the label with badging for accessibility services like talkback.
E.g. passing in "Email" and it might return "Work Email" for Email in the work profile.
Parameters
label
CharSequence: The label to change.
This value cannot be null.
user
UserHandle: The target user.
This value cannot be null.
public abstract CharSequence (https://developer.android.com/reference/java/lang/CharSequence) g
               UserHandle (https://developer.android.com/reference/android/os/UserHandle) user


Added in API level 36 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Returns
CharSequence
(https://developer.android.com/reference/java/lang/CharSequence)
A label that combines the original label
and a badge as determined by the
system.
This value cannot be null.
getVerifiedSigningInfo
Verifies and returns the app signing (https://source.android.com/docs/security/features/apksigning)
information of the file at the given path. This operation takes a few milliseconds. Unlike
getPackageArchiveInfo(String,PackageInfoFlags)
(https://developer.android.com/reference/android/content/pm/PackageManager#getPackageArchiveInfo(j
ava.lang.String,%20android.content.pm.PackageManager.PackageInfoFlags))
with GET_SIGNING_CERTIFICATES
(https://developer.android.com/reference/android/content/pm/PackageManager#GET_SIGNING_CERTIFIC
ATES)
, this method does not require the file to be a package archive file.
Parameters
path
String: This value cannot be null.
minAppSigningScheme
Version
int: Value is one of the following:
SigningInfo.VERSION_JAR
 (https://developer.android.com/reference/android/content/pm/Signing
public static SigningInfo (https://developer.android.com/reference/android/content/pm/SigningInfo
               int minAppSigningSchemeVersion)


Added in API level 29 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
SigningInfo.VERSION_SIGNING_BLOCK_V2
 (https://developer.android.com/reference/android/content/pm/Signing
SigningInfo.VERSION_SIGNING_BLOCK_V3
 (https://developer.android.com/reference/android/content/pm/Signing
SigningInfo.VERSION_SIGNING_BLOCK_V4
 (https://developer.android.com/reference/android/content/pm/Signing
Returns
SigningInfo
(https://developer.android.com/reference/android/content/pm/SigningInfo)
This value cannot be null.
Throws
SigningInfoException
(https://developer.android.com/reference/android/content/pm/SigningInfoException)
if the verification fails
getWhitelistedRestrictedPermissions
Gets the restricted permissions that have been whitelisted and the app is allowed to have them
granted in their full form.
Permissions can be hard restricted which means that the app cannot hold them or soft
restricted where the app can hold the permission but in a weaker form. Whether a permission
is hard restricted
public Set (https://developer.android.com/reference/java/util/Set)<String (https://developer.android.co
               int whitelistFlag)


(https://developer.android.com/reference/android/content/pm/PermissionInfo#FLAG_HARD_RESTRICTED)
or soft restricted
(https://developer.android.com/reference/android/content/pm/PermissionInfo#FLAG_SOFT_RESTRICTED)
depends on the permission declaration. Whitelisting a hard restricted permission allows for the
to hold that permission and whitelisting a soft restricted permission allows the app to hold the
permission in its full, unrestricted form.
There are four allowlists:
1. one for cases where the system permission policy whitelists a permission This list
corresponds to theFLAG_PERMISSION_WHITELIST_SYSTEM
 (https://developer.android.com/reference/android/content/pm/PackageManager#FLAG_PERMISSIO
N_WHITELIST_SYSTEM)
flag. Can only be accessed by pre-installed holders of a dedicated permission.
2. one for cases where the system whitelists the permission when upgrading from an OS
version in which the permission was not restricted to an OS version in which the
permission is restricted. This list corresponds to the
FLAG_PERMISSION_WHITELIST_UPGRADE
 (https://developer.android.com/reference/android/content/pm/PackageManager#FLAG_PERMISSIO
N_WHITELIST_UPGRADE)
flag. Can be accessed by pre-installed holders of a dedicated permission or the installer
on record.
3. one for cases where the installer of the package whitelists a permission. This list
corresponds to the FLAG_PERMISSION_WHITELIST_INSTALLER
 (https://developer.android.com/reference/android/content/pm/PackageManager#FLAG_PERMISSIO
N_WHITELIST_INSTALLER)
flag. Can be accessed by pre-installed holders of a dedicated permission or the installer
on record.
Note: In retrospect it would have been preferred to use more inclusive terminology when
naming this API. Similar APIs added will refrain from using the term "whitelist".
Parameters
packageName
String: The app for which to get whitelisted permissions.
This value cannot be null.


whitelistFlag
int: The flag to determine which whitelist to query. Only one flag can be p
Value is either 0 or a combination of the following:
FLAG_PERMISSION_WHITELIST_SYSTEM
 (https://developer.android.com/reference/android/content/pm/Packag
FLAG_PERMISSION_WHITELIST_INSTALLER
 (https://developer.android.com/reference/android/content/pm/Packag
FLAG_PERMISSION_WHITELIST_UPGRADE
 (https://developer.android.com/reference/android/content/pm/Packag
Returns
Set
(https://developer.android.com/reference/java/util/Set)
<String
(https://developer.android.com/reference/java/lang/String)
>
The whitelisted permissions that are on any of
the whitelists you query for.
This value cannot be null.
Throws
SecurityException
(https://developer.android.com/reference/java/lang/SecurityException)
if you try to access a whitelist that
you have no access to.
See also:
addWhitelistedRestrictedPermission(String,String,int)
(https://developer.android.com/reference/android/content/pm/PackageManager#addWhitelistedRestricted
Permission(java.lang.String,%20java.lang.String,%20int))
removeWhitelistedRestrictedPermission(String,String,int)
(https://developer.android.com/reference/android/content/pm/PackageManager#removeWhitelistedRestri
ctedPermission(java.lang.String,%20java.lang.String,%20int))


Added in API level 1 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
FLAG_PERMISSION_WHITELIST_SYSTEM
(https://developer.android.com/reference/android/content/pm/PackageManager#FLAG_PERMISSION_WHI
TELIST_SYSTEM)
FLAG_PERMISSION_WHITELIST_UPGRADE
(https://developer.android.com/reference/android/content/pm/PackageManager#FLAG_PERMISSION_WHI
TELIST_UPGRADE)
FLAG_PERMISSION_WHITELIST_INSTALLER
(https://developer.android.com/reference/android/content/pm/PackageManager#FLAG_PERMISSION_WHI
TELIST_INSTALLER)
getXml
Retrieve an XML file from a package. This is a low-level API used to retrieve XML meta data.
Parameters
packageName
String: The name of the package that this xml is coming from. Cannot
be null.
resid
int: The resource identifier of the desired xml. Cannot be 0.
appInfo
ApplicationInfo: Overall information about packageName. This may
be null, in which case the application information will be retrieved for you
if needed; if you already have this information around, it can be much
more efficient to supply it here.
public abstract XmlResourceParser (https://developer.android.com/reference/android/content/res/
               int resid, 
               ApplicationInfo (https://developer.android.com/reference/android/content/pm/Ap


Added in API level 28 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Returns
XmlResourceParser
(https://developer.android.com/reference/android/content/res/XmlResourceParser)
Returns an XmlPullPars
allowing you to parse ou
data. Returns null if the 
resource could not be fo
any reason.
hasSigningCertificate
Searches the set of signing certificates by which the package(s) for the given uid has proven to
have been signed. For multiple packages sharing the same uid, this will return the signing
certificates found in the signing history of the "newest" package, where "newest" indicates the
package with the newest signing certificate in the shared uid group. This method should be
used instead of getPackageInfo with GET_SIGNATURES since it takes into account the
possibility of signing certificate rotation, except in the case of packages that are signed by
multiple certificates, for which signing certificate rotation is not supported. This method is
analogous to using getPackagesForUid followed by getPackageInfo with
GET_SIGNING_CERTIFICATES, selecting the PackageInfo of the newest-signed bpackage , and
finally searching through the resulting signingInfo field to see if the desired certificate is
there.
Parameters
uid
int: uid whose signing certificates to check
public boolean hasSigningCertificate (int uid, 
               byte[] certificate, 
               int type)


Added in API level 28 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
certificate
byte: signing certificate for which to search.
This value cannot be null.
type
int: representation of the certificate
Value is one of the following:
CERT_INPUT_RAW_X509
 (https://developer.android.com/reference/android/content/pm/Packag
CERT_INPUT_SHA256
 (https://developer.android.com/reference/android/content/pm/Packag
Returns
boolean
true if this package was or is signed by exactly the certificate
certificate
hasSigningCertificate
Searches the set of signing certificates by which the given package has proven to have been
signed. This should be used instead of getPackageInfo with GET_SIGNATURES since it takes
into account the possibility of signing certificate rotation, except in the case of packages that
are signed by multiple certificates, for which signing certificate rotation is not supported. This
method is analogous to using getPackageInfo with GET_SIGNING_CERTIFICATES and then
searching through the resulting signingInfo field to see if the desired certificate is present.
public boolean hasSigningCertificate (String (https://developer.android.com/reference/java/la
               byte[] certificate, 
               int type)


Added in API level 5 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Parameters
packageName
String: package whose signing certificates to check.
This value cannot be null.
certificate
byte: signing certificate for which to search.
This value cannot be null.
type
int: representation of the certificate
Value is one of the following:
CERT_INPUT_RAW_X509
 (https://developer.android.com/reference/android/content/pm/Packag
CERT_INPUT_SHA256
 (https://developer.android.com/reference/android/content/pm/Packag
Returns
boolean
true if this package was or is signed by exactly the certificate
certificate
hasSystemFeature
Check whether the given feature name is one of the available features as returned by
getSystemAvailableFeatures()
public abstract boolean hasSystemFeature (String (https://developer.android.com/reference/j


Added in API level 24 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
(https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatu
res())
. This tests for the presence of any version of the given feature name; use
hasSystemFeature(String,int)
(https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.l
ang.String,%20int))
to check for a minimum version.
Parameters
featureName
String: This value cannot be null.
Returns
boolean
Returns true if the devices supports the feature, else false.
hasSystemFeature
Check whether the given feature name and version is one of the available features as returned
by getSystemAvailableFeatures()
(https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatu
res())
. Since features are defined to always be backwards compatible, this returns true if the
available feature version is greater than or equal to the requested version.
public abstract boolean hasSystemFeature (String (https://developer.android.com/reference/j
               int version)


Added in API level 35 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Parameters
featureName
String: This value cannot be null.
version
int
Returns
boolean
Returns true if the devices supports the feature, else false.
isAppArchivable
Returns true if an app is archivable.
Parameters
packageName
String: This value cannot be null.
Returns
boolean
public boolean isAppArchivable (String (https://developer.android.com/reference/java/lang/Strin


Added in API level 30 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Throws
PackageManager.NameNotFoundException
(https://developer.android.com/reference/android/content/pm/PackageManager.NameNotFoundException)
See also:
PackageInstaller.requestArchive
(https://developer.android.com/reference/android/content/pm/PackageInstaller#requestArchive(java.lang.
String,%20android.content.IntentSender))
isAutoRevokeWhitelisted
Checks whether an application is exempt from having its permissions be automatically revoked
when the app is unused for an extended period of time. Only the installer on record that
installed the given package, or a holder of WHITELIST_AUTO_REVOKE_PERMISSIONS is allowed
to call this.
Note: In retrospect it would have been preferred to use more inclusive terminology when
naming this API. Similar APIs added will refrain from using the term "whitelist".
Parameters
packageName
String: The app for which to set exemption.
This value cannot be null.
public boolean isAutoRevokeWhitelisted (String (https://developer.android.com/reference/java


Added in API level 30 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Returns
boolean
Whether the app is whitelisted.
Throws
SecurityException
(https://developer.android.com/reference/java/lang/SecurityException)
if you you have no access to this.
See also:
setAutoRevokeWhitelisted(String, boolean)
(https://developer.android.com/reference/android/content/pm/PackageManager#setAutoRevokeWhiteliste
d(java.lang.String,%20boolean))
isAutoRevokeWhitelisted
Note: In retrospect it would have been preferred to use more inclusive terminology when
naming this API. Similar APIs added will refrain from using the term "whitelist".
Returns
boolean
whether this package is whitelisted from having its runtime permission be
auto-revoked if unused for an extended period of time.
public boolean isAutoRevokeWhitelisted ()


Added in API level 30 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Added in API level 29 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
isDefaultApplicationIcon
Returns if the provided drawable represents the default activity icon provided by the system.
PackageManager silently returns a default application icon for any package/activity if the app
itself does not define one or if the system encountered any error when loading the icon.
Developers can use this to check implement app specific logic around retrying or caching.
Parameters
drawable
Drawable: This value cannot be null.
Returns
boolean
true if the drawable represents the default activity icon, false otherwise
See also:
getDefaultActivityIcon()
(https://developer.android.com/reference/android/content/pm/PackageManager#getDefaultActivityIcon())
getActivityIcon(ComponentName)
(https://developer.android.com/reference/android/content/pm/PackageManager#getActivityIcon(android.c
ontent.ComponentName))
LauncherActivityInfo.getIcon(int)
(https://developer.android.com/reference/android/content/pm/LauncherActivityInfo#getIcon(int))
isDeviceUpgrading
public boolean isDefaultApplicationIcon (Drawable (https://developer.android.com/reference/


Added in API level 26 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Returns true if the device is upgrading, such as first boot after OTA.
Returns
boolean
isInstantApp
Gets whether this application is an instant app.
Returns
boolean
Whether caller is an instant app.
See also:
isInstantApp(String)
(https://developer.android.com/reference/android/content/pm/PackageManager#isInstantApp(java.lang.St
ring))
updateInstantAppCookie(byte[])
(https://developer.android.com/reference/android/content/pm/PackageManager#updateInstantAppCookie
(byte[]))
public boolean isDeviceUpgrading ()
public abstract boolean isInstantApp ()


Added in API level 26 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
getInstantAppCookie()
(https://developer.android.com/reference/android/content/pm/PackageManager#getInstantAppCookie())
getInstantAppCookieMaxBytes()
(https://developer.android.com/reference/android/content/pm/PackageManager#getInstantAppCookieMax
Bytes())
isInstantApp
Gets whether the given package is an instant app.
Parameters
packageName
String: The package to check.
This value cannot be null.
Returns
boolean
Whether the given package is an instant app.
See also:
isInstantApp()
(https://developer.android.com/reference/android/content/pm/PackageManager#isInstantApp())
updateInstantAppCookie(byte[])
(https://developer.android.com/reference/android/content/pm/PackageManager#updateInstantAppCookie
(byte[]))
public abstract boolean isInstantApp (String (https://developer.android.com/reference/java/la


Added in API level 35 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
getInstantAppCookie()
(https://developer.android.com/reference/android/content/pm/PackageManager#getInstantAppCookie())
getInstantAppCookieMaxBytes()
(https://developer.android.com/reference/android/content/pm/PackageManager#getInstantAppCookieMax
Bytes())
clearInstantAppCookie()
(https://developer.android.com/reference/android/content/pm/PackageManager#clearInstantAppCookie())
isPackageStopped
Query if an app is currently stopped.
Parameters
packageName
String: This value cannot be null.
Returns
boolean
true if the given package is stopped, false otherwise
Throws
public boolean isPackageStopped (String (https://developer.android.com/reference/java/lang/Str


Added in API level 29 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
PackageManager.NameNotFoundException
(https://developer.android.com/reference/android/content/pm/PackageManager.NameNotFoundException)
See also:
ApplicationInfo.FLAG_STOPPED
(https://developer.android.com/reference/android/content/pm/ApplicationInfo#FLAG_STOPPED)
isPackageSuspended
Query if an app is currently suspended.
Parameters
packageName
String: This value cannot be null.
Returns
boolean
true if the given package is suspended, false otherwise
Throws
public boolean isPackageSuspended (String (https://developer.android.com/reference/java/lang/


Added in API level 28 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
PackageManager.NameNotFoundException
(https://developer.android.com/reference/android/content/pm/PackageManager.NameNotFoundException)
See also:
isPackageSuspended()
(https://developer.android.com/reference/android/content/pm/PackageManager#isPackageSuspended())
isPackageSuspended
Apps can query this to know if they have been suspended. A system app with the permission
android.permission.SUSPEND_APPS can put any app on the device into a suspended state.
While in this state, the application's notifications will be hidden, any of its started activities will
be stopped and it will not be able to show toasts or dialogs or play audio. When the user tries
to launch a suspended app, the system will, instead, show a dialog to the user informing them
that they cannot use this app while it is suspended.
When an app is put into this state, the broadcast action
Intent.ACTION_MY_PACKAGE_SUSPENDED
(https://developer.android.com/reference/android/content/Intent#ACTION_MY_PACKAGE_SUSPENDED)
will be delivered to any of its broadcast receivers that included this action in their intent-filters,
including manifest receivers. Similarly, a broadcast action
Intent.ACTION_MY_PACKAGE_UNSUSPENDED
(https://developer.android.com/reference/android/content/Intent#ACTION_MY_PACKAGE_UNSUSPENDED)
is delivered when a previously suspended app is taken out of this state. Apps are expected to
use these to gracefully deal with transitions to and from this state.
Returns
public boolean isPackageSuspended ()


Added in API level 23 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
boolean
true if the calling package has been suspended, false otherwise.
See also:
getSuspendedPackageAppExtras()
(https://developer.android.com/reference/android/content/pm/PackageManager#getSuspendedPackageA
ppExtras())
Intent.ACTION_MY_PACKAGE_SUSPENDED
(https://developer.android.com/reference/android/content/Intent#ACTION_MY_PACKAGE_SUSPENDED)
Intent.ACTION_MY_PACKAGE_UNSUSPENDED
(https://developer.android.com/reference/android/content/Intent#ACTION_MY_PACKAGE_UNSUSPENDED)
isPermissionRevokedByPolicy
Checks whether a particular permissions has been revoked for a package by policy. Typically
the device owner or the profile owner may apply such a policy. The user cannot grant policy
revoked permissions, hence the only way for an app to get such a permission is by a policy
change.
Parameters
permName
String: The name of the permission you are checking for.
This value cannot be null.
packageName
String: The name of the package you are checking against.
This value cannot be null.
public abstract boolean isPermissionRevokedByPolicy (String (https://developer.android.co
               String (https://developer.android.com/reference/java/lang/String) packageName)


Added in API level 3 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Added in API level 35 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Returns
boolean
Whether the permission is restricted by policy.
isSafeMode
Return whether the device has been booted into safe mode.
Returns
boolean
parseAndroidManifest
Retrieve AndroidManifest.xml information for the given application apk file.
Example:
public abstract boolean isSafeMode ()
public T parseAndroidManifest (File (https://developer.android.com/reference/java/io/File) apkF
               Function (https://developer.android.com/reference/java/util/function/Function)<Xml


Note: When the parserFunction is invoked, the client can read the AndroidManifest.xml
information by the XmlResourceParser object. After leaving the parserFunction, the
XmlResourceParser object will be closed. The caller should also handle the exception for
calling this method.
This method may take several seconds to complete, so it should only be called from a worker
thread.
Parameters
Bundle result;
try {
    result = getContext().getPackageManager().parseAndroidManifest(apkFile,
            xmlResourceParser -> {
                Bundle bundle = new Bundle();
                // Search the start tag
                int type;
                while ((type = xmlResourceParser.next()) != XmlPullParser.START
                        && type != XmlPullParser.END_DOCUMENT) {
                }
                if (type != XmlPullParser.START_TAG) {
                    return bundle;
                }
                // Start to read the tags and attributes from the xmlResourcePa
                if (!xmlResourceParser.getName().equals("manifest")) {
                    return bundle;
                }
                String packageName = xmlResourceParser.getAttributeValue(null, 
                bundle.putString("package", packageName);
                // Continue to read the tags and attributes from the xmlResourc
                return bundle;
            });
} catch (IOException e) {
}


Added in API level 36 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
apkFile
File: The file of an application apk.
This value cannot be null.
parserFunction
Function: The parserFunction will be invoked with the
XmlResourceParser object after getting the AndroidManifest.xml of an
application package.
This value cannot be null.
Returns
T
Returns the result of the Function.apply(Object)
 (https://developer.android.com/reference/java/util/function/Function#app
.
Throws
IOException
(https://developer.android.com/reference/java/io/IOException)
if the AndroidManifest.xml of an application
package cannot be read or accessed.
parseAndroidManifest
Similar to parseAndroidManifest(File,Function)
(https://developer.android.com/reference/android/content/pm/PackageManager#parseAndroidManifest(ja
va.io.File,%20java.util.function.Function%3Candroid.content.res.XmlResourceParser,T%3E))
public T parseAndroidManifest (ParcelFileDescriptor (https://developer.android.com/referen
               Function (https://developer.android.com/reference/java/util/function/Function)<Xml


Added in API level 31 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
, but accepting a file descriptor instead of a File object.
This method may take several seconds to complete, so it should only be called from a worker
thread.
Parameters
apkFileDescriptor
ParcelFileDescriptor: The file descriptor of an application apk. The
parserFunction will be invoked with the XmlResourceParser object after
getting the AndroidManifest.xml of an application package.
This value cannot be null.
parserFunction
Function: This value cannot be null.
Returns
T
Returns the result of the Function.apply(Object)
 (https://developer.android.com/reference/java/util/function/Function#app
.
Throws
IOException
(https://developer.android.com/reference/java/io/IOException)
if the AndroidManifest.xml of an application
package cannot be read or accessed.
queryActivityProperty


Added in API level 31 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Returns the property definition for all <activity> and <activity-alias> tags.
If the property is not defined with any <activity> and <activity-alias> tag, returns and empty list.
Parameters
propertyName
String: This value cannot be null.
Returns
List (https://developer.android.com/reference/java/util/List)<PackageManager.
Property
(https://developer.android.com/reference/android/content/pm/PackageManager.Property)
>
This value cannot
queryApplicationProperty
Returns the property definition for all <application> tags.
If the property is not defined with any <application> tag, returns and empty list.
public List (https://developer.android.com/reference/java/util/List)<PackageManager.Property (http
public List (https://developer.android.com/reference/java/util/List)<PackageManager.Property (http


Added in API level 33 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Parameters
propertyName
String: This value cannot be null.
Returns
List (https://developer.android.com/reference/java/util/List)<PackageManager.
Property
(https://developer.android.com/reference/android/content/pm/PackageManager.Property)
>
This value cannot
queryBroadcastReceivers
See queryBroadcastReceivers(Intent,int)
(https://developer.android.com/reference/android/content/pm/PackageManager#queryBroadcastReceivers
(android.content.Intent,%20int))
.
Parameters
intent
Intent: This value cannot be null.
flags
PackageManager.ResolveInfoFlags: This value cannot be null.
public List (https://developer.android.com/reference/java/util/List)<ResolveInfo (https://developer.an
               PackageManager.ResolveInfoFlags (https://developer.android.com/reference/an


Added in API level 1 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Returns
List (https://developer.android.com/reference/java/util/List)<Resolve
Info
(https://developer.android.com/reference/android/content/pm/ResolveInfo)
>
This value cannot be null.
queryBroadcastReceivers
Retrieve all receivers that can handle a broadcast of the given intent. Use
queryBroadcastReceivers(Intent,ResolveInfoFlags)
(https://developer.android.com/reference/android/content/pm/PackageManager#queryBroadcastReceivers
(android.content.Intent,%20android.content.pm.PackageManager.ResolveInfoFlags))
when long flags are needed.
Parameters
intent
Intent: The desired intent as per resolveActivity().
This value cannot be null.
flags
int: Additional option flags to modify the data returned.
Returns
public abstract List (https://developer.android.com/reference/java/util/List)<ResolveInfo (https://
               int flags)


Added in API level 1 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
List (https://developer.android.com/reference/java/util/List)<Resolve
Info
(https://developer.android.com/reference/android/content/pm/ResolveInfo)
>
Returns a List of ResolveInfo
objects containing one entry for
each matching receiver, ordered
from best to worst. If there are n
matching receivers, returns an
empty list.
This value cannot be null.
queryContentProviders
Retrieve content provider information.
Note: unlike most other methods, an empty result set is indicated by a null return instead of an
empty list. Use queryContentProviders(String,int,ComponentInfoFlags)
(https://developer.android.com/reference/android/content/pm/PackageManager#queryContentProviders(ja
va.lang.String,%20int,%20android.content.pm.PackageManager.ComponentInfoFlags))
when long flags are needed.
Parameters
processName
String: If non-null, limits the returned providers to only those that are
hosted by the given process. If null, all content providers are returned.
uid
int: If processName is non-null, this is the required uid owning the
requested content providers.
public abstract List (https://developer.android.com/reference/java/util/List)<ProviderInfo (https:/
               int uid, 
               int flags)


Added in API level 33 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
flags
int: Additional option flags to modify the data returned.
Returns
List (https://developer.android.com/reference/java/util/List)<Provider
Info
(https://developer.android.com/reference/android/content/pm/ProviderInfo)
>
A list of ProviderInfo
 (https://developer.android.com
objects containing one entry for
or, if processName is null, all kno
matching providers, null is return
queryContentProviders
See queryContentProviders(String,int,int)
(https://developer.android.com/reference/android/content/pm/PackageManager#queryContentProviders(ja
va.lang.String,%20int,%20int))
.
Parameters
processName
String: This value may be null.
uid
int
public List (https://developer.android.com/reference/java/util/List)<ProviderInfo (https://developer.a
               int uid, 
               PackageManager.ComponentInfoFlags (https://developer.android.com/reference/


Added in API level 1 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
flags
PackageManager.ComponentInfoFlags: This value cannot be null.
Returns
List (https://developer.android.com/reference/java/util/List)<Provider
Info
(https://developer.android.com/reference/android/content/pm/ProviderInfo)
>
This value cannot be null.
queryInstrumentation
Retrieve information about available instrumentation code. May be used to retrieve either all
instrumentation code, or only the code targeting a particular package.
Parameters
targetPackage
String: If null, all instrumentation is returned; only the instrumentation ta
returned.
flags
int: Additional option flags to modify the data returned.
Value is either 0 or
GET_META_DATA
 (https://developer.android.com/reference/android/content/pm/Packag
public abstract List (https://developer.android.com/reference/java/util/List)<InstrumentationInf
               int flags)


Added in API level 33 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Returns
List (https://developer.android.com/reference/java/util/List)<Instrumentation
Info
(https://developer.android.com/reference/android/content/pm/InstrumentationInfo)
>
A list of Instrumentat
 (https://developer.andro
objects containing one e
instrumentation availab
This value cannot be nu
queryIntentActivities
See queryIntentActivities(Intent,int)
(https://developer.android.com/reference/android/content/pm/PackageManager#queryIntentActivities(and
roid.content.Intent,%20int))
.
Parameters
intent
Intent: This value cannot be null.
flags
PackageManager.ResolveInfoFlags: This value cannot be null.
Returns
public List (https://developer.android.com/reference/java/util/List)<ResolveInfo (https://developer.an
               PackageManager.ResolveInfoFlags (https://developer.android.com/reference/an


Added in API level 1 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
List (https://developer.android.com/reference/java/util/List)<Resolve
Info
(https://developer.android.com/reference/android/content/pm/ResolveInfo)
>
This value cannot be null.
queryIntentActivities
Retrieve all activities that can be performed for the given intent. Use
queryIntentActivities(Intent,ResolveInfoFlags)
(https://developer.android.com/reference/android/content/pm/PackageManager#queryIntentActivities(and
roid.content.Intent,%20android.content.pm.PackageManager.ResolveInfoFlags))
when long flags are needed.
Parameters
intent
Intent: The desired intent as per resolveActivity().
This value cannot be null.
flags
int: Additional option flags to modify the data returned. The most importa
 (https://developer.android.com/reference/android/content/pm/PackageM
, to limit the resolution to only those activities that support the Intent.CA
 (https://developer.android.com/reference/android/content/Intent#CATEG
ALL (https://developer.android.com/reference/android/content/pm/Packa
prevent any filtering of the results.
public abstract List (https://developer.android.com/reference/java/util/List)<ResolveInfo (https://
               int flags)


Added in API level 1 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Returns
List (https://developer.android.com/reference/java/util/List)<Resolve
Info
(https://developer.android.com/reference/android/content/pm/ResolveInfo)
>
Returns a List of ResolveInfo ob
resolveActivity(Intent, 
 (https://developer.android.com/
. If there are no matching activit
This value cannot be null.
queryIntentActivityOptions
Retrieve a set of activities that should be presented to the user as similar options. This is like
queryIntentActivities(Intent, ResolveInfoFlags)
(https://developer.android.com/reference/android/content/pm/PackageManager#queryIntentActivities(and
roid.content.Intent,%20android.content.pm.PackageManager.ResolveInfoFlags))
, except it also allows you to supply a list of more explicit Intents that you would like to resolve
to particular options, and takes care of returning the final ResolveInfo list in a reasonable order,
with no duplicates, based on those inputs. Use
queryIntentActivityOptions(ComponentName,List,Intent,ResolveInfoFlags)
(https://developer.android.com/reference/android/content/pm/PackageManager#queryIntentActivityOption
s(android.content.ComponentName,%20java.util.List%3Candroid.content.Intent%3E,%20android.content.Inte
nt,%20android.content.pm.PackageManager.ResolveInfoFlags))
when long flags are needed.
Parameters
public abstract List (https://developer.android.com/reference/java/util/List)<ResolveInfo (https://
               Intent[] (https://developer.android.com/reference/android/content/Intent) specif
               Intent (https://developer.android.com/reference/android/content/Intent) intent, 
               int flags)


Added in API level 33 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
caller
ComponentName: The class name of the activity that is making the reques
in the output list. Can be null.
specifics
Intent: An array of Intents that should be resolved to the first specific res
intent
Intent: The desired intent as per resolveActivity().
This value cannot be null.
flags
int: Additional option flags to modify the data returned. The most importa
 (https://developer.android.com/reference/android/content/pm/PackageM
, to limit the resolution to only those activities that support the Intent.CA
 (https://developer.android.com/reference/android/content/Intent#CATEG
Returns
List (https://developer.android.com/reference/java/util/List)<Resolve
Info
(https://developer.android.com/reference/android/content/pm/ResolveInfo)
>
Returns a List of ResolveInfo
objects containing one entry for
each matching activity. The list i
ordered first by all of the intents
resolved in specifics and then an
additional activities that can
handle intent but did not get
included by one of the specifics
intents. If there are no matching
activities, an empty list is
returned.
This value cannot be null.
queryIntentActivityOptions


See queryIntentActivityOptions(ComponentName,Intent[],Intent,int)
(https://developer.android.com/reference/android/content/pm/PackageManager#queryIntentActivityOption
s(android.content.ComponentName,%20android.content.Intent[],%20android.content.Intent,%20int))
.
Parameters
caller
ComponentName: This value may be null.
specifics
List: This value may be null.
intent
Intent: This value cannot be null.
flags
PackageManager.ResolveInfoFlags: This value cannot be null.
Returns
List (https://developer.android.com/reference/java/util/List)<Resolve
Info
(https://developer.android.com/reference/android/content/pm/ResolveInfo)
>
This value cannot be null.
public List (https://developer.android.com/reference/java/util/List)<ResolveInfo (https://developer.an
               List (https://developer.android.com/reference/java/util/List)<Intent (https://develop
               Intent (https://developer.android.com/reference/android/content/Intent) intent, 
               PackageManager.ResolveInfoFlags (https://developer.android.com/reference/an


Added in API level 33 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Added in API level 19 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
queryIntentContentProviders
See queryIntentContentProviders(Intent,int)
(https://developer.android.com/reference/android/content/pm/PackageManager#queryIntentContentProvi
ders(android.content.Intent,%20int))
.
Parameters
intent
Intent: This value cannot be null.
flags
PackageManager.ResolveInfoFlags: This value cannot be null.
Returns
List (https://developer.android.com/reference/java/util/List)<Resolve
Info
(https://developer.android.com/reference/android/content/pm/ResolveInfo)
>
This value cannot be null.
queryIntentContentProviders
public List (https://developer.android.com/reference/java/util/List)<ResolveInfo (https://developer.an
               PackageManager.ResolveInfoFlags (https://developer.android.com/reference/an
public abstract List (https://developer.android.com/reference/java/util/List)<ResolveInfo (https://


Added in API level 1 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Retrieve all providers that can match the given intent. Use
queryIntentContentProviders(Intent,ResolveInfoFlags)
(https://developer.android.com/reference/android/content/pm/PackageManager#queryIntentContentProvi
ders(android.content.Intent,%20android.content.pm.PackageManager.ResolveInfoFlags))
when long flags are needed.
Parameters
intent
Intent: An intent containing all of the desired specification (action, data,
type, category, and/or component).
This value cannot be null.
flags
int: Additional option flags to modify the data returned.
Returns
List (https://developer.android.com/reference/java/util/List)<Resolve
Info
(https://developer.android.com/reference/android/content/pm/ResolveInfo)
>
Returns a List of ResolveInfo
objects containing one entry for
each matching provider, ordered
from best to worst. If there are n
matching services, returns an
empty list.
This value cannot be null.
queryIntentServices
               int flags)


Added in API level 33 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Retrieve all services that can match the given intent. Use
queryIntentServices(Intent,ResolveInfoFlags)
(https://developer.android.com/reference/android/content/pm/PackageManager#queryIntentServices(andr
oid.content.Intent,%20android.content.pm.PackageManager.ResolveInfoFlags))
when long flags are needed.
Parameters
intent
Intent: The desired intent as per resolveService().
This value cannot be null.
flags
int: Additional option flags to modify the data returned.
Returns
List (https://developer.android.com/reference/java/util/List)<Resolve
Info
(https://developer.android.com/reference/android/content/pm/ResolveInfo)
>
Returns a List of ResolveInfo ob
resolveService(Intent, R
 (https://developer.android.com/
. If there are no matching service
This value cannot be null.
queryIntentServices
public abstract List (https://developer.android.com/reference/java/util/List)<ResolveInfo (https://
               int flags)


Added in API level 1 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
See queryIntentServices(Intent,int)
(https://developer.android.com/reference/android/content/pm/PackageManager#queryIntentServices(andr
oid.content.Intent,%20int))
.
Parameters
intent
Intent: This value cannot be null.
flags
PackageManager.ResolveInfoFlags: This value cannot be null.
Returns
List (https://developer.android.com/reference/java/util/List)<Resolve
Info
(https://developer.android.com/reference/android/content/pm/ResolveInfo)
>
This value cannot be null.
queryPermissionsByGroup
public List (https://developer.android.com/reference/java/util/List)<ResolveInfo (https://developer.an
               PackageManager.ResolveInfoFlags (https://developer.android.com/reference/an
public abstract List (https://developer.android.com/reference/java/util/List)<PermissionInfo (http
               int flags)


Added in API level 31 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Query for all of the permissions associated with a particular group.
Parameters
permissionGroup
String: The fully qualified name (i.e. com.google.permission.LOGIN) of th
interested in. Use null to find all of the permissions not associated with a
flags
int: Additional option flags to modify the data returned.
Value is either 0 or
GET_META_DATA
 (https://developer.android.com/reference/android/content/pm/Packag
Returns
List (https://developer.android.com/reference/java/util/List)<Permission
Info
(https://developer.android.com/reference/android/content/pm/PermissionInfo)
>
Returns a list of Permissio
 (https://developer.android.c
containing information abou
This value cannot be null.
Throws
PackageManager.NameNotFoundException
(https://developer.android.com/reference/android/content/pm/PackageManager.NameNotFoundException)
queryProviderProperty


Added in API level 31 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Returns the property definition for all <provider> tags.
If the property is not defined with any <provider> tag, returns and empty list.
Parameters
propertyName
String: This value cannot be null.
Returns
List (https://developer.android.com/reference/java/util/List)<PackageManager.
Property
(https://developer.android.com/reference/android/content/pm/PackageManager.Property)
>
This value cannot
queryReceiverProperty
Returns the property definition for all <receiver> tags.
If the property is not defined with any <receiver> tag, returns and empty list.
public List (https://developer.android.com/reference/java/util/List)<PackageManager.Property (http
public List (https://developer.android.com/reference/java/util/List)<PackageManager.Property (http


Added in API level 31 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Parameters
propertyName
String: This value cannot be null.
Returns
List (https://developer.android.com/reference/java/util/List)<PackageManager.
Property
(https://developer.android.com/reference/android/content/pm/PackageManager.Property)
>
This value cannot
queryServiceProperty
Returns the property definition for all <service> tags.
If the property is not defined with any <service> tag, returns and empty list.
Parameters
propertyName
String: This value cannot be null.
Returns
public List (https://developer.android.com/reference/java/util/List)<PackageManager.Property (http


Added in API level 34 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
List (https://developer.android.com/reference/java/util/List)<PackageManager.
Property
(https://developer.android.com/reference/android/content/pm/PackageManager.Property)
>
This value cannot
relinquishUpdateOwnership
Attempt to relinquish the update ownership of the given package. Only the current update
owner of the given package can use this API.
Parameters
targetPackage
String: The installed package whose update owner will be changed.
This value cannot be null.
Throws
IllegalArgumentException
(https://developer.android.com/reference/java/lang/IllegalArgumentException)
if the given package is invalid
SecurityException
(https://developer.android.com/reference/java/lang/SecurityException)
if you are not the current upd
owner of the given package.
See also:
public void relinquishUpdateOwnership (String (https://developer.android.com/reference/java/


Added in API level 1 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Deprecated in API level 15
(https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
or
Added in API level 1 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
PackageInstaller.SessionParams.setRequestUpdateOwnership
(https://developer.android.com/reference/android/content/pm/PackageInstaller.SessionParams#setReque
stUpdateOwnership(boolean))
removePackageFromPreferred
This method was deprecated in API level 15.
This function no longer does anything. It is the platform's responsibility to assign preferred activities and this
cannot be modified directly. To determine the activities resolved by the platform, use
resolveActivity(Intent, ResolveInfoFlags)
(https://developer.android.com/reference/android/content/pm/PackageManager#resolveActivity(android.c
ontent.Intent,%20android.content.pm.PackageManager.ResolveInfoFlags))
or queryIntentActivities(Intent, ResolveInfoFlags)
(https://developer.android.com/reference/android/content/pm/PackageManager#queryIntentActivities(and
roid.content.Intent,%20android.content.pm.PackageManager.ResolveInfoFlags))
. To configure an app to be responsible for a particular role and to check current role holders, see
RoleManager (https://developer.android.com/reference/android/app/role/RoleManager).
Parameters
packageName
String: This value cannot be null.
removePermission
public abstract void removePackageFromPreferred (String (https://developer.android.com/re


Added in API level 29 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Removes a permission that was previously added with addPermission(PermissionInfo)
(https://developer.android.com/reference/android/content/pm/PackageManager#addPermission(android.c
ontent.pm.PermissionInfo))
. The same ownership rules apply -- you are only allowed to remove permissions that you are
allowed to add.
Parameters
permName
String: The name of the permission to remove.
This value cannot be null.
Throws
SecurityException
(https://developer.android.com/reference/java/lang/SecurityException)
if you are not allowed to remove the
given permission name.
See also:
addPermission(PermissionInfo)
(https://developer.android.com/reference/android/content/pm/PackageManager#addPermission(android.c
ontent.pm.PermissionInfo))
removeWhitelistedRestrictedPermission
public abstract void removePermission (String (https://developer.android.com/reference/java/
public boolean removeWhitelistedRestrictedPermission (String (https://developer.android.
               String (https://developer.android.com/reference/java/lang/String) permName, 


Removes a whitelisted restricted permission for an app.
Permissions can be hard restricted which means that the app cannot hold them or soft
restricted where the app can hold the permission but in a weaker form. Whether a permission
is hard restricted
(https://developer.android.com/reference/android/content/pm/PermissionInfo#FLAG_HARD_RESTRICTED)
or soft restricted
(https://developer.android.com/reference/android/content/pm/PermissionInfo#FLAG_SOFT_RESTRICTED)
depends on the permission declaration. Whitelisting a hard restricted permission allows for the
to hold that permission and whitelisting a soft restricted permission allows the app to hold the
permission in its full, unrestricted form.
There are four whitelists:
1. one for cases where the system permission policy whitelists a permission This list
corresponds to the FLAG_PERMISSION_WHITELIST_SYSTEM
 (https://developer.android.com/reference/android/content/pm/PackageManager#FLAG_PERMISSIO
N_WHITELIST_SYSTEM)
flag. Can only be modified by pre-installed holders of a dedicated permission.
2. one for cases where the system whitelists the permission when upgrading from an OS
version in which the permission was not restricted to an OS version in which the
permission is restricted. This list corresponds to the
FLAG_PERMISSION_WHITELIST_UPGRADE
 (https://developer.android.com/reference/android/content/pm/PackageManager#FLAG_PERMISSIO
N_WHITELIST_UPGRADE)
flag. Can be modified by pre-installed holders of a dedicated permission. The installer on
record can only remove permissions from this whitelist.
3. one for cases where the installer of the package whitelists a permission. This list
corresponds to the FLAG_PERMISSION_WHITELIST_INSTALLER
 (https://developer.android.com/reference/android/content/pm/PackageManager#FLAG_PERMISSIO
N_WHITELIST_INSTALLER)
flag. Can be modified by pre-installed holders of a dedicated permission or the installer
on record.
4. one for cases where the system exempts the permission when upgrading from an OS
version in which the permission was not restricted to an OS version in which the
               int whitelistFlags)


permission is restricted. This list corresponds to the
FLAG_PERMISSION_WHITELIST_UPGRADE
 (https://developer.android.com/reference/android/content/pm/PackageManager#FLAG_PERMISSIO
N_WHITELIST_UPGRADE)
flag. Can be modified by pre-installed holders of a dedicated permission. The installer on
record can only remove permissions from this allowlist.
You need to specify the whitelists for which to set the whitelisted permissions which will clear
the previous whitelisted permissions and replace them with the provided ones.
Note: In retrospect it would have been preferred to use more inclusive terminology when
naming this API. Similar APIs added will refrain from using the term "whitelist".
Parameters
packageName
String: The app for which to get whitelisted permissions.
This value cannot be null.
permName
String: The whitelisted permission to remove.
This value cannot be null.
whitelistFlags
int: The whitelists from which to remove. Passing multiple flags updates 
Value is either 0 or a combination of the following:
FLAG_PERMISSION_WHITELIST_SYSTEM
 (https://developer.android.com/reference/android/content/pm/Packag
FLAG_PERMISSION_WHITELIST_INSTALLER
 (https://developer.android.com/reference/android/content/pm/Packag
FLAG_PERMISSION_WHITELIST_UPGRADE
 (https://developer.android.com/reference/android/content/pm/Packag
Returns


Added in API level 31 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
boolean
Whether the permission was removed from the whitelist.
Throws
SecurityException
(https://developer.android.com/reference/java/lang/SecurityException)
if you try to modify a whitelist that
you have no access to.
See also:
getWhitelistedRestrictedPermissions(String,int)
(https://developer.android.com/reference/android/content/pm/PackageManager#getWhitelistedRestricted
Permissions(java.lang.String,%20int))
addWhitelistedRestrictedPermission(String,String,int)
(https://developer.android.com/reference/android/content/pm/PackageManager#addWhitelistedRestricted
Permission(java.lang.String,%20java.lang.String,%20int))
FLAG_PERMISSION_WHITELIST_SYSTEM
(https://developer.android.com/reference/android/content/pm/PackageManager#FLAG_PERMISSION_WHI
TELIST_SYSTEM)
FLAG_PERMISSION_WHITELIST_UPGRADE
(https://developer.android.com/reference/android/content/pm/PackageManager#FLAG_PERMISSION_WHI
TELIST_UPGRADE)
FLAG_PERMISSION_WHITELIST_INSTALLER
(https://developer.android.com/reference/android/content/pm/PackageManager#FLAG_PERMISSION_WHI
TELIST_INSTALLER)
requestChecksums
public void requestChecksums (String (https://developer.android.com/reference/java/lang/String)
               boolean includeSplits, 
               int required, 


Requests the checksums for APKs within a package. The checksums will be returned
asynchronously via onChecksumsReadyListener. By default returns all readily available
checksums: - enforced by platform, - enforced by installer. If caller needs a specific checksum
kind, they can specify it as required. Caution: Android can not verify installer-provided
checksums. Make sure you specify trusted installers.
Parameters
packageName
String: whose checksums to return.
This value cannot be null.
includeSplits
boolean: whether to include checksums for non-base splits.
               List (https://developer.android.com/reference/java/util/List)<Certificate (https://
               PackageManager.OnChecksumsReadyListener (https://developer.android.com/re


required
int: explicitly request the checksum types. May incur significant CPU/me
Value is either 0 or a combination of the following:
Checksum.TYPE_WHOLE_MERKLE_ROOT_4K_SHA256
 (https://developer.android.com/reference/android/content/pm/Checks
Checksum.TYPE_WHOLE_MD5
 (https://developer.android.com/reference/android/content/pm/Checks
Checksum.TYPE_WHOLE_SHA1
 (https://developer.android.com/reference/android/content/pm/Checks
Checksum.TYPE_WHOLE_SHA256
 (https://developer.android.com/reference/android/content/pm/Checks
Checksum.TYPE_WHOLE_SHA512
 (https://developer.android.com/reference/android/content/pm/Checks
Checksum.TYPE_PARTIAL_MERKLE_ROOT_1M_SHA256
 (https://developer.android.com/reference/android/content/pm/Checks
Checksum.TYPE_PARTIAL_MERKLE_ROOT_1M_SHA512
 (https://developer.android.com/reference/android/content/pm/Checks
trustedInstallers
List: for checksums enforced by installer, which installers are to be truste
 (https://developer.android.com/reference/android/content/pm/PackageM
any installer, TRUST_NONE (https://developer.android.com/reference/andr
disables optimized installer-enforced checksums, otherwise the list has to 
This value cannot be null.
onChecksumsReadyListener
PackageManager.OnChecksumsReadyListener: called once when th
This value cannot be null.
Throws
PackageManager.NameNotFoundException
(https://developer.android.com/reference/android/content/pm/PackageManager.NameNotFoundException)


Added in API level 33 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
IllegalArgumentException
(https://developer.android.com/reference/java/lang/IllegalArgumentException)
CertificateEncodingException
(https://developer.android.com/reference/java/security/cert/CertificateEncodingException)
resolveActivity
See resolveActivity(Intent,int)
(https://developer.android.com/reference/android/content/pm/PackageManager#resolveActivity(android.c
ontent.Intent,%20int))
.
Parameters
intent
Intent: This value cannot be null.
flags
PackageManager.ResolveInfoFlags: This value cannot be null.
Returns
ResolveInfo
(https://developer.android.com/reference/android/content/pm/ResolveInfo)
This value may be null.
public ResolveInfo (https://developer.android.com/reference/android/content/pm/ResolveInfo) resol
               PackageManager.ResolveInfoFlags (https://developer.android.com/reference/an


Added in API level 1 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
resolveActivity
Determine the best action to perform for a given Intent. This is how Intent.resolveActivity
(https://developer.android.com/reference/android/content/Intent#resolveActivity(android.content.pm.Pack
ageManager))
finds an activity if a class has not been explicitly specified.
Note: if using an implicit Intent (without an explicit ComponentName specified), be sure to
consider whether to set the MATCH_DEFAULT_ONLY
(https://developer.android.com/reference/android/content/pm/PackageManager#MATCH_DEFAULT_ONLY)
only flag. You need to do so to resolve the activity in the same way that
android.content.Context.startActivity(Intent)
(https://developer.android.com/reference/android/content/Context#startActivity(android.content.Intent))
and Intent.resolveActivity(PackageManager)
(https://developer.android.com/reference/android/content/Intent#resolveActivity(android.content.pm.Pack
ageManager))
do.
Use resolveActivity(Intent,ResolveInfoFlags)
(https://developer.android.com/reference/android/content/pm/PackageManager#resolveActivity(android.c
ontent.Intent,%20android.content.pm.PackageManager.ResolveInfoFlags))
when long flags are needed.
Parameters
intent
Intent: An intent containing all of the desired specification (action, data, 
component).
This value cannot be null.
flags
int: Additional option flags to modify the data returned. The most importa
 (https://developer.android.com/reference/android/content/pm/PackageM
public abstract ResolveInfo (https://developer.android.com/reference/android/content/pm/Resolve
               int flags)


Added in API level 33 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
, to limit the resolution to only those activities that support the Intent.CA
 (https://developer.android.com/reference/android/content/Intent#CATEG
Returns
ResolveInfo
(https://developer.android.com/reference/android/content/pm/ResolveInfo)
Returns a ResolveInfo object
containing the final activity inten
that was determined to be the
best action. Returns null if no
matching activity was found. If
multiple matching activities are
found and there is no default se
returns a ResolveInfo object
containing something else, such
as the activity resolver.
resolveContentProvider
See resolveContentProvider(String,int)
(https://developer.android.com/reference/android/content/pm/PackageManager#resolveContentProvider(j
ava.lang.String,%20int))
.
Parameters
authority
String: This value cannot be null.
public ProviderInfo (https://developer.android.com/reference/android/content/pm/ProviderInfo) res
               PackageManager.ComponentInfoFlags (https://developer.android.com/reference/


Added in API level 1 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
flags
PackageManager.ComponentInfoFlags: This value cannot be null.
Returns
ProviderInfo
(https://developer.android.com/reference/android/content/pm/ProviderInfo)
This value may be null.
resolveContentProvider
Find a single content provider by its authority.
Example:
Use resolveContentProvider(String,ComponentInfoFlags)
(https://developer.android.com/reference/android/content/pm/PackageManager#resolveContentProvider(j
ava.lang.String,%20android.content.pm.PackageManager.ComponentInfoFlags))
when long flags are needed.
Parameters
public abstract ProviderInfo (https://developer.android.com/reference/android/content/pm/Provid
               int flags)
Uri uri = Uri.parse("content://com.example.app.provider/table1");
ProviderInfo info = packageManager.resolveContentProvider(uri.getAuthority(), f


Added in API level 1 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
authority
String: The authority of the provider to find.
This value cannot be null.
flags
int: Additional option flags to modify the data returned.
Returns
ProviderInfo
(https://developer.android.com/reference/android/content/pm/ProviderInfo)
A ProviderInfo
 (https://developer.android.com
object containing information a
returns null.
resolveService
Determine the best service to handle for a given Intent. Use
resolveService(Intent,ResolveInfoFlags)
(https://developer.android.com/reference/android/content/pm/PackageManager#resolveService(android.c
ontent.Intent,%20android.content.pm.PackageManager.ResolveInfoFlags))
when long flags are needed.
Parameters
intent
Intent: An intent containing all of the desired specification (action, data,
type, category, and/or component).
This value cannot be null.
public abstract ResolveInfo (https://developer.android.com/reference/android/content/pm/Resolve
               int flags)


Added in API level 33 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
flags
int: Additional option flags to modify the data returned.
Returns
ResolveInfo
(https://developer.android.com/reference/android/content/pm/ResolveInfo)
Returns a ResolveInfo object
containing the final service inten
that was determined to be the
best action. Returns null if no
matching service was found.
resolveService
See resolveService(Intent,int)
(https://developer.android.com/reference/android/content/pm/PackageManager#resolveService(android.c
ontent.Intent,%20int))
.
Parameters
intent
Intent: This value cannot be null.
flags
PackageManager.ResolveInfoFlags: This value cannot be null.
public ResolveInfo (https://developer.android.com/reference/android/content/pm/ResolveInfo) resol
               PackageManager.ResolveInfoFlags (https://developer.android.com/reference/an


Added in API level 26 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Returns
ResolveInfo
(https://developer.android.com/reference/android/content/pm/ResolveInfo)
This value may be null.
setApplicationCategoryHint
Provide a hint of what the ApplicationInfo.category
(https://developer.android.com/reference/android/content/pm/ApplicationInfo#category) value should
be for the given package.
This hint can only be set by the app which installed this package, as determined by
getInstallerPackageName(String)
(https://developer.android.com/reference/android/content/pm/PackageManager#getInstallerPackageNam
e(java.lang.String))
.
Parameters
packageName
String: the package to change the category hint for.
This value cannot be null.
categoryHint
int: the category hint to set.
Value is one of the following:
ApplicationInfo.CATEGORY_UNDEFINED
 (https://developer.android.com/reference/android/content/pm/Applica
public abstract void setApplicationCategoryHint (String (https://developer.android.com/re
               int categoryHint)


Added in API level 1 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
ApplicationInfo.CATEGORY_GAME
 (https://developer.android.com/reference/android/content/pm/Applica
ApplicationInfo.CATEGORY_AUDIO
 (https://developer.android.com/reference/android/content/pm/Applica
ApplicationInfo.CATEGORY_VIDEO
 (https://developer.android.com/reference/android/content/pm/Applica
ApplicationInfo.CATEGORY_IMAGE
 (https://developer.android.com/reference/android/content/pm/Applica
ApplicationInfo.CATEGORY_SOCIAL
 (https://developer.android.com/reference/android/content/pm/Applica
ApplicationInfo.CATEGORY_NEWS
 (https://developer.android.com/reference/android/content/pm/Applica
ApplicationInfo.CATEGORY_MAPS
 (https://developer.android.com/reference/android/content/pm/Applica
ApplicationInfo.CATEGORY_PRODUCTIVITY
 (https://developer.android.com/reference/android/content/pm/Applica
ApplicationInfo.CATEGORY_ACCESSIBILITY
 (https://developer.android.com/reference/android/content/pm/Applica
setApplicationEnabledSetting
Set the enabled setting for an application This setting will override any enabled state which
may have been set by the application in its manifest. It also overrides the enabled state set in
the manifest for any of the application's components. It does not override any enabled state set
by setComponentEnabledSetting(ComponentName, int, int)
public abstract void setApplicationEnabledSetting (String (https://developer.android.com
               int newState, 
               int flags)


Added in API level 30 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
(https://developer.android.com/reference/android/content/pm/PackageManager#setComponentEnabledSe
tting(android.content.ComponentName,%20int,%20int))
for any of the application's components.
Parameters
packageName
String: The package name of the application to enable.
This value cannot be null.
newState
int: The new enabled state for the application.
Value is one of the following:
COMPONENT_ENABLED_STATE_DEFAULT
 (https://developer.android.com/reference/android/content/pm/Packag
COMPONENT_ENABLED_STATE_ENABLED
 (https://developer.android.com/reference/android/content/pm/Packag
COMPONENT_ENABLED_STATE_DISABLED
 (https://developer.android.com/reference/android/content/pm/Packag
COMPONENT_ENABLED_STATE_DISABLED_USER
 (https://developer.android.com/reference/android/content/pm/Packag
COMPONENT_ENABLED_STATE_DISABLED_UNTIL_USED
 (https://developer.android.com/reference/android/content/pm/Packag
flags
int: Optional behavior flags.
Value is either 0 or a combination of the following:
DONT_KILL_APP (https://developer.android.com/reference/android/co
SYNCHRONOUS (https://developer.android.com/reference/android/cont
setAutoRevokeWhitelisted


Marks an application exempt from having its permissions be automatically revoked when the
app is unused for an extended period of time. Only the installer on record that installed the
given package is allowed to call this. Packages start in whitelisted state, and it is the installer's
responsibility to un-whitelist the packages it installs, unless auto-revoking permissions from
that package would cause breakages beyond having to re-request the permission(s).
Note: In retrospect it would have been preferred to use more inclusive terminology when
naming this API. Similar APIs added will refrain from using the term "whitelist".
Parameters
packageName
String: The app for which to set exemption.
This value cannot be null.
whitelisted
boolean: Whether the app should be whitelisted.
Returns
boolean
whether any change took effect.
Throws
SecurityException
(https://developer.android.com/reference/java/lang/SecurityException)
if you you have no access to modify
this.
public boolean setAutoRevokeWhitelisted (String (https://developer.android.com/reference/jav
               boolean whitelisted)


Added in API level 1 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
See also:
isAutoRevokeWhitelisted()
(https://developer.android.com/reference/android/content/pm/PackageManager#isAutoRevokeWhitelisted
())
setComponentEnabledSetting
Set the enabled setting for a package component (activity, receiver, service, provider). This
setting will override any enabled state which may have been set by the component in its
manifest.
Consider using setComponentEnabledSettings(List)
(https://developer.android.com/reference/android/content/pm/PackageManager#setComponentEnabledSe
ttings(java.util.List%3Candroid.content.pm.PackageManager.ComponentEnabledSetting%3E))
if multiple components need to be updated atomically.
Parameters
componentName
ComponentName: The component to enable.
This value cannot be null.
newState
int: The new enabled state for the component.
Value is one of the following:
COMPONENT_ENABLED_STATE_DEFAULT
 (https://developer.android.com/reference/android/content/pm/Packag
COMPONENT_ENABLED_STATE_ENABLED
 (https://developer.android.com/reference/android/content/pm/Packag
public abstract void setComponentEnabledSetting (ComponentName (https://developer.andro
               int newState, 
               int flags)


Added in API level 33 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
COMPONENT_ENABLED_STATE_DISABLED
 (https://developer.android.com/reference/android/content/pm/Packag
COMPONENT_ENABLED_STATE_DISABLED_USER
 (https://developer.android.com/reference/android/content/pm/Packag
COMPONENT_ENABLED_STATE_DISABLED_UNTIL_USED
 (https://developer.android.com/reference/android/content/pm/Packag
flags
int: Optional behavior flags.
Value is either 0 or a combination of the following:
DONT_KILL_APP (https://developer.android.com/reference/android/co
SYNCHRONOUS (https://developer.android.com/reference/android/cont
setComponentEnabledSettings
Set the enabled settings for package components such as activities, receivers, services and
providers. This setting will override any enabled state which may have been set by the
component in its manifest.
This api accepts a list of component changes, and applies them all atomically. The application
can use this api if components have dependencies and need to be updated atomically.
The permission is not required if target components are running under the same uid with the
caller.
Parameters
settings
List: The list of component enabled settings to update. Note that an Ill
Exception (https://developer.android.com/reference/java/lang/IllegalArg
public void setComponentEnabledSettings (List (https://developer.android.com/reference/java/


Added in API level 11 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
thrown if the duplicated component name is in the list or there's a conflict 
 (https://developer.android.com/reference/android/content/pm/PackageM
flag between different components in the same package.
This value cannot be null.
See also:
setComponentEnabledSetting(ComponentName,int,int)
(https://developer.android.com/reference/android/content/pm/PackageManager#setComponentEnabledSe
tting(android.content.ComponentName,%20int,%20int))
setInstallerPackageName
Change the installer associated with a given package. There are limitations on how the installer
package can be changed; in particular:
A SecurityException will be thrown if installerPackageName is not signed with the same
certificate as the calling application.
A SecurityException will be thrown if targetPackage already has an installer package, and
that installer package is not signed with the same certificate as the calling application.
Parameters
targetPackage
String: The installed package whose installer will be changed.
This value cannot be null.
installerPackageName
String: The package name of the new installer. May be null to clear the
association.
public abstract void setInstallerPackageName (String (https://developer.android.com/refere
               String (https://developer.android.com/reference/java/lang/String) installerPack


Added in API level 30 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
Added in API level 26 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
setMimeGroup
Sets MIME group's MIME types. Libraries should use a reverse-DNS prefix followed by a ':'
character and library-specific group name to avoid namespace collisions, e.g.
"com.example:myFeature".
Parameters
mimeGroup
String: MIME group to modify.
This value cannot be null.
mimeTypes
Set: new MIME types contained by MIME group.
This value cannot be null.
Throws
IllegalArgumentException
(https://developer.android.com/reference/java/lang/IllegalArgumentException)
if the MIME group was not
declared in the manifest.
updateInstantAppCookie
public void setMimeGroup (String (https://developer.android.com/reference/java/lang/String) mim
               Set (https://developer.android.com/reference/java/util/Set)<String (https://develope


Updates the instant application cookie for the calling app. Non instant apps and apps that were
instant but were upgraded to normal apps can still access this API. For instant apps this cookie
is cached for some time after uninstall while for normal apps the cookie is deleted after the
app is uninstalled. The cookie is always present while the app is installed. The cookie size is
limited by getInstantAppCookieMaxBytes()
(https://developer.android.com/reference/android/content/pm/PackageManager#getInstantAppCookieMax
Bytes())
. Passing null or an empty array clears the cookie.
Parameters
cookie
byte: The cookie data.
This value may be null.
Throws
IllegalArgumentException
(https://developer.android.com/reference/java/lang/IllegalArgumentException)
if the array exceeds max coo
size.
See also:
isInstantApp()
(https://developer.android.com/reference/android/content/pm/PackageManager#isInstantApp())
isInstantApp(String)
(https://developer.android.com/reference/android/content/pm/PackageManager#isInstantApp(java.lang.St
ring))
getInstantAppCookieMaxBytes()
(https://developer.android.com/reference/android/content/pm/PackageManager#getInstantAppCookieMax
Bytes())
public abstract void updateInstantAppCookie (byte[] cookie)


Added in API level 14 (https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
getInstantAppCookie()
(https://developer.android.com/reference/android/content/pm/PackageManager#getInstantAppCookie())
clearInstantAppCookie()
(https://developer.android.com/reference/android/content/pm/PackageManager#clearInstantAppCookie())
verifyPendingInstall
Allows a package listening to the package verification broadcast
(https://developer.android.com/reference/android/content/Intent#ACTION_PACKAGE_NEEDS_VERIFICATIO
N)
to respond to the package manager. The response must include the verificationCode which
is one of PackageManager.VERIFICATION_ALLOW
(https://developer.android.com/reference/android/content/pm/PackageManager#VERIFICATION_ALLOW)
or PackageManager.VERIFICATION_REJECT
(https://developer.android.com/reference/android/content/pm/PackageManager#VERIFICATION_REJECT).
Parameters
id
int: pending package identifier as passed via the PackageManager.EXT
 (https://developer.android.com/reference/android/content/pm/PackageM
Intent extra.
verificationCode
int: either PackageManager.VERIFICATION_ALLOW
 (https://developer.android.com/reference/android/content/pm/PackageM
PackageManager.VERIFICATION_REJECT
 (https://developer.android.com/reference/android/content/pm/PackageM
public abstract void verifyPendingInstall (int id, 
               int verificationCode)


Throws
SecurityException
(https://developer.android.com/reference/java/lang/SecurityException)
if the caller does not have the
PACKAGE_VERIFICATION_AGENT
permission.
Content and code samples on this page are subject to the licenses described in the Content License
(https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle
and/or its affiliates.
Last updated 2026-06-23 UTC.
