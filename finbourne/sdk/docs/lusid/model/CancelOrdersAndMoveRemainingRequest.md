# CancelOrdersAndMoveRemainingRequest

A request to create or update a Order.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **cancel_order_id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **move_remaining_to_order_id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **move_remaining_to_block_id** | [ResourceId](ResourceId.md) | Required | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.CancelOrdersAndMoveRemainingRequest import CancelOrdersAndMoveRemainingRequest

instance = CancelOrdersAndMoveRemainingRequest(
    cancel_order_id=ResourceId(...),  # required
    move_remaining_to_order_id=ResourceId(...),  # required
    move_remaining_to_block_id=ResourceId(...)  # required
)
```


## Related Models

- [ResourceId](ResourceId.md)
- [ResourceId](ResourceId.md)
- [ResourceId](ResourceId.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

