# ServiceEndpointDuration

The request duration distribution for a single service and endpoint over the window.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **service** | **str** | Optional | The name of the service (application) that handled the requests. |
| **endpoint** | **str** | Optional | The endpoint (API operation) the requests were made to. |
| **total_requests** | **int** | Optional | The number of requests over the window, or null if not reported. |
| **mean_duration_ms** | **float** | Optional | The mean request duration in milliseconds, or null if not reported. |
| **median_duration_ms** | **float** | Optional | The median (50th percentile) request duration in milliseconds, or null if not reported. |
| **p95_duration_ms** | **float** | Optional | The 95th percentile request duration in milliseconds, or null if not reported. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.insights.models.ServiceEndpointDuration import ServiceEndpointDuration

instance = ServiceEndpointDuration(
    service="...",  # optional — The name of the service (application) that handled the requests.
    endpoint="...",  # optional — The endpoint (API operation) the requests were made to.
    total_requests=0,  # optional — The number of requests over the window, or null if not reported.
    mean_duration_ms=0.0,  # optional — The mean request duration in milliseconds, or null if not reported.
    median_duration_ms=0.0,  # optional — The median (50th percentile) request duration in milliseconds, or null if not reported.
    p95_duration_ms=0.0  # optional — The 95th percentile request duration in milliseconds, or null if not reported.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

