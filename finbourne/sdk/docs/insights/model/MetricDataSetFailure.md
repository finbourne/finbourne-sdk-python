# MetricDataSetFailure

Names a metric data set that was requested but could not be returned, with a caller-safe explanation.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **name** | **str** | Required | The data set that could not be returned. One of the Finbourne.Insights.WebApi.Dtos.Metrics.MetricDataSet values, and identical to the name of the Finbourne.Insights.WebApi.Dtos.Metrics.MetricsResponse property that would have carried it. |
| **reason** | **str** | Required | A generic, caller-safe explanation of why the data set is missing. Never contains provider names, query text, internal service names or exception detail. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.insights.models.MetricDataSetFailure import MetricDataSetFailure

instance = MetricDataSetFailure(
    name="...",  # required — The data set that could not be returned. One of the Finbourne.Insights.WebApi.Dtos.Metrics.MetricDataSet values, and identical to the name of the Finbourne.Insights.WebApi.Dtos.Metrics.MetricsResponse property that would have carried it.
    reason="..."  # required — A generic, caller-safe explanation of why the data set is missing. Never contains provider names, query text, internal service names or exception detail.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

