# lusid.TransactionTransactionFeesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_transaction_fee**](TransactionTransactionFeesApi.md#create_transaction_fee) | **POST** /api/api/transactions/transactionfees/{scope}/{code} | [EXPERIMENTAL] CreateTransactionFee: Create a TransactionFee
[**delete_transaction_fee**](TransactionTransactionFeesApi.md#delete_transaction_fee) | **DELETE** /api/api/transactions/transactionfees/{scope}/{code} | [EXPERIMENTAL] DeleteTransactionFee: Delete a TransactionFee
[**get_transaction_fee**](TransactionTransactionFeesApi.md#get_transaction_fee) | **GET** /api/api/transactions/transactionfees/{scope}/{code} | [EXPERIMENTAL] GetTransactionFee: Get a TransactionFee
[**list_transaction_fees**](TransactionTransactionFeesApi.md#list_transaction_fees) | **GET** /api/api/transactions/transactionfees | [EXPERIMENTAL] ListTransactionFees: List TransactionFees
[**update_transaction_fee**](TransactionTransactionFeesApi.md#update_transaction_fee) | **PUT** /api/api/transactions/transactionfees/{scope}/{code} | [EXPERIMENTAL] UpdateTransactionFee: Update a TransactionFee


### Example

```python
from finbourne.sdk.exceptions import ApiException
from finbourne.sdk.extensions.configuration_options import ConfigurationOptions
from finbourne.sdk.services.lusid.models import *

from finbourne.sdk.extensions import (
  SyncApiClientFactory
)

from finbourne.sdk.services.lusid.api.transaction_transaction_fees_api import TransactionTransactionFeesApi

# opts = ConfigurationOptions()
# opts.total_timeout_ms = 30_000

# uncomment the below to use an api client factory with overrides
# api_client_factory = SyncApiClientFactory(opts=opts)

api_client_factory = SyncApiClientFactory()
api_instance = api_client_factory.build(TransactionTransactionFeesApi)
```

---

# **create_transaction_fee**
> TransactionFee createTransactionFee = create_transaction_fee(scope, code, create_transaction_fee_request, effective_at=effective_at)

[EXPERIMENTAL] CreateTransactionFee: Create a TransactionFee

Create a TransactionFee for the specified scope and code.

### Example

```python
api_instance = api_client_factory.build(TransactionTransactionFeesApi)
scope = 'scope_example' # str
code = 'code_example' # str
create_transaction_fee_request = CreateTransactionFeeRequest()
effective_at = 'effective_at_example' # str (optional)
api_response = api_instance.create_transaction_fee(scope, code, create_transaction_fee_request, effective_at=effective_at)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the TransactionFee. | [required] 
 **code** | **str**| The code of the TransactionFee.              Together with the scope this uniquely identifies the TransactionFee. | [required] 
 **create_transaction_fee_request** | [**CreateTransactionFeeRequest**](CreateTransactionFeeRequest.md)| The contents of the TransactionFee. | [required] 
 **effective_at** | **str**| The date and time at which the TransactionFee should be effective. | [optional] 

### Return type

[**TransactionFee**](TransactionFee.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The newly created TransactionFee. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **delete_transaction_fee**
> DeletedEntityResponse deleteTransactionFee = delete_transaction_fee(scope, code)

[EXPERIMENTAL] DeleteTransactionFee: Delete a TransactionFee

Delete a TransactionFee for the specified scope and code. To note, this will be a monotemporal delete, meaning that  the TransactionFee will be deleted for all effective time (including past and future versions of the TransactionFee).

### Example

```python
api_instance = api_client_factory.build(TransactionTransactionFeesApi)
scope = 'scope_example' # str
code = 'code_example' # str
api_response = api_instance.delete_transaction_fee(scope, code)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the TransactionFee. | [required] 
 **code** | **str**| The code of the specified TransactionFee.              Together with the scope this uniquely identifies the TransactionFee. | [required] 

### Return type

[**DeletedEntityResponse**](DeletedEntityResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Delete a TransactionFee. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_transaction_fee**
> TransactionFee getTransactionFee = get_transaction_fee(scope, code, effective_at=effective_at, as_at=as_at, property_keys=property_keys)

[EXPERIMENTAL] GetTransactionFee: Get a TransactionFee

Get the TransactionFee for the specified scope and code.

### Example

```python
api_instance = api_client_factory.build(TransactionTransactionFeesApi)
scope = 'scope_example' # str
code = 'code_example' # str
effective_at = 'effective_at_example' # str (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
property_keys = ['property_keys_example'] # List[str] (optional)
api_response = api_instance.get_transaction_fee(scope, code, effective_at=effective_at, as_at=as_at, property_keys=property_keys)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the TransactionFee. | [required] 
 **code** | **str**| The code of the TransactionFee.              Together with the scope this uniquely identifies the TransactionFee. | [required] 
 **effective_at** | **str**| The date and time at which the query is effective. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the TransactionFees.              Defaults to latest if not specified. | [optional] 
 **property_keys** | [**List[str]**](str.md)| The collection of &#x60;PropertyKey&#x60;s that we want to decorate on identifies the TransactionFee. | [optional] 

### Return type

[**TransactionFee**](TransactionFee.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The TransactionFee matching the specified scope and code. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **list_transaction_fees**
> ResourceListOfTransactionFee listTransactionFees = list_transaction_fees(effective_at=effective_at, as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by, property_keys=property_keys)

[EXPERIMENTAL] ListTransactionFees: List TransactionFees

List TransactionFees that match the specified criteria.

### Example

```python
api_instance = api_client_factory.build(TransactionTransactionFeesApi)
effective_at = 'effective_at_example' # str (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
page = 'page_example' # str (optional)
limit = 56 # int (optional)
filter = 'filter_example' # str (optional)
sort_by = ['sort_by_example'] # List[str] (optional)
property_keys = ['property_keys_example'] # List[str] (optional)
api_response = api_instance.list_transaction_fees(effective_at=effective_at, as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by, property_keys=property_keys)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **effective_at** | **str**| The date and time at which the query is effective. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the TransactionFees.              Defaults to latest if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing TransactionFees from a previous call to list TransactionFees.  This value is returned from the previous call. If a pagination token is provided the filter,  sortBy and asAt field must not have changed since the original request. | [optional] 
 **limit** | **int**| When paginating, limit the number of returned results to this many. Defaults to 100 if not specified. | [optional] 
 **filter** | **str**| Expression to filter the result set.              For example, to filter on the Scope, use \&quot;scope eq &#39;ExampleScope&#39;\&quot;              Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. | [optional] 
 **sort_by** | [**List[str]**](str.md)| A list of field names to sort by, each suffixed by \&quot; ASC\&quot; or \&quot; DESC\&quot; | [optional] 
 **property_keys** | [**List[str]**](str.md)| The collection of &#x60;PropertyKey&#x60;s to filter on | [optional] 

### Return type

[**ResourceListOfTransactionFee**](ResourceListOfTransactionFee.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A collection of TransactionFees matching the specified criteria. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **update_transaction_fee**
> TransactionFee updateTransactionFee = update_transaction_fee(scope, code, update_transaction_fee_request, effective_at=effective_at)

[EXPERIMENTAL] UpdateTransactionFee: Update a TransactionFee

Update a TransactionFee by providing the new contents of the TransactionFee.  The name field and the capitalisation field can not be updated.

### Example

```python
api_instance = api_client_factory.build(TransactionTransactionFeesApi)
scope = 'scope_example' # str
code = 'code_example' # str
update_transaction_fee_request = UpdateTransactionFeeRequest()
effective_at = 'effective_at_example' # str (optional)
api_response = api_instance.update_transaction_fee(scope, code, update_transaction_fee_request, effective_at=effective_at)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the TransactionFee. | [required] 
 **code** | **str**| The code of the specified TransactionFee.              Together with the scope this uniquely identifies the TransactionFee. | [required] 
 **update_transaction_fee_request** | [**UpdateTransactionFeeRequest**](UpdateTransactionFeeRequest.md)| The contents of the TransactionFee. | [required] 
 **effective_at** | **str**| The date and time at which the update should take effect.             The updated contents of the TransactionFee. | [optional] 

### Return type

[**TransactionFee**](TransactionFee.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated TransactionFee. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

