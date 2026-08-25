# ServiceRequests24hDataSet

Request volume and server-error rate per service over a rolling twenty four hour window.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **name** | **str** | Required | The name of this data set. Always &#x60;ServiceRequests24h&#x60;, matching the corresponding Finbourne.Insights.WebApi.Dtos.Metrics.MetricDataSet value and Finbourne.Insights.WebApi.Dtos.Metrics.MetricsResponse property. |
| **window_start** | **datetime** | Required | Inclusive start of the window the data covers, in UTC, floored to a whole minute. |
| **window_end** | **datetime** | Required | End of the window the data covers, in UTC, floored to a whole minute. |
| **truncated** | **bool** | Required | True when the query reached the row cap, so some services are missing. False when the whole result set was returned. |
| **values** | [List[ServiceRequests]](ServiceRequests.md) | Required | The rows, ordered by service. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.insights.models.ServiceRequests24hDataSet import ServiceRequests24hDataSet

instance = ServiceRequests24hDataSet(
    name="...",  # required — The name of this data set. Always &#x60;ServiceRequests24h&#x60;, matching the corresponding Finbourne.Insights.WebApi.Dtos.Metrics.MetricDataSet value and Finbourne.Insights.WebApi.Dtos.Metrics.MetricsResponse property.
    window_start=datetime.now(),  # required — Inclusive start of the window the data covers, in UTC, floored to a whole minute.
    window_end=datetime.now(),  # required — End of the window the data covers, in UTC, floored to a whole minute.
    truncated=True,  # required — True when the query reached the row cap, so some services are missing. False when the whole result set was returned.
    values=[]  # required — The rows, ordered by service.
)
```

- [ServiceRequests](ServiceRequests.md) — used in `values`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

