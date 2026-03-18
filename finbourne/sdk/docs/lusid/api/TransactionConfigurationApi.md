# lusid.TransactionConfigurationApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_side_definition**](TransactionConfigurationApi.md#delete_side_definition) | **DELETE** /api/api/transactionconfiguration/sides/{side}/$delete | DeleteSideDefinition: Delete the given side definition
[**delete_transaction_type**](TransactionConfigurationApi.md#delete_transaction_type) | **DELETE** /api/api/transactionconfiguration/types/{source}/{type} | DeleteTransactionType: Delete a transaction type
[**delete_transaction_type_source**](TransactionConfigurationApi.md#delete_transaction_type_source) | **DELETE** /api/api/transactionconfiguration/types/{source}/$delete | DeleteTransactionTypeSource: Delete all transaction types for the given source and scope
[**get_side_definition**](TransactionConfigurationApi.md#get_side_definition) | **GET** /api/api/transactionconfiguration/sides/{side} | GetSideDefinition: Get the side definition for a given side name( or label)
[**get_transaction_type**](TransactionConfigurationApi.md#get_transaction_type) | **GET** /api/api/transactionconfiguration/types/{source}/{type} | GetTransactionType: Get a single transaction configuration type
[**list_side_definitions**](TransactionConfigurationApi.md#list_side_definitions) | **GET** /api/api/transactionconfiguration/sides | ListSideDefinitions: List the side definitions
[**list_transaction_types**](TransactionConfigurationApi.md#list_transaction_types) | **GET** /api/api/transactionconfiguration/types | ListTransactionTypes: List transaction types
[**set_side_definition**](TransactionConfigurationApi.md#set_side_definition) | **PUT** /api/api/transactionconfiguration/sides/{side} | SetSideDefinition: Set a side definition
[**set_side_definitions**](TransactionConfigurationApi.md#set_side_definitions) | **PUT** /api/api/transactionconfiguration/sides | SetSideDefinitions: Set the given side definitions
[**set_transaction_type**](TransactionConfigurationApi.md#set_transaction_type) | **PUT** /api/api/transactionconfiguration/types/{source}/{type} | SetTransactionType: Set a specific transaction type
[**set_transaction_type_source**](TransactionConfigurationApi.md#set_transaction_type_source) | **PUT** /api/api/transactionconfiguration/types/{source} | SetTransactionTypeSource: Set the transaction types for the given source and scope


### Example

```python
from finbourne.sdk.exceptions import ApiException
from finbourne.sdk.extensions.configuration_options import ConfigurationOptions
from finbourne.sdk.services.lusid.models import *

from finbourne.sdk.extensions import (
  SyncApiClientFactory
)

from finbourne.sdk.services.lusid.api.transaction_configuration_api import TransactionConfigurationApi

# opts = ConfigurationOptions()
# opts.total_timeout_ms = 30_000

# uncomment the below to use an api client factory with overrides
# api_client_factory = SyncApiClientFactory(opts=opts)

api_client_factory = SyncApiClientFactory()
api_instance = api_client_factory.build(TransactionConfigurationApi)
```

---

# **delete_side_definition**
> DeletedEntityResponse deleteSideDefinition = delete_side_definition(side, scope=scope)

DeleteSideDefinition: Delete the given side definition

Delete the side which user specify in the request.

### Example

```python
api_instance = api_client_factory.build(TransactionConfigurationApi)
side = 'side_example' # str
scope = 'default' # str (optional)
api_response = api_instance.delete_side_definition(side, scope=scope)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **side** | **str**| The label to uniquely identify the side. | [required] 
 **scope** | **str**| The scope in which the side exists. When not supplied the scope is &#39;default&#39;. | [optional] [default to &#39;default&#39;]

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

# **delete_transaction_type**
> DeletedEntityResponse deleteTransactionType = delete_transaction_type(source, type, scope=scope)

DeleteTransactionType: Delete a transaction type

/// WARNING! Changing existing transaction types has a material impact on how data, new and old,  is processed and aggregated by LUSID, and will affect your whole organisation. Only call this API if you are fully aware of the implications of the change.

### Example

```python
api_instance = api_client_factory.build(TransactionConfigurationApi)
source = 'source_example' # str
type = 'type_example' # str
scope = 'default' # str (optional)
api_response = api_instance.delete_transaction_type(source, type, scope=scope)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source** | **str**| The source that the type is in | [required] 
 **type** | **str**| One of the type&#39;s aliases | [required] 
 **scope** | **str**| The scope in which the transaction types exists. When not supplied the scope is &#39;default&#39;. | [optional] [default to &#39;default&#39;]

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

# **delete_transaction_type_source**
> DeletedEntityResponse deleteTransactionTypeSource = delete_transaction_type_source(source, scope=scope)

DeleteTransactionTypeSource: Delete all transaction types for the given source and scope

Delete all the types for the given source and scope.

### Example

```python
api_instance = api_client_factory.build(TransactionConfigurationApi)
source = 'source_example' # str
scope = 'default' # str (optional)
api_response = api_instance.delete_transaction_type_source(source, scope=scope)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source** | **str**| The source to set the transaction types for. | [required] 
 **scope** | **str**| The scope in which the transaction types exists. When not supplied the scope is &#39;default&#39;. | [optional] [default to &#39;default&#39;]

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

# **get_side_definition**
> SideDefinition getSideDefinition = get_side_definition(side, scope=scope, as_at=as_at)

GetSideDefinition: Get the side definition for a given side name( or label)

Get the side definition user requested.

### Example

```python
api_instance = api_client_factory.build(TransactionConfigurationApi)
side = 'side_example' # str
scope = 'default' # str (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
api_response = api_instance.get_side_definition(side, scope=scope, as_at=as_at)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **side** | **str**| The label to uniquely identify the side. | [required] 
 **scope** | **str**| The scope in which the side exists. When not supplied the scope is &#39;default&#39;. | [optional] [default to &#39;default&#39;]
 **as_at** | **datetime**| The asAt datetime at which to retrieve the transaction types. Defaults to returning the latest versions if not specified. | [optional] 

### Return type

[**SideDefinition**](SideDefinition.md)

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

# **get_transaction_type**
> TransactionType getTransactionType = get_transaction_type(source, type, as_at=as_at, scope=scope)

GetTransactionType: Get a single transaction configuration type

Get a single transaction type. Returns failure if not found

### Example

```python
api_instance = api_client_factory.build(TransactionConfigurationApi)
source = 'source_example' # str
type = 'type_example' # str
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
scope = 'default' # str (optional)
api_response = api_instance.get_transaction_type(source, type, as_at=as_at, scope=scope)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source** | **str**| The source that the type is in | [required] 
 **type** | **str**| One of the type&#39;s aliases | [required] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the transaction configuration.              Defaults to returning the latest version of the transaction configuration type if not specified | [optional] 
 **scope** | **str**| The scope in which the transaction types exists. When not supplied the scope is &#39;default&#39;. | [optional] [default to &#39;default&#39;]

### Return type

[**TransactionType**](TransactionType.md)

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

# **list_side_definitions**
> ResourceListOfSideDefinition listSideDefinitions = list_side_definitions(as_at=as_at, scope=scope)

ListSideDefinitions: List the side definitions

List all the side definitions in the given scope

### Example

```python
api_instance = api_client_factory.build(TransactionConfigurationApi)
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
scope = 'default' # str (optional)
api_response = api_instance.list_side_definitions(as_at=as_at, scope=scope)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **as_at** | **datetime**| The asAt datetime at which to retrieve the transaction types. Defaults to returning the latest versions if not specified. | [optional] 
 **scope** | **str**| The scope in which the side exists. When not supplied the scope is &#39;default&#39;. | [optional] [default to &#39;default&#39;]

### Return type

[**ResourceListOfSideDefinition**](ResourceListOfSideDefinition.md)

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

# **list_transaction_types**
> Dict[str, List[TransactionType]] listTransactionTypes = list_transaction_types(as_at=as_at, scope=scope)

ListTransactionTypes: List transaction types

Get the list of current transaction types. For information on the default transaction types provided with  LUSID, see https://support.lusid.com/knowledgebase/article/KA-01873/.

### Example

```python
api_instance = api_client_factory.build(TransactionConfigurationApi)
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
scope = 'default' # str (optional)
api_response = api_instance.list_transaction_types(as_at=as_at, scope=scope)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **as_at** | **datetime**| The asAt datetime at which to retrieve the transaction types. Defaults              to returning the latest versions if not specified. | [optional] 
 **scope** | **str**| The scope in which the side exists. When not supplied the scope is &#39;default&#39;. | [optional] [default to &#39;default&#39;]

### Return type

**Dict[str, List[TransactionType]]**

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

# **set_side_definition**
> SideDefinition setSideDefinition = set_side_definition(side, side_definition_request, scope=scope)

SetSideDefinition: Set a side definition

Set a new side definition for use in a transaction type. For more information, see https://support.lusid.com/knowledgebase/article/KA-01875.

### Example

```python
api_instance = api_client_factory.build(TransactionConfigurationApi)
side = 'side_example' # str
side_definition_request = SideDefinitionRequest()
scope = 'default' # str (optional)
api_response = api_instance.set_side_definition(side, side_definition_request, scope=scope)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **side** | **str**| The label to uniquely identify the side. | [required] 
 **side_definition_request** | [**SideDefinitionRequest**](SideDefinitionRequest.md)| The side definition to create or replace. | [required] 
 **scope** | **str**| The scope in which the side exists. When not supplied the scope is &#39;default&#39;. | [optional] [default to &#39;default&#39;]

### Return type

[**SideDefinition**](SideDefinition.md)

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

# **set_side_definitions**
> ResourceListOfSideDefinition setSideDefinitions = set_side_definitions(sides_definition_request, scope=scope)

SetSideDefinitions: Set the given side definitions

Set a new side definition for use in a transaction type. For more information, see https://support.lusid.com/knowledgebase/article/KA-01875.

### Example

```python
api_instance = api_client_factory.build(TransactionConfigurationApi)
sides_definition_request = [{"side":"Side1","sideRequest":{"security":"Txn:LusidInstrumentId","currency":"Txn:TradeCurrency","rate":"Txn:Units","units":"1","amount":"Transaction/MyScope/TradeAmount","notionalAmount":"Transaction/default/NotionalAmount","currentFace":"Txn:CurrentFace"}}] # List[SidesDefinitionRequest]
scope = 'default' # str (optional)
api_response = api_instance.set_side_definitions(sides_definition_request, scope=scope)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sides_definition_request** | [**List[SidesDefinitionRequest]**](SidesDefinitionRequest.md)| The list of side definitions to create, or replace. | [required] 
 **scope** | **str**| The scope in which the side exists. When not supplied the scope is &#39;default&#39;. | [optional] [default to &#39;default&#39;]

### Return type

[**ResourceListOfSideDefinition**](ResourceListOfSideDefinition.md)

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

# **set_transaction_type**
> TransactionType setTransactionType = set_transaction_type(source, type, transaction_type_request, scope=scope)

SetTransactionType: Set a specific transaction type

Set a transaction type for the given source and type. If the requested transaction type does not exist, it will be created    WARNING! Changing existing transaction types has a material impact on how data, new and old, is processed and aggregated by LUSID, and will affect your whole organisation. Only call this API if you are fully aware of the implications of the change.

### Example

```python
api_instance = api_client_factory.build(TransactionConfigurationApi)
source = 'source_example' # str
type = 'type_example' # str
transaction_type_request = TransactionTypeRequest()
scope = 'default' # str (optional)
api_response = api_instance.set_transaction_type(source, type, transaction_type_request, scope=scope)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source** | **str**| The source to set the transaction configuration for | [required] 
 **type** | **str**| One of the transaction configuration alias types to uniquely identify the configuration. If this type does not exist, then a new transaction type is created using the body of the request in the given source, without including this type | [required] 
 **transaction_type_request** | [**TransactionTypeRequest**](TransactionTypeRequest.md)| The transaction configuration to set | [required] 
 **scope** | **str**| The scope in which the transaction types exists. When not supplied the scope is &#39;default&#39;. | [optional] [default to &#39;default&#39;]

### Return type

[**TransactionType**](TransactionType.md)

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

# **set_transaction_type_source**
> ResourceListOfTransactionType setTransactionTypeSource = set_transaction_type_source(source, transaction_type_request, scope=scope)

SetTransactionTypeSource: Set the transaction types for the given source and scope

The complete set of transaction types for the source.

### Example

```python
api_instance = api_client_factory.build(TransactionConfigurationApi)
source = 'source_example' # str
transaction_type_request = [{"aliases":[{"type":"Simple-Sell","description":"Sale","transactionClass":"MyDefault","transactionRoles":"LongShorter","isDefault":false}],"movements":[{"movementTypes":"Traded","side":"Side1","direction":-1,"properties":{},"mappings":[],"movementOptions":[]},{"movementTypes":"CashSettlement","side":"Side2","direction":1,"properties":{},"mappings":[],"movementOptions":[],"settlementDateOverride":"Transaction/MyScope/SettlementDateOverride"}],"properties":{"TransactionConfiguration/default/Example":{"key":"TransactionConfiguration/default/Example","value":{"labelValue":"Value"}}},"calculations":[{"type":"TaxAmounts","side":"Side1"}]}] # List[TransactionTypeRequest]
scope = 'default' # str (optional)
api_response = api_instance.set_transaction_type_source(source, transaction_type_request, scope=scope)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source** | **str**| The source to set the transaction types for. | [required] 
 **transaction_type_request** | [**List[TransactionTypeRequest]**](TransactionTypeRequest.md)| The set of transaction types. | [required] 
 **scope** | **str**| The scope in which the transaction types exists. When not supplied the scope is &#39;default&#39;. | [optional] [default to &#39;default&#39;]

### Return type

[**ResourceListOfTransactionType**](ResourceListOfTransactionType.md)

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

