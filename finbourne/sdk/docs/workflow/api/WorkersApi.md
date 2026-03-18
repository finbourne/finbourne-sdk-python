# workflow.WorkersApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_worker**](WorkersApi.md#create_worker) | **POST** /workflow/api/workers | CreateWorker: Create a new Worker
[**delete_worker**](WorkersApi.md#delete_worker) | **DELETE** /workflow/api/workers/{scope}/{code} | DeleteWorker: Delete a Worker
[**get_worker**](WorkersApi.md#get_worker) | **GET** /workflow/api/workers/{scope}/{code} | GetWorker: Get a Worker
[**get_worker_result**](WorkersApi.md#get_worker_result) | **GET** /workflow/api/workers/{runId}/$result | GetWorkerResult: Get the status of a specific run of a worker with any relevant results
[**list_workers**](WorkersApi.md#list_workers) | **GET** /workflow/api/workers | ListWorkers: List Workers
[**run_worker**](WorkersApi.md#run_worker) | **POST** /workflow/api/workers/{scope}/{code}/$run | RunWorker: Run a Worker
[**update_worker**](WorkersApi.md#update_worker) | **PUT** /workflow/api/workers/{scope}/{code} | UpdateWorker: Update a Worker


### Example

```python
from finbourne.sdk.exceptions import ApiException
from finbourne.sdk.extensions.configuration_options import ConfigurationOptions
from finbourne.sdk.services.workflow.models import *

from finbourne.sdk.extensions import (
  SyncApiClientFactory
)

from finbourne.sdk.services.workflow.api.workers_api import WorkersApi

# opts = ConfigurationOptions()
# opts.total_timeout_ms = 30_000

# uncomment the below to use an api client factory with overrides
# api_client_factory = SyncApiClientFactory(opts=opts)

api_client_factory = SyncApiClientFactory()
api_instance = api_client_factory.build(WorkersApi)
```

---

# **create_worker**
> Worker createWorker = create_worker(create_worker_request)

CreateWorker: Create a new Worker

If the Worker already exists a failure will be returned

### Example

```python
api_instance = api_client_factory.build(WorkersApi)
create_worker_request = CreateWorkerRequest()
api_response = api_instance.create_worker(create_worker_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_worker_request** | [**CreateWorkerRequest**](CreateWorkerRequest.md)| Worker to be created | [required] 

### Return type

[**Worker**](Worker.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **delete_worker**
> DeletedEntityResponse deleteWorker = delete_worker(scope, code)

DeleteWorker: Delete a Worker

If the Worker does not exist a failure will be returned

### Example

```python
api_instance = api_client_factory.build(WorkersApi)
scope = 'scope_example' # str
code = 'code_example' # str
api_response = api_instance.delete_worker(scope, code)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| Scope of the worker to be deleted | [required] 
 **code** | **str**| Code of the worker to be deleted | [required] 

### Return type

[**DeletedEntityResponse**](DeletedEntityResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | The details of the input related failure |  -  |
**404** | Worker not found. |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_worker**
> Worker getWorker = get_worker(scope, code, as_at=as_at)

GetWorker: Get a Worker

Will return a NotFound failure if the Worker does not exist

### Example

```python
api_instance = api_client_factory.build(WorkersApi)
scope = 'scope_example' # str
code = 'code_example' # str
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
api_response = api_instance.get_worker(scope, code, as_at=as_at)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| Scope of the worker | [required] 
 **code** | **str**| Code of the worker | [required] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the Worker. Defaults to returning the latest version of the Worker if not specified. | [optional] 

### Return type

[**Worker**](Worker.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_worker_result**
> GetWorkerResultResponse getWorkerResult = get_worker_result(run_id)

GetWorkerResult: Get the status of a specific run of a worker with any relevant results

### Example

```python
api_instance = api_client_factory.build(WorkersApi)
run_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID
api_response = api_instance.get_worker_result(run_id)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_id** | **UUID**| The ID returned when calling Run Worker | [required] 

### Return type

[**GetWorkerResultResponse**](GetWorkerResultResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **list_workers**
> PagedResourceListOfWorker listWorkers = list_workers(as_at=as_at, filter=filter, sort_by=sort_by, limit=limit, page=page)

ListWorkers: List Workers

### Example

```python
api_instance = api_client_factory.build(WorkersApi)
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
filter = 'filter_example' # str (optional)
sort_by = ['sort_by_example'] # List[str] (optional)
limit = 10 # int (optional)
page = 'page_example' # str (optional)
api_response = api_instance.list_workers(as_at=as_at, filter=filter, sort_by=sort_by, limit=limit, page=page)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **as_at** | **datetime**| The asAt datetime at which to list the Workers. Defaults to return the latest version of each Worker if not specified. | [optional] 
 **filter** | **str**| Expression to filter the result set. Read more about filtering results from LUSID here: https://support.lusid.com/filtering-results-from-lusid. | [optional] 
 **sort_by** | [**List[str]**](str.md)| A list of field names or properties to sort by, each optionally suffixed by \&quot; ASC\&quot; or \&quot; DESC\&quot; | [optional] 
 **limit** | **int**| When paginating, limit the number of returned results to this many. | [optional] [default to 10]
 **page** | **str**| The pagination token to use to continue listing workers from a previous call to list workers. This value is returned from the previous call. If a pagination token is provided the sortBy, filter, effectiveAt, and asAt fields must not have changed since the original request. | [optional] 

### Return type

[**PagedResourceListOfWorker**](PagedResourceListOfWorker.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **run_worker**
> RunWorkerResponse runWorker = run_worker(scope, code, run_worker_request, as_at=as_at)

RunWorker: Run a Worker

### Example

```python
api_instance = api_client_factory.build(WorkersApi)
scope = 'scope_example' # str
code = 'code_example' # str
run_worker_request = RunWorkerRequest()
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
api_response = api_instance.run_worker(scope, code, run_worker_request, as_at=as_at)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| Scope of the worker | [required] 
 **code** | **str**| Code of the worker | [required] 
 **run_worker_request** | [**RunWorkerRequest**](RunWorkerRequest.md)|  | [required] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the Worker. Defaults to returning the latest version of the Worker if not specified. | [optional] 

### Return type

[**RunWorkerResponse**](RunWorkerResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **update_worker**
> Worker updateWorker = update_worker(scope, code, update_worker_request)

UpdateWorker: Update a Worker

If the Worker does not exist a failure will be returned

### Example

```python
api_instance = api_client_factory.build(WorkersApi)
scope = 'scope_example' # str
code = 'code_example' # str
update_worker_request = UpdateWorkerRequest()
api_response = api_instance.update_worker(scope, code, update_worker_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| Scope of the worker to be updated | [required] 
 **code** | **str**| Code of the worker to be updated | [required] 
 **update_worker_request** | [**UpdateWorkerRequest**](UpdateWorkerRequest.md)| State of the updated worker | [required] 

### Return type

[**Worker**](Worker.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | The details of the input related failure |  -  |
**404** | Worker not found. |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

