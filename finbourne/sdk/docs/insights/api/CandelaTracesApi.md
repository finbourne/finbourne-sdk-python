# insights.CandelaTracesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_trace_diagram**](CandelaTracesApi.md#get_trace_diagram) | **GET** /insights/api/candelatraces/{traceId}/diagram | [EARLY ACCESS] GetTraceDiagram: Get the diagram representation for a specific trace.
[**get_trace_log**](CandelaTracesApi.md#get_trace_log) | **GET** /insights/api/candelatraces/{traceId} | [EARLY ACCESS] GetTraceLog: Get the log for a specific trace.
[**list_trace_event_logs**](CandelaTracesApi.md#list_trace_event_logs) | **GET** /insights/api/candelatraces/{traceId}/events | [EARLY ACCESS] ListTraceEventLogs: Get the trace event logs for a specific trace.
[**list_trace_logs**](CandelaTracesApi.md#list_trace_logs) | **GET** /insights/api/candelatraces | [EARLY ACCESS] ListTraceLogs: Get the logs for traces.


### Example

```python
from finbourne.sdk.exceptions import ApiException
from finbourne.sdk.extensions.configuration_options import ConfigurationOptions
from finbourne.sdk.services.insights.models import *

from finbourne.sdk.extensions import (
  SyncApiClientFactory
)

from finbourne.sdk.services.insights.api.candela_traces_api import CandelaTracesApi

# opts = ConfigurationOptions()
# opts.total_timeout_ms = 30_000

# uncomment the below to use an api client factory with overrides
# api_client_factory = SyncApiClientFactory(opts=opts)

api_client_factory = SyncApiClientFactory()
api_instance = api_client_factory.build(CandelaTracesApi)
```

---

# **get_trace_diagram**
> TraceDiagramResponse getTraceDiagram = get_trace_diagram(trace_id)

[EARLY ACCESS] GetTraceDiagram: Get the diagram representation for a specific trace.

### Example

```python
api_instance = api_client_factory.build(CandelaTracesApi)
trace_id = 'trace_id_example' # str
api_response = api_instance.get_trace_diagram(trace_id)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trace_id** | **str**| The identifier of the trace. | [required] 

### Return type

[**TraceDiagramResponse**](TraceDiagramResponse.md)

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

# **get_trace_log**
> TraceLog getTraceLog = get_trace_log(trace_id)

[EARLY ACCESS] GetTraceLog: Get the log for a specific trace.

### Example

```python
api_instance = api_client_factory.build(CandelaTracesApi)
trace_id = 'trace_id_example' # str
api_response = api_instance.get_trace_log(trace_id)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trace_id** | **str**| The identifier of the request to obtain the log for. | [required] 

### Return type

[**TraceLog**](TraceLog.md)

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

# **list_trace_event_logs**
> ResourceListOfTraceEventLog listTraceEventLogs = list_trace_event_logs(trace_id, page=page)

[EARLY ACCESS] ListTraceEventLogs: Get the trace event logs for a specific trace.

### Example

```python
api_instance = api_client_factory.build(CandelaTracesApi)
trace_id = 'trace_id_example' # str
page = 'page_example' # str (optional)
api_response = api_instance.list_trace_event_logs(trace_id, page=page)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trace_id** | **str**| The identifier of the request to obtain the log for. | [required] 
 **page** | **str**|  | [optional] 

### Return type

[**ResourceListOfTraceEventLog**](ResourceListOfTraceEventLog.md)

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

# **list_trace_logs**
> ResourceListOfTraceLog listTraceLogs = list_trace_logs(filter=filter, sort_by=sort_by, limit=limit, page=page)

[EARLY ACCESS] ListTraceLogs: Get the logs for traces.

### Example

```python
api_instance = api_client_factory.build(CandelaTracesApi)
filter = 'filter_example' # str (optional)
sort_by = 'sort_by_example' # str (optional)
limit = 56 # int (optional)
page = 'page_example' # str (optional)
api_response = api_instance.list_trace_logs(filter=filter, sort_by=sort_by, limit=limit, page=page)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Expression to filter the result set. Read more about [filtering results from LUSID](https://support.lusid.com/filtering-results-from-lusid). | [optional] 
 **sort_by** | **str**| Order the results by these fields. Use the &#39;-&#39; sign to denote descending order e.g. -MyFieldName. Multiple fields can be denoted by a comma e.g. -MyFieldName,AnotherFieldName,-AFurtherFieldName | [optional] 
 **limit** | **int**| When paginating, only return this number of records. The minimum value is 0 and the maximum is 10000. | [optional] 
 **page** | **str**| Encoded pagwwwwe string returned from a previous search result that will retrieve the next page of data. When this field is supplied, filter and sortby fields should not be supplied. | [optional] 

### Return type

[**ResourceListOfTraceLog**](ResourceListOfTraceLog.md)

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

