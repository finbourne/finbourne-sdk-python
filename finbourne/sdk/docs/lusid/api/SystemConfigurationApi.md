# lusid.SystemConfigurationApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_configuration_transaction_type**](SystemConfigurationApi.md#create_configuration_transaction_type) | **POST** /api/api/systemconfiguration/transactions/type | [EARLY ACCESS] CreateConfigurationTransactionType: Create transaction type
[**create_side_definition**](SystemConfigurationApi.md#create_side_definition) | **POST** /api/api/systemconfiguration/transactions/side | [EXPERIMENTAL] CreateSideDefinition: Create side definition
[**delete_transaction_configuration_source**](SystemConfigurationApi.md#delete_transaction_configuration_source) | **DELETE** /api/api/systemconfiguration/transactions/type/{source} | [EXPERIMENTAL] DeleteTransactionConfigurationSource: Delete all transaction configurations for a source
[**get_transaction_configuration_source**](SystemConfigurationApi.md#get_transaction_configuration_source) | **GET** /api/api/systemconfiguration/transactions/type/{source} | [EXPERIMENTAL] GetTransactionConfigurationSource: Get all transaction configurations for a source
[**list_configuration_transaction_types**](SystemConfigurationApi.md#list_configuration_transaction_types) | **GET** /api/api/systemconfiguration/transactions | [EARLY ACCESS] ListConfigurationTransactionTypes: List transaction types
[**set_configuration_transaction_types**](SystemConfigurationApi.md#set_configuration_transaction_types) | **PUT** /api/api/systemconfiguration/transactions | [EXPERIMENTAL] SetConfigurationTransactionTypes: Set transaction types
[**set_transaction_configuration_source**](SystemConfigurationApi.md#set_transaction_configuration_source) | **PUT** /api/api/systemconfiguration/transactions/type/{source} | [EXPERIMENTAL] SetTransactionConfigurationSource: Set transaction types for a source


### Example

```python
from finbourne.sdk.exceptions import ApiException
from finbourne.sdk.extensions.configuration_options import ConfigurationOptions
from finbourne.sdk.services.lusid.models import *

from finbourne.sdk.extensions import (
  SyncApiClientFactory
)

from finbourne.sdk.services.lusid.api.system_configuration_api import SystemConfigurationApi

# opts = ConfigurationOptions()
# opts.total_timeout_ms = 30_000

# uncomment the below to use an api client factory with overrides
# api_client_factory = SyncApiClientFactory(opts=opts)

api_client_factory = SyncApiClientFactory()
api_instance = api_client_factory.build(SystemConfigurationApi)
```

---

# **create_configuration_transaction_type**
> TransactionSetConfigurationData createConfigurationTransactionType = create_configuration_transaction_type(transaction_configuration_data_request=transaction_configuration_data_request)

[EARLY ACCESS] CreateConfigurationTransactionType: Create transaction type

Create a new transaction type by specifying a definition and mappings to movements.

### Example

```python
api_instance = api_client_factory.build(SystemConfigurationApi)
transaction_configuration_data_request = TransactionConfigurationDataRequest()
api_response = api_instance.create_configuration_transaction_type(transaction_configuration_data_request=transaction_configuration_data_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_configuration_data_request** | [**TransactionConfigurationDataRequest**](TransactionConfigurationDataRequest.md)| A transaction type definition. | [optional] 

### Return type

[**TransactionSetConfigurationData**](TransactionSetConfigurationData.md)

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

# **create_side_definition**
> TransactionSetConfigurationData createSideDefinition = create_side_definition(side_configuration_data_request=side_configuration_data_request)

[EXPERIMENTAL] CreateSideDefinition: Create side definition

Create a new side definition for use in a transaction type. For more information, see https://support.lusid.com/knowledgebase/article/KA-01875.

### Example

```python
api_instance = api_client_factory.build(SystemConfigurationApi)
side_configuration_data_request = SideConfigurationDataRequest()
api_response = api_instance.create_side_definition(side_configuration_data_request=side_configuration_data_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **side_configuration_data_request** | [**SideConfigurationDataRequest**](SideConfigurationDataRequest.md)| The definition of the side. | [optional] 

### Return type

[**TransactionSetConfigurationData**](TransactionSetConfigurationData.md)

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

# **delete_transaction_configuration_source**
> DeletedEntityResponse deleteTransactionConfigurationSource = delete_transaction_configuration_source(source)

[EXPERIMENTAL] DeleteTransactionConfigurationSource: Delete all transaction configurations for a source

/// WARNING! Changing existing transaction types has a material impact on how data, new and old,  is processed and aggregated by LUSID, and will affect your whole organisation. Only call this API if you are fully aware of the implications of the change.

### Example

```python
api_instance = api_client_factory.build(SystemConfigurationApi)
source = 'source_example' # str
api_response = api_instance.delete_transaction_configuration_source(source)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source** | **str**| The source to delete transaction configurations for | [required] 

### Return type

[**DeletedEntityResponse**](DeletedEntityResponse.md)

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

# **get_transaction_configuration_source**
> TransactionSetConfigurationData getTransactionConfigurationSource = get_transaction_configuration_source(source, as_at=as_at)

[EXPERIMENTAL] GetTransactionConfigurationSource: Get all transaction configurations for a source

Returns failure if requested source is not found

### Example

```python
api_instance = api_client_factory.build(SystemConfigurationApi)
source = 'source_example' # str
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
api_response = api_instance.get_transaction_configuration_source(source, as_at=as_at)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source** | **str**| The source for which to retrieve transaction configurations | [required] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the transaction configurations.              Defaults to returning the latest version of the transaction configurations if not specified. | [optional] 

### Return type

[**TransactionSetConfigurationData**](TransactionSetConfigurationData.md)

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

# **list_configuration_transaction_types**
> TransactionSetConfigurationData listConfigurationTransactionTypes = list_configuration_transaction_types(as_at=as_at)

[EARLY ACCESS] ListConfigurationTransactionTypes: List transaction types

Get the list of current transaction types. For information on the default transaction types provided with  LUSID, see https://support.lusid.com/knowledgebase/article/KA-01873/.

### Example

```python
api_instance = api_client_factory.build(SystemConfigurationApi)
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
api_response = api_instance.list_configuration_transaction_types(as_at=as_at)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **as_at** | **datetime**| The asAt datetime at which to retrieve the transaction types. Defaults              to returning the latest versions if not specified. | [optional] 

### Return type

[**TransactionSetConfigurationData**](TransactionSetConfigurationData.md)

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

# **set_configuration_transaction_types**
> TransactionSetConfigurationData setConfigurationTransactionTypes = set_configuration_transaction_types(transaction_set_configuration_data_request=transaction_set_configuration_data_request)

[EXPERIMENTAL] SetConfigurationTransactionTypes: Set transaction types

Configure all existing transaction types. Note it is not possible to configure a single existing transaction type on its own.                WARNING! Changing existing transaction types has a material impact on how data, new and old, is processed and aggregated by LUSID, and will affect your whole organisation. Only call this API if you are fully aware of the implications of the change.

### Example

```python
api_instance = api_client_factory.build(SystemConfigurationApi)
transaction_set_configuration_data_request = TransactionSetConfigurationDataRequest()
api_response = api_instance.set_configuration_transaction_types(transaction_set_configuration_data_request=transaction_set_configuration_data_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_set_configuration_data_request** | [**TransactionSetConfigurationDataRequest**](TransactionSetConfigurationDataRequest.md)| The complete set of transaction type definitions. | [optional] 

### Return type

[**TransactionSetConfigurationData**](TransactionSetConfigurationData.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **set_transaction_configuration_source**
> TransactionSetConfigurationData setTransactionConfigurationSource = set_transaction_configuration_source(source, set_transaction_configuration_source_request)

[EXPERIMENTAL] SetTransactionConfigurationSource: Set transaction types for a source

This will replace all the existing transaction configurations for the given source                WARNING! Changing existing transaction types has a material impact on how data, new and old, is processed and aggregated by LUSID, and will affect your whole organisation. Only call this API if you are fully aware of the implications of the change.

### Example

```python
api_instance = api_client_factory.build(SystemConfigurationApi)
source = 'source_example' # str
set_transaction_configuration_source_request = [{"aliases":[{"type":"Simple-Sell","description":"Sale","transactionClass":"MyDefault","transactionRole":"LongShorter","isDefault":false}],"movements":[{"movementTypes":"StockMovement","side":"Side1","direction":-1,"properties":{},"mappings":[],"movementOptions":[]},{"movementTypes":"CashCommitment","side":"Side2","direction":1,"properties":{},"mappings":[],"movementOptions":[]}],"properties":{"TransactionConfiguration/default/Example":{"key":"TransactionConfiguration/default/Example","value":{"labelValue":"Value"}}}}] # List[SetTransactionConfigurationSourceRequest]
api_response = api_instance.set_transaction_configuration_source(source, set_transaction_configuration_source_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source** | **str**| The source to set the transaction configurations for | [required] 
 **set_transaction_configuration_source_request** | [**List[SetTransactionConfigurationSourceRequest]**](SetTransactionConfigurationSourceRequest.md)| The set of transaction configurations | [required] 

### Return type

[**TransactionSetConfigurationData**](TransactionSetConfigurationData.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

