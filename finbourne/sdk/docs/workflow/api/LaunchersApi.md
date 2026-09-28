# workflow.LaunchersApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_launcher**](LaunchersApi.md#create_launcher) | **POST** /workflow/api/workflows/{scope}/{code}/launchers | [EXPERIMENTAL] CreateLauncher: Create a new Launcher on a Workflow
[**delete_launcher**](LaunchersApi.md#delete_launcher) | **DELETE** /workflow/api/workflows/{scope}/{code}/launchers/{launcherId} | [EXPERIMENTAL] DeleteLauncher: Delete a Launcher of a Workflow
[**get_launcher**](LaunchersApi.md#get_launcher) | **GET** /workflow/api/workflows/{scope}/{code}/launchers/{launcherId} | [EXPERIMENTAL] GetLauncher: Get a Launcher of a Workflow
[**list_launchers**](LaunchersApi.md#list_launchers) | **GET** /workflow/api/workflows/{scope}/{code}/launchers | [EXPERIMENTAL] ListLaunchers: List the Launchers of a Workflow
[**update_launcher**](LaunchersApi.md#update_launcher) | **PUT** /workflow/api/workflows/{scope}/{code}/launchers/{launcherId} | [EXPERIMENTAL] UpdateLauncher: Update an existing Launcher of a Workflow


### Example

```python
from finbourne.sdk.exceptions import ApiException
from finbourne.sdk.extensions.configuration_options import ConfigurationOptions
from finbourne.sdk.services.workflow.models import *

from finbourne.sdk.extensions import (
  SyncApiClientFactory
)

from finbourne.sdk.services.workflow.api.launchers_api import LaunchersApi

# opts = ConfigurationOptions()
# opts.total_timeout_ms = 30_000

# uncomment the below to use an api client factory with overrides
# api_client_factory = SyncApiClientFactory(opts=opts)

api_client_factory = SyncApiClientFactory()
api_instance = api_client_factory.build(LaunchersApi)
```

---

# **create_launcher**
> LauncherResponse createLauncher = create_launcher(scope, code, create_launcher_request)

[EXPERIMENTAL] CreateLauncher: Create a new Launcher on a Workflow

### Example

```python
api_instance = api_client_factory.build(LaunchersApi)
scope = 'scope_example' # str
code = 'code_example' # str
create_launcher_request = CreateLauncherRequest()
api_response = api_instance.create_launcher(scope, code, create_launcher_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope that identifies the Workflow that owns the Launcher | [required] 
 **code** | **str**| The code that identifies the Workflow that owns the Launcher | [required] 
 **create_launcher_request** | [**CreateLauncherRequest**](../model/CreateLauncherRequest.md)| The data to create a Launcher | [required] 

### Return type

[**LauncherResponse**](../model/LauncherResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | The details of the input related failure |  -  |
**404** | Workflow not found. |  -  |
**409** | Launcher already exists. |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **delete_launcher**
> DeletedEntityResponse deleteLauncher = delete_launcher(scope, code, launcher_id)

[EXPERIMENTAL] DeleteLauncher: Delete a Launcher of a Workflow

If the Launcher does not exist a failure will be returned

### Example

```python
api_instance = api_client_factory.build(LaunchersApi)
scope = 'scope_example' # str
code = 'code_example' # str
launcher_id = 'launcher_id_example' # str
api_response = api_instance.delete_launcher(scope, code, launcher_id)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope that identifies the Workflow that owns the Launcher | [required] 
 **code** | **str**| The code that identifies the Workflow that owns the Launcher | [required] 
 **launcher_id** | **str**| The identifier of the Launcher inside its Workflow | [required] 

### Return type

[**DeletedEntityResponse**](../model/DeletedEntityResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | The details of the input related failure |  -  |
**404** | Launcher not found. |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_launcher**
> LauncherResponse getLauncher = get_launcher(scope, code, launcher_id, as_at=as_at)

[EXPERIMENTAL] GetLauncher: Get a Launcher of a Workflow

### Example

```python
api_instance = api_client_factory.build(LaunchersApi)
scope = 'scope_example' # str
code = 'code_example' # str
launcher_id = 'launcher_id_example' # str
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
api_response = api_instance.get_launcher(scope, code, launcher_id, as_at=as_at)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope that identifies the Workflow that owns the Launcher | [required] 
 **code** | **str**| The code that identifies the Workflow that owns the Launcher | [required] 
 **launcher_id** | **str**| The identifier of the Launcher inside its Workflow | [required] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the Launcher. Defaults to returning the latest             version if not specified. | [optional] 

### Return type

[**LauncherResponse**](../model/LauncherResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | The details of the input related failure |  -  |
**404** | Launcher not found. |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **list_launchers**
> PagedResourceListOfLauncherResponse listLaunchers = list_launchers(scope, code, as_at=as_at, filter=filter, sort_by=sort_by, limit=limit, page=page)

[EXPERIMENTAL] ListLaunchers: List the Launchers of a Workflow

### Example

```python
api_instance = api_client_factory.build(LaunchersApi)
scope = 'scope_example' # str
code = 'code_example' # str
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
filter = 'filter_example' # str (optional)
sort_by = ['sort_by_example'] # List[str] (optional)
limit = 10 # int (optional)
page = 'page_example' # str (optional)
api_response = api_instance.list_launchers(scope, code, as_at=as_at, filter=filter, sort_by=sort_by, limit=limit, page=page)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope that identifies the Workflow that owns the Launchers | [required] 
 **code** | **str**| The code that identifies the Workflow that owns the Launchers | [required] 
 **as_at** | **datetime**| The asAt datetime at which to list the Launchers. Defaults to return the latest version             of each Launcher if not specified. | [optional] 
 **filter** | **str**| Expression to filter the result set. Read more about filtering results from LUSID here:             https://support.lusid.com/filtering-results-from-lusid. | [optional] 
 **sort_by** | [**List[str]**](../model/str.md)| A list of field names to sort by, each suffixed by \&quot; ASC\&quot; or \&quot; DESC\&quot;. Defaults to             \&quot;launcherId ASC\&quot; if not specified. | [optional] 
 **limit** | **int**| When paginating, limit the number of returned results to this many. | [optional] [default to 10]
 **page** | **str**| The pagination token to use to continue listing Launchers from a previous call to list             Launchers. This value is returned from the previous call. If a pagination token is provided the sortBy,             filter, and asAt fields must not have changed since the original request. | [optional] 

### Return type

[**PagedResourceListOfLauncherResponse**](../model/PagedResourceListOfLauncherResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | The details of the input related failure |  -  |
**404** | Workflow not found. |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **update_launcher**
> LauncherResponse updateLauncher = update_launcher(scope, code, launcher_id, update_launcher_request)

[EXPERIMENTAL] UpdateLauncher: Update an existing Launcher of a Workflow

The type of a Launcher cannot be changed

### Example

```python
api_instance = api_client_factory.build(LaunchersApi)
scope = 'scope_example' # str
code = 'code_example' # str
launcher_id = 'launcher_id_example' # str
update_launcher_request = UpdateLauncherRequest()
api_response = api_instance.update_launcher(scope, code, launcher_id, update_launcher_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope that identifies the Workflow that owns the Launcher | [required] 
 **code** | **str**| The code that identifies the Workflow that owns the Launcher | [required] 
 **launcher_id** | **str**| The identifier of the Launcher inside its Workflow | [required] 
 **update_launcher_request** | [**UpdateLauncherRequest**](../model/UpdateLauncherRequest.md)| The data to update a Launcher | [required] 

### Return type

[**LauncherResponse**](../model/LauncherResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | The details of the input related failure |  -  |
**404** | Launcher not found. |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

