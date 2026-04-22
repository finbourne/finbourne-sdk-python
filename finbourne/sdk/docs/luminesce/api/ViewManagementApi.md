# luminesce.ViewManagementApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_view**](ViewManagementApi.md#delete_view) | **DELETE** /honeycomb/api/View/update | [EXPERIMENTAL] DeleteView: Deletes a view by name
[**get_view_creation_sql**](ViewManagementApi.md#get_view_creation_sql) | **PUT** /honeycomb/api/View/sql | [EXPERIMENTAL] GetViewCreationSql: Gets the original source Sql for a view (if available)
[**list_views**](ViewManagementApi.md#list_views) | **GET** /honeycomb/api/View/list | [EXPERIMENTAL] ListViews: List views which are visible to the current user
[**upsert_view**](ViewManagementApi.md#upsert_view) | **PUT** /honeycomb/api/View/update | [EXPERIMENTAL] UpsertView: Creates or updates a view from a full ViewDefinition.


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

# **delete_view**
> str deleteView = delete_view(view_name=view_name)

[EXPERIMENTAL] DeleteView: Deletes a view by name

 Deletes a view.  This is primarily intended for use by an automated tool to synchronise views between domains.  The following error codes are to be anticipated with standard Problem Detail reports: - 401 Unauthorized - 403 Forbidden 

### Example

```python
api_instance = api_client_factory.build(ViewManagementApi)
view_name = 'view_name_example' # str (optional)
api_response = api_instance.delete_view(view_name=view_name)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **view_name** | **str**| View to delete | [optional] 

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
> List[ViewItem] listViews = list_views(show_all=show_all, reg_ex_filter=reg_ex_filter, name_like_filter=name_like_filter)

[EXPERIMENTAL] ListViews: List views which are visible to the current user

 Lists all the views which you have access to see. These come from directly from persisted files in the file system. Some limited filtering is available.  The following error codes are to be anticipated with standard Problem Detail reports: - 401 Unauthorized - 403 Forbidden 

### Example

```python
api_instance = api_client_factory.build(ViewManagementApi)
show_all = False # bool (optional)
reg_ex_filter = 'reg_ex_filter_example' # str (optional)
name_like_filter = 'name_like_filter_example' # str (optional)
api_response = api_instance.list_views(show_all=show_all, reg_ex_filter=reg_ex_filter, name_like_filter=name_like_filter)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **show_all** | **bool**| Show additional views if permissions allow | [optional] [default to False]
 **reg_ex_filter** | **str**| Regular Expression filter to reduce the number of views returned, it is applied to the view *content* (this filter is applied withing the Filesystem itself.) | [optional] 
 **name_like_filter** | **str**| SQL Like-style filter on the view name, to reduce the number of views returned (this filter is applied to the Filesystem-returned view list.) | [optional] 

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

---

# **upsert_view**
> str upsertView = upsert_view(allow_warnings=allow_warnings, may_update_existing=may_update_existing, view_item=view_item)

[EXPERIMENTAL] UpsertView: Creates or updates a view from a full ViewDefinition.

 Creates or updates a view from a full ViewDefinition.  Adds or creates a view from a view definition - without running the SQL of the view.  This is primarily intended for use by an automated tool to copy views between domains.  What this is *absolutely not* intended to do is to update views to tampered with definitions that were not originally created by `Sys.Admin.SetupView`, not even the smallest of changes are permitted as they may not work and will lead to additional support loads.  The flow for using fbn-config and these endpoints should generally be: - version control the `Sys.Admin.SetupView` query or the fbn-config resource that runs that query. - that can be automatically deployed to a development environment / domain. - an automated process then uses the `list` endpoint to get the full view definition (see above) from the dev-domain - then that definition can be given to a sit/uat/prod domain via this endpoint   - fbn-config could be responsible for this via a new resource type or simply a new, or any other script with PATs for both domains could be responsible for that)  The following error codes are to be anticipated with standard Problem Detail reports: - 401 Unauthorized - 403 Forbidden 

### Example

```python
api_instance = api_client_factory.build(ViewManagementApi)
allow_warnings = False # bool (optional)
may_update_existing = False # bool (optional)
view_item = ViewItem()
api_response = api_instance.upsert_view(allow_warnings=allow_warnings, may_update_existing=may_update_existing, view_item=view_item)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **allow_warnings** | **bool**| May views with *warnings* be upserted?  Regardless of this views with *errors* may not be. Warnings includes things like: - not using macros properly so that filters or aggregations cannot be passed down - using things like &#x60;select *&#x60; that can lead to results changing over time Errors includes things like: - uses a provider or view that simply doesn&#39;t exists (so perhaps a view this depends on needs creating first?) - The SQL or Metadata of the view was manually edited, not setup correctly by &#x60;Sys.Admin.SetupView&#x60; | [optional] [default to False]
 **may_update_existing** | **bool**| May an existing view be overwritten?  Defaults to false to prevent accidental overwrites. Set to true when intentionally deploying an updated view definition to a domain. | [optional] [default to False]
 **view_item** | [**ViewItem**](ViewItem.md)| View to create / change the definition of. | [optional] 

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

