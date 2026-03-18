# workflow.TasksApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**batch_update_tasks**](TasksApi.md#batch_update_tasks) | **PATCH** /workflow/api/tasks/$update | [EXPERIMENTAL] BatchUpdateTasks: Batch update tasks
[**create_task**](TasksApi.md#create_task) | **POST** /workflow/api/tasks | CreateTask: Create a new Task
[**delete_task**](TasksApi.md#delete_task) | **DELETE** /workflow/api/tasks/{id} | DeleteTask: Delete a Task
[**delete_tasks**](TasksApi.md#delete_tasks) | **POST** /workflow/api/tasks/$delete | DeleteTasks: Batch Delete Tasks
[**get_task**](TasksApi.md#get_task) | **GET** /workflow/api/tasks/{id} | GetTask: Get a Task
[**get_task_history**](TasksApi.md#get_task_history) | **GET** /workflow/api/tasks/{id}/history | GetTaskHistory: Get the history of a Task
[**list_tasks**](TasksApi.md#list_tasks) | **GET** /workflow/api/tasks | ListTasks: List Tasks
[**update_task**](TasksApi.md#update_task) | **POST** /workflow/api/tasks/{id} | UpdateTask: Update a Task


### Example

```python
from finbourne.sdk.exceptions import ApiException
from finbourne.sdk.extensions.configuration_options import ConfigurationOptions
from finbourne.sdk.services.workflow.models import *

from finbourne.sdk.extensions import (
  SyncApiClientFactory
)

from finbourne.sdk.services.workflow.api.tasks_api import TasksApi

# opts = ConfigurationOptions()
# opts.total_timeout_ms = 30_000

# uncomment the below to use an api client factory with overrides
# api_client_factory = SyncApiClientFactory(opts=opts)

api_client_factory = SyncApiClientFactory()
api_instance = api_client_factory.build(TasksApi)
```

---

# **batch_update_tasks**
> BatchUpdateTasksResponse batchUpdateTasks = batch_update_tasks(batch_update_tasks_request=batch_update_tasks_request)

[EXPERIMENTAL] BatchUpdateTasks: Batch update tasks

### Example

```python
api_instance = api_client_factory.build(TasksApi)
batch_update_tasks_request = BatchUpdateTasksRequest()
api_response = api_instance.batch_update_tasks(batch_update_tasks_request=batch_update_tasks_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **batch_update_tasks_request** | [**BatchUpdateTasksRequest**](BatchUpdateTasksRequest.md)| The details of the request | [optional] 

### Return type

[**BatchUpdateTasksResponse**](BatchUpdateTasksResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **create_task**
> Task createTask = create_task(create_task_request, trigger=trigger)

CreateTask: Create a new Task

### Example

```python
api_instance = api_client_factory.build(TasksApi)
create_task_request = CreateTaskRequest()
trigger = 'trigger_example' # str (optional)
api_response = api_instance.create_task(create_task_request, trigger=trigger)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_task_request** | [**CreateTaskRequest**](CreateTaskRequest.md)| Request to create Task | [required] 
 **trigger** | **str**| The name of the Trigger to invoke | [optional] 

### Return type

[**Task**](Task.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **delete_task**
> DeletedEntityResponse deleteTask = delete_task(id)

DeleteTask: Delete a Task

### Example

```python
api_instance = api_client_factory.build(TasksApi)
id = 'id_example' # str
api_response = api_instance.delete_task(id)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The identifier for the Task to be deleted. | [required] 

### Return type

[**DeletedEntityResponse**](DeletedEntityResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | The details of the input related failure |  -  |
**404** | Task not found. |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **delete_tasks**
> DeletedEntityResponse deleteTasks = delete_tasks(delete_tasks_request=delete_tasks_request)

DeleteTasks: Batch Delete Tasks

### Example

```python
api_instance = api_client_factory.build(TasksApi)
delete_tasks_request = DeleteTasksRequest()
api_response = api_instance.delete_tasks(delete_tasks_request=delete_tasks_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_tasks_request** | [**DeleteTasksRequest**](DeleteTasksRequest.md)| Request with the task instance ids to delete. | [optional] 

### Return type

[**DeletedEntityResponse**](DeletedEntityResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | The details of the input related failure |  -  |
**404** | Task not found. |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_task**
> Task getTask = get_task(id, as_at=as_at)

GetTask: Get a Task

### Example

```python
api_instance = api_client_factory.build(TasksApi)
id = 'id_example' # str
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
api_response = api_instance.get_task(id, as_at=as_at)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Id of the Task to retrieve | [required] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the Task. Defaults to returning the latest version of the Task if not specified. | [optional] 

### Return type

[**Task**](Task.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | The details of the input related failure |  -  |
**404** | Task not found. |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_task_history**
> ResourceListOfChangeItem getTaskHistory = get_task_history(id, as_at=as_at)

GetTaskHistory: Get the history of a Task

### Example

```python
api_instance = api_client_factory.build(TasksApi)
id = 'id_example' # str
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
api_response = api_instance.get_task_history(id, as_at=as_at)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The Task Id for which to get the history | [required] 
 **as_at** | **datetime**| The asAt datetime of the oldest change to retrieve. Defaults to returning the latest version of the Task if not specified. | [optional] 

### Return type

[**ResourceListOfChangeItem**](ResourceListOfChangeItem.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | The details of the input related failure |  -  |
**404** | Task not found. |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **list_tasks**
> PagedResourceListOfTask listTasks = list_tasks(as_at=as_at, filter=filter, sort_by=sort_by, limit=limit, page=page)

ListTasks: List Tasks

### Example

```python
api_instance = api_client_factory.build(TasksApi)
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
filter = 'filter_example' # str (optional)
sort_by = ['sort_by_example'] # List[str] (optional)
limit = 10 # int (optional)
page = 'page_example' # str (optional)
api_response = api_instance.list_tasks(as_at=as_at, filter=filter, sort_by=sort_by, limit=limit, page=page)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **as_at** | **datetime**| The asAt datetime at which to list the Tasks. Defaults to return the latest version of each Task if not specified. | [optional] 
 **filter** | **str**| Expression to filter the result set. Read more about filtering results from LUSID here: https://support.lusid.com/filtering-results-from-lusid. | [optional] 
 **sort_by** | [**List[str]**](str.md)| A list of field names or properties to sort by, each optionally suffixed by \&quot; ASC\&quot; or \&quot; DESC\&quot; | [optional] 
 **limit** | **int**| When paginating, limit the number of returned results to this many. | [optional] [default to 10]
 **page** | **str**| The pagination token to use to continue listing tasks from a previous call to list tasks. This value is returned from the previous call. If a pagination token is provided the sortBy, filter, effectiveAt, and asAt fields must not have changed since the original request. | [optional] 

### Return type

[**PagedResourceListOfTask**](PagedResourceListOfTask.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | The details of the input related failure |  -  |
**404** | No Tasks found. |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **update_task**
> Task updateTask = update_task(id, trigger=trigger, update_task_request=update_task_request)

UpdateTask: Update a Task

### Example

```python
api_instance = api_client_factory.build(TasksApi)
id = 'id_example' # str
trigger = 'trigger_example' # str (optional)
update_task_request = UpdateTaskRequest()
api_response = api_instance.update_task(id, trigger=trigger, update_task_request=update_task_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Id of the Task to act upon | [required] 
 **trigger** | **str**|  | [optional] 
 **update_task_request** | [**UpdateTaskRequest**](UpdateTaskRequest.md)| The details of the request | [optional] 

### Return type

[**Task**](Task.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | The details of the input related failure |  -  |
**404** | Tasks not found. |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

