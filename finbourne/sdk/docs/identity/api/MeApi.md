# identity.MeApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_user_info**](MeApi.md#get_user_info) | **GET** /identity/api/me | GetUserInfo: Get User Info
[**set_password**](MeApi.md#set_password) | **PUT** /identity/api/me/password | SetPassword: Set password of current user


### Example

```python
from finbourne.sdk.exceptions import ApiException
from finbourne.sdk.extensions.configuration_options import ConfigurationOptions
from finbourne.sdk.services.identity.models import *

from finbourne.sdk.extensions import (
  SyncApiClientFactory
)

from finbourne.sdk.services.identity.api.me_api import MeApi

# opts = ConfigurationOptions()
# opts.total_timeout_ms = 30_000

# uncomment the below to use an api client factory with overrides
# api_client_factory = SyncApiClientFactory(opts=opts)

api_client_factory = SyncApiClientFactory()
api_instance = api_client_factory.build(MeApi)
```

---

# **get_user_info**
> CurrentUserResponse getUserInfo = get_user_info()

GetUserInfo: Get User Info

Get the requesting user's basic info

### Example

```python
api_instance = api_client_factory.build(MeApi)
api_response = api_instance.get_user_info()
pprint(api_response)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CurrentUserResponse**](CurrentUserResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get the specified user&#39;s info |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **set_password**
> SetPasswordResponse setPassword = set_password(set_password)

SetPassword: Set password of current user

Set the password of the current user to the specified value.              Note this is feature is only available to Service users authenticated using OpenID. For further information relating to usage of this feature please consult the documentation.

### Example

```python
api_instance = api_client_factory.build(MeApi)
set_password = SetPassword()
api_response = api_instance.set_password(set_password)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **set_password** | [**SetPassword**](SetPassword.md)| The request containing the new password value | [required] 

### Return type

[**SetPasswordResponse**](SetPasswordResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Set the current user&#39;s password |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

