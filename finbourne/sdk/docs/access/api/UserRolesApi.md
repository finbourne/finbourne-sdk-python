# access.UserRolesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_policy_collection_to_user_role**](UserRolesApi.md#add_policy_collection_to_user_role) | **POST** /access/api/userroles/{userid}/policycollections | AddPolicyCollectionToUserRole: Add a policy collection to a user-role
[**add_policy_to_user_role**](UserRolesApi.md#add_policy_to_user_role) | **POST** /access/api/userroles/{userid}/policies | AddPolicyToUserRole: Add a policy to a user-role
[**create_user_role**](UserRolesApi.md#create_user_role) | **POST** /access/api/userroles | CreateUserRole: Create a user-role
[**delete_user_role**](UserRolesApi.md#delete_user_role) | **DELETE** /access/api/userroles/{userid} | DeleteUserRole: Delete a user-role
[**get_user_role**](UserRolesApi.md#get_user_role) | **GET** /access/api/userroles/{userid} | GetUserRole: Get a user-role
[**list_user_roles**](UserRolesApi.md#list_user_roles) | **GET** /access/api/userroles | ListUserRoles: List user-roles
[**remove_policy_collection_from_user_role**](UserRolesApi.md#remove_policy_collection_from_user_role) | **DELETE** /access/api/userroles/{userid}/policycollections/{policyCollectionScope}/{policyCollectionCode} | RemovePolicyCollectionFromUserRole: Remove a policy collection from a user-role
[**remove_policy_from_user_role**](UserRolesApi.md#remove_policy_from_user_role) | **DELETE** /access/api/userroles/{userid}/policies/{policyScope}/{policyCode} | RemovePolicyFromUserRole: Remove a policy from a user-role
[**update_user_role**](UserRolesApi.md#update_user_role) | **POST** /access/api/userroles/{userid}/update | UpdateUserRole: Update a user-role


### Example

```python
from finbourne.sdk.exceptions import ApiException
from finbourne.sdk.extensions.configuration_options import ConfigurationOptions
from finbourne.sdk.services.access.models import *

from finbourne.sdk.extensions import (
  SyncApiClientFactory
)

from finbourne.sdk.services.access.api.user_roles_api import UserRolesApi

# opts = ConfigurationOptions()
# opts.total_timeout_ms = 30_000

# uncomment the below to use an api client factory with overrides
# api_client_factory = SyncApiClientFactory(opts=opts)

api_client_factory = SyncApiClientFactory()
api_instance = api_client_factory.build(UserRolesApi)
```

---

# **add_policy_collection_to_user_role**
> UserRoleResponse addPolicyCollectionToUserRole = add_policy_collection_to_user_role(userid, add_policy_collection_to_role_request)

AddPolicyCollectionToUserRole: Add a policy collection to a user-role

Adds a policy collection to a user-role.

### Example

```python
api_instance = api_client_factory.build(UserRolesApi)
userid = 'userid_example' # str
add_policy_collection_to_role_request = AddPolicyCollectionToRoleRequest()
api_response = api_instance.add_policy_collection_to_user_role(userid, add_policy_collection_to_role_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**| Id of the User Role to get | [required] 
 **add_policy_collection_to_role_request** | [**AddPolicyCollectionToRoleRequest**](AddPolicyCollectionToRoleRequest.md)| Dto of the policy collection to be added. | [required] 

### Return type

[**UserRoleResponse**](UserRoleResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User role with added policy collection. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **add_policy_to_user_role**
> UserRoleResponse addPolicyToUserRole = add_policy_to_user_role(userid, add_policy_to_role_request)

AddPolicyToUserRole: Add a policy to a user-role

Adds a policy to a user-role.

### Example

```python
api_instance = api_client_factory.build(UserRolesApi)
userid = 'userid_example' # str
add_policy_to_role_request = AddPolicyToRoleRequest()
api_response = api_instance.add_policy_to_user_role(userid, add_policy_to_role_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**| Id of the User Role to get | [required] 
 **add_policy_to_role_request** | [**AddPolicyToRoleRequest**](AddPolicyToRoleRequest.md)| Dto of the policy to be added. | [required] 

### Return type

[**UserRoleResponse**](UserRoleResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User role with added policy collection. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **create_user_role**
> UserRoleResponse createUserRole = create_user_role(user_role_creation_request)

CreateUserRole: Create a user-role

Creates a new user-role.

### Example

```python
api_instance = api_client_factory.build(UserRolesApi)
user_role_creation_request = UserRoleCreationRequest()
api_response = api_instance.create_user_role(user_role_creation_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_role_creation_request** | [**UserRoleCreationRequest**](UserRoleCreationRequest.md)| Definition of the user-role to create. | [required] 

### Return type

[**UserRoleResponse**](UserRoleResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User role that has been created. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **delete_user_role**
> deleteUserRole = delete_user_role(userid)

DeleteUserRole: Delete a user-role

Deletes an identified user-role.

### Example

```python
api_instance = api_client_factory.build(UserRolesApi)
userid = 'userid_example' # str
api_instance.delete_user_role(userid)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**| Id of the user-role to delete. | [required] 

### Return type

void (empty response body)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_user_role**
> UserRoleResponse getUserRole = get_user_role(userid)

GetUserRole: Get a user-role

Get an identified user-role.

### Example

```python
api_instance = api_client_factory.build(UserRolesApi)
userid = 'userid_example' # str
api_response = api_instance.get_user_role(userid)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**| Id of the user-role to get. | [required] 

### Return type

[**UserRoleResponse**](UserRoleResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested user role. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **list_user_roles**
> ResourceListOfUserRoleResponse listUserRoles = list_user_roles(filter=filter, sort_by=sort_by, limit=limit, page=page)

ListUserRoles: List user-roles

Lists all user-roles and pages.

### Example

```python
api_instance = api_client_factory.build(UserRolesApi)
filter = 'filter_example' # str (optional)
sort_by = 'sort_by_example' # str (optional)
limit = 56 # int (optional)
page = 'page_example' # str (optional)
api_response = api_instance.list_user_roles(filter=filter, sort_by=sort_by, limit=limit, page=page)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Optional. Expression to filter the result set | [optional] 
 **sort_by** | **str**| Optional. Order the results by these fields. Use the &#39;-&#39; sign to denote descending order e.g. -MyFieldName | [optional] 
 **limit** | **int**| Optional. When paginating, limit the number of returned results to this many. | [optional] 
 **page** | **str**| Optional. Encoded page string returned from a previous search result that will retrieve             the next page of data. | [optional] 

### Return type

[**ResourceListOfUserRoleResponse**](ResourceListOfUserRoleResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **remove_policy_collection_from_user_role**
> removePolicyCollectionFromUserRole = remove_policy_collection_from_user_role(userid, policy_collection_scope, policy_collection_code)

RemovePolicyCollectionFromUserRole: Remove a policy collection from a user-role

Removes a policy collection from a user-role.

### Example

```python
api_instance = api_client_factory.build(UserRolesApi)
userid = 'userid_example' # str
policy_collection_scope = 'policy_collection_scope_example' # str
policy_collection_code = 'policy_collection_code_example' # str
api_instance.remove_policy_collection_from_user_role(userid, policy_collection_scope, policy_collection_code)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**| Id of the User Role to get | [required] 
 **policy_collection_scope** | **str**| The scope of policy collection to remove from the User Role | [required] 
 **policy_collection_code** | **str**| The code of the policy collection to remove from the User Role | [required] 

### Return type

void (empty response body)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **remove_policy_from_user_role**
> removePolicyFromUserRole = remove_policy_from_user_role(userid, policy_scope, policy_code)

RemovePolicyFromUserRole: Remove a policy from a user-role

Removes a policy from a user-role.

### Example

```python
api_instance = api_client_factory.build(UserRolesApi)
userid = 'userid_example' # str
policy_scope = 'policy_scope_example' # str
policy_code = 'policy_code_example' # str
api_instance.remove_policy_from_user_role(userid, policy_scope, policy_code)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**| Id of the User Role to get | [required] 
 **policy_scope** | **str**| The scope of the policy to remove from the User Role | [required] 
 **policy_code** | **str**| The code of the policy to remove from the User Role | [required] 

### Return type

void (empty response body)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **update_user_role**
> UserRoleResponse updateUserRole = update_user_role(userid, user_role_update_request)

UpdateUserRole: Update a user-role

Updates an identified user-role.

### Example

```python
api_instance = api_client_factory.build(UserRolesApi)
userid = 'userid_example' # str
user_role_update_request = UserRoleUpdateRequest()
api_response = api_instance.update_user_role(userid, user_role_update_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**| Id of the user-role to be updated. | [required] 
 **user_role_update_request** | [**UserRoleUpdateRequest**](UserRoleUpdateRequest.md)| Definition of the update to apply to the user-role. | [required] 

### Return type

[**UserRoleResponse**](UserRoleResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User role that has been updated. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

