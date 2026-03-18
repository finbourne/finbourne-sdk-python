# lusid.OrderInstructionsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_order_instruction**](OrderInstructionsApi.md#delete_order_instruction) | **DELETE** /api/api/orderinstructions/{scope}/{code} | DeleteOrderInstruction: Delete orderInstruction
[**get_order_instruction**](OrderInstructionsApi.md#get_order_instruction) | **GET** /api/api/orderinstructions/{scope}/{code} | GetOrderInstruction: Get OrderInstruction
[**list_order_instructions**](OrderInstructionsApi.md#list_order_instructions) | **GET** /api/api/orderinstructions | ListOrderInstructions: List OrderInstructions
[**upsert_order_instructions**](OrderInstructionsApi.md#upsert_order_instructions) | **POST** /api/api/orderinstructions | UpsertOrderInstructions: Upsert OrderInstruction


### Example

```python
from finbourne.sdk.exceptions import ApiException
from finbourne.sdk.extensions.configuration_options import ConfigurationOptions
from finbourne.sdk.services.lusid.models import *

from finbourne.sdk.extensions import (
  SyncApiClientFactory
)

from finbourne.sdk.services.lusid.api.order_instructions_api import OrderInstructionsApi

# opts = ConfigurationOptions()
# opts.total_timeout_ms = 30_000

# uncomment the below to use an api client factory with overrides
# api_client_factory = SyncApiClientFactory(opts=opts)

api_client_factory = SyncApiClientFactory()
api_instance = api_client_factory.build(OrderInstructionsApi)
```

---

# **delete_order_instruction**
> DeletedEntityResponse deleteOrderInstruction = delete_order_instruction(scope, code)

DeleteOrderInstruction: Delete orderInstruction

Delete an orderInstruction. Deletion will be valid from the orderInstruction's creation datetime.  This means that the orderInstruction will no longer exist at any effective datetime from the asAt datetime of deletion.

### Example

```python
api_instance = api_client_factory.build(OrderInstructionsApi)
scope = 'scope_example' # str
code = 'code_example' # str
api_response = api_instance.delete_order_instruction(scope, code)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The orderInstruction scope. | [required] 
 **code** | **str**| The orderInstruction&#39;s code. This, together with the scope uniquely identifies the orderInstruction to delete. | [required] 

### Return type

[**DeletedEntityResponse**](DeletedEntityResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response from deleting an orderInstruction. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_order_instruction**
> OrderInstruction getOrderInstruction = get_order_instruction(scope, code, as_at=as_at, property_keys=property_keys)

GetOrderInstruction: Get OrderInstruction

Fetch a OrderInstruction that matches the specified identifier

### Example

```python
api_instance = api_client_factory.build(OrderInstructionsApi)
scope = 'scope_example' # str
code = 'code_example' # str
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
property_keys = ['property_keys_example'] # List[str] (optional)
api_response = api_instance.get_order_instruction(scope, code, as_at=as_at, property_keys=property_keys)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope to which the orderInstruction belongs. | [required] 
 **code** | **str**| The orderInstruction&#39;s unique identifier. | [required] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the orderInstruction. Defaults to return the latest version of the orderInstruction if not specified. | [optional] 
 **property_keys** | [**List[str]**](str.md)| A list of property keys from the \&quot;OrderInstruction\&quot; domain to decorate onto the orderInstruction.              These take the format {domain}/{scope}/{code} e.g. \&quot;OrderInstruction/system/Name\&quot;. | [optional] 

### Return type

[**OrderInstruction**](OrderInstruction.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The orderInstruction matching the given identifier. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **list_order_instructions**
> PagedResourceListOfOrderInstruction listOrderInstructions = list_order_instructions(as_at=as_at, page=page, sort_by=sort_by, limit=limit, filter=filter, property_keys=property_keys)

ListOrderInstructions: List OrderInstructions

Fetch the last pre-AsAt date version of each orderInstruction in scope (does not fetch the entire history).

### Example

```python
api_instance = api_client_factory.build(OrderInstructionsApi)
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
page = 'page_example' # str (optional)
sort_by = ['sort_by_example'] # List[str] (optional)
limit = 56 # int (optional)
filter = 'filter_example' # str (optional)
property_keys = ['property_keys_example'] # List[str] (optional)
api_response = api_instance.list_order_instructions(as_at=as_at, page=page, sort_by=sort_by, limit=limit, filter=filter, property_keys=property_keys)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **as_at** | **datetime**| The asAt datetime at which to retrieve the orderInstruction. Defaults to return the latest version of the orderInstruction if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing orderInstructions from a previous call to list orderInstructions.              This value is returned from the previous call. If a pagination token is provided the sortBy, filter, effectiveAt, and asAt fields              must not have changed since the original request. | [optional] 
 **sort_by** | [**List[str]**](str.md)| A list of field names or properties to sort by, each suffixed by \&quot; ASC\&quot; or \&quot; DESC\&quot;. | [optional] 
 **limit** | **int**| When paginating, limit the number of returned results to this many. | [optional] 
 **filter** | **str**| Expression to filter the result set. Read more about filtering results from LUSID here:              https://support.lusid.com/filtering-results-from-lusid. | [optional] 
 **property_keys** | [**List[str]**](str.md)| A list of property keys from the \&quot;OrderInstruction\&quot; domain to decorate onto each orderInstruction.                  These take the format {domain}/{scope}/{code} e.g. \&quot;OrderInstruction/system/Name\&quot;.                  All properties, except derived properties, are returned by default, without specifying here. | [optional] 

### Return type

[**PagedResourceListOfOrderInstruction**](PagedResourceListOfOrderInstruction.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OrderInstructions in scope. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **upsert_order_instructions**
> ResourceListOfOrderInstruction upsertOrderInstructions = upsert_order_instructions(order_instruction_set_request=order_instruction_set_request)

UpsertOrderInstructions: Upsert OrderInstruction

Upsert; update existing orderInstructions with given ids, or create new orderInstructions otherwise.

### Example

```python
api_instance = api_client_factory.build(OrderInstructionsApi)
order_instruction_set_request = OrderInstructionSetRequest()
api_response = api_instance.upsert_order_instructions(order_instruction_set_request=order_instruction_set_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_instruction_set_request** | [**OrderInstructionSetRequest**](OrderInstructionSetRequest.md)| The collection of orderInstruction requests. | [optional] 

### Return type

[**ResourceListOfOrderInstruction**](ResourceListOfOrderInstruction.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | A collection of orderInstructions. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

