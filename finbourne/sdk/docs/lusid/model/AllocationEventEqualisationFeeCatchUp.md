# AllocationEventEqualisationFeeCatchUp

The management fees one admitted partner owes from the first fee date to the close, as an explicit amount.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **investor_record_id** | **str** | Required | The admitted partner the fee catch-up is charged to. |
| **amount** | **float** | Required | The fee catch-up in the event currency. Must not be negative. |
| **due_date** | **datetime** | Optional | The date the fee would have been due had the partner been admitted at the first close, from which interest on it accrues when charged. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.AllocationEventEqualisationFeeCatchUp import AllocationEventEqualisationFeeCatchUp

instance = AllocationEventEqualisationFeeCatchUp(
    investor_record_id="...",  # required — The admitted partner the fee catch-up is charged to.
    amount=0.0,  # required — The fee catch-up in the event currency. Must not be negative.
    due_date=datetime.now()  # optional — The date the fee would have been due had the partner been admitted at the first close, from which interest on it accrues when charged.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

