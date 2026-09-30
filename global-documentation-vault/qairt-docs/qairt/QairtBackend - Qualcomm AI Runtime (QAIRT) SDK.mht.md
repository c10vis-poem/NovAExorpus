# QairtBackend - Qualcomm AI Runtime (QAIRT) SDK

# QairtBackend

# QairtBackend

Note

Some methods in this module are not yet implemented in the current release and will raise an exception if called. See the C API for full functionality.

**Include:** `#include "QairtCppApi/QairtBackend.hpp"`

C++ wrapper for the QAIRT Backend API.

- 
namespace qairt
- Enums - 
enum class BackendError : std::underlying_type_t<[QairtBackend_Error_t](https://docs.qualcomm.com/doc/80-63442-10/topic/QairtBackend.html#_CPPv420QairtBackend_Error_t)>
- Error codes returned by QAIRT backend operations. - Enumerator - Description - `NoError`- Operation succeeded. - `MemAlloc`- Memory allocation failure. - `UnsupportedPlatform`- [Backend](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtBackend.html#classqairt_1_1Backend)creation attempted on an unsupported platform.- `CannotInitialize`- [Backend](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtBackend.html#classqairt_1_1Backend)failed to initialize.- `TerminateFailed`- Failed to free allocated resources during termination. - `NotSupported`- Requested functionality is not supported by this backend. - `InvalidArgument`- An argument to the operation was invalid. - `OpPackageNotFound`- The specified op package library could not be found. - `OpPackageIfProviderNotFound`- The interface provider symbol was not found in the op package. - `OpPackageRegistrationFailed`- Op package registration failed. - `OpPackageUnsupportedVersion`- The op package interface version is not supported. - `OpPackageDuplicate`- An op with the same package and op name is already registered. - `InconsistentConfig`- [Backend](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtBackend.html#classqairt_1_1Backend)configuration is inconsistent across create calls.- `InvalidHandle`- The provided backend handle is not valid. - `InvalidConfig`- One or more configuration values are invalid. - `Undefined`- An undefined or unknown error occurred. - *Values:*- 
enumerator NoError = [QAIRT_BACKEND_NO_ERROR](https://docs.qualcomm.com/doc/80-63442-10/topic/QairtBackend.html#_CPPv4N20QairtBackend_Error_t22QAIRT_BACKEND_NO_ERRORE)
 - 
enumerator MemAlloc = [QAIRT_BACKEND_ERROR_MEM_ALLOC](https://docs.qualcomm.com/doc/80-63442-10/topic/QairtBackend.html#_CPPv4N20QairtBackend_Error_t29QAIRT_BACKEND_ERROR_MEM_ALLOCE)
 - 
enumerator UnsupportedPlatform = [QAIRT_BACKEND_ERROR_UNSUPPORTED_PLATFORM](https://docs.qualcomm.com/doc/80-63442-10/topic/QairtBackend.html#_CPPv4N20QairtBackend_Error_t40QAIRT_BACKEND_ERROR_UNSUPPORTED_PLATFORME)
 - 
enumerator CannotInitialize = [QAIRT_BACKEND_ERROR_CANNOT_INITIALIZE](https://docs.qualcomm.com/doc/80-63442-10/topic/QairtBackend.html#_CPPv4N20QairtBackend_Error_t37QAIRT_BACKEND_ERROR_CANNOT_INITIALIZEE)
 - 
enumerator TerminateFailed = [QAIRT_BACKEND_ERROR_TERMINATE_FAILED](https://docs.qualcomm.com/doc/80-63442-10/topic/QairtBackend.html#_CPPv4N20QairtBackend_Error_t36QAIRT_BACKEND_ERROR_TERMINATE_FAILEDE)
 - 
enumerator NotSupported = [QAIRT_BACKEND_ERROR_NOT_SUPPORTED](https://docs.qualcomm.com/doc/80-63442-10/topic/QairtBackend.html#_CPPv4N20QairtBackend_Error_t33QAIRT_BACKEND_ERROR_NOT_SUPPORTEDE)
 - 
enumerator InvalidArgument = [QAIRT_BACKEND_ERROR_INVALID_ARGUMENT](https://docs.qualcomm.com/doc/80-63442-10/topic/QairtBackend.html#_CPPv4N20QairtBackend_Error_t36QAIRT_BACKEND_ERROR_INVALID_ARGUMENTE)
 - 
enumerator OpPackageNotFound = [QAIRT_BACKEND_ERROR_OP_PACKAGE_NOT_FOUND](https://docs.qualcomm.com/doc/80-63442-10/topic/QairtBackend.html#_CPPv4N20QairtBackend_Error_t40QAIRT_BACKEND_ERROR_OP_PACKAGE_NOT_FOUNDE)
 - 
enumerator OpPackageIfProviderNotFound = [QAIRT_BACKEND_ERROR_OP_PACKAGE_IF_PROVIDER_NOT_FOUND](https://docs.qualcomm.com/doc/80-63442-10/topic/QairtBackend.html#_CPPv4N20QairtBackend_Error_t52QAIRT_BACKEND_ERROR_OP_PACKAGE_IF_PROVIDER_NOT_FOUNDE)
 - 
enumerator OpPackageRegistrationFailed = [QAIRT_BACKEND_ERROR_OP_PACKAGE_REGISTRATION_FAILED](https://docs.qualcomm.com/doc/80-63442-10/topic/QairtBackend.html#_CPPv4N20QairtBackend_Error_t50QAIRT_BACKEND_ERROR_OP_PACKAGE_REGISTRATION_FAILEDE)
 - 
enumerator OpPackageUnsupportedVersion = [QAIRT_BACKEND_ERROR_OP_PACKAGE_UNSUPPORTED_VERSION](https://docs.qualcomm.com/doc/80-63442-10/topic/QairtBackend.html#_CPPv4N20QairtBackend_Error_t50QAIRT_BACKEND_ERROR_OP_PACKAGE_UNSUPPORTED_VERSIONE)
 - 
enumerator OpPackageDuplicate = [QAIRT_BACKEND_ERROR_OP_PACKAGE_DUPLICATE](https://docs.qualcomm.com/doc/80-63442-10/topic/QairtBackend.html#_CPPv4N20QairtBackend_Error_t40QAIRT_BACKEND_ERROR_OP_PACKAGE_DUPLICATEE)
 - 
enumerator InconsistentConfig = [QAIRT_BACKEND_ERROR_INCONSISTENT_CONFIG](https://docs.qualcomm.com/doc/80-63442-10/topic/QairtBackend.html#_CPPv4N20QairtBackend_Error_t39QAIRT_BACKEND_ERROR_INCONSISTENT_CONFIGE)
 - 
enumerator InvalidHandle = [QAIRT_BACKEND_ERROR_INVALID_HANDLE](https://docs.qualcomm.com/doc/80-63442-10/topic/QairtBackend.html#_CPPv4N20QairtBackend_Error_t34QAIRT_BACKEND_ERROR_INVALID_HANDLEE)
 - 
enumerator InvalidConfig = [QAIRT_BACKEND_ERROR_INVALID_CONFIG](https://docs.qualcomm.com/doc/80-63442-10/topic/QairtBackend.html#_CPPv4N20QairtBackend_Error_t34QAIRT_BACKEND_ERROR_INVALID_CONFIGE)
 - 
enumerator Undefined = [QAIRT_BACKEND_ERROR_UNDEFINED](https://docs.qualcomm.com/doc/80-63442-10/topic/QairtBackend.html#_CPPv4N20QairtBackend_Error_t29QAIRT_BACKEND_ERROR_UNDEFINEDE)
 
- 
enumerator NoError = 
 - 
enum class ErrorReportingConfigLevel : std::underlying_type_t<[QairtErrorReporting_Config_Level_t](https://docs.qualcomm.com/doc/80-63442-10/topic/QairtCommon.html#_CPPv434QairtErrorReporting_Config_Level_t)>
- Verbosity levels for the error reporting configuration. - Enumerator - Description - `Brief`- Collect basic summary information about each error. - `Detailed`- Collect detailed, memory-resident error information. - `Undefined`- Level is unset or unknown. - *Values:*- 
enumerator Brief = [QAIRT_ERROR_REPORTING_LEVEL_BRIEF](https://docs.qualcomm.com/doc/80-63442-10/topic/QairtCommon.html#_CPPv4N34QairtErrorReporting_Config_Level_t33QAIRT_ERROR_REPORTING_LEVEL_BRIEFE)
 - 
enumerator Detailed = [QAIRT_ERROR_REPORTING_LEVEL_DETAILED](https://docs.qualcomm.com/doc/80-63442-10/topic/QairtCommon.html#_CPPv4N34QairtErrorReporting_Config_Level_t36QAIRT_ERROR_REPORTING_LEVEL_DETAILEDE)
 - 
enumerator Undefined = [QAIRT_ERROR_REPORTING_LEVEL_UNDEFINED](https://docs.qualcomm.com/doc/80-63442-10/topic/QairtCommon.html#_CPPv4N34QairtErrorReporting_Config_Level_t37QAIRT_ERROR_REPORTING_LEVEL_UNDEFINEDE)
 
- 
enumerator Brief = 
 - 
class Backend : public [qairt](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtBackend.html#_CPPv45qairt)::ApiType<[Backend](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtBackend.html#_CPPv4N5qairt7BackendE),[QairtBackend_V1_t](https://docs.qualcomm.com/doc/80-63442-10/topic/QairtBackend.html#_CPPv417QairtBackend_V1_t)>
- *#include <QairtBackend.hpp>*- Wrapper for a QAIRT - [Backend](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtBackend.html#classqairt_1_1Backend)handle.- Obtained via Api::createBackend(). - Public Functions - 
Backend() noexcept = default
 - 
Backend(const [Backend](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtBackend.html#_CPPv4N5qairt7Backend7BackendERK7Backend)&) = delete
 - 
Backend([Backend](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtBackend.html#_CPPv4N5qairt7Backend7BackendERR7Backend)&&) noexcept = default
 - 
inline void setConfig(const [BackendConfiguration](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtBackend.html#_CPPv4N5qairt20BackendConfigurationE)&config)
- Set configuration options on this backend after creation. - See also 
 - 
inline void registerOpPackage(const char *packagePath, const char *interfaceProvider, const char *target)
- Register an op package library with this backend. - Loads the shared library at - *packagePath*and registers its operations using the interface provider function- *interfaceProvider*. An optional- *target*platform string restricts registration to a specific processing unit.- See also - Parameters
- **packagePath**–- **[in]**Path on disk to the op package shared library. Must not be NULL.
- **interfaceProvider**–- **[in]**Name of the interface provider function exported by the op package library. Must not be NULL.
- **target**–- **[in]**Optional target platform string. NULL applies no target restriction.
 
- Throws
- invalid handle 
- NULL - *packagePath*or- *interfaceProvider*
- library not found 
- interface provider symbol not found 
- registration failure 
- unsupported op package interface version 
- duplicate op registration 
 
 
 - 
inline void registerOpPackage(const std::string &packagePath, const std::string &interfaceProvider, const std::string &target)
- Wrapper which allows for - `std::string`path arguments instead of- `const char*`.
 - 
inline std::vector<[BackendOperationName](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtBackend.html#_CPPv4N5qairt20BackendOperationNameE)> getSupportedOperations() const
- Get all operations supported by this backend, including built-in ops. - See also - Throws
- Returns
- Vector of - [BackendOperationName](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtBackend.html#classqairt_1_1BackendOperationName)descriptors, one per supported operation.
 
 - 
inline void validateOpConfig(const [OpConfig](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtOpConfig.html#_CPPv4N5qairt8OpConfigE)&opConfig)
- Validate an op configuration against the appropriate registered op package. - The backend selects the op package for validation based on attributes of - *opConfig*.- See also 
 - 
inline void validateContextBinary(ApiTypeRef<const [Device](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtDevice.html#_CPPv4N5qairt6DeviceE)&> device, ApiTypeRef<const[ContextBinaryBuffer](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtContext.html#_CPPv4N5qairt19ContextBinaryBufferE)&> contextBinary, ApiTypeRef<const[ContextConfiguration](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtContext.html#_CPPv4N5qairt20ContextConfigurationE)&> contextConfig)
- Validate a context binary against a device and context configuration. - Checks that the binary is compatible with - *device*and the options in- *contextConfig*before it is loaded via- [createContextFromBinary()](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtBackend.html#classqairt_1_1Backend_1a5c748e07f3e91a28fc55a43f32876df6).
 - 
inline [Context](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtContext.html#_CPPv4N5qairt7ContextE)createContext(ApiTypeRef<const[ContextConfiguration](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtContext.html#_CPPv4N5qairt20ContextConfigurationE)&> contextConfig = {})
- Create a context using this backend. - Creates a context with no device (uses backend default) and an optional context configuration. 
 - 
inline [Context](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtContext.html#_CPPv4N5qairt7ContextE)createContext(ApiTypeRef<const[Device](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtDevice.html#_CPPv4N5qairt6DeviceE)&> device, ApiTypeRef<const[ContextConfiguration](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtContext.html#_CPPv4N5qairt20ContextConfigurationE)&> contextConfig)
- Create a context for a specific device using this backend. 
 - 
inline [Context](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtContext.html#_CPPv4N5qairt7ContextE)createContextFromBinary(ApiTypeRef<const[Device](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtDevice.html#_CPPv4N5qairt6DeviceE)&> device, ApiTypeRef<const[ContextConfiguration](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtContext.html#_CPPv4N5qairt20ContextConfigurationE)&> contextConfig, ApiTypeRef<const[ContextBinaryBuffer](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtContext.html#_CPPv4N5qairt19ContextBinaryBufferE)&> contextBinaryBuffer, ApiTypeRef<const[Signal](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtSignal.html#_CPPv4N5qairt6SignalE)&> signal = {}, ApiTypeRef<const[Profile](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtProfile.html#_CPPv4N5qairt7ProfileE)&> profile = {})
- Create a context from a serialized context binary. - Pass a - [Signal](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtSignal.html#classqairt_1_1Signal)to enable aborting or timing out the load operation.- Parameters
- **device**–- **[in]**The device on which to load the context binary.
- **contextConfig**–- **[in]**- [Context](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtContext.html#classqairt_1_1Context)configuration. Optional.
- **contextBinaryBuffer**–- **[in]**The serialized context binary to load.
- **signal**–- **[in]**Optional signal to control the load operation.
- **profile**–- **[in]**Optional profile handle to collect load-time events.
 
- Throws
- [qairt](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtBackend.html#_CPPv45qairt)::- [Exception](https://docs.qualcomm.com/doc/80-63442-10/topic/QairtApi.html#_CPPv4N5qairt9ExceptionE)– on invalid handle, binary incompatibility, or configuration error.
- Returns
- A new - [Context](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtContext.html#classqairt_1_1Context).
 
 - 
inline [Profile](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtProfile.html#_CPPv4N5qairt7ProfileE)createProfile(uint32_t level)
- Create a profiling handle at the specified granularity. - See also 
 - Create a shared profiling handle at the specified granularity. - See also 
 - 
inline [Signal](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtSignal.html#_CPPv4N5qairt6SignalE)createSignal(ApiTypeRef<const[SignalConfiguration](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtSignal.html#_CPPv4N5qairt19SignalConfigurationE)&> signalConfig = {})
- Create a new signal object associated with this backend. - Signals are used to control the execution of API calls that accept them (e.g., Graph::execute, Context::createFromBinary). The created signal is idle and immediately available for use. - The signal is backend-scoped: the backend allocates any required synchronization primitives and validates signal support. A signal may only be used with the backend that created it. 
 - Private Functions - Private Members - 
[detail](https://docs.qualcomm.com/doc/80-63442-10/topic/QairtTypeTraits.html#_CPPv4N5qairt6detailE)::crossable<[detail](https://docs.qualcomm.com/doc/80-63442-10/topic/QairtTypeTraits.html#_CPPv4N5qairt6detailE)::set_only<[BackendConfiguration](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtBackend.html#_CPPv4N5qairt20BackendConfigurationE)>, nullptr, &interface_type::setConfig> m_memory
- Staging storage for a - [BackendConfiguration](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtBackend.html#classqairt_1_1BackendConfiguration)being crossed to the C layer.
 - Friends - 
*friend class*Api
 
- 
Backend() noexcept = default
 - 
class BackendConfiguration : public [qairt](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtBackend.html#_CPPv45qairt)::ApiType<[BackendConfiguration](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtBackend.html#_CPPv4N5qairt20BackendConfigurationE),[QairtBackend_ConfigV1_t](https://docs.qualcomm.com/doc/80-63442-10/topic/QairtBackend.html#_CPPv423QairtBackend_ConfigV1_t)>
- *#include <QairtBackend.hpp>*- Configuration object for backend creation and reconfiguration. - Construct directly — - `BackendConfiguration()`— and call setter methods to populate options before passing to Api::createBackend() or- [Backend::setConfig()](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtBackend.html#classqairt_1_1Backend_1a7da4018df5b85ea1b9eb0e86003e2eff). All setter methods return- `*this`to support method chaining.- Public Functions - 
BackendConfiguration() noexcept = default
 - 
BackendConfiguration(const [BackendConfiguration](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtBackend.html#_CPPv4N5qairt20BackendConfiguration20BackendConfigurationERK20BackendConfiguration)&) = delete
 - 
BackendConfiguration([BackendConfiguration](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtBackend.html#_CPPv4N5qairt20BackendConfiguration20BackendConfigurationERR20BackendConfiguration)&&) noexcept = default
 - 
[BackendConfiguration](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtBackend.html#_CPPv4N5qairt20BackendConfigurationE)&operator=(const[BackendConfiguration](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtBackend.html#_CPPv4N5qairt20BackendConfigurationE)&) = delete
 - 
[BackendConfiguration](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtBackend.html#_CPPv4N5qairt20BackendConfigurationE)&operator=([BackendConfiguration](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtBackend.html#_CPPv4N5qairt20BackendConfigurationE)&&) noexcept = default
 - 
inline [BackendConfiguration](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtBackend.html#_CPPv4N5qairt20BackendConfigurationE)&setCustomConfig(const[BackendCustomConfig](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtBackend.html#_CPPv4N5qairt19BackendCustomConfigE)&backendCustomConfig)
- Set a single backend-specific custom configuration item on this configuration. - See also 
 - 
inline [BackendConfiguration](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtBackend.html#_CPPv4N5qairt20BackendConfigurationE)&setCustomConfigs(const[BackendCustomConfiguration](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtBackend.html#_CPPv4N5qairt26BackendCustomConfigurationE)&config)
- Set a collection of backend-specific custom configuration items on this configuration. - See also 
 - 
inline uint32_t getNumPlatformOptions() const
- Get the number of platform options set on this configuration. 
 - 
inline std::string_view getPlatformOptionAt(uint32_t idx) const
- Get the platform option string at the specified index. - Parameters
- **idx**–- **[in]**Zero-based index into the platform options list. Must be less than- [getNumPlatformOptions()](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtBackend.html#classqairt_1_1BackendConfiguration_1ab694c821fc350e6f2964411b624f468d).
- Throws
- Returns
- The null-terminated platform option key-value pair string at - *idx*, or an empty view if the stored pointer is null.
 
 - 
inline std::vector<std::string_view> getPlatformOptions() const
- Get all platform option strings set on this configuration. 
 - 
inline [BackendConfiguration](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtBackend.html#_CPPv4N5qairt20BackendConfigurationE)&setPlatformOptions(const std::vector<const char*> &platformOptions)
- Set the platform options on this configuration from an array of C strings. 
 - 
inline [BackendConfiguration](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtBackend.html#_CPPv4N5qairt20BackendConfigurationE)&setPlatformOptions(const std::vector<std::string> &platformOptions)
- Wrapper which allows for - `std::string`platform option values instead of- `const char*`.
 - 
inline [BackendConfiguration](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtBackend.html#_CPPv4N5qairt20BackendConfigurationE)&setPlatformOptions(const std::vector<std::string_view> &platformOptions)
- Wrapper which allows for - `std::string_view`platform option values instead of- `const char*`.
 - 
inline [BackendConfiguration](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtBackend.html#_CPPv4N5qairt20BackendConfigurationE)&resetPlatformOptions()
- Clear all platform options from this configuration. 
 - 
inline std::optional<std::reference_wrapper<[ErrorReportingConfig](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtBackend.html#_CPPv4N5qairt20ErrorReportingConfigE)>> getErrorReportingConfig()
- Get the error reporting configuration attached to this backend configuration. - Throws
- Returns
- A reference wrapper to the attached - [ErrorReportingConfig](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtBackend.html#classqairt_1_1ErrorReportingConfig), or an empty optional if none has been set.
 
 - 
inline std::optional<std::reference_wrapper<[ErrorReportingConfig](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtBackend.html#_CPPv4N5qairt20ErrorReportingConfigE)>> getErrorReportingConfig() const
- Get the error reporting configuration attached to this backend configuration. - Throws
- Returns
- A const reference wrapper to the attached - [ErrorReportingConfig](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtBackend.html#classqairt_1_1ErrorReportingConfig), or an empty optional if none has been set.
 
 - 
inline void setErrorReportingConfig(const [ErrorReportingConfig](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtBackend.html#_CPPv4N5qairt20ErrorReportingConfigE)&errorReportingConfig)
- Attach an error reporting configuration to this backend configuration. 
 - Private Functions - 
inline void prepareToCross() const
 - 
inline void updateAfterCross() const
 - Private Members - 
std::optional<[detail](https://docs.qualcomm.com/doc/80-63442-10/topic/QairtTypeTraits.html#_CPPv4N5qairt6detailE)::crossable<[detail](https://docs.qualcomm.com/doc/80-63442-10/topic/QairtTypeTraits.html#_CPPv4N5qairt6detailE)::non_owning<[ErrorReportingConfig](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtBackend.html#_CPPv4N5qairt20ErrorReportingConfigE)>, &interface_type::getErrorReportingConfig, &interface_type::setErrorReportingConfig>> m_errorReportingConfig
- Optional error reporting configuration cross-linked to the C handle. 
 - Friends - 
*friend class*Api
 
- 
BackendConfiguration() noexcept = default
 - 
class BackendCustomConfig : public [qairt](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtBackend.html#_CPPv45qairt)::CustomConfigType
- *#include <QairtBackend.hpp>*- Abstract base class for a single backend-specific custom configuration item. - Subclass this to provide a backend-specific configuration handle to - [BackendConfiguration::setCustomConfig()](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtBackend.html#classqairt_1_1BackendConfiguration_1a98e1783af51c75c9f6cd8e7f78dd35e5). Refer to the backend documentation for the concrete subclass and valid handle values.- Public Functions - 
virtual ~BackendCustomConfig() = default
 - 
virtual [QairtBackend_CustomConfigHandle_t](https://docs.qualcomm.com/doc/80-63442-10/topic/QairtBackend.html#_CPPv433QairtBackend_CustomConfigHandle_t)getCustomConfigHandle() const = 0
- Get the underlying C handle for this custom configuration item. - Returns
- The backend-specific custom configuration handle. 
 
 - Protected Functions - 
BackendCustomConfig() = default
 - 
BackendCustomConfig(const [BackendCustomConfig](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtBackend.html#_CPPv4N5qairt19BackendCustomConfig19BackendCustomConfigERK19BackendCustomConfig)&) = default
 - 
BackendCustomConfig([BackendCustomConfig](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtBackend.html#_CPPv4N5qairt19BackendCustomConfig19BackendCustomConfigERR19BackendCustomConfig)&&) noexcept = default
 - 
[BackendCustomConfig](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtBackend.html#_CPPv4N5qairt19BackendCustomConfigE)&operator=(const[BackendCustomConfig](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtBackend.html#_CPPv4N5qairt19BackendCustomConfigE)&) = default
 - 
[BackendCustomConfig](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtBackend.html#_CPPv4N5qairt19BackendCustomConfigE)&operator=([BackendCustomConfig](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtBackend.html#_CPPv4N5qairt19BackendCustomConfigE)&&) noexcept = default
 
- 
virtual ~BackendCustomConfig() = default
 - 
class BackendCustomConfiguration
- *#include <QairtBackend.hpp>*- Abstract base class for a collection of backend-specific custom configuration items. - Subclass this to provide multiple backend-specific configuration handles to - [BackendConfiguration::setCustomConfigs()](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtBackend.html#classqairt_1_1BackendConfiguration_1a7d4f64eb9e7a204992b303ced8dbd0be). Refer to the backend documentation for the concrete subclass and valid handle values.- Public Functions - 
virtual ~BackendCustomConfiguration() = default
 - 
virtual std::vector<[QairtBackend_CustomConfigHandle_t](https://docs.qualcomm.com/doc/80-63442-10/topic/QairtBackend.html#_CPPv433QairtBackend_CustomConfigHandle_t)> getCustomConfigs() const = 0
- Get the list of underlying C handles for this custom configuration collection. - Returns
- Vector of backend-specific custom configuration handles. 
 
 - Protected Functions - 
BackendCustomConfiguration() = default
 - 
BackendCustomConfiguration(const [BackendCustomConfiguration](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtBackend.html#_CPPv4N5qairt26BackendCustomConfiguration26BackendCustomConfigurationERK26BackendCustomConfiguration)&) = default
 - 
BackendCustomConfiguration([BackendCustomConfiguration](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtBackend.html#_CPPv4N5qairt26BackendCustomConfiguration26BackendCustomConfigurationERR26BackendCustomConfiguration)&&) noexcept = default
 - 
[BackendCustomConfiguration](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtBackend.html#_CPPv4N5qairt26BackendCustomConfigurationE)&operator=(const[BackendCustomConfiguration](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtBackend.html#_CPPv4N5qairt26BackendCustomConfigurationE)&) = default
 - 
[BackendCustomConfiguration](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtBackend.html#_CPPv4N5qairt26BackendCustomConfigurationE)&operator=([BackendCustomConfiguration](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtBackend.html#_CPPv4N5qairt26BackendCustomConfigurationE)&&) noexcept = default
 
- 
virtual ~BackendCustomConfiguration() = default
 - 
class BackendOperationName
- *#include <QairtBackend.hpp>*- Name descriptor for a single operation supported by a backend. - Obtained from - [Backend::getSupportedOperations()](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtBackend.html#classqairt_1_1Backend_1a7fda133f7b89fadf2f68ccb9aaedac14). All string views are non-owning references to backend-managed memory.- Public Functions - 
constexpr BackendOperationName() noexcept = default
 - 
constexpr BackendOperationName(const [BackendOperationName](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtBackend.html#_CPPv4N5qairt20BackendOperationName20BackendOperationNameERK20BackendOperationName)&) noexcept = default
 - 
constexpr BackendOperationName([BackendOperationName](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtBackend.html#_CPPv4N5qairt20BackendOperationName20BackendOperationNameERR20BackendOperationName)&&) noexcept = default
 - 
constexpr [BackendOperationName](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtBackend.html#_CPPv4N5qairt20BackendOperationNameE)&operator=(const[BackendOperationName](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtBackend.html#_CPPv4N5qairt20BackendOperationNameE)&) noexcept = default
 - 
constexpr [BackendOperationName](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtBackend.html#_CPPv4N5qairt20BackendOperationNameE)&operator=([BackendOperationName](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtBackend.html#_CPPv4N5qairt20BackendOperationNameE)&&) noexcept = default
 - 
inline constexpr BackendOperationName(std::string_view packageName, std::string_view name, std::string_view target) noexcept
- Construct a - [BackendOperationName](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtBackend.html#classqairt_1_1BackendOperationName)from its three name components.- Parameters
- **packageName**–- **[in]**Name of the op package that provides this operation.
- **name**–- **[in]**Name of the operation within the op package.
- **target**–- **[in]**Target platform for this operation entry. May be empty if the backend does not distinguish targets.
 
 
 - 
inline const std::string_view &getPackageName() const noexcept
- Get the op package name for this operation. - Returns
- Name of the op package that provides this operation. 
 
 - 
inline const std::string_view &getName() const noexcept
- Get the operation name within its op package. - See also - Returns
- Name of the operation within its package. 
 
 - 
inline const std::string_view getTarget() const noexcept
- Get the target platform for this operation entry. - See also - Returns
- Target platform string, or an empty view if unused by this backend. 
 
 - Private Members - 
std::string_view m_packageName
- The op package that provides this operation. 
 - 
std::string_view m_name
- The name of the operation within its package. 
 - 
std::string_view m_target
- The target platform for which this operation entry is registered. 
 
- 
constexpr BackendOperationName() noexcept = default
 - 
class ErrorReportingConfig : public [qairt](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtBackend.html#_CPPv45qairt)::ApiType<[ErrorReportingConfig](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtBackend.html#_CPPv4N5qairt20ErrorReportingConfigE),[QairtErrorReporting_Config_V1_t](https://docs.qualcomm.com/doc/80-63442-10/topic/QairtCommon.html#_CPPv431QairtErrorReporting_Config_V1_t)>
- *#include <QairtBackend.hpp>*- Configuration object for backend error reporting behavior. - Controls how much detail is captured when errors occur and how much memory is reserved for error data. Obtained via Api::createBackend() or set on a - [BackendConfiguration](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtBackend.html#classqairt_1_1BackendConfiguration)before backend creation.- Public Functions - 
ErrorReportingConfig() = default
 - 
inline [ErrorReportingConfigLevel](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtBackend.html#_CPPv4N5qairt25ErrorReportingConfigLevelE)getReportingLevel() const
- Get the reporting verbosity level for this error reporting configuration. 
 - 
inline void setReportingLevel([ErrorReportingConfigLevel](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtBackend.html#_CPPv4N5qairt25ErrorReportingConfigLevelE)level)
- Set the reporting verbosity level for this error reporting configuration. 
 - 
inline uint32_t getStorageLimit() const
- Get the memory storage limit for this error reporting configuration. 
 - Private Functions - Friends - 
*friend class*Api
 - 
*friend class*::qairt::ApiType
 
- 
ErrorReportingConfig() = default
 
- 
enum class BackendError : std::underlying_type_t<