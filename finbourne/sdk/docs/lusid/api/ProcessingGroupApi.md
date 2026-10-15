# lusid.ProcessingGroupApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_processing_group**](ProcessingGroupApi.md#create_processing_group) | **POST** /api/api/processinggroups/{scope} | [EXPERIMENTAL] CreateProcessingGroup: Create a Processing Group.
[**delete_processing_group**](ProcessingGroupApi.md#delete_processing_group) | **DELETE** /api/api/processinggroups/{scope}/{code} | [EXPERIMENTAL] DeleteProcessingGroup: Delete a Processing Group.
[**get_processing_group**](ProcessingGroupApi.md#get_processing_group) | **GET** /api/api/processinggroups/{scope}/{code} | [EXPERIMENTAL] GetProcessingGroup: Get a Processing Group.
[**get_processing_group_next_scheduled_details**](ProcessingGroupApi.md#get_processing_group_next_scheduled_details) | **GET** /api/api/processinggroups/{scope}/{code}/schedule/$next | [EXPERIMENTAL] GetProcessingGroupNextScheduledDetails: Get the next scheduled date of a Processing Group.
[**get_resolved_processing_group_schedule**](ProcessingGroupApi.md#get_resolved_processing_group_schedule) | **GET** /api/api/processinggroups/{scope}/{code}/schedule/$dates | [EXPERIMENTAL] GetResolvedProcessingGroupSchedule: Get the resolved schedule of a Processing Group.
[**list_processing_groups**](ProcessingGroupApi.md#list_processing_groups) | **GET** /api/api/processinggroups | [EXPERIMENTAL] ListProcessingGroups: List Processing Groups.
[**patch_processing_group**](ProcessingGroupApi.md#patch_processing_group) | **PATCH** /api/api/processinggroups/{scope}/{code} | [EXPERIMENTAL] PatchProcessingGroup: Patch a Processing Group.


### Example

```python
from finbourne.sdk.exceptions import ApiException
from finbourne.sdk.extensions.configuration_options import ConfigurationOptions
from finbourne.sdk.services.lusid.models import *

from finbourne.sdk.extensions import (
  SyncApiClientFactory
)

from finbourne.sdk.services.lusid.api.processing_group_api import ProcessingGroupApi

# opts = ConfigurationOptions()
# opts.total_timeout_ms = 30_000

# uncomment the below to use an api client factory with overrides
# api_client_factory = SyncApiClientFactory(opts=opts)

api_client_factory = SyncApiClientFactory()
api_instance = api_client_factory.build(ProcessingGroupApi)
```

---

# **create_processing_group**
> ProcessingGroup createProcessingGroup = create_processing_group(scope, processing_group_request)

[EXPERIMENTAL] CreateProcessingGroup: Create a Processing Group.

Create the given Processing Group.

### Example

```python
api_instance = api_client_factory.build(ProcessingGroupApi)
scope = 'scope_example' # str
processing_group_request = ProcessingGroupRequest()
api_response = api_instance.create_processing_group(scope, processing_group_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Processing Group. | [required] 
 **processing_group_request** | [**ProcessingGroupRequest**](../model/ProcessingGroupRequest.md)| The definition of the Processing Group. | [required] 

### Return type

[**ProcessingGroup**](../model/ProcessingGroup.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The newly created Processing Group. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **delete_processing_group**
> DeletedEntityResponse deleteProcessingGroup = delete_processing_group(scope, code)

[EXPERIMENTAL] DeleteProcessingGroup: Delete a Processing Group.

Delete the given Processing Group.

### Example

```python
api_instance = api_client_factory.build(ProcessingGroupApi)
scope = 'scope_example' # str
code = 'code_example' # str
api_response = api_instance.delete_processing_group(scope, code)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Processing Group to be deleted. | [required] 
 **code** | **str**| The code of the Processing Group to be deleted. Together with the scope this uniquely identifies the Processing Group. | [required] 

### Return type

[**DeletedEntityResponse**](../model/DeletedEntityResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The datetime that the Processing Group was deleted |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_processing_group**
> ProcessingGroup getProcessingGroup = get_processing_group(scope, code, effective_at=effective_at, as_at=as_at)

[EXPERIMENTAL] GetProcessingGroup: Get a Processing Group.

Retrieve the definition of a particular Processing Group, including the resolved (executed) contents  of its referenced reference list.

### Example

```python
api_instance = api_client_factory.build(ProcessingGroupApi)
scope = 'scope_example' # str
code = 'code_example' # str
effective_at = 'effective_at_example' # str (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
api_response = api_instance.get_processing_group(scope, code, effective_at=effective_at, as_at=as_at)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Processing Group. | [required] 
 **code** | **str**| The code of the Processing Group. Together with the scope this uniquely identifies the Processing Group. | [required] 
 **effective_at** | **str**| The effective datetime or cut label at which to retrieve the Processing Group. Defaults to the current LUSID system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the Processing Group. Defaults to returning the latest version if not specified. | [optional] 

### Return type

[**ProcessingGroup**](../model/ProcessingGroup.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested Processing Group definition. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_processing_group_next_scheduled_details**
> ProcessingGroupNextScheduledDetails getProcessingGroupNextScheduledDetails = get_processing_group_next_scheduled_details(scope, code, effective_at, as_at=as_at)

[EXPERIMENTAL] GetProcessingGroupNextScheduledDetails: Get the next scheduled date of a Processing Group.

Return the first execution date strictly after the given date, bounded by the schedule's end,  together with the reference list resolved at that date.  Returns 404 if the schedule has no further dates or the referenced reference list no longer exists,  and fails rather than returning a date without a list if the list cannot be resolved.

### Example

```python
api_instance = api_client_factory.build(ProcessingGroupApi)
scope = 'scope_example' # str
code = 'code_example' # str
effective_at = 'effective_at_example' # str
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
api_response = api_instance.get_processing_group_next_scheduled_details(scope, code, effective_at, as_at=as_at)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Processing Group. | [required] 
 **code** | **str**| The code of the Processing Group. | [required] 
 **effective_at** | **str**| The date after which to find the next scheduled date. | [required] 
 **as_at** | **datetime**| The asAt datetime at which to read the Processing Group and its holiday calendars. | [optional] 

### Return type

[**ProcessingGroupNextScheduledDetails**](../model/ProcessingGroupNextScheduledDetails.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The next scheduled date and the resolved reference list. |  -  |
**404** | The schedule has no date after the given date, or the referenced reference list does not exist. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_resolved_processing_group_schedule**
> List[datetime] getResolvedProcessingGroupSchedule = get_resolved_processing_group_schedule(scope, code, from_effective_at, to_effective_at, as_at=as_at)

[EXPERIMENTAL] GetResolvedProcessingGroupSchedule: Get the resolved schedule of a Processing Group.

Resolve the Processing Group's schedule into the concrete set of execution dates that fall within the  given range, applying its tenor, roll convention, business-day convention and holiday calendars.

### Example

```python
api_instance = api_client_factory.build(ProcessingGroupApi)
scope = 'scope_example' # str
code = 'code_example' # str
from_effective_at = 'from_effective_at_example' # str
to_effective_at = 'to_effective_at_example' # str
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
api_response = api_instance.get_resolved_processing_group_schedule(scope, code, from_effective_at, to_effective_at, as_at=as_at)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Processing Group. | [required] 
 **code** | **str**| The code of the Processing Group. | [required] 
 **from_effective_at** | **str**| The inclusive start of the date range over which to resolve the schedule. | [required] 
 **to_effective_at** | **str**| The inclusive end of the date range over which to resolve the schedule. | [required] 
 **as_at** | **datetime**| The asAt datetime at which to read the Processing Group and its holiday calendars. | [optional] 

### Return type

**List[datetime]**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The resolved schedule dates within the range. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **list_processing_groups**
> PagedResourceListOfProcessingGroup listProcessingGroups = list_processing_groups(effective_at=effective_at, as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by)

[EXPERIMENTAL] ListProcessingGroups: List Processing Groups.

List all the Processing Groups matching particular criteria.

### Example

```python
api_instance = api_client_factory.build(ProcessingGroupApi)
effective_at = 'effective_at_example' # str (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
page = 'page_example' # str (optional)
limit = 56 # int (optional)
filter = 'filter_example' # str (optional)
sort_by = ['sort_by_example'] # List[str] (optional)
api_response = api_instance.list_processing_groups(effective_at=effective_at, as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **effective_at** | **str**| The effective datetime or cut label at which to list the Processing Groups. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to list the Processing Groups. | [optional] 
 **page** | **str**| The pagination token to use to continue listing Processing Groups. | [optional] 
 **limit** | **int**| When paginating, limit the results to this number. Defaults to 100 if not specified. | [optional] 
 **filter** | **str**| Expression to filter the results. | [optional] 
 **sort_by** | [**List[str]**](../model/str.md)| A list of field names or properties to sort by, each suffixed by \&quot; ASC\&quot; or \&quot; DESC\&quot;. | [optional] 

### Return type

[**PagedResourceListOfProcessingGroup**](../model/PagedResourceListOfProcessingGroup.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested Processing Groups. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **patch_processing_group**
> ProcessingGroup patchProcessingGroup = patch_processing_group(scope, code, operation)

[EXPERIMENTAL] PatchProcessingGroup: Patch a Processing Group.

Create or update certain fields (display name, description, schedule) for a particular Processing Group.  The behaviour is defined by the JSON Patch specification.    Currently supported fields are: DisplayName, Description, Schedule, WorkflowId, ListExceptionFilter.

### Example

```python
api_instance = api_client_factory.build(ProcessingGroupApi)
scope = 'scope_example' # str
code = 'code_example' # str
operation = [{"value":"My Renamed Processing Group","path":"/displayName","op":"add"}] # List[Operation]
api_response = api_instance.patch_processing_group(scope, code, operation)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Processing Group. | [required] 
 **code** | **str**| The code of the Processing Group. Together with the scope this uniquely identifies the Processing Group. | [required] 
 **operation** | [**List[Operation]**](../model/Operation.md)| The json patch document. For more information see: https://datatracker.ietf.org/doc/html/rfc6902. | [required] 

### Return type

[**ProcessingGroup**](../model/ProcessingGroup.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The newly patched Processing Group |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

