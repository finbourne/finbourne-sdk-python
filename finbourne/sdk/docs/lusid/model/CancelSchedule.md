# CancelSchedule

Cancel schedule represents the embedded option on a cancellable swap, allowing one party to  terminate the swap on one or more predefined dates.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **cancel_dates** | **List[datetime]** | Required | The dates on which cancellation may be elected. |
| **cancel_type** | **str** | Required | The type of cancellation option: European (single cancel date) or Bermudan (two or more).                Supported string (enumeration) values are: [European, Bermudan]. Available values: European, Bermudan. |
| **notice_convention** | [NoticeConvention](NoticeConvention.md) | Required | *No description available.* |
| **schedule_type** | **str** | Required | Available values: FixedSchedule, FloatSchedule, OptionalitySchedule, StepSchedule, Exercise, FxRateSchedule, FxLinkedNotionalSchedule, BondConversionSchedule, PikSchedule, Invalid, CancelSchedule. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.CancelSchedule import CancelSchedule

instance = CancelSchedule(
    cancel_dates=,  # required — The dates on which cancellation may be elected.
    cancel_type="...",  # required — The type of cancellation option: European (single cancel date) or Bermudan (two or more).                Supported string (enumeration) values are: [European, Bermudan]. Available values: European, Bermudan.
    notice_convention=NoticeConvention(...),  # required
    schedule_type="..."  # required — Available values: FixedSchedule, FloatSchedule, OptionalitySchedule, StepSchedule, Exercise, FxRateSchedule, FxLinkedNotionalSchedule, BondConversionSchedule, PikSchedule, Invalid, CancelSchedule.
)
```

- [NoticeConvention](NoticeConvention.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

