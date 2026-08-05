# lusid.RecsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_rec_result_set_approval_decision**](RecsApi.md#add_rec_result_set_approval_decision) | **POST** /api/api/recs/resultsets/{entityUniqueId}/$decide | [EXPERIMENTAL] AddRecResultSetApprovalDecision: AddRecResultSetApprovalDecision
[**get_rec_instance**](RecsApi.md#get_rec_instance) | **GET** /api/api/recs/instances/{instanceIdType}/{instanceIdValue} | [EXPERIMENTAL] GetRecInstance: GetRecInstance
[**get_rec_result_set**](RecsApi.md#get_rec_result_set) | **GET** /api/api/recs/resultsets/{entityUniqueId} | [EXPERIMENTAL] GetRecResultSet: GetRecResultSet
[**instantiate_rec**](RecsApi.md#instantiate_rec) | **POST** /api/api/recs/instances | [EXPERIMENTAL] InstantiateRec: InstantiateRec
[**list_rec_instances**](RecsApi.md#list_rec_instances) | **GET** /api/api/recs/instances | [EXPERIMENTAL] ListRecInstances: ListRecInstances
[**list_rec_result_sets**](RecsApi.md#list_rec_result_sets) | **GET** /api/api/recs/resultsets | [EXPERIMENTAL] ListRecResultSets: ListRecResultSets
[**submit_rec_result_set_review**](RecsApi.md#submit_rec_result_set_review) | **POST** /api/api/recs/resultsets/{entityUniqueId}/$submit | [EXPERIMENTAL] SubmitRecResultSetReview: Submit a rec result set review for approval, or resubmit after addressing requested revisions.
[**transition_rec_instance**](RecsApi.md#transition_rec_instance) | **POST** /api/api/recs/instances/{instanceIdType}/{instanceIdValue}/$transition | [EXPERIMENTAL] TransitionRecInstance: TransitionRecInstance


### Example

```python
from finbourne.sdk.exceptions import ApiException
from finbourne.sdk.extensions.configuration_options import ConfigurationOptions
from finbourne.sdk.services.lusid.models import *

from finbourne.sdk.extensions import (
  SyncApiClientFactory
)

from finbourne.sdk.services.lusid.api.recs_api import RecsApi

# opts = ConfigurationOptions()
# opts.total_timeout_ms = 30_000

# uncomment the below to use an api client factory with overrides
# api_client_factory = SyncApiClientFactory(opts=opts)

api_client_factory = SyncApiClientFactory()
api_instance = api_client_factory.build(RecsApi)
```

---

# **add_rec_result_set_approval_decision**
> RecResultSet addRecResultSetApprovalDecision = add_rec_result_set_approval_decision(entity_unique_id, rec_result_set_approval_decision_request)

[EXPERIMENTAL] AddRecResultSetApprovalDecision: AddRecResultSetApprovalDecision

Add an approver decision (approve or request revisions) to a rec result set.

### Example

```python
api_instance = api_client_factory.build(RecsApi)
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

# **get_rec_instance**
> RecInstance getRecInstance = get_rec_instance(instance_id_type, instance_id_value, as_at=as_at)

[EXPERIMENTAL] GetRecInstance: GetRecInstance

Retrieve a single rec instance by its identifier.

### Example

```python
api_instance = api_client_factory.build(RecsApi)
instance_id_type = 'instance_id_type_example' # str
instance_id_value = 'instance_id_value_example' # str
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
api_response = api_instance.get_rec_instance(instance_id_type, instance_id_value, as_at=as_at)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id_type** | **str**| How the instance was created: \&quot;WorkflowServiceTaskId\&quot; or \&quot;Manual\&quot;. Available values: WorkflowServiceTaskId, Manual. | [required] 
 **instance_id_value** | **str**| The instance identifier value (a GUID). | [required] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the instance. Defaults to latest if not specified. | [optional] 

### Return type

[**RecInstance**](RecInstance.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested rec instance. |  -  |
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
api_instance = api_client_factory.build(RecsApi)
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

# **instantiate_rec**
> RecInstance instantiateRec = instantiate_rec(instantiate_rec_request)

[EXPERIMENTAL] InstantiateRec: InstantiateRec

Instantiate a new rec instance from a rec definition and start its first run. The run              executes asynchronously; the response returns once the run has started, with the instance Running.

### Example

```python
api_instance = api_client_factory.build(RecsApi)
instantiate_rec_request = InstantiateRecRequest()
api_response = api_instance.instantiate_rec(instantiate_rec_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instantiate_rec_request** | [**InstantiateRecRequest**](InstantiateRecRequest.md)| The instantiation request. | [required] 

### Return type

[**RecInstance**](RecInstance.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The instantiated rec instance, in a Running state. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **list_rec_instances**
> PagedResourceListOfRecInstance listRecInstances = list_rec_instances(as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by)

[EXPERIMENTAL] ListRecInstances: ListRecInstances

List rec instances.

### Example

```python
api_instance = api_client_factory.build(RecsApi)
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
page = 'page_example' # str (optional)
limit = 56 # int (optional)
filter = 'filter_example' # str (optional)
sort_by = ['sort_by_example'] # List[str] (optional)
api_response = api_instance.list_rec_instances(as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **as_at** | **datetime**| The asAt datetime at which to list instances. Defaults to latest if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing instances from a previous call. If a pagination token is provided the filter and asAt fields must not have changed since the original request. | [optional] 
 **limit** | **int**| When paginating, limit the number of returned results to this many. Defaults to 100 if not specified. | [optional] 
 **filter** | **str**| Expression to filter the result set. Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. | [optional] 
 **sort_by** | [**List[str]**](str.md)| A list of field names suffixed by \&quot; ASC\&quot; or \&quot; DESC\&quot;. | [optional] 

### Return type

[**PagedResourceListOfRecInstance**](PagedResourceListOfRecInstance.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The rec instances. |  -  |
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
api_instance = api_client_factory.build(RecsApi)
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
api_instance = api_client_factory.build(RecsApi)
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

---

# **transition_rec_instance**
> RecInstance transitionRecInstance = transition_rec_instance(instance_id_type, instance_id_value, transition_rec_instance_request)

[EXPERIMENTAL] TransitionRecInstance: TransitionRecInstance

Apply a lifecycle transition (re-run, lock or unlock) to a rec instance.

### Example

```python
api_instance = api_client_factory.build(RecsApi)
instance_id_type = 'instance_id_type_example' # str
instance_id_value = 'instance_id_value_example' # str
transition_rec_instance_request = TransitionRecInstanceRequest()
api_response = api_instance.transition_rec_instance(instance_id_type, instance_id_value, transition_rec_instance_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id_type** | **str**| How the instance was created: \&quot;WorkflowServiceTaskId\&quot; or \&quot;Manual\&quot;. Available values: WorkflowServiceTaskId, Manual. | [required] 
 **instance_id_value** | **str**| The instance identifier value (a GUID). | [required] 
 **transition_rec_instance_request** | [**TransitionRecInstanceRequest**](TransitionRecInstanceRequest.md)| The transition request. | [required] 

### Return type

[**RecInstance**](RecInstance.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The rec instance in its post-transition state. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

