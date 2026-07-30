# lusid.RecResultSetsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_rec_result_set_approval_decision**](RecResultSetsApi.md#add_rec_result_set_approval_decision) | **POST** /api/api/recs/resultsets/{entityUniqueId}/$decide | [EXPERIMENTAL] AddRecResultSetApprovalDecision: AddRecResultSetApprovalDecision
[**get_rec_result_set**](RecResultSetsApi.md#get_rec_result_set) | **GET** /api/api/recs/resultsets/{entityUniqueId} | [EXPERIMENTAL] GetRecResultSet: GetRecResultSet
[**list_rec_result_sets**](RecResultSetsApi.md#list_rec_result_sets) | **GET** /api/api/recs/resultsets | [EXPERIMENTAL] ListRecResultSets: ListRecResultSets
[**submit_rec_result_set_review**](RecResultSetsApi.md#submit_rec_result_set_review) | **POST** /api/api/recs/resultsets/{entityUniqueId}/$submit | [EXPERIMENTAL] SubmitRecResultSetReview: Submit a rec result set review for approval, or resubmit after addressing requested revisions.


### Example

```python
from finbourne.sdk.exceptions import ApiException
from finbourne.sdk.extensions.configuration_options import ConfigurationOptions
from finbourne.sdk.services.lusid.models import *

from finbourne.sdk.extensions import (
  SyncApiClientFactory
)

from finbourne.sdk.services.lusid.api.rec_result_sets_api import RecResultSetsApi

# opts = ConfigurationOptions()
# opts.total_timeout_ms = 30_000

# uncomment the below to use an api client factory with overrides
# api_client_factory = SyncApiClientFactory(opts=opts)

api_client_factory = SyncApiClientFactory()
api_instance = api_client_factory.build(RecResultSetsApi)
```

---

# **add_rec_result_set_approval_decision**
> RecResultSet addRecResultSetApprovalDecision = add_rec_result_set_approval_decision(entity_unique_id, rec_result_set_approval_decision_request)

[EXPERIMENTAL] AddRecResultSetApprovalDecision: AddRecResultSetApprovalDecision

Add an approver decision (approve or request revisions) to a rec result set.

### Example

```python
api_instance = api_client_factory.build(RecResultSetsApi)
entity_unique_id = 'entity_unique_id_example' # str
rec_result_set_approval_decision_request = RecResultSetApprovalDecisionRequest()
api_response = api_instance.add_rec_result_set_approval_decision(entity_unique_id, rec_result_set_approval_decision_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_unique_id** | **str**| The entity unique id of the rec result set (its version.entityUniqueId). | [required] 
 **rec_result_set_approval_decision_request** | [**RecResultSetApprovalDecisionRequest**](RecResultSetApprovalDecisionRequest.md)| The approval decision request. | [required] 

### Return type

[**RecResultSet**](RecResultSet.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated rec result set. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_rec_result_set**
> RecResultSet getRecResultSet = get_rec_result_set(entity_unique_id, as_at=as_at, include_previous_runs=include_previous_runs)

[EXPERIMENTAL] GetRecResultSet: GetRecResultSet

Retrieve a single rec result set by its entity unique id.

### Example

```python
api_instance = api_client_factory.build(RecResultSetsApi)
entity_unique_id = 'entity_unique_id_example' # str
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
include_previous_runs = False # bool (optional)
api_response = api_instance.get_rec_result_set(entity_unique_id, as_at=as_at, include_previous_runs=include_previous_runs)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_unique_id** | **str**| The entity unique id of the rec result set (its version.entityUniqueId). | [required] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the result set. Defaults to latest if not specified. | [optional] 
 **include_previous_runs** | **bool**| When true, the previousRuns array is populated with prior run snapshots. Defaults to false. | [optional] [default to False]

### Return type

[**RecResultSet**](RecResultSet.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested rec result set. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **list_rec_result_sets**
> PagedResourceListOfRecResultSet listRecResultSets = list_rec_result_sets(as_at=as_at, include_previous_runs=include_previous_runs, page=page, limit=limit, filter=filter, sort_by=sort_by)

[EXPERIMENTAL] ListRecResultSets: ListRecResultSets

List rec result sets.

### Example

```python
api_instance = api_client_factory.build(RecResultSetsApi)
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
include_previous_runs = False # bool (optional)
page = 'page_example' # str (optional)
limit = 56 # int (optional)
filter = 'filter_example' # str (optional)
sort_by = ['sort_by_example'] # List[str] (optional)
api_response = api_instance.list_rec_result_sets(as_at=as_at, include_previous_runs=include_previous_runs, page=page, limit=limit, filter=filter, sort_by=sort_by)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **as_at** | **datetime**| The asAt datetime at which to list result sets. Defaults to latest if not specified. | [optional] 
 **include_previous_runs** | **bool**| When true, each item&#39;s previousRuns array is populated with prior run snapshots. Defaults to false. | [optional] [default to False]
 **page** | **str**| The pagination token to use to continue listing result sets from a previous call. If a pagination token is provided the filter and asAt fields must not have changed since the original request. | [optional] 
 **limit** | **int**| When paginating, limit the number of returned results to this many. Defaults to 100 if not specified. | [optional] 
 **filter** | **str**| Expression to filter the result set. Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. | [optional] 
 **sort_by** | [**List[str]**](str.md)| A list of field names suffixed by \&quot; ASC\&quot; or \&quot; DESC\&quot;. | [optional] 

### Return type

[**PagedResourceListOfRecResultSet**](PagedResourceListOfRecResultSet.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The rec result sets. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **submit_rec_result_set_review**
> RecResultSet submitRecResultSetReview = submit_rec_result_set_review(entity_unique_id, submit_rec_result_set_review_request)

[EXPERIMENTAL] SubmitRecResultSetReview: Submit a rec result set review for approval, or resubmit after addressing requested revisions.

Submit a rec result set review for approval, or resubmit after addressing requested revisions.

### Example

```python
api_instance = api_client_factory.build(RecResultSetsApi)
entity_unique_id = 'entity_unique_id_example' # str
submit_rec_result_set_review_request = SubmitRecResultSetReviewRequest()
api_response = api_instance.submit_rec_result_set_review(entity_unique_id, submit_rec_result_set_review_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_unique_id** | **str**| The entity unique id of the rec result set (its version.entityUniqueId). | [required] 
 **submit_rec_result_set_review_request** | [**SubmitRecResultSetReviewRequest**](SubmitRecResultSetReviewRequest.md)| The submission request. | [required] 

### Return type

[**RecResultSet**](RecResultSet.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated rec result set. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

