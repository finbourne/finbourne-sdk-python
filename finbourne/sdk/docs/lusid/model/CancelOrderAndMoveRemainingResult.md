# CancelOrderAndMoveRemainingResult

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **cancelled_order** | [Order](Order.md) | Optional | *No description available.* |
| **new_order** | [Order](Order.md) | Optional | *No description available.* |
| **new_block_id** | [ResourceId](ResourceId.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.CancelOrderAndMoveRemainingResult import CancelOrderAndMoveRemainingResult

instance = CancelOrderAndMoveRemainingResult(
    cancelled_order=Order(...),  # optional
    new_order=Order(...),  # optional
    new_block_id=ResourceId(...)  # optional
)
```


## Related Models

- [Order](Order.md)
- [Order](Order.md)
- [ResourceId](ResourceId.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

