# BlockAndOrders

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **block** | [Block](Block.md) | Required | *No description available.* |
| **orders** | [List[Order]](Order.md) | Required | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.BlockAndOrders import BlockAndOrders

instance = BlockAndOrders(
    block=Block(...),  # required
    orders=[]  # required
)
```


## Related Models

- [Block](Block.md)
- [Order](Order.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

