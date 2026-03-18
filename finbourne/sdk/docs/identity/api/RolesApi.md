# identity.RolesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_user_to_role**](RolesApi.md#add_user_to_role) | **PUT** /identity/api/roles/{id}/users/{userId} | AddUserToRole: Add User to Role
[**create_role**](RolesApi.md#create_role) | **POST** /identity/api/roles | CreateRole: Create Role
[**delete_role**](RolesApi.md#delete_role) | **DELETE** /identity/api/roles/{id} | DeleteRole: Delete Role
[**get_role**](RolesApi.md#get_role) | **GET** /identity/api/roles/{id} | GetRole: Get Role
[**list_roles**](RolesApi.md#list_roles) | **GET** /identity/api/roles | ListRoles: List Roles
[**list_users_in_role**](RolesApi.md#list_users_in_role) | **GET** /identity/api/roles/{id}/users | ListUsersInRole: Get the users in the specified role.
[**remove_user_from_role**](RolesApi.md#remove_user_from_role) | **DELETE** /identity/api/roles/{id}/users/{userId} | RemoveUserFromRole: Remove User from Role
[**update_role**](RolesApi.md#update_role) | **PUT** /identity/api/roles/{id} | UpdateRole: Update Role


### Example

```python
from finbourne.sdk.exceptions import ApiException
from finbourne.sdk.extensions.configuration_options import ConfigurationOptions
from finbourne.sdk.services.identity.models import *

from finbourne.sdk.extensions import (
  SyncApiClientFactory
)

from finbourne.sdk.services.identity.api.roles_api import RolesApi

# opts = ConfigurationOptions()
# opts.total_timeout_ms = 30_000

# uncomment the below to use an api client factory with overrides
# api_client_factory = SyncApiClientFactory(opts=opts)

api_client_factory = SyncApiClientFactory()
api_instance = api_client_factory.build(RolesApi)
```

---

# **add_user_to_role**
> addUserToRole = add_user_to_role(id, user_id)

AddUserToRole: Add User to Role

Adds the User to the specified Role

### Example

```python
api_instance = api_client_factory.build(RolesApi)
id = 'id_example' # str
user_id = 'user_id_example' # str
api_instance.add_user_to_role(id, user_id)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier for the Role | [required] 
 **user_id** | **str**| The unique identifier for the User | [required] 

### Return type

void (empty response body)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**404** | Not Found |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **create_role**
> RoleResponse createRole = create_role(create_role_request)

CreateRole: Create Role

Creates a new Role

### Example

```python
api_instance = api_client_factory.build(RolesApi)
create_role_request = CreateRoleRequest()
api_response = api_instance.create_role(create_role_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_role_request** | [**CreateRoleRequest**](CreateRoleRequest.md)| Details of the role to be created | [required] 

### Return type

[**RoleResponse**](RoleResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Create a new role |  -  |
**409** | A role with the same Name already exists. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **delete_role**
> deleteRole = delete_role(id)

DeleteRole: Delete Role

Delete the specified role

### Example

```python
api_instance = api_client_factory.build(RolesApi)
id = 'id_example' # str
api_instance.delete_role(id)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier for the role | [required] 

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

# **get_role**
> RoleResponse getRole = get_role(id)

GetRole: Get Role

Get the specified role

### Example

```python
api_instance = api_client_factory.build(RolesApi)
id = 'id_example' # str
api_response = api_instance.get_role(id)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier for the role | [required] 

### Return type

[**RoleResponse**](RoleResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get the specified role |  -  |
**404** | Not Found |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **list_roles**
> List[RoleResponse] listRoles = list_roles()

ListRoles: List Roles

List the available Roles

### Example

```python
api_instance = api_client_factory.build(RolesApi)
api_response = api_instance.list_roles()
pprint(api_response)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**List[RoleResponse]**](RoleResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List the available roles |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **list_users_in_role**
> List[UserResponse] listUsersInRole = list_users_in_role(id)

ListUsersInRole: Get the users in the specified role.

List all Users in the specified Role

### Example

```python
api_instance = api_client_factory.build(RolesApi)
id = 'id_example' # str
api_response = api_instance.list_users_in_role(id)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier for the Role | [required] 

### Return type

[**List[UserResponse]**](UserResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The users in the role |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **remove_user_from_role**
> removeUserFromRole = remove_user_from_role(id, user_id)

RemoveUserFromRole: Remove User from Role

Removes the User from the specified Role

### Example

```python
api_instance = api_client_factory.build(RolesApi)
id = 'id_example' # str
user_id = 'user_id_example' # str
api_instance.remove_user_from_role(id, user_id)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier for the Role | [required] 
 **user_id** | **str**| The unique identifier for the User | [required] 

### Return type

void (empty response body)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**404** | Not Found |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **update_role**
> RoleResponse updateRole = update_role(id, update_role_request=update_role_request)

UpdateRole: Update Role

Update the specified Role

### Example

```python
api_instance = api_client_factory.build(RolesApi)
id = 'id_example' # str
update_role_request = UpdateRoleRequest()
api_response = api_instance.update_role(id, update_role_request=update_role_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier for the role to be updated | [required] 
 **update_role_request** | [**UpdateRoleRequest**](UpdateRoleRequest.md)| The new definition of the role | [optional] 

### Return type

[**RoleResponse**](RoleResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Update a role |  -  |
**404** | Not Found |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

