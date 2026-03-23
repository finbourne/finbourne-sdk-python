# luminesce.ViewManagementApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_view_creation_sql**](ViewManagementApi.md#get_view_creation_sql) | **PUT** /honeycomb/api/View/sql | [EXPERIMENTAL] GetViewCreationSql: Gets the original source Sql for a view (if available)
[**list_views**](ViewManagementApi.md#list_views) | **GET** /honeycomb/api/View/list | [EXPERIMENTAL] ListViews: List views which are visible to the current users


### Example

```python
from finbourne.sdk.exceptions import ApiException
from finbourne.sdk.extensions.configuration_options import ConfigurationOptions
from finbourne.sdk.services.luminesce.models import *

from finbourne.sdk.extensions import (
  SyncApiClientFactory
)

from finbourne.sdk.services.luminesce.api.view_management_api import ViewManagementApi

# opts = ConfigurationOptions()
# opts.total_timeout_ms = 30_000

# uncomment the below to use an api client factory with overrides
# api_client_factory = SyncApiClientFactory(opts=opts)

api_client_factory = SyncApiClientFactory()
api_instance = api_client_factory.build(ViewManagementApi)
```

---

# **get_view_creation_sql**
> str getViewCreationSql = get_view_creation_sql(view_item=view_item)

[EXPERIMENTAL] GetViewCreationSql: Gets the original source Sql for a view (if available)

 Gets the original source Sql for a view (if available, 404 if not found in the logs)  The following error codes are to be anticipated with standard Problem Detail reports: - 401 Unauthorized - 403 Forbidden 

### Example

```python
api_instance = api_client_factory.build(ViewManagementApi)
view_item = ViewItem()
api_response = api_instance.get_view_creation_sql(view_item=view_item)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **view_item** | [**ViewItem**](ViewItem.md)| View to fetch the create SQL for. Only the LastUpdatedAt and LastUpdatedExecutionId properties are required. | [optional] 

### Return type

**str**

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **list_views**
> List[ViewItem] listViews = list_views(show_all=show_all, reg_ex_filter=reg_ex_filter)

[EXPERIMENTAL] ListViews: List views which are visible to the current users

 Lists all the views which you have access, some limited filtering is available. These come from directly from persisted files in the file system.  The following error codes are to be anticipated with standard Problem Detail reports: - 401 Unauthorized - 403 Forbidden 

### Example

```python
api_instance = api_client_factory.build(ViewManagementApi)
show_all = False # bool (optional)
reg_ex_filter = 'reg_ex_filter_example' # str (optional)
api_response = api_instance.list_views(show_all=show_all, reg_ex_filter=reg_ex_filter)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **show_all** | **bool**| Show additional views if permissions allow | [optional] [default to False]
 **reg_ex_filter** | **str**| Regular Expression filter to apply to the view content | [optional] 

### Return type

[**List[ViewItem]**](ViewItem.md)

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

