# luminesce.MultiQueryExecutionApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_multi_query**](MultiQueryExecutionApi.md#cancel_multi_query) | **DELETE** /honeycomb/api/MultiQueryBackground/{executionId} | CancelMultiQuery: Cancel / Clear a previously started query-set
[**get_progress_of_multi_query**](MultiQueryExecutionApi.md#get_progress_of_multi_query) | **GET** /honeycomb/api/MultiQueryBackground/{executionId} | GetProgressOfMultiQuery: View progress of the entire query-set load
[**start_queries**](MultiQueryExecutionApi.md#start_queries) | **PUT** /honeycomb/api/MultiQueryBackground | StartQueries: Run a given set of Sql queries in the background


### Example

```python
from finbourne.sdk.exceptions import ApiException
from finbourne.sdk.extensions.configuration_options import ConfigurationOptions
from finbourne.sdk.services.luminesce.models import *

from finbourne.sdk.extensions import (
  SyncApiClientFactory
)

from finbourne.sdk.services.luminesce.api.multi_query_execution_api import MultiQueryExecutionApi

# opts = ConfigurationOptions()
# opts.total_timeout_ms = 30_000

# uncomment the below to use an api client factory with overrides
# api_client_factory = SyncApiClientFactory(opts=opts)

api_client_factory = SyncApiClientFactory()
api_instance = api_client_factory.build(MultiQueryExecutionApi)
```

---

# **cancel_multi_query**
> BackgroundQueryCancelResponse cancelMultiQuery = cancel_multi_query(execution_id)

CancelMultiQuery: Cancel / Clear a previously started query-set

Cancel the query-set (if still running) / clear the data (if already returned) The following error codes are to be anticipated with standard Problem Detail reports: - 401 Unauthorized - 403 Forbidden - 404 Not Found : The requested query result doesn't exist and is not running. 

### Example

```python
api_instance = api_client_factory.build(MultiQueryExecutionApi)
execution_id = 'execution_id_example' # str
api_response = api_instance.cancel_multi_query(execution_id)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **execution_id** | **str**| ExecutionId returned when starting the query | [required] 

### Return type

[**BackgroundQueryCancelResponse**](BackgroundQueryCancelResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_progress_of_multi_query**
> BackgroundMultiQueryProgressResponse getProgressOfMultiQuery = get_progress_of_multi_query(execution_id)

GetProgressOfMultiQuery: View progress of the entire query-set load

View progress information (up until this point) for the entire query-set The following error codes are to be anticipated with standard Problem Detail reports: - 401 Unauthorized - 403 Forbidden - 404 Not Found : The requested query result doesn't exist and is not running. - 429 Too Many Requests : Please try your request again soon   1. The query has been executed successfully in the past yet the server-instance receiving this request (e.g. from a load balancer) doesn't yet have this data available.   1. By virtue of the request you have just placed this will have started to load from the persisted cache and will soon be available.   1. It is also the case that the original server-instance to process the original query is likely to already be able to service this request.

### Example

```python
api_instance = api_client_factory.build(MultiQueryExecutionApi)
execution_id = 'execution_id_example' # str
api_response = api_instance.get_progress_of_multi_query(execution_id)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **execution_id** | **str**| ExecutionId returned when starting the query | [required] 

### Return type

[**BackgroundMultiQueryProgressResponse**](BackgroundMultiQueryProgressResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **start_queries**
> BackgroundMultiQueryResponse startQueries = start_queries(type, body, as_at=as_at, effective_at=effective_at, limit1=limit1, limit2=limit2, input1=input1, input2=input2, input3=input3, timeout_seconds=timeout_seconds, keep_for_seconds=keep_for_seconds)

StartQueries: Run a given set of Sql queries in the background

 Allow for starting a potentially long running query and getting back an immediate response with how to  - fetch the data in various formats (if available, or if not simply being informed it is not yet ready), on a per result basis - view progress information (up until this point), for all results in one go - cancel the queries (if still running) / clear the data (if already returned)  The following error codes are to be anticipated with standard Problem Detail reports: - 400 BadRequest - there was something wrong with your query syntax (the issue was detected at parse-time) - 401 Unauthorized - 403 Forbidden 

### Example

```python
api_instance = api_client_factory.build(MultiQueryExecutionApi)
type = luminesce.MultiQueryDefinitionType() # MultiQueryDefinitionType
body = Apple # str
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
effective_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
limit1 = 56 # int (optional)
limit2 = 56 # int (optional)
input1 = 'input1_example' # str (optional)
input2 = 'input2_example' # str (optional)
input3 = 'input3_example' # str (optional)
timeout_seconds = 0 # int (optional)
keep_for_seconds = 0 # int (optional)
api_response = api_instance.start_queries(type, body, as_at=as_at, effective_at=effective_at, limit1=limit1, limit2=limit2, input1=input1, input2=input2, input3=input3, timeout_seconds=timeout_seconds, keep_for_seconds=keep_for_seconds)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | [**MultiQueryDefinitionType**](.md)| An enum value defining the set of statements being executed | [required] 
 **body** | **str**| A \&quot;search\&quot; value (e.g. &#39;Apple&#39; on an instrument search, a &#x60;Finbourne.Filtering&#x60; expression of Insights, etc.) In the cases where \&quot;Nothing\&quot; is valid for a &#x60;Finbourne.Filtering&#x60; expression, pass &#x60;True&#x60;. | [required] 
 **as_at** | **datetime**| The AsAt time used by any bitemporal provider in the queries. | [optional] 
 **effective_at** | **datetime**| The EffectiveAt time used by any bitemporal provider in the queries. | [optional] 
 **limit1** | **int**| A limit that is applied to first-level queries (e.g. Instruments themselves) | [optional] 
 **limit2** | **int**| A limit that is applied to second-level queries (e.g. Holdings based on the set of Instruments found) | [optional] 
 **input1** | **str**| A value available to queries, these vary by &#39;type&#39; and are only used by some types at all. e.g. a start-date of some sort | [optional] 
 **input2** | **str**| A second value available to queries, these vary by &#39;type&#39; and are only used by some types at all. | [optional] 
 **input3** | **str**| A third value available to queries, these vary by &#39;type&#39; and are only used by some types at all. | [optional] 
 **timeout_seconds** | **int**| Maximum time the query may run for, in seconds: &lt;0 → ∞, 0 → 1200s (20m) | [optional] [default to 0]
 **keep_for_seconds** | **int**| Maximum time the result may be kept for, in seconds: &lt;0 → 1200 (20m), 0 → 28800 (8h), max &#x3D; 2,678,400 (31d) | [optional] [default to 0]

### Return type

[**BackgroundMultiQueryResponse**](BackgroundMultiQueryResponse.md)

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

