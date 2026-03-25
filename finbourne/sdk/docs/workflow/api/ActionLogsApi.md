# workflow.ActionLogsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_action_logs**](ActionLogsApi.md#get_action_logs) | **GET** /workflow/api/actionlogs/{id} | GetActionLogs: Get the Action Logs for an Action Id


### Example

```python
from finbourne.sdk.exceptions import ApiException
from finbourne.sdk.extensions.configuration_options import ConfigurationOptions
from finbourne.sdk.services.workflow.models import *

from finbourne.sdk.extensions import (
  SyncApiClientFactory
)

from finbourne.sdk.services.workflow.api.action_logs_api import ActionLogsApi

# opts = ConfigurationOptions()
# opts.total_timeout_ms = 30_000

# uncomment the below to use an api client factory with overrides
# api_client_factory = SyncApiClientFactory(opts=opts)

api_client_factory = SyncApiClientFactory()
api_instance = api_client_factory.build(ActionLogsApi)
```

---

# **get_action_logs**
> ActionLog getActionLogs = get_action_logs(id)

GetActionLogs: Get the Action Logs for an Action Id

### Example

```python
api_instance = api_client_factory.build(ActionLogsApi)
id = 'id_example' # str
api_response = api_instance.get_action_logs(id)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The Action Id | [required] 

### Return type

[**ActionLog**](ActionLog.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | The details of the input related failure |  -  |
**404** | Action Log not found. |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

