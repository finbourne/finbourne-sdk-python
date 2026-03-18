# access.RolesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_policy_collection_to_role**](RolesApi.md#add_policy_collection_to_role) | **POST** /access/api/roles/{scope}/{code}/policycollections | AddPolicyCollectionToRole: Add policy collections to a role
[**create_role**](RolesApi.md#create_role) | **POST** /access/api/roles | CreateRole: Create Role
[**delete_role**](RolesApi.md#delete_role) | **DELETE** /access/api/roles/{code} | DeleteRole: Delete Role
[**get_role**](RolesApi.md#get_role) | **GET** /access/api/roles/{code} | GetRole: Get Role
[**list_roles**](RolesApi.md#list_roles) | **GET** /access/api/roles | ListRoles: List Roles
[**remove_policy_collection_from_role**](RolesApi.md#remove_policy_collection_from_role) | **DELETE** /access/api/roles/{scope}/{code}/policycollections/{policycollectionscope}/{policycollectioncode} | RemovePolicyCollectionFromRole: Remove policy collection from role
[**update_role**](RolesApi.md#update_role) | **PUT** /access/api/roles/{code} | UpdateRole: Update Role


### Example

```python
from finbourne.sdk.exceptions import ApiException
from finbourne.sdk.extensions.configuration_options import ConfigurationOptions
from finbourne.sdk.services.access.models import *

from finbourne.sdk.extensions import (
  SyncApiClientFactory
)

from finbourne.sdk.services.access.api.roles_api import RolesApi

# opts = ConfigurationOptions()
# opts.total_timeout_ms = 30_000

# uncomment the below to use an api client factory with overrides
# api_client_factory = SyncApiClientFactory(opts=opts)

api_client_factory = SyncApiClientFactory()
api_instance = api_client_factory.build(RolesApi)
```

---

# **add_policy_collection_to_role**
> RoleResponse addPolicyCollectionToRole = add_policy_collection_to_role(scope, code, add_policy_collection_to_role_request)

AddPolicyCollectionToRole: Add policy collections to a role

Assigns policy collections to a role

### Example

```python
api_instance = api_client_factory.build(RolesApi)
scope = 'scope_example' # str
code = 'code_example' # str
add_policy_collection_to_role_request = AddPolicyCollectionToRoleRequest()
api_response = api_instance.add_policy_collection_to_role(scope, code, add_policy_collection_to_role_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Role | [required] 
 **code** | **str**| The code of the Role | [required] 
 **add_policy_collection_to_role_request** | [**AddPolicyCollectionToRoleRequest**](AddPolicyCollectionToRoleRequest.md)| The policy collections to add | [required] 

### Return type

[**RoleResponse**](RoleResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | AddPolicyCollectionToRole |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **create_role**
> RoleResponse createRole = create_role(role_creation_request)

CreateRole: Create Role

Creates a Role

### Example

```python
api_instance = api_client_factory.build(RolesApi)
role_creation_request = RoleCreationRequest()
api_response = api_instance.create_role(role_creation_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_creation_request** | [**RoleCreationRequest**](RoleCreationRequest.md)| The definition of the Role | [required] 

### Return type

[**RoleResponse**](RoleResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created Role |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **delete_role**
> deleteRole = delete_role(code, scope=scope)

DeleteRole: Delete Role

Deletes an identified Role

### Example

```python
api_instance = api_client_factory.build(RolesApi)
code = 'code_example' # str
scope = 'scope_example' # str (optional)
api_instance.delete_role(code, scope=scope)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| The code of the Role | [required] 
 **scope** | **str**| &gt;Optional. Will use default scope if not supplied. The scope of the Role | [optional] 

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

# **get_role**
> RoleResponse getRole = get_role(code, scope=scope)

GetRole: Get Role

Gets an identified Role

### Example

```python
api_instance = api_client_factory.build(RolesApi)
code = 'code_example' # str
scope = 'scope_example' # str (optional)
api_response = api_instance.get_role(code, scope=scope)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| The code of the Role | [required] 
 **scope** | **str**| Optional. Will use default scope if not supplied. The scope of the Role | [optional] 

### Return type

[**RoleResponse**](RoleResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Requested Role |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **list_roles**
> List[RoleResponse] listRoles = list_roles(scope=scope)

ListRoles: List Roles

Gets all Roles in a scope

### Example

```python
api_instance = api_client_factory.build(RolesApi)
scope = 'scope_example' # str (optional)
api_response = api_instance.list_roles(scope=scope)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| Optional. Will use all scopes if not supplied. The requested scope | [optional] 

### Return type

[**List[RoleResponse]**](RoleResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of Roles |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **remove_policy_collection_from_role**
> RoleResponse removePolicyCollectionFromRole = remove_policy_collection_from_role(scope, code, policycollectionscope, policycollectioncode)

RemovePolicyCollectionFromRole: Remove policy collection from role

Removes a policy collection from a role

### Example

```python
api_instance = api_client_factory.build(RolesApi)
scope = 'scope_example' # str
code = 'code_example' # str
policycollectionscope = 'policycollectionscope_example' # str
policycollectioncode = 'policycollectioncode_example' # str
api_response = api_instance.remove_policy_collection_from_role(scope, code, policycollectionscope, policycollectioncode)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Role | [required] 
 **code** | **str**| The code of the Role | [required] 
 **policycollectionscope** | **str**| The scope of policy collection to remove from the Role | [required] 
 **policycollectioncode** | **str**| The code of the policy collection to remove from the Role | [required] 

### Return type

[**RoleResponse**](RoleResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | RemovePolicyCollectionFromRole |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **update_role**
> RoleResponse updateRole = update_role(code, role_update_request, scope=scope, before_scope=before_scope, before_code=before_code, after_scope=after_scope, after_code=after_code)

UpdateRole: Update Role

Updates a Role

### Example

```python
api_instance = api_client_factory.build(RolesApi)
code = 'code_example' # str
role_update_request = RoleUpdateRequest()
scope = 'scope_example' # str (optional)
before_scope = 'before_scope_example' # str (optional)
before_code = 'before_code_example' # str (optional)
after_scope = 'after_scope_example' # str (optional)
after_code = 'after_code_example' # str (optional)
api_response = api_instance.update_role(code, role_update_request, scope=scope, before_scope=before_scope, before_code=before_code, after_scope=after_scope, after_code=after_code)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| The code of the Role | [required] 
 **role_update_request** | [**RoleUpdateRequest**](RoleUpdateRequest.md)| The updated definition of the Role | [required] 
 **scope** | **str**| &gt;Optional. Will use default scope if not supplied. The scope of the Role | [optional] 
 **before_scope** | **str**| Optional. The scope of the Role. Will use default scope if not supplied. | [optional] 
 **before_code** | **str**| Optional. The code of the Role | [optional] 
 **after_scope** | **str**| Optional. The scope of the Role. Will use default scope if not supplied. | [optional] 
 **after_code** | **str**| Optional. The code of the Role | [optional] 

### Return type

[**RoleResponse**](RoleResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated Role |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

