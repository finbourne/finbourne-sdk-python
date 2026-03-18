# insights.AccessEvaluationsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_access_evaluation_log**](AccessEvaluationsApi.md#get_access_evaluation_log) | **GET** /insights/api/access/{id} | [EARLY ACCESS] GetAccessEvaluationLog: Get the log for a specific access evaluation. This endpoint will be deprecated in the near future.
[**list_access_evaluation_logs**](AccessEvaluationsApi.md#list_access_evaluation_logs) | **GET** /insights/api/access | [EARLY ACCESS] ListAccessEvaluationLogs: List the logs for access evaluations.


### Example

```python
from finbourne.sdk.exceptions import ApiException
from finbourne.sdk.extensions.configuration_options import ConfigurationOptions
from finbourne.sdk.services.insights.models import *

from finbourne.sdk.extensions import (
  SyncApiClientFactory
)

from finbourne.sdk.services.insights.api.access_evaluations_api import AccessEvaluationsApi

# opts = ConfigurationOptions()
# opts.total_timeout_ms = 30_000

# uncomment the below to use an api client factory with overrides
# api_client_factory = SyncApiClientFactory(opts=opts)

api_client_factory = SyncApiClientFactory()
api_instance = api_client_factory.build(AccessEvaluationsApi)
```

---

# **get_access_evaluation_log**
> AccessEvaluationLog getAccessEvaluationLog = get_access_evaluation_log(id)

[EARLY ACCESS] GetAccessEvaluationLog: Get the log for a specific access evaluation. This endpoint will be deprecated in the near future.

### Example

```python
api_instance = api_client_factory.build(AccessEvaluationsApi)
id = 'id_example' # str
api_response = api_instance.get_access_evaluation_log(id)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The identifier of the access evaluation to obtain the log for. | [required] 

### Return type

[**AccessEvaluationLog**](AccessEvaluationLog.md)

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

# **list_access_evaluation_logs**
> ResourceListWithHistogramOfAccessEvaluationLog listAccessEvaluationLogs = list_access_evaluation_logs(start_at=start_at, end_at=end_at, filter=filter, sort_by=sort_by, limit=limit, page=page, histogram_interval=histogram_interval)

[EARLY ACCESS] ListAccessEvaluationLogs: List the logs for access evaluations.

### Example

```python
api_instance = api_client_factory.build(AccessEvaluationsApi)
start_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
end_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
filter = 'filter_example' # str (optional)
sort_by = 'sort_by_example' # str (optional)
limit = 56 # int (optional)
page = 'page_example' # str (optional)
histogram_interval = 'histogram_interval_example' # str (optional)
api_response = api_instance.list_access_evaluation_logs(start_at=start_at, end_at=end_at, filter=filter, sort_by=sort_by, limit=limit, page=page, histogram_interval=histogram_interval)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_at** | **datetime**| Start date from which point to fetch logs. | [optional] 
 **end_at** | **datetime**| End date to which point to fetch logs. | [optional] 
 **filter** | **str**| Expression to filter the result set. Read more about [filtering results from LUSID](https://support.lusid.com/filtering-results-from-lusid). | [optional] 
 **sort_by** | **str**| Order the results by these fields. Use the &#39;-&#39; sign to denote descending order e.g. -MyFieldName. Multiple fields can be denoted by a comma e.g. -MyFieldName,AnotherFieldName,-AFurtherFieldName | [optional] 
 **limit** | **int**| When paginating, only return this number of records. The minimum value is 0 and the maximum is 10000. | [optional] 
 **page** | **str**| Encoded page string returned from a previous search result that will retrieve the next page of data. When this field is supplied, filter and sortby fields should not be supplied. | [optional] 
 **histogram_interval** | **str**| The interval for an included histogram of the logs | [optional] 

### Return type

[**ResourceListWithHistogramOfAccessEvaluationLog**](ResourceListWithHistogramOfAccessEvaluationLog.md)

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

