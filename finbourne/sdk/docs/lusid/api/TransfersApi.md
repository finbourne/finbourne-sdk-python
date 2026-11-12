# lusid.TransfersApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_transfer**](TransfersApi.md#create_transfer) | **POST** /api/api/transfers | [EXPERIMENTAL] CreateTransfer: Create a transfer.
[**delete_transfer**](TransfersApi.md#delete_transfer) | **DELETE** /api/api/transfers/{scope}/{code} | [EXPERIMENTAL] DeleteTransfer: Delete a transfer.
[**edit_transfer**](TransfersApi.md#edit_transfer) | **POST** /api/api/transfers/$edit | [EXPERIMENTAL] EditTransfer: Edit a transfer.
[**get_transfer**](TransfersApi.md#get_transfer) | **POST** /api/api/transfers/$get | [EXPERIMENTAL] GetTransfer: Get a transfer
[**list_transfers**](TransfersApi.md#list_transfers) | **GET** /api/api/transfers | [EXPERIMENTAL] ListTransfers: List transfers


### Example

```python
from finbourne.sdk.exceptions import ApiException
from finbourne.sdk.extensions.configuration_options import ConfigurationOptions
from finbourne.sdk.services.lusid.models import *

from finbourne.sdk.extensions import (
  SyncApiClientFactory
)

from finbourne.sdk.services.lusid.api.transfers_api import TransfersApi

# opts = ConfigurationOptions()
# opts.total_timeout_ms = 30_000

# uncomment the below to use an api client factory with overrides
# api_client_factory = SyncApiClientFactory(opts=opts)

api_client_factory = SyncApiClientFactory()
api_instance = api_client_factory.build(TransfersApi)
```

---

# **create_transfer**
> CreateTransferResponse createTransfer = create_transfer(create_transfer_request)

[EXPERIMENTAL] CreateTransfer: Create a transfer.

Move a position between two portfolios, exchange one instrument for another within a portfolio, or do  both at once.  The outgoing and incoming transaction legs and the Transfer entity recording them are written as a single  atomic operation: if any part of the request is rejected, nothing is written.

### Example

```python
api_instance = api_client_factory.build(TransfersApi)
create_transfer_request = CreateTransferRequest()
api_response = api_instance.create_transfer(create_transfer_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_transfer_request** | [**CreateTransferRequest**](../model/CreateTransferRequest.md)| The transfer to create. | [required] 

### Return type

[**CreateTransferResponse**](../model/CreateTransferResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The transfer that was created. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **delete_transfer**
> DeletedEntityResponse deleteTransfer = delete_transfer(scope, code, portfolio_scope_out, portfolio_code_out, portfolio_scope_in, portfolio_code_in)

[EXPERIMENTAL] DeleteTransfer: Delete a transfer.

Delete the Transfer entity recording a transfer and cancel the transaction legs it still has, as a single  atomic operation: if any part of the request is rejected, nothing is changed. A leg that has already gone is  skipped, so a transfer with no legs left can still be deleted to clear the record.                A transfer is identified by its scope, its code and both of its portfolios, so all four are required. Where  no transfer matches all four, the request is reported as not found.

### Example

```python
api_instance = api_client_factory.build(TransfersApi)
scope = 'scope_example' # str
code = 'code_example' # str
portfolio_scope_out = 'portfolio_scope_out_example' # str
portfolio_code_out = 'portfolio_code_out_example' # str
portfolio_scope_in = 'portfolio_scope_in_example' # str
portfolio_code_in = 'portfolio_code_in_example' # str
api_response = api_instance.delete_transfer(scope, code, portfolio_scope_out, portfolio_code_out, portfolio_scope_in, portfolio_code_in)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the transfer. | [required] 
 **code** | **str**| The code of the transfer. Together with the scope and both portfolios this uniquely               identifies the transfer. | [required] 
 **portfolio_scope_out** | **str**| The scope of the portfolio the outgoing leg is booked in. | [required] 
 **portfolio_code_out** | **str**| The code of the portfolio the outgoing leg is booked in. | [required] 
 **portfolio_scope_in** | **str**| The scope of the portfolio the incoming leg is booked in. | [required] 
 **portfolio_code_in** | **str**| The code of the portfolio the incoming leg is booked in. Equal to               portfolioCodeOut for a switch between instruments within one portfolio. | [required] 

### Return type

[**DeletedEntityResponse**](../model/DeletedEntityResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The asAt the deletion landed at. |  -  |
**400** | The details of the input related failure |  -  |
**404** | No transfer with the given scope, code and portfolios. |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **edit_transfer**
> EditTransferResponse editTransfer = edit_transfer(edit_transfer_request, preserve_properties=preserve_properties)

[EXPERIMENTAL] EditTransfer: Edit a transfer.

Replace an existing transfer with the request, which carries the same fields as a create request and is  validated in the same way. Both transaction legs are rebooked under their existing ids and the Transfer  entity is updated, as a single atomic operation: if any part of the request is rejected, nothing is  changed. A field not supplied is cleared, and the outgoing position is checked with the transfer's own  outgoing leg counted back in.                Properties are treated separately from fields: by default, a property not supplied is kept on the  transfer or leg that holds it, and only the properties supplied are updated. A property supplied with a  null value is deleted from the transfer or leg, and is ignored where the transfer or leg does not hold it.  Set preserveProperties to false to replace the whole property set of the transfer and both legs with the  ones supplied; a property supplied with a null value is then ignored.                A transfer is identified by its scope, its code and both of its portfolios, none of which can be changed.  Where no transfer has that scope and code between those portfolios, the request is reported as not found.

### Example

```python
api_instance = api_client_factory.build(TransfersApi)
edit_transfer_request = EditTransferRequest()
preserve_properties = True # bool (optional)
api_response = api_instance.edit_transfer(edit_transfer_request, preserve_properties=preserve_properties)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **edit_transfer_request** | [**EditTransferRequest**](../model/EditTransferRequest.md)| The transfer as it should now stand. | [required] 
 **preserve_properties** | **bool**| If set to false, the entire property set of the transfer and both legs               will be overwritten by the provided properties. If not specified or set to true, only the properties               provided will be updated. | [optional] [default to True]

### Return type

[**EditTransferResponse**](../model/EditTransferResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The transfer that was edited. |  -  |
**400** | The details of the input related failure |  -  |
**404** | No transfer exists with the requested scope, code and portfolios. |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_transfer**
> Transfer getTransfer = get_transfer(get_transfer_request, as_at=as_at)

[EXPERIMENTAL] GetTransfer: Get a transfer

Retrieve a transfer and both of the transactions it booked.  A transfer is identified by its scope, its code and both of its portfolios, so all four are supplied in  the request body rather than in the path.

### Example

```python
api_instance = api_client_factory.build(TransfersApi)
get_transfer_request = GetTransferRequest()
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
api_response = api_instance.get_transfer(get_transfer_request, as_at=as_at)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_transfer_request** | [**GetTransferRequest**](../model/GetTransferRequest.md)| The transfer to retrieve. | [required] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the transfer. Defaults to latest              version if not specified. | [optional] 

### Return type

[**Transfer**](../model/Transfer.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested transfer and both of its transactions. |  -  |
**400** | The details of the input related failure |  -  |
**404** | No transfer exists with the requested scope, code and portfolios. |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **list_transfers**
> ResourceListOfTransfer listTransfers = list_transfers(as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by, property_keys=property_keys)

[EXPERIMENTAL] ListTransfers: List transfers

List transfers matching the specified criteria, decorated with the requested properties.

### Example

```python
api_instance = api_client_factory.build(TransfersApi)
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
page = 'page_example' # str (optional)
limit = 56 # int (optional)
filter = 'filter_example' # str (optional)
sort_by = ['sort_by_example'] # List[str] (optional)
property_keys = ['property_keys_example'] # List[str] (optional)
api_response = api_instance.list_transfers(as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by, property_keys=property_keys)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **as_at** | **datetime**| The asAt datetime at which to retrieve the transfers. Defaults to latest              version if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing transfers from a previous call. | [optional] 
 **limit** | **int**| When paginating, limit the number of returned results to this many. | [optional] 
 **filter** | **str**| Expression to filter the result set. NOTE: Filtering on nested transaction out/in fields is not supported. | [optional] 
 **sort_by** | [**List[str]**](../model/str.md)| A list of field names to sort by, each suffixed by \&quot; ASC\&quot; or \&quot; DESC\&quot;. | [optional] 
 **property_keys** | [**List[str]**](../model/str.md)| The collection of &#x60;PropertyKey&#x60;s to decorate onto each transfer. | [optional] 

### Return type

[**ResourceListOfTransfer**](../model/ResourceListOfTransfer.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A collection of transfers matching the specified criteria. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

