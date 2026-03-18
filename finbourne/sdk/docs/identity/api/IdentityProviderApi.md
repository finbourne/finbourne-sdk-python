# identity.IdentityProviderApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_scim**](IdentityProviderApi.md#add_scim) | **PUT** /identity/api/identityprovider/scim | AddScim: Add SCIM
[**remove_scim**](IdentityProviderApi.md#remove_scim) | **DELETE** /identity/api/identityprovider/scim | RemoveScim: Remove SCIM


### Example

```python
from finbourne.sdk.exceptions import ApiException
from finbourne.sdk.extensions.configuration_options import ConfigurationOptions
from finbourne.sdk.services.identity.models import *

from finbourne.sdk.extensions import (
  SyncApiClientFactory
)

from finbourne.sdk.services.identity.api.identity_provider_api import IdentityProviderApi

# opts = ConfigurationOptions()
# opts.total_timeout_ms = 30_000

# uncomment the below to use an api client factory with overrides
# api_client_factory = SyncApiClientFactory(opts=opts)

api_client_factory = SyncApiClientFactory()
api_instance = api_client_factory.build(IdentityProviderApi)
```

---

# **add_scim**
> AddScimResponse addScim = add_scim(api_token_action=api_token_action, old_api_token_deactivation=old_api_token_deactivation)

AddScim: Add SCIM

Generates an API token to be used for SCIM

### Example

```python
api_instance = api_client_factory.build(IdentityProviderApi)
api_token_action = 'api_token_action_example' # str (optional)
old_api_token_deactivation = '2013-10-20T19:20:30+01:00' # datetime (optional)
api_response = api_instance.add_scim(api_token_action=api_token_action, old_api_token_deactivation=old_api_token_deactivation)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token_action** | **str**| The action to take. For the API token. Defaults to \&quot;ensure\&quot; | [optional] 
 **old_api_token_deactivation** | **datetime**| Optional deactivation date for the old API token. Only used if apiTokenAction is \&quot;regenerate\&quot; | [optional] 

### Return type

[**AddScimResponse**](AddScimResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The base URL and API token to be used |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **remove_scim**
> removeScim = remove_scim()

RemoveScim: Remove SCIM

Deactivates any existing SCIM API token

### Example

```python
api_instance = api_client_factory.build(IdentityProviderApi)
api_instance.remove_scim()
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

