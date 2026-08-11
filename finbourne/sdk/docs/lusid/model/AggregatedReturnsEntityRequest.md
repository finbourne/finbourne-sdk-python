# AggregatedReturnsEntityRequest

The request body for the aggregated-returns (TWR) endpoint: the entity to calculate returns for, the  Returns entity that configures the calculation, the effective window, the metrics to calculate and the  period grid granularity. Supports a single `Portfolio` entity, the period `Return` metric and  a `Daily` grid.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **entity** | [AggregatedReturnsEntityId](AggregatedReturnsEntityId.md) | Required | *No description available.* |
| **returns_scope** | **str** | Required | *No description available.* |
| **returns_code** | **str** | Required | *No description available.* |
| **metrics** | [List[ReturnsMetric]](ReturnsMetric.md) | Required | *No description available.* |
| **period** | **str** | Optional | Available values: Daily, Monthly. |
| **from_effective_at** | **str** | Optional | *No description available.* |
| **to_effective_at** | **str** | Optional | *No description available.* |
| **as_at** | **datetime** | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.AggregatedReturnsEntityRequest import AggregatedReturnsEntityRequest

instance = AggregatedReturnsEntityRequest(
    entity=AggregatedReturnsEntityId(...),  # required
    returns_scope="...",  # required
    returns_code="...",  # required
    metrics=[],  # required
    period="...",  # optional — Available values: Daily, Monthly.
    from_effective_at="...",  # optional
    to_effective_at="...",  # optional
    as_at=datetime.now()  # optional
)
```


## Related Models

- [AggregatedReturnsEntityId](AggregatedReturnsEntityId.md)
- [ReturnsMetric](ReturnsMetric.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

