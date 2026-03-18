# identity.PersonalAuthenticationTokensApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_api_key**](PersonalAuthenticationTokensApi.md#create_api_key) | **POST** /identity/api/keys | CreateApiKey: Create a Personal Access Token
[**delete_api_key**](PersonalAuthenticationTokensApi.md#delete_api_key) | **DELETE** /identity/api/keys/{id} | DeleteApiKey: Invalidate a Personal Access Token
[**list_own_api_keys**](PersonalAuthenticationTokensApi.md#list_own_api_keys) | **GET** /identity/api/keys | ListOwnApiKeys: Gets the meta data for all of the user&#39;s existing Personal Access Tokens.


### Example

```python
from finbourne.sdk.exceptions import ApiException
from finbourne.sdk.extensions.configuration_options import ConfigurationOptions
from finbourne.sdk.services.identity.models import *

from finbourne.sdk.extensions import (
  SyncApiClientFactory
)

from finbourne.sdk.services.identity.api.personal_authentication_tokens_api import PersonalAuthenticationTokensApi

# opts = ConfigurationOptions()
# opts.total_timeout_ms = 30_000

# uncomment the below to use an api client factory with overrides
# api_client_factory = SyncApiClientFactory(opts=opts)

api_client_factory = SyncApiClientFactory()
api_instance = api_client_factory.build(PersonalAuthenticationTokensApi)
```

---

# **create_api_key**
> CreatedApiKey createApiKey = create_api_key(create_api_key)

CreateApiKey: Create a Personal Access Token

Generates a Personal Access Token and returns the new key and its associated metadata.

### Example

```python
api_instance = api_client_factory.build(PersonalAuthenticationTokensApi)
create_api_key = CreateApiKey()
api_response = api_instance.create_api_key(create_api_key)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_api_key** | [**CreateApiKey**](CreateApiKey.md)| The request to create a new Personal Access Token | [required] 

### Return type

[**CreatedApiKey**](CreatedApiKey.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The Personal Access Token and associated meta data. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **delete_api_key**
> ApiKey deleteApiKey = delete_api_key(id)

DeleteApiKey: Invalidate a Personal Access Token

Immediately invalidates the specified Personal Access Token

### Example

```python
api_instance = api_client_factory.build(PersonalAuthenticationTokensApi)
id = 'id_example' # str
api_response = api_instance.delete_api_key(id)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the Personal Access Token to delete | [required] 

### Return type

[**ApiKey**](ApiKey.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Invalidates a Personal Access Token |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **list_own_api_keys**
> List[ApiKey] listOwnApiKeys = list_own_api_keys()

ListOwnApiKeys: Gets the meta data for all of the user's existing Personal Access Tokens.

Gets the meta data for all of the user's Personal Access Tokens that have not been deleted. They may be invalid due to the deactivation date having passed.

### Example

```python
api_instance = api_client_factory.build(PersonalAuthenticationTokensApi)
api_response = api_instance.list_own_api_keys()
pprint(api_response)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**List[ApiKey]**](ApiKey.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of user&#39;s existing Personal Access Tokens |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

