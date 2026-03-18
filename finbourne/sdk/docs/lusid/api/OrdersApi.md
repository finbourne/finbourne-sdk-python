# lusid.OrdersApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_order**](OrdersApi.md#delete_order) | **DELETE** /api/api/orders/{scope}/{code} | [EARLY ACCESS] DeleteOrder: Delete order
[**get_order**](OrdersApi.md#get_order) | **GET** /api/api/orders/{scope}/{code} | [EARLY ACCESS] GetOrder: Get Order
[**list_orders**](OrdersApi.md#list_orders) | **GET** /api/api/orders | ListOrders: List Orders
[**upsert_orders**](OrdersApi.md#upsert_orders) | **POST** /api/api/orders | UpsertOrders: Upsert Order


### Example

```python
from finbourne.sdk.exceptions import ApiException
from finbourne.sdk.extensions.configuration_options import ConfigurationOptions
from finbourne.sdk.services.lusid.models import *

from finbourne.sdk.extensions import (
  SyncApiClientFactory
)

from finbourne.sdk.services.lusid.api.orders_api import OrdersApi

# opts = ConfigurationOptions()
# opts.total_timeout_ms = 30_000

# uncomment the below to use an api client factory with overrides
# api_client_factory = SyncApiClientFactory(opts=opts)

api_client_factory = SyncApiClientFactory()
api_instance = api_client_factory.build(OrdersApi)
```

---

# **delete_order**
> DeletedEntityResponse deleteOrder = delete_order(scope, code)

[EARLY ACCESS] DeleteOrder: Delete order

Delete an order. Deletion will be valid from the order's creation datetime.  This means that the order will no longer exist at any effective datetime from the asAt datetime of deletion.

### Example

```python
api_instance = api_client_factory.build(OrdersApi)
scope = 'scope_example' # str
code = 'code_example' # str
api_response = api_instance.delete_order(scope, code)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The order scope. | [required] 
 **code** | **str**| The order&#39;s code. This, together with the scope uniquely identifies the order to delete. | [required] 

### Return type

[**DeletedEntityResponse**](DeletedEntityResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response from deleting an order. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_order**
> Order getOrder = get_order(scope, code, as_at=as_at, property_keys=property_keys)

[EARLY ACCESS] GetOrder: Get Order

Fetch an Order that matches the specified identifier.

### Example

```python
api_instance = api_client_factory.build(OrdersApi)
scope = 'scope_example' # str
code = 'code_example' # str
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
property_keys = ['property_keys_example'] # List[str] (optional)
api_response = api_instance.get_order(scope, code, as_at=as_at, property_keys=property_keys)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope to which the order belongs. | [required] 
 **code** | **str**| The order&#39;s unique identifier. | [required] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the order. Defaults to return the latest version of the order if not specified. | [optional] 
 **property_keys** | [**List[str]**](str.md)| A list of property keys from the \&quot;Orders\&quot; domain to decorate onto the order.              These take the format {domain}/{scope}/{code} e.g. \&quot;Orders/system/Name\&quot;. | [optional] 

### Return type

[**Order**](Order.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The order matching the given identifier. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **list_orders**
> PagedResourceListOfOrder listOrders = list_orders(as_at=as_at, page=page, sort_by=sort_by, limit=limit, filter=filter, property_keys=property_keys, data_model_scope=data_model_scope, data_model_code=data_model_code, membership_type=membership_type)

ListOrders: List Orders

Fetch the last pre-AsAt date version of each order with optional filtering (does not fetch the entire history).

### Example

```python
api_instance = api_client_factory.build(OrdersApi)
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
page = 'page_example' # str (optional)
sort_by = ['sort_by_example'] # List[str] (optional)
limit = 56 # int (optional)
filter = 'filter_example' # str (optional)
property_keys = ['property_keys_example'] # List[str] (optional)
data_model_scope = 'data_model_scope_example' # str (optional)
data_model_code = 'data_model_code_example' # str (optional)
membership_type = 'membership_type_example' # str (optional)
api_response = api_instance.list_orders(as_at=as_at, page=page, sort_by=sort_by, limit=limit, filter=filter, property_keys=property_keys, data_model_scope=data_model_scope, data_model_code=data_model_code, membership_type=membership_type)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **as_at** | **datetime**| The asAt datetime at which to retrieve the order. Defaults to return the latest version of the order if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing orders from a previous call to list orders.              This value is returned from the previous call. If a pagination token is provided the sortBy, filter, effectiveAt, and asAt fields              must not have changed since the original request. | [optional] 
 **sort_by** | [**List[str]**](str.md)| A list of field names or properties to sort by, each suffixed by \&quot; ASC\&quot; or \&quot; DESC\&quot;. | [optional] 
 **limit** | **int**| When paginating, limit the number of returned results to this many. | [optional] 
 **filter** | **str**| Expression to filter the result set. Read more about filtering results from LUSID here:              https://support.lusid.com/filtering-results-from-lusid. | [optional] 
 **property_keys** | [**List[str]**](str.md)| A list of property keys from the \&quot;Orders\&quot; domain to decorate onto each order.                  These take the format {domain}/{scope}/{code} e.g. \&quot;Orders/system/Name\&quot;.                  All properties, except derived properties, are returned by default, without specifying here. | [optional] 
 **data_model_scope** | **str**| The optional scope of a Custom Data Model to use | [optional] 
 **data_model_code** | **str**| The optional code of a Custom Data Model to use | [optional] 
 **membership_type** | **str**| The membership types of the specified Custom Data Model to return. Allowable values are Member, Candidate and All. Defaults to Member. | [optional] 

### Return type

[**PagedResourceListOfOrder**](PagedResourceListOfOrder.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Orders. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **upsert_orders**
> ResourceListOfOrder upsertOrders = upsert_orders(order_set_request, data_model_scope=data_model_scope, data_model_code=data_model_code)

UpsertOrders: Upsert Order

Upsert; update existing orders with given ids, or create new orders otherwise.

### Example

```python
api_instance = api_client_factory.build(OrdersApi)
order_set_request = OrderSetRequest()
data_model_scope = 'data_model_scope_example' # str (optional)
data_model_code = 'data_model_code_example' # str (optional)
api_response = api_instance.upsert_orders(order_set_request, data_model_scope=data_model_scope, data_model_code=data_model_code)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_set_request** | [**OrderSetRequest**](OrderSetRequest.md)| The collection of order requests. | [required] 
 **data_model_scope** | **str**| The optional scope of a Custom Data Model to use | [optional] 
 **data_model_code** | **str**| The optional code of a Custom Data Model to use | [optional] 

### Return type

[**ResourceListOfOrder**](ResourceListOfOrder.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | A collection of orders. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

