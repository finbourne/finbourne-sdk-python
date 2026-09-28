# QueryableKeysForMetricsRequest

Specification of the metrics whose queryable key definitions are being requested.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **metrics** | **List[str]** | Required | The address keys of the metrics to describe, given exactly as they would be supplied as the key of  a valuation request&#39;s metrics, for example &#39;Valuation/PV&#39; or &#39;Holding/Properties[Holding/MyScope/Rating]&#39;. |
| **recipe_id** | [ResourceId](ResourceId.md) | Optional | *No description available.* |
| **effective_at** | **datetime** | Optional | The effective time to describe the metrics at, for definitions and entitlements that vary  along the effective timeline. Optional; defaults to the current time. |
| **as_at** | **datetime** | Optional | The as-at time to describe the metrics at. Optional; defaults to the latest. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.QueryableKeysForMetricsRequest import QueryableKeysForMetricsRequest

instance = QueryableKeysForMetricsRequest(
    metrics=,  # required — The address keys of the metrics to describe, given exactly as they would be supplied as the key of  a valuation request&#39;s metrics, for example &#39;Valuation/PV&#39; or &#39;Holding/Properties[Holding/MyScope/Rating]&#39;.
    recipe_id=ResourceId(...),  # optional
    effective_at=datetime.now(),  # optional — The effective time to describe the metrics at, for definitions and entitlements that vary  along the effective timeline. Optional; defaults to the current time.
    as_at=datetime.now()  # optional — The as-at time to describe the metrics at. Optional; defaults to the latest.
)
```

- [ResourceId](ResourceId.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

