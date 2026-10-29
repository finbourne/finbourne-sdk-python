# luminesce.MultiQueryExecutionApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_multi_query**](MultiQueryExecutionApi.md#cancel_multi_query) | **DELETE** /honeycomb/api/MultiQueryBackground/{executionId} | CancelMultiQuery: Cancel / Clear a previously started query-set
[**download_multi_query_results**](MultiQueryExecutionApi.md#download_multi_query_results) | **GET** /honeycomb/api/MultiQueryBackground/{executionId}/download | DownloadMultiQueryResults: Downloads the results of a custom query-set as one file
[**get_progress_of_multi_query**](MultiQueryExecutionApi.md#get_progress_of_multi_query) | **GET** /honeycomb/api/MultiQueryBackground/{executionId} | GetProgressOfMultiQuery: View progress of the entire query-set load
[**list_custom_queries**](MultiQueryExecutionApi.md#list_custom_queries) | **GET** /honeycomb/api/MultiQueryBackground | ListCustomQueries: List the custom query-sets available to the calling user
[**save_multi_query_results_to_drive**](MultiQueryExecutionApi.md#save_multi_query_results_to_drive) | **GET** /honeycomb/api/MultiQueryBackground/{executionId}/drive | SaveMultiQueryResultsToDrive: Saves the results of a custom query-set directly to Drive, as one file
[**start_custom_queries**](MultiQueryExecutionApi.md#start_custom_queries) | **PUT** /honeycomb/api/MultiQueryBackground/custom | StartCustomQueries: Run a caller-supplied set of Sql queries in the background
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

[**BackgroundQueryCancelResponse**](../model/BackgroundQueryCancelResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **download_multi_query_results**
> bytes downloadMultiQueryResults = download_multi_query_results(execution_id, format=format, file_name=file_name, date_time_format=date_time_format, load_wait_milliseconds=load_wait_milliseconds)

DownloadMultiQueryResults: Downloads the results of a custom query-set as one file

Exports the results of all the queries of a custom query-set (other than those which are not external results) as one file. Queries that failed, or were skipped as a query they depend on failed, are left out - though if none succeeded there is nothing to export.  The following error codes are to be anticipated most with standard Problem Detail reports: - 400 BadRequest : no query succeeded, or a placeholder or Drive parameter was incorrect in some way - 401 Unauthorized - 403 Forbidden - 404 Not Found : The requested query-set doesn't exist, isn't a custom one, or the calling user did not run it. - 429 Too Many Requests : Please try your request again soon   1. The query has been executed successfully in the past yet the server-instance receiving this request (e.g. from a load balancer) doesn't yet have this data available.   1. By virtue of the request you have just placed this will have started to load from the persisted cache and will soon be available.   1. It is also the case that the original server-instance to process the original query is likely to already be able to service this request.

### Example

```python
api_instance = api_client_factory.build(MultiQueryExecutionApi)
execution_id = 'execution_id_example' # str
format = luminesce.ExportType() # ExportType (optional)
file_name = 'file_name_example' # str (optional)
date_time_format = 'date_time_format_example' # str (optional)
load_wait_milliseconds = 0 # int (optional)
api_response = api_instance.download_multi_query_results(execution_id, format=format, file_name=file_name, date_time_format=date_time_format, load_wait_milliseconds=load_wait_milliseconds)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **execution_id** | **str**| ExecutionId returned when starting the query-set | [required] 
 **format** | [**ExportType**](../model/.md)| Format to download in.  Several results are one worksheet each for Excel, one table each for Sqlite, and otherwise one file each within a zip. | [optional] 
 **file_name** | **str**| Name of the file (without extension).  Defaults to &#x60;{executionId}&#x60;. May contain the placeholders &#x60;{executionId}&#x60;, &#x60;{date:format}&#x60; (when the queries started, UTC, e.g. &#x60;{date:yyyyMMdd}&#x60;) and &#x60;{param:name}&#x60; (the value of a scalar parameter). | [optional] 
 **date_time_format** | **str**| Format to apply for DateTime data, leaving blank gives the Luminesce Exporter default, currently &#x60;yyyy-MM-dd HH:mm:ss.fff&#x60; | [optional] 
 **load_wait_milliseconds** | **int**| Optional maximum additional wait period for post execution platform processing. | [optional] [default to 0]

### Return type

**bytes**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |

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

[**BackgroundMultiQueryProgressResponse**](../model/BackgroundMultiQueryProgressResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **list_custom_queries**
> List[CustomMultiQueryListItem] listCustomQueries = list_custom_queries(sql_like=sql_like)

ListCustomQueries: List the custom query-sets available to the calling user

Lists the custom query-sets (started by the calling user via `custom`) that have finished with at least one result which may be fetched,  and which have not yet passed their `keepForSeconds` time, most recent first.  Each lists its queries that are external results, and which of those have results. Those that errored are included, as some of their queries may still have succeeded.  The following error codes are to be anticipated most with standard Problem Detail reports: - 401 Unauthorized

### Example

```python
api_instance = api_client_factory.build(MultiQueryExecutionApi)
sql_like = 'sql_like_example' # str (optional)
api_response = api_instance.list_custom_queries(sql_like=sql_like)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sql_like** | **str**| An optional SQL-LIKE style filter on the LuminesceSql of the queries (manually include wildcards if desired), a query-set matching should any of its queries. | [optional] 

### Return type

[**List[CustomMultiQueryListItem]**](../model/CustomMultiQueryListItem.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **save_multi_query_results_to_drive**
> str saveMultiQueryResultsToDrive = save_multi_query_results_to_drive(execution_id, drive_location_and_file_name, may_overwrite=may_overwrite, format=format, drive_template_location=drive_template_location, date_time_format=date_time_format, load_wait_milliseconds=load_wait_milliseconds)

SaveMultiQueryResultsToDrive: Saves the results of a custom query-set directly to Drive, as one file

Exports the results of all the queries of a custom query-set (other than those which are not external results) as one file. Queries that failed, or were skipped as a query they depend on failed, are left out - though if none succeeded there is nothing to export.  The following error codes are to be anticipated most with standard Problem Detail reports: - 400 BadRequest : no query succeeded, or a placeholder or Drive parameter was incorrect in some way - 401 Unauthorized - 403 Forbidden - 404 Not Found : The requested query-set doesn't exist, isn't a custom one, or the calling user did not run it. - 429 Too Many Requests : Please try your request again soon   1. The query has been executed successfully in the past yet the server-instance receiving this request (e.g. from a load balancer) doesn't yet have this data available.   1. By virtue of the request you have just placed this will have started to load from the persisted cache and will soon be available.   1. It is also the case that the original server-instance to process the original query is likely to already be able to service this request.

### Example

```python
api_instance = api_client_factory.build(MultiQueryExecutionApi)
execution_id = 'execution_id_example' # str
drive_location_and_file_name = 'drive_location_and_file_name_example' # str
may_overwrite = False # bool (optional)
format = luminesce.ExportType() # ExportType (optional)
drive_template_location = 'drive_template_location_example' # str (optional)
date_time_format = 'date_time_format_example' # str (optional)
load_wait_milliseconds = 0 # int (optional)
api_response = api_instance.save_multi_query_results_to_drive(execution_id, drive_location_and_file_name, may_overwrite=may_overwrite, format=format, drive_template_location=drive_template_location, date_time_format=date_time_format, load_wait_milliseconds=load_wait_milliseconds)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **execution_id** | **str**| ExecutionId returned when starting the query-set | [required] 
 **drive_location_and_file_name** | **str**| Location and file name within drive where this should be saved to. Missing paths will be created, and extension (if given) will be ignored and inferred from the chosen format (zip where several results are zipped). May contain the placeholders &#x60;{executionId}&#x60;, &#x60;{date:format}&#x60; (when the queries started, UTC, e.g. &#x60;{date:yyyyMMdd}&#x60;) and &#x60;{param:name}&#x60; (the value of a scalar parameter). | [required] 
 **may_overwrite** | **bool**| If there is an existing file at the requested location with the same name should this be overridden, or an error returned? | [optional] [default to False]
 **format** | [**ExportType**](../model/.md)| Format to save in.  Several results are one worksheet each for Excel, one table each for Sqlite, and otherwise one file each within a zip. | [optional] 
 **drive_template_location** | **str**| Drive path and full file name including extension to be used for the export. Only some export types support templates, such as Excel and Pdf, and this will need to match the format type, if given. | [optional] 
 **date_time_format** | **str**| Format to apply for DateTime data, leaving blank gives the Luminesce Exporter default, currently &#x60;yyyy-MM-dd HH:mm:ss.fff&#x60; | [optional] 
 **load_wait_milliseconds** | **int**| Optional maximum additional wait period for post execution platform processing. | [optional] [default to 0]

### Return type

**str**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **start_custom_queries**
> BackgroundMultiQueryResponse startCustomQueries = start_custom_queries(custom_multi_query_request)

StartCustomQueries: Run a caller-supplied set of Sql queries in the background

 Starts a caller-supplied set of named queries in the background, getting back an immediate response with how to - fetch the data of each (external) query in various formats, view progress information and cancel / clear them, as for any multi-query - download, or save to Drive, the results of all the (external) queries that succeeded as one file  The queries are started in the order given, at most `maxInParallel` at a time (1 by default, null for as many as possible). A query may use the results of an earlier one as a table variable of its name, e.g. `select * from @Holdings`, and is then only started once that has succeeded (and is skipped if it does not).  The scalar parameters are given to every query.  The multi-query as a whole is reported as failed if any of its queries fails or is skipped.  Rather than giving the `queries`, `queriesFromWorkspace` may name a custom multi-query saved in the Workspaces API to take them from, e.g. `shared/SomeWorkspace/items/sets/SomeSet`. It is read when the request is made, so it runs as it is saved at that time. Whichever of `maxInParallel`, `timeoutSeconds`, `keepForSeconds` and `queryName` the request does not give are taken from it, as are the scalar parameter values saved with it for any the request does not give.  Given an `export`, the results of the (external) queries are saved to Drive as one file once they are done, as by `{executionId}/drive`, before the multi-query is reported as done: the progress's `export.savedTo` is then the Drive path of the file (or `export.error` why it was not saved). By default nothing is saved if any query did not succeed, unless `export.whenSomeFail` is set (the multi-query is reported as failed either way), and the multi-query is reported as failed if the file could not be saved. Its results may still be saved via `{executionId}/drive` too, as often as wanted. With `queriesFromWorkspace`, whatever the `export` leaves unspecified is taken from the export settings saved with it.  An explicit `executionId` already in use (by a multi-query of the caller's that is running, or whose results are still kept) is a conflict, rather than it being started again: so a caller may rejoin one it started by its `executionId`, e.g. after it was itself restarted.  The following error codes are to be anticipated with standard Problem Detail reports: - 400 BadRequest - the request was invalid, its queries could not be loaded from Workspaces, a Saved Query could not be loaded, or there was something wrong with the syntax of a query - 401 Unauthorized - 403 Forbidden - 409 Conflict - the `executionId` given is already in use (not a Problem Detail report) 

### Example

```python
api_instance = api_client_factory.build(MultiQueryExecutionApi)
custom_multi_query_request = CustomMultiQueryRequest()
api_response = api_instance.start_custom_queries(custom_multi_query_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **custom_multi_query_request** | [**CustomMultiQueryRequest**](../model/CustomMultiQueryRequest.md)| The queries to run (as LuminesceSql or Saved Query references), the scalar parameters for them all, etc. | [required] 

### Return type

[**BackgroundMultiQueryResponse**](../model/BackgroundMultiQueryResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**409** | Conflict |  -  |

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
 **type** | [**MultiQueryDefinitionType**](../model/.md)| An enum value defining the set of statements being executed | [required] 
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

[**BackgroundMultiQueryResponse**](../model/BackgroundMultiQueryResponse.md)

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

