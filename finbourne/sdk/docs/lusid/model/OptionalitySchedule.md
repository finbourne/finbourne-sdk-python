# OptionalitySchedule

Optionality Schedule represents a class for creation of schedules for optionality (call, put)
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **exercise_type** | **str** | Optional | The exercise type of the optionality schedule (American or European).  For American type, the bond is perpetually callable from a given exercise date until it matures, or the next date in the schedule.  For European type, the bond is only callable on a given exercise date.    Supported string (enumeration) values are: [European, American].  Defaults to \&quot;European\&quot; if not set. |
| **option_entries** | [List[OptionEntry]](OptionEntry.md) | Optional | The dates at which the bond call/put may be actioned, and associated strikes. |
| **option_type** | **str** | Optional | Type of optionality for the schedule.    Supported string (enumeration) values are: [Call, Put].  Defaults to \&quot;Call\&quot; if not set. |
| **schedule_type** | **str** | Required | The available values are: FixedSchedule, FloatSchedule, OptionalitySchedule, StepSchedule, Exercise, FxRateSchedule, FxLinkedNotionalSchedule, BondConversionSchedule, Invalid |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.OptionalitySchedule import OptionalitySchedule

instance = OptionalitySchedule(
    exercise_type="...",  # optional — The exercise type of the optionality schedule (American or European).  For American type, the bond is perpetually callable from a given exercise date until it matures, or the next date in the schedule.  For European type, the bond is only callable on a given exercise date.    Supported string (enumeration) values are: [European, American].  Defaults to \&quot;European\&quot; if not set.
    option_entries=[],  # optional — The dates at which the bond call/put may be actioned, and associated strikes.
    option_type="...",  # optional — Type of optionality for the schedule.    Supported string (enumeration) values are: [Call, Put].  Defaults to \&quot;Call\&quot; if not set.
    schedule_type="..."  # required — The available values are: FixedSchedule, FloatSchedule, OptionalitySchedule, StepSchedule, Exercise, FxRateSchedule, FxLinkedNotionalSchedule, BondConversionSchedule, Invalid
)
```

- [OptionEntry](OptionEntry.md) — used in `option_entries`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

