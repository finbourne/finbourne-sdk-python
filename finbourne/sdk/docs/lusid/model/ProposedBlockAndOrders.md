# ProposedBlockAndOrders

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **request** | [BlockAndOrdersRequest](BlockAndOrdersRequest.md) | Optional | *No description available.* |
| **net_quantity** | **float** | Optional | The block&#39;s quantity, netted by direction, where any order is quantity-based. |
| **net_amount** | [CurrencyAndAmount](CurrencyAndAmount.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.ProposedBlockAndOrders import ProposedBlockAndOrders

instance = ProposedBlockAndOrders(
    request=BlockAndOrdersRequest(...),  # optional
    net_quantity=0.0,  # optional — The block&#39;s quantity, netted by direction, where any order is quantity-based.
    net_amount=CurrencyAndAmount(...)  # optional
)
```


## Related Models

- [BlockAndOrdersRequest](BlockAndOrdersRequest.md)
- [CurrencyAndAmount](CurrencyAndAmount.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

