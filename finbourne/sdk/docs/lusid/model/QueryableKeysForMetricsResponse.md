# QueryableKeysForMetricsResponse

The queryable key definition of each requested metric. Every requested metric appears in exactly one of  the two maps.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **metrics** | [Dict[str, QueryableKey]](QueryableKey.md) | Required | The definition of each metric that resolved, describing what a valuation returns for it and how to  present it. Keyed by the metric as it was requested, for example &#39;Valuation/PV&#39; or  &#39;ProfitAndLoss/Realised/Market(Window&#x3D;YTD)&#39;. Identical requested keys appear once; different  spellings of the same underlying key, such as a property&#39;s raw and wrapper forms, each appear. |
| **failed** | **Dict[str, Optional[str]]** | Required | Why each metric that did not resolve cannot be requested, keyed as for Metrics. Empty when every  metric resolved. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.QueryableKeysForMetricsResponse import QueryableKeysForMetricsResponse

instance = QueryableKeysForMetricsResponse(
    metrics=QueryableKey(...),  # required — The definition of each metric that resolved, describing what a valuation returns for it and how to  present it. Keyed by the metric as it was requested, for example &#39;Valuation/PV&#39; or  &#39;ProfitAndLoss/Realised/Market(Window&#x3D;YTD)&#39;. Identical requested keys appear once; different  spellings of the same underlying key, such as a property&#39;s raw and wrapper forms, each appear.
    failed=  # required — Why each metric that did not resolve cannot be requested, keyed as for Metrics. Empty when every  metric resolved.
)
```


## Related Models

- [QueryableKey](QueryableKey.md) — used in `metrics`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

