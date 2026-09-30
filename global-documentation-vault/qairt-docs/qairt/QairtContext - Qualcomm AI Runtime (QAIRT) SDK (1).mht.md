# QairtContext - Qualcomm AI Runtime (QAIRT) SDK (1)

# QairtContext

# QairtContext

Note

Some methods in this module are not yet implemented in the current release and will raise an exception if called. See the C API for full functionality.

**Include:** `#include "QairtCppApi/QairtContext.hpp"`

C++ wrapper for the QAIRT context API.

```
   A Backend must be created before constructing a Context object.
```
- 
namespace qairt
- Enums - 
enum class ContextBinaryCompatibilityType : std::underlying_type_t<[QairtContext_BinaryCompatibilityType_t](https://docs.qualcomm.com/doc/80-63442-10/topic/QairtContext.html#_CPPv438QairtContext_BinaryCompatibilityType_t)>
- Binary compatibility policy used when loading a cached context binary. - Enumerator - Description - `Permissive`- Binary is accepted if it can run on the device. Default policy. - `Strict`- Binary is accepted only if it fully utilizes hardware capability. - `Undefined`- Sentinel value; not a valid policy selection. - *Values:*- 
enumerator Permissive = [QAIRT_CONTEXT_BINARY_COMPATIBILITY_PERMISSIVE](https://docs.qualcomm.com/doc/80-63442-10/topic/QairtContext.html#_CPPv4N38QairtContext_BinaryCompatibilityType_t45QAIRT_CONTEXT_BINARY_COMPATIBILITY_PERMISSIVEE)
 - 
enumerator Strict = [QAIRT_CONTEXT_BINARY_COMPATIBILITY_STRICT](https://docs.qualcomm.com/doc/80-63442-10/topic/QairtContext.html#_CPPv4N38QairtContext_BinaryCompatibilityType_t41QAIRT_CONTEXT_BINARY_COMPATIBILITY_STRICTE)
 - 
enumerator Undefined = [QAIRT_CONTEXT_BINARY_COMPATIBILITY_TYPE_UNDEFINED](https://docs.qualcomm.com/doc/80-63442-10/topic/QairtContext.html#_CPPv4N38QairtContext_BinaryCompatibilityType_t49QAIRT_CONTEXT_BINARY_COMPATIBILITY_TYPE_UNDEFINEDE)
 
- 
enumerator Permissive = 
 - 
enum class ContextError : std::underlying_type_t<[QairtContext_Error_t](https://docs.qualcomm.com/doc/80-63442-10/topic/QairtContext.html#_CPPv420QairtContext_Error_t)>
- Error codes returned by QAIRT context operations. - Enumerator - Description - `NoError`- Operation succeeded. - `UnsupportedFeature`- An optional API feature is not supported by the backend. - `MemAlloc`- Memory allocation or deallocation failure. - `InvalidArgument`- An argument to the operation was invalid. - `CtxDoesNotExist`- The context has not yet been created in the backend. - `InvalidHandle`- The provided handle is not valid. - `NotFinalized`- Operation attempted before all graphs in the context were finalized. - `BinaryVersion`- The context binary has an incompatible version. - `CreateFromBinary`- Failed to create a context from a binary. - `GetBinarySizeFailed`- Failed to retrieve the size of the serialized context. - `GetBinaryFailed`- Failed to generate the serialized context. - `BinaryConfiguration`- The context binary configuration is invalid. - `SetProfile`- Failed to set profiling information. - `InvalidConfig`- One or more configuration values are invalid. - `BinarySuboptimal`- A suboptimal binary was used with strict compatibility mode. - `Aborted`- Call was aborted early due to a signal trigger. - `TimedOut`- Call was aborted early due to a signal timeout. - `IncrementInvalidBuffer`- The incremental binary buffer was not allocated by the backend. - `Undefined`- An undefined or unknown error occurred. - *Values:*- 
enumerator NoError = [QAIRT_CONTEXT_NO_ERROR](https://docs.qualcomm.com/doc/80-63442-10/topic/QairtContext.html#_CPPv4N20QairtContext_Error_t22QAIRT_CONTEXT_NO_ERRORE)
 - 
enumerator UnsupportedFeature = [QAIRT_CONTEXT_ERROR_UNSUPPORTED_FEATURE](https://docs.qualcomm.com/doc/80-63442-10/topic/QairtContext.html#_CPPv4N20QairtContext_Error_t39QAIRT_CONTEXT_ERROR_UNSUPPORTED_FEATUREE)
 - 
enumerator MemAlloc = [QAIRT_CONTEXT_ERROR_MEM_ALLOC](https://docs.qualcomm.com/doc/80-63442-10/topic/QairtContext.html#_CPPv4N20QairtContext_Error_t29QAIRT_CONTEXT_ERROR_MEM_ALLOCE)
 - 
enumerator InvalidArgument = [QAIRT_CONTEXT_ERROR_INVALID_ARGUMENT](https://docs.qualcomm.com/doc/80-63442-10/topic/QairtContext.html#_CPPv4N20QairtContext_Error_t36QAIRT_CONTEXT_ERROR_INVALID_ARGUMENTE)
 - 
enumerator CtxDoesNotExist = [QAIRT_CONTEXT_ERROR_CTX_DOES_NOT_EXIST](https://docs.qualcomm.com/doc/80-63442-10/topic/QairtContext.html#_CPPv4N20QairtContext_Error_t38QAIRT_CONTEXT_ERROR_CTX_DOES_NOT_EXISTE)
 - 
enumerator InvalidHandle = [QAIRT_CONTEXT_ERROR_INVALID_HANDLE](https://docs.qualcomm.com/doc/80-63442-10/topic/QairtContext.html#_CPPv4N20QairtContext_Error_t34QAIRT_CONTEXT_ERROR_INVALID_HANDLEE)
 - 
enumerator NotFinalized = [QAIRT_CONTEXT_ERROR_NOT_FINALIZED](https://docs.qualcomm.com/doc/80-63442-10/topic/QairtContext.html#_CPPv4N20QairtContext_Error_t33QAIRT_CONTEXT_ERROR_NOT_FINALIZEDE)
 - 
enumerator BinaryVersion = [QAIRT_CONTEXT_ERROR_BINARY_VERSION](https://docs.qualcomm.com/doc/80-63442-10/topic/QairtContext.html#_CPPv4N20QairtContext_Error_t34QAIRT_CONTEXT_ERROR_BINARY_VERSIONE)
 - 
enumerator CreateFromBinary = [QAIRT_CONTEXT_ERROR_CREATE_FROM_BINARY](https://docs.qualcomm.com/doc/80-63442-10/topic/QairtContext.html#_CPPv4N20QairtContext_Error_t38QAIRT_CONTEXT_ERROR_CREATE_FROM_BINARYE)
 - 
enumerator GetBinarySizeFailed = [QAIRT_CONTEXT_ERROR_GET_BINARY_SIZE_FAILED](https://docs.qualcomm.com/doc/80-63442-10/topic/QairtContext.html#_CPPv4N20QairtContext_Error_t42QAIRT_CONTEXT_ERROR_GET_BINARY_SIZE_FAILEDE)
 - 
enumerator GetBinaryFailed = [QAIRT_CONTEXT_ERROR_GET_BINARY_FAILED](https://docs.qualcomm.com/doc/80-63442-10/topic/QairtContext.html#_CPPv4N20QairtContext_Error_t37QAIRT_CONTEXT_ERROR_GET_BINARY_FAILEDE)
 - 
enumerator BinaryConfiguration = [QAIRT_CONTEXT_ERROR_BINARY_CONFIGURATION](https://docs.qualcomm.com/doc/80-63442-10/topic/QairtContext.html#_CPPv4N20QairtContext_Error_t40QAIRT_CONTEXT_ERROR_BINARY_CONFIGURATIONE)
 - 
enumerator SetProfile = [QAIRT_CONTEXT_ERROR_SET_PROFILE](https://docs.qualcomm.com/doc/80-63442-10/topic/QairtContext.html#_CPPv4N20QairtContext_Error_t31QAIRT_CONTEXT_ERROR_SET_PROFILEE)
 - 
enumerator InvalidConfig = [QAIRT_CONTEXT_ERROR_INVALID_CONFIG](https://docs.qualcomm.com/doc/80-63442-10/topic/QairtContext.html#_CPPv4N20QairtContext_Error_t34QAIRT_CONTEXT_ERROR_INVALID_CONFIGE)
 - 
enumerator BinarySuboptimal = [QAIRT_CONTEXT_ERROR_BINARY_SUBOPTIMAL](https://docs.qualcomm.com/doc/80-63442-10/topic/QairtContext.html#_CPPv4N20QairtContext_Error_t37QAIRT_CONTEXT_ERROR_BINARY_SUBOPTIMALE)
 - 
enumerator Aborted = [QAIRT_CONTEXT_ERROR_ABORTED](https://docs.qualcomm.com/doc/80-63442-10/topic/QairtContext.html#_CPPv4N20QairtContext_Error_t27QAIRT_CONTEXT_ERROR_ABORTEDE)
 - 
enumerator TimedOut = [QAIRT_CONTEXT_ERROR_TIMED_OUT](https://docs.qualcomm.com/doc/80-63442-10/topic/QairtContext.html#_CPPv4N20QairtContext_Error_t29QAIRT_CONTEXT_ERROR_TIMED_OUTE)
 - 
enumerator IncrementInvalidBuffer = [QAIRT_CONTEXT_ERROR_INCREMENT_INVALID_BUFFER](https://docs.qualcomm.com/doc/80-63442-10/topic/QairtContext.html#_CPPv4N20QairtContext_Error_t44QAIRT_CONTEXT_ERROR_INCREMENT_INVALID_BUFFERE)
 - 
enumerator Undefined = [QAIRT_CONTEXT_ERROR_UNDEFINED](https://docs.qualcomm.com/doc/80-63442-10/topic/QairtContext.html#_CPPv4N20QairtContext_Error_t29QAIRT_CONTEXT_ERROR_UNDEFINEDE)
 
- 
enumerator NoError = 
 - 
enum class ContextBinaryType : std::underlying_type_t<[QairtContext_BinaryType_t](https://docs.qualcomm.com/doc/80-63442-10/topic/QairtContext.html#_CPPv425QairtContext_BinaryType_t)>
- Storage format of a context binary. - Enumerator - Description - `Raw`- Binary stored as a raw memory buffer. - `MemHandle`- Binary referenced via a memory handle. - `Undefined`- Sentinel value; not a valid binary type. - *Values:*- 
enumerator Raw = [QAIRT_CONTEXT_BINARY_TYPE_RAW](https://docs.qualcomm.com/doc/80-63442-10/topic/QairtContext.html#_CPPv4N25QairtContext_BinaryType_t29QAIRT_CONTEXT_BINARY_TYPE_RAWE)
 - 
enumerator MemHandle = [QAIRT_CONTEXT_BINARY_TYPE_MEM_HANDLE](https://docs.qualcomm.com/doc/80-63442-10/topic/QairtContext.html#_CPPv4N25QairtContext_BinaryType_t36QAIRT_CONTEXT_BINARY_TYPE_MEM_HANDLEE)
 - 
enumerator Undefined = [QAIRT_CONTEXT_BINARY_TYPE_UNDEFINED](https://docs.qualcomm.com/doc/80-63442-10/topic/QairtContext.html#_CPPv4N25QairtContext_BinaryType_t35QAIRT_CONTEXT_BINARY_TYPE_UNDEFINEDE)
 
- 
enumerator Raw = 
 - 
enum class ContextSectionType : std::underlying_type_t<[QairtContext_SectionType_t](https://docs.qualcomm.com/doc/80-63442-10/topic/QairtContext.html#_CPPv426QairtContext_SectionType_t)>
- Portion of the context binary targeted by section operations. - Enumerator - Description - `Updatable`- Section containing all recent updates applied via tensor update APIs. - `UpdatableWeights`- Section containing recent static weight updates only. - `UpdatableQuantParams`- Section containing recent quantization parameter updates only. - `Undefined`- Sentinel value; not a valid section type. - *Values:*- 
enumerator Updatable = [QAIRT_CONTEXT_SECTION_UPDATABLE](https://docs.qualcomm.com/doc/80-63442-10/topic/QairtContext.html#_CPPv4N26QairtContext_SectionType_t31QAIRT_CONTEXT_SECTION_UPDATABLEE)
 - 
enumerator UpdatableWeights = [QAIRT_CONTEXT_SECTION_UPDATABLE_WEIGHTS](https://docs.qualcomm.com/doc/80-63442-10/topic/QairtContext.html#_CPPv4N26QairtContext_SectionType_t39QAIRT_CONTEXT_SECTION_UPDATABLE_WEIGHTSE)
 - 
enumerator UpdatableQuantParams = [QAIRT_CONTEXT_SECTION_UPDATABLE_QUANT_PARAMS](https://docs.qualcomm.com/doc/80-63442-10/topic/QairtContext.html#_CPPv4N26QairtContext_SectionType_t44QAIRT_CONTEXT_SECTION_UPDATABLE_QUANT_PARAMSE)
 - 
enumerator Undefined = [QAIRT_CONTEXT_SECTION_UNDEFINED](https://docs.qualcomm.com/doc/80-63442-10/topic/QairtContext.html#_CPPv4N26QairtContext_SectionType_t31QAIRT_CONTEXT_SECTION_UNDEFINEDE)
 
- 
enumerator Updatable = 
 - 
class Context : public [qairt](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtBackend.html#_CPPv45qairt)::ApiType<[Context](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtContext.html#_CPPv4N5qairt7ContextE),[QairtContext_V1_t](https://docs.qualcomm.com/doc/80-63442-10/topic/QairtContext.html#_CPPv417QairtContext_V1_t)>
- Public Functions - 
Context() = default
 - 
Context(const [Context](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtContext.html#_CPPv4N5qairt7Context7ContextERK7Context)&) = delete
 - 
Context([Context](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtContext.html#_CPPv4N5qairt7Context7ContextERR7Context)&&) noexcept = default
 - 
inline void setConfig(const [ContextConfiguration](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtContext.html#_CPPv4N5qairt20ContextConfigurationE)&config)
- Set or modify configuration options on this context. - Backends are not required to support reconfiguration after context creation. If the backend does not support the provided configuration, this call will fail. - See also 
 - 
template<typename T>
 inline std::enable_if_t<std::is_base_of_v<[ContextCustomConfiguration](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtContext.html#_CPPv4N5qairt26ContextCustomConfigurationE),[T](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtContext.html#_CPPv4I0EN5qairt7Context16setConfigurationENSt11enable_if_tINSt12is_base_of_vI26ContextCustomConfiguration1TEEEERK1T)>> setConfiguration(const[T](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtContext.html#_CPPv4I0EN5qairt7Context16setConfigurationENSt11enable_if_tINSt12is_base_of_vI26ContextCustomConfiguration1TEEEERK1T)&customConfigs)
- Apply a collection of backend-specific custom configuration entries to this context. 
 - 
inline uint64_t getBinarySize() const
- Get the size in bytes of the serialized binary representation of this context. - All graphs in the context must be finalized before calling this method. Call - [getBinary()](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtContext.html#classqairt_1_1Context_1a321b460b9330e51fc0db8368d8007d53)or- [getBinary(void*, uint64_t)](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtContext.html#classqairt_1_1Context_1a4777c57b3e8eff1e9f4cf355ff26e7a1)after allocating a buffer of at least this size.- See also 
 - 
inline uint64_t getBinary([ContextBinaryBuffer](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtContext.html#_CPPv4N5qairt19ContextBinaryBufferE)&buffer)
- Serialize this context into the provided binary buffer. - All graphs in the context must be finalized before calling this method. Call - [getBinarySize()](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtContext.html#classqairt_1_1Context_1a2c297ab8963a6352cd3c3944b93d54bf)first to determine the required buffer size. The buffer’s data pointer and size must be set before calling this method.- See also - Parameters
- **buffer**–- **[inout]**Pre-allocated binary buffer to receive the serialized context. The buffer’s size field must be at least- [getBinarySize()](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtContext.html#classqairt_1_1Context_1a2c297ab8963a6352cd3c3944b93d54bf)bytes.
- Throws
- invalid handle 
- unsupported feature 
- unfinalized graphs in the context 
- other serialization failure 
 
- Returns
- Number of bytes written into the buffer. 
 
 - 
inline uint64_t getBinary(void *buffer, uint64_t bufferSize)
- Wrapper which allows for serializing directly into a caller-managed raw memory buffer. 
 - 
inline void updateContextTensors(const std::vector<[Tensor](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtTensor.html#_CPPv4N5qairt6TensorE)*> &tensors)
- Update the data and quantization parameters of previously created context tensors. - Valid fields to update depend on tensor type: - UPDATEABLE_STATIC: data and quantization parameters. 
- UPDATEABLE_NATIVE, UPDATEABLE_APP_READ, UPDATEABLE_APP_WRITE, UPDATEABLE_APP_READWRITE: quantization parameters only. 
 - Updates take effect only after QairtGraph_finalize() is called for one or more of the graphs to which the context tensors are associated. - See also 
 - 
inline uint64_t getBinarySectionSize(const [Graph](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtGraph.html#_CPPv4N5qairt5GraphE)&graph,[ContextSectionType](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtContext.html#_CPPv4N5qairt18ContextSectionTypeE)section) const
- Get the size in bytes of a binary section for a specific graph. - All graphs in the context must be finalized before calling this method. Use this to determine the buffer size needed before calling - [getBinarySection()](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtContext.html#classqairt_1_1Context_1a4c4e6dfa533af9a6eb5f2de98e84156f).- See also - Parameters
- **graph**–- **[in]**- [Graph](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtGraph.html#classqairt_1_1Graph)whose binary section size is queried.
- **section**–- **[in]**Portion of the context binary to query.
 
- Throws
- invalid handle 
- unsupported feature 
- unfinalized graphs in the context 
- other retrieval failure 
 
- Returns
- Size in bytes needed to hold the requested binary section. 
 
 - 
inline uint64_t getBinarySection(const [Graph](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtGraph.html#_CPPv4N5qairt5GraphE)&graph,[ContextSectionType](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtContext.html#_CPPv4N5qairt18ContextSectionTypeE)section,[ContextBinaryBuffer](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtContext.html#_CPPv4N5qairt19ContextBinaryBufferE)&buffer, ApiTypeRef<const[Profile](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtProfile.html#_CPPv4N5qairt7ProfileE)&> profile, ApiTypeRef<const[Signal](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtSignal.html#_CPPv4N5qairt6SignalE)&> signal)
- Retrieve a section of the context binary for a specific graph. - All graphs in the context must be finalized before calling this method. Call - [getBinarySectionSize()](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtContext.html#classqairt_1_1Context_1ab38c3c184bb374eb55cbf1efec772268)first to determine the required buffer size. The signal, if non-null, is considered in-use for the duration of this call.- See also - Parameters
- **graph**–- **[in]**- [Graph](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtGraph.html#classqairt_1_1Graph)whose binary section is retrieved.
- **section**–- **[in]**Portion of the context binary to retrieve.
- **buffer**–- **[inout]**Pre-allocated binary buffer to receive the section. Must be sized to at least- [getBinarySectionSize()](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtContext.html#classqairt_1_1Context_1ab38c3c184bb374eb55cbf1efec772268)bytes.
- **profile**–- **[in]**Optional profile handle to collect metrics.
- **signal**–- **[in]**Optional signal handle for controlling the operation.
 
- Throws
- invalid handle 
- unsupported feature 
- unfinalized graphs in the context 
- other serialization failure 
 
- Returns
- Number of bytes written into the buffer. 
 
 - 
inline void applyBinarySection(const [Graph](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtGraph.html#_CPPv4N5qairt5GraphE)&graph,[ContextSectionType](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtContext.html#_CPPv4N5qairt18ContextSectionTypeE)section,[ContextBinaryBuffer](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtContext.html#_CPPv4N5qairt19ContextBinaryBufferE)&buffer, ApiTypeRef<const[Profile](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtProfile.html#_CPPv4N5qairt7ProfileE)&> profile, ApiTypeRef<const[Signal](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtSignal.html#_CPPv4N5qairt6SignalE)&> signal)
- Apply a previously retrieved binary section to this context. - See also - Parameters
- **graph**–- **[in]**- [Graph](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtGraph.html#classqairt_1_1Graph)to which the binary section applies.
- **section**–- **[in]**Portion of the context binary being applied.
- **buffer**–- **[in]**Binary buffer containing the section to apply. When persistent binary mode is enabled, this buffer must remain valid through context teardown.
- **profile**–- **[in]**Optional profile handle to collect metrics.
- **signal**–- **[in]**Optional signal handle for controlling the operation.
 
- Throws
- invalid handle 
- unsupported feature 
- memory allocation failure 
- profiling error 
 
 
 - 
inline [Graph](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtGraph.html#_CPPv4N5qairt5GraphE)createGraph(const char *graphName, ApiTypeRef<const[qairt](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtBackend.html#_CPPv45qairt)::[GraphConfiguration](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtGraph.html#_CPPv4N5qairt18GraphConfigurationE)&> graphConfiguration)
- Create a new graph within this context. - See also - Parameters
- **graphName**–- **[in]**Unique null-terminated identifier for the graph within this context.
- **graphConfiguration**–- **[in]**Configuration options for the graph. Optional.
 
- Throws
- invalid context handle 
- NULL or duplicate graph name 
- memory or resource allocation failure 
- unsupported configuration options 
 
- Returns
- The newly created - [Graph](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtGraph.html#classqairt_1_1Graph)object.
 
 - 
inline std::shared_ptr<[Graph](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtGraph.html#_CPPv4N5qairt5GraphE)> retrieveGraph(const char *graphName)
 - 
inline std::shared_ptr<[Graph](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtGraph.html#_CPPv4N5qairt5GraphE)> retrieveGraph(const std::string &graphName)
- Retrieve an existing graph from this context by name. - See also 
 - 
inline void setFreeProfile([Profile](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtProfile.html#_CPPv4N5qairt7ProfileE)&profile)
- Set the profile handle used to collect metrics during context teardown. - See also - Parameters
- **profile**–- **[in]**- [Profile](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtProfile.html#classqairt_1_1Profile)object to populate during context teardown.
 
 - 
template<typename T, typename U, typename V>
 inline ApiType(const[ApiType](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtContext.html#_CPPv4I000EN5qairt7Context7ApiTypeERK7ApiTypeI1T1U1VEN6detail17non_owning_handleI11handle_typeEE)<[T](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtContext.html#_CPPv4I000EN5qairt7Context7ApiTypeERK7ApiTypeI1T1U1VEN6detail17non_owning_handleI11handle_typeEE),[U](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtContext.html#_CPPv4I000EN5qairt7Context7ApiTypeERK7ApiTypeI1T1U1VEN6detail17non_owning_handleI11handle_typeEE),[V](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtContext.html#_CPPv4I000EN5qairt7Context7ApiTypeERK7ApiTypeI1T1U1VEN6detail17non_owning_handleI11handle_typeEE)> &parent,[detail](https://docs.qualcomm.com/doc/80-63442-10/topic/QairtTypeTraits.html#_CPPv4N5qairt6detailE)::non_owning_handle<handle_type> noh)
 - 
inline ApiType(copy_table_tag_t, const [ApiType](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtContext.html#_CPPv4N5qairt7Context7ApiTypeE16copy_table_tag_tRK7ApiType)&other)
 - 
ApiType() noexcept = default
 - 
ApiType(const [ApiType](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtContext.html#_CPPv4N5qairt7Context7ApiTypeERK7ApiType)&) = delete
 - 
ApiType([ApiType](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtContext.html#_CPPv4N5qairt7Context7ApiTypeERR7ApiType)&&) noexcept = default
 - Private Members - friend Api
 - 
[QairtProfile_Handle_t](https://docs.qualcomm.com/doc/80-63442-10/topic/QairtProfile.html#_CPPv421QairtProfile_Handle_t)m_freeProfileHandle = nullptr
- [Profile](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtProfile.html#classqairt_1_1Profile)handle used to collect metrics during context teardown.
 - Friends - 
*friend class*::qairt::ApiType
 
- 
Context() = default
 - 
class ContextAsyncExecutionQueueDepth : public [qairt](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtBackend.html#_CPPv45qairt)::ApiType<[ContextAsyncExecutionQueueDepth](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtContext.html#_CPPv4N5qairt31ContextAsyncExecutionQueueDepthE),[QairtContext_AsyncExecutionDepthV1_t](https://docs.qualcomm.com/doc/80-63442-10/topic/QairtContext.html#_CPPv436QairtContext_AsyncExecutionDepthV1_t)>
- *#include <QairtContext.hpp>*- Queue depth configuration for asynchronous context execution. - Public Functions - 
ContextAsyncExecutionQueueDepth() noexcept = default
 - 
ContextAsyncExecutionQueueDepth([ContextAsyncExecutionQueueDepth](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtContext.html#_CPPv4N5qairt31ContextAsyncExecutionQueueDepth31ContextAsyncExecutionQueueDepthERR31ContextAsyncExecutionQueueDepth)&&) noexcept = default
 - 
[ContextAsyncExecutionQueueDepth](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtContext.html#_CPPv4N5qairt31ContextAsyncExecutionQueueDepthE)&operator=([ContextAsyncExecutionQueueDepth](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtContext.html#_CPPv4N5qairt31ContextAsyncExecutionQueueDepthE)&&) noexcept = default
 - 
inline uint32_t getDepth() const
- Get the current queue depth for asynchronous execution. - See also 
 - 
inline void setDepth(uint32_t depth)
- Set the queue depth for asynchronous execution. - See also 
 - Private Functions - Friends - 
*friend class*Api
 
- 
ContextAsyncExecutionQueueDepth() noexcept = default
 - 
class ContextBinary : public [qairt](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtBackend.html#_CPPv45qairt)::ApiType<[ContextBinary](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtContext.html#_CPPv4N5qairt13ContextBinaryE),[QairtContext_BinaryV1_t](https://docs.qualcomm.com/doc/80-63442-10/topic/QairtContext.html#_CPPv423QairtContext_BinaryV1_t)>
- *#include <QairtContext.hpp>*- Descriptor pairing a binary type with its associated buffer for context serialization. - Public Functions - 
ContextBinary() noexcept = default
 - 
ContextBinary([ContextBinary](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtContext.html#_CPPv4N5qairt13ContextBinary13ContextBinaryERR13ContextBinary)&&) noexcept = default
 - 
[ContextBinary](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtContext.html#_CPPv4N5qairt13ContextBinaryE)&operator=([ContextBinary](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtContext.html#_CPPv4N5qairt13ContextBinaryE)&&) noexcept = default
 - 
inline [ContextBinaryType](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtContext.html#_CPPv4N5qairt17ContextBinaryTypeE)getType() const
- Get the storage format type of this context binary. - See also 
 - 
inline [ContextBinaryBuffer](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtContext.html#_CPPv4N5qairt19ContextBinaryBufferE)&getBuffer()
- Get the binary buffer associated with this context binary. - See also - Throws
- Returns
- Reference to the associated - [ContextBinaryBuffer](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtContext.html#classqairt_1_1ContextBinaryBuffer).
 
 - 
inline const [ContextBinaryBuffer](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtContext.html#_CPPv4N5qairt19ContextBinaryBufferE)&getBuffer() const
- Get the binary buffer associated with this context binary. - See also - Throws
- Returns
- Const reference to the associated - [ContextBinaryBuffer](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtContext.html#classqairt_1_1ContextBinaryBuffer).
 
 - 
inline void setBuffer([ContextBinaryBuffer](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtContext.html#_CPPv4N5qairt19ContextBinaryBufferE)&&buffer)
- Set the binary buffer for this context binary. - See also 
 - Private Members - friend Api
 - 
[detail](https://docs.qualcomm.com/doc/80-63442-10/topic/QairtTypeTraits.html#_CPPv4N5qairt6detailE)::crossable<[detail](https://docs.qualcomm.com/doc/80-63442-10/topic/QairtTypeTraits.html#_CPPv4N5qairt6detailE)::non_owning<[ContextBinaryBuffer](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtContext.html#_CPPv4N5qairt19ContextBinaryBufferE)>, &interface_type::getBuffer, &interface_type::setBuffer> m_buffer
- Binary buffer associated with this context binary object. 
 
- 
ContextBinary() noexcept = default
 - 
class ContextBinaryBuffer : public [qairt](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtBackend.html#_CPPv45qairt)::ApiType<[ContextBinaryBuffer](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtContext.html#_CPPv4N5qairt19ContextBinaryBufferE),[QairtContext_BinaryBufferV1_t](https://docs.qualcomm.com/doc/80-63442-10/topic/QairtContext.html#_CPPv429QairtContext_BinaryBufferV1_t)>
- *#include <QairtContext.hpp>*- [Buffer](https://docs.qualcomm.com/doc/80-63442-10/topic/QairtBuffer.html#classqairt_1_1Buffer)descriptor for a serialized context binary.- `Obtained via `Api::make<ContextBinaryBuffer>()`.`- Public Functions - 
ContextBinaryBuffer() noexcept = default
 - 
ContextBinaryBuffer([ContextBinaryBuffer](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtContext.html#_CPPv4N5qairt19ContextBinaryBuffer19ContextBinaryBufferERR19ContextBinaryBuffer)&&) noexcept = default
 - 
[ContextBinaryBuffer](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtContext.html#_CPPv4N5qairt19ContextBinaryBufferE)&operator=([ContextBinaryBuffer](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtContext.html#_CPPv4N5qairt19ContextBinaryBufferE)&&) noexcept = default
 - 
inline void *getData()
- Get the raw data pointer stored in this buffer. - See also 
 - 
inline const void *getData() const
- Get the raw data pointer stored in this buffer. - See also 
 - 
inline void setData(void *data)
- Set the raw data pointer for this buffer. - See also 
 - 
inline uint64_t getSize() const
- Get the size of this buffer in bytes. - See also 
 - 
inline void setSize(uint64_t size) const
- Set the size of this buffer in bytes. - See also 
 - Private Functions - Private Members - friend Api
 - Friends - 
*friend class*::qairt::ApiType
 
- 
ContextBinaryBuffer() noexcept = default
 - 
class ContextConfiguration : public [qairt](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtBackend.html#_CPPv45qairt)::ApiType<[ContextConfiguration](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtContext.html#_CPPv4N5qairt20ContextConfigurationE),[QairtContext_ConfigV1_t](https://docs.qualcomm.com/doc/80-63442-10/topic/QairtContext.html#_CPPv423QairtContext_ConfigV1_t)>
- *#include <QairtContext.hpp>*- Configuration object for context creation and reconfiguration. - Public Functions - 
ContextConfiguration() noexcept = default
 - 
ContextConfiguration([ContextConfiguration](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtContext.html#_CPPv4N5qairt20ContextConfiguration20ContextConfigurationERR20ContextConfiguration)&&) noexcept = default
 - 
[ContextConfiguration](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtContext.html#_CPPv4N5qairt20ContextConfigurationE)&operator=([ContextConfiguration](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtContext.html#_CPPv4N5qairt20ContextConfigurationE)&&) noexcept = default
 - 
inline void setPriority([Priority](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtGraph.html#_CPPv4N5qairt8PriorityE)p)
- Set the scheduling priority for this context configuration. - See also 
 - 
inline [Priority](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtGraph.html#_CPPv4N5qairt8PriorityE)getPriority() const
- Get the scheduling priority for this context configuration. - See also 
 - 
inline std::string &getOemKey()
- Get the Original Equipment Manufacturer (OEM) key string for this context configuration. - See also 
 - 
inline const std::string &getOemKey() const
- Get the Original Equipment Manufacturer (OEM) key string for this context configuration. - See also 
 - 
inline void setOemKey(std::string &&oemKey)
- Set the Original Equipment Manufacturer (OEM) key string for this context configuration. - See also 
 - 
inline void getOemKey(const std::string &oemKey)
 - 
inline void setAsyncExecutionQueueDepth(const [ContextAsyncExecutionQueueDepth](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtContext.html#_CPPv4N5qairt31ContextAsyncExecutionQueueDepthE)&aed)
- Set the asynchronous execution queue depth for this context configuration. 
 - 
inline [ContextAsyncExecutionQueueDepth](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtContext.html#_CPPv4N5qairt31ContextAsyncExecutionQueueDepthE)&getAsyncExecutionQueueDepth()
- Get the asynchronous execution queue depth configuration for this context. 
 - 
inline const [ContextAsyncExecutionQueueDepth](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtContext.html#_CPPv4N5qairt31ContextAsyncExecutionQueueDepthE)&getAsyncExecutionQueueDepth() const
- Get the asynchronous execution queue depth configuration for this context. 
 - 
inline [ContextConfiguration](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtContext.html#_CPPv4N5qairt20ContextConfigurationE)&setCustomConfig(const[ContextCustomConfig](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtContext.html#_CPPv4N5qairt19ContextCustomConfigE)&config)
- Set a single backend-specific custom configuration entry on this context configuration. - See also 
 - 
inline [ContextConfiguration](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtContext.html#_CPPv4N5qairt20ContextConfigurationE)&setCustomConfigs(const[ContextCustomConfiguration](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtContext.html#_CPPv4N5qairt26ContextCustomConfigurationE)&config)
- Set a collection of backend-specific custom configuration entries on this context configuration. - See also 
 - 
inline std::vector<std::string> &getEnableGraphs()
- Get the list of graph names selectively enabled for this context configuration. 
 - 
inline const std::vector<std::string> &getEnableGraphs() const
- Get the list of graph names selectively enabled for this context configuration. 
 - 
inline void setEnableGraphs(std::vector<std::string> enabledGraphs)
- Set the list of graph names selectively enabled for this context configuration. - See also 
 - 
inline void setMemoryLimitHint(uint64_t limit)
- Set a hint on the maximum memory the backend should use for this context. - This is advisory only; the backend may exceed the limit if required. 
 - 
inline uint64_t getMemoryLimitHint() const
- Get the memory limit hint for this context configuration. 
 - 
inline void setIsPersistentBinary(bool isPersistentBinary)
- Set whether the context binary should be treated as persistent. 
 - 
inline bool getIsPersistentBinary() const
- Get whether the context binary is configured as persistent. 
 - 
inline void setBinaryCompatibilityType([ContextBinaryCompatibilityType](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtContext.html#_CPPv4N5qairt30ContextBinaryCompatibilityTypeE)bct)
- Set the binary compatibility policy for loading cached context binaries. 
 - 
inline [ContextBinaryCompatibilityType](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtContext.html#_CPPv4N5qairt30ContextBinaryCompatibilityTypeE)getBinaryCompatibilityType() const
- Get the binary compatibility policy for loading cached context binaries. 
 - Private Functions - 
inline void prepareToCross() const
 - 
inline void updateAfterCross() const
 - Private Members - friend Api
 - 
[detail](https://docs.qualcomm.com/doc/80-63442-10/topic/QairtTypeTraits.html#_CPPv4N5qairt6detailE)::crossable<std::string, &interface_type::getOemKey, &interface_type::setOemKey> m_oemKey
- Original Equipment Manufacturer (OEM) key string for backend authentication. 
 - 
[detail](https://docs.qualcomm.com/doc/80-63442-10/topic/QairtTypeTraits.html#_CPPv4N5qairt6detailE)::crossable<[detail](https://docs.qualcomm.com/doc/80-63442-10/topic/QairtTypeTraits.html#_CPPv4N5qairt6detailE)::non_owning<[ContextAsyncExecutionQueueDepth](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtContext.html#_CPPv4N5qairt31ContextAsyncExecutionQueueDepthE)>, &interface_type::getAsyncQueueDepth, &interface_type::setAsyncQueueDepth> m_depth
- Maximum number of outstanding asynchronous execution requests. 
 - 
mutable std::vector<std::string> m_enabledGraphs
- Names of graphs selectively enabled for this context configuration. 
 
- 
ContextConfiguration() noexcept = default
 - 
class ContextCustomConfig : public [qairt](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtBackend.html#_CPPv45qairt)::CustomConfigType
- *#include <QairtContext.hpp>*- Abstract base class for a single backend-specific context custom configuration entry. - Public Functions - 
virtual ~ContextCustomConfig() = default
 - 
virtual [QairtContext_CustomConfigHandle_t](https://docs.qualcomm.com/doc/80-63442-10/topic/QairtContext.html#_CPPv433QairtContext_CustomConfigHandle_t)getCustomConfigHandle() const = 0
 - Protected Functions - 
ContextCustomConfig() = default
 - 
ContextCustomConfig(const [ContextCustomConfig](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtContext.html#_CPPv4N5qairt19ContextCustomConfig19ContextCustomConfigERK19ContextCustomConfig)&) = default
 - 
ContextCustomConfig([ContextCustomConfig](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtContext.html#_CPPv4N5qairt19ContextCustomConfig19ContextCustomConfigERR19ContextCustomConfig)&&) noexcept = default
 - 
[ContextCustomConfig](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtContext.html#_CPPv4N5qairt19ContextCustomConfigE)&operator=(const[ContextCustomConfig](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtContext.html#_CPPv4N5qairt19ContextCustomConfigE)&) = default
 - 
[ContextCustomConfig](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtContext.html#_CPPv4N5qairt19ContextCustomConfigE)&operator=([ContextCustomConfig](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtContext.html#_CPPv4N5qairt19ContextCustomConfigE)&&) noexcept = default
 
- 
virtual ~ContextCustomConfig() = default
 - 
class ContextCustomConfiguration
- *#include <QairtContext.hpp>*- Abstract base class for a collection of backend-specific context custom configuration entries. - Public Functions - 
virtual ~ContextCustomConfiguration() = default
 - 
virtual std::vector<[QairtContext_CustomConfigHandle_t](https://docs.qualcomm.com/doc/80-63442-10/topic/QairtContext.html#_CPPv433QairtContext_CustomConfigHandle_t)> getCustomConfigs() const = 0
 - Protected Functions - 
ContextCustomConfiguration() = default
 - 
ContextCustomConfiguration(const [ContextCustomConfiguration](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtContext.html#_CPPv4N5qairt26ContextCustomConfiguration26ContextCustomConfigurationERK26ContextCustomConfiguration)&) = default
 - 
ContextCustomConfiguration([ContextCustomConfiguration](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtContext.html#_CPPv4N5qairt26ContextCustomConfiguration26ContextCustomConfigurationERR26ContextCustomConfiguration)&&) noexcept = default
 - 
[ContextCustomConfiguration](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtContext.html#_CPPv4N5qairt26ContextCustomConfigurationE)&operator=(const[ContextCustomConfiguration](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtContext.html#_CPPv4N5qairt26ContextCustomConfigurationE)&) = default
 - 
[ContextCustomConfiguration](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtContext.html#_CPPv4N5qairt26ContextCustomConfigurationE)&operator=([ContextCustomConfiguration](https://docs.qualcomm.com/doc/80-63442-10/topic/cpp-api_QairtContext.html#_CPPv4N5qairt26ContextCustomConfigurationE)&&) noexcept = default
 
- 
virtual ~ContextCustomConfiguration() = default
 
- 
enum class ContextBinaryCompatibilityType : std::underlying_type_t<