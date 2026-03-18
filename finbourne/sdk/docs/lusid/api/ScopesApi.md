# lusid.ScopesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_entity_scopes**](ScopesApi.md#list_entity_scopes) | **GET** /api/api/scopes/{entityType} | ListEntityScopes: List Entity Scopes
[**list_scopes**](ScopesApi.md#list_scopes) | **GET** /api/api/scopes | ListScopes: List Scopes


### Example

```python
from finbourne.sdk.exceptions import ApiException
from finbourne.sdk.extensions.configuration_options import ConfigurationOptions
from finbourne.sdk.services.lusid.models import *

from finbourne.sdk.extensions import (
  SyncApiClientFactory
)

from finbourne.sdk.services.lusid.api.scopes_api import ScopesApi

# opts = ConfigurationOptions()
# opts.total_timeout_ms = 30_000

# uncomment the below to use an api client factory with overrides
# api_client_factory = SyncApiClientFactory(opts=opts)

api_client_factory = SyncApiClientFactory()
api_instance = api_client_factory.build(ScopesApi)
```

---

# **list_entity_scopes**
> ResourceListOfScopeDefinition listEntityScopes = list_entity_scopes(entity_type, as_at=as_at, page=page, limit=limit)

ListEntityScopes: List Entity Scopes

List all the scopes for a given entity type that contain data.

### Example

```python
api_instance = api_client_factory.build(ScopesApi)
entity_type = 'entity_type_example' # str
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
page = 'page_example' # str (optional)
limit = 56 # int (optional)
api_response = api_instance.list_entity_scopes(entity_type, as_at=as_at, page=page, limit=limit)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_type** | **str**| The entity type to list scopes for. | [required] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve scopes. Defaults to latest datetime if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing scopes from a previous call to list scopes.              This value is returned from the previous call. If a pagination token is provided, the limit and asAt fields              must not have changed since the original request. | [optional] 
 **limit** | **int**| When paginating, limit the number of returned results to this number. Defaults to 100 if not specified. | [optional] 

### Return type

[**ResourceListOfScopeDefinition**](ResourceListOfScopeDefinition.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of scopes |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **list_scopes**
> ResourceListOfScopeDefinition listScopes = list_scopes(filter=filter)

ListScopes: List Scopes

List all the scopes that contain data.

### Example

```python
api_instance = api_client_factory.build(ScopesApi)
filter = 'filter_example' # str (optional)
api_response = api_instance.list_scopes(filter=filter)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Expression to filter the result set.              For example, to filter on the Scope, use \&quot;scope eq &#39;string&#39;\&quot;              Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. | [optional] 

### Return type

[**ResourceListOfScopeDefinition**](ResourceListOfScopeDefinition.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of scopes |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

