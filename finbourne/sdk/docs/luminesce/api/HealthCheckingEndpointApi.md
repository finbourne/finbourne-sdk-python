# luminesce.HealthCheckingEndpointApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fake_node_reclaim**](HealthCheckingEndpointApi.md#fake_node_reclaim) | **GET** /honeycomb/fakeNodeReclaim | [INTERNAL] FakeNodeReclaim: Helps testing of AWS node reclaim behaviour


### Example

```python
from finbourne.sdk.exceptions import ApiException
from finbourne.sdk.extensions.configuration_options import ConfigurationOptions
from finbourne.sdk.services.luminesce.models import *

from finbourne.sdk.extensions import (
  SyncApiClientFactory
)

from finbourne.sdk.services.luminesce.api.health_checking_endpoint_api import HealthCheckingEndpointApi

# opts = ConfigurationOptions()
# opts.total_timeout_ms = 30_000

# uncomment the below to use an api client factory with overrides
# api_client_factory = SyncApiClientFactory(opts=opts)

api_client_factory = SyncApiClientFactory()
api_instance = api_client_factory.build(HealthCheckingEndpointApi)
```

---

# **fake_node_reclaim**
> object fakeNodeReclaim = fake_node_reclaim(seconds_until_reclaim=seconds_until_reclaim)

[INTERNAL] FakeNodeReclaim: Helps testing of AWS node reclaim behaviour

 An internal Method used to mark the next SIGTERM as though an Aws Node reclaim were about to take place. Simulates having received an AWS node reclaim warning, or similar.

### Example

```python
api_instance = api_client_factory.build(HealthCheckingEndpointApi)
seconds_until_reclaim = 119 # int (optional)
api_response = api_instance.fake_node_reclaim(seconds_until_reclaim=seconds_until_reclaim)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **seconds_until_reclaim** | **int**| the number of seconds from which to assume node termination | [optional] [default to 119]

### Return type

**object**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

