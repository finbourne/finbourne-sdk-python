# FxLinkedNotionalSchedule

Schedule for notional changes based on the change in FX rate.  Used in the representation of a resettable cross currency interest rate swap.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **fx_conventions** | [FxConventions](FxConventions.md) | Required | *No description available.* |
| **varying_notional_currency** | **str** | Required | The currency of the varying notional amount. |
| **varying_notional_fixing_dates** | [RelativeDateOffset](RelativeDateOffset.md) | Required | *No description available.* |
| **varying_notional_interim_exchange_payment_dates** | [RelativeDateOffset](RelativeDateOffset.md) | Optional | *No description available.* |
| **schedule_type** | **str** | Required | The available values are: FixedSchedule, FloatSchedule, OptionalitySchedule, StepSchedule, Exercise, FxRateSchedule, FxLinkedNotionalSchedule, BondConversionSchedule, Invalid |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.FxLinkedNotionalSchedule import FxLinkedNotionalSchedule

instance = FxLinkedNotionalSchedule(
    fx_conventions=FxConventions(...),  # required
    varying_notional_currency="...",  # required — The currency of the varying notional amount.
    varying_notional_fixing_dates=RelativeDateOffset(...),  # required
    varying_notional_interim_exchange_payment_dates=RelativeDateOffset(...),  # optional
    schedule_type="..."  # required — The available values are: FixedSchedule, FloatSchedule, OptionalitySchedule, StepSchedule, Exercise, FxRateSchedule, FxLinkedNotionalSchedule, BondConversionSchedule, Invalid
)
```


## Related Models

- [FxConventions](FxConventions.md)
- [RelativeDateOffset](RelativeDateOffset.md)
- [RelativeDateOffset](RelativeDateOffset.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

