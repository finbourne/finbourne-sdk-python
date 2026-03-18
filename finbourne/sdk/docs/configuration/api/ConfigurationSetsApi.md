# configuration.ConfigurationSetsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_configuration_to_set**](ConfigurationSetsApi.md#add_configuration_to_set) | **POST** /configuration/api/sets/{type}/{scope}/{code}/items | [EARLY ACCESS] AddConfigurationToSet: Add a configuration item to an existing set
[**check_access_token_exists**](ConfigurationSetsApi.md#check_access_token_exists) | **HEAD** /configuration/api/sets/personal/me | [DEPRECATED] CheckAccessTokenExists: Check the Personal Access Token exists for the current user
[**create_configuration_set**](ConfigurationSetsApi.md#create_configuration_set) | **POST** /configuration/api/sets | [EARLY ACCESS] CreateConfigurationSet: Create a configuration set
[**delete_access_token**](ConfigurationSetsApi.md#delete_access_token) | **DELETE** /configuration/api/sets/personal/me | [DEPRECATED] DeleteAccessToken: Delete any stored Personal Access Token for the current user
[**delete_configuration_item**](ConfigurationSetsApi.md#delete_configuration_item) | **DELETE** /configuration/api/sets/{type}/{scope}/{code}/items/{key} | [EARLY ACCESS] DeleteConfigurationItem: Remove the specified configuration item from the specified configuration set
[**delete_configuration_set**](ConfigurationSetsApi.md#delete_configuration_set) | **DELETE** /configuration/api/sets/{type}/{scope}/{code} | [EARLY ACCESS] DeleteConfigurationSet: Deletes a configuration set along with all their configuration items
[**generate_access_token**](ConfigurationSetsApi.md#generate_access_token) | **PUT** /configuration/api/sets/personal/me | [DEPRECATED] GenerateAccessToken: Generate a Personal Access Token for the current user and stores it in the me token
[**get_configuration_item**](ConfigurationSetsApi.md#get_configuration_item) | **GET** /configuration/api/sets/{type}/{scope}/{code}/items/{key} | GetConfigurationItem: Get the specific configuration item within an existing set
[**get_configuration_set**](ConfigurationSetsApi.md#get_configuration_set) | **GET** /configuration/api/sets/{type}/{scope}/{code} | GetConfigurationSet: Get a configuration set, including all the associated metadata. By default secrets will not be revealed
[**get_system_configuration_items**](ConfigurationSetsApi.md#get_system_configuration_items) | **GET** /configuration/api/sets/system/{code}/items/{key} | [EARLY ACCESS] GetSystemConfigurationItems: Get the specific system configuration items within a system set All users have access to this endpoint
[**get_system_configuration_sets**](ConfigurationSetsApi.md#get_system_configuration_sets) | **GET** /configuration/api/sets/system/{code} | GetSystemConfigurationSets: Get the specified system configuration sets, including all their associated metadata. By default secrets will not be revealed All users have access to this endpoint
[**list_configuration_sets**](ConfigurationSetsApi.md#list_configuration_sets) | **GET** /configuration/api/sets | [EARLY ACCESS] ListConfigurationSets: List all configuration sets summaries (I.e. list of scope/code combinations available)
[**update_configuration_item**](ConfigurationSetsApi.md#update_configuration_item) | **PUT** /configuration/api/sets/{type}/{scope}/{code}/items/{key} | [EARLY ACCESS] UpdateConfigurationItem: Update a configuration item&#39;s value and/or description
[**update_configuration_set**](ConfigurationSetsApi.md#update_configuration_set) | **PUT** /configuration/api/sets/{type}/{scope}/{code} | [EARLY ACCESS] UpdateConfigurationSet: Update the description of a configuration set


### Example

```python
from finbourne.sdk.exceptions import ApiException
from finbourne.sdk.extensions.configuration_options import ConfigurationOptions
from finbourne.sdk.services.configuration.models import *

from finbourne.sdk.extensions import (
  SyncApiClientFactory
)

from finbourne.sdk.services.configuration.api.configuration_sets_api import ConfigurationSetsApi

# opts = ConfigurationOptions()
# opts.total_timeout_ms = 30_000

# uncomment the below to use an api client factory with overrides
# api_client_factory = SyncApiClientFactory(opts=opts)

api_client_factory = SyncApiClientFactory()
api_instance = api_client_factory.build(ConfigurationSetsApi)
```

---

# **add_configuration_to_set**
> ConfigurationSet addConfigurationToSet = add_configuration_to_set(type, scope, code, create_configuration_item, user_id=user_id)

[EARLY ACCESS] AddConfigurationToSet: Add a configuration item to an existing set

### Example

```python
api_instance = api_client_factory.build(ConfigurationSetsApi)
type = 'type_example' # str
scope = 'scope_example' # str
code = 'code_example' # str
create_configuration_item = CreateConfigurationItem()
user_id = 'user_id_example' # str (optional)
api_response = api_instance.add_configuration_to_set(type, scope, code, create_configuration_item, user_id=user_id)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| Whether the configuration set is Personal or Shared | [required] 
 **scope** | **str**| The scope that identifies a configuration set | [required] 
 **code** | **str**| The code that identifies a configuration set | [required] 
 **create_configuration_item** | [**CreateConfigurationItem**](CreateConfigurationItem.md)| The data to create a configuration item | [required] 
 **user_id** | **str**| Feature that allows Administrators to administer personal settings  (but never reveal the value of secrets) of a specific user. | [optional] 

### Return type

[**ConfigurationSet**](ConfigurationSet.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | The details of the input related failure |  -  |
**404** | No configuration set exists with the provided identifiers |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **check_access_token_exists**
> checkAccessTokenExists = check_access_token_exists()

[DEPRECATED] CheckAccessTokenExists: Check the Personal Access Token exists for the current user

### Example

```python
api_instance = api_client_factory.build(ConfigurationSetsApi)
api_instance.check_access_token_exists()
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
**200** | The Personal Access Token exists |  -  |
**404** | The Personal Access Token does not exist |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **create_configuration_set**
> ConfigurationSet createConfigurationSet = create_configuration_set(create_configuration_set, user_id=user_id)

[EARLY ACCESS] CreateConfigurationSet: Create a configuration set

### Example

```python
api_instance = api_client_factory.build(ConfigurationSetsApi)
create_configuration_set = CreateConfigurationSet()
user_id = 'user_id_example' # str (optional)
api_response = api_instance.create_configuration_set(create_configuration_set, user_id=user_id)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_configuration_set** | [**CreateConfigurationSet**](CreateConfigurationSet.md)| The data to create a configuration set | [required] 
 **user_id** | **str**| Feature that allows Administrators to administer personal settings  (but never reveal the value of secrets) of a specific user. | [optional] 

### Return type

[**ConfigurationSet**](ConfigurationSet.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **delete_access_token**
> deleteAccessToken = delete_access_token()

[DEPRECATED] DeleteAccessToken: Delete any stored Personal Access Token for the current user

### Example

```python
api_instance = api_client_factory.build(ConfigurationSetsApi)
api_instance.delete_access_token()
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

---

# **delete_configuration_item**
> deleteConfigurationItem = delete_configuration_item(type, scope, code, key, user_id=user_id)

[EARLY ACCESS] DeleteConfigurationItem: Remove the specified configuration item from the specified configuration set

### Example

```python
api_instance = api_client_factory.build(ConfigurationSetsApi)
type = 'type_example' # str
scope = 'scope_example' # str
code = 'code_example' # str
key = 'key_example' # str
user_id = 'user_id_example' # str (optional)
api_instance.delete_configuration_item(type, scope, code, key, user_id=user_id)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| Whether the configuration set is Personal or Shared | [required] 
 **scope** | **str**| The scope that identifies a configuration set | [required] 
 **code** | **str**| The code that identifies a configuration set | [required] 
 **key** | **str**| The key that identifies a configuration item | [required] 
 **user_id** | **str**| Feature that allows Administrators to administer personal settings  (but never reveal the value of secrets) of a specific user. | [optional] 

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
**404** | No configuration item exists with the provided identifiers |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **delete_configuration_set**
> deleteConfigurationSet = delete_configuration_set(type, scope, code, user_id=user_id)

[EARLY ACCESS] DeleteConfigurationSet: Deletes a configuration set along with all their configuration items

### Example

```python
api_instance = api_client_factory.build(ConfigurationSetsApi)
type = 'type_example' # str
scope = 'scope_example' # str
code = 'code_example' # str
user_id = 'user_id_example' # str (optional)
api_instance.delete_configuration_set(type, scope, code, user_id=user_id)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| Whether the configuration set is Personal or Shared | [required] 
 **scope** | **str**| The scope that identifies a configuration set | [required] 
 **code** | **str**| The code that identifies a configuration set | [required] 
 **user_id** | **str**| Feature that allows Administrators to administer personal settings  (but never reveal the value of secrets) of a specific user. | [optional] 

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
**404** | No configuration set exists with the provided identifiers |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **generate_access_token**
> PersonalAccessToken generateAccessToken = generate_access_token(action=action)

[DEPRECATED] GenerateAccessToken: Generate a Personal Access Token for the current user and stores it in the me token

### Example

```python
api_instance = api_client_factory.build(ConfigurationSetsApi)
action = 'action_example' # str (optional)
api_response = api_instance.generate_access_token(action=action)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **action** | **str**| action&#x3D;regenerate &#x3D; Even if an existing parameter exists, forcibly regenerate a new one (deleting the old) action&#x3D;ensure &#x3D; If no parameter exists, create one. If one does already exist, verify that it is still valid (call a service?), and if so, return it. If it is not still valid, then regenerate a new one. action&#x3D;default &#x3D; If a parameter exists, return it. If not then create one. If this parameter is not provided, this is the default behaviour. | [optional] 

### Return type

[**PersonalAccessToken**](PersonalAccessToken.md)

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

# **get_configuration_item**
> ConfigurationItem getConfigurationItem = get_configuration_item(type, scope, code, key, reveal=reveal, user_id=user_id)

GetConfigurationItem: Get the specific configuration item within an existing set

### Example

```python
api_instance = api_client_factory.build(ConfigurationSetsApi)
type = 'type_example' # str
scope = 'scope_example' # str
code = 'code_example' # str
key = 'key_example' # str
reveal = True # bool (optional)
user_id = 'user_id_example' # str (optional)
api_response = api_instance.get_configuration_item(type, scope, code, key, reveal=reveal, user_id=user_id)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| Whether the configuration set is Personal or Shared | [required] 
 **scope** | **str**| The scope that identifies a configuration set | [required] 
 **code** | **str**| The code that identifies a configuration set | [required] 
 **key** | **str**| The key that identifies a configuration item | [required] 
 **reveal** | **bool**| Whether to reveal the secrets. This is only available when the userId query setting has not been specified. | [optional] 
 **user_id** | **str**| Feature that allows Administrators to administer personal settings  (but never reveal the value of secrets) of a specific user. | [optional] 

### Return type

[**ConfigurationItem**](ConfigurationItem.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | The details of the input related failure |  -  |
**404** | No configuration item exists with the provided identifiers |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_configuration_set**
> ConfigurationSet getConfigurationSet = get_configuration_set(type, scope, code, reveal=reveal, user_id=user_id)

GetConfigurationSet: Get a configuration set, including all the associated metadata. By default secrets will not be revealed

### Example

```python
api_instance = api_client_factory.build(ConfigurationSetsApi)
type = 'type_example' # str
scope = 'scope_example' # str
code = 'code_example' # str
reveal = True # bool (optional)
user_id = 'user_id_example' # str (optional)
api_response = api_instance.get_configuration_set(type, scope, code, reveal=reveal, user_id=user_id)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| Whether the configuration set is Personal or Shared | [required] 
 **scope** | **str**| The scope that identifies a configuration set | [required] 
 **code** | **str**| The code that identifies a configuration set | [required] 
 **reveal** | **bool**| Whether to reveal the secrets. This is only available when the userId query setting has not been specified. | [optional] 
 **user_id** | **str**| Feature that allows Administrators to administer personal settings  (but never reveal the value of secrets) of a specific user. | [optional] 

### Return type

[**ConfigurationSet**](ConfigurationSet.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | The details of the input related failure |  -  |
**404** | No configuration set exists with the provided identifiers |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_system_configuration_items**
> ResourceListOfConfigurationItem getSystemConfigurationItems = get_system_configuration_items(code, key, reveal=reveal)

[EARLY ACCESS] GetSystemConfigurationItems: Get the specific system configuration items within a system set All users have access to this endpoint

### Example

```python
api_instance = api_client_factory.build(ConfigurationSetsApi)
code = 'code_example' # str
key = 'key_example' # str
reveal = True # bool (optional)
api_response = api_instance.get_system_configuration_items(code, key, reveal=reveal)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| The code that identifies a system configuration set | [required] 
 **key** | **str**| The key that identifies a system configuration item | [required] 
 **reveal** | **bool**| Whether to reveal the secrets | [optional] 

### Return type

[**ResourceListOfConfigurationItem**](ResourceListOfConfigurationItem.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | The details of the input related failure |  -  |
**404** | No system configuration item exists with the provided identifiers |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_system_configuration_sets**
> ResourceListOfConfigurationSet getSystemConfigurationSets = get_system_configuration_sets(code, reveal=reveal)

GetSystemConfigurationSets: Get the specified system configuration sets, including all their associated metadata. By default secrets will not be revealed All users have access to this endpoint

### Example

```python
api_instance = api_client_factory.build(ConfigurationSetsApi)
code = 'code_example' # str
reveal = True # bool (optional)
api_response = api_instance.get_system_configuration_sets(code, reveal=reveal)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| The code that identifies a system configuration set | [required] 
 **reveal** | **bool**| Whether to reveal the secrets | [optional] 

### Return type

[**ResourceListOfConfigurationSet**](ResourceListOfConfigurationSet.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | The details of the input related failure |  -  |
**404** | No system configuration set exists with the provided identifiers |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **list_configuration_sets**
> ResourceListOfConfigurationSetSummary listConfigurationSets = list_configuration_sets(type=type, user_id=user_id)

[EARLY ACCESS] ListConfigurationSets: List all configuration sets summaries (I.e. list of scope/code combinations available)

### Example

```python
api_instance = api_client_factory.build(ConfigurationSetsApi)
type = 'type_example' # str (optional)
user_id = 'user_id_example' # str (optional)
api_response = api_instance.list_configuration_sets(type=type, user_id=user_id)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| Whether the configuration set is Personal or Shared | [optional] 
 **user_id** | **str**| Feature that allows Administrators to administer personal settings  (but never reveal the value of secrets) of a specific user. | [optional] 

### Return type

[**ResourceListOfConfigurationSetSummary**](ResourceListOfConfigurationSetSummary.md)

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

# **update_configuration_item**
> ConfigurationItem updateConfigurationItem = update_configuration_item(type, scope, code, key, update_configuration_item, user_id=user_id)

[EARLY ACCESS] UpdateConfigurationItem: Update a configuration item's value and/or description

### Example

```python
api_instance = api_client_factory.build(ConfigurationSetsApi)
type = 'type_example' # str
scope = 'scope_example' # str
code = 'code_example' # str
key = 'key_example' # str
update_configuration_item = UpdateConfigurationItem()
user_id = 'user_id_example' # str (optional)
api_response = api_instance.update_configuration_item(type, scope, code, key, update_configuration_item, user_id=user_id)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| Whether the configuration set is Personal or Shared | [required] 
 **scope** | **str**| The scope that identifies a configuration set | [required] 
 **code** | **str**| The code that identifies a configuration set | [required] 
 **key** | **str**| The key that identifies a configuration item | [required] 
 **update_configuration_item** | [**UpdateConfigurationItem**](UpdateConfigurationItem.md)| The data to update a configuration item | [required] 
 **user_id** | **str**| Feature that allows Administrators to administer personal settings  (but never reveal the value of secrets) of a specific user. | [optional] 

### Return type

[**ConfigurationItem**](ConfigurationItem.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | The details of the input related failure |  -  |
**404** | No configuration item exists with the provided identifiers |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **update_configuration_set**
> ConfigurationSet updateConfigurationSet = update_configuration_set(type, scope, code, update_configuration_set, user_id=user_id)

[EARLY ACCESS] UpdateConfigurationSet: Update the description of a configuration set

### Example

```python
api_instance = api_client_factory.build(ConfigurationSetsApi)
type = 'type_example' # str
scope = 'scope_example' # str
code = 'code_example' # str
update_configuration_set = UpdateConfigurationSet()
user_id = 'user_id_example' # str (optional)
api_response = api_instance.update_configuration_set(type, scope, code, update_configuration_set, user_id=user_id)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| Whether the configuration set is Personal or Shared | [required] 
 **scope** | **str**| The scope that identifies a configuration set | [required] 
 **code** | **str**| The code that identifies a configuration set | [required] 
 **update_configuration_set** | [**UpdateConfigurationSet**](UpdateConfigurationSet.md)| The data to update a configuration set | [required] 
 **user_id** | **str**| Feature that allows Administrators to administer personal settings  (but never reveal the value of secrets) of a specific user. | [optional] 

### Return type

[**ConfigurationSet**](ConfigurationSet.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | The details of the input related failure |  -  |
**404** | No configuration set exists with the provided identifiers |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

