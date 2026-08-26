# lusid.TransferAgencyApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**calculate_order_dates**](TransferAgencyApi.md#calculate_order_dates) | **POST** /api/api/transferagency/orderdates | [EXPERIMENTAL] CalculateOrderDates: Calculate the key dates associated with transfer agency orders
[**delete_transfer_agency_orders**](TransferAgencyApi.md#delete_transfer_agency_orders) | **POST** /api/api/transferagency/orders/$delete | [EXPERIMENTAL] DeleteTransferAgencyOrders: Delete transfer agency orders
[**upsert_transfer_agency_orders**](TransferAgencyApi.md#upsert_transfer_agency_orders) | **POST** /api/api/transferagency/orders | [EXPERIMENTAL] UpsertTransferAgencyOrders: Upsert transfer agency orders


### Example

```python
from finbourne.sdk.exceptions import ApiException
from finbourne.sdk.extensions.configuration_options import ConfigurationOptions
from finbourne.sdk.services.lusid.models import *

from finbourne.sdk.extensions import (
  SyncApiClientFactory
)

from finbourne.sdk.services.lusid.api.transfer_agency_api import TransferAgencyApi

# opts = ConfigurationOptions()
# opts.total_timeout_ms = 30_000

# uncomment the below to use an api client factory with overrides
# api_client_factory = SyncApiClientFactory(opts=opts)

api_client_factory = SyncApiClientFactory()
api_instance = api_client_factory.build(TransferAgencyApi)
```

---

# **calculate_order_dates**
> CalculateOrderDatesResponse calculateOrderDates = calculate_order_dates(request_body)

[EXPERIMENTAL] CalculateOrderDates: Calculate the key dates associated with transfer agency orders

The response contains both the collection of successfully calculated dates and any failed calculations,  each in the form of a dictionary keyed by the request's keys.  For each failure, a reason is provided. It is important to check the failed set for unsuccessful results.

### Example

```python
api_instance = api_client_factory.build(TransferAgencyApi)
request_body = {"calculation1":{"instrumentIdentifierType":"LusidInstrumentId","instrumentIdentifier":"LUID_00000000","instrumentScope":"MyScope","receivedDate":"2024-10-01T00:00:00.0000000+00:00","transactionCategory":"Subscription"}} # Dict[str, CalculateOrderDatesRequest]
api_response = api_instance.calculate_order_dates(request_body)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**Dict[str, CalculateOrderDatesRequest]**](../model/CalculateOrderDatesRequest.md)| The request containing the dates used for calculation | [required] 

### Return type

[**CalculateOrderDatesResponse**](../model/CalculateOrderDatesResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully calculated dates and any failed calculations. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **delete_transfer_agency_orders**
> DeleteTransferAgencyOrdersResponse deleteTransferAgencyOrders = delete_transfer_agency_orders(request_body)

[EXPERIMENTAL] DeleteTransferAgencyOrders: Delete transfer agency orders

Deletes each order supplied, cancelling any cash transaction(s) already booked for it. Only an order in  'New' or 'Pending' can be deleted. A priced order must be un-priced first. An order with no cash transaction  booked against it is deleted successfully and reports no cancelled transactions. Transaction staging rules are not applied to these  cancellations.  The response contains both successfully deleted orders and any failures, each in the form of a  dictionary keyed by the request's keys. For each failure, a reason is provided. It is important to  check the failed set for unsuccessful results.

### Example

```python
api_instance = api_client_factory.build(TransferAgencyApi)
request_body = {"Order1":{"orderId":{"scope":"example-scope","code":"order-1"}}} # Dict[str, DeleteTransferAgencyOrderRequest]
api_response = api_instance.delete_transfer_agency_orders(request_body)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**Dict[str, DeleteTransferAgencyOrderRequest]**](../model/DeleteTransferAgencyOrderRequest.md)| The transfer agency orders to delete, keyed by a unique request identifier. | [required] 

### Return type

[**DeleteTransferAgencyOrdersResponse**](../model/DeleteTransferAgencyOrdersResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully deleted orders and any failures. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **upsert_transfer_agency_orders**
> TransferAgencyOrdersResponse upsertTransferAgencyOrders = upsert_transfer_agency_orders(request_body)

[EXPERIMENTAL] UpsertTransferAgencyOrders: Upsert transfer agency orders

Creates a transaction and updates the relevant order for each order supplied.  The response contains both successfully processed orders and any failures, each in the form of a  dictionary keyed by the request's keys. For each failure, a reason is provided. It is important to  check the failed set for unsuccessful results.

### Example

```python
api_instance = api_client_factory.build(TransferAgencyApi)
request_body = {"Order1":{"orderId":{"scope":"example-scope","code":"order-1"}}} # Dict[str, UpsertTransferAgencyOrderRequest]
api_response = api_instance.upsert_transfer_agency_orders(request_body)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**Dict[str, UpsertTransferAgencyOrderRequest]**](../model/UpsertTransferAgencyOrderRequest.md)| The transfer agency orders to upsert, keyed by a unique request identifier. | [required] 

### Return type

[**TransferAgencyOrdersResponse**](../model/TransferAgencyOrdersResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully processed orders and any failures. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

