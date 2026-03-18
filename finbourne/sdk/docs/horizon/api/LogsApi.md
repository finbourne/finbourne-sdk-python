# horizon.LogsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_integration_log_results**](LogsApi.md#get_integration_log_results) | **GET** /horizon/api/logs | [EXPERIMENTAL] GetIntegrationLogResults: Get integration log results
[**insert_external_logs**](LogsApi.md#insert_external_logs) | **POST** /horizon/api/logs/{instanceid}/{runid} | [EXPERIMENTAL] InsertExternalLogs: Inserts external logs into the specified ExternalApp Integration instance execution


### Example

```python
from finbourne.sdk.exceptions import ApiException
from finbourne.sdk.extensions.configuration_options import ConfigurationOptions
from finbourne.sdk.services.horizon.models import *

from finbourne.sdk.extensions import (
  SyncApiClientFactory
)

from finbourne.sdk.services.horizon.api.logs_api import LogsApi

# opts = ConfigurationOptions()
# opts.total_timeout_ms = 30_000

# uncomment the below to use an api client factory with overrides
# api_client_factory = SyncApiClientFactory(opts=opts)

api_client_factory = SyncApiClientFactory()
api_instance = api_client_factory.build(LogsApi)
```

---

# **get_integration_log_results**
> PagedResourceListOfIIntegrationLogResponse getIntegrationLogResults = get_integration_log_results(filter=filter, sort_by=sort_by, limit=limit, page_token=page_token)

[EXPERIMENTAL] GetIntegrationLogResults: Get integration log results

Get integration log results

### Example

```python
api_instance = api_client_factory.build(LogsApi)
filter = 'filter_example' # str (optional)
sort_by = ['sort_by_example'] # List[str] (optional)
limit = 100 # int (optional)
page_token = '' # str (optional)
api_response = api_instance.get_integration_log_results(filter=filter, sort_by=sort_by, limit=limit, page_token=page_token)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Expression to filter the result set. | [optional] 
 **sort_by** | [**List[str]**](str.md)| A list of field names or properties to sort by, each suffixed by \&quot; ASC\&quot; or \&quot; DESC\&quot;. | [optional] 
 **limit** | **int**| When paginating, limit the results to this number. | [optional] [default to 100]
 **page_token** | **str**| The pagination token to use to continue listing integration logs; this value is returned from             the previous call. If a pagination token is provided, the &lt;i&gt;sortBy&lt;/i&gt; and &lt;i&gt;filter&lt;/i&gt; fields must not have changed since the original request.             For more information, see https://support.lusid.com/knowledgebase/article/KA-01915. | [optional] [default to &#39;&#39;]

### Return type

[**PagedResourceListOfIIntegrationLogResponse**](PagedResourceListOfIIntegrationLogResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | The details of the input related failure |  -  |
**404** | Not Found |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **insert_external_logs**
> object insertExternalLogs = insert_external_logs(instanceid, runid, external_log_insertion_request)

[EXPERIMENTAL] InsertExternalLogs: Inserts external logs into the specified ExternalApp Integration instance execution

### Example

```python
api_instance = api_client_factory.build(LogsApi)
instanceid = 'instanceid_example' # str
runid = 'runid_example' # str
external_log_insertion_request = ExternalLogInsertionRequest()
api_response = api_instance.insert_external_logs(instanceid, runid, external_log_insertion_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instanceid** | **str**|  | [required] 
 **runid** | **str**|  | [required] 
 **external_log_insertion_request** | [**ExternalLogInsertionRequest**](ExternalLogInsertionRequest.md)|  | [required] 

### Return type

**object**

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

