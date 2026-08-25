# RequestsPerMinuteDataSet

Request volume, error count and total duration per minute, broken down by service and endpoint, over a rolling three hour window.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **name** | **str** | Required | The name of this data set. Always &#x60;RequestsPerMinute&#x60;, matching the corresponding Finbourne.Insights.WebApi.Dtos.Metrics.MetricDataSet value and Finbourne.Insights.WebApi.Dtos.Metrics.MetricsResponse property. |
| **window_start** | **datetime** | Required | Inclusive start of the window the data covers, in UTC, floored to a whole minute. |
| **window_end** | **datetime** | Required | End of the window the data covers, in UTC, floored to a whole minute. |
| **truncated** | **bool** | Required | True when the query reached the row cap, so the data covers only part of the window and totals are understated. False when the whole window was returned. |
| **values** | [List[RequestsPerMinuteBucket]](RequestsPerMinuteBucket.md) | Required | The per-minute rows, ordered by minute, then service, then endpoint. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.insights.models.RequestsPerMinuteDataSet import RequestsPerMinuteDataSet

instance = RequestsPerMinuteDataSet(
    name="...",  # required — The name of this data set. Always &#x60;RequestsPerMinute&#x60;, matching the corresponding Finbourne.Insights.WebApi.Dtos.Metrics.MetricDataSet value and Finbourne.Insights.WebApi.Dtos.Metrics.MetricsResponse property.
    window_start=datetime.now(),  # required — Inclusive start of the window the data covers, in UTC, floored to a whole minute.
    window_end=datetime.now(),  # required — End of the window the data covers, in UTC, floored to a whole minute.
    truncated=True,  # required — True when the query reached the row cap, so the data covers only part of the window and totals are understated. False when the whole window was returned.
    values=[]  # required — The per-minute rows, ordered by minute, then service, then endpoint.
)
```

- [RequestsPerMinuteBucket](RequestsPerMinuteBucket.md) — used in `values`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

