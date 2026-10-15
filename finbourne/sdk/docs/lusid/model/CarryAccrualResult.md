# CarryAccrualResult

The outcome of a carry accrual: the movement in each partner's carry against what was last accrued.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **fund_id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **period_end** | **datetime** | Required | The date carry is accrued to. |
| **source** | **str** | Required | The waterfall or model the carry amounts came from. |
| **lines** | [List[CarryAccrualLine]](CarryAccrualLine.md) | Required | The accrual movement per partner. |
| **booked_transaction_ids** | **List[str]** | Required | The identifiers of the transactions booked, if any. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.CarryAccrualResult import CarryAccrualResult

instance = CarryAccrualResult(
    fund_id=ResourceId(...),  # required
    period_end=datetime.now(),  # required — The date carry is accrued to.
    source="...",  # required — The waterfall or model the carry amounts came from.
    lines=[],  # required — The accrual movement per partner.
    booked_transaction_ids=  # required — The identifiers of the transactions booked, if any.
)
```


## Related Models

- [ResourceId](ResourceId.md)
- [CarryAccrualLine](CarryAccrualLine.md) — used in `lines`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

