# workflow.WorkflowsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_workflow**](WorkflowsApi.md#create_workflow) | **POST** /workflow/api/workflows | [EXPERIMENTAL] CreateWorkflow: Create a new Workflow
[**get_workflow**](WorkflowsApi.md#get_workflow) | **GET** /workflow/api/workflows/{scope}/{code} | [EXPERIMENTAL] GetWorkflow: Get a Workflow


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

[EXPERIMENTAL] CreateWorkflow: Create a new Workflow

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

[EXPERIMENTAL] GetWorkflow: Get a Workflow

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

