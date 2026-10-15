# CarryAccrualAmount

A partner's carry to date as produced by the waterfall.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **investor_record_id** | **str** | Required | The investor record the amount belongs to. |
| **carry_to_date** | **float** | Required | The cumulative carry the partner has earned to the period end. |
| **by_tier** | [List[CarryTierAmount]](CarryTierAmount.md) | Optional | The carry by waterfall tier. |
| **clawback_exposure** | **float** | Optional | The carry that would have to be returned if the fund liquidated at the period end. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.CarryAccrualAmount import CarryAccrualAmount

instance = CarryAccrualAmount(
    investor_record_id="...",  # required — The investor record the amount belongs to.
    carry_to_date=0.0,  # required — The cumulative carry the partner has earned to the period end.
    by_tier=[],  # optional — The carry by waterfall tier.
    clawback_exposure=0.0  # optional — The carry that would have to be returned if the fund liquidated at the period end.
)
```

- [CarryTierAmount](CarryTierAmount.md) — used in `by_tier`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

