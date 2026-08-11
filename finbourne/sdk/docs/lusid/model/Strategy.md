# Strategy

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **keys** | [List[PerpetualProperty]](PerpetualProperty.md) | Required | *No description available.* |
| **value_type** | **str** | Required | Available values: Units, Weight. |
| **value** | **float** | Required | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.Strategy import Strategy

instance = Strategy(
    keys=[],  # required
    value_type="...",  # required — Available values: Units, Weight.
    value=0.0  # required
)
```


## Related Models

- [PerpetualProperty](PerpetualProperty.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

