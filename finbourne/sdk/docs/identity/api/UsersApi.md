# identity.UsersApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_user**](UsersApi.md#create_user) | **POST** /identity/api/users | CreateUser: Create User
[**delete_user**](UsersApi.md#delete_user) | **DELETE** /identity/api/users/{id} | DeleteUser: Delete User
[**expire_password**](UsersApi.md#expire_password) | **POST** /identity/api/users/{id}/lifecycle/$expirepassword | ExpirePassword: Reset the user&#39;s password to a temporary one
[**find_users_by_id**](UsersApi.md#find_users_by_id) | **GET** /identity/api/directory | FindUsersById: Find users by id endpoint
[**get_user**](UsersApi.md#get_user) | **GET** /identity/api/users/{id} | GetUser: Get User
[**get_user_schema**](UsersApi.md#get_user_schema) | **GET** /identity/api/users/schema | [EARLY ACCESS] GetUserSchema: Get User Schema
[**list_runnable_users**](UsersApi.md#list_runnable_users) | **GET** /identity/api/users/$runnable | [EARLY ACCESS] ListRunnableUsers: List Runable Users
[**list_users**](UsersApi.md#list_users) | **GET** /identity/api/users | ListUsers: List Users
[**reset_factors**](UsersApi.md#reset_factors) | **POST** /identity/api/users/{id}/lifecycle/$resetfactors | ResetFactors: Reset MFA factors
[**reset_password**](UsersApi.md#reset_password) | **POST** /identity/api/users/{id}/lifecycle/$resetpassword | ResetPassword: Reset Password
[**send_activation_email**](UsersApi.md#send_activation_email) | **POST** /identity/api/users/{id}/lifecycle/$activate | SendActivationEmail: Sends an activation email to the User
[**unlock_user**](UsersApi.md#unlock_user) | **POST** /identity/api/users/{id}/lifecycle/$unlock | UnlockUser: Unlock User
[**unsuspend_user**](UsersApi.md#unsuspend_user) | **POST** /identity/api/users/{id}/lifecycle/$unsuspend | [EXPERIMENTAL] UnsuspendUser: Unsuspend user
[**update_user**](UsersApi.md#update_user) | **PUT** /identity/api/users/{id} | UpdateUser: Update User
[**update_user_schema**](UsersApi.md#update_user_schema) | **PUT** /identity/api/users/schema | [EARLY ACCESS] UpdateUserSchema: Update User Schema


### Example

```python
from finbourne.sdk.exceptions import ApiException
from finbourne.sdk.extensions.configuration_options import ConfigurationOptions
from finbourne.sdk.services.identity.models import *

from finbourne.sdk.extensions import (
  SyncApiClientFactory
)

from finbourne.sdk.services.identity.api.users_api import UsersApi

# opts = ConfigurationOptions()
# opts.total_timeout_ms = 30_000

# uncomment the below to use an api client factory with overrides
# api_client_factory = SyncApiClientFactory(opts=opts)

api_client_factory = SyncApiClientFactory()
api_instance = api_client_factory.build(UsersApi)
```

---

# **create_user**
> UserResponse createUser = create_user(create_user_request, wait_for_reindex=wait_for_reindex)

CreateUser: Create User

Create a new User

### Example

```python
api_instance = api_client_factory.build(UsersApi)
create_user_request = CreateUserRequest()
wait_for_reindex = False # bool (optional)
api_response = api_instance.create_user(create_user_request, wait_for_reindex=wait_for_reindex)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_user_request** | [**CreateUserRequest**](CreateUserRequest.md)| Details of the User to be created | [required] 
 **wait_for_reindex** | **bool**| Should the request wait until the newly created User is indexed (available in List) before returning | [optional] [default to False]

### Return type

[**UserResponse**](UserResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Create a new user |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **delete_user**
> deleteUser = delete_user(id, purge=purge)

DeleteUser: Delete User

By default the user will be de-provisioned and inactive, however their record will remain in the identity provider for audit purposes. If this is not desirable and removal of all trace of the user is required, the purge parameter can be specified to indicate the details should be purged completely.

### Example

```python
api_instance = api_client_factory.build(UsersApi)
id = 'id_example' # str
purge = True # bool (optional)
api_instance.delete_user(id, purge=purge)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier for the user | [required] 
 **purge** | **bool**| Whether to purge any trace of the user from the identity provider (will affect audit) | [optional] 

### Return type

void (empty response body)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **expire_password**
> TemporaryPassword expirePassword = expire_password(id)

ExpirePassword: Reset the user's password to a temporary one

Resets the user's password to a temporary one which is then expired

### Example

```python
api_instance = api_client_factory.build(UsersApi)
id = 'id_example' # str
api_response = api_instance.expire_password(id)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier for the User having its password reset | [required] 

### Return type

[**TemporaryPassword**](TemporaryPassword.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Reset the user&#39;s password |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **find_users_by_id**
> ListUsersResponse findUsersById = find_users_by_id(id)

FindUsersById: Find users by id endpoint

Finds a maximum of 50 users by ID

### Example

```python
api_instance = api_client_factory.build(UsersApi)
id = ['id_example'] # List[str]
api_response = api_instance.find_users_by_id(id)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**List[str]**](str.md)| A list of unique identifiers for the users | [required] 

### Return type

[**ListUsersResponse**](ListUsersResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_user**
> UserResponse getUser = get_user(id, include_roles=include_roles)

GetUser: Get User

Get the specified User

### Example

```python
api_instance = api_client_factory.build(UsersApi)
id = 'id_example' # str
include_roles = True # bool (optional)
api_response = api_instance.get_user(id, include_roles=include_roles)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier for the User | [required] 
 **include_roles** | **bool**| Flag indicating that the users roles should be included in the response | [optional] 

### Return type

[**UserResponse**](UserResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get the specified user |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_user_schema**
> UserSchemaResponse getUserSchema = get_user_schema()

[EARLY ACCESS] GetUserSchema: Get User Schema

Get the User Schema

### Example

```python
api_instance = api_client_factory.build(UsersApi)
api_response = api_instance.get_user_schema()
pprint(api_response)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**UserSchemaResponse**](UserSchemaResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Update the User Schema |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **list_runnable_users**
> List[UserResponse] listRunnableUsers = list_runnable_users()

[EARLY ACCESS] ListRunnableUsers: List Runable Users

List the available runnable Users

### Example

```python
api_instance = api_client_factory.build(UsersApi)
api_response = api_instance.list_runnable_users()
pprint(api_response)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**List[UserResponse]**](UserResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List the available runnable users |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **list_users**
> List[UserResponse] listUsers = list_users(include_deactivated=include_deactivated)

ListUsers: List Users

List the available Users

### Example

```python
api_instance = api_client_factory.build(UsersApi)
include_deactivated = False # bool (optional)
api_response = api_instance.list_users(include_deactivated=include_deactivated)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include_deactivated** | **bool**| Include previously deleted (not purged) users | [optional] [default to False]

### Return type

[**List[UserResponse]**](UserResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List the available users |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **reset_factors**
> resetFactors = reset_factors(id)

ResetFactors: Reset MFA factors

Resets the MFA factors of the specified User

### Example

```python
api_instance = api_client_factory.build(UsersApi)
id = 'id_example' # str
api_instance.reset_factors(id)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier for the User having their MFA factors reset | [required] 

### Return type

void (empty response body)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **reset_password**
> resetPassword = reset_password(id)

ResetPassword: Reset Password

Resets the password of the specified User

### Example

```python
api_instance = api_client_factory.build(UsersApi)
id = 'id_example' # str
api_instance.reset_password(id)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier for the User having their password reset | [required] 

### Return type

void (empty response body)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **send_activation_email**
> sendActivationEmail = send_activation_email(id)

SendActivationEmail: Sends an activation email to the User

Sends an activation email to the specified User

### Example

```python
api_instance = api_client_factory.build(UsersApi)
id = 'id_example' # str
api_instance.send_activation_email(id)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier for the User to be activated | [required] 

### Return type

void (empty response body)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **unlock_user**
> unlockUser = unlock_user(id)

UnlockUser: Unlock User

Unlocks the specified User

### Example

```python
api_instance = api_client_factory.build(UsersApi)
id = 'id_example' # str
api_instance.unlock_user(id)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier for the User to be unlocked | [required] 

### Return type

void (empty response body)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **unsuspend_user**
> unsuspendUser = unsuspend_user(id)

[EXPERIMENTAL] UnsuspendUser: Unsuspend user

Unsuspend the user

### Example

```python
api_instance = api_client_factory.build(UsersApi)
id = 'id_example' # str
api_instance.unsuspend_user(id)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier for the User to Unsuspend | [required] 

### Return type

void (empty response body)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **update_user**
> UserResponse updateUser = update_user(id, update_user_request)

UpdateUser: Update User

Updates the specified User

### Example

```python
api_instance = api_client_factory.build(UsersApi)
id = 'id_example' # str
update_user_request = UpdateUserRequest()
api_response = api_instance.update_user(id, update_user_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier for the User to be updated | [required] 
 **update_user_request** | [**UpdateUserRequest**](UpdateUserRequest.md)| The new definition of the User | [required] 

### Return type

[**UserResponse**](UserResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Update a user |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **update_user_schema**
> UserSchemaResponse updateUserSchema = update_user_schema(update_user_schema_request)

[EARLY ACCESS] UpdateUserSchema: Update User Schema

Update the User Schema

### Example

```python
api_instance = api_client_factory.build(UsersApi)
update_user_schema_request = UpdateUserSchemaRequest()
api_response = api_instance.update_user_schema(update_user_schema_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_user_schema_request** | [**UpdateUserSchemaRequest**](UpdateUserSchemaRequest.md)| The new User Schema | [required] 

### Return type

[**UserSchemaResponse**](UserSchemaResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Update the User Schema |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

