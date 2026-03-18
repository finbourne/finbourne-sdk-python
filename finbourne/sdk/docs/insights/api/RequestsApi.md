# insights.RequestsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_request**](RequestsApi.md#get_request) | **GET** /insights/api/requests/{id}/request | GetRequest: Get the request content for a specific API request.
[**get_request_log**](RequestsApi.md#get_request_log) | **GET** /insights/api/requests/{id} | GetRequestLog: Get the log for a specific API request.
[**get_response**](RequestsApi.md#get_response) | **GET** /insights/api/requests/{id}/response | GetResponse: Get the response for a specific API request.
[**list_request_logs**](RequestsApi.md#list_request_logs) | **GET** /insights/api/requests | ListRequestLogs: Get the logs for API requests.


### Example

```python
from finbourne.sdk.exceptions import ApiException
from finbourne.sdk.extensions.configuration_options import ConfigurationOptions
from finbourne.sdk.services.insights.models import *

from finbourne.sdk.extensions import (
  SyncApiClientFactory
)

from finbourne.sdk.services.insights.api.requests_api import RequestsApi

# opts = ConfigurationOptions()
# opts.total_timeout_ms = 30_000

# uncomment the below to use an api client factory with overrides
# api_client_factory = SyncApiClientFactory(opts=opts)

api_client_factory = SyncApiClientFactory()
api_instance = api_client_factory.build(RequestsApi)
```

---

# **get_request**
> Request getRequest = get_request(id)

GetRequest: Get the request content for a specific API request.

### Example

```python
api_instance = api_client_factory.build(RequestsApi)
id = 'id_example' # str
api_response = api_instance.get_request(id)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The identifier of the request to obtain the content for. | [required] 

### Return type

[**Request**](Request.md)

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

# **get_request_log**
> RequestLog getRequestLog = get_request_log(id)

GetRequestLog: Get the log for a specific API request.

### Example

```python
api_instance = api_client_factory.build(RequestsApi)
id = 'id_example' # str
api_response = api_instance.get_request_log(id)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The identifier of the request to obtain the log for. | [required] 

### Return type

[**RequestLog**](RequestLog.md)

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

# **get_response**
> Response getResponse = get_response(id)

GetResponse: Get the response for a specific API request.

### Example

```python
api_instance = api_client_factory.build(RequestsApi)
id = 'id_example' # str
api_response = api_instance.get_response(id)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The identifier of the request to obtain the response for. | [required] 

### Return type

[**Response**](Response.md)

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

# **list_request_logs**
> ResourceListWithHistogramOfRequestLog listRequestLogs = list_request_logs(filter=filter, sort_by=sort_by, limit=limit, page=page, histogram_interval=histogram_interval)

ListRequestLogs: Get the logs for API requests.

### Example

```python
api_instance = api_client_factory.build(RequestsApi)
filter = 'filter_example' # str (optional)
sort_by = 'sort_by_example' # str (optional)
limit = 56 # int (optional)
page = 'page_example' # str (optional)
histogram_interval = 'histogram_interval_example' # str (optional)
api_response = api_instance.list_request_logs(filter=filter, sort_by=sort_by, limit=limit, page=page, histogram_interval=histogram_interval)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Expression to filter the result set. Read more about [filtering results from LUSID](https://support.lusid.com/filtering-results-from-lusid). | [optional] 
 **sort_by** | **str**| Order the results by these fields. Use the &#39;-&#39; sign to denote descending order e.g. -MyFieldName. Multiple fields can be denoted by a comma e.g. -MyFieldName,AnotherFieldName,-AFurtherFieldName | [optional] 
 **limit** | **int**| When paginating, only return this number of records. The minimum value is 0 and the maximum is 10000. | [optional] 
 **page** | **str**| Encoded page string returned from a previous search result that will retrieve the next page of data. When this field is supplied, filter and sortby fields should not be supplied. | [optional] 
 **histogram_interval** | **str**| Optional interval to use in a histogram of the returned values. If not provided, no histogram will be generated. | [optional] 

### Return type

[**ResourceListWithHistogramOfRequestLog**](ResourceListWithHistogramOfRequestLog.md)

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

