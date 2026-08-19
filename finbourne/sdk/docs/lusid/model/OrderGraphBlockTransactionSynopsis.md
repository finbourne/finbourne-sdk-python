# OrderGraphBlockTransactionSynopsis

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **quantity** | **float** | Required | Total number of units booked. |
| **amount** | **float** | Optional | Total consideration booked, in the block currency. |
| **details** | [List[OrderGraphBlockTransactionDetail]](OrderGraphBlockTransactionDetail.md) | Required | Identifiers for each transaction in this block. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.OrderGraphBlockTransactionSynopsis import OrderGraphBlockTransactionSynopsis

instance = OrderGraphBlockTransactionSynopsis(
    quantity=0.0,  # required — Total number of units booked.
    amount=0.0,  # optional — Total consideration booked, in the block currency.
    details=[]  # required — Identifiers for each transaction in this block.
)
```

- [OrderGraphBlockTransactionDetail](OrderGraphBlockTransactionDetail.md) — used in `details`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

