# insights.VendorLogsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_vendor_log**](VendorLogsApi.md#get_vendor_log) | **GET** /insights/api/vendor/{id} | [EXPERIMENTAL] GetVendorLog: Get the log for a specific vendor request.
[**get_vendor_request**](VendorLogsApi.md#get_vendor_request) | **GET** /insights/api/vendor/{id}/request | [EXPERIMENTAL] GetVendorRequest: Get the request body for a vendor request.
[**get_vendor_response**](VendorLogsApi.md#get_vendor_response) | **GET** /insights/api/vendor/{id}/response | [EXPERIMENTAL] GetVendorResponse: Get the response from a vendor request.
[**list_vendor_logs**](VendorLogsApi.md#list_vendor_logs) | **GET** /insights/api/vendor | [EXPERIMENTAL] ListVendorLogs: List the logs for vendor requests.


### Example

```python
from finbourne.sdk.exceptions import ApiException
from finbourne.sdk.extensions.configuration_options import ConfigurationOptions
from finbourne.sdk.services.insights.models import *

from finbourne.sdk.extensions import (
  SyncApiClientFactory
)

from finbourne.sdk.services.insights.api.vendor_logs_api import VendorLogsApi

# opts = ConfigurationOptions()
# opts.total_timeout_ms = 30_000

# uncomment the below to use an api client factory with overrides
# api_client_factory = SyncApiClientFactory(opts=opts)

api_client_factory = SyncApiClientFactory()
api_instance = api_client_factory.build(VendorLogsApi)
```

---

# **get_vendor_log**
> VendorLog getVendorLog = get_vendor_log(id)

[EXPERIMENTAL] GetVendorLog: Get the log for a specific vendor request.

### Example

```python
api_instance = api_client_factory.build(VendorLogsApi)
id = 'id_example' # str
api_response = api_instance.get_vendor_log(id)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The identifier of the request to obtain the log for. | [required] 

### Return type

[**VendorLog**](VendorLog.md)

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

# **get_vendor_request**
> VendorRequest getVendorRequest = get_vendor_request(id)

[EXPERIMENTAL] GetVendorRequest: Get the request body for a vendor request.

### Example

```python
api_instance = api_client_factory.build(VendorLogsApi)
id = 'id_example' # str
api_response = api_instance.get_vendor_request(id)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The identifier of the request to obtain the content for. | [required] 

### Return type

[**VendorRequest**](VendorRequest.md)

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

# **get_vendor_response**
> VendorResponse getVendorResponse = get_vendor_response(id)

[EXPERIMENTAL] GetVendorResponse: Get the response from a vendor request.

### Example

```python
api_instance = api_client_factory.build(VendorLogsApi)
id = 'id_example' # str
api_response = api_instance.get_vendor_response(id)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The identifier of the request to obtain the response for. | [required] 

### Return type

[**VendorResponse**](VendorResponse.md)

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

# **list_vendor_logs**
> ResourceListWithHistogramOfVendorLog listVendorLogs = list_vendor_logs(filter=filter, sort_by=sort_by, limit=limit, page=page, histogram_interval=histogram_interval)

[EXPERIMENTAL] ListVendorLogs: List the logs for vendor requests.

### Example

```python
api_instance = api_client_factory.build(VendorLogsApi)
filter = 'filter_example' # str (optional)
sort_by = 'sort_by_example' # str (optional)
limit = 56 # int (optional)
page = 'page_example' # str (optional)
histogram_interval = 'histogram_interval_example' # str (optional)
api_response = api_instance.list_vendor_logs(filter=filter, sort_by=sort_by, limit=limit, page=page, histogram_interval=histogram_interval)
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

[**ResourceListWithHistogramOfVendorLog**](ResourceListWithHistogramOfVendorLog.md)

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

