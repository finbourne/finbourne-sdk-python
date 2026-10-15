# CarryAccrualRequest

The request to accrue carried interest on a partnership fund from amounts a waterfall has produced.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **period_end** | **datetime** | Required | The date carry is accrued to. |
| **source** | **str** | Required | The waterfall or model the carry amounts came from. |
| **amounts** | [List[CarryAccrualAmount]](CarryAccrualAmount.md) | Required | The carry each partner has earned to the period end, as the source states it. |
| **book** | **bool** | Optional | When true, the accrual deltas are booked. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.CarryAccrualRequest import CarryAccrualRequest

instance = CarryAccrualRequest(
    period_end=datetime.now(),  # required — The date carry is accrued to.
    source="...",  # required — The waterfall or model the carry amounts came from.
    amounts=[],  # required — The carry each partner has earned to the period end, as the source states it.
    book=True  # optional — When true, the accrual deltas are booked.
)
```

- [CarryAccrualAmount](CarryAccrualAmount.md) — used in `amounts`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

