# OrderGraphBlockAllocationDetail

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **allocated_order_id** | [ResourceId](ResourceId.md) | Optional | *No description available.* |
| **quantity** | **float** | Required | The quantity of this allocation, with direction relative to the containing block. |
| **amount** | **float** | Optional | The amount of this allocation, derived from the quantity and price of the allocation. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.OrderGraphBlockAllocationDetail import OrderGraphBlockAllocationDetail

instance = OrderGraphBlockAllocationDetail(
    id=ResourceId(...),  # required
    allocated_order_id=ResourceId(...),  # optional
    quantity=0.0,  # required — The quantity of this allocation, with direction relative to the containing block.
    amount=0.0  # optional — The amount of this allocation, derived from the quantity and price of the allocation.
)
```


## Related Models

- [ResourceId](ResourceId.md)
- [ResourceId](ResourceId.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

