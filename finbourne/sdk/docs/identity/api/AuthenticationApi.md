# identity.AuthenticationApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_authentication_information**](AuthenticationApi.md#get_authentication_information) | **GET** /identity/api/authentication/information | GetAuthenticationInformation: Gets AuthenticationInformation
[**get_password_policy**](AuthenticationApi.md#get_password_policy) | **GET** /identity/api/authentication/password-policy/{userType} | GetPasswordPolicy: Gets password policy for a user type
[**get_support_access_history**](AuthenticationApi.md#get_support_access_history) | **GET** /identity/api/authentication/support | GetSupportAccessHistory: Get the history of all support access granted and any information pertaining to their termination
[**get_support_roles**](AuthenticationApi.md#get_support_roles) | **GET** /identity/api/authentication/support-roles | GetSupportRoles: Get mapping of support roles, the internal representation to a human friendly representation
[**grant_support_access**](AuthenticationApi.md#grant_support_access) | **POST** /identity/api/authentication/support | GrantSupportAccess: Grants FINBOURNE support access to your account
[**invalidate_support_access**](AuthenticationApi.md#invalidate_support_access) | **DELETE** /identity/api/authentication/support | InvalidateSupportAccess: Revoke any FINBOURNE support access to your account
[**update_password_policy**](AuthenticationApi.md#update_password_policy) | **PUT** /identity/api/authentication/password-policy/{userType} | UpdatePasswordPolicy: Updates password policy for a user type


### Example

```python
from finbourne.sdk.exceptions import ApiException
from finbourne.sdk.extensions.configuration_options import ConfigurationOptions
from finbourne.sdk.services.identity.models import *

from finbourne.sdk.extensions import (
  SyncApiClientFactory
)

from finbourne.sdk.services.identity.api.authentication_api import AuthenticationApi

# opts = ConfigurationOptions()
# opts.total_timeout_ms = 30_000

# uncomment the below to use an api client factory with overrides
# api_client_factory = SyncApiClientFactory(opts=opts)

api_client_factory = SyncApiClientFactory()
api_instance = api_client_factory.build(AuthenticationApi)
```

---

# **get_authentication_information**
> AuthenticationInformation getAuthenticationInformation = get_authentication_information()

GetAuthenticationInformation: Gets AuthenticationInformation

Get the AuthenticationInformation associated with the current domain. This includes all the necessary information to login to this domain.

### Example

```python
api_instance = api_client_factory.build(AuthenticationApi)
api_response = api_instance.get_authentication_information()
pprint(api_response)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AuthenticationInformation**](AuthenticationInformation.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get authentication information |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_password_policy**
> PasswordPolicyResponse getPasswordPolicy = get_password_policy(user_type)

GetPasswordPolicy: Gets password policy for a user type

Get the password policy for a given user type

### Example

```python
api_instance = api_client_factory.build(AuthenticationApi)
user_type = 'user_type_example' # str
api_response = api_instance.get_password_policy(user_type)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_type** | **str**| The type of user (should only be personal or service) | [required] 

### Return type

[**PasswordPolicyResponse**](PasswordPolicyResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get password policy |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_support_access_history**
> List[SupportAccessResponse] getSupportAccessHistory = get_support_access_history(start=start, end=end)

GetSupportAccessHistory: Get the history of all support access granted and any information pertaining to their termination

The active and inactive support requests will be returned, inactive support requests will have information pertaining to their termination including obfuscated userIds of those who created and terminated the request

### Example

```python
api_instance = api_client_factory.build(AuthenticationApi)
start = '2013-10-20T19:20:30+01:00' # datetime (optional)
end = '2013-10-20T19:20:30+01:00' # datetime (optional)
api_response = api_instance.get_support_access_history(start=start, end=end)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start** | **datetime**| The start expiry date to query support access requests from | [optional] 
 **end** | **datetime**| The end expiry date to query support access requests to | [optional] 

### Return type

[**List[SupportAccessResponse]**](SupportAccessResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get support access history |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_support_roles**
> SupportRolesResponse getSupportRoles = get_support_roles()

GetSupportRoles: Get mapping of support roles, the internal representation to a human friendly representation

Get mapping of support roles, the internal representation to a human friendly representation

### Example

```python
api_instance = api_client_factory.build(AuthenticationApi)
api_response = api_instance.get_support_roles()
pprint(api_response)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SupportRolesResponse**](SupportRolesResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get support roles |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **grant_support_access**
> SupportAccessResponse grantSupportAccess = grant_support_access(support_access_request)

GrantSupportAccess: Grants FINBOURNE support access to your account

Granting support access will allow FINBOURNE employees full access to your data with the express intent to investigate support issues You can revoke this (and all) access at any time using the InvalidateSupportAccess endpoint.

### Example

```python
api_instance = api_client_factory.build(AuthenticationApi)
support_access_request = SupportAccessRequest()
api_response = api_instance.grant_support_access(support_access_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **support_access_request** | [**SupportAccessRequest**](SupportAccessRequest.md)| Request detailing the duration and reasons for supplying support access | [required] 

### Return type

[**SupportAccessResponse**](SupportAccessResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Grant Support Access |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **invalidate_support_access**
> List[SupportAccessResponse] invalidateSupportAccess = invalidate_support_access()

InvalidateSupportAccess: Revoke any FINBOURNE support access to your account

This will result in a loss of access to your data for all FINBOURNE support agents

### Example

```python
api_instance = api_client_factory.build(AuthenticationApi)
api_response = api_instance.invalidate_support_access()
pprint(api_response)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**List[SupportAccessResponse]**](SupportAccessResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Invalidate all currently active support requests |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **update_password_policy**
> PasswordPolicyResponse updatePasswordPolicy = update_password_policy(user_type, update_password_policy_request=update_password_policy_request)

UpdatePasswordPolicy: Updates password policy for a user type

Update the password policy for a given user type

### Example

```python
api_instance = api_client_factory.build(AuthenticationApi)
user_type = 'user_type_example' # str
update_password_policy_request = UpdatePasswordPolicyRequest()
api_response = api_instance.update_password_policy(user_type, update_password_policy_request=update_password_policy_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_type** | **str**| The type of user (should only be personal or service) | [required] 
 **update_password_policy_request** | [**UpdatePasswordPolicyRequest**](UpdatePasswordPolicyRequest.md)| The password policy for the given user type | [optional] 

### Return type

[**PasswordPolicyResponse**](PasswordPolicyResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Update password policy |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

