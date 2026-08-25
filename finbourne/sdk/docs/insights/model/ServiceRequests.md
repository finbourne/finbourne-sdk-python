# ServiceRequests

The request volume and server-error rate for a single service over the window.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **service** | **str** | Optional | The name of the service (application) that handled the requests. |
| **total_requests** | **int** | Optional | The number of requests over the window, or null if not reported. |
| **requests5xx** | **int** | Optional | The number of requests over the window that returned a 5xx status code, or null if not reported. |
| **pct5xx** | **float** | Optional | The percentage of requests that returned a 5xx status code, or null if not reported. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.insights.models.ServiceRequests import ServiceRequests

instance = ServiceRequests(
    service="...",  # optional — The name of the service (application) that handled the requests.
    total_requests=0,  # optional — The number of requests over the window, or null if not reported.
    requests5xx=0,  # optional — The number of requests over the window that returned a 5xx status code, or null if not reported.
    pct5xx=0.0  # optional — The percentage of requests that returned a 5xx status code, or null if not reported.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

