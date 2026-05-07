# lusid.TransactionFeeTypesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_transaction_fee_type**](TransactionFeeTypesApi.md#create_transaction_fee_type) | **POST** /api/api/transactions/transactionfeetypes/{scope}/{code} | [EXPERIMENTAL] CreateTransactionFeeType: Create a transaction fee type
[**delete_transaction_fee_type**](TransactionFeeTypesApi.md#delete_transaction_fee_type) | **DELETE** /api/api/transactions/transactionfeetypes/{scope}/{code} | [EXPERIMENTAL] DeleteTransactionFeeType: Delete a transaction fee type
[**get_transaction_fee_type**](TransactionFeeTypesApi.md#get_transaction_fee_type) | **GET** /api/api/transactions/transactionfeetypes/{scope}/{code} | [EXPERIMENTAL] GetTransactionFeeType: Get a transaction fee type
[**list_transaction_fee_types**](TransactionFeeTypesApi.md#list_transaction_fee_types) | **GET** /api/api/transactions/transactionfeetypes | [EXPERIMENTAL] ListTransactionFeeTypes: List transaction fee types
[**update_transaction_fee_type**](TransactionFeeTypesApi.md#update_transaction_fee_type) | **PUT** /api/api/transactions/transactionfeetypes/{scope}/{code} | [EXPERIMENTAL] UpdateTransactionFeeType: Update a transaction fee type


### Example

```python
from finbourne.sdk.exceptions import ApiException
from finbourne.sdk.extensions.configuration_options import ConfigurationOptions
from finbourne.sdk.services.lusid.models import *

from finbourne.sdk.extensions import (
  SyncApiClientFactory
)

from finbourne.sdk.services.lusid.api.transaction_fee_types_api import TransactionFeeTypesApi

# opts = ConfigurationOptions()
# opts.total_timeout_ms = 30_000

# uncomment the below to use an api client factory with overrides
# api_client_factory = SyncApiClientFactory(opts=opts)

api_client_factory = SyncApiClientFactory()
api_instance = api_client_factory.build(TransactionFeeTypesApi)
```

---

# **create_transaction_fee_type**
> TransactionFeeType createTransactionFeeType = create_transaction_fee_type(scope, code, create_transaction_fee_type_request)

[EXPERIMENTAL] CreateTransactionFeeType: Create a transaction fee type

Create a transaction fee type for the specified scope and code.

### Example

```python
api_instance = api_client_factory.build(TransactionFeeTypesApi)
scope = 'scope_example' # str
code = 'code_example' # str
create_transaction_fee_type_request = CreateTransactionFeeTypeRequest()
api_response = api_instance.create_transaction_fee_type(scope, code, create_transaction_fee_type_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the transaction fee type. | [required] 
 **code** | **str**| The code of the transaction fee type.              Together with the scope this uniquely identifies the transaction fee type. | [required] 
 **create_transaction_fee_type_request** | [**CreateTransactionFeeTypeRequest**](CreateTransactionFeeTypeRequest.md)| The contents of the transaction fee type. | [required] 

### Return type

[**TransactionFeeType**](TransactionFeeType.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The newly created transaction fee type. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **delete_transaction_fee_type**
> DeletedEntityResponse deleteTransactionFeeType = delete_transaction_fee_type(scope, code)

[EXPERIMENTAL] DeleteTransactionFeeType: Delete a transaction fee type

Delete a transaction fee type for the specified scope and code. To note, this will be a monotemporal delete, meaning that  the transaction fee type will be deleted for all effective time (including past and future versions of the transaction fee type).

### Example

```python
api_instance = api_client_factory.build(TransactionFeeTypesApi)
scope = 'scope_example' # str
code = 'code_example' # str
api_response = api_instance.delete_transaction_fee_type(scope, code)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the transaction fee type. | [required] 
 **code** | **str**| The code of the specified transaction fee type.              Together with the scope this uniquely identifies the transaction fee type. | [required] 

### Return type

[**DeletedEntityResponse**](DeletedEntityResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Delete a transaction fee type. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_transaction_fee_type**
> TransactionFeeType getTransactionFeeType = get_transaction_fee_type(scope, code, effective_at=effective_at, as_at=as_at, property_keys=property_keys)

[EXPERIMENTAL] GetTransactionFeeType: Get a transaction fee type

Get the transaction fee type for the specified scope and code.

### Example

```python
api_instance = api_client_factory.build(TransactionFeeTypesApi)
scope = 'scope_example' # str
code = 'code_example' # str
effective_at = 'effective_at_example' # str (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
property_keys = ['property_keys_example'] # List[str] (optional)
api_response = api_instance.get_transaction_fee_type(scope, code, effective_at=effective_at, as_at=as_at, property_keys=property_keys)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the transaction fee type. | [required] 
 **code** | **str**| The code of the transaction fee type.              Together with the scope this uniquely identifies the transaction fee type. | [required] 
 **effective_at** | **str**| The effective datetime at which to retrieve the transaction fee type properties.              Defaults to the current LUSID system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the transaction fee types.              Defaults to latest if not specified. | [optional] 
 **property_keys** | [**List[str]**](str.md)| The collection of &#x60;PropertyKey&#x60;s that we want to decorate on the transaction fee type. | [optional] 

### Return type

[**TransactionFeeType**](TransactionFeeType.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The transaction fee type matching the specified scope and code. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **list_transaction_fee_types**
> ResourceListOfTransactionFeeType listTransactionFeeTypes = list_transaction_fee_types(effective_at=effective_at, as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by, property_keys=property_keys)

[EXPERIMENTAL] ListTransactionFeeTypes: List transaction fee types

List transaction fee types that match the specified criteria.

### Example

```python
api_instance = api_client_factory.build(TransactionFeeTypesApi)
effective_at = 'effective_at_example' # str (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
page = 'page_example' # str (optional)
limit = 56 # int (optional)
filter = 'filter_example' # str (optional)
sort_by = ['sort_by_example'] # List[str] (optional)
property_keys = ['property_keys_example'] # List[str] (optional)
api_response = api_instance.list_transaction_fee_types(effective_at=effective_at, as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by, property_keys=property_keys)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **effective_at** | **str**| The effective datetime at which to retrieve transaction fee type properties.              Defaults to the current LUSID system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the transaction fee types.              Defaults to latest if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing transaction fee types from a previous call to list transaction fee types.  This value is returned from the previous call. If a pagination token is provided the filter,  sortBy, effectiveAt and asAt field must not have changed since the original request. | [optional] 
 **limit** | **int**| When paginating, limit the number of returned results to this many. Defaults to 100 if not specified. | [optional] 
 **filter** | **str**| Expression to filter the result set.              For example, to filter on the Scope, use \&quot;scope eq &#39;ExampleScope&#39;\&quot;              Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. | [optional] 
 **sort_by** | [**List[str]**](str.md)| A list of field names to sort by, each suffixed by \&quot; ASC\&quot; or \&quot; DESC\&quot; | [optional] 
 **property_keys** | [**List[str]**](str.md)| The collection of &#x60;PropertyKey&#x60;s to filter on | [optional] 

### Return type

[**ResourceListOfTransactionFeeType**](ResourceListOfTransactionFeeType.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A collection of transaction fee types matching the specified criteria. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **update_transaction_fee_type**
> TransactionFeeType updateTransactionFeeType = update_transaction_fee_type(scope, code, update_transaction_fee_type_request)

[EXPERIMENTAL] UpdateTransactionFeeType: Update a transaction fee type

Update a transaction fee type by providing the new contents of the transaction fee type.  The displayName field cannot be updated.

### Example

```python
api_instance = api_client_factory.build(TransactionFeeTypesApi)
scope = 'scope_example' # str
code = 'code_example' # str
update_transaction_fee_type_request = UpdateTransactionFeeTypeRequest()
api_response = api_instance.update_transaction_fee_type(scope, code, update_transaction_fee_type_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the transaction fee type. | [required] 
 **code** | **str**| The code of the specified transaction fee type.              Together with the scope this uniquely identifies the transaction fee type. | [required] 
 **update_transaction_fee_type_request** | [**UpdateTransactionFeeTypeRequest**](UpdateTransactionFeeTypeRequest.md)| The updated contents of the transaction fee type. | [required] 

### Return type

[**TransactionFeeType**](TransactionFeeType.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated transaction fee type. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

