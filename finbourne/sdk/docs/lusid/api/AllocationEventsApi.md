# lusid.AllocationEventsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**book_allocation_event**](AllocationEventsApi.md#book_allocation_event) | **POST** /api/api/allocationevents/{scope}/{code}/book | [EXPERIMENTAL] BookAllocationEvent: Book an Allocation Event.
[**create_allocation_event**](AllocationEventsApi.md#create_allocation_event) | **POST** /api/api/allocationevents/{scope} | [EXPERIMENTAL] CreateAllocationEvent: Create an Allocation Event.
[**delete_allocation_event**](AllocationEventsApi.md#delete_allocation_event) | **DELETE** /api/api/allocationevents/{scope}/{code} | [EXPERIMENTAL] DeleteAllocationEvent: Delete an Allocation Event.
[**get_allocation_event**](AllocationEventsApi.md#get_allocation_event) | **GET** /api/api/allocationevents/{scope}/{code} | [EXPERIMENTAL] GetAllocationEvent: Get an Allocation Event.
[**list_allocation_events**](AllocationEventsApi.md#list_allocation_events) | **GET** /api/api/allocationevents | [EXPERIMENTAL] ListAllocationEvents: List Allocation Events.
[**reallocate_allocation_event**](AllocationEventsApi.md#reallocate_allocation_event) | **POST** /api/api/allocationevents/{scope}/{code}/reallocate | [EXPERIMENTAL] ReallocateAllocationEvent: Reallocate an Allocation Event.
[**upsert_allocation_event**](AllocationEventsApi.md#upsert_allocation_event) | **PUT** /api/api/allocationevents/{scope}/{code} | [EXPERIMENTAL] UpsertAllocationEvent: Upsert an Allocation Event.


### Example

```python
from finbourne.sdk.exceptions import ApiException
from finbourne.sdk.extensions.configuration_options import ConfigurationOptions
from finbourne.sdk.services.lusid.models import *

from finbourne.sdk.extensions import (
  SyncApiClientFactory
)

from finbourne.sdk.services.lusid.api.allocation_events_api import AllocationEventsApi

# opts = ConfigurationOptions()
# opts.total_timeout_ms = 30_000

# uncomment the below to use an api client factory with overrides
# api_client_factory = SyncApiClientFactory(opts=opts)

api_client_factory = SyncApiClientFactory()
api_instance = api_client_factory.build(AllocationEventsApi)
```

---

# **book_allocation_event**
> AllocationEvent bookAllocationEvent = book_allocation_event(scope, code, allocation_event_book_request, effective_at=effective_at)

[EXPERIMENTAL] BookAllocationEvent: Book an Allocation Event.

Freeze a computed Allocation Event under a booking reference, from an effective datetime. Once booked the  event can no longer be replaced or reallocated. Booking again under the same reference returns the event  unchanged; booking under a different reference is refused.

### Example

```python
api_instance = api_client_factory.build(AllocationEventsApi)
scope = 'scope_example' # str
code = 'code_example' # str
allocation_event_book_request = AllocationEventBookRequest()
effective_at = 'effective_at_example' # str (optional)
api_response = api_instance.book_allocation_event(scope, code, allocation_event_book_request, effective_at=effective_at)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Allocation Event. | [required] 
 **code** | **str**| The code of the Allocation Event. Together with the scope this uniquely identifies the Allocation Event. | [required] 
 **allocation_event_book_request** | [**AllocationEventBookRequest**](../model/AllocationEventBookRequest.md)| The booking reference to freeze the event under. | [required] 
 **effective_at** | **str**| The effective datetime or cut label from which the booking applies. Defaults to the current LUSID system datetime if not specified. | [optional] 

### Return type

[**AllocationEvent**](../model/AllocationEvent.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The booked Allocation Event. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **create_allocation_event**
> AllocationEvent createAllocationEvent = create_allocation_event(scope, allocation_event_request)

[EXPERIMENTAL] CreateAllocationEvent: Create an Allocation Event.

Raise a new Allocation Event. The scope is provided in the route and the code in the request body. The event  names the Allocation Map it is shared by, the kind of event, the amount and the date. Its per-investor shares  are computed on creation from the map as it stood on the event date, so the response comes back Computed.

### Example

```python
api_instance = api_client_factory.build(AllocationEventsApi)
scope = 'scope_example' # str
allocation_event_request = AllocationEventRequest()
api_response = api_instance.create_allocation_event(scope, allocation_event_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Allocation Event. | [required] 
 **allocation_event_request** | [**AllocationEventRequest**](../model/AllocationEventRequest.md)| The definition of the Allocation Event. | [required] 

### Return type

[**AllocationEvent**](../model/AllocationEvent.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The newly created Allocation Event. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **delete_allocation_event**
> DeletedEntityResponse deleteAllocationEvent = delete_allocation_event(scope, code, effective_at=effective_at)

[EXPERIMENTAL] DeleteAllocationEvent: Delete an Allocation Event.

Delete an Allocation Event from an effective datetime. The Allocation Event remains retrievable at earlier  effective datetimes.

### Example

```python
api_instance = api_client_factory.build(AllocationEventsApi)
scope = 'scope_example' # str
code = 'code_example' # str
effective_at = 'effective_at_example' # str (optional)
api_response = api_instance.delete_allocation_event(scope, code, effective_at=effective_at)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Allocation Event. | [required] 
 **code** | **str**| The code of the Allocation Event. Together with the scope this uniquely identifies the Allocation Event. | [required] 
 **effective_at** | **str**| The effective datetime or cut label from which to delete the Allocation Event. Defaults to the current LUSID system datetime if not specified. | [optional] 

### Return type

[**DeletedEntityResponse**](../model/DeletedEntityResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The datetime that the Allocation Event was deleted. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_allocation_event**
> AllocationEvent getAllocationEvent = get_allocation_event(scope, code, effective_at=effective_at, as_at=as_at)

[EXPERIMENTAL] GetAllocationEvent: Get an Allocation Event.

Retrieve a particular Allocation Event at an effective and asAt datetime, including its computed  per-investor shares and, once booked, its booking reference.

### Example

```python
api_instance = api_client_factory.build(AllocationEventsApi)
scope = 'scope_example' # str
code = 'code_example' # str
effective_at = 'effective_at_example' # str (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
api_response = api_instance.get_allocation_event(scope, code, effective_at=effective_at, as_at=as_at)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Allocation Event. | [required] 
 **code** | **str**| The code of the Allocation Event. Together with the scope this uniquely identifies the Allocation Event. | [required] 
 **effective_at** | **str**| The effective datetime or cut label at which to retrieve the Allocation Event. Defaults to the current LUSID system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the Allocation Event. Defaults to returning the latest version if not specified. | [optional] 

### Return type

[**AllocationEvent**](../model/AllocationEvent.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested Allocation Event. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **list_allocation_events**
> PagedResourceListOfAllocationEvent listAllocationEvents = list_allocation_events(effective_at=effective_at, as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by)

[EXPERIMENTAL] ListAllocationEvents: List Allocation Events.

List all the Allocation Events matching a particular criteria.

### Example

```python
api_instance = api_client_factory.build(AllocationEventsApi)
effective_at = 'effective_at_example' # str (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
page = 'page_example' # str (optional)
limit = 56 # int (optional)
filter = 'filter_example' # str (optional)
sort_by = ['sort_by_example'] # List[str] (optional)
api_response = api_instance.list_allocation_events(effective_at=effective_at, as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **effective_at** | **str**| The effective datetime or cut label at which to list the Allocation Events. Defaults to the current LUSID system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to list the Allocation Events. Defaults to returning the latest version of each Allocation Event if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing Allocation Events; this value is returned from the previous call.              If a pagination token is provided, the filter, effectiveAt and asAt fields must not have changed since the original request. | [optional] 
 **limit** | **int**| When paginating, limit the results to this number. Defaults to 100 if not specified. | [optional] 
 **filter** | **str**| Expression to filter the results. For example, to filter on the Allocation Event status, specify \&quot;status eq &#39;Booked&#39;\&quot;.              For more information about filtering LUSID results, see https://support.lusid.com/knowledgebase/article/KA-01914. | [optional] 
 **sort_by** | [**List[str]**](../model/str.md)| A list of field names or properties to sort by, each suffixed by \&quot; ASC\&quot; or \&quot; DESC\&quot;. | [optional] 

### Return type

[**PagedResourceListOfAllocationEvent**](../model/PagedResourceListOfAllocationEvent.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested Allocation Events. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **reallocate_allocation_event**
> AllocationEvent reallocateAllocationEvent = reallocate_allocation_event(scope, code, allocation_event_reallocate_request, effective_at=effective_at)

[EXPERIMENTAL] ReallocateAllocationEvent: Reallocate an Allocation Event.

Recompute the per-investor shares of an unbooked Allocation Event against its map, from an effective  datetime, recording the reason. Any basis values supplied replace those used before. A booked Allocation  Event cannot be reallocated.

### Example

```python
api_instance = api_client_factory.build(AllocationEventsApi)
scope = 'scope_example' # str
code = 'code_example' # str
allocation_event_reallocate_request = AllocationEventReallocateRequest()
effective_at = 'effective_at_example' # str (optional)
api_response = api_instance.reallocate_allocation_event(scope, code, allocation_event_reallocate_request, effective_at=effective_at)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Allocation Event. | [required] 
 **code** | **str**| The code of the Allocation Event. Together with the scope this uniquely identifies the Allocation Event. | [required] 
 **allocation_event_reallocate_request** | [**AllocationEventReallocateRequest**](../model/AllocationEventReallocateRequest.md)| The reason for the reallocation and any basis values to use. | [required] 
 **effective_at** | **str**| The effective datetime or cut label from which the reallocation applies. Defaults to the current LUSID system datetime if not specified. | [optional] 

### Return type

[**AllocationEvent**](../model/AllocationEvent.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The reallocated Allocation Event. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **upsert_allocation_event**
> AllocationEvent upsertAllocationEvent = upsert_allocation_event(scope, code, allocation_event_request)

[EXPERIMENTAL] UpsertAllocationEvent: Upsert an Allocation Event.

Update or insert an Allocation Event. If the Allocation Event does not exist it is created, otherwise it is  replaced and its shares recomputed. The code in the request body must match the code in the route. A booked  Allocation Event is frozen and cannot be replaced.

### Example

```python
api_instance = api_client_factory.build(AllocationEventsApi)
scope = 'scope_example' # str
code = 'code_example' # str
allocation_event_request = AllocationEventRequest()
api_response = api_instance.upsert_allocation_event(scope, code, allocation_event_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Allocation Event. | [required] 
 **code** | **str**| The code of the Allocation Event. Together with the scope this uniquely identifies the Allocation Event. | [required] 
 **allocation_event_request** | [**AllocationEventRequest**](../model/AllocationEventRequest.md)| The definition of the Allocation Event. | [required] 

### Return type

[**AllocationEvent**](../model/AllocationEvent.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The upserted Allocation Event. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

