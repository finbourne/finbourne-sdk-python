# AggregatedReturnsEntityId

Identifies an entity whose aggregated (time-weighted) returns are calculated: its scope, code and  type. Mirrors the valuation endpoint's entity identifier. Currently, supports only the  `Portfolio` entity type.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **scope** | **str** | Required | *No description available.* |
| **code** | **str** | Required | *No description available.* |
| **entity_type** | **str** | Required | Available values: Portfolio. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.AggregatedReturnsEntityId import AggregatedReturnsEntityId

instance = AggregatedReturnsEntityId(
    scope="...",  # required
    code="...",  # required
    entity_type="..."  # required — Available values: Portfolio.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

