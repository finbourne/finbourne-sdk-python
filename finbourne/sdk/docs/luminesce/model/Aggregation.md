# Aggregation

How to aggregate over a field
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **type** | [AggregateFunction](AggregateFunction.md) | Required | *No description available.* |
| **alias** | **str** | Optional | Alias, if any, for the Aggregate expression when selected |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.luminesce.models.Aggregation import Aggregation

instance = Aggregation(
    type=AggregateFunction(...),  # required
    alias="..."  # optional — Alias, if any, for the Aggregate expression when selected
)
```


## Related Models

- [AggregateFunction](AggregateFunction.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

