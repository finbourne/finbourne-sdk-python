# lusid.AllocationMapsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_allocation_map_exception**](AllocationMapsApi.md#add_allocation_map_exception) | **POST** /api/api/allocationmaps/{scope}/{code}/exceptions | [EXPERIMENTAL] AddAllocationMapException: Add an exception to an Allocation Map.
[**create_allocation_map**](AllocationMapsApi.md#create_allocation_map) | **POST** /api/api/allocationmaps/{scope} | [EXPERIMENTAL] CreateAllocationMap: Create an Allocation Map.
[**delete_allocation_map**](AllocationMapsApi.md#delete_allocation_map) | **DELETE** /api/api/allocationmaps/{scope}/{code} | [EXPERIMENTAL] DeleteAllocationMap: Delete an Allocation Map.
[**get_allocation_map**](AllocationMapsApi.md#get_allocation_map) | **GET** /api/api/allocationmaps/{scope}/{code} | [EXPERIMENTAL] GetAllocationMap: Get an Allocation Map.
[**list_allocation_maps**](AllocationMapsApi.md#list_allocation_maps) | **GET** /api/api/allocationmaps | [EXPERIMENTAL] ListAllocationMaps: List Allocation Maps.
[**remove_allocation_map_exception**](AllocationMapsApi.md#remove_allocation_map_exception) | **DELETE** /api/api/allocationmaps/{scope}/{code}/exceptions/{investorRecordId} | [EXPERIMENTAL] RemoveAllocationMapException: Remove an exception from an Allocation Map.
[**resolve_allocation_map**](AllocationMapsApi.md#resolve_allocation_map) | **POST** /api/api/allocationmaps/{scope}/{code}/resolve | [EXPERIMENTAL] ResolveAllocationMap: Resolve an Allocation Map.
[**upsert_allocation_map**](AllocationMapsApi.md#upsert_allocation_map) | **PUT** /api/api/allocationmaps/{scope}/{code} | [EXPERIMENTAL] UpsertAllocationMap: Upsert an Allocation Map.


### Example

```python
from finbourne.sdk.exceptions import ApiException
from finbourne.sdk.extensions.configuration_options import ConfigurationOptions
from finbourne.sdk.services.lusid.models import *

from finbourne.sdk.extensions import (
  SyncApiClientFactory
)

from finbourne.sdk.services.lusid.api.allocation_maps_api import AllocationMapsApi

# opts = ConfigurationOptions()
# opts.total_timeout_ms = 30_000

# uncomment the below to use an api client factory with overrides
# api_client_factory = SyncApiClientFactory(opts=opts)

api_client_factory = SyncApiClientFactory()
api_instance = api_client_factory.build(AllocationMapsApi)
```

---

# **add_allocation_map_exception**
> AllocationMap addAllocationMapException = add_allocation_map_exception(scope, code, allocation_map_exception, effective_at=effective_at)

[EXPERIMENTAL] AddAllocationMapException: Add an exception to an Allocation Map.

Add a per-investor exception (an exclusion or a fixed percentage) to the map's participants, from an  effective datetime. The result is a new bitemporal version of the map. An investor record may carry at most  one exception; to change it, remove the existing one first or upsert the whole map.

### Example

```python
api_instance = api_client_factory.build(AllocationMapsApi)
scope = 'scope_example' # str
code = 'code_example' # str
allocation_map_exception = AllocationMapException()
effective_at = 'effective_at_example' # str (optional)
api_response = api_instance.add_allocation_map_exception(scope, code, allocation_map_exception, effective_at=effective_at)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Allocation Map. | [required] 
 **code** | **str**| The code of the Allocation Map. Together with the scope this uniquely identifies the Allocation Map. | [required] 
 **allocation_map_exception** | [**AllocationMapException**](../model/AllocationMapException.md)| The exception to add. | [required] 
 **effective_at** | **str**| The effective datetime or cut label from which the exception applies. Defaults to the current LUSID system datetime if not specified. | [optional] 

### Return type

[**AllocationMap**](../model/AllocationMap.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The Allocation Map with the exception added. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **create_allocation_map**
> AllocationMap createAllocationMap = create_allocation_map(scope, allocation_map_request)

[EXPERIMENTAL] CreateAllocationMap: Create an Allocation Map.

Create a new Allocation Map. The scope is provided in the route and the code in the request body. The map  names the structure member it hangs off, who participates, and the basis used to share each kind of event.

### Example

```python
api_instance = api_client_factory.build(AllocationMapsApi)
scope = 'scope_example' # str
allocation_map_request = AllocationMapRequest()
api_response = api_instance.create_allocation_map(scope, allocation_map_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Allocation Map. | [required] 
 **allocation_map_request** | [**AllocationMapRequest**](../model/AllocationMapRequest.md)| The definition of the Allocation Map. | [required] 

### Return type

[**AllocationMap**](../model/AllocationMap.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The newly created Allocation Map. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **delete_allocation_map**
> DeletedEntityResponse deleteAllocationMap = delete_allocation_map(scope, code, effective_at=effective_at)

[EXPERIMENTAL] DeleteAllocationMap: Delete an Allocation Map.

Delete an Allocation Map from an effective datetime. The Allocation Map is no longer readable from that  effective datetime onwards.

### Example

```python
api_instance = api_client_factory.build(AllocationMapsApi)
scope = 'scope_example' # str
code = 'code_example' # str
effective_at = 'effective_at_example' # str (optional)
api_response = api_instance.delete_allocation_map(scope, code, effective_at=effective_at)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Allocation Map. | [required] 
 **code** | **str**| The code of the Allocation Map. Together with the scope this uniquely identifies the Allocation Map. | [required] 
 **effective_at** | **str**| The effective datetime or cut label from which the Allocation Map is deleted. Defaults to the current LUSID system datetime if not specified. | [optional] 

### Return type

[**DeletedEntityResponse**](../model/DeletedEntityResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The datetime that the Allocation Map was deleted. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_allocation_map**
> AllocationMap getAllocationMap = get_allocation_map(scope, code, effective_at=effective_at, as_at=as_at)

[EXPERIMENTAL] GetAllocationMap: Get an Allocation Map.

Retrieve the definition of a particular Allocation Map at an effective and asAt datetime, including its  participants, exceptions and the basis declared for each event type.

### Example

```python
api_instance = api_client_factory.build(AllocationMapsApi)
scope = 'scope_example' # str
code = 'code_example' # str
effective_at = 'effective_at_example' # str (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
api_response = api_instance.get_allocation_map(scope, code, effective_at=effective_at, as_at=as_at)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Allocation Map. | [required] 
 **code** | **str**| The code of the Allocation Map. Together with the scope this uniquely identifies the Allocation Map. | [required] 
 **effective_at** | **str**| The effective datetime or cut label at which to retrieve the Allocation Map. Defaults to the current LUSID system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the Allocation Map. Defaults to returning the latest version if not specified. | [optional] 

### Return type

[**AllocationMap**](../model/AllocationMap.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested Allocation Map. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **list_allocation_maps**
> PagedResourceListOfAllocationMap listAllocationMaps = list_allocation_maps(effective_at=effective_at, as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by)

[EXPERIMENTAL] ListAllocationMaps: List Allocation Maps.

List all the Allocation Maps matching a particular criteria.

### Example

```python
api_instance = api_client_factory.build(AllocationMapsApi)
effective_at = 'effective_at_example' # str (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
page = 'page_example' # str (optional)
limit = 56 # int (optional)
filter = 'filter_example' # str (optional)
sort_by = ['sort_by_example'] # List[str] (optional)
api_response = api_instance.list_allocation_maps(effective_at=effective_at, as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **effective_at** | **str**| The effective datetime or cut label at which to list the Allocation Maps. Defaults to the current LUSID system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to list the Allocation Maps. Defaults to returning the latest version of each Allocation Map if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing Allocation Maps; this value is returned from the previous call.              If a pagination token is provided, the filter, effectiveAt and asAt fields must not have changed since the original request. | [optional] 
 **limit** | **int**| When paginating, limit the results to this number. Defaults to 100 if not specified. | [optional] 
 **filter** | **str**| Expression to filter the results. For example, to filter on the Allocation Map code, specify \&quot;id.Code eq &#39;AllocationMap1&#39;\&quot;.              For more information about filtering LUSID results, see https://support.lusid.com/knowledgebase/article/KA-01914. | [optional] 
 **sort_by** | [**List[str]**](../model/str.md)| A list of field names or properties to sort by, each suffixed by \&quot; ASC\&quot; or \&quot; DESC\&quot;. | [optional] 

### Return type

[**PagedResourceListOfAllocationMap**](../model/PagedResourceListOfAllocationMap.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested Allocation Maps. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **remove_allocation_map_exception**
> AllocationMap removeAllocationMapException = remove_allocation_map_exception(scope, code, investor_record_id, effective_at=effective_at)

[EXPERIMENTAL] RemoveAllocationMapException: Remove an exception from an Allocation Map.

Remove the exception held against an investor record, from an effective datetime. The result is a new  bitemporal version of the map in which that investor is treated like every other participant.

### Example

```python
api_instance = api_client_factory.build(AllocationMapsApi)
scope = 'scope_example' # str
code = 'code_example' # str
investor_record_id = 'investor_record_id_example' # str
effective_at = 'effective_at_example' # str (optional)
api_response = api_instance.remove_allocation_map_exception(scope, code, investor_record_id, effective_at=effective_at)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Allocation Map. | [required] 
 **code** | **str**| The code of the Allocation Map. Together with the scope this uniquely identifies the Allocation Map. | [required] 
 **investor_record_id** | **str**| The investor record whose exception is removed. | [required] 
 **effective_at** | **str**| The effective datetime or cut label from which the exception no longer applies. Defaults to the current LUSID system datetime if not specified. | [optional] 

### Return type

[**AllocationMap**](../model/AllocationMap.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The Allocation Map with the exception removed. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **resolve_allocation_map**
> AllocationMapResolution resolveAllocationMap = resolve_allocation_map(scope, code, allocation_map_resolve_request, effective_at=effective_at, as_at=as_at)

[EXPERIMENTAL] ResolveAllocationMap: Resolve an Allocation Map.

Dry-run the map against an event: share the supplied amount across the participants in force at the  effective datetime, applying fixed-percentage exceptions off the top and the declared basis to the remainder.  Nothing is booked. Basis values (for example committed capital per investor) are supplied in the request  until the investor register can provide them.

### Example

```python
api_instance = api_client_factory.build(AllocationMapsApi)
scope = 'scope_example' # str
code = 'code_example' # str
allocation_map_resolve_request = AllocationMapResolveRequest()
effective_at = 'effective_at_example' # str (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
api_response = api_instance.resolve_allocation_map(scope, code, allocation_map_resolve_request, effective_at=effective_at, as_at=as_at)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Allocation Map. | [required] 
 **code** | **str**| The code of the Allocation Map. Together with the scope this uniquely identifies the Allocation Map. | [required] 
 **allocation_map_resolve_request** | [**AllocationMapResolveRequest**](../model/AllocationMapResolveRequest.md)| The event to resolve and the basis values to use. | [required] 
 **effective_at** | **str**| The effective datetime or cut label at which to resolve the map. Defaults to the current LUSID system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to read the map. Defaults to the latest version if not specified. | [optional] 

### Return type

[**AllocationMapResolution**](../model/AllocationMapResolution.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The resolved allocation. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **upsert_allocation_map**
> AllocationMap upsertAllocationMap = upsert_allocation_map(scope, code, allocation_map_request)

[EXPERIMENTAL] UpsertAllocationMap: Upsert an Allocation Map.

Update or insert an Allocation Map. If the Allocation Map does not exist it is created, otherwise it is  updated. The code in the request body must match the code in the route.

### Example

```python
api_instance = api_client_factory.build(AllocationMapsApi)
scope = 'scope_example' # str
code = 'code_example' # str
allocation_map_request = AllocationMapRequest()
api_response = api_instance.upsert_allocation_map(scope, code, allocation_map_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Allocation Map. | [required] 
 **code** | **str**| The code of the Allocation Map. Together with the scope this uniquely identifies the Allocation Map. | [required] 
 **allocation_map_request** | [**AllocationMapRequest**](../model/AllocationMapRequest.md)| The definition of the Allocation Map. | [required] 

### Return type

[**AllocationMap**](../model/AllocationMap.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The upserted Allocation Map. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

