# luminesce.SqlExecutionApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_by_query_csv**](SqlExecutionApi.md#get_by_query_csv) | **GET** /honeycomb/api/Sql/csv/{query} | GetByQueryCsv: Execute Sql from the url returning CSV
[**get_by_query_excel**](SqlExecutionApi.md#get_by_query_excel) | **GET** /honeycomb/api/Sql/excel/{query} | GetByQueryExcel: Execute Sql from the url returning an Excel file
[**get_by_query_json**](SqlExecutionApi.md#get_by_query_json) | **GET** /honeycomb/api/Sql/json/{query} | GetByQueryJson: Execute Sql from the url returning JSON
[**get_by_query_parquet**](SqlExecutionApi.md#get_by_query_parquet) | **GET** /honeycomb/api/Sql/parquet/{query} | GetByQueryParquet: Execute Sql from the url returning a Parquet file
[**get_by_query_pipe**](SqlExecutionApi.md#get_by_query_pipe) | **GET** /honeycomb/api/Sql/pipe/{query} | GetByQueryPipe: Execute Sql from the url returning pipe-delimited
[**get_by_query_sqlite**](SqlExecutionApi.md#get_by_query_sqlite) | **GET** /honeycomb/api/Sql/sqlite/{query} | GetByQuerySqlite: Execute Sql from the url returning SqLite DB
[**get_by_query_xml**](SqlExecutionApi.md#get_by_query_xml) | **GET** /honeycomb/api/Sql/xml/{query} | GetByQueryXml: Execute Sql from the url returning XML
[**put_by_query_csv**](SqlExecutionApi.md#put_by_query_csv) | **PUT** /honeycomb/api/Sql/csv | PutByQueryCsv: Execute Sql from the body returning CSV
[**put_by_query_excel**](SqlExecutionApi.md#put_by_query_excel) | **PUT** /honeycomb/api/Sql/excel | PutByQueryExcel: Execute Sql from the body making an Excel file
[**put_by_query_json**](SqlExecutionApi.md#put_by_query_json) | **PUT** /honeycomb/api/Sql/json | PutByQueryJson: Execute Sql from the body returning JSON
[**put_by_query_parquet**](SqlExecutionApi.md#put_by_query_parquet) | **PUT** /honeycomb/api/Sql/parquet | PutByQueryParquet: Execute Sql from the body making a Parquet file
[**put_by_query_pipe**](SqlExecutionApi.md#put_by_query_pipe) | **PUT** /honeycomb/api/Sql/pipe | PutByQueryPipe: Execute Sql from the body making pipe-delimited
[**put_by_query_sqlite**](SqlExecutionApi.md#put_by_query_sqlite) | **PUT** /honeycomb/api/Sql/sqlite | PutByQuerySqlite: Execute Sql from the body returning SqLite DB
[**put_by_query_xml**](SqlExecutionApi.md#put_by_query_xml) | **PUT** /honeycomb/api/Sql/xml | PutByQueryXml: Execute Sql from the body returning XML


### Example

```python
from finbourne.sdk.exceptions import ApiException
from finbourne.sdk.extensions.configuration_options import ConfigurationOptions
from finbourne.sdk.services.luminesce.models import *

from finbourne.sdk.extensions import (
  SyncApiClientFactory
)

from finbourne.sdk.services.luminesce.api.sql_execution_api import SqlExecutionApi

# opts = ConfigurationOptions()
# opts.total_timeout_ms = 30_000

# uncomment the below to use an api client factory with overrides
# api_client_factory = SyncApiClientFactory(opts=opts)

api_client_factory = SyncApiClientFactory()
api_instance = api_client_factory.build(SqlExecutionApi)
```

---

# **get_by_query_csv**
> str getByQueryCsv = get_by_query_csv(query, scalar_parameters=scalar_parameters, query_name=query_name, download=download, timeout=timeout, delimiter=delimiter, escape=escape, date_time_format=date_time_format)

GetByQueryCsv: Execute Sql from the url returning CSV

 Returns data from a simple single-line query execution which is specified on the url. e.g. `select ^ from Sys.Field order by 1, 2`, returned in the format of the method name.  The following error codes are to be anticipated with standard Problem Detail reports: - 400 BadRequest - something failed with the execution or parsing of your query - 401 Unauthorized - 403 Forbidden 

### Example

```python
api_instance = api_client_factory.build(SqlExecutionApi)
query = 'select ^ from Sys.Field order by 1, 2' # str
scalar_parameters = {'key': '{\"someParameter\":12,\"someOtherParameter\":\"someValue\"}'} # Dict[str, str] (optional)
query_name = 'Get tables/fields' # str (optional)
download = False # bool (optional)
timeout = 0 # int (optional)
delimiter = 'delimiter_example' # str (optional)
escape = 'escape_example' # str (optional)
date_time_format = 'date_time_format_example' # str (optional)
api_response = api_instance.get_by_query_csv(query, scalar_parameters=scalar_parameters, query_name=query_name, download=download, timeout=timeout, delimiter=delimiter, escape=escape, date_time_format=date_time_format)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| LuminesceSql to Execute (must be one line only) | [required] 
 **scalar_parameters** | [**Dict[str, str]**](str.md)| Json encoded dictionary of key-value pairs for scalar parameter values to use in the sql execution. | [optional] 
 **query_name** | **str**| Name to apply to the query in logs and &#x60;Sys.Logs.HcQueryStart&#x60; | [optional] 
 **download** | **bool**| Makes this a file-download request (as opposed to returning the data in the response-body) | [optional] [default to False]
 **timeout** | **int**| In seconds: &lt;0 or &gt; 175 → 175s (Maximum allowed), 0 → 120s | [optional] [default to 0]
 **delimiter** | **str**| Delimiter string to override the default | [optional] 
 **escape** | **str**| Escape character to override the default | [optional] 
 **date_time_format** | **str**| Format to apply for DateTime data, leaving blank gives the Luminesce Exporter default, currently &#x60;yyyy-MM-dd HH:mm:ss.fff&#x60; | [optional] 

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

# **get_by_query_excel**
> bytes getByQueryExcel = get_by_query_excel(query, scalar_parameters=scalar_parameters, query_name=query_name, date_time_format=date_time_format, timeout=timeout)

GetByQueryExcel: Execute Sql from the url returning an Excel file

 Returns data from a simple single-line query execution which is specified on the url. e.g. `select ^ from Sys.Field order by 1, 2`, returned in the format of the method name.  The following error codes are to be anticipated with standard Problem Detail reports: - 400 BadRequest - something failed with the execution or parsing of your query - 401 Unauthorized - 403 Forbidden 

### Example

```python
api_instance = api_client_factory.build(SqlExecutionApi)
query = 'select ^ from Sys.Field order by 1, 2' # str
scalar_parameters = {'key': '{\"someParameter\":12,\"someOtherParameter\":\"someValue\"}'} # Dict[str, str] (optional)
query_name = 'Get tables/fields' # str (optional)
date_time_format = 'date_time_format_example' # str (optional)
timeout = 0 # int (optional)
api_response = api_instance.get_by_query_excel(query, scalar_parameters=scalar_parameters, query_name=query_name, date_time_format=date_time_format, timeout=timeout)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| LuminesceSql to Execute (must be one line only) | [required] 
 **scalar_parameters** | [**Dict[str, str]**](str.md)| Json encoded dictionary of key-value pairs for scalar parameter values to use in the sql execution. | [optional] 
 **query_name** | **str**| Name to apply to the query in logs and &#x60;Sys.Logs.HcQueryStart&#x60; | [optional] 
 **date_time_format** | **str**| Format to apply for DateTime data, leaving blank gives the Luminesce Exporter default, currently &#x60;yyyy-MM-dd HH:mm:ss.000&#x60; (Excel support for this is limited) | [optional] 
 **timeout** | **int**| In seconds: &lt;0 or &gt; 175 → 175s (Maximum allowed), 0 → 120s | [optional] [default to 0]

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

# **get_by_query_json**
> str getByQueryJson = get_by_query_json(query, scalar_parameters=scalar_parameters, query_name=query_name, timeout=timeout, json_proper=json_proper, include_lineage=include_lineage)

GetByQueryJson: Execute Sql from the url returning JSON

 Returns data from a simple single-line query execution which is specified on the url. e.g. `select ^ from Sys.Field order by 1, 2`, returned in the format of the method name.  The following error codes are to be anticipated with standard Problem Detail reports: - 400 BadRequest - something failed with the execution or parsing of your query - 401 Unauthorized - 403 Forbidden 

### Example

```python
api_instance = api_client_factory.build(SqlExecutionApi)
query = 'select ^ from Sys.Field order by 1, 2' # str
scalar_parameters = {'key': '{\"someParameter\":12,\"someOtherParameter\":\"someValue\"}'} # Dict[str, str] (optional)
query_name = 'Get tables/fields' # str (optional)
timeout = 0 # int (optional)
json_proper = False # bool (optional)
include_lineage = False # bool (optional)
api_response = api_instance.get_by_query_json(query, scalar_parameters=scalar_parameters, query_name=query_name, timeout=timeout, json_proper=json_proper, include_lineage=include_lineage)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| LuminesceSql to Execute (must be one line only) | [required] 
 **scalar_parameters** | [**Dict[str, str]**](str.md)| Json encoded dictionary of key-value pairs for scalar parameter values to use in the sql execution. | [optional] 
 **query_name** | **str**| Name to apply to the query in logs and &#x60;Sys.Logs.HcQueryStart&#x60; | [optional] 
 **timeout** | **int**| In seconds: &lt;0 or &gt; 175 → 175s (Maximum allowed), 0 → 120s | [optional] [default to 0]
 **json_proper** | **bool**| Should this be text/json (not json-encoded-as-a-string) | [optional] [default to False]
 **include_lineage** | **bool**| Should lineage be included? If true this will be &#x60;properJson&#x60; and the jsonProper flag ignored | [optional] [default to False]

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

# **get_by_query_parquet**
> bytes getByQueryParquet = get_by_query_parquet(query, scalar_parameters=scalar_parameters, query_name=query_name, timeout=timeout)

GetByQueryParquet: Execute Sql from the url returning a Parquet file

 Returns data from a simple single-line query execution which is specified on the url. e.g. `select ^ from Sys.Field order by 1, 2`, returned in the format of the method name.  The following error codes are to be anticipated with standard Problem Detail reports: - 400 BadRequest - something failed with the execution or parsing of your query - 401 Unauthorized - 403 Forbidden 

### Example

```python
api_instance = api_client_factory.build(SqlExecutionApi)
query = 'select ^ from Sys.Field order by 1, 2' # str
scalar_parameters = {'key': '{\"someParameter\":12,\"someOtherParameter\":\"someValue\"}'} # Dict[str, str] (optional)
query_name = 'Get tables/fields' # str (optional)
timeout = 0 # int (optional)
api_response = api_instance.get_by_query_parquet(query, scalar_parameters=scalar_parameters, query_name=query_name, timeout=timeout)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| LuminesceSql to Execute (must be one line only) | [required] 
 **scalar_parameters** | [**Dict[str, str]**](str.md)| Json encoded dictionary of key-value pairs for scalar parameter values to use in the sql execution. | [optional] 
 **query_name** | **str**| Name to apply to the query in logs and &#x60;Sys.Logs.HcQueryStart&#x60; | [optional] 
 **timeout** | **int**| In seconds: &lt;0 or &gt; 175 → 175s (Maximum allowed), 0 → 120s | [optional] [default to 0]

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

# **get_by_query_pipe**
> str getByQueryPipe = get_by_query_pipe(query, scalar_parameters=scalar_parameters, query_name=query_name, download=download, date_time_format=date_time_format, timeout=timeout)

GetByQueryPipe: Execute Sql from the url returning pipe-delimited

 Returns data from a simple single-line query execution which is specified on the url. e.g. `select ^ from Sys.Field order by 1, 2`, returned in the format of the method name.  The following error codes are to be anticipated with standard Problem Detail reports: - 400 BadRequest - something failed with the execution or parsing of your query - 401 Unauthorized - 403 Forbidden 

### Example

```python
api_instance = api_client_factory.build(SqlExecutionApi)
query = 'select ^ from Sys.Field order by 1, 2' # str
scalar_parameters = {'key': '{\"someParameter\":12,\"someOtherParameter\":\"someValue\"}'} # Dict[str, str] (optional)
query_name = 'Get tables/fields' # str (optional)
download = False # bool (optional)
date_time_format = 'date_time_format_example' # str (optional)
timeout = 0 # int (optional)
api_response = api_instance.get_by_query_pipe(query, scalar_parameters=scalar_parameters, query_name=query_name, download=download, date_time_format=date_time_format, timeout=timeout)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| LuminesceSql to Execute (must be one line only) | [required] 
 **scalar_parameters** | [**Dict[str, str]**](str.md)| Json encoded dictionary of key-value pairs for scalar parameter values to use in the sql execution. | [optional] 
 **query_name** | **str**| Name to apply to the query in logs and &#x60;Sys.Logs.HcQueryStart&#x60; | [optional] 
 **download** | **bool**| Makes this a file-download request (as opposed to returning the data in the response-body) | [optional] [default to False]
 **date_time_format** | **str**| Format to apply for DateTime data, leaving blank gives the Luminesce Exporter default, currently &#x60;yyyy-MM-dd HH:mm:ss.fff&#x60; | [optional] 
 **timeout** | **int**| In seconds: &lt;0 or &gt; 175 → 175s (Maximum allowed), 0 → 120s | [optional] [default to 0]

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

# **get_by_query_sqlite**
> bytes getByQuerySqlite = get_by_query_sqlite(query, scalar_parameters=scalar_parameters, query_name=query_name, timeout=timeout)

GetByQuerySqlite: Execute Sql from the url returning SqLite DB

 Returns data from a simple single-line query execution which is specified on the url. e.g. `select ^ from Sys.Field order by 1, 2`, returned in the format of the method name.  The following error codes are to be anticipated with standard Problem Detail reports: - 400 BadRequest - something failed with the execution or parsing of your query - 401 Unauthorized - 403 Forbidden 

### Example

```python
api_instance = api_client_factory.build(SqlExecutionApi)
query = 'select ^ from Sys.Field order by 1, 2' # str
scalar_parameters = {'key': '{\"someParameter\":12,\"someOtherParameter\":\"someValue\"}'} # Dict[str, str] (optional)
query_name = 'Get tables/fields' # str (optional)
timeout = 0 # int (optional)
api_response = api_instance.get_by_query_sqlite(query, scalar_parameters=scalar_parameters, query_name=query_name, timeout=timeout)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| LuminesceSql to Execute (must be one line only) | [required] 
 **scalar_parameters** | [**Dict[str, str]**](str.md)| Json encoded dictionary of key-value pairs for scalar parameter values to use in the sql execution. | [optional] 
 **query_name** | **str**| Name to apply to the query in logs and &#x60;Sys.Logs.HcQueryStart&#x60; | [optional] 
 **timeout** | **int**| In seconds: &lt;0 or &gt; 175 → 175s (Maximum allowed), 0 → 120s | [optional] [default to 0]

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

# **get_by_query_xml**
> str getByQueryXml = get_by_query_xml(query, scalar_parameters=scalar_parameters, query_name=query_name, download=download, timeout=timeout)

GetByQueryXml: Execute Sql from the url returning XML

 Returns data from a simple single-line query execution which is specified on the url. e.g. `select ^ from Sys.Field order by 1, 2`, returned in the format of the method name.  The following error codes are to be anticipated with standard Problem Detail reports: - 400 BadRequest - something failed with the execution or parsing of your query - 401 Unauthorized - 403 Forbidden 

### Example

```python
api_instance = api_client_factory.build(SqlExecutionApi)
query = 'select ^ from Sys.Field order by 1, 2' # str
scalar_parameters = {'key': '{\"someParameter\":12,\"someOtherParameter\":\"someValue\"}'} # Dict[str, str] (optional)
query_name = 'Get tables/fields' # str (optional)
download = False # bool (optional)
timeout = 0 # int (optional)
api_response = api_instance.get_by_query_xml(query, scalar_parameters=scalar_parameters, query_name=query_name, download=download, timeout=timeout)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| LuminesceSql to Execute (must be one line only) | [required] 
 **scalar_parameters** | [**Dict[str, str]**](str.md)| Json encoded dictionary of key-value pairs for scalar parameter values to use in the sql execution. | [optional] 
 **query_name** | **str**| Name to apply to the query in logs and &#x60;Sys.Logs.HcQueryStart&#x60; | [optional] 
 **download** | **bool**| Makes this a file-download request (as opposed to returning the data in the response-body) | [optional] [default to False]
 **timeout** | **int**| In seconds: &lt;0 or &gt; 175 → 175s (Maximum allowed), 0 → 120s | [optional] [default to 0]

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

# **put_by_query_csv**
> str putByQueryCsv = put_by_query_csv(body, scalar_parameters=scalar_parameters, query_name=query_name, download=download, timeout_seconds=timeout_seconds, delimiter=delimiter, escape=escape, date_time_format=date_time_format)

PutByQueryCsv: Execute Sql from the body returning CSV

 For more complex LuminesceSql a PUT will allow for longer and line break delimited Sql, whic will be returned in the format of the method name. e.g.: ```sql @@cutoff = select #2020-02-01#; @issues = select Id, SortId, Summary, Created, Updated from Dev.Jira.Issue where Project='HC' and Created < @@cutoff and Updated > @@cutoff;  select i.Id, i.SortId, i.Summary, LinkText, LinkedIssueId, LinkedIssueSortId, LinkedIssueSummary from @issues i inner join Dev.Jira.Issue.Link li     on i.Id = li.IssueId ```  The following error codes are to be anticipated with standard Problem Detail reports: - 400 BadRequest - something failed with the execution or parsing of your query - 401 Unauthorized - 403 Forbidden 

### Example

```python
api_instance = api_client_factory.build(SqlExecutionApi)
body = select * from sys.field # str
scalar_parameters = {'key': '{\"someParameter\":12,\"someOtherParameter\":\"someValue\"}'} # Dict[str, str] (optional)
query_name = 'Get tables/fields' # str (optional)
download = False # bool (optional)
timeout_seconds = 0 # int (optional)
delimiter = 'delimiter_example' # str (optional)
escape = 'escape_example' # str (optional)
date_time_format = 'date_time_format_example' # str (optional)
api_response = api_instance.put_by_query_csv(body, scalar_parameters=scalar_parameters, query_name=query_name, download=download, timeout_seconds=timeout_seconds, delimiter=delimiter, escape=escape, date_time_format=date_time_format)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **str**| LuminesceSql to Execute (may be multi-line) | [required] 
 **scalar_parameters** | [**Dict[str, str]**](str.md)| Json encoded dictionary of key-value pairs for scalar parameter values to use in the sql execution. | [optional] 
 **query_name** | **str**| Name to apply to the query in logs and &#x60;Sys.Logs.HcQueryStart&#x60; | [optional] 
 **download** | **bool**| Makes this a file-download request (as opposed to returning the data in the response-body) | [optional] [default to False]
 **timeout_seconds** | **int**| In seconds: &lt;0 or &gt; 175 → 175s (Maximum allowed), 0 → 120s | [optional] [default to 0]
 **delimiter** | **str**| Delimiter string to override the default | [optional] 
 **escape** | **str**| Escape character to override the default | [optional] 
 **date_time_format** | **str**| Format to apply for DateTime data, leaving blank gives the Luminesce Exporter default, currently &#x60;yyyy-MM-dd HH:mm:ss.fff&#x60; | [optional] 

### Return type

**str**

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **put_by_query_excel**
> bytes putByQueryExcel = put_by_query_excel(body, scalar_parameters=scalar_parameters, query_name=query_name, date_time_format=date_time_format, timeout_seconds=timeout_seconds)

PutByQueryExcel: Execute Sql from the body making an Excel file

 For more complex LuminesceSql a PUT will allow for longer and line break delimited Sql, whic will be returned in the format of the method name. e.g.: ```sql @@cutoff = select #2020-02-01#; @issues = select Id, SortId, Summary, Created, Updated from Dev.Jira.Issue where Project='HC' and Created < @@cutoff and Updated > @@cutoff;  select i.Id, i.SortId, i.Summary, LinkText, LinkedIssueId, LinkedIssueSortId, LinkedIssueSummary from @issues i inner join Dev.Jira.Issue.Link li     on i.Id = li.IssueId ```  The following error codes are to be anticipated with standard Problem Detail reports: - 400 BadRequest - something failed with the execution or parsing of your query - 401 Unauthorized - 403 Forbidden 

### Example

```python
api_instance = api_client_factory.build(SqlExecutionApi)
body = select * from sys.field # str
scalar_parameters = {'key': '{\"someParameter\":12,\"someOtherParameter\":\"someValue\"}'} # Dict[str, str] (optional)
query_name = 'Get tables/fields' # str (optional)
date_time_format = 'date_time_format_example' # str (optional)
timeout_seconds = 0 # int (optional)
api_response = api_instance.put_by_query_excel(body, scalar_parameters=scalar_parameters, query_name=query_name, date_time_format=date_time_format, timeout_seconds=timeout_seconds)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **str**| LuminesceSql to Execute (may be multi-line) | [required] 
 **scalar_parameters** | [**Dict[str, str]**](str.md)| Json encoded dictionary of key-value pairs for scalar parameter values to use in the sql execution. | [optional] 
 **query_name** | **str**| Name to apply to the query in logs and &#x60;Sys.Logs.HcQueryStart&#x60; | [optional] 
 **date_time_format** | **str**| Format to apply for DateTime data, leaving blank gives the Luminesce Exporter default, currently &#x60;yyyy-MM-dd HH:mm:ss.000&#x60; (Excel support for this is limited) | [optional] 
 **timeout_seconds** | **int**| In seconds: &lt;0 or &gt; 175 → 175s (Maximum allowed), 0 → 120s | [optional] [default to 0]

### Return type

**bytes**

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **put_by_query_json**
> str putByQueryJson = put_by_query_json(body, scalar_parameters=scalar_parameters, query_name=query_name, timeout_seconds=timeout_seconds, json_proper=json_proper, include_lineage=include_lineage)

PutByQueryJson: Execute Sql from the body returning JSON

 For more complex LuminesceSql a PUT will allow for longer and line break delimited Sql, whic will be returned in the format of the method name. e.g.: ```sql @@cutoff = select #2020-02-01#; @issues = select Id, SortId, Summary, Created, Updated from Dev.Jira.Issue where Project='HC' and Created < @@cutoff and Updated > @@cutoff;  select i.Id, i.SortId, i.Summary, LinkText, LinkedIssueId, LinkedIssueSortId, LinkedIssueSummary from @issues i inner join Dev.Jira.Issue.Link li     on i.Id = li.IssueId ```  The following error codes are to be anticipated with standard Problem Detail reports: - 400 BadRequest - something failed with the execution or parsing of your query - 401 Unauthorized - 403 Forbidden 

### Example

```python
api_instance = api_client_factory.build(SqlExecutionApi)
body = select * from sys.field # str
scalar_parameters = {'key': '{\"someParameter\":12,\"someOtherParameter\":\"someValue\"}'} # Dict[str, str] (optional)
query_name = 'Get tables/fields' # str (optional)
timeout_seconds = 0 # int (optional)
json_proper = False # bool (optional)
include_lineage = False # bool (optional)
api_response = api_instance.put_by_query_json(body, scalar_parameters=scalar_parameters, query_name=query_name, timeout_seconds=timeout_seconds, json_proper=json_proper, include_lineage=include_lineage)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **str**| LuminesceSql to Execute (may be multi-line) | [required] 
 **scalar_parameters** | [**Dict[str, str]**](str.md)| Json encoded dictionary of key-value pairs for scalar parameter values to use in the sql execution. | [optional] 
 **query_name** | **str**| Name to apply to the query in logs and &#x60;Sys.Logs.HcQueryStart&#x60; | [optional] 
 **timeout_seconds** | **int**| In seconds: &lt;0 or &gt; 175 → 175s (Maximum allowed), 0 → 120s | [optional] [default to 0]
 **json_proper** | **bool**| Should this be text/json (not json-encoded-as-a-string) | [optional] [default to False]
 **include_lineage** | **bool**| Should lineage be included? If true this will be &#x60;properJson&#x60; and the jsonProper flag ignored | [optional] [default to False]

### Return type

**str**

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **put_by_query_parquet**
> bytes putByQueryParquet = put_by_query_parquet(body, scalar_parameters=scalar_parameters, query_name=query_name, timeout_seconds=timeout_seconds)

PutByQueryParquet: Execute Sql from the body making a Parquet file

 For more complex LuminesceSql a PUT will allow for longer and line break delimited Sql, whic will be returned in the format of the method name. e.g.: ```sql @@cutoff = select #2020-02-01#; @issues = select Id, SortId, Summary, Created, Updated from Dev.Jira.Issue where Project='HC' and Created < @@cutoff and Updated > @@cutoff;  select i.Id, i.SortId, i.Summary, LinkText, LinkedIssueId, LinkedIssueSortId, LinkedIssueSummary from @issues i inner join Dev.Jira.Issue.Link li     on i.Id = li.IssueId ```  The following error codes are to be anticipated with standard Problem Detail reports: - 400 BadRequest - something failed with the execution or parsing of your query - 401 Unauthorized - 403 Forbidden 

### Example

```python
api_instance = api_client_factory.build(SqlExecutionApi)
body = select * from sys.field # str
scalar_parameters = {'key': '{\"someParameter\":12,\"someOtherParameter\":\"someValue\"}'} # Dict[str, str] (optional)
query_name = 'Get tables/fields' # str (optional)
timeout_seconds = 0 # int (optional)
api_response = api_instance.put_by_query_parquet(body, scalar_parameters=scalar_parameters, query_name=query_name, timeout_seconds=timeout_seconds)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **str**| LuminesceSql to Execute (may be multi-line) | [required] 
 **scalar_parameters** | [**Dict[str, str]**](str.md)| Json encoded dictionary of key-value pairs for scalar parameter values to use in the sql execution. | [optional] 
 **query_name** | **str**| Name to apply to the query in logs and &#x60;Sys.Logs.HcQueryStart&#x60; | [optional] 
 **timeout_seconds** | **int**| In seconds: &lt;0 or &gt; 175 → 175s (Maximum allowed), 0 → 120s | [optional] [default to 0]

### Return type

**bytes**

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **put_by_query_pipe**
> str putByQueryPipe = put_by_query_pipe(body, scalar_parameters=scalar_parameters, query_name=query_name, download=download, date_time_format=date_time_format, timeout_seconds=timeout_seconds)

PutByQueryPipe: Execute Sql from the body making pipe-delimited

 For more complex LuminesceSql a PUT will allow for longer and line break delimited Sql, whic will be returned in the format of the method name. e.g.: ```sql @@cutoff = select #2020-02-01#; @issues = select Id, SortId, Summary, Created, Updated from Dev.Jira.Issue where Project='HC' and Created < @@cutoff and Updated > @@cutoff;  select i.Id, i.SortId, i.Summary, LinkText, LinkedIssueId, LinkedIssueSortId, LinkedIssueSummary from @issues i inner join Dev.Jira.Issue.Link li     on i.Id = li.IssueId ```  The following error codes are to be anticipated with standard Problem Detail reports: - 400 BadRequest - something failed with the execution or parsing of your query - 401 Unauthorized - 403 Forbidden 

### Example

```python
api_instance = api_client_factory.build(SqlExecutionApi)
body = select * from sys.field # str
scalar_parameters = {'key': '{\"someParameter\":12,\"someOtherParameter\":\"someValue\"}'} # Dict[str, str] (optional)
query_name = 'Get tables/fields' # str (optional)
download = False # bool (optional)
date_time_format = 'date_time_format_example' # str (optional)
timeout_seconds = 0 # int (optional)
api_response = api_instance.put_by_query_pipe(body, scalar_parameters=scalar_parameters, query_name=query_name, download=download, date_time_format=date_time_format, timeout_seconds=timeout_seconds)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **str**| LuminesceSql to Execute (may be multi-line) | [required] 
 **scalar_parameters** | [**Dict[str, str]**](str.md)| Json encoded dictionary of key-value pairs for scalar parameter values to use in the sql execution. | [optional] 
 **query_name** | **str**| Name to apply to the query in logs and &#x60;Sys.Logs.HcQueryStart&#x60; | [optional] 
 **download** | **bool**| Makes this a file-download request (as opposed to returning the data in the response-body) | [optional] [default to False]
 **date_time_format** | **str**| Format to apply for DateTime data, leaving blank gives the Luminesce Exporter default, currently &#x60;yyyy-MM-dd HH:mm:ss.fff&#x60; | [optional] 
 **timeout_seconds** | **int**| In seconds: &lt;0 or &gt; 175 → 175s (Maximum allowed), 0 → 120s | [optional] [default to 0]

### Return type

**str**

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **put_by_query_sqlite**
> bytes putByQuerySqlite = put_by_query_sqlite(body, scalar_parameters=scalar_parameters, query_name=query_name, timeout_seconds=timeout_seconds)

PutByQuerySqlite: Execute Sql from the body returning SqLite DB

 For more complex LuminesceSql a PUT will allow for longer and line break delimited Sql, whic will be returned in the format of the method name. e.g.: ```sql @@cutoff = select #2020-02-01#; @issues = select Id, SortId, Summary, Created, Updated from Dev.Jira.Issue where Project='HC' and Created < @@cutoff and Updated > @@cutoff;  select i.Id, i.SortId, i.Summary, LinkText, LinkedIssueId, LinkedIssueSortId, LinkedIssueSummary from @issues i inner join Dev.Jira.Issue.Link li     on i.Id = li.IssueId ```  The following error codes are to be anticipated with standard Problem Detail reports: - 400 BadRequest - something failed with the execution or parsing of your query - 401 Unauthorized - 403 Forbidden 

### Example

```python
api_instance = api_client_factory.build(SqlExecutionApi)
body = select * from sys.field # str
scalar_parameters = {'key': '{\"someParameter\":12,\"someOtherParameter\":\"someValue\"}'} # Dict[str, str] (optional)
query_name = 'Get tables/fields' # str (optional)
timeout_seconds = 0 # int (optional)
api_response = api_instance.put_by_query_sqlite(body, scalar_parameters=scalar_parameters, query_name=query_name, timeout_seconds=timeout_seconds)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **str**| LuminesceSql to Execute (may be multi-line) | [required] 
 **scalar_parameters** | [**Dict[str, str]**](str.md)| Json encoded dictionary of key-value pairs for scalar parameter values to use in the sql execution. | [optional] 
 **query_name** | **str**| Name to apply to the query in logs and &#x60;Sys.Logs.HcQueryStart&#x60; | [optional] 
 **timeout_seconds** | **int**| In seconds: &lt;0 or &gt; 175 → 175s (Maximum allowed), 0 → 120s | [optional] [default to 0]

### Return type

**bytes**

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **put_by_query_xml**
> str putByQueryXml = put_by_query_xml(body, scalar_parameters=scalar_parameters, query_name=query_name, download=download, timeout_seconds=timeout_seconds)

PutByQueryXml: Execute Sql from the body returning XML

 For more complex LuminesceSql a PUT will allow for longer and line break delimited Sql, whic will be returned in the format of the method name. e.g.: ```sql @@cutoff = select #2020-02-01#; @issues = select Id, SortId, Summary, Created, Updated from Dev.Jira.Issue where Project='HC' and Created < @@cutoff and Updated > @@cutoff;  select i.Id, i.SortId, i.Summary, LinkText, LinkedIssueId, LinkedIssueSortId, LinkedIssueSummary from @issues i inner join Dev.Jira.Issue.Link li     on i.Id = li.IssueId ```  The following error codes are to be anticipated with standard Problem Detail reports: - 400 BadRequest - something failed with the execution or parsing of your query - 401 Unauthorized - 403 Forbidden 

### Example

```python
api_instance = api_client_factory.build(SqlExecutionApi)
body = select * from sys.field # str
scalar_parameters = {'key': '{\"someParameter\":12,\"someOtherParameter\":\"someValue\"}'} # Dict[str, str] (optional)
query_name = 'Get tables/fields' # str (optional)
download = False # bool (optional)
timeout_seconds = 0 # int (optional)
api_response = api_instance.put_by_query_xml(body, scalar_parameters=scalar_parameters, query_name=query_name, download=download, timeout_seconds=timeout_seconds)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **str**| LuminesceSql to Execute (may be multi-line) | [required] 
 **scalar_parameters** | [**Dict[str, str]**](str.md)| Json encoded dictionary of key-value pairs for scalar parameter values to use in the sql execution. | [optional] 
 **query_name** | **str**| Name to apply to the query in logs and &#x60;Sys.Logs.HcQueryStart&#x60; | [optional] 
 **download** | **bool**| Makes this a file-download request (as opposed to returning the data in the response-body) | [optional] [default to False]
 **timeout_seconds** | **int**| In seconds: &lt;0 or &gt; 175 → 175s (Maximum allowed), 0 → 120s | [optional] [default to 0]

### Return type

**str**

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

