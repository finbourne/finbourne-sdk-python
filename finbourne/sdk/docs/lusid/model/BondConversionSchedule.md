# BondConversionSchedule

A BondConversionSchedule object represents a class containing the  information required for the creation of convertible features in a ComplexBond
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **identifiers** | **Dict[str, Optional[str]]** | Optional | The market identifier(s) of the share that the bond converts to. The instrument  will not fail validation if no identifier is supplied. |
| **bond_conversion_entries** | [List[BondConversionEntry]](BondConversionEntry.md) | Optional | The dates at which the bond may be converted and associated information required about the conversion. |
| **conversion_trigger** | **str** | Required | Corporate event that triggers a conversion    Supported string (enumeration) values are: [NextEquityFinancing, IpoConversion, KnownDates, SoftCall]. |
| **delivery_type** | **str** | Optional | Is a conversion made into cash or into shares?  Defaults to \&quot;Physical\&quot; if not set.    Supported string (enumeration) values are: [Cash, Physical]. |
| **exercise_type** | **str** | Required | The exercise type of the conversion schedule (American or European).  For American type, the bond is convertible from a given exercise date until the next date in the schedule, or until it matures.  For European type, the bond is only convertible on the given exercise date.    Supported string (enumeration) values are: [European, Bermudan, American]. |
| **includes_accrued** | **bool** | Optional | Set this to true if a accrued interest is included in the conversion. Defaults to true. |
| **mandatory_conversion** | **bool** | Optional | Set this to true if a conversion is mandatory if the trigger occurs. Defaults to false. |
| **notification_period_end** | **datetime** | Optional | The last day in the notification period for the conversion of the bond |
| **notification_period_start** | **datetime** | Optional | The first day in the notification period for the conversion of the bond |
| **schedule_type** | **str** | Required | The available values are: FixedSchedule, FloatSchedule, OptionalitySchedule, StepSchedule, Exercise, FxRateSchedule, FxLinkedNotionalSchedule, BondConversionSchedule, Invalid |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.BondConversionSchedule import BondConversionSchedule

instance = BondConversionSchedule(
    identifiers=,  # optional — The market identifier(s) of the share that the bond converts to. The instrument  will not fail validation if no identifier is supplied.
    bond_conversion_entries=[],  # optional — The dates at which the bond may be converted and associated information required about the conversion.
    conversion_trigger="...",  # required — Corporate event that triggers a conversion    Supported string (enumeration) values are: [NextEquityFinancing, IpoConversion, KnownDates, SoftCall].
    delivery_type="...",  # optional — Is a conversion made into cash or into shares?  Defaults to \&quot;Physical\&quot; if not set.    Supported string (enumeration) values are: [Cash, Physical].
    exercise_type="...",  # required — The exercise type of the conversion schedule (American or European).  For American type, the bond is convertible from a given exercise date until the next date in the schedule, or until it matures.  For European type, the bond is only convertible on the given exercise date.    Supported string (enumeration) values are: [European, Bermudan, American].
    includes_accrued=True,  # optional — Set this to true if a accrued interest is included in the conversion. Defaults to true.
    mandatory_conversion=True,  # optional — Set this to true if a conversion is mandatory if the trigger occurs. Defaults to false.
    notification_period_end=datetime.now(),  # optional — The last day in the notification period for the conversion of the bond
    notification_period_start=datetime.now(),  # optional — The first day in the notification period for the conversion of the bond
    schedule_type="..."  # required — The available values are: FixedSchedule, FloatSchedule, OptionalitySchedule, StepSchedule, Exercise, FxRateSchedule, FxLinkedNotionalSchedule, BondConversionSchedule, Invalid
)
```

- [BondConversionEntry](BondConversionEntry.md) — used in `bond_conversion_entries`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

