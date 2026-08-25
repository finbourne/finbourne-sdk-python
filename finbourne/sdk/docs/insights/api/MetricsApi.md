# insights.MetricsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_metrics**](MetricsApi.md#get_metrics) | **GET** /insights/api/metrics | [EARLY ACCESS] GetMetrics: Get the aggregated platform metrics for the caller&#39;s domain.


### Example

```python
from finbourne.sdk.exceptions import ApiException
from finbourne.sdk.extensions.configuration_options import ConfigurationOptions
from finbourne.sdk.services.insights.models import *

from finbourne.sdk.extensions import (
  SyncApiClientFactory
)

from finbourne.sdk.services.insights.api.metrics_api import MetricsApi

# opts = ConfigurationOptions()
# opts.total_timeout_ms = 30_000

# uncomment the below to use an api client factory with overrides
# api_client_factory = SyncApiClientFactory(opts=opts)

api_client_factory = SyncApiClientFactory()
api_instance = api_client_factory.build(MetricsApi)
```

---

# **get_metrics**
> MetricsResponse getMetrics = get_metrics(include=include)

[EARLY ACCESS] GetMetrics: Get the aggregated platform metrics for the caller's domain.

 Returns request volumes, error rates and duration distributions for the domain's services, plus its identity             population and activity counts. The domain is taken from the authenticated request, never from a parameter.  <b>This endpoint is slow by design.</b> It runs several analytical queries in parallel and commonly takes             upwards of thirty seconds when the underlying data is cold. The server abandons a data set that has not             completed within its configured budget and reports it in `failed`, so a call returns rather than hanging             indefinitely; allow comfortably more than that budget on the client, and do not call this on a             user-interactive code path without showing progress.  Partial success is normal and is still reported as a `200`. A data set that could not be retrieved is             null in the response and named in `failed` with a reason; a data set excluded via             include is null and named in `notIncluded`. Render a null data set as unavailable             rather than as an absence of activity.

### Example

```python
api_instance = api_client_factory.build(MetricsApi)
include = ['include_example'] # List[str] (optional)
api_response = api_instance.get_metrics(include=include)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include** | [**List[str]**](../model/str.md)| The data sets to return, by name. Omit to return all of them. Repeat the parameter to request several, for example &#x60;?include&#x3D;RequestsPerMinute&amp;include&#x3D;IdentityMetrics&#x60;. Matched case-insensitively against the data set names, which are the &#x60;name&#x60; values on the response&#39;s data sets; duplicates are ignored. | [optional] 

### Return type

[**MetricsResponse**](../model/MetricsResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

