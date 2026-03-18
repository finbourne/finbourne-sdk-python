# workflow.TaskDefinitionsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_task_definition**](TaskDefinitionsApi.md#create_task_definition) | **POST** /workflow/api/taskdefinitions | CreateTaskDefinition: Create a new Task Definition
[**delete_task_definition**](TaskDefinitionsApi.md#delete_task_definition) | **DELETE** /workflow/api/taskdefinitions/{scope}/{code} | DeleteTaskDefinition: Delete a Task Definition
[**get_task_definition**](TaskDefinitionsApi.md#get_task_definition) | **GET** /workflow/api/taskdefinitions/{scope}/{code} | GetTaskDefinition: Get a Task Definition
[**list_task_definitions**](TaskDefinitionsApi.md#list_task_definitions) | **GET** /workflow/api/taskdefinitions | ListTaskDefinitions: List Task Definitions
[**list_tasks_for_task_definition**](TaskDefinitionsApi.md#list_tasks_for_task_definition) | **GET** /workflow/api/taskdefinitions/{scope}/{code}/tasks | ListTasksForTaskDefinition: List Tasks for a Task Definition
[**update_task_definition**](TaskDefinitionsApi.md#update_task_definition) | **PUT** /workflow/api/taskdefinitions/{scope}/{code} | UpdateTaskDefinition: Update an existing Task Definition


### Example

```python
from finbourne.sdk.exceptions import ApiException
from finbourne.sdk.extensions.configuration_options import ConfigurationOptions
from finbourne.sdk.services.workflow.models import *

from finbourne.sdk.extensions import (
  SyncApiClientFactory
)

from finbourne.sdk.services.workflow.api.task_definitions_api import TaskDefinitionsApi

# opts = ConfigurationOptions()
# opts.total_timeout_ms = 30_000

# uncomment the below to use an api client factory with overrides
# api_client_factory = SyncApiClientFactory(opts=opts)

api_client_factory = SyncApiClientFactory()
api_instance = api_client_factory.build(TaskDefinitionsApi)
```

---

# **create_task_definition**
> TaskDefinition createTaskDefinition = create_task_definition(create_task_definition_request)

CreateTaskDefinition: Create a new Task Definition

### Example

```python
api_instance = api_client_factory.build(TaskDefinitionsApi)
create_task_definition_request = CreateTaskDefinitionRequest()
api_response = api_instance.create_task_definition(create_task_definition_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_task_definition_request** | [**CreateTaskDefinitionRequest**](CreateTaskDefinitionRequest.md)| The data to create a Task Definition | [required] 

### Return type

[**TaskDefinition**](TaskDefinition.md)

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

# **delete_task_definition**
> DeletedEntityResponse deleteTaskDefinition = delete_task_definition(scope, code)

DeleteTaskDefinition: Delete a Task Definition

### Example

```python
api_instance = api_client_factory.build(TaskDefinitionsApi)
scope = 'scope_example' # str
code = 'code_example' # str
api_response = api_instance.delete_task_definition(scope, code)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope that identifies a Task Definition | [required] 
 **code** | **str**| The code that identifies a Task Definition | [required] 

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
**404** | Task Definition not found. |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_task_definition**
> TaskDefinition getTaskDefinition = get_task_definition(scope, code, as_at=as_at)

GetTaskDefinition: Get a Task Definition

### Example

```python
api_instance = api_client_factory.build(TaskDefinitionsApi)
scope = 'scope_example' # str
code = 'code_example' # str
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
api_response = api_instance.get_task_definition(scope, code, as_at=as_at)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope that identifies a Task Definition | [required] 
 **code** | **str**| The code that identifies a Task Definition | [required] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the Task Definition. Defaults to returning the latest version of the Task Definition if not specified. | [optional] 

### Return type

[**TaskDefinition**](TaskDefinition.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | The details of the input related failure |  -  |
**404** | Task Definition not found. |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **list_task_definitions**
> PagedResourceListOfTaskDefinition listTaskDefinitions = list_task_definitions(as_at=as_at, filter=filter, sort_by=sort_by, limit=limit, page=page)

ListTaskDefinitions: List Task Definitions

### Example

```python
api_instance = api_client_factory.build(TaskDefinitionsApi)
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
filter = 'filter_example' # str (optional)
sort_by = ['sort_by_example'] # List[str] (optional)
limit = 10 # int (optional)
page = 'page_example' # str (optional)
api_response = api_instance.list_task_definitions(as_at=as_at, filter=filter, sort_by=sort_by, limit=limit, page=page)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **as_at** | **datetime**| The asAt datetime at which to list the Task Definitions. Defaults to return the latest version of each Task Definition if not specified. | [optional] 
 **filter** | **str**| Expression to filter the result set. Read more about filtering results from LUSID here: https://support.lusid.com/filtering-results-from-lusid. | [optional] 
 **sort_by** | [**List[str]**](str.md)| A list of field names or properties to sort by, each suffixed by \&quot; ASC\&quot; or \&quot; DESC\&quot; | [optional] 
 **limit** | **int**| When paginating, limit the number of returned results to this many. | [optional] [default to 10]
 **page** | **str**| The pagination token to use to continue listing task definitions from a previous call to list task definitions. This value is returned from the previous call. If a pagination token is provided the sortBy, filter, effectiveAt, and asAt fields must not have changed since the original request. | [optional] 

### Return type

[**PagedResourceListOfTaskDefinition**](PagedResourceListOfTaskDefinition.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of Task Definitions |  -  |
**400** | The details of the input related failure |  -  |
**404** | No Task Definitions found. |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **list_tasks_for_task_definition**
> ResourceListOfTask listTasksForTaskDefinition = list_tasks_for_task_definition(scope, code, as_at=as_at)

ListTasksForTaskDefinition: List Tasks for a Task Definition

### Example

```python
api_instance = api_client_factory.build(TaskDefinitionsApi)
scope = 'scope_example' # str
code = 'code_example' # str
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
api_response = api_instance.list_tasks_for_task_definition(scope, code, as_at=as_at)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope that identifies a Task Definition | [required] 
 **code** | **str**| The code that identifies a Task Definition | [required] 
 **as_at** | **datetime**| The asAt datetime at which to list the Tasks. Defaults to return the latest version of each Task if not specified. | [optional] 

### Return type

[**ResourceListOfTask**](ResourceListOfTask.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | The details of the input related failure |  -  |
**404** | No tasks found for this Task Definition. |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **update_task_definition**
> TaskDefinition updateTaskDefinition = update_task_definition(scope, code, update_task_definition_request)

UpdateTaskDefinition: Update an existing Task Definition

### Example

```python
api_instance = api_client_factory.build(TaskDefinitionsApi)
scope = 'scope_example' # str
code = 'code_example' # str
update_task_definition_request = UpdateTaskDefinitionRequest()
api_response = api_instance.update_task_definition(scope, code, update_task_definition_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope that identifies a Task Definition | [required] 
 **code** | **str**| The code that identifies a Task Definition | [required] 
 **update_task_definition_request** | [**UpdateTaskDefinitionRequest**](UpdateTaskDefinitionRequest.md)| The data to update a Task Definition | [required] 

### Return type

[**TaskDefinition**](TaskDefinition.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | The details of the input related failure |  -  |
**404** | Task Definition not found. |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

