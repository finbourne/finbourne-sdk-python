# MetricsResponse

The aggregated platform metrics for a domain: one nullable, strongly-typed property per data set.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **as_at** | **datetime** | Required | When this response was assembled, in UTC. Every data set in the response was resolved against this instant. |
| **domain** | **str** | Required | The domain the metrics are for, resolved from the authenticated request rather than from any parameter. |
| **requests_per_minute** | [RequestsPerMinuteDataSet](RequestsPerMinuteDataSet.md) | Optional | *No description available.* |
| **service_endpoint_durations24h** | [ServiceEndpointDurations24hDataSet](ServiceEndpointDurations24hDataSet.md) | Optional | *No description available.* |
| **service_requests24h** | [ServiceRequests24hDataSet](ServiceRequests24hDataSet.md) | Optional | *No description available.* |
| **identity_metrics** | [IdentityMetricsDataSet](IdentityMetricsDataSet.md) | Optional | *No description available.* |
| **not_included** | **List[str]** | Required | The data sets the caller excluded via the &#x60;include&#x60; parameter, and which were therefore never queried. Each value is one of the Finbourne.Insights.WebApi.Dtos.Metrics.MetricDataSet values. |
| **failed** | [List[MetricDataSetFailure]](MetricDataSetFailure.md) | Required | The data sets that were requested but could not be returned, each with a caller-safe reason. |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.insights.models.MetricsResponse import MetricsResponse

instance = MetricsResponse(
    as_at=datetime.now(),  # required — When this response was assembled, in UTC. Every data set in the response was resolved against this instant.
    domain="...",  # required — The domain the metrics are for, resolved from the authenticated request rather than from any parameter.
    requests_per_minute=RequestsPerMinuteDataSet(...),  # optional
    service_endpoint_durations24h=ServiceEndpointDurations24hDataSet(...),  # optional
    service_requests24h=ServiceRequests24hDataSet(...),  # optional
    identity_metrics=IdentityMetricsDataSet(...),  # optional
    not_included=,  # required — The data sets the caller excluded via the &#x60;include&#x60; parameter, and which were therefore never queried. Each value is one of the Finbourne.Insights.WebApi.Dtos.Metrics.MetricDataSet values.
    failed=[],  # required — The data sets that were requested but could not be returned, each with a caller-safe reason.
    links=[]  # optional
)
```

- [RequestsPerMinuteDataSet](RequestsPerMinuteDataSet.md)
- [ServiceEndpointDurations24hDataSet](ServiceEndpointDurations24hDataSet.md)
- [ServiceRequests24hDataSet](ServiceRequests24hDataSet.md)
- [IdentityMetricsDataSet](IdentityMetricsDataSet.md)
- [MetricDataSetFailure](MetricDataSetFailure.md) — used in `failed`
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

