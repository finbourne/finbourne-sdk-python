# CarryAccrualLine

One partner's line on a carry accrual.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **investor_record_id** | **str** | Required | The investor record the amount belongs to. |
| **previous_carry_to_date** | **float** | Required | The cumulative carry already on the books for the partner. |
| **carry_to_date** | **float** | Required | The cumulative carry the partner has earned to the period end. |
| **delta** | **float** | Required | The accrual booked: the carry to date less what was already on the books. |
| **clawback_exposure** | **float** | Required | The carry that would have to be returned if the fund liquidated at the period end. |
| **status** | **str** | Required | What happened to the line. Available values: Unchanged, Accrued, Released. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.CarryAccrualLine import CarryAccrualLine

instance = CarryAccrualLine(
    investor_record_id="...",  # required — The investor record the amount belongs to.
    previous_carry_to_date=0.0,  # required — The cumulative carry already on the books for the partner.
    carry_to_date=0.0,  # required — The cumulative carry the partner has earned to the period end.
    delta=0.0,  # required — The accrual booked: the carry to date less what was already on the books.
    clawback_exposure=0.0,  # required — The carry that would have to be returned if the fund liquidated at the period end.
    status="..."  # required — What happened to the line. Available values: Unchanged, Accrued, Released.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

