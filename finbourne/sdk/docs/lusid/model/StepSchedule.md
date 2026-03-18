# StepSchedule

Schedule that steps at known dated points in time.  Used in representation of a sinking bond, also called amortisation, steps in coupons for fixed bonds and spreads for floating bonds.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **level_type** | **str** | Required | The type of shift or adjustment that the quantity represents.    Supported string (enumeration) values are: [Absolute, AbsoluteShift, Percentage, AbsolutePercentage]. |
| **step_schedule_type** | **str** | Required | The type of step that this schedule is for.  Supported string (enumeration) values are: [Coupon, Notional, Spread]. |
| **steps** | [List[LevelStep]](LevelStep.md) | Required | The level steps which are applied. |
| **schedule_type** | **str** | Required | The available values are: FixedSchedule, FloatSchedule, OptionalitySchedule, StepSchedule, Exercise, FxRateSchedule, FxLinkedNotionalSchedule, BondConversionSchedule, Invalid |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.StepSchedule import StepSchedule

instance = StepSchedule(
    level_type="...",  # required — The type of shift or adjustment that the quantity represents.    Supported string (enumeration) values are: [Absolute, AbsoluteShift, Percentage, AbsolutePercentage].
    step_schedule_type="...",  # required — The type of step that this schedule is for.  Supported string (enumeration) values are: [Coupon, Notional, Spread].
    steps=[],  # required — The level steps which are applied.
    schedule_type="..."  # required — The available values are: FixedSchedule, FloatSchedule, OptionalitySchedule, StepSchedule, Exercise, FxRateSchedule, FxLinkedNotionalSchedule, BondConversionSchedule, Invalid
)
```

- [LevelStep](LevelStep.md) — used in `steps`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

