# AllocationEventRefund

Cash the fund owes back to an investor record.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **investor_record_id** | **str** | Optional | The investor record the refund is owed to. |
| **amount** | **float** | Optional | The amount owed back, in the event currency. |
| **reason** | **str** | Optional | Why the refund arose: Overpayment or Reversal. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.AllocationEventRefund import AllocationEventRefund

instance = AllocationEventRefund(
    investor_record_id="...",  # optional — The investor record the refund is owed to.
    amount=0.0,  # optional — The amount owed back, in the event currency.
    reason="..."  # optional — Why the refund arose: Overpayment or Reversal.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

