# lusid.TransfersApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_transfer**](TransfersApi.md#create_transfer) | **POST** /api/api/transfers | [EXPERIMENTAL] CreateTransfer: Create a transfer.


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

Move a position between two portfolios, exchange one instrument for another within a portfolio, or do  both at once.                The outgoing and incoming transaction legs and the Transfer entity recording them are written as a single  atomic operation: if any part of the request is rejected, nothing is written.

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

