# horizon.IntegrationsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_instance**](IntegrationsApi.md#create_instance) | **POST** /horizon/api/integrations/instances | [EXPERIMENTAL] CreateInstance: Create a single integration instance.
[**delete_instance**](IntegrationsApi.md#delete_instance) | **DELETE** /horizon/api/integrations/instances/{instanceId} | [EXPERIMENTAL] DeleteInstance: Delete a single integration instance.
[**execute_instance**](IntegrationsApi.md#execute_instance) | **POST** /horizon/api/integrations/instances/{instanceId}/execute | [EXPERIMENTAL] ExecuteInstance: Execute an integration instance.
[**execute_instance_with_params**](IntegrationsApi.md#execute_instance_with_params) | **POST** /horizon/api/integrations/instances/{instanceId}/executewithparams | [EXPERIMENTAL] ExecuteInstanceWithParams: Execute an integration instance with runtime parameters
[**get_execution_ids_for_instance**](IntegrationsApi.md#get_execution_ids_for_instance) | **GET** /horizon/api/integrations/instances/{instanceId}/executions | [EXPERIMENTAL] GetExecutionIdsForInstance: Get integration instance execution ids.
[**get_instance**](IntegrationsApi.md#get_instance) | **GET** /horizon/api/integrations/instances/{instanceId} | [EXPERIMENTAL] GetInstance: Get a specified Instance for a given integration.
[**get_instance_optional_property_mapping**](IntegrationsApi.md#get_instance_optional_property_mapping) | **GET** /horizon/api/integrations/instances/configuration/{integration}/{instanceId} | [EXPERIMENTAL] GetInstanceOptionalPropertyMapping: Get the Optional Property Mapping for an Integration Instance
[**get_integration_configuration**](IntegrationsApi.md#get_integration_configuration) | **GET** /horizon/api/integrations/configuration/{integration} | [EXPERIMENTAL] GetIntegrationConfiguration: Get the Field and Property Mapping configuration for a given integration
[**get_integration_configuration_fields**](IntegrationsApi.md#get_integration_configuration_fields) | **GET** /horizon/api/integrations/configuration/{integration}/fields | [EXPERIMENTAL] GetIntegrationConfigurationFields: Get the Field Mapping configuration for a given integration
[**get_integration_configuration_properties**](IntegrationsApi.md#get_integration_configuration_properties) | **GET** /horizon/api/integrations/configuration/{integration}/properties | [EXPERIMENTAL] GetIntegrationConfigurationProperties: Get the Property Mapping configuration for a given integration
[**get_schema**](IntegrationsApi.md#get_schema) | **GET** /horizon/api/integrations/schema/{integration} | [EXPERIMENTAL] GetSchema: Get the JSON schema for the details section of an integration instance.
[**list_instances**](IntegrationsApi.md#list_instances) | **GET** /horizon/api/integrations/instances | [EXPERIMENTAL] ListInstances: List instances across all integrations.
[**list_integrations**](IntegrationsApi.md#list_integrations) | **GET** /horizon/api/integrations | [EXPERIMENTAL] ListIntegrations: List available integrations.
[**set_instance_optional_property_mapping**](IntegrationsApi.md#set_instance_optional_property_mapping) | **PUT** /horizon/api/integrations/instances/configuration/{integration}/{instanceId} | [EXPERIMENTAL] SetInstanceOptionalPropertyMapping: Set the Optional Property Mapping for an Integration Instance
[**update_instance**](IntegrationsApi.md#update_instance) | **PUT** /horizon/api/integrations/instances/{instanceId} | [EXPERIMENTAL] UpdateInstance: Update a single integration instance.


### Example

```python
from finbourne.sdk.exceptions import ApiException
from finbourne.sdk.extensions.configuration_options import ConfigurationOptions
from finbourne.sdk.services.horizon.models import *

from finbourne.sdk.extensions import (
  SyncApiClientFactory
)

from finbourne.sdk.services.horizon.api.integrations_api import IntegrationsApi

# opts = ConfigurationOptions()
# opts.total_timeout_ms = 30_000

# uncomment the below to use an api client factory with overrides
# api_client_factory = SyncApiClientFactory(opts=opts)

api_client_factory = SyncApiClientFactory()
api_instance = api_client_factory.build(IntegrationsApi)
```

---

# **create_instance**
> InstanceIdentifier createInstance = create_instance(create_instance_request=create_instance_request)

[EXPERIMENTAL] CreateInstance: Create a single integration instance.

Creates a new instance of an integration, returning its identifier. The user must be authenticated, entitled to call this method, and the user's domain must be licensed for the integration.

### Example

```python
api_instance = api_client_factory.build(IntegrationsApi)
create_instance_request = CreateInstanceRequest()
api_response = api_instance.create_instance(create_instance_request=create_instance_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_instance_request** | [**CreateInstanceRequest**](CreateInstanceRequest.md)| The new integration instance. | [optional] 

### Return type

[**InstanceIdentifier**](InstanceIdentifier.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Identifier of the created instance. |  -  |
**400** | The details of the input related failure |  -  |
**404** | The integration type does not exist. |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **delete_instance**
> deleteInstance = delete_instance(instance_id)

[EXPERIMENTAL] DeleteInstance: Delete a single integration instance.

Deletes an existing instance of an integration, returning its identifier. The user must be authenticated, entitled to call this method, and the user's domain must be licensed for the integration.

### Example

```python
api_instance = api_client_factory.build(IntegrationsApi)
instance_id = 'instance_id_example' # str
api_instance.delete_instance(instance_id)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **str**| Instance identifier e.g. \&quot;b64135e7-98a0-41af-a845-d86167d54cc7\&quot;. | [required] 

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
**404** | The instance does not exist. |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **execute_instance**
> ExecuteInstanceResponse executeInstance = execute_instance(instance_id)

[EXPERIMENTAL] ExecuteInstance: Execute an integration instance.

Starts execution of an instance, returning its execution identifier. The user must be authenticated, entitled to call this method, and the user's domain must be licensed for the integration.

### Example

```python
api_instance = api_client_factory.build(IntegrationsApi)
instance_id = 'instance_id_example' # str
api_response = api_instance.execute_instance(instance_id)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **str**| Instance identifier e.g. \&quot;b64135e7-98a0-41af-a845-d86167d54cc7\&quot;. | [required] 

### Return type

[**ExecuteInstanceResponse**](ExecuteInstanceResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The execution id |  -  |
**400** | The details of the input related failure |  -  |
**404** | The integration instance does not exist |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **execute_instance_with_params**
> ExecuteInstanceResponse executeInstanceWithParams = execute_instance_with_params(instance_id, request_body)

[EXPERIMENTAL] ExecuteInstanceWithParams: Execute an integration instance with runtime parameters

Starts execution of an instance, returning its execution identifier. The user must be authenticated, entitled to call this method, and the user's domain must be licensed for the integration.

### Example

```python
api_instance = api_client_factory.build(IntegrationsApi)
instance_id = 'instance_id_example' # str
request_body = {"para1":"val1","para2":"val2"} # Dict[str, str]
api_response = api_instance.execute_instance_with_params(instance_id, request_body)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **str**| Instance identifier e.g. \&quot;b64135e7-98a0-41af-a845-d86167d54cc7\&quot;. | [required] 
 **request_body** | [**Dict[str, str]**](str.md)| Dictionary(string,string) of runtime parameters passed to the integration instance | [required] 

### Return type

[**ExecuteInstanceResponse**](ExecuteInstanceResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The execution id |  -  |
**400** | The details of the input related failure |  -  |
**404** | The integration instance does not exist |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_execution_ids_for_instance**
> List[str] getExecutionIdsForInstance = get_execution_ids_for_instance(instance_id, limit=limit)

[EXPERIMENTAL] GetExecutionIdsForInstance: Get integration instance execution ids.

Get the most recent execution ids for an integration instance. The user must be authenticated, entitled to call this method, and the user's domain must be licensed for the integration.

### Example

```python
api_instance = api_client_factory.build(IntegrationsApi)
instance_id = 'instance_id_example' # str
limit = 56 # int (optional)
api_response = api_instance.get_execution_ids_for_instance(instance_id, limit=limit)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **str**| Instance identifier e.g. \&quot;30dc93c6-a127-46bf-aea8-e466d720b72d\&quot;. | [required] 
 **limit** | **int**| Maximum number of returned execution ids | [optional] 

### Return type

**List[str]**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The execution ids sorted by start date (descending) |  -  |
**400** | The details of the input related failure |  -  |
**404** | The integration instance does not exist |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_instance**
> IntegrationInstanceResponse getInstance = get_instance(instance_id)

[EXPERIMENTAL] GetInstance: Get a specified Instance for a given integration.

The user must be authenticated to call this method.

### Example

```python
api_instance = api_client_factory.build(IntegrationsApi)
instance_id = 'instance_id_example' # str
api_response = api_instance.get_instance(instance_id)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **str**|  | [required] 

### Return type

[**IntegrationInstanceResponse**](IntegrationInstanceResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | The details of the input related failure |  -  |
**404** | The requested instance does not exist. |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_instance_optional_property_mapping**
> Dict[str, LusidPropertyDefinitionOverridesByType] getInstanceOptionalPropertyMapping = get_instance_optional_property_mapping(integration, instance_id)

[EXPERIMENTAL] GetInstanceOptionalPropertyMapping: Get the Optional Property Mapping for an Integration Instance

Will return the full list of optional properties configured for this integration instance and any naming overrides

### Example

```python
api_instance = api_client_factory.build(IntegrationsApi)
integration = 'integration_example' # str
instance_id = 'instance_id_example' # str
api_response = api_instance.get_instance_optional_property_mapping(integration, instance_id)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **integration** | **str**| The type of the integration e.g. \&quot;copp-clark\&quot;. | [required] 
 **instance_id** | **str**| Identifier of the instance | [required] 

### Return type

[**Dict[str, LusidPropertyDefinitionOverridesByType]**](LusidPropertyDefinitionOverridesByType.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**404** | The requested instance(s) do not exist. |  -  |
**400** | The details of the input related failure |  -  |
**200** | OK |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_integration_configuration**
> IntegrationPropertyConfiguration getIntegrationConfiguration = get_integration_configuration(integration)

[EXPERIMENTAL] GetIntegrationConfiguration: Get the Field and Property Mapping configuration for a given integration

The user must be authenticated, entitled to call this method, but the user's domain does not need to be licensed for the integration.

### Example

```python
api_instance = api_client_factory.build(IntegrationsApi)
integration = 'integration_example' # str
api_response = api_instance.get_integration_configuration(integration)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **integration** | **str**|  | [required] 

### Return type

[**IntegrationPropertyConfiguration**](IntegrationPropertyConfiguration.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | The details of the input related failure |  -  |
**404** | The requested integration does not exist. |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_integration_configuration_fields**
> PagedResourceListOfIFieldMapping getIntegrationConfigurationFields = get_integration_configuration_fields(integration, filter=filter, sort_by=sort_by, limit=limit, page_token=page_token)

[EXPERIMENTAL] GetIntegrationConfigurationFields: Get the Field Mapping configuration for a given integration

The user must be authenticated, entitled to call this method, but the user's domain does not need to be licensed for the integration.

### Example

```python
api_instance = api_client_factory.build(IntegrationsApi)
integration = 'integration_example' # str
filter = 'filter_example' # str (optional)
sort_by = ['sort_by_example'] # List[str] (optional)
limit = 100 # int (optional)
page_token = '' # str (optional)
api_response = api_instance.get_integration_configuration_fields(integration, filter=filter, sort_by=sort_by, limit=limit, page_token=page_token)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **integration** | **str**|  | [required] 
 **filter** | **str**|  | [optional] 
 **sort_by** | [**List[str]**](str.md)|  | [optional] 
 **limit** | **int**|  | [optional] [default to 100]
 **page_token** | **str**|  | [optional] [default to &#39;&#39;]

### Return type

[**PagedResourceListOfIFieldMapping**](PagedResourceListOfIFieldMapping.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | The details of the input related failure |  -  |
**404** | The requested integration does not exist. |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_integration_configuration_properties**
> PagedResourceListOfIPropertyMapping getIntegrationConfigurationProperties = get_integration_configuration_properties(integration, filter=filter, sort_by=sort_by, limit=limit, page_token=page_token)

[EXPERIMENTAL] GetIntegrationConfigurationProperties: Get the Property Mapping configuration for a given integration

The user must be authenticated, entitled to call this method, but the user's domain does not need to be licensed for the integration.

### Example

```python
api_instance = api_client_factory.build(IntegrationsApi)
integration = 'integration_example' # str
filter = 'filter_example' # str (optional)
sort_by = ['sort_by_example'] # List[str] (optional)
limit = 100 # int (optional)
page_token = '' # str (optional)
api_response = api_instance.get_integration_configuration_properties(integration, filter=filter, sort_by=sort_by, limit=limit, page_token=page_token)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **integration** | **str**|  | [required] 
 **filter** | **str**|  | [optional] 
 **sort_by** | [**List[str]**](str.md)|  | [optional] 
 **limit** | **int**|  | [optional] [default to 100]
 **page_token** | **str**|  | [optional] [default to &#39;&#39;]

### Return type

[**PagedResourceListOfIPropertyMapping**](PagedResourceListOfIPropertyMapping.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | The details of the input related failure |  -  |
**404** | The requested integration does not exist. |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_schema**
> JSchema getSchema = get_schema(integration)

[EXPERIMENTAL] GetSchema: Get the JSON schema for the details section of an integration instance.

The user must be authenticated, entitled to call this method, and the user's domain must be licensed for the integration.

### Example

```python
api_instance = api_client_factory.build(IntegrationsApi)
integration = 'integration_example' # str
api_response = api_instance.get_schema(integration)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **integration** | **str**| The type of the integration e.g. \&quot;copp-clark\&quot;. | [required] 

### Return type

[**JSchema**](JSchema.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The system defined JSON schema for the details of a specified integration. |  -  |
**400** | The details of the input related failure |  -  |
**404** | The integration type does not exist or is not enabled. |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **list_instances**
> List[IntegrationInstance] listInstances = list_instances()

[EXPERIMENTAL] ListInstances: List instances across all integrations.

The user must be authenticated to call this method.

### Example

```python
api_instance = api_client_factory.build(IntegrationsApi)
api_response = api_instance.list_instances()
pprint(api_response)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**List[IntegrationInstance]**](IntegrationInstance.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | The requested instance(s) do not exist. |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **list_integrations**
> List[IntegrationDescription] listIntegrations = list_integrations()

[EXPERIMENTAL] ListIntegrations: List available integrations.

List all available integrations. ```\"licensed\"``` indicates your domain is licensed to use this integration. To request a licence contact your [FINBOURNE sales representative](https://www.finbourne.com/contact/). Any authenticated user can call this method.

### Example

```python
api_instance = api_client_factory.build(IntegrationsApi)
api_response = api_instance.list_integrations()
pprint(api_response)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**List[IntegrationDescription]**](IntegrationDescription.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **set_instance_optional_property_mapping**
> Dict[str, LusidPropertyDefinitionOverridesByType] setInstanceOptionalPropertyMapping = set_instance_optional_property_mapping(instance_id, integration, request_body=request_body)

[EXPERIMENTAL] SetInstanceOptionalPropertyMapping: Set the Optional Property Mapping for an Integration Instance

The full list of properties must be supplied, the removal of a property from this list will remove it from the integration instance

### Example

```python
api_instance = api_client_factory.build(IntegrationsApi)
instance_id = 'instance_id_example' # str
integration = 'integration_example' # str
request_body = {"Instrument/TestVendor/CreditRating":{"displayNameOverride":"Vendor Credit Rating","entityType":"Instrument","entitySubType":["Equity"],"vendorPackage":["Transaction"]}} # Dict[str, LusidPropertyDefinitionOverridesByType] (optional)
api_response = api_instance.set_instance_optional_property_mapping(instance_id, integration, request_body=request_body)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **str**| Identifier of the instance | [required] 
 **integration** | **str**| The type of the integration e.g. \&quot;copp-clark\&quot;. | [required] 
 **request_body** | [**Dict[str, LusidPropertyDefinitionOverridesByType]**](LusidPropertyDefinitionOverridesByType.md)| Properties to be included and any overrides | [optional] 

### Return type

[**Dict[str, LusidPropertyDefinitionOverridesByType]**](LusidPropertyDefinitionOverridesByType.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**404** | The requested instance(s) do not exist. |  -  |
**400** | The details of the input related failure |  -  |
**200** | OK |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **update_instance**
> updateInstance = update_instance(instance_id, update_instance_request=update_instance_request)

[EXPERIMENTAL] UpdateInstance: Update a single integration instance.

Updates an existing instance of an integration, returning its identifier. The user must be authenticated, entitled to call this method, and the user's domain must be licensed for the integration.

### Example

```python
api_instance = api_client_factory.build(IntegrationsApi)
instance_id = 'instance_id_example' # str
update_instance_request = UpdateInstanceRequest()
api_instance.update_instance(instance_id, update_instance_request=update_instance_request)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **str**| Instance identifier e.g. \&quot;b64135e7-98a0-41af-a845-d86167d54cc7\&quot;. | [required] 
 **update_instance_request** | [**UpdateInstanceRequest**](UpdateInstanceRequest.md)| The new integration instance. | [optional] 

### Return type

void (empty response body)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**400** | The details of the input related failure |  -  |
**404** | The instance does not exist. |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

