# lusid.StagedModificationsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_decision**](StagedModificationsApi.md#add_decision) | **POST** /api/api/stagedmodifications/{id}/decision | AddDecision: AddDecision
[**get_staged_modification**](StagedModificationsApi.md#get_staged_modification) | **GET** /api/api/stagedmodifications/{id} | GetStagedModification: GetStagedModification
[**list_requested_changes**](StagedModificationsApi.md#list_requested_changes) | **GET** /api/api/stagedmodifications/{id}/requestedChanges | ListRequestedChanges: ListRequestedChanges
[**list_staged_modifications**](StagedModificationsApi.md#list_staged_modifications) | **GET** /api/api/stagedmodifications | ListStagedModifications: ListStagedModifications


### Example

```python
from finbourne.sdk.exceptions import ApiException
from finbourne.sdk.extensions.configuration_options import ConfigurationOptions
from finbourne.sdk.services.lusid.models import *

from finbourne.sdk.extensions import (
  SyncApiClientFactory
)

from finbourne.sdk.services.lusid.api.staged_modifications_api import StagedModificationsApi

# opts = ConfigurationOptions()
# opts.total_timeout_ms = 30_000

# uncomment the below to use an api client factory with overrides
# api_client_factory = SyncApiClientFactory(opts=opts)

api_client_factory = SyncApiClientFactory()
api_instance = api_client_factory.build(StagedModificationsApi)
```

---

# **add_decision**
> StagedModification addDecision = add_decision(id, staged_modification_decision_request)

AddDecision: AddDecision

Add decision to staged modification, Approve or Reject.

### Example

```python
api_instance = api_client_factory.build(StagedModificationsApi)
id = 'id_example' # str
staged_modification_decision_request = StagedModificationDecisionRequest()
api_response = api_instance.add_decision(id, staged_modification_decision_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique Id for a staged modification.. | [required] 
 **staged_modification_decision_request** | [**StagedModificationDecisionRequest**](StagedModificationDecisionRequest.md)| The decision on the requested staged modification, \&quot;Approve\&quot; or \&quot;Reject\&quot;. | [required] 

### Return type

[**StagedModification**](StagedModification.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The staged modification. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_staged_modification**
> StagedModification getStagedModification = get_staged_modification(id, as_at=as_at)

GetStagedModification: GetStagedModification

Retrieve the details of a staged modification.

### Example

```python
api_instance = api_client_factory.build(StagedModificationsApi)
id = 'id_example' # str
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
api_response = api_instance.get_staged_modification(id, as_at=as_at)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier for a staged modification. | [required] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the staged modification. Defaults to latest if not specified. | [optional] 

### Return type

[**StagedModification**](StagedModification.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested staged modification. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **list_requested_changes**
> PagedResourceListOfStagedModificationsRequestedChangeInterval listRequestedChanges = list_requested_changes(id, as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by)

ListRequestedChanges: ListRequestedChanges

List the requested changes for a staged modification.

### Example

```python
api_instance = api_client_factory.build(StagedModificationsApi)
id = 'id_example' # str
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
page = 'page_example' # str (optional)
limit = 56 # int (optional)
filter = 'filter_example' # str (optional)
sort_by = ['sort_by_example'] # List[str] (optional)
api_response = api_instance.list_requested_changes(id, as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique Id for a staged modification.. | [required] 
 **as_at** | **datetime**| The asAt datetime at which to list changes. Defaults to return the latest version              of each staged change if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing requested staged modification changes from a previous call to list requested              staged modifications. This value is returned from the previous call. If a pagination token is provided the filter, effectiveAt              and asAt fields must not have changed since the original request. | [optional] 
 **limit** | **int**| When paginating, limit the number of returned results to this many. Defaults to 100 if not specified. | [optional] 
 **filter** | **str**| Expression to filter the result set.              Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. | [optional] 
 **sort_by** | [**List[str]**](str.md)| A list of field names suffixed by \&quot; ASC\&quot; or \&quot; DESC\&quot; | [optional] 

### Return type

[**PagedResourceListOfStagedModificationsRequestedChangeInterval**](PagedResourceListOfStagedModificationsRequestedChangeInterval.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Requested changes in staged modification. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **list_staged_modifications**
> PagedResourceListOfStagedModification listStagedModifications = list_staged_modifications(as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by)

ListStagedModifications: ListStagedModifications

List summaries of the staged modifications.

### Example

```python
api_instance = api_client_factory.build(StagedModificationsApi)
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
page = 'page_example' # str (optional)
limit = 56 # int (optional)
filter = 'filter_example' # str (optional)
sort_by = ['sort_by_example'] # List[str] (optional)
api_response = api_instance.list_staged_modifications(as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **as_at** | **datetime**| The asAt datetime at which to list staged modifications. Defaults to return the latest version              of each staged modification if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing staged modifications from a previous call to list staged modifications. This              value is returned from the previous call. If a pagination token is provided the filter, effectiveAt              and asAt fields must not have changed since the original request. | [optional] 
 **limit** | **int**| When paginating, limit the number of returned results to this many. Defaults to 100 if not specified. | [optional] 
 **filter** | **str**| Expression to filter the result set.               Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. | [optional] 
 **sort_by** | [**List[str]**](str.md)| A list of field names suffixed by \&quot; ASC\&quot; or \&quot; DESC\&quot; | [optional] 

### Return type

[**PagedResourceListOfStagedModification**](PagedResourceListOfStagedModification.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List summary of staged modifications. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

