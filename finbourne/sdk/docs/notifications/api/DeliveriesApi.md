# notifications.DeliveriesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_deliveries**](DeliveriesApi.md#list_deliveries) | **GET** /notification/api/deliveries | ListDeliveries: List Deliveries


### Example

```python
from finbourne.sdk.exceptions import ApiException
from finbourne.sdk.extensions.configuration_options import ConfigurationOptions
from finbourne.sdk.services.notifications.models import *

from finbourne.sdk.extensions import (
  SyncApiClientFactory
)

from finbourne.sdk.services.notifications.api.deliveries_api import DeliveriesApi

# opts = ConfigurationOptions()
# opts.total_timeout_ms = 30_000

# uncomment the below to use an api client factory with overrides
# api_client_factory = SyncApiClientFactory(opts=opts)

api_client_factory = SyncApiClientFactory()
api_instance = api_client_factory.build(DeliveriesApi)
```

---

# **list_deliveries**
> ResourceListOfDelivery listDeliveries = list_deliveries(page=page, limit=limit, filter=filter)

ListDeliveries: List Deliveries

Currently only returns deliveries with failed attempts.

### Example

```python
api_instance = api_client_factory.build(DeliveriesApi)
page = 'page_example' # str (optional)
limit = 56 # int (optional)
filter = 'filter_example' # str (optional)
api_response = api_instance.list_deliveries(page=page, limit=limit, filter=filter)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **str**| The pagination token to use to continue listing delivery attempts. This value is returned from the previous call. When this field is supplied the filter field should not be supplied. | [optional] 
 **limit** | **int**| The maximum number of delivery attempts to retrieve. Defaults to 200 if not specified. | [optional] 
 **filter** | **str**| Expression to filter the result set. For more information about filtering results, see https://support.lusid.com/knowledgebase/article/KA-01914. By default, we set this filter to only query for the last week&#39;s worth of Deliveries, however if a filter is explicitly set, this will be overriden. An example filter to override the attempt time date might be &#39;AttemptTime gt 2023-08-25&#39; for example | [optional] 

### Return type

[**ResourceListOfDelivery**](ResourceListOfDelivery.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | The details of the input related failure |  -  |
**404** | No deliveries exists with the provided filter(s) |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

