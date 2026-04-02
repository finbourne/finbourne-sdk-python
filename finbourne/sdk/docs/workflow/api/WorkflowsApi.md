# workflow.WorkflowsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_workflow**](WorkflowsApi.md#create_workflow) | **POST** /workflow/api/workflows | CreateWorkflow: Create a new Workflow
[**get_workflow**](WorkflowsApi.md#get_workflow) | **GET** /workflow/api/workflows/{scope}/{code} | GetWorkflow: Get a Workflow
[**list_workflows**](WorkflowsApi.md#list_workflows) | **GET** /workflow/api/workflows | ListWorkflows: List Workflows


### Example

```python
from finbourne.sdk.exceptions import ApiException
from finbourne.sdk.extensions.configuration_options import ConfigurationOptions
from finbourne.sdk.services.workflow.models import *

from finbourne.sdk.extensions import (
  SyncApiClientFactory
)

from finbourne.sdk.services.workflow.api.workflows_api import WorkflowsApi

# opts = ConfigurationOptions()
# opts.total_timeout_ms = 30_000

# uncomment the below to use an api client factory with overrides
# api_client_factory = SyncApiClientFactory(opts=opts)

api_client_factory = SyncApiClientFactory()
api_instance = api_client_factory.build(WorkflowsApi)
```

---

# **create_workflow**
> WorkflowResponse createWorkflow = create_workflow(create_workflow_request)

CreateWorkflow: Create a new Workflow

### Example

```python
api_instance = api_client_factory.build(WorkflowsApi)
create_workflow_request = CreateWorkflowRequest()
api_response = api_instance.create_workflow(create_workflow_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_workflow_request** | [**CreateWorkflowRequest**](CreateWorkflowRequest.md)| The data to create a Workflow | [required] 

### Return type

[**WorkflowResponse**](WorkflowResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | The details of the input related failure |  -  |
**409** | Workflow already exists. |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_workflow**
> WorkflowResponse getWorkflow = get_workflow(scope, code, as_at=as_at)

GetWorkflow: Get a Workflow

### Example

```python
api_instance = api_client_factory.build(WorkflowsApi)
scope = 'scope_example' # str
code = 'code_example' # str
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
api_response = api_instance.get_workflow(scope, code, as_at=as_at)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope that identifies a Workflow | [required] 
 **code** | **str**| The code that identifies a Workflow | [required] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the Workflow. Defaults to returning the latest version if not specified. | [optional] 

### Return type

[**WorkflowResponse**](WorkflowResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | The details of the input related failure |  -  |
**404** | Workflow not found. |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **list_workflows**
> PagedResourceListOfWorkflowResponse listWorkflows = list_workflows(as_at=as_at, filter=filter, sort_by=sort_by, limit=limit, page=page)

ListWorkflows: List Workflows

### Example

```python
api_instance = api_client_factory.build(WorkflowsApi)
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
filter = 'filter_example' # str (optional)
sort_by = ['sort_by_example'] # List[str] (optional)
limit = 10 # int (optional)
page = 'page_example' # str (optional)
api_response = api_instance.list_workflows(as_at=as_at, filter=filter, sort_by=sort_by, limit=limit, page=page)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **as_at** | **datetime**| The asAt datetime at which to list the Workflows. Defaults to return the latest version of each Workflow if not specified. | [optional] 
 **filter** | **str**| Expression to filter the result set. Read more about filtering results from LUSID here: https://support.lusid.com/filtering-results-from-lusid. | [optional] 
 **sort_by** | [**List[str]**](str.md)| A list of field names or properties to sort by, each suffixed by \&quot; ASC\&quot; or \&quot; DESC\&quot; | [optional] 
 **limit** | **int**| When paginating, limit the number of returned results to this many. | [optional] [default to 10]
 **page** | **str**| The pagination token to use to continue listing workflows from a previous call to list workflows. This value is returned from the previous call. If a pagination token is provided the sortBy, filter, effectiveAt, and asAt fields must not have changed since the original request. | [optional] 

### Return type

[**PagedResourceListOfWorkflowResponse**](PagedResourceListOfWorkflowResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | The details of the input related failure |  -  |
**404** | No Workflows found. |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

