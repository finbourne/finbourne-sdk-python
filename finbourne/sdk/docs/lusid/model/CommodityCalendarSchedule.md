# CommodityCalendarSchedule

Schedule describing the periodic calendar-average settlement periods of a commodity calendar swap.  Each period settles in cash against the average of the observed commodity price over the period.  The schedule is currently stored and validated only; period expansion is not yet implemented.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **start_date** | **datetime** | Optional | The date from which the first settlement period accrues. |
| **maturity_date** | **datetime** | Optional | The date on which the final settlement period ends. |
| **flow_conventions** | [FlowConventions](FlowConventions.md) | Optional | *No description available.* |
| **payment_currency** | **str** | Optional | The currency in which each periodic cash settlement is paid. |
| **stub_type** | **str** | Optional | How any non-integral first or last period is handled when generating the settlement periods.  If not specified, this defaults to None.                Supported string (enumeration) values are: [ShortFront, ShortBack, LongBack, LongFront, Both]. Available values: None, ShortFront, ShortBack, LongBack, LongFront, Both, Invalid. |
| **schedule_type** | **str** | Required | Available values: FixedSchedule, FloatSchedule, OptionalitySchedule, StepSchedule, Exercise, FxRateSchedule, FxLinkedNotionalSchedule, BondConversionSchedule, PikSchedule, CommodityCalendarSchedule, Invalid, CancelSchedule. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.CommodityCalendarSchedule import CommodityCalendarSchedule

instance = CommodityCalendarSchedule(
    start_date=datetime.now(),  # optional — The date from which the first settlement period accrues.
    maturity_date=datetime.now(),  # optional — The date on which the final settlement period ends.
    flow_conventions=FlowConventions(...),  # optional
    payment_currency="...",  # optional — The currency in which each periodic cash settlement is paid.
    stub_type="...",  # optional — How any non-integral first or last period is handled when generating the settlement periods.  If not specified, this defaults to None.                Supported string (enumeration) values are: [ShortFront, ShortBack, LongBack, LongFront, Both]. Available values: None, ShortFront, ShortBack, LongBack, LongFront, Both, Invalid.
    schedule_type="..."  # required — Available values: FixedSchedule, FloatSchedule, OptionalitySchedule, StepSchedule, Exercise, FxRateSchedule, FxLinkedNotionalSchedule, BondConversionSchedule, PikSchedule, CommodityCalendarSchedule, Invalid, CancelSchedule.
)
```

- [FlowConventions](FlowConventions.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

