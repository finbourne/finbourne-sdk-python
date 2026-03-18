# MovedOrderToDifferentBlockResponse

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **destination_block** | [Block](Block.md) | Optional | *No description available.* |
| **order** | [Order](Order.md) | Optional | *No description available.* |
| **source_block_id** | [ResourceId](ResourceId.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.MovedOrderToDifferentBlockResponse import MovedOrderToDifferentBlockResponse

instance = MovedOrderToDifferentBlockResponse(
    destination_block=Block(...),  # optional
    order=Order(...),  # optional
    source_block_id=ResourceId(...)  # optional
)
```


## Related Models

- [Block](Block.md)
- [Order](Order.md)
- [ResourceId](ResourceId.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

