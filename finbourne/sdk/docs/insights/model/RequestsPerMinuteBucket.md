# RequestsPerMinuteBucket

One minute of request activity for a single service and endpoint.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **minute_bucket** | **datetime** | Required | Start of the whole minute this row covers, in UTC. |
| **service** | **str** | Optional | The name of the service (application) that handled the requests. |
| **endpoint** | **str** | Optional | The endpoint (API operation) the requests were made to. |
| **total_requests** | **int** | Optional | The number of requests in this minute, or null if not reported. |
| **requests5xx** | **int** | Optional | The number of requests in this minute that returned a 5xx status code, or null if not reported. |
| **duration_sum_ms** | **float** | Optional | The sum of the request durations in this minute, in milliseconds, or null if not reported. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.insights.models.RequestsPerMinuteBucket import RequestsPerMinuteBucket

instance = RequestsPerMinuteBucket(
    minute_bucket=datetime.now(),  # required — Start of the whole minute this row covers, in UTC.
    service="...",  # optional — The name of the service (application) that handled the requests.
    endpoint="...",  # optional — The endpoint (API operation) the requests were made to.
    total_requests=0,  # optional — The number of requests in this minute, or null if not reported.
    requests5xx=0,  # optional — The number of requests in this minute that returned a 5xx status code, or null if not reported.
    duration_sum_ms=0.0  # optional — The sum of the request durations in this minute, in milliseconds, or null if not reported.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

