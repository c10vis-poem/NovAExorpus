# PackageManager  _  API reference  _  Android Developers (1)

[API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

# PackageManager
      
       
       
     
   
    
      
        
        
           
      
           
        
      
      

```
  public
  
  
  abstract
  class
  PackageManager
```

```
  
    extends 
```
[Object](https://developer.android.com/reference/java/lang/Object)
  
  
  
```
  
  
  
```

| [java.lang.Object](https://developer.android.com/reference/java/lang/Object) | |
| ↳ | android.content.pm.PackageManager | 

| 
 | 

Class for retrieving various kinds of information related to the application
 packages that are currently installed on the device.
 You can find this class through [Context.getPackageManager](https://developer.android.com/reference/android/content/Context#getPackageManager())

**Note: **If your app targets Android 11 (API level 30) or
 higher, the methods in this class each return a filtered list of apps. Learn more about how to
 [manage package visibility](https://developer.android.com/training/basics/intents/package-visibility).
 

## Summary

| ## Nested classes | |
|---|---|
| ```
        
        
        
        
        class
```
 | Specific flags used for retrieving application info. | 
| ```
        
        
        
        
        class
```
 | The class containing the enabled setting of a package component. | 
| ```
        
        
        
        
        class
```
 | Specific flags used for retrieving component info. | 
| ```
        
        
        
        
        class
```
 | This exception is thrown when a given package, application, or component name cannot be found. | 
| ```
        
        
        
        
        interface
```
 | Listener that gets notified when checksums are available. | 
| ```
        
        
        
        
        class
```
 | Specific flags used for retrieving package info. | 
| ```
        
        
        
        
        class
```
 | A property value set within the manifest. | 
| ```
        
        
        
        
        class
```
 | Specific flags used for retrieving resolve info. | 

| ## Constants | |
|---|---|
| `int` | Certificate input bytes: the input bytes represent an encoded X.509 Certificate which could
 be generated using an  | 
| `int` | Certificate input bytes: the input bytes represent the SHA256 output of an encoded X.509 Certificate. | 
| `int` | Flag for  | 
| `int` | Flag for  | 
| `int` | Flag for  | 
| `int` | Flag for  | 
| `int` | Flag for  | 
| `int` | Flag parameter for  | 
| `int` | Flag parameter for
  | 
|  | Extra field name for the ID of a package pending verification. | 
|  | Extra field name for the result of a verification, either
  | 
|  | Feature for  | 
|  | Feature for  | 
|  | Feature for  | 
|  | Feature for  | 
|  | Feature for  | 
|  | Feature for  | 
|  | Feature for  | 
|  | Feature for  | 
|  | Feature for  | 
|  | Feature for  | 
|  | Feature for  | 
|  | Feature for  | 
|  | Feature for  | 
|  | Feature for  | 
|  | Feature for  | 
|  | Feature for  | 
|  | Feature for  | 
|  | Feature for  | 
|  | Feature for  | 
|  | Feature for  | 
|  | Feature for  | 
|  | Feature for  | 
|  | Feature for  | 
|  | Feature for  | 
|  | Feature for  | 
|  | Feature for  | 
|  | 
 [FEATURE_TELECOM](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_TELECOM)instead. | 
|  | Feature for  | 
|  | Feature for  | 
|  | Feature for  | 
|  | Feature for  | 
|  | Feature for  | 
|  | Feature for  | 
|  | Feature for  | 
|  | Feature for  | 
|  | Feature for  | 
|  | Feature for  | 
|  | Feature for  | 
|  | Feature for  | 
|  | Feature for  | 
|  | Feature for  | 
|  | Feature for  | 
|  | Feature for  | 
|  | Feature for  | 
|  | Feature for  | 
|  | Feature for  | 
|  | Feature for  | 
|  | Feature for  | 
|  | Feature for  | 
|  | Feature for  | 
|  | Feature for  | 
|  | Feature for  | 
|  | Feature for  | 
|  | Feature for  | 
|  | Feature for  | 
|  | Feature for  | 
|  | Feature for  | 
|  | Feature for  | 
|  | Feature for  | 
|  | Feature for  | 
|  | Feature for  | 
|  | Feature for  | 
|  | Feature for  | 
|  | Feature for  | 
|  | Feature for  | 
|  | Feature for  | 
|  | Feature for  | 
|  | Feature for  | 
|  | Feature for  | 
|  | Feature for  | 
|  | Feature for  | 
|  | Feature for  | 
|  | Feature for  | 
|  | Feature for  | 
|  | Feature for  | 
|  | Feature for  | 
|  | Feature for  | 
|  | Feature for  | 
|  | Feature for  | 
|  | Feature for  | 
|  | Feature for  | 
|  | Feature for  | 
|  | Feature for  | 
|  | Feature for  | 
|  | Feature for  | 
|  | Feature for  | 
|  | Feature for  | 
|  | Feature for  | 
|  | Feature for  | 
|  | Feature for  | 
|  | Feature for  | 
|  | Feature for  | 
|  | Feature for  | 
|  | Feature for  | 
|  | Feature for  | 
|  | Feature for  | 
|  | Feature for  | 
|  | Feature for  | 
|  | Feature for  | 
|  | Feature for  | 
|  | Feature for  | 
|  | Feature for  | 
|  | Feature for  | 
|  | Feature for  | 
|  | Feature for  | 
|  | Feature for  | 
|  | Feature for  | 
|  | Feature for  | 
|  | Feature for  | 
|  | Feature for  | 
|  | Feature for  | 
|  | Feature for  | 
|  | Feature for  | 
|  | Feature for  | 
|  | Feature for  | 
|  | Feature for  | 
|  | Feature for  | 
|  | Feature for  | 
|  | Feature for  | 
|  | Feature for  | 
|  | Feature for  | 
|  | Feature for  | 
|  | 
 [FEATURE_LEANBACK](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_LEANBACK)instead. | 
|  | Feature for  | 
|  | Feature for  | 
|  | Feature for  | 
|  | Feature for  | 
|  | Feature for  | 
|  | Feature for  | 
|  | Feature for  | 
|  | Feature for  | 
|  | Feature for  | 
|  | Feature for  | 
|  | 
 [FEATURE_VR_MODE_HIGH_PERFORMANCE](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_VR_MODE_HIGH_PERFORMANCE)instead. | 
|  | Feature for  | 
|  | Feature for  | 
|  | Feature for  | 
|  | Feature for  | 
|  | Feature for  | 
|  | Feature for  | 
|  | Feature for  | 
|  | Feature for  | 
|  | Feature for  | 
|  | Feature for  | 
|  | Feature for  | 
|  | Feature for  | 
|  | Feature for  | 
|  | Feature for  | 
| `int` | Permission whitelist flag: permissions whitelisted by the installer. | 
| `int` | Permission whitelist flag: permissions whitelisted by the system. | 
| `int` | Permission whitelist flag: permissions whitelisted by the system when upgrading from an OS version where the permission was not restricted to an OS version where the permission is restricted. | 
| `int` | 
 | 
| `int` | 
 [GET_ATTRIBUTIONS_LONG](https://developer.android.com/reference/android/content/pm/PackageManager#GET_ATTRIBUTIONS_LONG)to avoid unintended sign extension. Operations
 with this flag may cause unintended results and potential[RuntimeException](https://developer.android.com/reference/java/lang/RuntimeException). | 
| `long` | 
 | 
| `int` | 
 | 
| `int` | 
 [MATCH_DISABLED_COMPONENTS](https://developer.android.com/reference/android/content/pm/PackageManager#MATCH_DISABLED_COMPONENTS) | 
| `int` | 
 [MATCH_DISABLED_UNTIL_USED_COMPONENTS](https://developer.android.com/reference/android/content/pm/PackageManager#MATCH_DISABLED_UNTIL_USED_COMPONENTS). | 
| `int` | 
 | 
| `int` | 
 | 
| `int` | 
 [IntentFilter](https://developer.android.com/reference/android/content/IntentFilter)s for the package. | 
| `int` | 
 | 
| `int` | 
 | 
| `int` | 
 | 
| `int` | 
 | 
| `int` | 
 | 
| `int` | 
 | 
| `int` | 
 | 
| `int` | 
 | 
| `int` | 
 | 
| `int` | 
 [MATCH_UNINSTALLED_PACKAGES](https://developer.android.com/reference/android/content/pm/PackageManager#MATCH_UNINSTALLED_PACKAGES) | 
| `int` | 
 | 
| `int` | Code indicating that this package was installed as part of restoring from another device. | 
| `int` | Code indicating that this package was installed as part of device setup. | 
| `int` | Code indicating that this package was installed due to enterprise policy. | 
| `int` | Code indicating that the reason for installing this package is unknown. | 
| `int` | Code indicating that the package installation was initiated by the user. | 
| `int` | Installation scenario indicating a bulk operation with the desired result of a fully optimized application. | 
| `int` | Installation scenario indicating a bulk operation that prioritizes minimal system health impact over application optimization. | 
| `int` | A value to indicate the lack of CUJ information, disabling all installation scenario logic. | 
| `int` | Installation scenario providing the fastest "install button to launch" experience possible. | 
| `int` | Querying flag: if set and if the platform is doing any filtering of the results, then the filtering will not happen. | 
| `int` | 
 | 
| `long` | Flag parameter to also retrieve some information about archived packages. | 
| `int` | Resolution and querying flag: if set, only filters that support the
  | 
| `int` | Querying flag: automatically match components based on their Direct Boot awareness and the current user state. | 
| `int` | Querying flag: match components which are direct boot  | 
| `int` | Querying flag: match components which are direct boot  | 
| `int` | 
 | 
| `int` | 
 | 
| `int` | Querying flag: include only components from applications that are marked
 with  | 
| `int` | Flag parameter to retrieve some information about all applications (even uninstalled ones) which have data directories. | 
| `long` | Can be used as the  | 
| `int` | Permission check result: this is returned by  | 
| `int` | Permission check result: this is returned by  | 
|  | Application level  | 
|  | <application> level  | 
|  | Service level  | 
|  | Service level  | 
|  | <application> level  | 
|  | <service> level  | 
|  | <application> level  | 
| `int` | Signature check result: this is returned by  | 
| `int` | Signature check result: this is returned by  | 
| `int` | Signature check result: this is returned by  | 
| `int` | Signature check result: this is returned by  | 
| `int` | Signature check result: this is returned by  | 
| `int` | Signature check result: this is returned by  | 
| `int` | Flag parameter for
  | 
| `int` | Used as the  | 
| `int` | Used as the  | 
| `int` | Constant for specifying the highest installed package version code. | 

| ## Fields | |
|---|---|
| ```
    public
    static
    final
    
```
 | Trust any Installer to provide checksums for the package. | 
| ```
    public
    static
    final
    
```
 | Don't trust any Installer to provide checksums for the package. | 

| ## Public constructors | |
|---|---|
| ```
      
```
 [Context.getPackageManager](https://developer.android.com/reference/android/content/Context#getPackageManager()) | |

| ## Public methods | |
|---|---|
| ```
        abstract
        
        
        
        
        void
```
 | ```
      
```
 [resolveActivity(Intent, ResolveInfoFlags)](https://developer.android.com/reference/android/content/pm/PackageManager#resolveActivity(android.content.Intent,%20android.content.pm.PackageManager.ResolveInfoFlags))or[queryIntentActivities(Intent, ResolveInfoFlags)](https://developer.android.com/reference/android/content/pm/PackageManager#queryIntentActivities(android.content.Intent,%20android.content.pm.PackageManager.ResolveInfoFlags)). To configure
 an app to be responsible for a particular role and to check current role
 holders, see[RoleManager](https://developer.android.com/reference/android/app/role/RoleManager). | 
| ```
        abstract
        
        
        
        
        boolean
```
 | ```
      
```
Add a new dynamic permission to the system. | 
| ```
        abstract
        
        
        
        
        boolean
```
 | ```
      
```
Like  | 
| ```
        abstract
        
        
        
        
        void
```
 | ```
      
```
 [resolveActivity(Intent, ResolveInfoFlags)](https://developer.android.com/reference/android/content/pm/PackageManager#resolveActivity(android.content.Intent,%20android.content.pm.PackageManager.ResolveInfoFlags))or[queryIntentActivities(Intent, ResolveInfoFlags)](https://developer.android.com/reference/android/content/pm/PackageManager#queryIntentActivities(android.content.Intent,%20android.content.pm.PackageManager.ResolveInfoFlags)). To configure
 an app to be responsible for a particular role and to check current role
 holders, see[RoleManager](https://developer.android.com/reference/android/app/role/RoleManager). | 
| ```
        
        
        
        
        
        boolean
```
 | ```
      
```
Adds a whitelisted restricted permission for an app. | 
| ```
        
        
        
        
        
        boolean
```
 | ```
      
```
Returns  | 
| ```
        
        
        
        
        
        boolean[]
```
 | ```
      
```
Same as  | 
| ```
        abstract
        
        
        
        
        boolean
```
 | ```
      
```
Checks whether the calling package is allowed to request package installs through package installer. | 
| ```
        abstract
        
        
        
        
        
```
 | ```
      
```
Map from a packages canonical name to the current name in use on the device. | 
| ```
        abstract
        
        
        
        
        int
```
 | ```
      
```
Check whether a particular package has been granted a particular permission. | 
| ```
        abstract
        
        
        
        
        int
```
 | ```
      
```
Compare the signatures of two packages to determine if the same signature appears in both of them. | 
| ```
        abstract
        
        
        
        
        int
```
 | ```
      
```
Like  | 
| ```
        abstract
        
        
        
        
        void
```
 | ```
      
```
Clears the instant application cookie for the calling app. | 
| ```
        abstract
        
        
        
        
        void
```
 | ```
      
```
 [resolveActivity(Intent, ResolveInfoFlags)](https://developer.android.com/reference/android/content/pm/PackageManager#resolveActivity(android.content.Intent,%20android.content.pm.PackageManager.ResolveInfoFlags))or[queryIntentActivities(Intent, ResolveInfoFlags)](https://developer.android.com/reference/android/content/pm/PackageManager#queryIntentActivities(android.content.Intent,%20android.content.pm.PackageManager.ResolveInfoFlags)). To configure
 an app to be responsible for a particular role and to check current role
 holders, see[RoleManager](https://developer.android.com/reference/android/app/role/RoleManager). | 
| ```
        abstract
        
        
        
        
        
```
 | ```
      
```
Map from the current package names in use on the device to whatever the current canonical name of that package is. | 
| ```
        abstract
        
        
        
        
        void
```
 | ```
      
```
Allows a package listening to the
  | 
| ```
        abstract
        
        
        
        
        
```
 | ```
      
```
Retrieve the banner associated with an activity. | 
| ```
        abstract
        
        
        
        
        
```
 | ```
      
```
Retrieve the banner associated with an Intent. | 
| ```
        abstract
        
        
        
        
        
```
 | ```
      
```
Retrieve the icon associated with an Intent. | 
| ```
        abstract
        
        
        
        
        
```
 | ```
      
```
Retrieve the icon associated with an activity. | 
| ```
        abstract
        
        
        
        
        
```
 | ```
      
```
Retrieve all of the information we know about a particular activity class. | 
| ```
        
        
        
        
        
        
```
 | ```
      
```
 | 
| ```
        abstract
        
        
        
        
        
```
 | ```
      
```
Retrieve the logo associated with an Intent. | 
| ```
        abstract
        
        
        
        
        
```
 | ```
      
```
Retrieve the logo associated with an activity. | 
| ```
        abstract
        
        
        
        
        
```
 | ```
      
```
Retrieve all of the known permission groups in the system. | 
| ```
        
        
        
        
        
        int
```
 | ```
      
```
Maps a Private Compute Core (PCC) UID to its corresponding application UID. | 
| ```
        abstract
        
        
        
        
        
```
 | ```
      
```
Retrieve the banner associated with an application. | 
| ```
        abstract
        
        
        
        
        
```
 | ```
      
```
Retrieve the banner associated with an application. | 
| ```
        abstract
        
        
        
        
        int
```
 | ```
      
```
Return the enabled setting for an application. | 
| ```
        abstract
        
        
        
        
        
```
 | ```
      
```
Retrieve the icon associated with an application. | 
| ```
        abstract
        
        
        
        
        
```
 | ```
      
```
Retrieve the icon associated with an application. | 
| ```
        
        
        
        
        
        
```
 | ```
      
```
 | 
| ```
        abstract
        
        
        
        
        
```
 | ```
      
```
Retrieve all of the information we know about a particular package/application. | 
| ```
        abstract
        
        
        
        
        
```
 | ```
      
```
Return the label to use for this application. | 
| ```
        abstract
        
        
        
        
        
```
 | ```
      
```
Retrieve the logo associated with an application. | 
| ```
        abstract
        
        
        
        
        
```
 | ```
      
```
Retrieve the logo associated with an application. | 
| ```
        
        
        
        
        
        
```
 | ```
      
```
Return archived package info for the package or null if the package is not installed. | 
| ```
        
        
        
        
        
        
```
 | ```
      
```
Gets the localized label that corresponds to the option in settings for granting background access. | 
| ```
        abstract
        
        
        
        
        
```
 | ```
      
```
Returns the names of the packages that have been changed [eg. | 
| ```
        abstract
        
        
        
        
        int
```
 | ```
      
```
Return the enabled setting for a package component (activity, receiver, service, provider). | 
| ```
        abstract
        
        
        
        
        
```
 | ```
      
```
Return the generic icon for an activity that is used when no specific icon is defined. | 
| ```
        abstract
        
        
        
        
        
```
 | ```
      
```
Retrieve an image from a package. | 
| ```
        
        
        
        
        
        void
```
 | ```
      
```
Get the platform-defined permission group of a particular permission, if the permission is a platform-defined permission. | 
| ```
        
        
        
        
        
        
```
 | ```
      
```
Retrieves information about how a package was installed or updated. | 
| ```
        abstract
        
        
        
        
        
```
 | ```
      
```
Return a List of all application packages that are installed for the current user. | 
| ```
        
        
        
        
        
        
```
 | ```
      
```
 | 
| ```
        
        
        
        
        
        
```
 | ```
      
```
Return a List of all modules that are installed. | 
| ```
        abstract
        
        
        
        
        
```
 | ```
      
```
Return a List of all packages that are installed for the current user. | 
| ```
        
        
        
        
        
        
```
 | ```
      
```
 | 
| ```
        abstract
        
        
        
        
        
```
 | ```
      
```
 [getInstallSourceInfo(String)](https://developer.android.com/reference/android/content/pm/PackageManager#getInstallSourceInfo(java.lang.String))instead | 
| ```
        abstract
        
        
        
        
        byte[]
```
 | ```
      
```
Gets the instant application cookie for this app. | 
| ```
        abstract
        
        
        
        
        int
```
 | ```
      
```
Gets the maximum size in bytes of the cookie data an instant app can store on the device. | 
| ```
        abstract
        
        
        
        
        
```
 | ```
      
```
Retrieve all of the information we know about a particular instrumentation class. | 
| ```
        abstract
        
        
        
        
        
```
 | ```
      
```
Returns a "good" intent to launch a front-door activity in a package. | 
| ```
        
        
        
        
        
        
```
 | ```
      
```
Returns an  | 
| ```
        abstract
        
        
        
        
        
```
 | ```
      
```
Return a "good" intent to launch a front-door Leanback activity in a package, for use for example to implement an "open" button when browsing through packages. | 
| ```
        
        
        
        
        
        
```
 | ```
      
```
Gets all MIME types contained by MIME group. | 
| ```
        
        
        
        
        
        
```
 | ```
      
```
Retrieve information for a particular module. | 
| ```
        abstract
        
        
        
        
        
```
 | ```
      
```
Retrieve the official name associated with a uid. | 
| ```
        
        
        
        
        
        
```
 | ```
      
```
Retrieve overall information about an application package defined in a
 package archive file
 Use  | 
| ```
        
        
        
        
        
        
```
 | ```
      
```
 | 
| ```
        abstract
        
        
        
        
        int[]
```
 | ```
      
```
Return an array of all of the POSIX secondary group IDs that have been assigned to the given package. | 
| ```
        abstract
        
        
        
        
        int[]
```
 | ```
      
```
Return an array of all of the POSIX secondary group IDs that have been assigned to the given package. | 
| ```
        
        
        
        
        
        int[]
```
 | ```
      
```
 | 
| ```
        abstract
        
        
        
        
        
```
 | ```
      
```
Retrieve overall information about an application package that is installed on the system. | 
| ```
        
        
        
        
        
        
```
 | ```
      
```
 | 
| ```
        
        
        
        
        
        
```
 | ```
      
```
 | 
| ```
        abstract
        
        
        
        
        
```
 | ```
      
```
Retrieve overall information about an application package that is installed on the system. | 
| ```
        abstract
        
        
        
        
        
```
 | ```
      
```
Return interface that offers the ability to install, upgrade, and remove applications on the device. | 
| ```
        
        
        
        
        
        int
```
 | ```
      
```
 | 
| ```
        abstract
        
        
        
        
        int
```
 | ```
      
```
Return the UID associated with the given package name. | 
| ```
        abstract
        
        
        
        
        
```
 | ```
      
```
Retrieve the names of all packages that are associated with a particular user id. | 
| ```
        abstract
        
        
        
        
        
```
 | ```
      
```
Return a List of all installed packages that are currently holding any of the given permissions. | 
| ```
        
        
        
        
        
        
```
 | ```
      
```
 | 
| ```
        abstract
        
        
        
        
        
```
 | ```
      
```
Retrieve all of the information we know about a particular group of permissions. | 
| ```
        abstract
        
        
        
        
        
```
 | ```
      
```
Retrieve all of the information we know about a particular permission. | 
| ```
        
        
        
        
        
        void
```
 | ```
      
```
Get the platform-defined permissions which belong to a particular permission group. | 
| ```
        abstract
        
        
        
        
        int
```
 | ```
      
```
 [resolveActivity(Intent, ResolveInfoFlags)](https://developer.android.com/reference/android/content/pm/PackageManager#resolveActivity(android.content.Intent,%20android.content.pm.PackageManager.ResolveInfoFlags))or[queryIntentActivities(Intent, ResolveInfoFlags)](https://developer.android.com/reference/android/content/pm/PackageManager#queryIntentActivities(android.content.Intent,%20android.content.pm.PackageManager.ResolveInfoFlags)). To configure
 an app to be responsible for a particular role and to check current role
 holders, see[RoleManager](https://developer.android.com/reference/android/app/role/RoleManager). | 
| ```
        abstract
        
        
        
        
        
```
 | ```
      
```
 [resolveActivity(Intent, ResolveInfoFlags)](https://developer.android.com/reference/android/content/pm/PackageManager#resolveActivity(android.content.Intent,%20android.content.pm.PackageManager.ResolveInfoFlags))or[queryIntentActivities(Intent, ResolveInfoFlags)](https://developer.android.com/reference/android/content/pm/PackageManager#queryIntentActivities(android.content.Intent,%20android.content.pm.PackageManager.ResolveInfoFlags)). To configure
 an app to be responsible for a particular role and to check current role
 holders, see[RoleManager](https://developer.android.com/reference/android/app/role/RoleManager). | 
| ```
        
        
        
        
        
        
```
 | ```
      
```
Returns the property defined in the given package's <application> tag. | 
| ```
        
        
        
        
        
        
```
 | ```
      
```
Returns the property defined in the given component declaration. | 
| ```
        abstract
        
        
        
        
        
```
 | ```
      
```
Retrieve all of the information we know about a particular content provider class. | 
| ```
        
        
        
        
        
        
```
 | ```
      
```
 | 
| ```
        abstract
        
        
        
        
        
```
 | ```
      
```
Retrieve all of the information we know about a particular receiver class. | 
| ```
        
        
        
        
        
        
```
 | ```
      
```
 | 
| ```
        abstract
        
        
        
        
        
```
 | ```
      
```
Retrieve the resources associated with an activity. | 
| ```
        abstract
        
        
        
        
        
```
 | ```
      
```
Retrieve the resources for an application. | 
| ```
        abstract
        
        
        
        
        
```
 | ```
      
```
Retrieve the resources associated with an application. | 
| ```
        
        
        
        
        
        
```
 | ```
      
```
Retrieve the resources for an application for the provided configuration. | 
| ```
        
        
        
        
        
        
```
 | ```
      
```
 | 
| ```
        abstract
        
        
        
        
        
```
 | ```
      
```
Retrieve all of the information we know about a particular service class. | 
| ```
        
        
        
        
        
        
```
 | ```
      
```
 | 
| ```
        abstract
        
        
        
        
        
```
 | ```
      
```
Get a list of shared libraries on the device. | 
| ```
        
        
        
        
        
        
```
 | ```
      
```
Returns a  | 
| ```
        
        
        
        
        
        boolean
```
 | ```
      
```
Return whether a synthetic app details activity will be generated if the app has no enabled launcher activity. | 
| ```
        abstract
        
        
        
        
        
```
 | ```
      
```
Get a list of features that are available on the system. | 
| ```
        abstract
        
        
        
        
        
```
 | ```
      
```
Get a list of shared libraries that are available on the system. | 
| ```
        
        
        
        
        
        int
```
 | ```
      
```
 | 
| ```
        abstract
        
        
        
        
        
```
 | ```
      
```
Retrieve text from a package. | 
| ```
        abstract
        
        
        
        
        
```
 | ```
      
```
If the target user is a managed profile of the calling user or the caller is itself a managed profile, then this returns a badged copy of the given drawable allowing the user to distinguish it from the original drawable. | 
| ```
        abstract
        
        
        
        
        
```
 | ```
      
```
If the target user is a managed profile, then this returns a badged copy of the given icon to be able to distinguish it from the original icon. | 
| ```
        abstract
        
        
        
        
        
```
 | ```
      
```
If the target user is a managed profile of the calling user or the caller is itself a managed profile, then this returns a copy of the label with badging for accessibility services like talkback. | 
| ```
        
        
        static
        
        
        
```
 | ```
      
```
Verifies and returns the
  | 
| ```
        
        
        
        
        
        
```
 | ```
      
```
Gets the restricted permissions that have been whitelisted and the app is allowed to have them granted in their full form. | 
| ```
        abstract
        
        
        
        
        
```
 | ```
      
```
Retrieve an XML file from a package. | 
| ```
        
        
        
        
        
        boolean
```
 | ```
      
```
Searches the set of signing certificates by which the package(s) for the given uid has proven to have been signed. | 
| ```
        
        
        
        
        
        boolean
```
 | ```
      
```
Searches the set of signing certificates by which the given package has proven to have been signed. | 
| ```
        abstract
        
        
        
        
        boolean
```
 | ```
      
```
Check whether the given feature name is one of the available features as
 returned by  | 
| ```
        abstract
        
        
        
        
        boolean
```
 | ```
      
```
Check whether the given feature name and version is one of the available
 features as returned by  | 
| ```
        
        
        
        
        
        boolean
```
 | ```
      
```
Returns true if an app is archivable. | 
| ```
        
        
        
        
        
        boolean
```
 | ```
      
```
Checks whether an application is exempt from having its permissions be automatically revoked when the app is unused for an extended period of time. | 
| ```
        
        
        
        
        
        boolean
```
 | ```
      
```
  | 
| ```
        
        
        
        
        
        boolean
```
 | ```
      
```
Returns if the provided drawable represents the default activity icon provided by the system. | 
| ```
        
        
        
        
        
        boolean
```
 | ```
      
```
Returns true if the device is upgrading, such as first boot after OTA. | 
| ```
        abstract
        
        
        
        
        boolean
```
 | ```
      
```
Gets whether this application is an instant app. | 
| ```
        abstract
        
        
        
        
        boolean
```
 | ```
      
```
Gets whether the given package is an instant app. | 
| ```
        
        
        
        
        
        boolean
```
 | ```
      
```
Query if an app is currently stopped. | 
| ```
        
        
        
        
        
        boolean
```
 | ```
      
```
Query if an app is currently suspended. | 
| ```
        
        
        
        
        
        boolean
```
 | ```
      
```
Apps can query this to know if they have been suspended. | 
| ```
        abstract
        
        
        
        
        boolean
```
 | ```
      
```
Checks whether a particular permissions has been revoked for a package by policy. | 
| ```
        abstract
        
        
        
        
        boolean
```
 | ```
      
```
Return whether the device has been booted into safe mode. | 
| ```
        
        
        
        
        <T>
        T
```
 | ```
      
```
Retrieve AndroidManifest.xml information for the given application apk file. | 
| ```
        
        
        
        
        <T>
        T
```
 | ```
      
```
Similar to  | 
| ```
        
        
        
        
        
        
```
 | ```
      
```
Returns the property definition for all <activity> and <activity-alias> tags. | 
| ```
        
        
        
        
        
        
```
 | ```
      
```
Returns the property definition for all <application> tags. | 
| ```
        
        
        
        
        
        
```
 | ```
      
```
 | 
| ```
        abstract
        
        
        
        
        
```
 | ```
      
```
Retrieve all receivers that can handle a broadcast of the given intent. | 
| ```
        abstract
        
        
        
        
        
```
 | ```
      
```
Retrieve content provider information. | 
| ```
        
        
        
        
        
        
```
 | ```
      
```
 | 
| ```
        abstract
        
        
        
        
        
```
 | ```
      
```
Retrieve information about available instrumentation code. | 
| ```
        
        
        
        
        
        
```
 | ```
      
```
 | 
| ```
        abstract
        
        
        
        
        
```
 | ```
      
```
Retrieve all activities that can be performed for the given intent. | 
| ```
        abstract
        
        
        
        
        
```
 | ```
      
```
Retrieve a set of activities that should be presented to the user as similar options. | 
| ```
        
        
        
        
        
        
```
 | ```
      
```
See  | 
| ```
        
        
        
        
        
        
```
 | ```
      
```
 | 
| ```
        abstract
        
        
        
        
        
```
 | ```
      
```
Retrieve all providers that can match the given intent. | 
| ```
        abstract
        
        
        
        
        
```
 | ```
      
```
Retrieve all services that can match the given intent. | 
| ```
        
        
        
        
        
        
```
 | ```
      
```
 | 
| ```
        abstract
        
        
        
        
        
```
 | ```
      
```
Query for all of the permissions associated with a particular group. | 
| ```
        
        
        
        
        
        
```
 | ```
      
```
Returns the property definition for all <provider> tags. | 
| ```
        
        
        
        
        
        
```
 | ```
      
```
Returns the property definition for all <receiver> tags. | 
| ```
        
        
        
        
        
        
```
 | ```
      
```
Returns the property definition for all <service> tags. | 
| ```
        
        
        
        
        
        void
```
 | ```
      
```
Attempt to relinquish the update ownership of the given package. | 
| ```
        abstract
        
        
        
        
        void
```
 | ```
      
```
 [resolveActivity(Intent, ResolveInfoFlags)](https://developer.android.com/reference/android/content/pm/PackageManager#resolveActivity(android.content.Intent,%20android.content.pm.PackageManager.ResolveInfoFlags))or[queryIntentActivities(Intent, ResolveInfoFlags)](https://developer.android.com/reference/android/content/pm/PackageManager#queryIntentActivities(android.content.Intent,%20android.content.pm.PackageManager.ResolveInfoFlags)). To configure
 an app to be responsible for a particular role and to check current role
 holders, see[RoleManager](https://developer.android.com/reference/android/app/role/RoleManager). | 
| ```
        abstract
        
        
        
        
        void
```
 | ```
      
```
Removes a permission that was previously added with
  | 
| ```
        
        
        
        
        
        boolean
```
 | ```
      
```
Removes a whitelisted restricted permission for an app. | 
| ```
        
        
        
        
        
        void
```
 | ```
      
```
Requests the checksums for APKs within a package. | 
| ```
        
        
        
        
        
        
```
 | ```
      
```
 | 
| ```
        abstract
        
        
        
        
        
```
 | ```
      
```
Determine the best action to perform for a given Intent. | 
| ```
        
        
        
        
        
        
```
 | ```
      
```
 | 
| ```
        abstract
        
        
        
        
        
```
 | ```
      
```
Find a single content provider by its authority. | 
| ```
        abstract
        
        
        
        
        
```
 | ```
      
```
Determine the best service to handle for a given Intent. | 
| ```
        
        
        
        
        
        
```
 | ```
      
```
 | 
| ```
        abstract
        
        
        
        
        void
```
 | ```
      
```
Provide a hint of what the  | 
| ```
        abstract
        
        
        
        
        void
```
 | ```
      
```
Set the enabled setting for an application This setting will override any enabled state which may have been set by the application in its manifest. | 
| ```
        
        
        
        
        
        boolean
```
 | ```
      
```
Marks an application exempt from having its permissions be automatically revoked when the app is unused for an extended period of time. | 
| ```
        abstract
        
        
        
        
        void
```
 | ```
      
```
Set the enabled setting for a package component (activity, receiver, service, provider). | 
| ```
        
        
        
        
        
        void
```
 | ```
      
```
Set the enabled settings for package components such as activities, receivers, services and providers. | 
| ```
        abstract
        
        
        
        
        void
```
 | ```
      
```
Change the installer associated with a given package. | 
| ```
        
        
        
        
        
        void
```
 | ```
      
```
Sets MIME group's MIME types. | 
| ```
        abstract
        
        
        
        
        void
```
 | ```
      
```
Updates the instant application cookie for the calling app. | 
| ```
        abstract
        
        
        
        
        void
```
 | ```
      
```
Allows a package listening to the
  | 

| ## Inherited methods | |||||||||||||||||||||||
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 
 | |||||||||||||||||||||||

## Constants

### CERT_INPUT_RAW_X509   

    [API level 28](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final int CERT_INPUT_RAW_X509

Certificate input bytes: the input bytes represent an encoded X.509 Certificate which could
 be generated using an `CertificateFactory`

Constant Value: 0 (0x00000000)

### CERT_INPUT_SHA256  

    [API level 28](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final int CERT_INPUT_SHA256

Certificate input bytes: the input bytes represent the SHA256 output of an encoded X.509 Certificate.

Constant Value: 1 (0x00000001)

### COMPONENT_ENABLED_STATE_DEFAULT   

    [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final int COMPONENT_ENABLED_STATE_DEFAULT

Flag for [setApplicationEnabledSetting(String,int,int)](https://developer.android.com/reference/android/content/pm/PackageManager#setApplicationEnabledSetting(java.lang.String,%20int,%20int))[setComponentEnabledSetting(ComponentName,int,int)](https://developer.android.com/reference/android/content/pm/PackageManager#setComponentEnabledSetting(android.content.ComponentName,%20int,%20int))

Explicitly setting the component state to this value restores it's enabled state to whatever is set in the manifest.

Constant Value: 0 (0x00000000)

### COMPONENT_ENABLED_STATE_DISABLED   

    [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final int COMPONENT_ENABLED_STATE_DISABLED

Flag for [setApplicationEnabledSetting(String,int,int)](https://developer.android.com/reference/android/content/pm/PackageManager#setApplicationEnabledSetting(java.lang.String,%20int,%20int))[setComponentEnabledSetting(ComponentName,int,int)](https://developer.android.com/reference/android/content/pm/PackageManager#setComponentEnabledSetting(android.content.ComponentName,%20int,%20int))

Constant Value: 2 (0x00000002)

### COMPONENT_ENABLED_STATE_DISABLED_UNTIL_USED     

    [API level 18](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final int COMPONENT_ENABLED_STATE_DISABLED_UNTIL_USED

Flag for [setApplicationEnabledSetting(String,int,int)](https://developer.android.com/reference/android/content/pm/PackageManager#setApplicationEnabledSetting(java.lang.String,%20int,%20int))[GET_DISABLED_UNTIL_USED_COMPONENTS](https://developer.android.com/reference/android/content/pm/PackageManager#GET_DISABLED_UNTIL_USED_COMPONENTS)**can not** be used with
 [setComponentEnabledSetting(ComponentName,int,int)](https://developer.android.com/reference/android/content/pm/PackageManager#setComponentEnabledSetting(android.content.ComponentName,%20int,%20int))

Constant Value: 4 (0x00000004)

### COMPONENT_ENABLED_STATE_DISABLED_USER    

    [API level 14](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final int COMPONENT_ENABLED_STATE_DISABLED_USER

Flag for [setApplicationEnabledSetting(String,int,int)](https://developer.android.com/reference/android/content/pm/PackageManager#setApplicationEnabledSetting(java.lang.String,%20int,%20int))**cannot** be used with
 [setComponentEnabledSetting(ComponentName,int,int)](https://developer.android.com/reference/android/content/pm/PackageManager#setComponentEnabledSetting(android.content.ComponentName,%20int,%20int))

Constant Value: 3 (0x00000003)

### COMPONENT_ENABLED_STATE_ENABLED   

    [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final int COMPONENT_ENABLED_STATE_ENABLED

Flag for [setApplicationEnabledSetting(String,int,int)](https://developer.android.com/reference/android/content/pm/PackageManager#setApplicationEnabledSetting(java.lang.String,%20int,%20int))[setComponentEnabledSetting(ComponentName,int,int)](https://developer.android.com/reference/android/content/pm/PackageManager#setComponentEnabledSetting(android.content.ComponentName,%20int,%20int))

Constant Value: 1 (0x00000001)

### DELETE_ARCHIVE 

    [API level 35](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final int DELETE_ARCHIVE

Flag parameter for [PackageInstaller.uninstall(VersionedPackage,int,IntentSender)](https://developer.android.com/reference/android/content/pm/PackageInstaller#uninstall(android.content.pm.VersionedPackage,%20int,%20android.content.IntentSender))[PackageInstaller.requestArchive](https://developer.android.com/reference/android/content/pm/PackageInstaller#requestArchive(java.lang.String,%20android.content.IntentSender))

Constant Value: 16 (0x00000010)

### DONT_KILL_APP  

    [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final int DONT_KILL_APP

Flag parameter for
 [setComponentEnabledSetting(android.content.ComponentName, int, int)](https://developer.android.com/reference/android/content/pm/PackageManager#setComponentEnabledSetting(android.content.ComponentName,%20int,%20int))

Constant Value: 1 (0x00000001)

### EXTRA_VERIFICATION_ID  

    [API level 14](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final[String](https://developer.android.com/reference/java/lang/String)EXTRA_VERIFICATION_ID

Extra field name for the ID of a package pending verification. Passed to
 a package verifier and is used to call back to
 [PackageManager.verifyPendingInstall(int,int)](https://developer.android.com/reference/android/content/pm/PackageManager#verifyPendingInstall(int,%20int))

Constant Value: "android.content.pm.extra.VERIFICATION_ID"

### EXTRA_VERIFICATION_RESULT  

    [API level 17](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final[String](https://developer.android.com/reference/java/lang/String)EXTRA_VERIFICATION_RESULT

Extra field name for the result of a verification, either
 [VERIFICATION_ALLOW](https://developer.android.com/reference/android/content/pm/PackageManager#VERIFICATION_ALLOW)[VERIFICATION_REJECT](https://developer.android.com/reference/android/content/pm/PackageManager#VERIFICATION_REJECT)

Constant Value: "android.content.pm.extra.VERIFICATION_RESULT"

### FEATURE_ACTIVITIES_ON_SECONDARY_DISPLAYS    

    [API level 26](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final[String](https://developer.android.com/reference/java/lang/String)FEATURE_ACTIVITIES_ON_SECONDARY_DISPLAYS

Feature for [getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures())[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.lang.String))

Constant Value: "android.software.activities_on_secondary_displays"

### FEATURE_APP_WIDGETS  

    [API level 18](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final[String](https://developer.android.com/reference/java/lang/String)FEATURE_APP_WIDGETS

Feature for [getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures())[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.lang.String))

Constant Value: "android.software.app_widgets"

### FEATURE_AUDIO_LOW_LATENCY   

    [API level 9](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final[String](https://developer.android.com/reference/java/lang/String)FEATURE_AUDIO_LOW_LATENCY

Feature for [getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures())[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.lang.String))

Constant Value: "android.hardware.audio.low_latency"

### FEATURE_AUDIO_OUTPUT  

    [API level 21](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final[String](https://developer.android.com/reference/java/lang/String)FEATURE_AUDIO_OUTPUT

Feature for [getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures())[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.lang.String))[section 7.8 Audio](https://source.android.com/compatibility/android-cdd#7_8_audio).

Constant Value: "android.hardware.audio.output"

### FEATURE_AUDIO_PRO  

    [API level 23](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final[String](https://developer.android.com/reference/java/lang/String)FEATURE_AUDIO_PRO

Feature for [getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures())[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.lang.String))

Constant Value: "android.hardware.audio.pro"

### FEATURE_AUDIO_SPATIAL_HEADTRACKING_LOW_LATENCY     

    [API level 36](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final[String](https://developer.android.com/reference/java/lang/String)FEATURE_AUDIO_SPATIAL_HEADTRACKING_LOW_LATENCY

Feature for [getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures())[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.lang.String))

Constant Value: "android.hardware.audio.spatial.headtracking.low_latency"

### FEATURE_AUTOFILL 

    [API level 26](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final[String](https://developer.android.com/reference/java/lang/String)FEATURE_AUTOFILL

Feature for [getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures())[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.lang.String))[autofill
 providers](https://developer.android.com/reference/android/service/autofill/AutofillService)

Constant Value: "android.software.autofill"

### FEATURE_AUTOMOTIVE 

    [API level 23](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final[String](https://developer.android.com/reference/java/lang/String)FEATURE_AUTOMOTIVE

Feature for [getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures())[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.lang.String))

Constant Value: "android.hardware.type.automotive"

### FEATURE_BACKUP 

    [API level 20](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final[String](https://developer.android.com/reference/java/lang/String)FEATURE_BACKUP

Feature for [getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures())[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.lang.String))

Constant Value: "android.software.backup"

### FEATURE_BLUETOOTH 

    [API level 8](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final[String](https://developer.android.com/reference/java/lang/String)FEATURE_BLUETOOTH

Feature for [getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures())[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.lang.String))

Constant Value: "android.hardware.bluetooth"

### FEATURE_BLUETOOTH_LE  

    [API level 18](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final[String](https://developer.android.com/reference/java/lang/String)FEATURE_BLUETOOTH_LE

Feature for [getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures())[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.lang.String))

Constant Value: "android.hardware.bluetooth_le"

### FEATURE_BLUETOOTH_LE_CHANNEL_SOUNDING    

    [API level 36](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final[String](https://developer.android.com/reference/java/lang/String)FEATURE_BLUETOOTH_LE_CHANNEL_SOUNDING

Feature for [getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures())[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.lang.String))

Constant Value: "android.hardware.bluetooth_le.channel_sounding"

### FEATURE_CAMERA 

    [API level 7](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final[String](https://developer.android.com/reference/java/lang/String)FEATURE_CAMERA

Feature for [getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures())[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.lang.String))

Constant Value: "android.hardware.camera"

### FEATURE_CAMERA_ANY  

    [API level 17](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final[String](https://developer.android.com/reference/java/lang/String)FEATURE_CAMERA_ANY

Feature for [getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures())[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.lang.String))[virtual](https://developer.android.com/reference/android/companion/virtual/VirtualDevice)

Constant Value: "android.hardware.camera.any"

### FEATURE_CAMERA_AR  

    [API level 28](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final[String](https://developer.android.com/reference/java/lang/String)FEATURE_CAMERA_AR

Feature for [getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures())[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.lang.String))[MOTION_TRACKING](https://developer.android.com/reference/android/hardware/camera2/CameraMetadata#REQUEST_AVAILABLE_CAPABILITIES_MOTION_TRACKING)

Constant Value: "android.hardware.camera.ar"

### FEATURE_CAMERA_AUTOFOCUS  

    [API level 7](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final[String](https://developer.android.com/reference/java/lang/String)FEATURE_CAMERA_AUTOFOCUS

Feature for [getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures())[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.lang.String))

Constant Value: "android.hardware.camera.autofocus"

### FEATURE_CAMERA_CAPABILITY_MANUAL_POST_PROCESSING     

    [API level 21](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final[String](https://developer.android.com/reference/java/lang/String)FEATURE_CAMERA_CAPABILITY_MANUAL_POST_PROCESSING

Feature for [getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures())[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.lang.String))[manual post-processing](https://developer.android.com/reference/android/hardware/camera2/CameraMetadata#REQUEST_AVAILABLE_CAPABILITIES_MANUAL_POST_PROCESSING)

Constant Value: "android.hardware.camera.capability.manual_post_processing"

### FEATURE_CAMERA_CAPABILITY_MANUAL_SENSOR    

    [API level 21](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final[String](https://developer.android.com/reference/java/lang/String)FEATURE_CAMERA_CAPABILITY_MANUAL_SENSOR

Feature for [getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures())[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.lang.String))[manual sensor](https://developer.android.com/reference/android/hardware/camera2/CameraMetadata#REQUEST_AVAILABLE_CAPABILITIES_MANUAL_SENSOR)

Constant Value: "android.hardware.camera.capability.manual_sensor"

### FEATURE_CAMERA_CAPABILITY_RAW   

    [API level 21](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final[String](https://developer.android.com/reference/java/lang/String)FEATURE_CAMERA_CAPABILITY_RAW

Feature for [getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures())[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.lang.String))[RAW](https://developer.android.com/reference/android/hardware/camera2/CameraMetadata#REQUEST_AVAILABLE_CAPABILITIES_RAW)

Constant Value: "android.hardware.camera.capability.raw"

### FEATURE_CAMERA_CONCURRENT  

    [API level 30](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final[String](https://developer.android.com/reference/java/lang/String)FEATURE_CAMERA_CONCURRENT

Feature for [getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures())[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.lang.String))[CameraManager.getConcurrentCameraIds()](https://developer.android.com/reference/android/hardware/camera2/CameraManager#getConcurrentCameraIds())

While [CameraManager.getConcurrentCameraIds()](https://developer.android.com/reference/android/hardware/camera2/CameraManager#getConcurrentCameraIds())[CameraDevice.createCaptureSession(android.hardware.camera2.params.SessionConfiguration)](https://developer.android.com/reference/android/hardware/camera2/CameraDevice#createCaptureSession(android.hardware.camera2.params.SessionConfiguration))

Constant Value: "android.hardware.camera.concurrent"

### FEATURE_CAMERA_EXTERNAL  

    [API level 20](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final[String](https://developer.android.com/reference/java/lang/String)FEATURE_CAMERA_EXTERNAL

Feature for [getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures())[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.lang.String))

Constant Value: "android.hardware.camera.external"

### FEATURE_CAMERA_FLASH  

    [API level 7](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final[String](https://developer.android.com/reference/java/lang/String)FEATURE_CAMERA_FLASH

Feature for [getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures())[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.lang.String))

Constant Value: "android.hardware.camera.flash"

### FEATURE_CAMERA_FRONT  

    [API level 9](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final[String](https://developer.android.com/reference/java/lang/String)FEATURE_CAMERA_FRONT

Feature for [getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures())[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.lang.String))

Constant Value: "android.hardware.camera.front"

### FEATURE_CAMERA_LEVEL_FULL   

    [API level 21](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final[String](https://developer.android.com/reference/java/lang/String)FEATURE_CAMERA_LEVEL_FULL

Feature for [getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures())[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.lang.String))[full hardware](https://developer.android.com/reference/android/hardware/camera2/CameraCharacteristics#INFO_SUPPORTED_HARDWARE_LEVEL)

Constant Value: "android.hardware.camera.level.full"

### FEATURE_CANT_SAVE_STATE   

    [API level 28](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final[String](https://developer.android.com/reference/java/lang/String)FEATURE_CANT_SAVE_STATE

Feature for [getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures())[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.lang.String))[R.attr.cantSaveState](https://developer.android.com/reference/android/R.attr#cantSaveState)

Constant Value: "android.software.cant_save_state"

### FEATURE_COMPANION_DEVICE_SETUP   

    [API level 26](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final[String](https://developer.android.com/reference/java/lang/String)FEATURE_COMPANION_DEVICE_SETUP

Feature for [getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures())[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.lang.String))[associating](https://developer.android.com/reference/android/companion/CompanionDeviceManager#associate(android.companion.AssociationRequest,%20android.companion.CompanionDeviceManager.Callback,%20android.os.Handler))[CompanionDeviceManager](https://developer.android.com/reference/android/companion/CompanionDeviceManager)

Constant Value: "android.software.companion_device_setup"

### FEATURE_CONNECTION_SERVICE  

    
public static final[String](https://developer.android.com/reference/java/lang/String)FEATURE_CONNECTION_SERVICE


**
      This constant was deprecated
      in API level 33.**

    use [FEATURE_TELECOM](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_TELECOM)

Feature for [getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures())[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.lang.String))

Constant Value: "android.software.connectionservice"

### FEATURE_CONSUMER_IR  

    [API level 19](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final[String](https://developer.android.com/reference/java/lang/String)FEATURE_CONSUMER_IR

Feature for [getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures())[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.lang.String))

Constant Value: "android.hardware.consumerir"

### FEATURE_CONTROLS 

    [API level 30](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final[String](https://developer.android.com/reference/java/lang/String)FEATURE_CONTROLS

Feature for [getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures())[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.lang.String))

**See also:**

Constant Value: "android.software.controls"

### FEATURE_CREDENTIALS 

    [API level 34](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final[String](https://developer.android.com/reference/java/lang/String)FEATURE_CREDENTIALS

Feature for [getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures())[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.lang.String))

Constant Value: "android.software.credentials"

### FEATURE_DEVICE_ADMIN  

    [API level 19](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final[String](https://developer.android.com/reference/java/lang/String)FEATURE_DEVICE_ADMIN

Feature for [getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures())[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.lang.String))

Constant Value: "android.software.device_admin"

### FEATURE_DEVICE_ID_ATTESTATION   

    [API level 37](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final[String](https://developer.android.com/reference/java/lang/String)FEATURE_DEVICE_ID_ATTESTATION

Feature for [getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures())[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.lang.String))[the public documentation](https://source.android.com/docs/security/features/keystore/attestation#id-attestation)
 for more information about device ID attestation.

Constant Value: "android.software.device_id_attestation"

### FEATURE_DEVICE_LOCK  

    [API level 34](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final[String](https://developer.android.com/reference/java/lang/String)FEATURE_DEVICE_LOCK

Feature for [getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures())[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.lang.String))

Constant Value: "android.software.device_lock"

### FEATURE_EMBEDDED 

    [API level 26](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final[String](https://developer.android.com/reference/java/lang/String)FEATURE_EMBEDDED

Feature for [getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures())[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.lang.String))

Constant Value: "android.hardware.type.embedded"

### FEATURE_ETHERNET 

    [API level 24](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final[String](https://developer.android.com/reference/java/lang/String)FEATURE_ETHERNET

Feature for [getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures())[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.lang.String))

Constant Value: "android.hardware.ethernet"

### FEATURE_EXPANDED_PICTURE_IN_PICTURE    

    [API level 33](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final[String](https://developer.android.com/reference/java/lang/String)FEATURE_EXPANDED_PICTURE_IN_PICTURE

Feature for [getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures())[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.lang.String))

Constant Value: "android.software.expanded_picture_in_picture"

### FEATURE_FACE 

    [API level 29](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final[String](https://developer.android.com/reference/java/lang/String)FEATURE_FACE

Feature for [getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures())[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.lang.String))

Constant Value: "android.hardware.biometrics.face"

### FEATURE_FAKETOUCH 

    [API level 11](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final[String](https://developer.android.com/reference/java/lang/String)FEATURE_FAKETOUCH

Feature for [getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures())[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.lang.String))

Constant Value: "android.hardware.faketouch"

### FEATURE_FAKETOUCH_MULTITOUCH_DISTINCT   

    [API level 13](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final[String](https://developer.android.com/reference/java/lang/String)FEATURE_FAKETOUCH_MULTITOUCH_DISTINCT

Feature for [getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures())[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.lang.String))[FEATURE_FAKETOUCH](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_FAKETOUCH)[FEATURE_TOUCHSCREEN_MULTITOUCH_DISTINCT](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_TOUCHSCREEN_MULTITOUCH_DISTINCT)

Constant Value: "android.hardware.faketouch.multitouch.distinct"

### FEATURE_FAKETOUCH_MULTITOUCH_JAZZHAND   

    [API level 13](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final[String](https://developer.android.com/reference/java/lang/String)FEATURE_FAKETOUCH_MULTITOUCH_JAZZHAND

Feature for [getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures())[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.lang.String))[FEATURE_FAKETOUCH](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_FAKETOUCH)[FEATURE_TOUCHSCREEN_MULTITOUCH_JAZZHAND](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_TOUCHSCREEN_MULTITOUCH_JAZZHAND)[FEATURE_FAKETOUCH_MULTITOUCH_DISTINCT](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_FAKETOUCH_MULTITOUCH_DISTINCT)

Constant Value: "android.hardware.faketouch.multitouch.jazzhand"

### FEATURE_FINGERPRINT 

    [API level 23](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final[String](https://developer.android.com/reference/java/lang/String)FEATURE_FINGERPRINT

Feature for [getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures())[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.lang.String))

Constant Value: "android.hardware.fingerprint"

### FEATURE_FREEFORM_WINDOW_MANAGEMENT   

    [API level 24](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final[String](https://developer.android.com/reference/java/lang/String)FEATURE_FREEFORM_WINDOW_MANAGEMENT

Feature for [getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures())[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.lang.String))

Constant Value: "android.software.freeform_window_management"

### FEATURE_GAMEPAD 

    [API level 21](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final[String](https://developer.android.com/reference/java/lang/String)FEATURE_GAMEPAD

Feature for [getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures())[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.lang.String))

Constant Value: "android.hardware.gamepad"

### FEATURE_HARDWARE_KEYSTORE  

    [API level 31](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final[String](https://developer.android.com/reference/java/lang/String)FEATURE_HARDWARE_KEYSTORE

Feature for [getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures())[hasSystemFeature(String,int)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.lang.String,%20int))

- 500: Hardware support for ML-DSA signature generation.
- 400: Inclusion of module information (via tag MODULE_HASH) in the attestation record.
- 300: Ability to include a second IMEI in the ID attestation record, see
 [DevicePolicyManager.ID_TYPE_IMEI](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#ID_TYPE_IMEI)
- 200: Hardware support for Curve 25519 (including both Ed25519 signature generation and X25519 key agreement).
- 100: Hardware support for ECDH (see [KeyAgreement](https://developer.android.com/reference/javax/crypto/KeyAgreement)[android.security.keystore.KeyGenParameterSpec.Builder.setAttestKeyAlias(String)](https://developer.android.com/reference/android/security/keystore/KeyGenParameterSpec.Builder#setAttestKeyAlias(java.lang.String))
- 41: Hardware enforcement of device-unlocked keys (see [KeyGenParameterSpec.Builder.setUnlockedDeviceRequired(boolean)](https://developer.android.com/reference/android/security/keystore/KeyGenParameterSpec.Builder#setUnlockedDeviceRequired(boolean))
- 40: Support for wrapped key import (see [WrappedKeyEntry](https://developer.android.com/reference/android/security/keystore/WrappedKeyEntry)[KeyGenParameterSpec.Builder.setDevicePropertiesAttestationIncluded(boolean)](https://developer.android.com/reference/android/security/keystore/KeyGenParameterSpec.Builder#setDevicePropertiesAttestationIncluded(boolean))[KeyGenParameterSpec.Builder.setAttestationChallenge(byte[])](https://developer.android.com/reference/android/security/keystore/KeyGenParameterSpec.Builder#setAttestationChallenge(byte[]))

Constant Value: "android.hardware.hardware_keystore"

### FEATURE_HIFI_SENSORS  

    [API level 23](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final[String](https://developer.android.com/reference/java/lang/String)FEATURE_HIFI_SENSORS

Feature for [getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures())[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.lang.String))

Constant Value: "android.hardware.sensor.hifi_sensors"

### FEATURE_HOME_SCREEN  

    [API level 18](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final[String](https://developer.android.com/reference/java/lang/String)FEATURE_HOME_SCREEN

Feature for [getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures())[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.lang.String))

Constant Value: "android.software.home_screen"

### FEATURE_IDENTITY_CREDENTIAL_HARDWARE   

    [API level 31](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final[String](https://developer.android.com/reference/java/lang/String)FEATURE_IDENTITY_CREDENTIAL_HARDWARE

Feature for [getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures())[hasSystemFeature(String,int)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.lang.String,%20int))[IdentityCredentialStore](https://developer.android.com/reference/android/security/identity/IdentityCredentialStore)

Known feature versions include:

- `202009`: corresponds to the features included in the Identity Credential API shipped in Android 11.
- `202101`: corresponds to the features included in the Identity Credential API shipped in Android 12.
- `202201`: corresponds to the features included in the Identity Credential API shipped in Android 13.

Constant Value: "android.hardware.identity_credential"

### FEATURE_IDENTITY_CREDENTIAL_HARDWARE_DIRECT_ACCESS     

    [API level 31](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final[String](https://developer.android.com/reference/java/lang/String)FEATURE_IDENTITY_CREDENTIAL_HARDWARE_DIRECT_ACCESS

Feature for [getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures())[hasSystemFeature(String,int)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.lang.String,%20int))[IdentityCredentialStore](https://developer.android.com/reference/android/security/identity/IdentityCredentialStore)[FEATURE_IDENTITY_CREDENTIAL_HARDWARE](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_IDENTITY_CREDENTIAL_HARDWARE)

Constant Value: "android.hardware.identity_credential_direct_access"

### FEATURE_INPUT_METHODS  

    [API level 18](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final[String](https://developer.android.com/reference/java/lang/String)FEATURE_INPUT_METHODS

Feature for [getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures())[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.lang.String))[InputMethodService](https://developer.android.com/reference/android/inputmethodservice/InputMethodService)

Constant Value: "android.software.input_methods"

### FEATURE_IPSEC_TUNNELS  

    [API level 29](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final[String](https://developer.android.com/reference/java/lang/String)FEATURE_IPSEC_TUNNELS

Feature for [getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures())[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.lang.String))

This feature implies that the device supports XFRM Interfaces (CONFIG_XFRM_INTERFACE), or VTIs with kernel patches allowing updates of output/set mark via UPDSA.

Constant Value: "android.software.ipsec_tunnels"

### FEATURE_IPSEC_TUNNEL_MIGRATION   

    [API level 34](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final[String](https://developer.android.com/reference/java/lang/String)FEATURE_IPSEC_TUNNEL_MIGRATION

Feature for [getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures())[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.lang.String))

This feature implies that the device supports XFRM Migration (CONFIG_XFRM_MIGRATE) and has the kernel fixes to support cross-address-family IPsec tunnel migration

Constant Value: "android.software.ipsec_tunnel_migration"

### FEATURE_IRIS 

    [API level 29](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final[String](https://developer.android.com/reference/java/lang/String)FEATURE_IRIS

Feature for [getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures())[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.lang.String))

Constant Value: "android.hardware.biometrics.iris"

### FEATURE_KEYSTORE_APP_ATTEST_KEY    

    [API level 31](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final[String](https://developer.android.com/reference/java/lang/String)FEATURE_KEYSTORE_APP_ATTEST_KEY

Feature for [getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures())[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.lang.String))[KeyGenParameterSpec.Builder.setAttestKeyAlias(String)](https://developer.android.com/reference/android/security/keystore/KeyGenParameterSpec.Builder#setAttestKeyAlias(java.lang.String))

Constant Value: "android.hardware.keystore.app_attest_key"

### FEATURE_KEYSTORE_LIMITED_USE_KEY    

    [API level 31](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final[String](https://developer.android.com/reference/java/lang/String)FEATURE_KEYSTORE_LIMITED_USE_KEY

Feature for [getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures())[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.lang.String))

Constant Value: "android.hardware.keystore.limited_use_key"

### FEATURE_KEYSTORE_SINGLE_USE_KEY    

    [API level 31](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final[String](https://developer.android.com/reference/java/lang/String)FEATURE_KEYSTORE_SINGLE_USE_KEY

Feature for [getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures())[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.lang.String))

Constant Value: "android.hardware.keystore.single_use_key"

### FEATURE_LEANBACK 

    [API level 21](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final[String](https://developer.android.com/reference/java/lang/String)FEATURE_LEANBACK

Feature for [getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures())[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.lang.String))[FEATURE_TELEVISION](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_TELEVISION)

Constant Value: "android.software.leanback"

### FEATURE_LEANBACK_ONLY  

    [API level 26](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final[String](https://developer.android.com/reference/java/lang/String)FEATURE_LEANBACK_ONLY

Feature for [getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures())[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.lang.String))

Constant Value: "android.software.leanback_only"

### FEATURE_LIVE_TV  

    [API level 21](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final[String](https://developer.android.com/reference/java/lang/String)FEATURE_LIVE_TV

Feature for [getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures())[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.lang.String))[TvInputService](https://developer.android.com/reference/android/media/tv/TvInputService)

Constant Value: "android.software.live_tv"

### FEATURE_LIVE_WALLPAPER  

    [API level 7](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final[String](https://developer.android.com/reference/java/lang/String)FEATURE_LIVE_WALLPAPER

Feature for [getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures())[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.lang.String))

Constant Value: "android.software.live_wallpaper"

### FEATURE_LOCATION 

    [API level 8](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final[String](https://developer.android.com/reference/java/lang/String)FEATURE_LOCATION

Feature for [getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures())[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.lang.String))

Constant Value: "android.hardware.location"

### FEATURE_LOCATION_GPS  

    [API level 8](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final[String](https://developer.android.com/reference/java/lang/String)FEATURE_LOCATION_GPS

Feature for [getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures())[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.lang.String))

Constant Value: "android.hardware.location.gps"

### FEATURE_LOCATION_NETWORK  

    [API level 8](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final[String](https://developer.android.com/reference/java/lang/String)FEATURE_LOCATION_NETWORK

Feature for [getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures())[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.lang.String))

Constant Value: "android.hardware.location.network"

### FEATURE_MANAGED_USERS  

    [API level 21](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final[String](https://developer.android.com/reference/java/lang/String)FEATURE_MANAGED_USERS

Feature for [getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures())[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.lang.String))[DevicePolicyManager](https://developer.android.com/reference/android/app/admin/DevicePolicyManager)

Constant Value: "android.software.managed_users"

### FEATURE_MICROPHONE 

    [API level 8](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final[String](https://developer.android.com/reference/java/lang/String)FEATURE_MICROPHONE

Feature for [getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures())[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.lang.String))

Constant Value: "android.hardware.microphone"

### FEATURE_MIDI 

    [API level 23](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final[String](https://developer.android.com/reference/java/lang/String)FEATURE_MIDI

Feature for [getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures())[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.lang.String))

Constant Value: "android.software.midi"

### FEATURE_NEURAL_PROCESSING_UNIT   

    [API level 37](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final[String](https://developer.android.com/reference/java/lang/String)FEATURE_NEURAL_PROCESSING_UNIT

Feature for [getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures())[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.lang.String))

Constant Value: "android.hardware.npu"

### FEATURE_NFC 

    [API level 9](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final[String](https://developer.android.com/reference/java/lang/String)FEATURE_NFC

Feature for [getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures())[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.lang.String))

Constant Value: "android.hardware.nfc"

### FEATURE_NFC_BEAM  

    [API level 29](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final[String](https://developer.android.com/reference/java/lang/String)FEATURE_NFC_BEAM

Feature for [getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures())[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.lang.String))

Constant Value: "android.sofware.nfc.beam"

### FEATURE_NFC_HOST_CARD_EMULATION    

    [API level 19](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final[String](https://developer.android.com/reference/java/lang/String)FEATURE_NFC_HOST_CARD_EMULATION

Feature for [getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures())[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.lang.String))

Constant Value: "android.hardware.nfc.hce"

### FEATURE_NFC_HOST_CARD_EMULATION_NFCF     

    [API level 24](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final[String](https://developer.android.com/reference/java/lang/String)FEATURE_NFC_HOST_CARD_EMULATION_NFCF

Feature for [getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures())[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.lang.String))

Constant Value: "android.hardware.nfc.hcef"

### FEATURE_NFC_OFF_HOST_CARD_EMULATION_ESE      

    [API level 29](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final[String](https://developer.android.com/reference/java/lang/String)FEATURE_NFC_OFF_HOST_CARD_EMULATION_ESE

Feature for [getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures())[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.lang.String))

Constant Value: "android.hardware.nfc.ese"

### FEATURE_NFC_OFF_HOST_CARD_EMULATION_UICC      

    [API level 29](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final[String](https://developer.android.com/reference/java/lang/String)FEATURE_NFC_OFF_HOST_CARD_EMULATION_UICC

Feature for [getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures())[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.lang.String))

Constant Value: "android.hardware.nfc.uicc"

### FEATURE_OPENGLES_DEQP_LEVEL   

    [API level 31](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final[String](https://developer.android.com/reference/java/lang/String)FEATURE_OPENGLES_DEQP_LEVEL

Feature for [getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures())[hasSystemFeature(String,int)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.lang.String,%20int))

- Year in bits 31-16
- Month in bits 15-8
- Day in bits 7-0

Example: 2021-03-01 is encoded as 0x07E50301, and would indicate that the device passes the OpenGL ES dEQP test suite version that was current on 2021-03-01.

Constant Value: "android.software.opengles.deqp.level"

### FEATURE_OPENGLES_EXTENSION_PACK   

    [API level 21](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final[String](https://developer.android.com/reference/java/lang/String)FEATURE_OPENGLES_EXTENSION_PACK

Feature for [getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures())[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.lang.String))[
 Android Extension Pack](http://www.khronos.org/registry/gles/extensions/ANDROID/ANDROID_extension_pack_es31a.txt).

Constant Value: "android.hardware.opengles.aep"

### FEATURE_PC 

    [API level 27](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final[String](https://developer.android.com/reference/java/lang/String)FEATURE_PC

Feature for [getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures())[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.lang.String))[FEATURE_FREEFORM_WINDOW_MANAGEMENT](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_FREEFORM_WINDOW_MANAGEMENT)

Constant Value: "android.hardware.type.pc"

### FEATURE_PICTURE_IN_PICTURE   

    [API level 24](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final[String](https://developer.android.com/reference/java/lang/String)FEATURE_PICTURE_IN_PICTURE

Feature for [getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures())[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.lang.String))

Constant Value: "android.software.picture_in_picture"

### FEATURE_PRINTING 

    [API level 20](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final[String](https://developer.android.com/reference/java/lang/String)FEATURE_PRINTING

Feature for [getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures())[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.lang.String))

Constant Value: "android.software.print"

### FEATURE_RAM_LOW  

    [API level 27](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final[String](https://developer.android.com/reference/java/lang/String)FEATURE_RAM_LOW

Feature for [getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures())[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.lang.String))[ActivityManager.isLowRamDevice()](https://developer.android.com/reference/android/app/ActivityManager#isLowRamDevice())

Constant Value: "android.hardware.ram.low"

### FEATURE_RAM_NORMAL  

    [API level 27](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final[String](https://developer.android.com/reference/java/lang/String)FEATURE_RAM_NORMAL

Feature for [getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures())[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.lang.String))[ActivityManager.isLowRamDevice()](https://developer.android.com/reference/android/app/ActivityManager#isLowRamDevice())

Constant Value: "android.hardware.ram.normal"

### FEATURE_SCREEN_LANDSCAPE  

    [API level 13](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final[String](https://developer.android.com/reference/java/lang/String)FEATURE_SCREEN_LANDSCAPE

Feature for [getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures())[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.lang.String))[FEATURE_SCREEN_PORTRAIT](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_SCREEN_PORTRAIT)

Constant Value: "android.hardware.screen.landscape"

### FEATURE_SCREEN_PORTRAIT  

    [API level 13](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final[String](https://developer.android.com/reference/java/lang/String)FEATURE_SCREEN_PORTRAIT

Feature for [getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures())[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.lang.String))[FEATURE_SCREEN_LANDSCAPE](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_SCREEN_LANDSCAPE)

Constant Value: "android.hardware.screen.portrait"

### FEATURE_SECURELY_REMOVES_USERS   

    [API level 21](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final[String](https://developer.android.com/reference/java/lang/String)FEATURE_SECURELY_REMOVES_USERS

Feature for [getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures())[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.lang.String))

Constant Value: "android.software.securely_removes_users"

### FEATURE_SECURE_LOCK_SCREEN   

    [API level 29](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final[String](https://developer.android.com/reference/java/lang/String)FEATURE_SECURE_LOCK_SCREEN

Feature for [getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures())[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.lang.String))

Constant Value: "android.software.secure_lock_screen"

### FEATURE_SECURITY_MODEL_COMPATIBLE   

    [API level 31](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final[String](https://developer.android.com/reference/java/lang/String)FEATURE_SECURITY_MODEL_COMPATIBLE

Feature for [getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures())[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.lang.String))

See sections 2 and 9 in the
 [Android CDD](https://source.android.com/compatibility/android-cdd) for more
 details.

Constant Value: "android.hardware.security.model.compatible"

### FEATURE_SENSOR_ACCELEROMETER  

    [API level 8](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final[String](https://developer.android.com/reference/java/lang/String)FEATURE_SENSOR_ACCELEROMETER

Feature for [getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures())[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.lang.String))

Constant Value: "android.hardware.sensor.accelerometer"

### FEATURE_SENSOR_ACCELEROMETER_LIMITED_AXES    

    [API level 33](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final[String](https://developer.android.com/reference/java/lang/String)FEATURE_SENSOR_ACCELEROMETER_LIMITED_AXES

Feature for [getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures())[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.lang.String))

Constant Value: "android.hardware.sensor.accelerometer_limited_axes"

### FEATURE_SENSOR_ACCELEROMETER_LIMITED_AXES_UNCALIBRATED     

    [API level 33](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final[String](https://developer.android.com/reference/java/lang/String)FEATURE_SENSOR_ACCELEROMETER_LIMITED_AXES_UNCALIBRATED

Feature for [getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures())[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.lang.String))

Constant Value: "android.hardware.sensor.accelerometer_limited_axes_uncalibrated"

### FEATURE_SENSOR_AMBIENT_TEMPERATURE   

    [API level 21](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final[String](https://developer.android.com/reference/java/lang/String)FEATURE_SENSOR_AMBIENT_TEMPERATURE

Feature for [getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures())[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.lang.String))

Constant Value: "android.hardware.sensor.ambient_temperature"

### FEATURE_SENSOR_BAROMETER  

    [API level 9](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final[String](https://developer.android.com/reference/java/lang/String)FEATURE_SENSOR_BAROMETER

Feature for [getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures())[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.lang.String))

Constant Value: "android.hardware.sensor.barometer"

### FEATURE_SENSOR_COMPASS  

    [API level 8](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final[String](https://developer.android.com/reference/java/lang/String)FEATURE_SENSOR_COMPASS

Feature for [getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures())[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.lang.String))

Constant Value: "android.hardware.sensor.compass"

### FEATURE_SENSOR_DYNAMIC_HEAD_TRACKER    

    [API level 33](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final[String](https://developer.android.com/reference/java/lang/String)FEATURE_SENSOR_DYNAMIC_HEAD_TRACKER

Feature for [getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures())[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.lang.String))

Constant Value: "android.hardware.sensor.dynamic.head_tracker"

### FEATURE_SENSOR_GYROSCOPE  

    [API level 9](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final[String](https://developer.android.com/reference/java/lang/String)FEATURE_SENSOR_GYROSCOPE

Feature for [getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures())[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.lang.String))

Constant Value: "android.hardware.sensor.gyroscope"

### FEATURE_SENSOR_GYROSCOPE_LIMITED_AXES    

    [API level 33](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final[String](https://developer.android.com/reference/java/lang/String)FEATURE_SENSOR_GYROSCOPE_LIMITED_AXES

Feature for [getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures())[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.lang.String))

Constant Value: "android.hardware.sensor.gyroscope_limited_axes"

### FEATURE_SENSOR_GYROSCOPE_LIMITED_AXES_UNCALIBRATED     

    [API level 33](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final[String](https://developer.android.com/reference/java/lang/String)FEATURE_SENSOR_GYROSCOPE_LIMITED_AXES_UNCALIBRATED

Feature for [getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures())[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.lang.String))

Constant Value: "android.hardware.sensor.gyroscope_limited_axes_uncalibrated"

### FEATURE_SENSOR_HEADING  

    [API level 33](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final[String](https://developer.android.com/reference/java/lang/String)FEATURE_SENSOR_HEADING

Feature for [getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures())[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.lang.String))

Constant Value: "android.hardware.sensor.heading"

### FEATURE_SENSOR_HEART_RATE   

    [API level 20](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final[String](https://developer.android.com/reference/java/lang/String)FEATURE_SENSOR_HEART_RATE

Feature for [getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures())[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.lang.String))

Constant Value: "android.hardware.sensor.heartrate"

### FEATURE_SENSOR_HEART_RATE_ECG    

    [API level 21](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final[String](https://developer.android.com/reference/java/lang/String)FEATURE_SENSOR_HEART_RATE_ECG

Feature for [getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures())[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.lang.String))

Constant Value: "android.hardware.sensor.heartrate.ecg"

### FEATURE_SENSOR_HINGE_ANGLE   

    [API level 30](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final[String](https://developer.android.com/reference/java/lang/String)FEATURE_SENSOR_HINGE_ANGLE

Feature for [getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures())[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.lang.String))

Constant Value: "android.hardware.sensor.hinge_angle"

### FEATURE_SENSOR_LIGHT  

    [API level 7](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final[String](https://developer.android.com/reference/java/lang/String)FEATURE_SENSOR_LIGHT

Feature for [getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures())[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.lang.String))

Constant Value: "android.hardware.sensor.light"

### FEATURE_SENSOR_PROXIMITY  

    [API level 7](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final[String](https://developer.android.com/reference/java/lang/String)FEATURE_SENSOR_PROXIMITY

Feature for [getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures())[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.lang.String))

Constant Value: "android.hardware.sensor.proximity"

### FEATURE_SENSOR_RELATIVE_HUMIDITY   

    [API level 21](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final[String](https://developer.android.com/reference/java/lang/String)FEATURE_SENSOR_RELATIVE_HUMIDITY

Feature for [getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures())[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.lang.String))

Constant Value: "android.hardware.sensor.relative_humidity"

### FEATURE_SENSOR_STEP_COUNTER   

    [API level 19](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final[String](https://developer.android.com/reference/java/lang/String)FEATURE_SENSOR_STEP_COUNTER

Feature for [getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures())[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.lang.String))

Constant Value: "android.hardware.sensor.stepcounter"

### FEATURE_SENSOR_STEP_DETECTOR   

    [API level 19](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final[String](https://developer.android.com/reference/java/lang/String)FEATURE_SENSOR_STEP_DETECTOR

Feature for [getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures())[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.lang.String))

Constant Value: "android.hardware.sensor.stepdetector"

### FEATURE_SE_OMAPI_ESE   

    [API level 30](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final[String](https://developer.android.com/reference/java/lang/String)FEATURE_SE_OMAPI_ESE

Feature for [getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures())[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.lang.String))

Constant Value: "android.hardware.se.omapi.ese"

### FEATURE_SE_OMAPI_SD   

    [API level 30](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final[String](https://developer.android.com/reference/java/lang/String)FEATURE_SE_OMAPI_SD

Feature for [getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures())[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.lang.String))

Constant Value: "android.hardware.se.omapi.sd"

### FEATURE_SE_OMAPI_UICC   

    [API level 30](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final[String](https://developer.android.com/reference/java/lang/String)FEATURE_SE_OMAPI_UICC

Feature for [getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures())[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.lang.String))

Constant Value: "android.hardware.se.omapi.uicc"

### FEATURE_SIP 

    [API level 9](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final[String](https://developer.android.com/reference/java/lang/String)FEATURE_SIP

Feature for [getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures())[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.lang.String))

Constant Value: "android.software.sip"

### FEATURE_SIP_VOIP  

    [API level 9](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final[String](https://developer.android.com/reference/java/lang/String)FEATURE_SIP_VOIP

Feature for [getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures())[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.lang.String))

Constant Value: "android.software.sip.voip"

### FEATURE_STRONGBOX_KEYSTORE  

    [API level 28](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final[String](https://developer.android.com/reference/java/lang/String)FEATURE_STRONGBOX_KEYSTORE

Feature for [getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures())[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.lang.String))[hasSystemFeature(String,int)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.lang.String,%20int))[
 StrongBox](https://source.android.com/security/best-practices/hardware#strongbox-keymaster). If this feature has a version, the version number indicates which features are
 implemented in StrongBox:
 

- 400: Inclusion of module information (via tag MODULE_HASH) in the attestation record.
- 300: Ability to include a second IMEI in the ID attestation record, see
 [DevicePolicyManager.ID_TYPE_IMEI](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#ID_TYPE_IMEI)
- 200: No new features for StrongBox (the Android Keystore environment backed by an isolated execution environment has gained support for Curve 25519 in this version, but the implementation backed by a dedicated secure processor is not expected to implement it).
- 100: Hardware support for ECDH (see [KeyAgreement](https://developer.android.com/reference/javax/crypto/KeyAgreement)[android.security.keystore.KeyGenParameterSpec.Builder.setAttestKeyAlias(String)](https://developer.android.com/reference/android/security/keystore/KeyGenParameterSpec.Builder#setAttestKeyAlias(java.lang.String))
- 41: Hardware enforcement of device-unlocked keys (see [KeyGenParameterSpec.Builder.setUnlockedDeviceRequired(boolean)](https://developer.android.com/reference/android/security/keystore/KeyGenParameterSpec.Builder#setUnlockedDeviceRequired(boolean))
- 40: Support for wrapped key import (see [WrappedKeyEntry](https://developer.android.com/reference/android/security/keystore/WrappedKeyEntry)[KeyGenParameterSpec.Builder.setDevicePropertiesAttestationIncluded(boolean)](https://developer.android.com/reference/android/security/keystore/KeyGenParameterSpec.Builder#setDevicePropertiesAttestationIncluded(boolean))[KeyGenParameterSpec.Builder.setAttestationChallenge(byte[])](https://developer.android.com/reference/android/security/keystore/KeyGenParameterSpec.Builder#setAttestationChallenge(byte[]))

Constant Value: "android.hardware.strongbox_keystore"

### FEATURE_TELECOM 

    [API level 33](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final[String](https://developer.android.com/reference/java/lang/String)FEATURE_TELECOM

Feature for [getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures())[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.lang.String))

Constant Value: "android.software.telecom"

### FEATURE_TELEPHONY 

    [API level 7](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final[String](https://developer.android.com/reference/java/lang/String)FEATURE_TELEPHONY

Feature for [getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures())[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.lang.String))

Constant Value: "android.hardware.telephony"

### FEATURE_TELEPHONY_CALLING  

    [API level 33](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final[String](https://developer.android.com/reference/java/lang/String)FEATURE_TELEPHONY_CALLING

Feature for [getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures())[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.lang.String))

This feature should only be defined if [FEATURE_TELEPHONY_RADIO_ACCESS](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_TELEPHONY_RADIO_ACCESS)[FEATURE_TELEPHONY_SUBSCRIPTION](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_TELEPHONY_SUBSCRIPTION)[FEATURE_TELECOM](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_TELECOM)

Constant Value: "android.hardware.telephony.calling"

### FEATURE_TELEPHONY_CDMA  

    [API level 7](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final[String](https://developer.android.com/reference/java/lang/String)FEATURE_TELEPHONY_CDMA

Feature for [getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures())[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.lang.String))

This feature should only be defined if [FEATURE_TELEPHONY](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_TELEPHONY)

Constant Value: "android.hardware.telephony.cdma"

### FEATURE_TELEPHONY_DATA  

    [API level 33](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final[String](https://developer.android.com/reference/java/lang/String)FEATURE_TELEPHONY_DATA

Feature for [getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures())[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.lang.String))

This feature should only be defined if both [FEATURE_TELEPHONY_SUBSCRIPTION](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_TELEPHONY_SUBSCRIPTION)[FEATURE_TELEPHONY_RADIO_ACCESS](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_TELEPHONY_RADIO_ACCESS)

Constant Value: "android.hardware.telephony.data"

### FEATURE_TELEPHONY_EUICC  

    [API level 28](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final[String](https://developer.android.com/reference/java/lang/String)FEATURE_TELEPHONY_EUICC

Feature for [getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures())[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.lang.String))[FEATURE_TELEPHONY_SUBSCRIPTION](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_TELEPHONY_SUBSCRIPTION)

Constant Value: "android.hardware.telephony.euicc"

### FEATURE_TELEPHONY_EUICC_MEP   

    [API level 33](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final[String](https://developer.android.com/reference/java/lang/String)FEATURE_TELEPHONY_EUICC_MEP

Feature for [getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures())[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.lang.String))

Devices declaring this feature must have an implementation of the
  [UiccCardInfo.getPorts](https://developer.android.com/reference/android/telephony/UiccCardInfo#getPorts())[UiccCardInfo.isMultipleEnabledProfilesSupported](https://developer.android.com/reference/android/telephony/UiccCardInfo#isMultipleEnabledProfilesSupported())[(with portIndex)](https://developer.android.com/reference/android/telephony/euicc/EuiccManager#switchToSubscription(int,%20android.app.PendingIntent))[FEATURE_TELEPHONY_EUICC](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_TELEPHONY_EUICC)

Constant Value: "android.hardware.telephony.euicc.mep"

### FEATURE_TELEPHONY_GSM  

    [API level 7](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final[String](https://developer.android.com/reference/java/lang/String)FEATURE_TELEPHONY_GSM

Feature for [getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures())[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.lang.String))

This feature should only be defined if [FEATURE_TELEPHONY](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_TELEPHONY)

Constant Value: "android.hardware.telephony.gsm"

### FEATURE_TELEPHONY_IMS  

    [API level 29](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final[String](https://developer.android.com/reference/java/lang/String)FEATURE_TELEPHONY_IMS

Feature for [getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures())[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.lang.String))

This feature should only be defined if [FEATURE_TELEPHONY_DATA](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_TELEPHONY_DATA)

Constant Value: "android.hardware.telephony.ims"

### FEATURE_TELEPHONY_MBMS  

    [API level 28](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final[String](https://developer.android.com/reference/java/lang/String)FEATURE_TELEPHONY_MBMS

Feature for [getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures())[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.lang.String))

This feature should only be defined if both [FEATURE_TELEPHONY_SUBSCRIPTION](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_TELEPHONY_SUBSCRIPTION)[FEATURE_TELEPHONY_RADIO_ACCESS](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_TELEPHONY_RADIO_ACCESS)

Constant Value: "android.hardware.telephony.mbms"

### FEATURE_TELEPHONY_MESSAGING  

    [API level 33](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final[String](https://developer.android.com/reference/java/lang/String)FEATURE_TELEPHONY_MESSAGING

Feature for [getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures())[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.lang.String))

This feature should only be defined if both [FEATURE_TELEPHONY_SUBSCRIPTION](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_TELEPHONY_SUBSCRIPTION)[FEATURE_TELEPHONY_RADIO_ACCESS](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_TELEPHONY_RADIO_ACCESS)

Constant Value: "android.hardware.telephony.messaging"

### FEATURE_TELEPHONY_RADIO_ACCESS   

    [API level 33](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final[String](https://developer.android.com/reference/java/lang/String)FEATURE_TELEPHONY_RADIO_ACCESS

Feature for [getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures())[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.lang.String))

This feature should only be defined if [FEATURE_TELEPHONY](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_TELEPHONY)

Constant Value: "android.hardware.telephony.radio.access"

### FEATURE_TELEPHONY_SUBSCRIPTION  

    [API level 33](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final[String](https://developer.android.com/reference/java/lang/String)FEATURE_TELEPHONY_SUBSCRIPTION

Feature for [getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures())[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.lang.String))

This feature should only be defined if [FEATURE_TELEPHONY](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_TELEPHONY)

Constant Value: "android.hardware.telephony.subscription"

### FEATURE_TELEVISION 

    
public static final[String](https://developer.android.com/reference/java/lang/String)FEATURE_TELEVISION


**
      This constant was deprecated
      in API level 21.**

    use [FEATURE_LEANBACK](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_LEANBACK)

Feature for [getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures())[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.lang.String))

Constant Value: "android.hardware.type.television"

### FEATURE_THREAD_NETWORK  

    [API level 36](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final[String](https://developer.android.com/reference/java/lang/String)FEATURE_THREAD_NETWORK

Feature for [getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures())[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.lang.String))[Thread](https://www.threadgroup.org/) networking protocol.

Constant Value: "android.hardware.thread_network"

### FEATURE_TOUCHSCREEN 

    [API level 8](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final[String](https://developer.android.com/reference/java/lang/String)FEATURE_TOUCHSCREEN

Feature for [getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures())[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.lang.String))

Constant Value: "android.hardware.touchscreen"

### FEATURE_TOUCHSCREEN_MULTITOUCH  

    [API level 7](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final[String](https://developer.android.com/reference/java/lang/String)FEATURE_TOUCHSCREEN_MULTITOUCH

Feature for [getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures())[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.lang.String))

Constant Value: "android.hardware.touchscreen.multitouch"

### FEATURE_TOUCHSCREEN_MULTITOUCH_DISTINCT   

    [API level 8](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final[String](https://developer.android.com/reference/java/lang/String)FEATURE_TOUCHSCREEN_MULTITOUCH_DISTINCT

Feature for [getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures())[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.lang.String))

Constant Value: "android.hardware.touchscreen.multitouch.distinct"

### FEATURE_TOUCHSCREEN_MULTITOUCH_JAZZHAND   

    [API level 9](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final[String](https://developer.android.com/reference/java/lang/String)FEATURE_TOUCHSCREEN_MULTITOUCH_JAZZHAND

Feature for [getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures())[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.lang.String))

Constant Value: "android.hardware.touchscreen.multitouch.jazzhand"

### FEATURE_USB_ACCESSORY  

    [API level 12](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final[String](https://developer.android.com/reference/java/lang/String)FEATURE_USB_ACCESSORY

Feature for [getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures())[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.lang.String))

Constant Value: "android.hardware.usb.accessory"

### FEATURE_USB_HOST  

    [API level 12](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final[String](https://developer.android.com/reference/java/lang/String)FEATURE_USB_HOST

Feature for [getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures())[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.lang.String))

Constant Value: "android.hardware.usb.host"

### FEATURE_UWB 

    [API level 34](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final[String](https://developer.android.com/reference/java/lang/String)FEATURE_UWB

Feature for [getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures())[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.lang.String))

Constant Value: "android.hardware.uwb"

### FEATURE_VERIFIED_BOOT  

    [API level 21](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final[String](https://developer.android.com/reference/java/lang/String)FEATURE_VERIFIED_BOOT

Feature for [getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures())[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.lang.String))

Constant Value: "android.software.verified_boot"

### FEATURE_VR_HEADTRACKING  

    [API level 26](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final[String](https://developer.android.com/reference/java/lang/String)FEATURE_VR_HEADTRACKING

Feature for [getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures())[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.lang.String))

Constant Value: "android.hardware.vr.headtracking"

### FEATURE_VR_MODE  

    
public static final[String](https://developer.android.com/reference/java/lang/String)FEATURE_VR_MODE


**
      This constant was deprecated
      in API level 28.**

    use [FEATURE_VR_MODE_HIGH_PERFORMANCE](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_VR_MODE_HIGH_PERFORMANCE)

Feature for [getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures())[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.lang.String))[VrListenerService](https://developer.android.com/reference/android/service/vr/VrListenerService)[Activity.setVrModeEnabled(boolean, ComponentName)](https://developer.android.com/reference/android/app/Activity#setVrModeEnabled(boolean,%20android.content.ComponentName))

Constant Value: "android.software.vr.mode"

### FEATURE_VR_MODE_HIGH_PERFORMANCE    

    [API level 24](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final[String](https://developer.android.com/reference/java/lang/String)FEATURE_VR_MODE_HIGH_PERFORMANCE

Feature for [getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures())[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.lang.String))[VrListenerService](https://developer.android.com/reference/android/service/vr/VrListenerService)[Activity.setVrModeEnabled(boolean, ComponentName)](https://developer.android.com/reference/android/app/Activity#setVrModeEnabled(boolean,%20android.content.ComponentName))

Constant Value: "android.hardware.vr.high_performance"

### FEATURE_VULKAN_DEQP_LEVEL   

    [API level 30](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final[String](https://developer.android.com/reference/java/lang/String)FEATURE_VULKAN_DEQP_LEVEL

Feature for [getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures())[hasSystemFeature(String,int)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.lang.String,%20int))

- Year in bits 31-16
- Month in bits 15-8
- Day in bits 7-0

Example: 2019-03-01 is encoded as 0x07E30301, and would indicate that the device passes the Vulkan dEQP test suite version that was current on 2019-03-01.

Constant Value: "android.software.vulkan.deqp.level"

### FEATURE_VULKAN_HARDWARE_COMPUTE   

    [API level 26](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final[String](https://developer.android.com/reference/java/lang/String)FEATURE_VULKAN_HARDWARE_COMPUTE

Feature for [getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures())[hasSystemFeature(String,int)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.lang.String,%20int))`VkPhysicalDevice`, and the feature version will indicate what
 level of optional compute features that device supports beyond the Vulkan 1.0 requirements.
 

Compute level 0 indicates:

- The `VK_KHR_variable_pointers`extension and`VkPhysicalDeviceVariablePointerFeaturesKHR::variablePointers`feature are supported.
- `VkPhysicalDeviceLimits::maxPerStageDescriptorStorageBuffers`is at least 16.

Constant Value: "android.hardware.vulkan.compute"

### FEATURE_VULKAN_HARDWARE_LEVEL   

    [API level 24](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final[String](https://developer.android.com/reference/java/lang/String)FEATURE_VULKAN_HARDWARE_LEVEL

Feature for [getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures())[hasSystemFeature(String,int)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.lang.String,%20int))`VkPhysicalDevice`, and the feature version will indicate what
 level of optional hardware features limits it supports.
 

Level 0 includes the base Vulkan requirements as well as:

- `VkPhysicalDeviceFeatures::textureCompressionETC2`

Level 1 additionally includes:

- `VkPhysicalDeviceFeatures::fullDrawIndexUint32`
- `VkPhysicalDeviceFeatures::imageCubeArray`
- `VkPhysicalDeviceFeatures::independentBlend`
- `VkPhysicalDeviceFeatures::geometryShader`
- `VkPhysicalDeviceFeatures::tessellationShader`
- `VkPhysicalDeviceFeatures::sampleRateShading`
- `VkPhysicalDeviceFeatures::textureCompressionASTC_LDR`
- `VkPhysicalDeviceFeatures::fragmentStoresAndAtomics`
- `VkPhysicalDeviceFeatures::shaderImageGatherExtended`
- `VkPhysicalDeviceFeatures::shaderUniformBufferArrayDynamicIndexing`
- `VkPhysicalDeviceFeatures::shaderSampledImageArrayDynamicIndexing`

Constant Value: "android.hardware.vulkan.level"

### FEATURE_VULKAN_HARDWARE_VERSION   

    [API level 24](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final[String](https://developer.android.com/reference/java/lang/String)FEATURE_VULKAN_HARDWARE_VERSION

Feature for [getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures())[hasSystemFeature(String,int)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.lang.String,%20int))`VkPhysicalDeviceProperties::apiVersion` supported by the physical devices
 that support the hardware level indicated by [FEATURE_VULKAN_HARDWARE_LEVEL](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_VULKAN_HARDWARE_LEVEL)

- Major version number in bits 31-22
- Minor version number in bits 21-12
- Patch version number in bits 11-0

- The `VK_ANDROID_external_memory_android_hardware_buffer`extension is supported.
- `SYNC_FD`external semaphore and fence handles are supported.
- `VkPhysicalDeviceSamplerYcbcrConversionFeatures::samplerYcbcrConversion`is supported.

[Vulkan Design Guidelines](https://developer.android.com/ndk/guides/graphics/design-notes).

Constant Value: "android.hardware.vulkan.version"

### FEATURE_WALLET_LOCATION_BASED_SUGGESTIONS    

    [API level 34](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final[String](https://developer.android.com/reference/java/lang/String)FEATURE_WALLET_LOCATION_BASED_SUGGESTIONS

Feature for [getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures())[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.lang.String))

Constant Value: "android.software.wallet_location_based_suggestions"

### FEATURE_WATCH 

    [API level 20](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final[String](https://developer.android.com/reference/java/lang/String)FEATURE_WATCH

Feature for [getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures())[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.lang.String))

Constant Value: "android.hardware.type.watch"

### FEATURE_WEBVIEW 

    [API level 20](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final[String](https://developer.android.com/reference/java/lang/String)FEATURE_WEBVIEW

Feature for [getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures())[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.lang.String))

Constant Value: "android.software.webview"

### FEATURE_WIFI 

    [API level 8](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final[String](https://developer.android.com/reference/java/lang/String)FEATURE_WIFI

Feature for [getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures())[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.lang.String))

Constant Value: "android.hardware.wifi"

### FEATURE_WIFI_AWARE  

    [API level 26](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final[String](https://developer.android.com/reference/java/lang/String)FEATURE_WIFI_AWARE

Feature for [getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures())[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.lang.String))

Constant Value: "android.hardware.wifi.aware"

### FEATURE_WIFI_DIRECT  

    [API level 14](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final[String](https://developer.android.com/reference/java/lang/String)FEATURE_WIFI_DIRECT

Feature for [getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures())[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.lang.String))

Constant Value: "android.hardware.wifi.direct"

### FEATURE_WIFI_PASSPOINT  

    [API level 27](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final[String](https://developer.android.com/reference/java/lang/String)FEATURE_WIFI_PASSPOINT

Feature for [getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures())[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.lang.String))[WifiManager](https://developer.android.com/reference/android/net/wifi/WifiManager)[WifiManager.addOrUpdatePasspointConfiguration](https://developer.android.com/reference/android/net/wifi/WifiManager#addOrUpdatePasspointConfiguration(android.net.wifi.hotspot2.PasspointConfiguration))

Constant Value: "android.hardware.wifi.passpoint"

### FEATURE_WIFI_RTT  

    [API level 28](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final[String](https://developer.android.com/reference/java/lang/String)FEATURE_WIFI_RTT

Feature for [getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures())[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.lang.String))

Constant Value: "android.hardware.wifi.rtt"

### FEATURE_WINDOW_MAGNIFICATION  

    [API level 33](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final[String](https://developer.android.com/reference/java/lang/String)FEATURE_WINDOW_MAGNIFICATION

Feature for [getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures())[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.lang.String))

Constant Value: "android.software.window_magnification"

### FLAG_PERMISSION_WHITELIST_INSTALLER   

    [API level 29](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final int FLAG_PERMISSION_WHITELIST_INSTALLER

Permission whitelist flag: permissions whitelisted by the installer. Permissions can also be whitelisted by the system, on upgrade, or on role grant.

 **Note: **In retrospect it would have been preferred to use
 more inclusive terminology when naming this API. Similar APIs added will
 refrain from using the term "whitelist".
 

Constant Value: 2 (0x00000002)

### FLAG_PERMISSION_WHITELIST_SYSTEM   

    [API level 29](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final int FLAG_PERMISSION_WHITELIST_SYSTEM

Permission whitelist flag: permissions whitelisted by the system. Permissions can also be whitelisted by the installer, on upgrade, or on role grant.

 **Note: **In retrospect it would have been preferred to use
 more inclusive terminology when naming this API. Similar APIs added will
 refrain from using the term "whitelist".
 

Constant Value: 1 (0x00000001)

### FLAG_PERMISSION_WHITELIST_UPGRADE   

    [API level 29](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final int FLAG_PERMISSION_WHITELIST_UPGRADE

Permission whitelist flag: permissions whitelisted by the system when upgrading from an OS version where the permission was not restricted to an OS version where the permission is restricted. Permissions can also be whitelisted by the installer, the system, or on role grant.

 **Note: **In retrospect it would have been preferred to use
 more inclusive terminology when naming this API. Similar APIs added will
 refrain from using the term "whitelist".
 

Constant Value: 4 (0x00000004)

### GET_ACTIVITIES 

    [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final int GET_ACTIVITIES

[PackageInfo](https://developer.android.com/reference/android/content/pm/PackageInfo)[PackageInfo.activities](https://developer.android.com/reference/android/content/pm/PackageInfo#activities)

Constant Value: 1 (0x00000001)

### GET_ATTRIBUTIONS 

    
public static final int GET_ATTRIBUTIONS


**
      This constant was deprecated
      in API level 34.**

    Use [GET_ATTRIBUTIONS_LONG](https://developer.android.com/reference/android/content/pm/PackageManager#GET_ATTRIBUTIONS_LONG)[RuntimeException](https://developer.android.com/reference/java/lang/RuntimeException)

Constant Value: -2147483648 (0x80000000)

### GET_ATTRIBUTIONS_LONG  

    [API level 34](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final long GET_ATTRIBUTIONS_LONG

[PackageInfo](https://developer.android.com/reference/android/content/pm/PackageInfo)

Constant Value: 2147483648 (0x0000000080000000)

### GET_CONFIGURATIONS 

    [API level 3](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final int GET_CONFIGURATIONS

[PackageInfo](https://developer.android.com/reference/android/content/pm/PackageInfo)[PackageInfo.configPreferences](https://developer.android.com/reference/android/content/pm/PackageInfo#configPreferences)[PackageInfo.reqFeatures](https://developer.android.com/reference/android/content/pm/PackageInfo#reqFeatures)[PackageInfo.featureGroups](https://developer.android.com/reference/android/content/pm/PackageInfo#featureGroups)

Constant Value: 16384 (0x00004000)

### GET_DISABLED_COMPONENTS  

    
public static final int GET_DISABLED_COMPONENTS


**
      This constant was deprecated
      in API level 24.**

    replaced with [MATCH_DISABLED_COMPONENTS](https://developer.android.com/reference/android/content/pm/PackageManager#MATCH_DISABLED_COMPONENTS)

Constant Value: 512 (0x00000200)

### GET_DISABLED_UNTIL_USED_COMPONENTS    

    
public static final int GET_DISABLED_UNTIL_USED_COMPONENTS


**
      This constant was deprecated
      in API level 24.**

    replaced with [MATCH_DISABLED_UNTIL_USED_COMPONENTS](https://developer.android.com/reference/android/content/pm/PackageManager#MATCH_DISABLED_UNTIL_USED_COMPONENTS)

Constant Value: 32768 (0x00008000)

### GET_GIDS 

    [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final int GET_GIDS

[PackageInfo](https://developer.android.com/reference/android/content/pm/PackageInfo)[group ids](https://developer.android.com/reference/android/content/pm/PackageInfo#gids)

Constant Value: 256 (0x00000100)

### GET_INSTRUMENTATION 

    [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final int GET_INSTRUMENTATION

[PackageInfo](https://developer.android.com/reference/android/content/pm/PackageInfo)[PackageInfo.instrumentation](https://developer.android.com/reference/android/content/pm/PackageInfo#instrumentation)

Constant Value: 16 (0x00000010)

### GET_INTENT_FILTERS  

    
public static final int GET_INTENT_FILTERS


**
      This constant was deprecated
      in API level 31.**

    The platform does not support getting [IntentFilter](https://developer.android.com/reference/android/content/IntentFilter)

[PackageInfo](https://developer.android.com/reference/android/content/pm/PackageInfo)

Constant Value: 32 (0x00000020)

### GET_META_DATA  

    [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final int GET_META_DATA

[ComponentInfo](https://developer.android.com/reference/android/content/pm/ComponentInfo)[ComponentInfo.metaData](https://developer.android.com/reference/android/content/pm/PackageItemInfo#metaData)[Bundle](https://developer.android.com/reference/android/os/Bundle)

Constant Value: 128 (0x00000080)

### GET_PERMISSIONS 

    [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final int GET_PERMISSIONS

[PackageInfo](https://developer.android.com/reference/android/content/pm/PackageInfo)[PackageInfo.permissions](https://developer.android.com/reference/android/content/pm/PackageInfo#permissions)

Constant Value: 4096 (0x00001000)

### GET_PROVIDERS 

    [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final int GET_PROVIDERS

[PackageInfo](https://developer.android.com/reference/android/content/pm/PackageInfo)[PackageInfo.providers](https://developer.android.com/reference/android/content/pm/PackageInfo#providers)

Constant Value: 8 (0x00000008)

### GET_RECEIVERS 

    [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final int GET_RECEIVERS

[PackageInfo](https://developer.android.com/reference/android/content/pm/PackageInfo)[PackageInfo.receivers](https://developer.android.com/reference/android/content/pm/PackageInfo#receivers)

Constant Value: 2 (0x00000002)

### GET_RESOLVED_FILTER  

    [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final int GET_RESOLVED_FILTER

[ResolveInfo](https://developer.android.com/reference/android/content/pm/ResolveInfo)[ResolveInfo.filter](https://developer.android.com/reference/android/content/pm/ResolveInfo#filter)

Constant Value: 64 (0x00000040)

### GET_SERVICES 

    [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final int GET_SERVICES

[PackageInfo](https://developer.android.com/reference/android/content/pm/PackageInfo)[PackageInfo.services](https://developer.android.com/reference/android/content/pm/PackageInfo#services)

Constant Value: 4 (0x00000004)

### GET_SHARED_LIBRARY_FILES   

    [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final int GET_SHARED_LIBRARY_FILES

[ApplicationInfo](https://developer.android.com/reference/android/content/pm/ApplicationInfo)[paths to the shared libraries](https://developer.android.com/reference/android/content/pm/ApplicationInfo#sharedLibraryFiles)

Constant Value: 1024 (0x00000400)

### GET_SIGNATURES 

    
public static final int GET_SIGNATURES


**
      This constant was deprecated
      in API level 28.**

    use `GET_SIGNING_CERTIFICATES` instead
  

[PackageInfo](https://developer.android.com/reference/android/content/pm/PackageInfo)

Constant Value: 64 (0x00000040)

### GET_SIGNING_CERTIFICATES  

    [API level 28](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final int GET_SIGNING_CERTIFICATES

[PackageInfo](https://developer.android.com/reference/android/content/pm/PackageInfo)

Constant Value: 134217728 (0x08000000)

### GET_UNINSTALLED_PACKAGES  

    
public static final int GET_UNINSTALLED_PACKAGES


**
      This constant was deprecated
      in API level 24.**

    replaced with [MATCH_UNINSTALLED_PACKAGES](https://developer.android.com/reference/android/content/pm/PackageManager#MATCH_UNINSTALLED_PACKAGES)

Constant Value: 8192 (0x00002000)

### GET_URI_PERMISSION_PATTERNS   

    [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final int GET_URI_PERMISSION_PATTERNS

[ProviderInfo](https://developer.android.com/reference/android/content/pm/ProviderInfo)[URI permission patterns](https://developer.android.com/reference/android/content/pm/ProviderInfo#uriPermissionPatterns)

Constant Value: 2048 (0x00000800)

### INSTALL_REASON_DEVICE_RESTORE   

    [API level 26](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final int INSTALL_REASON_DEVICE_RESTORE

Code indicating that this package was installed as part of restoring from another device.

Constant Value: 2 (0x00000002)

### INSTALL_REASON_DEVICE_SETUP   

    [API level 26](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final int INSTALL_REASON_DEVICE_SETUP

Code indicating that this package was installed as part of device setup.

Constant Value: 3 (0x00000003)

### INSTALL_REASON_POLICY  

    [API level 26](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final int INSTALL_REASON_POLICY

Code indicating that this package was installed due to enterprise policy.

Constant Value: 1 (0x00000001)

### INSTALL_REASON_UNKNOWN  

    [API level 26](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final int INSTALL_REASON_UNKNOWN

Code indicating that the reason for installing this package is unknown.

Constant Value: 0 (0x00000000)

### INSTALL_REASON_USER  

    [API level 26](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final int INSTALL_REASON_USER

Code indicating that the package installation was initiated by the user.

Constant Value: 4 (0x00000004)

### INSTALL_SCENARIO_BULK  

    [API level 31](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final int INSTALL_SCENARIO_BULK

Installation scenario indicating a bulk operation with the desired result of a fully optimized application. If the system is busy or resources are scarce the system will perform less work to avoid impacting system health. Examples of bulk installation scenarios might include device restore, background updates of multiple applications, or user-triggered updates for all applications. The decision to use BULK or BULK_SECONDARY should be based on the desired user experience. BULK_SECONDARY operations may take less time to complete but, when they do, will produce less optimized applications. The device state (e.g. memory usage or battery status) should not be considered when making this decision as those factors are taken into account by the Package Manager when acting on the installation scenario.

Constant Value: 2 (0x00000002)

### INSTALL_SCENARIO_BULK_SECONDARY   

    [API level 31](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final int INSTALL_SCENARIO_BULK_SECONDARY

Installation scenario indicating a bulk operation that prioritizes minimal system health impact over application optimization. The application may undergo additional optimization if the system is idle and system resources are abundant. The more elements of a bulk operation that are marked BULK_SECONDARY, the faster the entire bulk operation will be. See the comments for INSTALL_SCENARIO_BULK for more information.

Constant Value: 3 (0x00000003)

### INSTALL_SCENARIO_DEFAULT  

    [API level 31](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final int INSTALL_SCENARIO_DEFAULT

A value to indicate the lack of CUJ information, disabling all installation scenario logic.

Constant Value: 0 (0x00000000)

### INSTALL_SCENARIO_FAST  

    [API level 31](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final int INSTALL_SCENARIO_FAST

Installation scenario providing the fastest "install button to launch" experience possible.

Constant Value: 1 (0x00000001)

### MATCH_ALL 

    [API level 23](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final int MATCH_ALL

Querying flag: if set and if the platform is doing any filtering of the results, then the filtering will not happen. This is a synonym for saying that all results should be returned.

 *This flag should be used with extreme care.*

Constant Value: 131072 (0x00020000)

### MATCH_APEX 

    [API level 29](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final int MATCH_APEX

[PackageInfo](https://developer.android.com/reference/android/content/pm/PackageInfo)

Constant Value: 1073741824 (0x40000000)

### MATCH_ARCHIVED_PACKAGES  

    [API level 35](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final long MATCH_ARCHIVED_PACKAGES

Flag parameter to also retrieve some information about archived packages.
 Packages can be archived through [PackageInstaller.requestArchive](https://developer.android.com/reference/android/content/pm/PackageInstaller#requestArchive(java.lang.String,%20android.content.IntentSender))

 Note: Archived apps are a subset of apps returned by [MATCH_UNINSTALLED_PACKAGES](https://developer.android.com/reference/android/content/pm/PackageManager#MATCH_UNINSTALLED_PACKAGES)

Note: this flag may cause less information about currently installed applications to be returned.

Note: use of this flag requires the android.permission.QUERY_ALL_PACKAGES permission to see uninstalled packages.

Constant Value: 4294967296 (0x0000000100000000)

### MATCH_DEFAULT_ONLY  

    [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final int MATCH_DEFAULT_ONLY

Resolution and querying flag: if set, only filters that support the
 [Intent.CATEGORY_DEFAULT](https://developer.android.com/reference/android/content/Intent#CATEGORY_DEFAULT)

Constant Value: 65536 (0x00010000)

### MATCH_DIRECT_BOOT_AUTO   

    [API level 29](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final int MATCH_DIRECT_BOOT_AUTO

Querying flag: automatically match components based on their Direct Boot awareness and the current user state.

Since the default behavior is to automatically apply the current user state, this is effectively a sentinel value that doesn't change the output of any queries based on its presence or absence.

 Instead, this value can be useful in conjunction with
 [StrictMode.VmPolicy.Builder.detectImplicitDirectBoot()](https://developer.android.com/reference/android/os/StrictMode.VmPolicy.Builder#detectImplicitDirectBoot())

Constant Value: 268435456 (0x10000000)

### MATCH_DIRECT_BOOT_AWARE   

    [API level 24](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final int MATCH_DIRECT_BOOT_AWARE

Querying flag: match components which are direct boot *aware* in
 the returned info, regardless of the current user state.
 

 When neither [MATCH_DIRECT_BOOT_AWARE](https://developer.android.com/reference/android/content/pm/PackageManager#MATCH_DIRECT_BOOT_AWARE)[MATCH_DIRECT_BOOT_UNAWARE](https://developer.android.com/reference/android/content/pm/PackageManager#MATCH_DIRECT_BOOT_UNAWARE)[MATCH_DIRECT_BOOT_AWARE](https://developer.android.com/reference/android/content/pm/PackageManager#MATCH_DIRECT_BOOT_AWARE)[MATCH_DIRECT_BOOT_AWARE](https://developer.android.com/reference/android/content/pm/PackageManager#MATCH_DIRECT_BOOT_AWARE)[MATCH_DIRECT_BOOT_UNAWARE](https://developer.android.com/reference/android/content/pm/PackageManager#MATCH_DIRECT_BOOT_UNAWARE)

**See also:**

Constant Value: 524288 (0x00080000)

### MATCH_DIRECT_BOOT_UNAWARE   

    [API level 24](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final int MATCH_DIRECT_BOOT_UNAWARE

Querying flag: match components which are direct boot *unaware* in
 the returned info, regardless of the current user state.
 

 When neither [MATCH_DIRECT_BOOT_AWARE](https://developer.android.com/reference/android/content/pm/PackageManager#MATCH_DIRECT_BOOT_AWARE)[MATCH_DIRECT_BOOT_UNAWARE](https://developer.android.com/reference/android/content/pm/PackageManager#MATCH_DIRECT_BOOT_UNAWARE)[MATCH_DIRECT_BOOT_AWARE](https://developer.android.com/reference/android/content/pm/PackageManager#MATCH_DIRECT_BOOT_AWARE)[MATCH_DIRECT_BOOT_AWARE](https://developer.android.com/reference/android/content/pm/PackageManager#MATCH_DIRECT_BOOT_AWARE)[MATCH_DIRECT_BOOT_UNAWARE](https://developer.android.com/reference/android/content/pm/PackageManager#MATCH_DIRECT_BOOT_UNAWARE)

**See also:**

Constant Value: 262144 (0x00040000)

### MATCH_DISABLED_COMPONENTS  

    [API level 24](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final int MATCH_DISABLED_COMPONENTS

[PackageInfo](https://developer.android.com/reference/android/content/pm/PackageInfo)

Constant Value: 512 (0x00000200)

### MATCH_DISABLED_UNTIL_USED_COMPONENTS    

    [API level 24](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final int MATCH_DISABLED_UNTIL_USED_COMPONENTS

[PackageInfo](https://developer.android.com/reference/android/content/pm/PackageInfo)[COMPONENT_ENABLED_STATE_DISABLED_UNTIL_USED](https://developer.android.com/reference/android/content/pm/PackageManager#COMPONENT_ENABLED_STATE_DISABLED_UNTIL_USED)

Constant Value: 32768 (0x00008000)

### MATCH_SYSTEM_ONLY  

    [API level 24](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final int MATCH_SYSTEM_ONLY

Querying flag: include only components from applications that are marked
 with [ApplicationInfo.FLAG_SYSTEM](https://developer.android.com/reference/android/content/pm/ApplicationInfo#FLAG_SYSTEM)

Constant Value: 1048576 (0x00100000)

### MATCH_UNINSTALLED_PACKAGES  

    [API level 24](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final int MATCH_UNINSTALLED_PACKAGES

Flag parameter to retrieve some information about all applications (even
 uninstalled ones) which have data directories. This state could have
 resulted if applications have been deleted with flag
 `DELETE_KEEP_DATA` with a possibility of being replaced or
 reinstalled in future.
 

Note: this flag may cause less information about currently installed applications to be returned.

Note: use of this flag requires the android.permission.QUERY_ALL_PACKAGES permission to see uninstalled packages.

Constant Value: 8192 (0x00002000)

### MAXIMUM_VERIFICATION_TIMEOUT  

    [API level 17](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final long MAXIMUM_VERIFICATION_TIMEOUT

Can be used as the `millisecondsToDelay` argument for
 [PackageManager.extendVerificationTimeout](https://developer.android.com/reference/android/content/pm/PackageManager#extendVerificationTimeout(int,%20int,%20long))`PackageManager` waits for the verification
 agent to return (in milliseconds).

Constant Value: 3600000 (0x000000000036ee80)

### PERMISSION_DENIED 

    [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final int PERMISSION_DENIED

Permission check result: this is returned by [checkPermission(String, String)](https://developer.android.com/reference/android/content/pm/PackageManager#checkPermission(java.lang.String,%20java.lang.String))

Constant Value: -1 (0xffffffff)

### PERMISSION_GRANTED 

    [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final int PERMISSION_GRANTED

Permission check result: this is returned by [checkPermission(String, String)](https://developer.android.com/reference/android/content/pm/PackageManager#checkPermission(java.lang.String,%20java.lang.String))

Constant Value: 0 (0x00000000)

### PROPERTY_COMPAT_OVERRIDE_LANDSCAPE_TO_PORTRAIT     

    [API level 34](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final[String](https://developer.android.com/reference/java/lang/String)PROPERTY_COMPAT_OVERRIDE_LANDSCAPE_TO_PORTRAIT

Application level [PackageManager
 .Property](https://developer.android.com/reference/android/content/pm/PackageManager.Property)

The treatment is disabled by default but device manufacturers can enable the treatment
 using their discretion to improve camera compatibility. With this property set to
 `false`, the rotation will not be applied. A value of `true`
 will ensure that rotation is applied, provided it is enabled for the device. In most cases,
 if rotation is the desired behavior this property need not be set. However, if your app
 experiences stretching or incorrect rotation on these devices, explicitly setting this to
 `true` may resolve that behavior. Apps should set this to `false` if there
 is confidence that the app handles
 [CameraCharacteristics.SENSOR_ORIENTATION](https://developer.android.com/reference/android/hardware/camera2/CameraCharacteristics#SENSOR_ORIENTATION)[ the
 documentation for best practice.](https://developer.android.com/training/camera2/camera-preview)
 

**Syntax:**
 

```
 <application>
   <property
     android:name="android.camera.PROPERTY_COMPAT_OVERRIDE_LANDSCAPE_TO_PORTRAIT"
     android:value="true|false"/>
 </application>
 
```
Constant Value: "android.camera.PROPERTY_COMPAT_OVERRIDE_LANDSCAPE_TO_PORTRAIT"

### PROPERTY_MEDIA_CAPABILITIES  

    [API level 31](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final[String](https://developer.android.com/reference/java/lang/String)PROPERTY_MEDIA_CAPABILITIES

<application> level [PackageManager.Property](https://developer.android.com/reference/android/content/pm/PackageManager.Property)

Constant Value: "android.media.PROPERTY_MEDIA_CAPABILITIES"

### PROPERTY_NATIVE_SERVICE_FUNCTION_NAME    

    [API level 37](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final[String](https://developer.android.com/reference/java/lang/String)PROPERTY_NATIVE_SERVICE_FUNCTION_NAME

Service level [PackageManager.Property](https://developer.android.com/reference/android/content/pm/PackageManager.Property)`ANativeService_onCreate`.
 

Example:

```
 <service android:isolatedProcess="true"
                   android:nativeService="true">
   <property
     android:name="android.app.PROPERTY_NATIVE_SERVICE_FUNCTION_NAME"
     android:value="native_service_createService"/>
 </service>
 
```
Constant Value: "android.app.PROPERTY_NATIVE_SERVICE_FUNCTION_NAME"

### PROPERTY_NATIVE_SERVICE_LIBRARY_NAME    

    [API level 37](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final[String](https://developer.android.com/reference/java/lang/String)PROPERTY_NATIVE_SERVICE_LIBRARY_NAME

Service level [PackageManager.Property](https://developer.android.com/reference/android/content/pm/PackageManager.Property)`libmain.so`.
 

Example:

```
 <service android:isolatedProcess="true"
                   android:nativeService="true">
   <property
     android:name="android.app.PROPERTY_NATIVE_SERVICE_LIBRARY_NAME"
     android:value="libnativeservice.so"/>
 </service>
 
```
Constant Value: "android.app.PROPERTY_NATIVE_SERVICE_LIBRARY_NAME"

### PROPERTY_SELF_CERTIFIED_NETWORK_CAPABILITIES    

    [API level 34](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final[String](https://developer.android.com/reference/java/lang/String)PROPERTY_SELF_CERTIFIED_NETWORK_CAPABILITIES

<application> level [PackageManager.Property](https://developer.android.com/reference/android/content/pm/PackageManager.Property)

 Starting from Android 14, usage of some network capabilities in
 [ConnectivityManager.requestNetwork(NetworkRequest, PendingIntent)](https://developer.android.com/reference/android/net/ConnectivityManager#requestNetwork(android.net.NetworkRequest,%20android.app.PendingIntent))[NetworkCapabilities](https://developer.android.com/reference/android/net/NetworkCapabilities)

 The detail format of self_certified_network_capabilities.xml is described in
 [NetworkRequest](https://developer.android.com/reference/android/net/NetworkRequest)

Constant Value: "android.net.PROPERTY_SELF_CERTIFIED_NETWORK_CAPABILITIES"

### PROPERTY_SPECIAL_USE_FGS_SUBTYPE    

    [API level 34](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final[String](https://developer.android.com/reference/java/lang/String)PROPERTY_SPECIAL_USE_FGS_SUBTYPE

<service> level [PackageManager.Property](https://developer.android.com/reference/android/content/pm/PackageManager.Property)[ServiceInfo.FOREGROUND_SERVICE_TYPE_SPECIAL_USE](https://developer.android.com/reference/android/content/pm/ServiceInfo#FOREGROUND_SERVICE_TYPE_SPECIAL_USE)

For example: <service> <property android:name="android.app.PROPERTY_SPECIAL_USE_FGS_SUBTYPE" android:value="foo"/> </service>

Constant Value: "android.app.PROPERTY_SPECIAL_USE_FGS_SUBTYPE"

### PROPERTY_USE_RESTRICTED_BACKUP_MODE    

    [API level 36](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final[String](https://developer.android.com/reference/java/lang/String)PROPERTY_USE_RESTRICTED_BACKUP_MODE

<application> level [PackageManager.Property](https://developer.android.com/reference/android/content/pm/PackageManager.Property)

 See [ for
 information about restricted mode](https://developer.android.com/identity/data/autobackup#ImplementingBackupAgent).
 

Starting with Android 16 apps may not be started in restricted mode based on this property.

**Syntax:**
 

```
 <application>
   <property
     android:name="android.app.backup.PROPERTY_USE_RESTRICTED_BACKUP_MODE"
     android:value="true|false"/>
 </application>
 
```
If this property is set, the operating system will respect it for now (see Note below).
 If it's not set, the behavior depends on the SDK level that the app is targeting. For apps
 targeting SDK level [Build.VERSION_CODES.VANILLA_ICE_CREAM](https://developer.android.com/reference/android/os/Build.VERSION_CODES#VANILLA_ICE_CREAM)`true`. For apps targeting SDK level
 [Build.VERSION_CODES.BAKLAVA](https://developer.android.com/reference/android/os/Build.VERSION_CODES#BAKLAVA)

Note: It's not recommended to set this property to `true` unless absolutely
 necessary. In a future Android version, this property may be deprecated in favor of removing
 restricted mode completely.

Constant Value: "android.app.backup.PROPERTY_USE_RESTRICTED_BACKUP_MODE"

### SIGNATURE_FIRST_NOT_SIGNED   

    [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final int SIGNATURE_FIRST_NOT_SIGNED

Signature check result: this is returned by [checkSignatures(int, int)](https://developer.android.com/reference/android/content/pm/PackageManager#checkSignatures(int,%20int))

Constant Value: -1 (0xffffffff)

### SIGNATURE_MATCH 

    [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final int SIGNATURE_MATCH

Signature check result: this is returned by [checkSignatures(int, int)](https://developer.android.com/reference/android/content/pm/PackageManager#checkSignatures(int,%20int))

Constant Value: 0 (0x00000000)

### SIGNATURE_NEITHER_SIGNED  

    [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final int SIGNATURE_NEITHER_SIGNED

Signature check result: this is returned by [checkSignatures(int, int)](https://developer.android.com/reference/android/content/pm/PackageManager#checkSignatures(int,%20int))

Constant Value: 1 (0x00000001)

### SIGNATURE_NO_MATCH  

    [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final int SIGNATURE_NO_MATCH

Signature check result: this is returned by [checkSignatures(int, int)](https://developer.android.com/reference/android/content/pm/PackageManager#checkSignatures(int,%20int))

Constant Value: -3 (0xfffffffd)

### SIGNATURE_SECOND_NOT_SIGNED   

    [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final int SIGNATURE_SECOND_NOT_SIGNED

Signature check result: this is returned by [checkSignatures(int, int)](https://developer.android.com/reference/android/content/pm/PackageManager#checkSignatures(int,%20int))

Constant Value: -2 (0xfffffffe)

### SIGNATURE_UNKNOWN_PACKAGE  

    [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final int SIGNATURE_UNKNOWN_PACKAGE

Signature check result: this is returned by [checkSignatures(int, int)](https://developer.android.com/reference/android/content/pm/PackageManager#checkSignatures(int,%20int))

Constant Value: -4 (0xfffffffc)

### SYNCHRONOUS

[API level 30](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final int SYNCHRONOUS

Flag parameter for
 [setComponentEnabledSetting(android.content.ComponentName, int, int)](https://developer.android.com/reference/android/content/pm/PackageManager#setComponentEnabledSetting(android.content.ComponentName,%20int,%20int))

Constant Value: 2 (0x00000002)

### VERIFICATION_ALLOW 

    [API level 14](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final int VERIFICATION_ALLOW

Used as the `verificationCode` argument for
 [PackageManager.verifyPendingInstall](https://developer.android.com/reference/android/content/pm/PackageManager#verifyPendingInstall(int,%20int))

Constant Value: 1 (0x00000001)

### VERIFICATION_REJECT 

    [API level 14](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final int VERIFICATION_REJECT

Used as the `verificationCode` argument for
 [PackageManager.verifyPendingInstall](https://developer.android.com/reference/android/content/pm/PackageManager#verifyPendingInstall(int,%20int))

Constant Value: -1 (0xffffffff)

### VERSION_CODE_HIGHEST  

    [API level 26](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final int VERSION_CODE_HIGHEST

Constant for specifying the highest installed package version code.

Constant Value: -1 (0xffffffff)

## Fields

### TRUST_ALL 

    [API level 31](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final[List](https://developer.android.com/reference/java/util/List)<[Certificate](https://developer.android.com/reference/java/security/cert/Certificate)> TRUST_ALL

Trust any Installer to provide checksums for the package.

### TRUST_NONE 

    [API level 31](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static final[List](https://developer.android.com/reference/java/util/List)<[Certificate](https://developer.android.com/reference/java/security/cert/Certificate)> TRUST_NONE

Don't trust any Installer to provide checksums for the package. This effectively disables optimized Installer-enforced checksums.

## Public constructors

### PackageManager 

    [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public PackageManager ()


**
      This constructor is deprecated.**

    Do not instantiate or subclass - obtain an instance from
 [Context.getPackageManager](https://developer.android.com/reference/android/content/Context#getPackageManager())

## Public methods

### addPackageToPreferred   

    public abstract void addPackageToPreferred ([String](https://developer.android.com/reference/java/lang/String)packageName)


**
      This method was deprecated
      in API level 15.**

    This function no longer does anything. It is the platform's
 responsibility to assign preferred activities and this cannot be modified
 directly. To determine the activities resolved by the platform, use
 [resolveActivity(Intent, ResolveInfoFlags)](https://developer.android.com/reference/android/content/pm/PackageManager#resolveActivity(android.content.Intent,%20android.content.pm.PackageManager.ResolveInfoFlags))[queryIntentActivities(Intent, ResolveInfoFlags)](https://developer.android.com/reference/android/content/pm/PackageManager#queryIntentActivities(android.content.Intent,%20android.content.pm.PackageManager.ResolveInfoFlags))[RoleManager](https://developer.android.com/reference/android/app/role/RoleManager)

| Parameters | |
|---|---|
| `package` | `String`: This value cannot be`null`. | 

### addPermission 

    [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public abstract boolean addPermission ([PermissionInfo](https://developer.android.com/reference/android/content/pm/PermissionInfo)info)

Add a new dynamic permission to the system.  For this to work, your
 package must have defined a permission tree through the
 [<permission-tree>](https://developer.android.com/reference/android/R.styleable#AndroidManifestPermissionTree)

It is good to make your permission tree name descriptive, because you are taking possession of that entire set of permission names. Thus, it must be under a domain you control, with a suffix that will not match any normal permissions that may be declared in any applications that are part of that domain.

New permissions must be added before any .apks are installed that use those permissions. Permissions you add through this method are remembered across reboots of the device. If the given permission already exists, the info you supply here will be used to update it.

| Parameters | |
|---|---|
| `info` | `Permission`: Description of the permission to be added.This value cannot be `null`. | 

| Returns | |
|---|---|
| `boolean` | Returns true if a new permission was created, false if an existing one was updated. | 

| Throws | |
|---|---|
|  | if you are not allowed to add the given permission name. | 

**See also:**

### addPermissionAsync  

    [API level 8](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public abstract boolean addPermissionAsync ([PermissionInfo](https://developer.android.com/reference/android/content/pm/PermissionInfo)info)

Like [addPermission(PermissionInfo)](https://developer.android.com/reference/android/content/pm/PackageManager#addPermission(android.content.pm.PermissionInfo))

| Parameters | |
|---|---|
| `info` | `Permission`: This value cannot be`null`. | 

| Returns | |
|---|---|
| `boolean` | |

### addPreferredActivity  

    public abstract void addPreferredActivity ([IntentFilter](https://developer.android.com/reference/android/content/IntentFilter)filter, int match,[ComponentName[]](https://developer.android.com/reference/android/content/ComponentName)set,[ComponentName](https://developer.android.com/reference/android/content/ComponentName)activity)


**
      This method was deprecated
      in API level 15.**

    This function no longer does anything. It is the platform's
 responsibility to assign preferred activities and this cannot be modified
 directly. To determine the activities resolved by the platform, use
 [resolveActivity(Intent, ResolveInfoFlags)](https://developer.android.com/reference/android/content/pm/PackageManager#resolveActivity(android.content.Intent,%20android.content.pm.PackageManager.ResolveInfoFlags))[queryIntentActivities(Intent, ResolveInfoFlags)](https://developer.android.com/reference/android/content/pm/PackageManager#queryIntentActivities(android.content.Intent,%20android.content.pm.PackageManager.ResolveInfoFlags))[RoleManager](https://developer.android.com/reference/android/app/role/RoleManager)

Add a new preferred activity mapping to the system.  This will be used
 to automatically select the given activity component when
 [Context.startActivity()](https://developer.android.com/reference/android/content/Context#startActivity(android.content.Intent))

| Parameters | |
|---|---|
| `filter` | `Intent`: The set of intents under which this activity will be
 made preferred.This value cannot be `null`. | 
| `match` | `int`: The IntentFilter match category that this preference
 applies to. | 
| `set` | `Component`: The set of activities that the user was picking from when
 this preference was made.This value may be `null`. | 
| `activity` | `Component`: The component name of the activity that is to be
 preferred.This value cannot be `null`. | 

### addWhitelistedRestrictedPermission   

    [API level 29](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public boolean addWhitelistedRestrictedPermission ([String](https://developer.android.com/reference/java/lang/String)packageName,[String](https://developer.android.com/reference/java/lang/String)permName, int whitelistFlags)

Adds a whitelisted restricted permission for an app.

 Permissions can be hard restricted which means that the app cannot hold
 them or soft restricted where the app can hold the permission but in a weaker
 form. Whether a permission is [hard
 restricted](https://developer.android.com/reference/android/content/pm/PermissionInfo#FLAG_HARD_RESTRICTED)[soft restricted](https://developer.android.com/reference/android/content/pm/PermissionInfo#FLAG_SOFT_RESTRICTED)

- There are four whitelists:
 
- one for cases where the system permission policy whitelists a permission
 This list corresponds to the [FLAG_PERMISSION_WHITELIST_SYSTEM](https://developer.android.com/reference/android/content/pm/PackageManager#FLAG_PERMISSION_WHITELIST_SYSTEM)
- one for cases where the system whitelists the permission when upgrading
 from an OS version in which the permission was not restricted to an OS version
 in which the permission is restricted. This list corresponds to the [FLAG_PERMISSION_WHITELIST_UPGRADE](https://developer.android.com/reference/android/content/pm/PackageManager#FLAG_PERMISSION_WHITELIST_UPGRADE)
- one for cases where the installer of the package whitelists a permission.
 This list corresponds to the [FLAG_PERMISSION_WHITELIST_INSTALLER](https://developer.android.com/reference/android/content/pm/PackageManager#FLAG_PERMISSION_WHITELIST_INSTALLER)

You need to specify the whitelists for which to set the whitelisted permissions which will clear the previous whitelisted permissions and replace them with the provided ones.

 **Note: **In retrospect it would have been preferred to use
 more inclusive terminology when naming this API. Similar APIs added will
 refrain from using the term "whitelist".
 

| Parameters | |
|---|---|
| `package` | `String`: The app for which to get whitelisted permissions.This value cannot be `null`. | 
| `perm` | `String`: The whitelisted permission to add.This value cannot be `null`. | 
| `whitelist` | `int`: The whitelists to which to add. Passing multiple flags
 updates all specified whitelists.Value is either `0`or a combination of the following: | 

| Returns | |
|---|---|
| `boolean` | Whether the permission was added to the whitelist. | 

| Throws | |
|---|---|
|  | if you try to modify a whitelist that you have no access to. | 

### canPackageQuery  

    [API level 33](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public boolean canPackageQuery ([String](https://developer.android.com/reference/java/lang/String)sourcePackageName,[String](https://developer.android.com/reference/java/lang/String)targetPackageName)

Returns `true` if the source package is able to query for details about the
 target package. Applications that share details about other applications should
 use this API to determine if those details should be withheld from callers that
 do not otherwise have visibility of them.
 

 Note: The caller must be able to query for details about the source and target
 package. A [NameNotFoundException](https://developer.android.com/reference/android/content/pm/PackageManager.NameNotFoundException)

| Parameters | |
|---|---|
| `source` | `String`: The source package that would receive details about the
                          target package.This value cannot be `null`. | 
| `target` | `String`: The target package whose details would be shared with the
                          source package.This value cannot be `null`. | 

| Returns | |
|---|---|
| `boolean` | `true`if the source package is able to query for details about the
 target package. | 

| Throws | |
|---|---|
|  | if either a given package can not be found on the system, or if the caller is not able to query for details about the source or target package. | 

### canPackageQuery  

    [API level 34](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public boolean[] canPackageQuery ([String](https://developer.android.com/reference/java/lang/String)sourcePackageName,[String[]](https://developer.android.com/reference/java/lang/String)targetPackageNames)

Same as [canPackageQuery(String,String)](https://developer.android.com/reference/android/content/pm/PackageManager#canPackageQuery(java.lang.String,%20java.lang.String))

| Parameters | |
|---|---|
| `source` | `String`: The source package that would receive details about the
                          target package.This value cannot be `null`. | 
| `target` | `String`: An array of target packages whose details would be shared with the
                           source package.This value cannot be `null`. | 

| Returns | |
|---|---|
| `boolean[]` | An array of booleans where each member specifies whether the source package is able
 to query for details about the target package given by the corresponding value at the same
 index in the array of target packages. This value cannot be `null`. | 

| Throws | |
|---|---|
|  | if either a given package can not be found on the system, or if the caller is not able to query for details about the source or target packages. | 

### canRequestPackageInstalls   

    [API level 26](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public abstract boolean canRequestPackageInstalls ()

Checks whether the calling package is allowed to request package installs through package
 installer. Apps are encouraged to call this API before launching the package installer via
 intent [Intent.ACTION_INSTALL_PACKAGE](https://developer.android.com/reference/android/content/Intent#ACTION_INSTALL_PACKAGE)[Manifest.permission.REQUEST_INSTALL_PACKAGES](https://developer.android.com/reference/android/Manifest.permission#REQUEST_INSTALL_PACKAGES)

| Returns | |
|---|---|
| `boolean` | true if the calling package is trusted by the user to request install packages on the device, false otherwise. | 

### canonicalToCurrentPackageNames    

    [API level 8](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public abstract[String[]](https://developer.android.com/reference/java/lang/String)canonicalToCurrentPackageNames ([String[]](https://developer.android.com/reference/java/lang/String)packageNames)

Map from a packages canonical name to the current name in use on the device.

| Parameters | |
|---|---|
| `package` | `String`: Array of new names to be mapped.This value cannot be `null`. | 

| Returns | |
|---|---|
|  | Returns an array of the same size as the original, containing the current name for each package. | 

### checkPermission 

    [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public abstract int checkPermission ([String](https://developer.android.com/reference/java/lang/String)permName,[String](https://developer.android.com/reference/java/lang/String)packageName)

Check whether a particular package has been granted a particular permission.

 **Note: **This API returns the underlying permission state
 as-is and is mostly intended for permission managing system apps. To
 perform an access check for a certain app, please use the
 [Context.checkPermission](https://developer.android.com/reference/android/content/Context#checkPermission(java.lang.String,%20int,%20int))

| Parameters | |
|---|---|
| `perm` | `String`: The name of the permission you are checking for.This value cannot be `null`. | 
| `package` | `String`: The name of the package you are checking against.This value cannot be `null`. | 

| Returns | |
|---|---|
| `int` | If the package has the permission, PERMISSION_GRANTED is
 returned.  If it does not have the permission, PERMISSION_DENIED
 is returned. Value is one of the following: | 

**See also:**

### checkSignatures 

    [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public abstract int checkSignatures ([String](https://developer.android.com/reference/java/lang/String)packageName1,[String](https://developer.android.com/reference/java/lang/String)packageName2)

Compare the signatures of two packages to determine if the same signature appears in both of them. If they do contain the same signature, then they are allowed special privileges when working with each other: they can share the same user-id, run instrumentation against each other, etc.

| Parameters | |
|---|---|
| `package` | `String`: First package name whose signature will be compared.This value cannot be `null`. | 
| `package` | `String`: Second package name whose signature will be compared.This value cannot be `null`. | 

| Returns | |
|---|---|
| `int` | Returns an integer indicating whether all signatures on the
 two packages match. The value is >= 0 ( ) if
 all signatures match or < 0 if there is not a match (or).Value is one of the following: | 

**See also:**

### checkSignatures 

    [API level 5](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

```
public abstract int checkSignatures (int uid1, 
                int uid2)
```
Like [checkSignatures(String,String)](https://developer.android.com/reference/android/content/pm/PackageManager#checkSignatures(java.lang.String,%20java.lang.String))

| Parameters | |
|---|---|
| `uid1` | `int`: First UID whose signature will be compared. | 
| `uid2` | `int`: Second UID whose signature will be compared. | 

| Returns | |
|---|---|
| `int` | Returns an integer indicating whether all signatures on the
 two packages match. The value is >= 0 ( ) if
 all signatures match or < 0 if there is not a match (or).Value is one of the following: | 

**See also:**

### clearInstantAppCookie   

    [API level 26](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public abstract void clearInstantAppCookie ()

Clears the instant application cookie for the calling app.

### clearPackagePreferredActivities   

    public abstract void clearPackagePreferredActivities ([String](https://developer.android.com/reference/java/lang/String)packageName)


**
      This method was deprecated
      in API level 29.**

    This function no longer does anything. It is the platform's
 responsibility to assign preferred activities and this cannot be modified
 directly. To determine the activities resolved by the platform, use
 [resolveActivity(Intent, ResolveInfoFlags)](https://developer.android.com/reference/android/content/pm/PackageManager#resolveActivity(android.content.Intent,%20android.content.pm.PackageManager.ResolveInfoFlags))[queryIntentActivities(Intent, ResolveInfoFlags)](https://developer.android.com/reference/android/content/pm/PackageManager#queryIntentActivities(android.content.Intent,%20android.content.pm.PackageManager.ResolveInfoFlags))[RoleManager](https://developer.android.com/reference/android/app/role/RoleManager)

Remove all preferred activity mappings, previously added with
 [addPreferredActivity(IntentFilter, int, ComponentName, ComponentName)](https://developer.android.com/reference/android/content/pm/PackageManager#addPreferredActivity(android.content.IntentFilter,%20int,%20android.content.ComponentName[],%20android.content.ComponentName))

| Parameters | |
|---|---|
| `package` | `String`: The name of the package whose preferred activity
 mappings are to be removed.This value cannot be `null`. | 

### currentToCanonicalPackageNames    

    [API level 8](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public abstract[String[]](https://developer.android.com/reference/java/lang/String)currentToCanonicalPackageNames ([String[]](https://developer.android.com/reference/java/lang/String)packageNames)

Map from the current package names in use on the device to whatever the current canonical name of that package is.

| Parameters | |
|---|---|
| `package` | `String`: Array of current names to be mapped.This value cannot be `null`. | 

| Returns | |
|---|---|
|  | Returns an array of the same size as the original, containing the canonical name for each package. | 

### extendVerificationTimeout  

    [API level 17](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

```
public abstract void extendVerificationTimeout (int id, 
                int verificationCodeAtTimeout, 
                long millisecondsToDelay)
```
Allows a package listening to the
 [package verification
 broadcast](https://developer.android.com/reference/android/content/Intent#ACTION_PACKAGE_NEEDS_VERIFICATION)`verificationCodeAtTimeout` which is one of
 [PackageManager.VERIFICATION_ALLOW](https://developer.android.com/reference/android/content/pm/PackageManager#VERIFICATION_ALLOW)[PackageManager.VERIFICATION_REJECT](https://developer.android.com/reference/android/content/pm/PackageManager#VERIFICATION_REJECT)[PackageManager.MAXIMUM_VERIFICATION_TIMEOUT](https://developer.android.com/reference/android/content/pm/PackageManager#MAXIMUM_VERIFICATION_TIMEOUT)`verificationCodeAtTimeout`, then previous
 `verificationCodeAtTimeout` will be ignored and only the latest one will take effect.
 If this method is called after calling [PackageManager.verifyPendingInstall](https://developer.android.com/reference/android/content/pm/PackageManager#verifyPendingInstall(int,%20int))

| Parameters | |
|---|---|
| `id` | `int`: pending package identifier as passed via theIntent extra. | 
| `verification` | `int`: eitheror. If`verification`is neitheror, then`verification`will default to. | 
| `milliseconds` | `long`: the amount of time requested for the timeout.
            Must be positive and less than. If`milliseconds`is out of bounds,`milliseconds`will be set to the closest in
            bounds value; namely, 0 or. | 

| Throws | |
|---|---|
|  | if the caller does not have the PACKAGE_VERIFICATION_AGENT permission. | 

### getActivityBanner  

    [API level 20](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public abstract[Drawable](https://developer.android.com/reference/android/graphics/drawable/Drawable)getActivityBanner ([ComponentName](https://developer.android.com/reference/android/content/ComponentName)activityName)

Retrieve the banner associated with an activity. Given the full name of
 an activity, retrieves the information about it and calls
 [ComponentInfo.loadIcon()](https://developer.android.com/reference/android/content/pm/PackageItemInfo#loadIcon(android.content.pm.PackageManager))

| Parameters | |
|---|---|
| `activity` | `Component`: Name of the activity whose banner is to be retrieved.This value cannot be `null`. | 

| Returns | |
|---|---|
|  | Returns the image of the banner, or null if the activity has no banner specified. | 

| Throws | |
|---|---|
|  | Thrown if the resources for the given activity could not be loaded. | 

**See also:**

### getActivityBanner  

    [API level 20](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public abstract[Drawable](https://developer.android.com/reference/android/graphics/drawable/Drawable)getActivityBanner ([Intent](https://developer.android.com/reference/android/content/Intent)intent)

Retrieve the banner associated with an Intent. If intent.getClassName() is set, this simply returns the result of getActivityBanner(intent.getClassName()). Otherwise it resolves the intent's component and returns the banner associated with the resolved component. If intent.getClassName() cannot be found or the Intent cannot be resolved to a component, NameNotFoundException is thrown.

| Parameters | |
|---|---|
| `intent` | `Intent`: The intent for which you would like to retrieve a banner.This value cannot be `null`. | 

| Returns | |
|---|---|
|  | Returns the image of the banner, or null if the activity has no banner specified. | 

| Throws | |
|---|---|
|  | Thrown if the resources for application matching the given intent could not be loaded. | 

**See also:**

### getActivityIcon  

    [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public abstract[Drawable](https://developer.android.com/reference/android/graphics/drawable/Drawable)getActivityIcon ([Intent](https://developer.android.com/reference/android/content/Intent)intent)

Retrieve the icon associated with an Intent. If intent.getClassName() is set, this simply returns the result of getActivityIcon(intent.getClassName()). Otherwise it resolves the intent's component and returns the icon associated with the resolved component. If intent.getClassName() cannot be found or the Intent cannot be resolved to a component, NameNotFoundException is thrown.

| Parameters | |
|---|---|
| `intent` | `Intent`: The intent for which you would like to retrieve an icon.This value cannot be `null`. | 

| Returns | |
|---|---|
|  | Returns the image of the icon, or the default activity icon if it could not be found. Does not return null. | 

| Throws | |
|---|---|
|  | Thrown if the resources for application matching the given intent could not be loaded. | 

**See also:**

### getActivityIcon  

    [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public abstract[Drawable](https://developer.android.com/reference/android/graphics/drawable/Drawable)getActivityIcon ([ComponentName](https://developer.android.com/reference/android/content/ComponentName)activityName)

Retrieve the icon associated with an activity.  Given the full name of
 an activity, retrieves the information about it and calls
 [ComponentInfo.loadIcon()](https://developer.android.com/reference/android/content/pm/PackageItemInfo#loadIcon(android.content.pm.PackageManager))

| Parameters | |
|---|---|
| `activity` | `Component`: Name of the activity whose icon is to be retrieved.This value cannot be `null`. | 

| Returns | |
|---|---|
|  | Returns the image of the icon, or the default activity icon if it could not be found. Does not return null. | 

| Throws | |
|---|---|
|  | Thrown if the resources for the given activity could not be loaded. | 

**See also:**

### getActivityInfo  

    [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public abstract[ActivityInfo](https://developer.android.com/reference/android/content/pm/ActivityInfo)getActivityInfo ([ComponentName](https://developer.android.com/reference/android/content/ComponentName)component, int flags)

Retrieve all of the information we know about a particular activity
 class.
 Use [getActivityInfo(ComponentName,ComponentInfoFlags)](https://developer.android.com/reference/android/content/pm/PackageManager#getActivityInfo(android.content.ComponentName,%20android.content.pm.PackageManager.ComponentInfoFlags))

| Parameters | |
|---|---|
| `component` | `Component`: The full component name (i.e.
            com.google.apps.contacts/com.google.apps.contacts.
            ContactsList) of an Activity class.This value cannot be `null`. | 
| `flags` | `int`: Additional option flags to modify the data returned. | 

| Returns | |
|---|---|
|  | An containing information about the
         activity.This value cannot be `null`. | 

| Throws | |
|---|---|
|  | if a package with the given name cannot be found on the system. | 

### getActivityInfo  

    [API level 33](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public[ActivityInfo](https://developer.android.com/reference/android/content/pm/ActivityInfo)getActivityInfo ([ComponentName](https://developer.android.com/reference/android/content/ComponentName)component,[PackageManager.ComponentInfoFlags](https://developer.android.com/reference/android/content/pm/PackageManager.ComponentInfoFlags)flags)

See [getActivityInfo(ComponentName,int)](https://developer.android.com/reference/android/content/pm/PackageManager#getActivityInfo(android.content.ComponentName,%20int))

| Parameters | |
|---|---|
| `component` | `Component`: This value cannot be`null`. | 
| `flags` | `Package`: This value cannot be`null`. | 

| Returns | |
|---|---|
|  | This value cannot be `null`. | 

### getActivityLogo  

    [API level 9](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public abstract[Drawable](https://developer.android.com/reference/android/graphics/drawable/Drawable)getActivityLogo ([Intent](https://developer.android.com/reference/android/content/Intent)intent)

Retrieve the logo associated with an Intent. If intent.getClassName() is set, this simply returns the result of getActivityLogo(intent.getClassName()). Otherwise it resolves the intent's component and returns the logo associated with the resolved component. If intent.getClassName() cannot be found or the Intent cannot be resolved to a component, NameNotFoundException is thrown.

| Parameters | |
|---|---|
| `intent` | `Intent`: The intent for which you would like to retrieve a logo.This value cannot be `null`. | 

| Returns | |
|---|---|
|  | Returns the image of the logo, or null if the activity has no logo specified. | 

| Throws | |
|---|---|
|  | Thrown if the resources for application matching the given intent could not be loaded. | 

**See also:**

### getActivityLogo  

    [API level 9](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public abstract[Drawable](https://developer.android.com/reference/android/graphics/drawable/Drawable)getActivityLogo ([ComponentName](https://developer.android.com/reference/android/content/ComponentName)activityName)

Retrieve the logo associated with an activity. Given the full name of an
 activity, retrieves the information about it and calls
 [ComponentInfo.loadLogo()](https://developer.android.com/reference/android/content/pm/PackageItemInfo#loadLogo(android.content.pm.PackageManager))

| Parameters | |
|---|---|
| `activity` | `Component`: Name of the activity whose logo is to be retrieved.This value cannot be `null`. | 

| Returns | |
|---|---|
|  | Returns the image of the logo or null if the activity has no logo specified. | 

| Throws | |
|---|---|
|  | Thrown if the resources for the given activity could not be loaded. | 

**See also:**

### getAllPermissionGroups   

    [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public abstract[List](https://developer.android.com/reference/java/util/List)<[PermissionGroupInfo](https://developer.android.com/reference/android/content/pm/PermissionGroupInfo)> getAllPermissionGroups (int flags)

Retrieve all of the known permission groups in the system.

| Parameters | |
|---|---|
| `flags` | `int`: Additional option flags to modify the data returned.Value is either `0`or | 

| Returns | |
|---|---|
|  | Returns a list of containing
         information about all of the known permission groups.This value cannot be `null`. | 

### getAppUidForPrivateComputeCoreUid       

    [API level 37](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public int getAppUidForPrivateComputeCoreUid (int pccUid)

Maps a Private Compute Core (PCC) UID to its corresponding application UID.

| Parameters | |
|---|---|
| `pcc` | `int`: The PCC UID to map. | 

| Returns | |
|---|---|
| `int` | The corresponding application UID, or if the
         provided UID is not a valid PCC UID or no mapping exists. | 

### getApplicationBanner  

    [API level 20](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public abstract[Drawable](https://developer.android.com/reference/android/graphics/drawable/Drawable)getApplicationBanner ([String](https://developer.android.com/reference/java/lang/String)packageName)

Retrieve the banner associated with an application. Given the name of the application's package, retrieves the information about it and calls getApplicationIcon() to return its banner. If the application cannot be found, NameNotFoundException is thrown.

| Parameters | |
|---|---|
| `package` | `String`: Name of the package whose application banner is to be
            retrieved.This value cannot be `null`. | 

| Returns | |
|---|---|
|  | Returns the image of the banner or null if the application has no banner specified. | 

| Throws | |
|---|---|
|  | Thrown if the resources for the given application could not be loaded. | 

**See also:**

### getApplicationBanner  

    [API level 20](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public abstract[Drawable](https://developer.android.com/reference/android/graphics/drawable/Drawable)getApplicationBanner ([ApplicationInfo](https://developer.android.com/reference/android/content/pm/ApplicationInfo)info)

Retrieve the banner associated with an application.

| Parameters | |
|---|---|
| `info` | `Application`: Information about application being queried.This value cannot be `null`. | 

| Returns | |
|---|---|
|  | Returns the image of the banner or null if the application has no banner specified. | 

**See also:**

### getApplicationEnabledSetting   

    [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public abstract int getApplicationEnabledSetting ([String](https://developer.android.com/reference/java/lang/String)packageName)

Return the enabled setting for an application. This returns
 the last value set by
 [setApplicationEnabledSetting(String,int,int)](https://developer.android.com/reference/android/content/pm/PackageManager#setApplicationEnabledSetting(java.lang.String,%20int,%20int))[COMPONENT_ENABLED_STATE_DEFAULT](https://developer.android.com/reference/android/content/pm/PackageManager#COMPONENT_ENABLED_STATE_DEFAULT)

| Parameters | |
|---|---|
| `package` | `String`: The package name of the application to retrieve.This value cannot be `null`. | 

| Returns | |
|---|---|
| `int` | Returns the current enabled state for the application. Value is one of the following: | 

| Throws | |
|---|---|
|  | if the named package does not exist. | 

### getApplicationIcon  

    [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public abstract[Drawable](https://developer.android.com/reference/android/graphics/drawable/Drawable)getApplicationIcon ([ApplicationInfo](https://developer.android.com/reference/android/content/pm/ApplicationInfo)info)

Retrieve the icon associated with an application. If it has not defined an icon, the default app icon is returned. Does not return null.

| Parameters | |
|---|---|
| `info` | `Application`: Information about application being queried.This value cannot be `null`. | 

| Returns | |
|---|---|
|  | Returns the image of the icon, or the default application icon if it could not be found. | 

**See also:**

### getApplicationIcon  

    [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public abstract[Drawable](https://developer.android.com/reference/android/graphics/drawable/Drawable)getApplicationIcon ([String](https://developer.android.com/reference/java/lang/String)packageName)

Retrieve the icon associated with an application. Given the name of the application's package, retrieves the information about it and calls getApplicationIcon() to return its icon. If the application cannot be found, NameNotFoundException is thrown.

| Parameters | |
|---|---|
| `package` | `String`: Name of the package whose application icon is to be
                    retrieved.This value cannot be `null`. | 

| Returns | |
|---|---|
|  | Returns the image of the icon, or the default application icon if it could not be found. Does not return null. | 

| Throws | |
|---|---|
|  | Thrown if the resources for the given application could not be loaded. | 

**See also:**

### getApplicationInfo  

    [API level 33](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public[ApplicationInfo](https://developer.android.com/reference/android/content/pm/ApplicationInfo)getApplicationInfo ([String](https://developer.android.com/reference/java/lang/String)packageName,[PackageManager.ApplicationInfoFlags](https://developer.android.com/reference/android/content/pm/PackageManager.ApplicationInfoFlags)flags)

See [getApplicationInfo(String,int)](https://developer.android.com/reference/android/content/pm/PackageManager#getApplicationInfo(java.lang.String,%20int))

| Parameters | |
|---|---|
| `package` | `String`: This value cannot be`null`. | 
| `flags` | `Package`: This value cannot be`null`. | 

| Returns | |
|---|---|
|  | This value cannot be `null`. | 

### getApplicationInfo  

    [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public abstract[ApplicationInfo](https://developer.android.com/reference/android/content/pm/ApplicationInfo)getApplicationInfo ([String](https://developer.android.com/reference/java/lang/String)packageName, int flags)

Retrieve all of the information we know about a particular
 package/application.
 Use [getApplicationInfo(String,ApplicationInfoFlags)](https://developer.android.com/reference/android/content/pm/PackageManager#getApplicationInfo(java.lang.String,%20android.content.pm.PackageManager.ApplicationInfoFlags))

| Parameters | |
|---|---|
| `package` | `String`: The full name (i.e. com.google.apps.contacts) of an
            application.This value cannot be `null`. | 
| `flags` | `int`: Additional option flags to modify the data returned. | 

| Returns | |
|---|---|
|  | An containing information about the
         package. If flag`MATCH_`is set and if
         the package is not found in the list of installed applications,
         the application information is retrieved from the list of
         uninstalled applications (which includes installed applications
         as well as applications with data directory i.e. applications
         which had been deleted with`DELETE_`flag set).This value cannot be `null`. | 

| Throws | |
|---|---|
|  | if a package with the given name cannot be found on the system. | 

### getApplicationLabel  

    [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public abstract[CharSequence](https://developer.android.com/reference/java/lang/CharSequence)getApplicationLabel ([ApplicationInfo](https://developer.android.com/reference/android/content/pm/ApplicationInfo)info)

Return the label to use for this application.

| Parameters | |
|---|---|
| `info` | `Application`: Theof the application to get the label of.This value cannot be `null`. | 

| Returns | |
|---|---|
|  | Returns a containing the label associated with
 this application, or its name the  item does not have a label.This value cannot be `null`. | 

### getApplicationLogo  

    [API level 9](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public abstract[Drawable](https://developer.android.com/reference/android/graphics/drawable/Drawable)getApplicationLogo ([String](https://developer.android.com/reference/java/lang/String)packageName)

Retrieve the logo associated with an application. Given the name of the application's package, retrieves the information about it and calls getApplicationLogo() to return its logo. If the application cannot be found, NameNotFoundException is thrown.

| Parameters | |
|---|---|
| `package` | `String`: Name of the package whose application logo is to be
                    retrieved.This value cannot be `null`. | 

| Returns | |
|---|---|
|  | Returns the image of the logo, or null if no application logo has been specified. | 

| Throws | |
|---|---|
|  | Thrown if the resources for the given application could not be loaded. | 

**See also:**

### getApplicationLogo  

    [API level 9](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public abstract[Drawable](https://developer.android.com/reference/android/graphics/drawable/Drawable)getApplicationLogo ([ApplicationInfo](https://developer.android.com/reference/android/content/pm/ApplicationInfo)info)

Retrieve the logo associated with an application. If it has not specified a logo, this method returns null.

| Parameters | |
|---|---|
| `info` | `Application`: Information about application being queried.This value cannot be `null`. | 

| Returns | |
|---|---|
|  | Returns the image of the logo, or null if no logo is specified by the application. | 

**See also:**

### getArchivedPackage  

    [API level 35](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public[ArchivedPackageInfo](https://developer.android.com/reference/android/content/pm/ArchivedPackageInfo)getArchivedPackage ([String](https://developer.android.com/reference/java/lang/String)packageName)

Return archived package info for the package or null if the package is not installed.

| Parameters | |
|---|---|
| `package` | `String`: This value cannot be`null`. | 

| Returns | |
|---|---|
|  | |

**See also:**

### getBackgroundPermissionOptionLabel    

    [API level 30](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public[CharSequence](https://developer.android.com/reference/java/lang/CharSequence)getBackgroundPermissionOptionLabel ()

Gets the localized label that corresponds to the option in settings for granting background access.

The intended use is for apps to reference this label in its instruction for users to grant a background permission.

| Returns | |
|---|---|
|  | the localized label that corresponds to the settings option for granting
 background access. This value cannot be `null`. | 

### getChangedPackages  

    [API level 26](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public abstract[ChangedPackages](https://developer.android.com/reference/android/content/pm/ChangedPackages)getChangedPackages (int sequenceNumber)

Returns the names of the packages that have been changed [eg. added, removed or updated] since the given sequence number.

If no packages have been changed, returns `null`.
 

The sequence number starts at `0` and is
 reset every boot.

| Parameters | |
|---|---|
| `sequence` | `int`: The first sequence number for which to retrieve package changes.Value is 0 or greater | 

| Returns | |
|---|---|
|  | |

**See also:**

### getComponentEnabledSetting   

    [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public abstract int getComponentEnabledSetting ([ComponentName](https://developer.android.com/reference/android/content/ComponentName)componentName)

Return the enabled setting for a package component (activity,
 receiver, service, provider).  This returns the last value set by
 [setComponentEnabledSetting(ComponentName,int,int)](https://developer.android.com/reference/android/content/pm/PackageManager#setComponentEnabledSetting(android.content.ComponentName,%20int,%20int))[COMPONENT_ENABLED_STATE_DEFAULT](https://developer.android.com/reference/android/content/pm/PackageManager#COMPONENT_ENABLED_STATE_DEFAULT)

| Parameters | |
|---|---|
| `component` | `Component`: The component to retrieve.This value cannot be `null`. | 

| Returns | |
|---|---|
| `int` | Returns the current enabled state for the component. Value is one of the following: | 

### getDefaultActivityIcon   

    [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public abstract[Drawable](https://developer.android.com/reference/android/graphics/drawable/Drawable)getDefaultActivityIcon ()

Return the generic icon for an activity that is used when no specific icon is defined.

| Returns | |
|---|---|
|  | Drawable Image of the icon. This value cannot be `null`. | 

### getDrawable 

    [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public abstract[Drawable](https://developer.android.com/reference/android/graphics/drawable/Drawable)getDrawable ([String](https://developer.android.com/reference/java/lang/String)packageName, int resid,[ApplicationInfo](https://developer.android.com/reference/android/content/pm/ApplicationInfo)appInfo)

Retrieve an image from a package.  This is a low-level API used by
 the various package manager info structures (such as
 [ComponentInfo](https://developer.android.com/reference/android/content/pm/ComponentInfo)

| Parameters | |
|---|---|
| `package` | `String`: The name of the package that this icon is coming from.
 Cannot be null. | 
| `resid` | `int`: The resource identifier of the desired image.  Cannot be 0. | 
| `app` | `Application`: Overall information aboutpackageName.  This
 may be null, in which case the application information will be retrieved
 for you if needed; if you already have this information around, it can
 be much more efficient to supply it here. | 

| Returns | |
|---|---|
|  | Returns a Drawable holding the requested image. Returns null if an image could not be found for any reason. | 

### getGroupOfPlatformPermission    

    [API level 31](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public void getGroupOfPlatformPermission ([String](https://developer.android.com/reference/java/lang/String)permissionName,[Executor](https://developer.android.com/reference/java/util/concurrent/Executor)executor,[Consumer](https://developer.android.com/reference/java/util/function/Consumer)<[String](https://developer.android.com/reference/java/lang/String)> callback)

Get the platform-defined permission group of a particular permission, if the permission is a platform-defined permission.

| Parameters | |
|---|---|
| `permission` | `String`: the permission whose group is desired.This value cannot be `null`. | 
| `executor` | `Executor`: theon which to invoke the callback.This value cannot be `null`.Callback and listener events are dispatched through this , providing an easy way to control which thread is
           used. To dispatch events through the main thread of your
           application, you can use.
           Otherwise, provide anthat dispatches to an appropriate thread. | 
| `callback` | `Consumer`: the callback which will receive the name of the permission group this
                 permission belongs to, or`null`if it has no group, is not a
                 platform-defined permission, or there was an exception | 

### getInstallSourceInfo   

    [API level 30](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public[InstallSourceInfo](https://developer.android.com/reference/android/content/pm/InstallSourceInfo)getInstallSourceInfo ([String](https://developer.android.com/reference/java/lang/String)packageName)

Retrieves information about how a package was installed or updated.

 If the calling application does not hold the INSTALL_PACKAGES permission then
 the result will always return `null` from
 [InstallSourceInfo.getOriginatingPackageName()](https://developer.android.com/reference/android/content/pm/InstallSourceInfo#getOriginatingPackageName())

 If the package that requested the install has been uninstalled, then information about it
 will only be returned from [InstallSourceInfo.getInitiatingPackageName()](https://developer.android.com/reference/android/content/pm/InstallSourceInfo#getInitiatingPackageName())[InstallSourceInfo.getInitiatingPackageSigningInfo()](https://developer.android.com/reference/android/content/pm/InstallSourceInfo#getInitiatingPackageSigningInfo())

| Parameters | |
|---|---|
| `package` | `String`: The name of the package to query.This value cannot be `null`. | 

| Returns | |
|---|---|
|  | |

| Throws | |
|---|---|
|  | if the given package name is not available to the caller. | 

### getInstalledApplications  

    [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public abstract[List](https://developer.android.com/reference/java/util/List)<[ApplicationInfo](https://developer.android.com/reference/android/content/pm/ApplicationInfo)> getInstalledApplications (int flags)

Return a List of all application packages that are installed for the
 current user. If flag GET_UNINSTALLED_PACKAGES has been set, a list of all
 applications including those deleted with `DELETE_KEEP_DATA`
 (partially installed apps with data directory) will be returned.
 Use [getInstalledApplications(ApplicationInfoFlags)](https://developer.android.com/reference/android/content/pm/PackageManager#getInstalledApplications(android.content.pm.PackageManager.ApplicationInfoFlags))

| Parameters | |
|---|---|
| `flags` | `int`: Additional option flags to modify the data returned. | 

| Returns | |
|---|---|
|  | A List of ApplicationInfo objects, one for each installed
         application. In the unlikely case there are no installed
         packages, an empty list is returned. If flag `MATCH_`is set, the application
         information is retrieved from the list of uninstalled
         applications (which includes installed applications as well as
         applications with data directory i.e. applications which had been
         deleted with`DELETE_`flag set).This value cannot be `null`. | 

### getInstalledApplications  

    [API level 33](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public[List](https://developer.android.com/reference/java/util/List)<[ApplicationInfo](https://developer.android.com/reference/android/content/pm/ApplicationInfo)> getInstalledApplications ([PackageManager.ApplicationInfoFlags](https://developer.android.com/reference/android/content/pm/PackageManager.ApplicationInfoFlags)flags)

See [getInstalledApplications(int)](https://developer.android.com/reference/android/content/pm/PackageManager#getInstalledApplications(int))

| Parameters | |
|---|---|
| `flags` | `Package`: This value cannot be`null`. | 

| Returns | |
|---|---|
|  | This value cannot be `null`. | 

### getInstalledModules  

    [API level 29](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public[List](https://developer.android.com/reference/java/util/List)<[ModuleInfo](https://developer.android.com/reference/android/content/pm/ModuleInfo)> getInstalledModules (int flags)

Return a List of all modules that are installed.

| Parameters | |
|---|---|
| `flags` | `int`: Additional option flags to modify the data returned.Value is either `0`or | 

| Returns | |
|---|---|
|  | A ofobjects, one for each installed
         module, containing information about the module. In the unlikely case
         there are no installed modules, an empty list is returned.This value cannot be `null`. | 

### getInstalledPackages  

    [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public abstract[List](https://developer.android.com/reference/java/util/List)<[PackageInfo](https://developer.android.com/reference/android/content/pm/PackageInfo)> getInstalledPackages (int flags)

Return a List of all packages that are installed for the current user.
 Use [getInstalledPackages(PackageInfoFlags)](https://developer.android.com/reference/android/content/pm/PackageManager#getInstalledPackages(android.content.pm.PackageManager.PackageInfoFlags))

| Parameters | |
|---|---|
| `flags` | `int`: Additional option flags to modify the data returned. | 

| Returns | |
|---|---|
|  | A List of PackageInfo objects, one for each installed package,
         containing information about the package. In the unlikely case
         there are no installed packages, an empty list is returned. If
         flag `MATCH_`is set, the package
         information is retrieved from the list of uninstalled
         applications (which includes installed applications as well as
         applications with data directory i.e. applications which had been
         deleted with`DELETE_`flag set).This value cannot be `null`. | 

### getInstalledPackages  

    [API level 33](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public[List](https://developer.android.com/reference/java/util/List)<[PackageInfo](https://developer.android.com/reference/android/content/pm/PackageInfo)> getInstalledPackages ([PackageManager.PackageInfoFlags](https://developer.android.com/reference/android/content/pm/PackageManager.PackageInfoFlags)flags)

See [getInstalledPackages(int)](https://developer.android.com/reference/android/content/pm/PackageManager#getInstalledPackages(int))

| Parameters | |
|---|---|
| `flags` | `Package`: This value cannot be`null`. | 

| Returns | |
|---|---|
|  | This value cannot be `null`. | 

### getInstallerPackageName   

    public abstract[String](https://developer.android.com/reference/java/lang/String)getInstallerPackageName ([String](https://developer.android.com/reference/java/lang/String)packageName)


**
      This method was deprecated
      in API level 30.**

    use [getInstallSourceInfo(String)](https://developer.android.com/reference/android/content/pm/PackageManager#getInstallSourceInfo(java.lang.String))

Retrieve the package name of the application that installed a package. This identifies which market the package came from.

| Parameters | |
|---|---|
| `package` | `String`: The name of the package to query.This value cannot be `null`. | 

| Returns | |
|---|---|
|  | This value may be `null`. | 

| Throws | |
|---|---|
|  | if the given package name is not installed | 

### getInstantAppCookie   

    [API level 26](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public abstract byte[] getInstantAppCookie ()

Gets the instant application cookie for this app. Non instant apps and apps that were instant but were upgraded to normal apps can still access this API. For instant apps this cookie is cached for some time after uninstall while for normal apps the cookie is deleted after the app is uninstalled. The cookie is always present while the app is installed.

| Returns | |
|---|---|
| `byte[]` | The cookie. This value cannot be `null`. | 

### getInstantAppCookieMaxBytes     

    [API level 26](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public abstract int getInstantAppCookieMaxBytes ()

Gets the maximum size in bytes of the cookie data an instant app can store on the device.

| Returns | |
|---|---|
| `int` | The max cookie size in bytes. | 

### getInstrumentationInfo  

    [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public abstract[InstrumentationInfo](https://developer.android.com/reference/android/content/pm/InstrumentationInfo)getInstrumentationInfo ([ComponentName](https://developer.android.com/reference/android/content/ComponentName)className, int flags)

Retrieve all of the information we know about a particular instrumentation class.

| Parameters | |
|---|---|
| `class` | `Component`: The full name (i.e.
            com.google.apps.contacts.InstrumentList) of an Instrumentation
            class.This value cannot be `null`. | 
| `flags` | `int`: Additional option flags to modify the data returned.Value is either `0`or | 

| Returns | |
|---|---|
|  | An object containing information
         about the instrumentation.This value cannot be `null`. | 

| Throws | |
|---|---|
|  | if a package with the given name cannot be found on the system. | 

### getLaunchIntentForPackage    

    [API level 3](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public abstract[Intent](https://developer.android.com/reference/android/content/Intent)getLaunchIntentForPackage ([String](https://developer.android.com/reference/java/lang/String)packageName)

Returns a "good" intent to launch a front-door activity in a package.
 This is used, for example, to implement an "open" button when browsing
 through packages.  The current implementation looks first for a main
 activity in the category [Intent.CATEGORY_INFO](https://developer.android.com/reference/android/content/Intent#CATEGORY_INFO)[Intent.CATEGORY_LAUNCHER](https://developer.android.com/reference/android/content/Intent#CATEGORY_LAUNCHER)`null` if neither are found.
 

Consider using [getLaunchIntentSenderForPackage(String)](https://developer.android.com/reference/android/content/pm/PackageManager#getLaunchIntentSenderForPackage(java.lang.String))`packageName`.

| Parameters | |
|---|---|
| `package` | `String`: The name of the package to inspect.This value cannot be `null`. | 

| Returns | |
|---|---|
|  | A fully-qualified that can be used to launch the
 main activity in the package. Returns`null`if the package
 does not contain such an activity, or ifpackageNameis not
 recognized. | 

**See also:**

### getLaunchIntentSenderForPackage     

    [API level 33](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public[IntentSender](https://developer.android.com/reference/android/content/IntentSender)getLaunchIntentSenderForPackage ([String](https://developer.android.com/reference/java/lang/String)packageName)

Returns an [IntentSender](https://developer.android.com/reference/android/content/IntentSender)[getLaunchIntentForPackage(String)](https://developer.android.com/reference/android/content/pm/PackageManager#getLaunchIntentForPackage(java.lang.String))[Intent](https://developer.android.com/reference/android/content/Intent)[IntentSender](https://developer.android.com/reference/android/content/IntentSender)

The caller can invoke
 [IntentSender.sendIntent(Context,int,Intent,IntentSender.OnFinished,Handler)](https://developer.android.com/reference/android/content/IntentSender#sendIntent(android.content.Context,%20int,%20android.content.Intent,%20android.content.IntentSender.OnFinished,%20android.os.Handler))[IntentSender.SendIntentException](https://developer.android.com/reference/android/content/IntentSender.SendIntentException)*packageName* is not recognized.

| Parameters | |
|---|---|
| `package` | `String`: The name of the package to inspect.This value cannot be `null`. | 

| Returns | |
|---|---|
|  | Returns a to launch the activity.This value cannot be `null`. | 

**See also:**

### getLeanbackLaunchIntentForPackage     

    [API level 21](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public abstract[Intent](https://developer.android.com/reference/android/content/Intent)getLeanbackLaunchIntentForPackage ([String](https://developer.android.com/reference/java/lang/String)packageName)

Return a "good" intent to launch a front-door Leanback activity in a
 package, for use for example to implement an "open" button when browsing
 through packages. The current implementation will look for a main
 activity in the category [Intent.CATEGORY_LEANBACK_LAUNCHER](https://developer.android.com/reference/android/content/Intent#CATEGORY_LEANBACK_LAUNCHER)

| Parameters | |
|---|---|
| `package` | `String`: The name of the package to inspect.This value cannot be `null`. | 

| Returns | |
|---|---|
|  | Returns either a fully-qualified Intent that can be used to launch the main Leanback activity in the package, or null if the package does not contain such an activity. | 

### getMimeGroup  

    [API level 30](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public[Set](https://developer.android.com/reference/java/util/Set)<[String](https://developer.android.com/reference/java/lang/String)> getMimeGroup ([String](https://developer.android.com/reference/java/lang/String)mimeGroup)

Gets all MIME types contained by MIME group. Libraries should use a reverse-DNS prefix followed by a ':' character and library-specific group name to avoid namespace collisions, e.g. "com.example:myFeature".

| Parameters | |
|---|---|
| `mime` | `String`: MIME group to retrieve.This value cannot be `null`. | 

| Throws | |
|---|---|
|  | if the MIME group was not declared in the manifest. | 

### getModuleInfo  

    [API level 29](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public[ModuleInfo](https://developer.android.com/reference/android/content/pm/ModuleInfo)getModuleInfo ([String](https://developer.android.com/reference/java/lang/String)packageName, int flags)

Retrieve information for a particular module.

| Parameters | |
|---|---|
| `package` | `String`: The name of the module.This value cannot be `null`. | 
| `flags` | `int`: Additional option flags to modify the data returned.Value is either `0`or | 

| Returns | |
|---|---|
|  | A object containing information about the
         module.This value cannot be `null`. | 

| Throws | |
|---|---|
|  | if a module with the given name cannot be found on the system. | 

### getNameForUid   

    [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public abstract[String](https://developer.android.com/reference/java/lang/String)getNameForUid (int uid)

Retrieve the official name associated with a uid. This name is guaranteed to never change, though it is possible for the underlying uid to be changed. That is, if you are storing information about uids in persistent storage, you should use the string returned by this function instead of the raw uid.

| Parameters | |
|---|---|
| `uid` | `int`: The uid for which you would like to retrieve a name. | 

| Returns | |
|---|---|
|  | Returns a unique name for the given uid, or null if the uid is not currently assigned. | 

### getPackageArchiveInfo   

    [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public[PackageInfo](https://developer.android.com/reference/android/content/pm/PackageInfo)getPackageArchiveInfo ([String](https://developer.android.com/reference/java/lang/String)archiveFilePath, int flags)

Retrieve overall information about an application package defined in a
 package archive file
 Use [getPackageArchiveInfo(String,PackageInfoFlags)](https://developer.android.com/reference/android/content/pm/PackageManager#getPackageArchiveInfo(java.lang.String,%20android.content.pm.PackageManager.PackageInfoFlags))

| Parameters | |
|---|---|
| `archive` | `String`: The path to the archive file.This value cannot be `null`. | 
| `flags` | `int`: Additional option flags to modify the data returned. | 

| Returns | |
|---|---|
|  | A PackageInfo object containing information about the package archive. If the package could not be parsed, returns null. | 

### getPackageArchiveInfo   

    [API level 33](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public[PackageInfo](https://developer.android.com/reference/android/content/pm/PackageInfo)getPackageArchiveInfo ([String](https://developer.android.com/reference/java/lang/String)archiveFilePath,[PackageManager.PackageInfoFlags](https://developer.android.com/reference/android/content/pm/PackageManager.PackageInfoFlags)flags)

See [getPackageArchiveInfo(String,int)](https://developer.android.com/reference/android/content/pm/PackageManager#getPackageArchiveInfo(java.lang.String,%20int))

| Parameters | |
|---|---|
| `archive` | `String`: This value cannot be`null`. | 
| `flags` | `Package`: This value cannot be`null`. | 

| Returns | |
|---|---|
|  | This value may be `null`. | 

### getPackageGids  

    [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public abstract int[] getPackageGids ([String](https://developer.android.com/reference/java/lang/String)packageName)

Return an array of all of the POSIX secondary group IDs that have been assigned to the given package.

 Note that the same package may have different GIDs under different
 [UserHandle](https://developer.android.com/reference/android/os/UserHandle)

| Parameters | |
|---|---|
| `package` | `String`: The full name (i.e. com.google.apps.contacts) of the
            desired package.This value cannot be `null`. | 

| Returns | |
|---|---|
| `int[]` | Returns an int array of the assigned GIDs, or null if there are none. | 

| Throws | |
|---|---|
|  | if no such package is available to the caller. | 

### getPackageGids  

    [API level 24](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public abstract int[] getPackageGids ([String](https://developer.android.com/reference/java/lang/String)packageName, int flags)

Return an array of all of the POSIX secondary group IDs that have been assigned to the given package.

 Note that the same package may have different GIDs under different
 [UserHandle](https://developer.android.com/reference/android/os/UserHandle)[getPackageGids(String,PackageInfoFlags)](https://developer.android.com/reference/android/content/pm/PackageManager#getPackageGids(java.lang.String,%20android.content.pm.PackageManager.PackageInfoFlags))

| Parameters | |
|---|---|
| `package` | `String`: The full name (i.e. com.google.apps.contacts) of the
            desired package.This value cannot be `null`. | 
| `flags` | `int` | 

| Returns | |
|---|---|
| `int[]` | Returns an int array of the assigned gids, or null if there are none. | 

| Throws | |
|---|---|
|  | if no such package is available to the caller. | 

### getPackageGids  

    [API level 33](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public int[] getPackageGids ([String](https://developer.android.com/reference/java/lang/String)packageName,[PackageManager.PackageInfoFlags](https://developer.android.com/reference/android/content/pm/PackageManager.PackageInfoFlags)flags)

See [getPackageGids(String,int)](https://developer.android.com/reference/android/content/pm/PackageManager#getPackageGids(java.lang.String,%20int))

| Parameters | |
|---|---|
| `package` | `String`: This value cannot be`null`. | 
| `flags` | `Package`: This value cannot be`null`. | 

| Returns | |
|---|---|
| `int[]` | This value may be `null`. | 

### getPackageInfo  

    [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public abstract[PackageInfo](https://developer.android.com/reference/android/content/pm/PackageInfo)getPackageInfo ([String](https://developer.android.com/reference/java/lang/String)packageName, int flags)

Retrieve overall information about an application package that is
 installed on the system.
 Use [getPackageInfo(String,PackageInfoFlags)](https://developer.android.com/reference/android/content/pm/PackageManager#getPackageInfo(java.lang.String,%20android.content.pm.PackageManager.PackageInfoFlags))

| Parameters | |
|---|---|
| `package` | `String`: The full name (i.e. com.google.apps.contacts) of the
            desired package.This value cannot be `null`. | 
| `flags` | `int`: Additional option flags to modify the data returned. | 

| Returns | |
|---|---|
|  | A PackageInfo object containing information about the package. If
         flag `MATCH_`is set and if the package
         is not found in the list of installed applications, the package
         information is retrieved from the list of uninstalled
         applications (which includes installed applications as well as
         applications with data directory i.e. applications which had been
         deleted with`DELETE_`flag set). | 

| Throws | |
|---|---|
|  | if no such package is available to the caller. | 

### getPackageInfo  

    [API level 33](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public[PackageInfo](https://developer.android.com/reference/android/content/pm/PackageInfo)getPackageInfo ([String](https://developer.android.com/reference/java/lang/String)packageName,[PackageManager.PackageInfoFlags](https://developer.android.com/reference/android/content/pm/PackageManager.PackageInfoFlags)flags)

See [getPackageInfo(String,int)](https://developer.android.com/reference/android/content/pm/PackageManager#getPackageInfo(java.lang.String,%20int))

| Parameters | |
|---|---|
| `package` | `String`: This value cannot be`null`. | 
| `flags` | `Package`: This value cannot be`null`. | 

| Returns | |
|---|---|
|  | This value cannot be `null`. | 

### getPackageInfo  

    [API level 33](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public[PackageInfo](https://developer.android.com/reference/android/content/pm/PackageInfo)getPackageInfo ([VersionedPackage](https://developer.android.com/reference/android/content/pm/VersionedPackage)versionedPackage,[PackageManager.PackageInfoFlags](https://developer.android.com/reference/android/content/pm/PackageManager.PackageInfoFlags)flags)

See [getPackageInfo(VersionedPackage,int)](https://developer.android.com/reference/android/content/pm/PackageManager#getPackageInfo(android.content.pm.VersionedPackage,%20int))

| Parameters | |
|---|---|
| `versioned` | `Versioned`: This value cannot be`null`. | 
| `flags` | `Package`: This value cannot be`null`. | 

| Returns | |
|---|---|
|  | This value cannot be `null`. | 

### getPackageInfo  

    [API level 26](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public abstract[PackageInfo](https://developer.android.com/reference/android/content/pm/PackageInfo)getPackageInfo ([VersionedPackage](https://developer.android.com/reference/android/content/pm/VersionedPackage)versionedPackage, int flags)

Retrieve overall information about an application package that is
 installed on the system. This method can be used for retrieving
 information about packages for which multiple versions can be installed
 at the time. Currently only packages hosting static shared libraries can
 have multiple installed versions. The method can also be used to get info
 for a package that has a single version installed by passing
 [VERSION_CODE_HIGHEST](https://developer.android.com/reference/android/content/pm/PackageManager#VERSION_CODE_HIGHEST)[VersionedPackage](https://developer.android.com/reference/android/content/pm/VersionedPackage)[getPackageInfo(VersionedPackage,PackageInfoFlags)](https://developer.android.com/reference/android/content/pm/PackageManager#getPackageInfo(android.content.pm.VersionedPackage,%20android.content.pm.PackageManager.PackageInfoFlags))

| Parameters | |
|---|---|
| `versioned` | `Versioned`: The versioned package for which to query.This value cannot be `null`. | 
| `flags` | `int`: Additional option flags to modify the data returned. | 

| Returns | |
|---|---|
|  | A PackageInfo object containing information about the package. If
         flag `MATCH_`is set and if the package
         is not found in the list of installed applications, the package
         information is retrieved from the list of uninstalled
         applications (which includes installed applications as well as
         applications with data directory i.e. applications which had been
         deleted with`DELETE_`flag set). | 

| Throws | |
|---|---|
|  | if no such package is available to the caller. | 

### getPackageInstaller  

    [API level 21](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public abstract[PackageInstaller](https://developer.android.com/reference/android/content/pm/PackageInstaller)getPackageInstaller ()

Return interface that offers the ability to install, upgrade, and remove applications on the device.

| Returns | |
|---|---|
|  | This value cannot be `null`. | 

### getPackageUid  

    [API level 33](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public int getPackageUid ([String](https://developer.android.com/reference/java/lang/String)packageName,[PackageManager.PackageInfoFlags](https://developer.android.com/reference/android/content/pm/PackageManager.PackageInfoFlags)flags)

See [getPackageUid(String,int)](https://developer.android.com/reference/android/content/pm/PackageManager#getPackageUid(java.lang.String,%20int))

| Parameters | |
|---|---|
| `package` | `String`: This value cannot be`null`. | 
| `flags` | `Package`: This value cannot be`null`. | 

| Returns | |
|---|---|
| `int` | |

### getPackageUid  

    [API level 24](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public abstract int getPackageUid ([String](https://developer.android.com/reference/java/lang/String)packageName, int flags)

Return the UID associated with the given package name.

 Note that the same package will have different UIDs under different
 [UserHandle](https://developer.android.com/reference/android/os/UserHandle)[getPackageUid(String,PackageInfoFlags)](https://developer.android.com/reference/android/content/pm/PackageManager#getPackageUid(java.lang.String,%20android.content.pm.PackageManager.PackageInfoFlags))

| Parameters | |
|---|---|
| `package` | `String`: The full name (i.e. com.google.apps.contacts) of the
            desired package.This value cannot be `null`. | 
| `flags` | `int` | 

| Returns | |
|---|---|
| `int` | Returns an integer UID who owns the given package name. | 

| Throws | |
|---|---|
|  | if no such package is available to the caller. | 

### getPackagesForUid   

    [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public abstract[String[]](https://developer.android.com/reference/java/lang/String)getPackagesForUid (int uid)

Retrieve the names of all packages that are associated with a particular user id. In most cases, this will be a single package name, the package that has been assigned that user id. Where there are multiple packages sharing the same user id through the "sharedUserId" mechanism, all packages with that id will be returned.

| Parameters | |
|---|---|
| `uid` | `int`: The user id for which you would like to retrieve the
 associated packages. | 

| Returns | |
|---|---|
|  | Returns an array of one or more packages assigned to the user id, or null if there are no known packages with the given id. | 

### getPackagesHoldingPermissions   

    [API level 18](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public abstract[List](https://developer.android.com/reference/java/util/List)<[PackageInfo](https://developer.android.com/reference/android/content/pm/PackageInfo)> getPackagesHoldingPermissions ([String[]](https://developer.android.com/reference/java/lang/String)permissions, int flags)

Return a List of all installed packages that are currently holding any of
 the given permissions.
 Use [getPackagesHoldingPermissions(String[],PackageInfoFlags)](https://developer.android.com/reference/android/content/pm/PackageManager#getPackagesHoldingPermissions(java.lang.String[],%20android.content.pm.PackageManager.PackageInfoFlags))

| Parameters | |
|---|---|
| `permissions` | `String`: This value cannot be`null`. | 
| `flags` | `int`: Additional option flags to modify the data returned. | 

| Returns | |
|---|---|
|  | A List of PackageInfo objects, one for each installed package
         that holds any of the permissions that were provided, containing
         information about the package. If no installed packages hold any
         of the permissions, an empty list is returned. If flag `MATCH_`is set, the package
         information is retrieved from the list of uninstalled
         applications (which includes installed applications as well as
         applications with data directory i.e. applications which had been
         deleted with`DELETE_`flag set).This value cannot be `null`. | 

### getPackagesHoldingPermissions   

    [API level 33](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public[List](https://developer.android.com/reference/java/util/List)<[PackageInfo](https://developer.android.com/reference/android/content/pm/PackageInfo)> getPackagesHoldingPermissions ([String[]](https://developer.android.com/reference/java/lang/String)permissions,[PackageManager.PackageInfoFlags](https://developer.android.com/reference/android/content/pm/PackageManager.PackageInfoFlags)flags)

See [getPackagesHoldingPermissions(String[],int)](https://developer.android.com/reference/android/content/pm/PackageManager#getPackagesHoldingPermissions(java.lang.String[],%20int))

| Parameters | |
|---|---|
| `permissions` | `String`: This value cannot be`null`. | 
| `flags` | `Package`: This value cannot be`null`. | 

| Returns | |
|---|---|
|  | This value cannot be `null`. | 

### getPermissionGroupInfo   

    [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public abstract[PermissionGroupInfo](https://developer.android.com/reference/android/content/pm/PermissionGroupInfo)getPermissionGroupInfo ([String](https://developer.android.com/reference/java/lang/String)groupName, int flags)

Retrieve all of the information we know about a particular group of permissions.

| Parameters | |
|---|---|
| `group` | `String`: The fully qualified name (i.e.
            com.google.permission_group.APPS) of the permission you are
            interested in.This value cannot be `null`. | 
| `flags` | `int`: Additional option flags to modify the data returned.Value is either `0`or | 

| Returns | |
|---|---|
|  | Returns a containing information
         about the permission.This value cannot be `null`. | 

| Throws | |
|---|---|
|  | if a package with the given name cannot be found on the system. | 

### getPermissionInfo  

    [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public abstract[PermissionInfo](https://developer.android.com/reference/android/content/pm/PermissionInfo)getPermissionInfo ([String](https://developer.android.com/reference/java/lang/String)permName, int flags)

Retrieve all of the information we know about a particular permission.

| Parameters | |
|---|---|
| `perm` | `String`: The fully qualified name (i.e. com.google.permission.LOGIN)
            of the permission you are interested in.This value cannot be `null`. | 
| `flags` | `int`: Additional option flags to modify the data returned.Value is either `0`or | 

| Returns | |
|---|---|
|  | Returns a containing information about the
         permission. | 

| Throws | |
|---|---|
|  | if a package with the given name cannot be found on the system. | 

### getPlatformPermissionsForGroup    

    [API level 31](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public void getPlatformPermissionsForGroup ([String](https://developer.android.com/reference/java/lang/String)permissionGroupName,[Executor](https://developer.android.com/reference/java/util/concurrent/Executor)executor,[Consumer](https://developer.android.com/reference/java/util/function/Consumer)<[List](https://developer.android.com/reference/java/util/List)<[String](https://developer.android.com/reference/java/lang/String)>> callback)

Get the platform-defined permissions which belong to a particular permission group.

| Parameters | |
|---|---|
| `permission` | `String`: the permission group whose permissions are desired.This value cannot be `null`. | 
| `executor` | `Executor`: theon which to invoke the callback.This value cannot be `null`.Callback and listener events are dispatched through this , providing an easy way to control which thread is
           used. To dispatch events through the main thread of your
           application, you can use.
           Otherwise, provide anthat dispatches to an appropriate thread. | 
| `callback` | `Consumer`: the callback which will receive a list of the platform-defined permissions in
                 the group, or empty if the group is not a valid platform-defined permission
                 group, or there was an exception.This value cannot be `null`. | 

### getPreferredActivities  

    public abstract int getPreferredActivities ([List](https://developer.android.com/reference/java/util/List)<[IntentFilter](https://developer.android.com/reference/android/content/IntentFilter)> outFilters,[List](https://developer.android.com/reference/java/util/List)<[ComponentName](https://developer.android.com/reference/android/content/ComponentName)> outActivities,[String](https://developer.android.com/reference/java/lang/String)packageName)


**
      This method was deprecated
      in API level 29.**

    This function no longer does anything. It is the platform's
 responsibility to assign preferred activities and this cannot be modified
 directly. To determine the activities resolved by the platform, use
 [resolveActivity(Intent, ResolveInfoFlags)](https://developer.android.com/reference/android/content/pm/PackageManager#resolveActivity(android.content.Intent,%20android.content.pm.PackageManager.ResolveInfoFlags))[queryIntentActivities(Intent, ResolveInfoFlags)](https://developer.android.com/reference/android/content/pm/PackageManager#queryIntentActivities(android.content.Intent,%20android.content.pm.PackageManager.ResolveInfoFlags))[RoleManager](https://developer.android.com/reference/android/app/role/RoleManager)

Retrieve all preferred activities, previously added with
 [addPreferredActivity(IntentFilter, int, ComponentName, ComponentName)](https://developer.android.com/reference/android/content/pm/PackageManager#addPreferredActivity(android.content.IntentFilter,%20int,%20android.content.ComponentName[],%20android.content.ComponentName))

| Parameters | |
|---|---|
| `out` | `List`: A required list in which to place the filters of all of the
 preferred activities.This value cannot be `null`. | 
| `out` | `List`: A required list in which to place the component names of
 all of the preferred activities.This value cannot be `null`. | 
| `package` | `String`: An optional package in which you would like to limit
 the list.  If null, all activities will be returned; if non-null, only
 those activities in the given package are returned. | 

| Returns | |
|---|---|
| `int` | Returns the total number of registered preferred activities (the number of distinct IntentFilter records, not the number of unique activity components) that were found. | 

### getPreferredPackages  

    public abstract[List](https://developer.android.com/reference/java/util/List)<[PackageInfo](https://developer.android.com/reference/android/content/pm/PackageInfo)> getPreferredPackages (int flags)


**
      This method was deprecated
      in API level 29.**

    This function no longer does anything. It is the platform's
 responsibility to assign preferred activities and this cannot be modified
 directly. To determine the activities resolved by the platform, use
 [resolveActivity(Intent, ResolveInfoFlags)](https://developer.android.com/reference/android/content/pm/PackageManager#resolveActivity(android.content.Intent,%20android.content.pm.PackageManager.ResolveInfoFlags))[queryIntentActivities(Intent, ResolveInfoFlags)](https://developer.android.com/reference/android/content/pm/PackageManager#queryIntentActivities(android.content.Intent,%20android.content.pm.PackageManager.ResolveInfoFlags))[RoleManager](https://developer.android.com/reference/android/app/role/RoleManager)

Retrieve the list of all currently configured preferred packages. The first package on the list is the most preferred, the last is the least preferred.

| Parameters | |
|---|---|
| `flags` | `int`: Additional option flags to modify the data returned. | 

| Returns | |
|---|---|
|  | A List of PackageInfo objects, one for each preferred
         application, in order of preference. This value cannot be `null`. | 

### getProperty 

    [API level 31](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public[PackageManager.Property](https://developer.android.com/reference/android/content/pm/PackageManager.Property)getProperty ([String](https://developer.android.com/reference/java/lang/String)propertyName,[String](https://developer.android.com/reference/java/lang/String)packageName)

Returns the property defined in the given package's <application> tag.

| Parameters | |
|---|---|
| `property` | `String`: This value cannot be`null`. | 
| `package` | `String`: This value cannot be`null`. | 

| Returns | |
|---|---|
|  | This value cannot be `null`. | 

| Throws | |
|---|---|
|  | if either the given package is not installed or if the given property is not defined within the <application> tag. | 

### getProperty 

    [API level 31](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public[PackageManager.Property](https://developer.android.com/reference/android/content/pm/PackageManager.Property)getProperty ([String](https://developer.android.com/reference/java/lang/String)propertyName,[ComponentName](https://developer.android.com/reference/android/content/ComponentName)component)

Returns the property defined in the given component declaration.

| Parameters | |
|---|---|
| `property` | `String`: This value cannot be`null`. | 
| `component` | `Component`: This value cannot be`null`. | 

| Returns | |
|---|---|
|  | This value cannot be `null`. | 

| Throws | |
|---|---|
|  | if either the given component does not exist or if the given property is not defined within the component declaration. | 

### getProviderInfo  

    [API level 9](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public abstract[ProviderInfo](https://developer.android.com/reference/android/content/pm/ProviderInfo)getProviderInfo ([ComponentName](https://developer.android.com/reference/android/content/ComponentName)component, int flags)

Retrieve all of the information we know about a particular content
 provider class.
 Use [getProviderInfo(ComponentName,ComponentInfoFlags)](https://developer.android.com/reference/android/content/pm/PackageManager#getProviderInfo(android.content.ComponentName,%20android.content.pm.PackageManager.ComponentInfoFlags))

| Parameters | |
|---|---|
| `component` | `Component`: The full component name (i.e.
            com.google.providers.media/com.google.providers.media.
            MediaProvider) of a ContentProvider class.This value cannot be `null`. | 
| `flags` | `int`: Additional option flags to modify the data returned. | 

| Returns | |
|---|---|
|  | A object containing information about the
         provider.This value cannot be `null`. | 

| Throws | |
|---|---|
|  | if a package with the given name cannot be found on the system. | 

### getProviderInfo  

    [API level 33](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public[ProviderInfo](https://developer.android.com/reference/android/content/pm/ProviderInfo)getProviderInfo ([ComponentName](https://developer.android.com/reference/android/content/ComponentName)component,[PackageManager.ComponentInfoFlags](https://developer.android.com/reference/android/content/pm/PackageManager.ComponentInfoFlags)flags)

See [getProviderInfo(ComponentName,int)](https://developer.android.com/reference/android/content/pm/PackageManager#getProviderInfo(android.content.ComponentName,%20int))

| Parameters | |
|---|---|
| `component` | `Component`: This value cannot be`null`. | 
| `flags` | `Package`: This value cannot be`null`. | 

| Returns | |
|---|---|
|  | This value cannot be `null`. | 

### getReceiverInfo  

    [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public abstract[ActivityInfo](https://developer.android.com/reference/android/content/pm/ActivityInfo)getReceiverInfo ([ComponentName](https://developer.android.com/reference/android/content/ComponentName)component, int flags)

Retrieve all of the information we know about a particular receiver
 class.
 Use [getReceiverInfo(ComponentName,ComponentInfoFlags)](https://developer.android.com/reference/android/content/pm/PackageManager#getReceiverInfo(android.content.ComponentName,%20android.content.pm.PackageManager.ComponentInfoFlags))

| Parameters | |
|---|---|
| `component` | `Component`: The full component name (i.e.
            com.google.apps.calendar/com.google.apps.calendar.
            CalendarAlarm) of a Receiver class.This value cannot be `null`. | 
| `flags` | `int`: Additional option flags to modify the data returned. | 

| Returns | |
|---|---|
|  | An containing information about the
         receiver.This value cannot be `null`. | 

| Throws | |
|---|---|
|  | if a package with the given name cannot be found on the system. | 

### getReceiverInfo  

    [API level 33](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public[ActivityInfo](https://developer.android.com/reference/android/content/pm/ActivityInfo)getReceiverInfo ([ComponentName](https://developer.android.com/reference/android/content/ComponentName)component,[PackageManager.ComponentInfoFlags](https://developer.android.com/reference/android/content/pm/PackageManager.ComponentInfoFlags)flags)

See [getReceiverInfo(ComponentName,int)](https://developer.android.com/reference/android/content/pm/PackageManager#getReceiverInfo(android.content.ComponentName,%20int))

| Parameters | |
|---|---|
| `component` | `Component`: This value cannot be`null`. | 
| `flags` | `Package`: This value cannot be`null`. | 

| Returns | |
|---|---|
|  | This value cannot be `null`. | 

### getResourcesForActivity   

    [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public abstract[Resources](https://developer.android.com/reference/android/content/res/Resources)getResourcesForActivity ([ComponentName](https://developer.android.com/reference/android/content/ComponentName)activityName)

Retrieve the resources associated with an activity. Given the full name of an activity, retrieves the information about it and calls getResources() to return its application's resources. If the activity cannot be found, NameNotFoundException is thrown.

| Parameters | |
|---|---|
| `activity` | `Component`: Name of the activity whose resources are to be
                     retrieved.This value cannot be `null`. | 

| Returns | |
|---|---|
|  | Returns the application's Resources. This value cannot be `null`. | 

| Throws | |
|---|---|
|  | Thrown if the resources for the given application could not be loaded. | 

### getResourcesForApplication   

    [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public abstract[Resources](https://developer.android.com/reference/android/content/res/Resources)getResourcesForApplication ([ApplicationInfo](https://developer.android.com/reference/android/content/pm/ApplicationInfo)app)

Retrieve the resources for an application. Throws NameNotFoundException if the package is no longer installed.

| Parameters | |
|---|---|
| `app` | `Application`: Information about the desired application.This value cannot be `null`. | 

| Returns | |
|---|---|
|  | Returns the application's Resources. This value cannot be `null`. | 

| Throws | |
|---|---|
|  | Thrown if the resources for the given application could not be loaded (most likely because it was uninstalled). | 

### getResourcesForApplication   

    [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public abstract[Resources](https://developer.android.com/reference/android/content/res/Resources)getResourcesForApplication ([String](https://developer.android.com/reference/java/lang/String)packageName)

Retrieve the resources associated with an application. Given the full package name of an application, retrieves the information about it and calls getResources() to return its application's resources. If the appPackageName cannot be found, NameNotFoundException is thrown.

| Parameters | |
|---|---|
| `package` | `String`: Package name of the application whose resources
                       are to be retrieved.This value cannot be `null`. | 

| Returns | |
|---|---|
|  | Returns the application's Resources. This value cannot be `null`. | 

| Throws | |
|---|---|
|  | Thrown if the resources for the given application could not be loaded. | 

### getResourcesForApplication   

    [API level 31](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public[Resources](https://developer.android.com/reference/android/content/res/Resources)getResourcesForApplication ([ApplicationInfo](https://developer.android.com/reference/android/content/pm/ApplicationInfo)app,[Configuration](https://developer.android.com/reference/android/content/res/Configuration)configuration)

Retrieve the resources for an application for the provided configuration.

| Parameters | |
|---|---|
| `app` | `Application`: Information about the desired application.This value cannot be `null`. | 
| `configuration` | `Configuration`: Overridden configuration when loading the Resources.This value may be `null`. | 

| Returns | |
|---|---|
|  | Returns the application's Resources. This value cannot be `null`. | 

| Throws | |
|---|---|
|  | Thrown if the resources for the given application could not be loaded (most likely because it was uninstalled). | 

### getServiceInfo  

    [API level 33](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public[ServiceInfo](https://developer.android.com/reference/android/content/pm/ServiceInfo)getServiceInfo ([ComponentName](https://developer.android.com/reference/android/content/ComponentName)component,[PackageManager.ComponentInfoFlags](https://developer.android.com/reference/android/content/pm/PackageManager.ComponentInfoFlags)flags)

See [getServiceInfo(ComponentName,int)](https://developer.android.com/reference/android/content/pm/PackageManager#getServiceInfo(android.content.ComponentName,%20int))

| Parameters | |
|---|---|
| `component` | `Component`: This value cannot be`null`. | 
| `flags` | `Package`: This value cannot be`null`. | 

| Returns | |
|---|---|
|  | This value cannot be `null`. | 

### getServiceInfo  

    [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public abstract[ServiceInfo](https://developer.android.com/reference/android/content/pm/ServiceInfo)getServiceInfo ([ComponentName](https://developer.android.com/reference/android/content/ComponentName)component, int flags)

Retrieve all of the information we know about a particular service class.
 Use [getServiceInfo(ComponentName,ComponentInfoFlags)](https://developer.android.com/reference/android/content/pm/PackageManager#getServiceInfo(android.content.ComponentName,%20android.content.pm.PackageManager.ComponentInfoFlags))

| Parameters | |
|---|---|
| `component` | `Component`: The full component name (i.e.
            com.google.apps.media/com.google.apps.media.
            BackgroundPlayback) of a Service class.This value cannot be `null`. | 
| `flags` | `int`: Additional option flags to modify the data returned. | 

| Returns | |
|---|---|
|  | A object containing information about the
         service.This value cannot be `null`. | 

| Throws | |
|---|---|
|  | if the component cannot be found on the system. | 

### getSharedLibraries  

    [API level 33](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public[List](https://developer.android.com/reference/java/util/List)<[SharedLibraryInfo](https://developer.android.com/reference/android/content/pm/SharedLibraryInfo)> getSharedLibraries ([PackageManager.PackageInfoFlags](https://developer.android.com/reference/android/content/pm/PackageManager.PackageInfoFlags)flags)

| Parameters | |
|---|---|
| `flags` | `Package`: This value cannot be`null`. | 

| Returns | |
|---|---|
|  | This value cannot be `null`. | 

### getSharedLibraries  

    [API level 26](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public abstract[List](https://developer.android.com/reference/java/util/List)<[SharedLibraryInfo](https://developer.android.com/reference/android/content/pm/SharedLibraryInfo)> getSharedLibraries (int flags)

Get a list of shared libraries on the device.
 Use [getSharedLibraries(PackageInfoFlags)](https://developer.android.com/reference/android/content/pm/PackageManager#getSharedLibraries(android.content.pm.PackageManager.PackageInfoFlags))

| Parameters | |
|---|---|
| `flags` | `int`: To filter the libraries to return. | 

| Returns | |
|---|---|
|  | The shared library list. This value cannot be `null`. | 

**See also:**

### getSuspendedPackageAppExtras    

    [API level 28](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public[Bundle](https://developer.android.com/reference/android/os/Bundle)getSuspendedPackageAppExtras ()

Returns a [Bundle](https://developer.android.com/reference/android/os/Bundle)`android.permission.SUSPEND_APPS` can supply this
 to the system at the time of suspending an app.
 

This is the same [Bundle](https://developer.android.com/reference/android/os/Bundle)[Intent.ACTION_MY_PACKAGE_SUSPENDED](https://developer.android.com/reference/android/content/Intent#ACTION_MY_PACKAGE_SUSPENDED)[Bundle](https://developer.android.com/reference/android/os/Bundle)

Note: These extras are optional, so if no extras were supplied to the system, this method
 will return `null`, even when the calling app has been suspended.

### getSyntheticAppDetailsActivityEnabled     

    [API level 29](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public boolean getSyntheticAppDetailsActivityEnabled ([String](https://developer.android.com/reference/java/lang/String)packageName)

Return whether a synthetic app details activity will be generated if the app has no enabled launcher activity.

| Parameters | |
|---|---|
| `package` | `String`: The package name of the app.This value cannot be `null`. | 

| Returns | |
|---|---|
| `boolean` | Returns the enabled state for the synthetic app details activity. | 

### getSystemAvailableFeatures   

    [API level 5](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public abstract[FeatureInfo[]](https://developer.android.com/reference/android/content/pm/FeatureInfo)getSystemAvailableFeatures ()

Get a list of features that are available on the system.

| Returns | |
|---|---|
|  | An array of FeatureInfo classes describing the features that are available on the system, or null if there are none(!!). | 

### getSystemSharedLibraryNames    

    [API level 3](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public abstract[String[]](https://developer.android.com/reference/java/lang/String)getSystemSharedLibraryNames ()

Get a list of shared libraries that are available on the system.

| Returns | |
|---|---|
|  | An array of shared library names that are available on the system, or null if none are installed. | 

### getTargetSdkVersion   

    [API level 31](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public int getTargetSdkVersion ([String](https://developer.android.com/reference/java/lang/String)packageName)

| Parameters | |
|---|---|
| `package` | `String`: This value cannot be`null`. | 

| Returns | |
|---|---|
| `int` | The target SDK version for the given package name. Value is 0 or greater | 

| Throws | |
|---|---|
|  | if a package with the given name cannot be found on the system. | 

### getText 

    [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public abstract[CharSequence](https://developer.android.com/reference/java/lang/CharSequence)getText ([String](https://developer.android.com/reference/java/lang/String)packageName, int resid,[ApplicationInfo](https://developer.android.com/reference/android/content/pm/ApplicationInfo)appInfo)

Retrieve text from a package.  This is a low-level API used by
 the various package manager info structures (such as
 [ComponentInfo](https://developer.android.com/reference/android/content/pm/ComponentInfo)

| Parameters | |
|---|---|
| `package` | `String`: The name of the package that this text is coming from.
 Cannot be null. | 
| `resid` | `int`: The resource identifier of the desired text.  Cannot be 0. | 
| `app` | `Application`: Overall information aboutpackageName.  This
 may be null, in which case the application information will be retrieved
 for you if needed; if you already have this information around, it can
 be much more efficient to supply it here. | 

| Returns | |
|---|---|
|  | Returns a CharSequence holding the requested text. Returns null if the text could not be found for any reason. | 

### getUserBadgedDrawableForDensity     

    [API level 21](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public abstract[Drawable](https://developer.android.com/reference/android/graphics/drawable/Drawable)getUserBadgedDrawableForDensity ([Drawable](https://developer.android.com/reference/android/graphics/drawable/Drawable)drawable,[UserHandle](https://developer.android.com/reference/android/os/UserHandle)user,[Rect](https://developer.android.com/reference/android/graphics/Rect)badgeLocation, int badgeDensity)

If the target user is a managed profile of the calling user or the caller is itself a managed profile, then this returns a badged copy of the given drawable allowing the user to distinguish it from the original drawable. The caller can specify the location in the bounds of the drawable to be badged where the badge should be applied as well as the density of the badge to be used.

 If the original drawable is a BitmapDrawable and the backing bitmap is
 mutable as per [Bitmap.isMutable()](https://developer.android.com/reference/android/graphics/Bitmap#isMutable())

| Parameters | |
|---|---|
| `drawable` | `Drawable`: The drawable to badge.This value cannot be `null`. | 
| `user` | `User`: The target user.This value cannot be `null`. | 
| `badge` | `Rect`: Where in the bounds of the badged drawable to place
         the badge. If it's`null`, the badge is applied on top of the entire
         drawable being badged. | 
| `badge` | `int`: The optional desired density for the badge as per. If it's not positive,
         the density of the display is used. | 

| Returns | |
|---|---|
|  | A drawable that combines the original drawable and a badge as
         determined by the system. This value cannot be `null`. | 

### getUserBadgedIcon   

    [API level 21](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public abstract[Drawable](https://developer.android.com/reference/android/graphics/drawable/Drawable)getUserBadgedIcon ([Drawable](https://developer.android.com/reference/android/graphics/drawable/Drawable)drawable,[UserHandle](https://developer.android.com/reference/android/os/UserHandle)user)

If the target user is a managed profile, then this returns a badged copy of the given icon
 to be able to distinguish it from the original icon. For badging an arbitrary drawable use
 [getUserBadgedDrawableForDensity(android.graphics.drawable.Drawable,UserHandle,android.graphics.Rect,int)](https://developer.android.com/reference/android/content/pm/PackageManager#getUserBadgedDrawableForDensity(android.graphics.drawable.Drawable,%20android.os.UserHandle,%20android.graphics.Rect,%20int))

 If the original drawable is a BitmapDrawable and the backing bitmap is
 mutable as per [Bitmap.isMutable()](https://developer.android.com/reference/android/graphics/Bitmap#isMutable())

| Parameters | |
|---|---|
| `drawable` | `Drawable`: The drawable to badge.This value cannot be `null`. | 
| `user` | `User`: The target user.This value cannot be `null`. | 

| Returns | |
|---|---|
|  | A drawable that combines the original icon and a badge as
         determined by the system. This value cannot be `null`. | 

### getUserBadgedLabel   

    [API level 21](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public abstract[CharSequence](https://developer.android.com/reference/java/lang/CharSequence)getUserBadgedLabel ([CharSequence](https://developer.android.com/reference/java/lang/CharSequence)label,[UserHandle](https://developer.android.com/reference/android/os/UserHandle)user)

If the target user is a managed profile of the calling user or the caller is itself a managed profile, then this returns a copy of the label with badging for accessibility services like talkback. E.g. passing in "Email" and it might return "Work Email" for Email in the work profile.

| Parameters | |
|---|---|
| `label` | `Char`: The label to change.This value cannot be `null`. | 
| `user` | `User`: The target user.This value cannot be `null`. | 

| Returns | |
|---|---|
|  | A label that combines the original label and a badge as
         determined by the system. This value cannot be `null`. | 

### getVerifiedSigningInfo   

    [API level 36](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public static[SigningInfo](https://developer.android.com/reference/android/content/pm/SigningInfo)getVerifiedSigningInfo ([String](https://developer.android.com/reference/java/lang/String)path, int minAppSigningSchemeVersion)

Verifies and returns the
 [app signing](https://source.android.com/docs/security/features/apksigning)
 information of the file at the given path. This operation takes a few milliseconds.
 Unlike [getPackageArchiveInfo(String,PackageInfoFlags)](https://developer.android.com/reference/android/content/pm/PackageManager#getPackageArchiveInfo(java.lang.String,%20android.content.pm.PackageManager.PackageInfoFlags))[GET_SIGNING_CERTIFICATES](https://developer.android.com/reference/android/content/pm/PackageManager#GET_SIGNING_CERTIFICATES)

| Parameters | |
|---|---|
| `path` | `String`: This value cannot be`null`. | 
| `min` | `int`: Value is one of the following: | 

| Returns | |
|---|---|
|  | This value cannot be `null`. | 

| Throws | |
|---|---|
|  | if the verification fails | 

### getWhitelistedRestrictedPermissions   

    [API level 29](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public[Set](https://developer.android.com/reference/java/util/Set)<[String](https://developer.android.com/reference/java/lang/String)> getWhitelistedRestrictedPermissions ([String](https://developer.android.com/reference/java/lang/String)packageName, int whitelistFlag)

Gets the restricted permissions that have been whitelisted and the app is allowed to have them granted in their full form.

 Permissions can be hard restricted which means that the app cannot hold
 them or soft restricted where the app can hold the permission but in a weaker
 form. Whether a permission is [hard
 restricted](https://developer.android.com/reference/android/content/pm/PermissionInfo#FLAG_HARD_RESTRICTED)[soft restricted](https://developer.android.com/reference/android/content/pm/PermissionInfo#FLAG_SOFT_RESTRICTED)

- There are four allowlists:
 
- one for cases where the system permission policy whitelists a permission
 This list corresponds to the[FLAG_PERMISSION_WHITELIST_SYSTEM](https://developer.android.com/reference/android/content/pm/PackageManager#FLAG_PERMISSION_WHITELIST_SYSTEM)
- one for cases where the system whitelists the permission when upgrading
 from an OS version in which the permission was not restricted to an OS version
 in which the permission is restricted. This list corresponds to the [FLAG_PERMISSION_WHITELIST_UPGRADE](https://developer.android.com/reference/android/content/pm/PackageManager#FLAG_PERMISSION_WHITELIST_UPGRADE)
- one for cases where the installer of the package whitelists a permission.
 This list corresponds to the [FLAG_PERMISSION_WHITELIST_INSTALLER](https://developer.android.com/reference/android/content/pm/PackageManager#FLAG_PERMISSION_WHITELIST_INSTALLER)

 **Note: **In retrospect it would have been preferred to use
 more inclusive terminology when naming this API. Similar APIs added will
 refrain from using the term "whitelist".
 

| Parameters | |
|---|---|
| `package` | `String`: The app for which to get whitelisted permissions.This value cannot be `null`. | 
| `whitelist` | `int`: The flag to determine which whitelist to query. Only one flag
 can be passed.s.Value is either `0`or a combination of the following: | 

| Returns | |
|---|---|
|  | The whitelisted permissions that are on any of the whitelists you query for. This value cannot be `null`. | 

| Throws | |
|---|---|
|  | if you try to access a whitelist that you have no access to. | 

### getXml 

    [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public abstract[XmlResourceParser](https://developer.android.com/reference/android/content/res/XmlResourceParser)getXml ([String](https://developer.android.com/reference/java/lang/String)packageName, int resid,[ApplicationInfo](https://developer.android.com/reference/android/content/pm/ApplicationInfo)appInfo)

Retrieve an XML file from a package. This is a low-level API used to retrieve XML meta data.

| Parameters | |
|---|---|
| `package` | `String`: The name of the package that this xml is coming from.
 Cannot be null. | 
| `resid` | `int`: The resource identifier of the desired xml.  Cannot be 0. | 
| `app` | `Application`: Overall information aboutpackageName.  This
 may be null, in which case the application information will be retrieved
 for you if needed; if you already have this information around, it can
 be much more efficient to supply it here. | 

| Returns | |
|---|---|
|  | Returns an XmlPullParser allowing you to parse out the XML data. Returns null if the xml resource could not be found for any reason. | 

### hasSigningCertificate  

    [API level 28](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

```
public boolean hasSigningCertificate (int uid, 
                byte[] certificate, 
                int type)
```
Searches the set of signing certificates by which the package(s) for the given uid has proven
 to have been signed.  For multiple packages sharing the same uid, this will return the
 signing certificates found in the signing history of the "newest" package, where "newest"
 indicates the package with the newest signing certificate in the shared uid group.  This
 method should be used instead of `getPackageInfo` with `GET_SIGNATURES`
 since it takes into account the possibility of signing certificate rotation, except in the
 case of packages that are signed by multiple certificates, for which signing certificate
 rotation is not supported. This method is analogous to using `getPackagesForUid`
 followed by `getPackageInfo` with `GET_SIGNING_CERTIFICATES`, selecting the
 `PackageInfo` of the newest-signed bpackage , and finally searching through the
 resulting `signingInfo` field to see if the desired certificate is there.

| Parameters | |
|---|---|
| `uid` | `int`: uid whose signing certificates to check | 
| `certificate` | `byte`: signing certificate for which to search.This value cannot be `null`. | 
| `type` | `int`: representation of the`certificate`Value is one of the following: | 

| Returns | |
|---|---|
| `boolean` | true if this package was or is signed by exactly the certificate `certificate` | 

### hasSigningCertificate  

    [API level 28](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public boolean hasSigningCertificate ([String](https://developer.android.com/reference/java/lang/String)packageName, byte[] certificate, int type)

Searches the set of signing certificates by which the given package has proven to have been
 signed.  This should be used instead of `getPackageInfo` with `GET_SIGNATURES`
 since it takes into account the possibility of signing certificate rotation, except in the
 case of packages that are signed by multiple certificates, for which signing certificate
 rotation is not supported.  This method is analogous to using `getPackageInfo` with
 `GET_SIGNING_CERTIFICATES` and then searching through the resulting `signingInfo` field to see if the desired certificate is present.

| Parameters | |
|---|---|
| `package` | `String`: package whose signing certificates to check.This value cannot be `null`. | 
| `certificate` | `byte`: signing certificate for which to search.This value cannot be `null`. | 
| `type` | `int`: representation of the`certificate`Value is one of the following: | 

| Returns | |
|---|---|
| `boolean` | true if this package was or is signed by exactly the certificate `certificate` | 

### hasSystemFeature  

    [API level 5](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public abstract boolean hasSystemFeature ([String](https://developer.android.com/reference/java/lang/String)featureName)

Check whether the given feature name is one of the available features as
 returned by [getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures())*any* version of the given feature name; use
 [hasSystemFeature(String,int)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.lang.String,%20int))

| Parameters | |
|---|---|
| `feature` | `String`: This value cannot be`null`. | 

| Returns | |
|---|---|
| `boolean` | Returns true if the devices supports the feature, else false. | 

### hasSystemFeature  

    [API level 24](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public abstract boolean hasSystemFeature ([String](https://developer.android.com/reference/java/lang/String)featureName, int version)

Check whether the given feature name and version is one of the available
 features as returned by [getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures())

| Parameters | |
|---|---|
| `feature` | `String`: This value cannot be`null`. | 
| `version` | `int` | 

| Returns | |
|---|---|
| `boolean` | Returns true if the devices supports the feature, else false. | 

### isAppArchivable  

    [API level 35](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public boolean isAppArchivable ([String](https://developer.android.com/reference/java/lang/String)packageName)

Returns true if an app is archivable.

| Parameters | |
|---|---|
| `package` | `String`: This value cannot be`null`. | 

| Returns | |
|---|---|
| `boolean` | |

| Throws | |
|---|---|
|  | if the given package name is not available to the caller. | 

**See also:**

### isAutoRevokeWhitelisted   

    [API level 30](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public boolean isAutoRevokeWhitelisted ([String](https://developer.android.com/reference/java/lang/String)packageName)

Checks whether an application is exempt from having its permissions be automatically revoked
 when the app is unused for an extended period of time.
 Only the installer on record that installed the given package, or a holder of
 `WHITELIST_AUTO_REVOKE_PERMISSIONS` is allowed to call this.
 

 **Note: **In retrospect it would have been preferred to use
 more inclusive terminology when naming this API. Similar APIs added will
 refrain from using the term "whitelist".
 

| Parameters | |
|---|---|
| `package` | `String`: The app for which to set exemption.This value cannot be `null`. | 

| Returns | |
|---|---|
| `boolean` | Whether the app is whitelisted. | 

| Throws | |
|---|---|
|  | if you you have no access to this. | 

### isAutoRevokeWhitelisted   

    [API level 30](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public boolean isAutoRevokeWhitelisted ()

 **Note: **In retrospect it would have been preferred to use
 more inclusive terminology when naming this API. Similar APIs added will
 refrain from using the term "whitelist".
 

| Returns | |
|---|---|
| `boolean` | whether this package is whitelisted from having its runtime permission be auto-revoked if unused for an extended period of time. | 

### isDefaultApplicationIcon   

    [API level 30](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public boolean isDefaultApplicationIcon ([Drawable](https://developer.android.com/reference/android/graphics/drawable/Drawable)drawable)

Returns if the provided drawable represents the default activity icon provided by the system. PackageManager silently returns a default application icon for any package/activity if the app itself does not define one or if the system encountered any error when loading the icon. Developers can use this to check implement app specific logic around retrying or caching.

| Parameters | |
|---|---|
| `drawable` | `Drawable`: This value cannot be`null`. | 

| Returns | |
|---|---|
| `boolean` | true if the drawable represents the default activity icon, false otherwise | 

### isDeviceUpgrading  

    [API level 29](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public boolean isDeviceUpgrading ()

Returns true if the device is upgrading, such as first boot after OTA.

| Returns | |
|---|---|
| `boolean` | |

### isInstantApp  

    [API level 26](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public abstract boolean isInstantApp ()

Gets whether this application is an instant app.

| Returns | |
|---|---|
| `boolean` | Whether caller is an instant app. | 

### isInstantApp  

    [API level 26](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public abstract boolean isInstantApp ([String](https://developer.android.com/reference/java/lang/String)packageName)

Gets whether the given package is an instant app.

| Parameters | |
|---|---|
| `package` | `String`: The package to check.This value cannot be `null`. | 

| Returns | |
|---|---|
| `boolean` | Whether the given package is an instant app. | 

### isPackageStopped  

    [API level 35](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public boolean isPackageStopped ([String](https://developer.android.com/reference/java/lang/String)packageName)

Query if an app is currently stopped.

| Parameters | |
|---|---|
| `package` | `String`: This value cannot be`null`. | 

| Returns | |
|---|---|
| `boolean` | `true`if the given package is stopped,`false`otherwise | 

| Throws | |
|---|---|
|  | if the package could not be found. | 

**See also:**

### isPackageSuspended  

    [API level 29](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public boolean isPackageSuspended ([String](https://developer.android.com/reference/java/lang/String)packageName)

Query if an app is currently suspended.

| Parameters | |
|---|---|
| `package` | `String`: This value cannot be`null`. | 

| Returns | |
|---|---|
| `boolean` | `true`if the given package is suspended,`false`otherwise | 

| Throws | |
|---|---|
|  | if the package could not be found. | 

**See also:**

### isPackageSuspended  

    [API level 28](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public boolean isPackageSuspended ()

Apps can query this to know if they have been suspended. A system app with the permission
 `android.permission.SUSPEND_APPS` can put any app on the device into a suspended state.
 

While in this state, the application's notifications will be hidden, any of its started activities will be stopped and it will not be able to show toasts or dialogs or play audio. When the user tries to launch a suspended app, the system will, instead, show a dialog to the user informing them that they cannot use this app while it is suspended.

When an app is put into this state, the broadcast action
 [Intent.ACTION_MY_PACKAGE_SUSPENDED](https://developer.android.com/reference/android/content/Intent#ACTION_MY_PACKAGE_SUSPENDED)*including manifest
 receivers.* Similarly, a broadcast action [Intent.ACTION_MY_PACKAGE_UNSUSPENDED](https://developer.android.com/reference/android/content/Intent#ACTION_MY_PACKAGE_UNSUSPENDED)

| Returns | |
|---|---|
| `boolean` | `true`if the calling package has been suspended,`false`otherwise. | 

### isPermissionRevokedByPolicy    

    [API level 23](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public abstract boolean isPermissionRevokedByPolicy ([String](https://developer.android.com/reference/java/lang/String)permName,[String](https://developer.android.com/reference/java/lang/String)packageName)

Checks whether a particular permissions has been revoked for a package by policy. Typically the device owner or the profile owner may apply such a policy. The user cannot grant policy revoked permissions, hence the only way for an app to get such a permission is by a policy change.

| Parameters | |
|---|---|
| `perm` | `String`: The name of the permission you are checking for.This value cannot be `null`. | 
| `package` | `String`: The name of the package you are checking against.This value cannot be `null`. | 

| Returns | |
|---|---|
| `boolean` | Whether the permission is restricted by policy. | 

### isSafeMode  

    [API level 3](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public abstract boolean isSafeMode ()

Return whether the device has been booted into safe mode.

| Returns | |
|---|---|
| `boolean` | |

### parseAndroidManifest  

    [API level 35](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public T parseAndroidManifest ([File](https://developer.android.com/reference/java/io/File)apkFile,[Function](https://developer.android.com/reference/java/util/function/Function)<[XmlResourceParser](https://developer.android.com/reference/android/content/res/XmlResourceParser), T> parserFunction)

Retrieve AndroidManifest.xml information for the given application apk file.

Example:

```
 Bundle result;
 try {
     result = getContext().getPackageManager().parseAndroidManifest(apkFile,
             xmlResourceParser -> {
                 Bundle bundle = new Bundle();
                 // Search the start tag
                 int type;
                 while ((type = xmlResourceParser.next()) != XmlPullParser.START_TAG
                         && type != XmlPullParser.END_DOCUMENT) {
                 }
                 if (type != XmlPullParser.START_TAG) {
                     return bundle;
                 }
                 // Start to read the tags and attributes from the xmlResourceParser
                 if (!xmlResourceParser.getName().equals("manifest")) {
                     return bundle;
                 }
                 String packageName = xmlResourceParser.getAttributeValue(null, "package");
                 bundle.putString("package", packageName);
                 // Continue to read the tags and attributes from the xmlResourceParser
                 return bundle;
             });
 } catch (IOException e) {
 }
 
```
This method may take several seconds to complete, so it should only be called from a worker thread.

| Parameters | |
|---|---|
| `apk` | `File`: The file of an application apk.This value cannot be `null`. | 
| `parser` | `Function`: The parserFunction will be invoked with the XmlResourceParser object
        after getting the AndroidManifest.xml of an application package.This value cannot be `null`. | 

| Returns | |
|---|---|
| `T` | Returns the result of the . | 

| Throws | |
|---|---|
|  | if the AndroidManifest.xml of an application package cannot be read or accessed. | 

### parseAndroidManifest  

    [API level 36](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public T parseAndroidManifest ([ParcelFileDescriptor](https://developer.android.com/reference/android/os/ParcelFileDescriptor)apkFileDescriptor,[Function](https://developer.android.com/reference/java/util/function/Function)<[XmlResourceParser](https://developer.android.com/reference/android/content/res/XmlResourceParser), T> parserFunction)

Similar to [parseAndroidManifest(File,Function)](https://developer.android.com/reference/android/content/pm/PackageManager#parseAndroidManifest(java.io.File,%20java.util.function.Function%3Candroid.content.res.XmlResourceParser,T%3E))

 This method may take several seconds to complete, so it should
            only be called from a worker thread.

| Parameters | |
|---|---|
| `apk` | `Parcel`: The file descriptor of an application apk.
 The parserFunction will be invoked with the XmlResourceParser object
        after getting the AndroidManifest.xml of an application package.This value cannot be `null`. | 
| `parser` | `Function`: This value cannot be`null`. | 

| Returns | |
|---|---|
| `T` | Returns the result of the . | 

| Throws | |
|---|---|
|  | if the AndroidManifest.xml of an application package cannot be read or accessed. | 

### queryActivityProperty  

    [API level 31](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public[List](https://developer.android.com/reference/java/util/List)<[PackageManager.Property](https://developer.android.com/reference/android/content/pm/PackageManager.Property)> queryActivityProperty ([String](https://developer.android.com/reference/java/lang/String)propertyName)

Returns the property definition for all <activity> and <activity-alias> tags.

If the property is not defined with any <activity> and <activity-alias> tag, returns and empty list.

| Parameters | |
|---|---|
| `property` | `String`: This value cannot be`null`. | 

| Returns | |
|---|---|
|  | This value cannot be `null`. | 

### queryApplicationProperty  

    [API level 31](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public[List](https://developer.android.com/reference/java/util/List)<[PackageManager.Property](https://developer.android.com/reference/android/content/pm/PackageManager.Property)> queryApplicationProperty ([String](https://developer.android.com/reference/java/lang/String)propertyName)

Returns the property definition for all <application> tags.

If the property is not defined with any <application> tag, returns and empty list.

| Parameters | |
|---|---|
| `property` | `String`: This value cannot be`null`. | 

| Returns | |
|---|---|
|  | This value cannot be `null`. | 

### queryBroadcastReceivers  

    [API level 33](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public[List](https://developer.android.com/reference/java/util/List)<[ResolveInfo](https://developer.android.com/reference/android/content/pm/ResolveInfo)> queryBroadcastReceivers ([Intent](https://developer.android.com/reference/android/content/Intent)intent,[PackageManager.ResolveInfoFlags](https://developer.android.com/reference/android/content/pm/PackageManager.ResolveInfoFlags)flags)

See [queryBroadcastReceivers(Intent,int)](https://developer.android.com/reference/android/content/pm/PackageManager#queryBroadcastReceivers(android.content.Intent,%20int))

| Parameters | |
|---|---|
| `intent` | `Intent`: This value cannot be`null`. | 
| `flags` | `Package`: This value cannot be`null`. | 

| Returns | |
|---|---|
|  | This value cannot be `null`. | 

### queryBroadcastReceivers  

    [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public abstract[List](https://developer.android.com/reference/java/util/List)<[ResolveInfo](https://developer.android.com/reference/android/content/pm/ResolveInfo)> queryBroadcastReceivers ([Intent](https://developer.android.com/reference/android/content/Intent)intent, int flags)

Retrieve all receivers that can handle a broadcast of the given intent.
 Use [queryBroadcastReceivers(Intent,ResolveInfoFlags)](https://developer.android.com/reference/android/content/pm/PackageManager#queryBroadcastReceivers(android.content.Intent,%20android.content.pm.PackageManager.ResolveInfoFlags))

| Parameters | |
|---|---|
| `intent` | `Intent`: The desired intent as per resolveActivity().This value cannot be `null`. | 
| `flags` | `int`: Additional option flags to modify the data returned. | 

| Returns | |
|---|---|
|  | Returns a List of ResolveInfo objects containing one entry for
         each matching receiver, ordered from best to worst. If there are
         no matching receivers, returns an empty list. This value cannot be `null`. | 

### queryContentProviders  

    [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public abstract[List](https://developer.android.com/reference/java/util/List)<[ProviderInfo](https://developer.android.com/reference/android/content/pm/ProviderInfo)> queryContentProviders ([String](https://developer.android.com/reference/java/lang/String)processName, int uid, int flags)

Retrieve content provider information.

 *Note: unlike most other methods, an empty result set is indicated
 by a null return instead of an empty list.*
 Use [queryContentProviders(String,int,ComponentInfoFlags)](https://developer.android.com/reference/android/content/pm/PackageManager#queryContentProviders(java.lang.String,%20int,%20android.content.pm.PackageManager.ComponentInfoFlags))

| Parameters | |
|---|---|
| `process` | `String`: If non-null, limits the returned providers to only
            those that are hosted by the given process. If null, all
            content providers are returned. | 
| `uid` | `int`: IfprocessNameis non-null, this is the required
            uid owning the requested content providers. | 
| `flags` | `int`: Additional option flags to modify the data returned. | 

| Returns | |
|---|---|
|  | A list of objects containing one entry for
         each provider either matchingprocessNameor, ifprocessNameis null, all known content providers.If there are no matching providers, null is returned. | 

### queryContentProviders  

    [API level 33](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public[List](https://developer.android.com/reference/java/util/List)<[ProviderInfo](https://developer.android.com/reference/android/content/pm/ProviderInfo)> queryContentProviders ([String](https://developer.android.com/reference/java/lang/String)processName, int uid,[PackageManager.ComponentInfoFlags](https://developer.android.com/reference/android/content/pm/PackageManager.ComponentInfoFlags)flags)

See [queryContentProviders(String,int,int)](https://developer.android.com/reference/android/content/pm/PackageManager#queryContentProviders(java.lang.String,%20int,%20int))

| Parameters | |
|---|---|
| `process` | `String`: This value may be`null`. | 
| `uid` | `int` | 
| `flags` | `Package`: This value cannot be`null`. | 

| Returns | |
|---|---|
|  | This value cannot be `null`. | 

### queryInstrumentation 

    [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public abstract[List](https://developer.android.com/reference/java/util/List)<[InstrumentationInfo](https://developer.android.com/reference/android/content/pm/InstrumentationInfo)> queryInstrumentation ([String](https://developer.android.com/reference/java/lang/String)targetPackage, int flags)

Retrieve information about available instrumentation code. May be used to retrieve either all instrumentation code, or only the code targeting a particular package.

| Parameters | |
|---|---|
| `target` | `String`: If null, all instrumentation is returned; only the
            instrumentation targeting this package name is returned. | 
| `flags` | `int`: Additional option flags to modify the data returned.Value is either `0`or | 

| Returns | |
|---|---|
|  | A list of objects containing one
         entry for each matching instrumentation. If there are no
         instrumentation available, returns an empty list.This value cannot be `null`. | 

### queryIntentActivities  

    [API level 33](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public[List](https://developer.android.com/reference/java/util/List)<[ResolveInfo](https://developer.android.com/reference/android/content/pm/ResolveInfo)> queryIntentActivities ([Intent](https://developer.android.com/reference/android/content/Intent)intent,[PackageManager.ResolveInfoFlags](https://developer.android.com/reference/android/content/pm/PackageManager.ResolveInfoFlags)flags)

See [queryIntentActivities(Intent,int)](https://developer.android.com/reference/android/content/pm/PackageManager#queryIntentActivities(android.content.Intent,%20int))

| Parameters | |
|---|---|
| `intent` | `Intent`: This value cannot be`null`. | 
| `flags` | `Package`: This value cannot be`null`. | 

| Returns | |
|---|---|
|  | This value cannot be `null`. | 

### queryIntentActivities  

    [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public abstract[List](https://developer.android.com/reference/java/util/List)<[ResolveInfo](https://developer.android.com/reference/android/content/pm/ResolveInfo)> queryIntentActivities ([Intent](https://developer.android.com/reference/android/content/Intent)intent, int flags)

Retrieve all activities that can be performed for the given intent.
 Use [queryIntentActivities(Intent,ResolveInfoFlags)](https://developer.android.com/reference/android/content/pm/PackageManager#queryIntentActivities(android.content.Intent,%20android.content.pm.PackageManager.ResolveInfoFlags))

| Parameters | |
|---|---|
| `intent` | `Intent`: The desired intent as per resolveActivity().This value cannot be `null`. | 
| `flags` | `int`: Additional option flags to modify the data returned. The
            most important is, to limit the
            resolution to only those activities that support the. Or, setto prevent any filtering of the results. | 

| Returns | |
|---|---|
|  | Returns a List of ResolveInfo objects containing one entry for
         each matching activity, ordered from best to worst. In other
         words, the first item is what would be returned by . If there are no matching activities, an
         empty list is returned.This value cannot be `null`. | 

### queryIntentActivityOptions   

    [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public abstract[List](https://developer.android.com/reference/java/util/List)<[ResolveInfo](https://developer.android.com/reference/android/content/pm/ResolveInfo)> queryIntentActivityOptions ([ComponentName](https://developer.android.com/reference/android/content/ComponentName)caller,[Intent[]](https://developer.android.com/reference/android/content/Intent)specifics,[Intent](https://developer.android.com/reference/android/content/Intent)intent, int flags)

Retrieve a set of activities that should be presented to the user as
 similar options. This is like [queryIntentActivities(Intent, ResolveInfoFlags)](https://developer.android.com/reference/android/content/pm/PackageManager#queryIntentActivities(android.content.Intent,%20android.content.pm.PackageManager.ResolveInfoFlags))[queryIntentActivityOptions(ComponentName,List,Intent,ResolveInfoFlags)](https://developer.android.com/reference/android/content/pm/PackageManager#queryIntentActivityOptions(android.content.ComponentName,%20java.util.List%3Candroid.content.Intent%3E,%20android.content.Intent,%20android.content.pm.PackageManager.ResolveInfoFlags))

| Parameters | |
|---|---|
| `caller` | `Component`: The class name of the activity that is making the request.
            This activity will never appear in the output list. Can be
            null. | 
| `specifics` | `Intent`: An array of Intents that should be resolved to the first
            specific results. Can be null. | 
| `intent` | `Intent`: The desired intent as per resolveActivity().This value cannot be `null`. | 
| `flags` | `int`: Additional option flags to modify the data returned. The
            most important is, to limit the
            resolution to only those activities that support the. | 

| Returns | |
|---|---|
|  | Returns a List of ResolveInfo objects containing one entry for
         each matching activity. The list is ordered first by all of the
         intents resolved in specificsand then any additional
         activities that can handleintentbut did not get
         included by one of thespecificsintents. If there are
         no matching activities, an empty list is returned.This value cannot be `null`. | 

### queryIntentActivityOptions   

    [API level 33](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public[List](https://developer.android.com/reference/java/util/List)<[ResolveInfo](https://developer.android.com/reference/android/content/pm/ResolveInfo)> queryIntentActivityOptions ([ComponentName](https://developer.android.com/reference/android/content/ComponentName)caller,[List](https://developer.android.com/reference/java/util/List)<[Intent](https://developer.android.com/reference/android/content/Intent)> specifics,[Intent](https://developer.android.com/reference/android/content/Intent)intent,[PackageManager.ResolveInfoFlags](https://developer.android.com/reference/android/content/pm/PackageManager.ResolveInfoFlags)flags)

See [queryIntentActivityOptions(ComponentName,Intent[],Intent,int)](https://developer.android.com/reference/android/content/pm/PackageManager#queryIntentActivityOptions(android.content.ComponentName,%20android.content.Intent[],%20android.content.Intent,%20int))

| Parameters | |
|---|---|
| `caller` | `Component`: This value may be`null`. | 
| `specifics` | `List`: This value may be`null`. | 
| `intent` | `Intent`: This value cannot be`null`. | 
| `flags` | `Package`: This value cannot be`null`. | 

| Returns | |
|---|---|
|  | This value cannot be `null`. | 

### queryIntentContentProviders   

    [API level 33](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public[List](https://developer.android.com/reference/java/util/List)<[ResolveInfo](https://developer.android.com/reference/android/content/pm/ResolveInfo)> queryIntentContentProviders ([Intent](https://developer.android.com/reference/android/content/Intent)intent,[PackageManager.ResolveInfoFlags](https://developer.android.com/reference/android/content/pm/PackageManager.ResolveInfoFlags)flags)

See [queryIntentContentProviders(Intent,int)](https://developer.android.com/reference/android/content/pm/PackageManager#queryIntentContentProviders(android.content.Intent,%20int))

| Parameters | |
|---|---|
| `intent` | `Intent`: This value cannot be`null`. | 
| `flags` | `Package`: This value cannot be`null`. | 

| Returns | |
|---|---|
|  | This value cannot be `null`. | 

### queryIntentContentProviders   

    [API level 19](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public abstract[List](https://developer.android.com/reference/java/util/List)<[ResolveInfo](https://developer.android.com/reference/android/content/pm/ResolveInfo)> queryIntentContentProviders ([Intent](https://developer.android.com/reference/android/content/Intent)intent, int flags)

Retrieve all providers that can match the given intent.
 Use [queryIntentContentProviders(Intent,ResolveInfoFlags)](https://developer.android.com/reference/android/content/pm/PackageManager#queryIntentContentProviders(android.content.Intent,%20android.content.pm.PackageManager.ResolveInfoFlags))

| Parameters | |
|---|---|
| `intent` | `Intent`: An intent containing all of the desired specification
            (action, data, type, category, and/or component).This value cannot be `null`. | 
| `flags` | `int`: Additional option flags to modify the data returned. | 

| Returns | |
|---|---|
|  | Returns a List of ResolveInfo objects containing one entry for
         each matching provider, ordered from best to worst. If there are
         no matching services, returns an empty list. This value cannot be `null`. | 

### queryIntentServices  

    [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public abstract[List](https://developer.android.com/reference/java/util/List)<[ResolveInfo](https://developer.android.com/reference/android/content/pm/ResolveInfo)> queryIntentServices ([Intent](https://developer.android.com/reference/android/content/Intent)intent, int flags)

Retrieve all services that can match the given intent.
 Use [queryIntentServices(Intent,ResolveInfoFlags)](https://developer.android.com/reference/android/content/pm/PackageManager#queryIntentServices(android.content.Intent,%20android.content.pm.PackageManager.ResolveInfoFlags))

| Parameters | |
|---|---|
| `intent` | `Intent`: The desired intent as per resolveService().This value cannot be `null`. | 
| `flags` | `int`: Additional option flags to modify the data returned. | 

| Returns | |
|---|---|
|  | Returns a List of ResolveInfo objects containing one entry for
         each matching service, ordered from best to worst. In other
         words, the first item is what would be returned by . If there are no matching services,
         returns an empty list.This value cannot be `null`. | 

### queryIntentServices  

    [API level 33](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public[List](https://developer.android.com/reference/java/util/List)<[ResolveInfo](https://developer.android.com/reference/android/content/pm/ResolveInfo)> queryIntentServices ([Intent](https://developer.android.com/reference/android/content/Intent)intent,[PackageManager.ResolveInfoFlags](https://developer.android.com/reference/android/content/pm/PackageManager.ResolveInfoFlags)flags)

See [queryIntentServices(Intent,int)](https://developer.android.com/reference/android/content/pm/PackageManager#queryIntentServices(android.content.Intent,%20int))

| Parameters | |
|---|---|
| `intent` | `Intent`: This value cannot be`null`. | 
| `flags` | `Package`: This value cannot be`null`. | 

| Returns | |
|---|---|
|  | This value cannot be `null`. | 

### queryPermissionsByGroup   

    [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public abstract[List](https://developer.android.com/reference/java/util/List)<[PermissionInfo](https://developer.android.com/reference/android/content/pm/PermissionInfo)> queryPermissionsByGroup ([String](https://developer.android.com/reference/java/lang/String)permissionGroup, int flags)

Query for all of the permissions associated with a particular group.

| Parameters | |
|---|---|
| `permission` | `String`: The fully qualified name (i.e. com.google.permission.LOGIN)
            of the permission group you are interested in. Use`null`to
            find all of the permissions not associated with a group. | 
| `flags` | `int`: Additional option flags to modify the data returned.Value is either `0`or | 

| Returns | |
|---|---|
|  | Returns a list of containing information
         about all of the permissions in the given group.This value cannot be `null`. | 

| Throws | |
|---|---|
|  | if a group with the given name cannot be found on the system. | 

### queryProviderProperty  

    [API level 31](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public[List](https://developer.android.com/reference/java/util/List)<[PackageManager.Property](https://developer.android.com/reference/android/content/pm/PackageManager.Property)> queryProviderProperty ([String](https://developer.android.com/reference/java/lang/String)propertyName)

Returns the property definition for all <provider> tags.

If the property is not defined with any <provider> tag, returns and empty list.

| Parameters | |
|---|---|
| `property` | `String`: This value cannot be`null`. | 

| Returns | |
|---|---|
|  | This value cannot be `null`. | 

### queryReceiverProperty  

    [API level 31](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public[List](https://developer.android.com/reference/java/util/List)<[PackageManager.Property](https://developer.android.com/reference/android/content/pm/PackageManager.Property)> queryReceiverProperty ([String](https://developer.android.com/reference/java/lang/String)propertyName)

Returns the property definition for all <receiver> tags.

If the property is not defined with any <receiver> tag, returns and empty list.

| Parameters | |
|---|---|
| `property` | `String`: This value cannot be`null`. | 

| Returns | |
|---|---|
|  | This value cannot be `null`. | 

### queryServiceProperty  

    [API level 31](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public[List](https://developer.android.com/reference/java/util/List)<[PackageManager.Property](https://developer.android.com/reference/android/content/pm/PackageManager.Property)> queryServiceProperty ([String](https://developer.android.com/reference/java/lang/String)propertyName)

Returns the property definition for all <service> tags.

If the property is not defined with any <service> tag, returns and empty list.

| Parameters | |
|---|---|
| `property` | `String`: This value cannot be`null`. | 

| Returns | |
|---|---|
|  | This value cannot be `null`. | 

### relinquishUpdateOwnership  

    [API level 34](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public void relinquishUpdateOwnership ([String](https://developer.android.com/reference/java/lang/String)targetPackage)

Attempt to relinquish the update ownership of the given package. Only the current update owner of the given package can use this API.

| Parameters | |
|---|---|
| `target` | `String`: The installed package whose update owner will be changed.This value cannot be `null`. | 

| Throws | |
|---|---|
|  | if the given package is invalid. | 
|  | if you are not the current update owner of the given package. | 

### removePackageFromPreferred   

    public abstract void removePackageFromPreferred ([String](https://developer.android.com/reference/java/lang/String)packageName)


**
      This method was deprecated
      in API level 15.**

    This function no longer does anything. It is the platform's
 responsibility to assign preferred activities and this cannot be modified
 directly. To determine the activities resolved by the platform, use
 [resolveActivity(Intent, ResolveInfoFlags)](https://developer.android.com/reference/android/content/pm/PackageManager#resolveActivity(android.content.Intent,%20android.content.pm.PackageManager.ResolveInfoFlags))[queryIntentActivities(Intent, ResolveInfoFlags)](https://developer.android.com/reference/android/content/pm/PackageManager#queryIntentActivities(android.content.Intent,%20android.content.pm.PackageManager.ResolveInfoFlags))[RoleManager](https://developer.android.com/reference/android/app/role/RoleManager)

| Parameters | |
|---|---|
| `package` | `String`: This value cannot be`null`. | 

### removePermission 

    [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public abstract void removePermission ([String](https://developer.android.com/reference/java/lang/String)permName)

Removes a permission that was previously added with
 [addPermission(PermissionInfo)](https://developer.android.com/reference/android/content/pm/PackageManager#addPermission(android.content.pm.PermissionInfo))

| Parameters | |
|---|---|
| `perm` | `String`: The name of the permission to remove.This value cannot be `null`. | 

| Throws | |
|---|---|
|  | if you are not allowed to remove the given permission name. | 

**See also:**

### removeWhitelistedRestrictedPermission   

    [API level 29](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public boolean removeWhitelistedRestrictedPermission ([String](https://developer.android.com/reference/java/lang/String)packageName,[String](https://developer.android.com/reference/java/lang/String)permName, int whitelistFlags)

Removes a whitelisted restricted permission for an app.

 Permissions can be hard restricted which means that the app cannot hold
 them or soft restricted where the app can hold the permission but in a weaker
 form. Whether a permission is [hard
 restricted](https://developer.android.com/reference/android/content/pm/PermissionInfo#FLAG_HARD_RESTRICTED)[soft restricted](https://developer.android.com/reference/android/content/pm/PermissionInfo#FLAG_SOFT_RESTRICTED)

- There are four whitelists:
 
- one for cases where the system permission policy whitelists a permission
 This list corresponds to the [FLAG_PERMISSION_WHITELIST_SYSTEM](https://developer.android.com/reference/android/content/pm/PackageManager#FLAG_PERMISSION_WHITELIST_SYSTEM)
- one for cases where the system whitelists the permission when upgrading
 from an OS version in which the permission was not restricted to an OS version
 in which the permission is restricted. This list corresponds to the [FLAG_PERMISSION_WHITELIST_UPGRADE](https://developer.android.com/reference/android/content/pm/PackageManager#FLAG_PERMISSION_WHITELIST_UPGRADE)
- one for cases where the installer of the package whitelists a permission.
 This list corresponds to the [FLAG_PERMISSION_WHITELIST_INSTALLER](https://developer.android.com/reference/android/content/pm/PackageManager#FLAG_PERMISSION_WHITELIST_INSTALLER)
- one for cases where the system exempts the permission when upgrading
 from an OS version in which the permission was not restricted to an OS version
 in which the permission is restricted. This list corresponds to the [FLAG_PERMISSION_WHITELIST_UPGRADE](https://developer.android.com/reference/android/content/pm/PackageManager#FLAG_PERMISSION_WHITELIST_UPGRADE)

You need to specify the whitelists for which to set the whitelisted permissions which will clear the previous whitelisted permissions and replace them with the provided ones.

 **Note: **In retrospect it would have been preferred to use
 more inclusive terminology when naming this API. Similar APIs added will
 refrain from using the term "whitelist".
 

| Parameters | |
|---|---|
| `package` | `String`: The app for which to get whitelisted permissions.This value cannot be `null`. | 
| `perm` | `String`: The whitelisted permission to remove.This value cannot be `null`. | 
| `whitelist` | `int`: The whitelists from which to remove. Passing multiple flags
 updates all specified whitelists.Value is either `0`or a combination of the following: | 

| Returns | |
|---|---|
| `boolean` | Whether the permission was removed from the whitelist. | 

| Throws | |
|---|---|
|  | if you try to modify a whitelist that you have no access to. | 

### requestChecksums 

    [API level 31](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public void requestChecksums ([String](https://developer.android.com/reference/java/lang/String)packageName, boolean includeSplits, int required,[List](https://developer.android.com/reference/java/util/List)<[Certificate](https://developer.android.com/reference/java/security/cert/Certificate)> trustedInstallers,[PackageManager.OnChecksumsReadyListener](https://developer.android.com/reference/android/content/pm/PackageManager.OnChecksumsReadyListener)onChecksumsReadyListener)

Requests the checksums for APKs within a package.
 The checksums will be returned asynchronously via onChecksumsReadyListener.
 By default returns all readily available checksums:
 - enforced by platform,
 - enforced by installer.
 If caller needs a specific checksum kind, they can specify it as required.
 **Caution: Android can not verify installer-provided checksums. Make sure you specify
 trusted installers.**

| Parameters | |
|---|---|
| `package` | `String`: whose checksums to return.This value cannot be `null`. | 
| `include` | `boolean`: whether to include checksums for non-base splits. | 
| `required` | `int`: explicitly request the checksum types. May incur significant
                 CPU/memory/disk usage.Value is either `0`or a combination of the following: | 
| `trusted` | `List`: for checksums enforced by installer, which installers are to be
                          trusted.will return checksums from any installer,disables optimized installer-enforced checksums,
                          otherwise the list has to be non-empty list of certificates.This value cannot be `null`. | 
| `on` | `Package`: called once when the results are available.This value cannot be `null`. | 

| Throws | |
|---|---|
|  | if a package with the given name cannot be found on the system. | 
|  | if the list of trusted installer certificates is empty. | 
|  | if an encoding error occurs for trustedInstallers. | 

### resolveActivity 

    [API level 33](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public[ResolveInfo](https://developer.android.com/reference/android/content/pm/ResolveInfo)resolveActivity ([Intent](https://developer.android.com/reference/android/content/Intent)intent,[PackageManager.ResolveInfoFlags](https://developer.android.com/reference/android/content/pm/PackageManager.ResolveInfoFlags)flags)

See [resolveActivity(Intent,int)](https://developer.android.com/reference/android/content/pm/PackageManager#resolveActivity(android.content.Intent,%20int))

| Parameters | |
|---|---|
| `intent` | `Intent`: This value cannot be`null`. | 
| `flags` | `Package`: This value cannot be`null`. | 

| Returns | |
|---|---|
|  | This value may be `null`. | 

### resolveActivity 

    [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public abstract[ResolveInfo](https://developer.android.com/reference/android/content/pm/ResolveInfo)resolveActivity ([Intent](https://developer.android.com/reference/android/content/Intent)intent, int flags)

Determine the best action to perform for a given Intent. This is how
 [Intent.resolveActivity](https://developer.android.com/reference/android/content/Intent#resolveActivity(android.content.pm.PackageManager))

 *Note:* if using an implicit Intent (without an explicit
 ComponentName specified), be sure to consider whether to set the
 [MATCH_DEFAULT_ONLY](https://developer.android.com/reference/android/content/pm/PackageManager#MATCH_DEFAULT_ONLY)[android.content.Context.startActivity(Intent)](https://developer.android.com/reference/android/content/Context#startActivity(android.content.Intent))[Intent.resolveActivity(PackageManager)](https://developer.android.com/reference/android/content/Intent#resolveActivity(android.content.pm.PackageManager))

[resolveActivity(Intent,ResolveInfoFlags)](https://developer.android.com/reference/android/content/pm/PackageManager#resolveActivity(android.content.Intent,%20android.content.pm.PackageManager.ResolveInfoFlags))| Parameters | |
|---|---|
| `intent` | `Intent`: An intent containing all of the desired specification
            (action, data, type, category, and/or component).This value cannot be `null`. | 
| `flags` | `int`: Additional option flags to modify the data returned. The
            most important is, to limit the
            resolution to only those activities that support the. | 

| Returns | |
|---|---|
|  | Returns a ResolveInfo object containing the final activity intent that was determined to be the best action. Returns null if no matching activity was found. If multiple matching activities are found and there is no default set, returns a ResolveInfo object containing something else, such as the activity resolver. | 

### resolveContentProvider  

    [API level 33](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public[ProviderInfo](https://developer.android.com/reference/android/content/pm/ProviderInfo)resolveContentProvider ([String](https://developer.android.com/reference/java/lang/String)authority,[PackageManager.ComponentInfoFlags](https://developer.android.com/reference/android/content/pm/PackageManager.ComponentInfoFlags)flags)

See [resolveContentProvider(String,int)](https://developer.android.com/reference/android/content/pm/PackageManager#resolveContentProvider(java.lang.String,%20int))

| Parameters | |
|---|---|
| `authority` | `String`: This value cannot be`null`. | 
| `flags` | `Package`: This value cannot be`null`. | 

| Returns | |
|---|---|
|  | This value may be `null`. | 

### resolveContentProvider  

    [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public abstract[ProviderInfo](https://developer.android.com/reference/android/content/pm/ProviderInfo)resolveContentProvider ([String](https://developer.android.com/reference/java/lang/String)authority, int flags)

Find a single content provider by its authority.

Example:


```
 Uri uri = Uri.parse("content://com.example.app.provider/table1");
 ProviderInfo info = packageManager.resolveContentProvider(uri.getAuthority(), flags);
 
```
[resolveContentProvider(String,ComponentInfoFlags)](https://developer.android.com/reference/android/content/pm/PackageManager#resolveContentProvider(java.lang.String,%20android.content.pm.PackageManager.ComponentInfoFlags))| Parameters | |
|---|---|
| `authority` | `String`: The authority of the provider to find.This value cannot be `null`. | 
| `flags` | `int`: Additional option flags to modify the data returned. | 

| Returns | |
|---|---|
|  | A object containing information about the
         provider. If a provider was not found, returns null. | 

### resolveService 

    [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public abstract[ResolveInfo](https://developer.android.com/reference/android/content/pm/ResolveInfo)resolveService ([Intent](https://developer.android.com/reference/android/content/Intent)intent, int flags)

Determine the best service to handle for a given Intent.
 Use [resolveService(Intent,ResolveInfoFlags)](https://developer.android.com/reference/android/content/pm/PackageManager#resolveService(android.content.Intent,%20android.content.pm.PackageManager.ResolveInfoFlags))

| Parameters | |
|---|---|
| `intent` | `Intent`: An intent containing all of the desired specification
            (action, data, type, category, and/or component).This value cannot be `null`. | 
| `flags` | `int`: Additional option flags to modify the data returned. | 

| Returns | |
|---|---|
|  | Returns a ResolveInfo object containing the final service intent that was determined to be the best action. Returns null if no matching service was found. | 

### resolveService 

    [API level 33](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public[ResolveInfo](https://developer.android.com/reference/android/content/pm/ResolveInfo)resolveService ([Intent](https://developer.android.com/reference/android/content/Intent)intent,[PackageManager.ResolveInfoFlags](https://developer.android.com/reference/android/content/pm/PackageManager.ResolveInfoFlags)flags)

See [resolveService(Intent,int)](https://developer.android.com/reference/android/content/pm/PackageManager#resolveService(android.content.Intent,%20int))

| Parameters | |
|---|---|
| `intent` | `Intent`: This value cannot be`null`. | 
| `flags` | `Package`: This value cannot be`null`. | 

| Returns | |
|---|---|
|  | This value may be `null`. | 

### setApplicationCategoryHint   

    [API level 26](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public abstract void setApplicationCategoryHint ([String](https://developer.android.com/reference/java/lang/String)packageName, int categoryHint)

Provide a hint of what the [ApplicationInfo.category](https://developer.android.com/reference/android/content/pm/ApplicationInfo#category)

 This hint can only be set by the app which installed this package, as
 determined by [getInstallerPackageName(String)](https://developer.android.com/reference/android/content/pm/PackageManager#getInstallerPackageName(java.lang.String))

| Parameters | |
|---|---|
| `package` | `String`: the package to change the category hint for.This value cannot be `null`. | 
| `category` | `int`: the category hint to set.Value is one of the following: 
 | 

### setApplicationEnabledSetting   

    [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public abstract void setApplicationEnabledSetting ([String](https://developer.android.com/reference/java/lang/String)packageName, int newState, int flags)

Set the enabled setting for an application
 This setting will override any enabled state which may have been set by the application in
 its manifest.  It also overrides the enabled state set in the manifest for any of the
 application's components.  It does not override any enabled state set by
 [setComponentEnabledSetting(ComponentName, int, int)](https://developer.android.com/reference/android/content/pm/PackageManager#setComponentEnabledSetting(android.content.ComponentName,%20int,%20int))

| Parameters | |
|---|---|
| `package` | `String`: The package name of the application to enable.This value cannot be `null`. | 
| `new` | `int`: The new enabled state for the application.Value is one of the following: | 
| `flags` | `int`: Optional behavior flags.Value is either `0`or a combination of the following: | 

### setAutoRevokeWhitelisted   

    [API level 30](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public boolean setAutoRevokeWhitelisted ([String](https://developer.android.com/reference/java/lang/String)packageName, boolean whitelisted)

Marks an application exempt from having its permissions be automatically revoked when the app is unused for an extended period of time. Only the installer on record that installed the given package is allowed to call this. Packages start in whitelisted state, and it is the installer's responsibility to un-whitelist the packages it installs, unless auto-revoking permissions from that package would cause breakages beyond having to re-request the permission(s).

 **Note: **In retrospect it would have been preferred to use
 more inclusive terminology when naming this API. Similar APIs added will
 refrain from using the term "whitelist".
 

| Parameters | |
|---|---|
| `package` | `String`: The app for which to set exemption.This value cannot be `null`. | 
| `whitelisted` | `boolean`: Whether the app should be whitelisted. | 

| Returns | |
|---|---|
| `boolean` | whether any change took effect. | 

| Throws | |
|---|---|
|  | if you you have no access to modify this. | 

**See also:**

### setComponentEnabledSetting   

    [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public abstract void setComponentEnabledSetting ([ComponentName](https://developer.android.com/reference/android/content/ComponentName)componentName, int newState, int flags)

Set the enabled setting for a package component (activity, receiver, service, provider). This setting will override any enabled state which may have been set by the component in its manifest.

Consider using [setComponentEnabledSettings(List)](https://developer.android.com/reference/android/content/pm/PackageManager#setComponentEnabledSettings(java.util.List%3Candroid.content.pm.PackageManager.ComponentEnabledSetting%3E))

| Parameters | |
|---|---|
| `component` | `Component`: The component to enable.This value cannot be `null`. | 
| `new` | `int`: The new enabled state for the component.Value is one of the following: | 
| `flags` | `int`: Optional behavior flags.Value is either `0`or a combination of the following: | 

### setComponentEnabledSettings   

    [API level 33](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public void setComponentEnabledSettings ([List](https://developer.android.com/reference/java/util/List)<[PackageManager.ComponentEnabledSetting](https://developer.android.com/reference/android/content/pm/PackageManager.ComponentEnabledSetting)> settings)

Set the enabled settings for package components such as activities, receivers, services and providers. This setting will override any enabled state which may have been set by the component in its manifest.

This api accepts a list of component changes, and applies them all atomically. The application can use this api if components have dependencies and need to be updated atomically.

The permission is not required if target components are running under the same uid with the caller.

| Parameters | |
|---|---|
| `settings` | `List`: The list of component enabled settings to update. Note that anis thrown if the duplicated component name
                 is in the list or there's a conflictflag between
                 different components in the same package.This value cannot be `null`. | 

### setInstallerPackageName   

    [API level 11](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public abstract void setInstallerPackageName ([String](https://developer.android.com/reference/java/lang/String)targetPackage,[String](https://developer.android.com/reference/java/lang/String)installerPackageName)

Change the installer associated with a given package. There are limitations on how the installer package can be changed; in particular:

-  A SecurityException will be thrown if `installerPackageName`is not signed with the same certificate as the calling application.
-  A SecurityException will be thrown if `targetPackage`already has an installer package, and that installer package is not signed with the same certificate as the calling application.

| Parameters | |
|---|---|
| `target` | `String`: The installed package whose installer will be changed.This value cannot be `null`. | 
| `installer` | `String`: The package name of the new installer.  May be
 null to clear the association. | 

### setMimeGroup  

    [API level 30](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public void setMimeGroup ([String](https://developer.android.com/reference/java/lang/String)mimeGroup,[Set](https://developer.android.com/reference/java/util/Set)<[String](https://developer.android.com/reference/java/lang/String)> mimeTypes)

Sets MIME group's MIME types. Libraries should use a reverse-DNS prefix followed by a ':' character and library-specific group name to avoid namespace collisions, e.g. "com.example:myFeature".

| Parameters | |
|---|---|
| `mime` | `String`: MIME group to modify.This value cannot be `null`. | 
| `mime` | `Set`: new MIME types contained by MIME group.This value cannot be `null`. | 

| Throws | |
|---|---|
|  | if the MIME group was not declared in the manifest. | 

### updateInstantAppCookie   

    [API level 26](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

public abstract void updateInstantAppCookie (byte[] cookie)

Updates the instant application cookie for the calling app. Non
 instant apps and apps that were instant but were upgraded
 to normal apps can still access this API. For instant apps
 this cookie is cached for some time after uninstall while for
 normal apps the cookie is deleted after the app is uninstalled.
 The cookie is always present while the app is installed. The
 cookie size is limited by [getInstantAppCookieMaxBytes()](https://developer.android.com/reference/android/content/pm/PackageManager#getInstantAppCookieMaxBytes())`null` or an empty array clears the cookie.
 

| Parameters | |
|---|---|
| `cookie` | `byte`: The cookie data.This value may be `null`. | 

| Throws | |
|---|---|
|  | if the array exceeds max cookie size. | 

### verifyPendingInstall  

    [API level 14](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

```
public abstract void verifyPendingInstall (int id, 
                int verificationCode)
```
Allows a package listening to the
 [package verification
 broadcast](https://developer.android.com/reference/android/content/Intent#ACTION_PACKAGE_NEEDS_VERIFICATION)`verificationCode` which is one of
 [PackageManager.VERIFICATION_ALLOW](https://developer.android.com/reference/android/content/pm/PackageManager#VERIFICATION_ALLOW)[PackageManager.VERIFICATION_REJECT](https://developer.android.com/reference/android/content/pm/PackageManager#VERIFICATION_REJECT)

| Parameters | |
|---|---|
| `id` | `int`: pending package identifier as passed via theIntent extra. | 
| `verification` | `int`: eitheror. | 

| Throws | |
|---|---|
|  | if the caller does not have the PACKAGE_VERIFICATION_AGENT permission. |