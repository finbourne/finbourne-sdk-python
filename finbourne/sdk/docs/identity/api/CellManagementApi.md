# identity.CellManagementApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**accept_cell_attachment**](CellManagementApi.md#accept_cell_attachment) | **POST** /identity/api/cellmanagement/acceptattachment | [EARLY ACCESS] AcceptCellAttachment: Accept (or retry) a cell attachment
[**detach_parent_cell**](CellManagementApi.md#detach_parent_cell) | **PUT** /identity/api/cellmanagement/detach | [EARLY ACCESS] DetachParentCell: Detach this cell from its parent
[**get_cell_parent_status**](CellManagementApi.md#get_cell_parent_status) | **GET** /identity/api/cellmanagement/parentcell | [EARLY ACCESS] GetCellParentStatus: Get cell parent status
[**refuse_cell_attachment**](CellManagementApi.md#refuse_cell_attachment) | **POST** /identity/api/cellmanagement/refuseattachment | [EARLY ACCESS] RefuseCellAttachment: Refuse a Proposed cell attachment
[**remove_primary_domain**](CellManagementApi.md#remove_primary_domain) | **DELETE** /identity/api/cellmanagement/primarydomain | [EARLY ACCESS] RemovePrimaryDomain: Remove primary domain
[**rotate_attaching_key**](CellManagementApi.md#rotate_attaching_key) | **PUT** /identity/api/cellmanagement/attachingkey/rotate | [EARLY ACCESS] RotateAttachingKey: Rotate the stored Attaching Key on an Attached cell
[**rotate_domain_keys**](CellManagementApi.md#rotate_domain_keys) | **POST** /identity/api/cellmanagement/rotatedomainkeys | [EARLY ACCESS] RotateDomainKeys: Force a sweep-rotation of every parent-cell service-user PAT on this cell
[**set_attaching_key**](CellManagementApi.md#set_attaching_key) | **PUT** /identity/api/cellmanagement/attachingkey | [EARLY ACCESS] SetAttachingKey: Store the Attaching Key pasted from the parent admin portal
[**set_parent_cell**](CellManagementApi.md#set_parent_cell) | **PUT** /identity/api/cellmanagement/parentcell | [EARLY ACCESS] SetParentCell: Set parent cell
[**set_primary_domain**](CellManagementApi.md#set_primary_domain) | **PUT** /identity/api/cellmanagement/primarydomain | [EARLY ACCESS] SetPrimaryDomain: Set primary domain


### Example

```python
from finbourne.sdk.exceptions import ApiException
from finbourne.sdk.extensions.configuration_options import ConfigurationOptions
from finbourne.sdk.services.identity.models import *

from finbourne.sdk.extensions import (
  SyncApiClientFactory
)

from finbourne.sdk.services.identity.api.cell_management_api import CellManagementApi

# opts = ConfigurationOptions()
# opts.total_timeout_ms = 30_000

# uncomment the below to use an api client factory with overrides
# api_client_factory = SyncApiClientFactory(opts=opts)

api_client_factory = SyncApiClientFactory()
api_instance = api_client_factory.build(CellManagementApi)
```

---

# **accept_cell_attachment**
> CellParentStatusResponse acceptCellAttachment = accept_cell_attachment()

[EARLY ACCESS] AcceptCellAttachment: Accept (or retry) a cell attachment

Confirms a Proposed attachment, or retries one that previously failed: transitions the cell to Attaching and runs the shared registration service to provision the parent-cell service user, mint a PAT, and push it to the parent admin domain. Accepted starting states are `Proposed` (the normal first confirm — anti-circumvention is enforced by requiring a prior `SetAttachingKey`) and `Failed` (recovery from a previous failed attempt). The registration service is idempotent and resumes from the persisted `RegistrationStep` checkpoint, so this is safe to call any number of times after a failure. To abandon a failed attempt instead of retrying, call `Detach`. Only the designated primary domain may call this. Requires JWT authentication.

### Example

```python
api_instance = api_client_factory.build(CellManagementApi)
api_response = api_instance.accept_cell_attachment()
pprint(api_response)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CellParentStatusResponse**](CellParentStatusResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated cell parent status |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **detach_parent_cell**
> CellParentStatusResponse detachParentCell = detach_parent_cell(detach_parent_cell_request)

[EARLY ACCESS] DetachParentCell: Detach this cell from its parent

Double-invoke pattern. First call with `Confirm=false` transitions the cell into Detaching; second call with `Confirm=true` executes: deactivates the parent-cell service user, deletes the Attaching Key from ParameterStore, and best-effort notifies the parent admin domain. Accepts `Attached`, `Attaching`, `Failed`, and `Detaching` as valid starting states (call `AcceptAttachment` instead if you'd rather retry a Failed cell than abandon it). Only the designated primary domain may call this. Requires JWT authentication.

### Example

```python
api_instance = api_client_factory.build(CellManagementApi)
detach_parent_cell_request = DetachParentCellRequest()
api_response = api_instance.detach_parent_cell(detach_parent_cell_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **detach_parent_cell_request** | [**DetachParentCellRequest**](DetachParentCellRequest.md)|  | [required] 

### Return type

[**CellParentStatusResponse**](CellParentStatusResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated cell parent status |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_cell_parent_status**
> CellParentStatusResponse getCellParentStatus = get_cell_parent_status()

[EARLY ACCESS] GetCellParentStatus: Get cell parent status

Returns the current cell parent relationship status including primary domain, admin domain name, and attachment status.

### Example

```python
api_instance = api_client_factory.build(CellManagementApi)
api_response = api_instance.get_cell_parent_status()
pprint(api_response)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CellParentStatusResponse**](CellParentStatusResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The cell parent status |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **refuse_cell_attachment**
> CellParentStatusResponse refuseCellAttachment = refuse_cell_attachment()

[EARLY ACCESS] RefuseCellAttachment: Refuse a Proposed cell attachment

Rejects a Proposed attachment, deletes the Attaching Key from ParameterStore, and returns the cell to Standalone. Only the designated primary domain may call this. Requires JWT authentication.

### Example

```python
api_instance = api_client_factory.build(CellManagementApi)
api_response = api_instance.refuse_cell_attachment()
pprint(api_response)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CellParentStatusResponse**](CellParentStatusResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated cell parent status |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **remove_primary_domain**
> CellParentStatusResponse removePrimaryDomain = remove_primary_domain()

[EARLY ACCESS] RemovePrimaryDomain: Remove primary domain

Removes the primary domain designation for this cell. Only the current primary domain or FINBOURNE staff can perform this. Requires JWT authentication (PAT tokens are rejected).

### Example

```python
api_instance = api_client_factory.build(CellManagementApi)
api_response = api_instance.remove_primary_domain()
pprint(api_response)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CellParentStatusResponse**](CellParentStatusResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated cell parent status |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **rotate_attaching_key**
> CellParentStatusResponse rotateAttachingKey = rotate_attaching_key(rotate_attaching_key_request)

[EARLY ACCESS] RotateAttachingKey: Rotate the stored Attaching Key on an Attached cell

Upserts a new Attaching Key PAT into the cell's ParameterStore / Azure Key Vault at the canonical per-cell path (`Lydia/CellManagement/{primaryDomain}/AttachingKey`) and re-stamps the path on the `cell_status` row. Does not require a prior key to exist in the secret store, and does not change the cell's attachment status or the recorded parent identity. Intended for two callers: the parent admin portal pushing a freshly-rotated PAT, and manual operator use (e.g. to migrate an existing cell onto the per-primary-domain path layout). Requires the cell to be currently `Attached` to a parent admin domain. Only the designated primary domain may call this. Requires JWT authentication (PAT tokens are rejected).

### Example

```python
api_instance = api_client_factory.build(CellManagementApi)
rotate_attaching_key_request = RotateAttachingKeyRequest()
api_response = api_instance.rotate_attaching_key(rotate_attaching_key_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rotate_attaching_key_request** | [**RotateAttachingKeyRequest**](RotateAttachingKeyRequest.md)|  | [required] 

### Return type

[**CellParentStatusResponse**](CellParentStatusResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated cell parent status |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **rotate_domain_keys**
> CellParentStatusResponse rotateDomainKeys = rotate_domain_keys()

[EARLY ACCESS] RotateDomainKeys: Force a sweep-rotation of every parent-cell service-user PAT on this cell

Stamps the per-cell rotation cutoff to \"now\". On its next tick (and any subsequent tick until every provisioned PAT has been refreshed past the cutoff), the steady-state AdminCellSync job force-rotates any provisioned parent-cell PAT whose `CreatedDate` is strictly before the cutoff, regardless of the normal expiry-based window. Used to rapidly invalidate suspected-compromised PATs and to recover a cell whose recent rotations failed to be pushed to the parent admin portal. The cutoff is sticky: re-calling moves it forward, and new PATs naturally have `CreatedDate > cutoff` so subsequent ticks pass the check without further intervention. Only the designated primary domain may call this. Requires JWT authentication (PAT tokens are rejected). Cell must currently be `Attached`.

### Example

```python
api_instance = api_client_factory.build(CellManagementApi)
api_response = api_instance.rotate_domain_keys()
pprint(api_response)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CellParentStatusResponse**](CellParentStatusResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The cell parent status after stamping the cutoff |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **set_attaching_key**
> CellParentStatusResponse setAttachingKey = set_attaching_key(set_attaching_key_request)

[EARLY ACCESS] SetAttachingKey: Store the Attaching Key pasted from the parent admin portal

Persists the Attaching Key PAT to the cell's ParameterStore / Azure Key Vault and records a Proposed attachment against the provided parent admin domain. Only the designated primary domain may call this. Requires JWT authentication (PAT tokens are rejected).

### Example

```python
api_instance = api_client_factory.build(CellManagementApi)
set_attaching_key_request = SetAttachingKeyRequest()
api_response = api_instance.set_attaching_key(set_attaching_key_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **set_attaching_key_request** | [**SetAttachingKeyRequest**](SetAttachingKeyRequest.md)|  | [required] 

### Return type

[**CellParentStatusResponse**](CellParentStatusResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated cell parent status |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **set_parent_cell**
> CellParentStatusResponse setParentCell = set_parent_cell(set_parent_cell_request)

[EARLY ACCESS] SetParentCell: Set parent cell

Sets the parent cell for this cell. Uses a double-invoke pattern: first call (confirm=false) sets status to Proposed, second call (confirm=true) transitions to Attaching. Only the designated primary domain can call this. Requires JWT authentication (PAT tokens are rejected).

### Example

```python
api_instance = api_client_factory.build(CellManagementApi)
set_parent_cell_request = SetParentCellRequest()
api_response = api_instance.set_parent_cell(set_parent_cell_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **set_parent_cell_request** | [**SetParentCellRequest**](SetParentCellRequest.md)|  | [required] 

### Return type

[**CellParentStatusResponse**](CellParentStatusResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated cell parent status |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **set_primary_domain**
> CellParentStatusResponse setPrimaryDomain = set_primary_domain()

[EARLY ACCESS] SetPrimaryDomain: Set primary domain

Designates the calling domain as the primary domain for this cell. Requires JWT authentication (PAT tokens are rejected).

### Example

```python
api_instance = api_client_factory.build(CellManagementApi)
api_response = api_instance.set_primary_domain()
pprint(api_response)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CellParentStatusResponse**](CellParentStatusResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated cell parent status |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

