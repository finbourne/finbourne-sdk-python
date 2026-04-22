# horizon.ClientConfigurationsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_client_configuration_draft**](ClientConfigurationsApi.md#create_client_configuration_draft) | **POST** /horizon/api/clientconfiguration/{configType}/{name}/draft | [EXPERIMENTAL] CreateClientConfigurationDraft: Create a draft client configuration.
[**get_client_configuration**](ClientConfigurationsApi.md#get_client_configuration) | **GET** /horizon/api/clientconfiguration/{configType}/{name} | [EXPERIMENTAL] GetClientConfiguration: Get a client configuration.
[**list_client_configurations**](ClientConfigurationsApi.md#list_client_configurations) | **GET** /horizon/api/clientconfiguration/{configType} | [EXPERIMENTAL] ListClientConfigurations: List client configurations.
[**lock_client_configuration_version**](ClientConfigurationsApi.md#lock_client_configuration_version) | **POST** /horizon/api/clientconfiguration/{configType}/{name}/{majorVersion}/{minorVersion}/lock | [EXPERIMENTAL] LockClientConfigurationVersion: Lock a client configuration version.
[**update_client_configuration_draft**](ClientConfigurationsApi.md#update_client_configuration_draft) | **PUT** /horizon/api/clientconfiguration/{configType}/{name}/{majorVersion}/{minorVersion}/draft | [EXPERIMENTAL] UpdateClientConfigurationDraft: Update a draft client configuration.


### Example

```python
from finbourne.sdk.exceptions import ApiException
from finbourne.sdk.extensions.configuration_options import ConfigurationOptions
from finbourne.sdk.services.horizon.models import *

from finbourne.sdk.extensions import (
  SyncApiClientFactory
)

from finbourne.sdk.services.horizon.api.client_configurations_api import ClientConfigurationsApi

# opts = ConfigurationOptions()
# opts.total_timeout_ms = 30_000

# uncomment the below to use an api client factory with overrides
# api_client_factory = SyncApiClientFactory(opts=opts)

api_client_factory = SyncApiClientFactory()
api_instance = api_client_factory.build(ClientConfigurationsApi)
```

---

# **create_client_configuration_draft**
> ClientConfigurationResponse createClientConfigurationDraft = create_client_configuration_draft(config_type, name, create_client_configuration_draft_request=create_client_configuration_draft_request)

[EXPERIMENTAL] CreateClientConfigurationDraft: Create a draft client configuration.

Creates a new draft configuration record. Configurations follow a draft/locked lifecycle: create a draft here, refine it with the update endpoint, then commit it with the lock endpoint. If both majorVersion and minorVersion are omitted in the request body, the next version is assigned automatically by incrementing the minor version of the current highest version (starting at 1.0 if none exists). The user must be authenticated and entitled to call this method.

### Example

```python
api_instance = api_client_factory.build(ClientConfigurationsApi)
config_type = 'config_type_example' # str
name = 'name_example' # str
create_client_configuration_draft_request = CreateClientConfigurationDraftRequest()
api_response = api_instance.create_client_configuration_draft(config_type, name, create_client_configuration_draft_request=create_client_configuration_draft_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config_type** | **str**| The category of configuration. | [required] 
 **name** | **str**| The logical name of the configuration. | [required] 
 **create_client_configuration_draft_request** | [**CreateClientConfigurationDraftRequest**](CreateClientConfigurationDraftRequest.md)| Options for the new draft, including optional explicit version and source version. | [optional] 

### Return type

[**ClientConfigurationResponse**](ClientConfigurationResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | The details of the input related failure |  -  |
**404** | The client does not exist. |  -  |
**409** | A configuration with the specified version already exists. |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_client_configuration**
> ClientConfigurationResponse getClientConfiguration = get_client_configuration(config_type, name, major_version=major_version, minor_version=minor_version)

[EXPERIMENTAL] GetClientConfiguration: Get a client configuration.

Returns a specific configuration record. When both majorVersion and minorVersion are omitted, the highest available version is returned. Both must be supplied together or both omitted. The user must be authenticated and entitled to call this method.

### Example

```python
api_instance = api_client_factory.build(ClientConfigurationsApi)
config_type = 'config_type_example' # str
name = 'name_example' # str
major_version = 56 # int (optional)
minor_version = 56 # int (optional)
api_response = api_instance.get_client_configuration(config_type, name, major_version=major_version, minor_version=minor_version)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config_type** | **str**| The category of configuration. | [required] 
 **name** | **str**| The logical name of the configuration. | [required] 
 **major_version** | **int**| The major version to retrieve. Must be supplied together with minorVersion, or both omitted. | [optional] 
 **minor_version** | **int**| The minor version to retrieve. Must be supplied together with majorVersion, or both omitted. | [optional] 

### Return type

[**ClientConfigurationResponse**](ClientConfigurationResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | The details of the input related failure |  -  |
**404** | The client or configuration does not exist. |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **list_client_configurations**
> List[ClientConfigurationResponse] listClientConfigurations = list_client_configurations(config_type)

[EXPERIMENTAL] ListClientConfigurations: List client configurations.

Returns all configuration records for the given config type, across all versions and states (both draft and locked), ordered by version descending. The user must be authenticated and entitled to call this method.

### Example

```python
api_instance = api_client_factory.build(ClientConfigurationsApi)
config_type = 'config_type_example' # str
api_response = api_instance.list_client_configurations(config_type)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config_type** | **str**| The category of configuration to list. | [required] 

### Return type

[**List[ClientConfigurationResponse]**](ClientConfigurationResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | The details of the input related failure |  -  |
**404** | The client does not exist. |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **lock_client_configuration_version**
> ClientConfigurationResponse lockClientConfigurationVersion = lock_client_configuration_version(config_type, name, major_version, minor_version)

[EXPERIMENTAL] LockClientConfigurationVersion: Lock a client configuration version.

Locks a draft configuration version, making it immutable and ready for use. Once locked, a version cannot be edited or unlocked. All versions are retained permanently. The user must be authenticated and entitled to call this method.

### Example

```python
api_instance = api_client_factory.build(ClientConfigurationsApi)
config_type = 'config_type_example' # str
name = 'name_example' # str
major_version = 56 # int
minor_version = 56 # int
api_response = api_instance.lock_client_configuration_version(config_type, name, major_version, minor_version)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config_type** | **str**| The category of configuration. | [required] 
 **name** | **str**| The logical name of the configuration. | [required] 
 **major_version** | **int**| The major version to lock. | [required] 
 **minor_version** | **int**| The minor version to lock. | [required] 

### Return type

[**ClientConfigurationResponse**](ClientConfigurationResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | The details of the input related failure |  -  |
**404** | The client or configuration version does not exist, or the version is already locked. |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **update_client_configuration_draft**
> ClientConfigurationResponse updateClientConfigurationDraft = update_client_configuration_draft(config_type, name, major_version, minor_version, update_client_configuration_draft_request=update_client_configuration_draft_request)

[EXPERIMENTAL] UpdateClientConfigurationDraft: Update a draft client configuration.

Updates the value of an existing draft configuration. Only draft versions can be updated; locked versions are immutable. This endpoint can be called multiple times before locking. The user must be authenticated and entitled to call this method.

### Example

```python
api_instance = api_client_factory.build(ClientConfigurationsApi)
config_type = 'config_type_example' # str
name = 'name_example' # str
major_version = 56 # int
minor_version = 56 # int
update_client_configuration_draft_request = UpdateClientConfigurationDraftRequest()
api_response = api_instance.update_client_configuration_draft(config_type, name, major_version, minor_version, update_client_configuration_draft_request=update_client_configuration_draft_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config_type** | **str**| The category of configuration. | [required] 
 **name** | **str**| The logical name of the configuration. | [required] 
 **major_version** | **int**| The major version of the draft to update. | [required] 
 **minor_version** | **int**| The minor version of the draft to update. | [required] 
 **update_client_configuration_draft_request** | [**UpdateClientConfigurationDraftRequest**](UpdateClientConfigurationDraftRequest.md)| The updated value. | [optional] 

### Return type

[**ClientConfigurationResponse**](ClientConfigurationResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | The details of the input related failure |  -  |
**404** | The client or configuration version does not exist, or the version is already locked. |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

