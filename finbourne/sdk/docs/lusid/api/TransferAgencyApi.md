# lusid.TransferAgencyApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**calculate_order_dates**](TransferAgencyApi.md#calculate_order_dates) | **POST** /api/api/transferagency/orderdates | [EXPERIMENTAL] CalculateOrderDates: Calculate the key dates associated with transfer agency orders


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
 **request_body** | [**Dict[str, CalculateOrderDatesRequest]**](CalculateOrderDatesRequest.md)| The request containing the dates used for calculation | [required] 

### Return type

[**CalculateOrderDatesResponse**](CalculateOrderDatesResponse.md)

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

