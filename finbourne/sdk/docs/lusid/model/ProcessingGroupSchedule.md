# ProcessingGroupSchedule

Specification of the dates on which a Processing Group is executed: a date range plus  tenor / roll / business-day conventions and holiday calendars that generate the schedule,  or an explicit override set of dates. Modelled on the valuation schedule shape, without the  bitemporal timeline fields.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **effective_from** | **str** | Optional | The start of the date range over which the schedule is generated. |
| **effective_at** | **str** | Optional | The end of the date range over which the schedule is generated. |
| **tenor** | **str** | Optional | Tenor, e.g. \&quot;1D\&quot;, \&quot;1M\&quot;, used to generate the date schedule between EffectiveFrom and EffectiveAt. |
| **roll_convention** | **str** | Optional | When Tenor is \&quot;1M\&quot; or longer, the rule used to generate the date schedule, e.g. \&quot;EndOfMonth\&quot; or \&quot;1\&quot;. |
| **holiday_calendars** | **List[str]** | Optional | The holiday calendar(s), by name, used when determining business days for the schedule. |
| **schedule_dates** | **List[str]** | Optional | If given, the exact set of dates on which to execute. Overrides the generated schedule. |
| **business_day_convention** | **str** | Optional | When Tenor is not \&quot;1D\&quot;, the convention (e.g. \&quot;MF\&quot;) used to roll dates that land on non-business days. |
| **time_zone** | **str** | Optional | The IANA approved time zone (tzdb id, e.g. \&quot;Europe/London\&quot;) the schedule is expressed in.  Informational for consumers of the schedule: the generated schedule dates are calendar dates  and are not adjusted by this time zone. Optional. |
| **business_day_offset** | **int** | Optional | If given, the number of good business days (per the holiday calendars) added to each generated  date. Can be negative. For example, the 10th business day of each month is a \&quot;1M\&quot; tenor with an  \&quot;EndOfMonth\&quot; roll convention and a business day offset of 10. Cannot be combined with ScheduleDates. |
| **date_exceptions** | **List[str]** | Optional | Dates, in yyyy-MM-dd format, on which the Processing Group does not run. These are removed  from the generated schedule after all other conventions and offsets have been applied. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.ProcessingGroupSchedule import ProcessingGroupSchedule

instance = ProcessingGroupSchedule(
    effective_from="...",  # optional — The start of the date range over which the schedule is generated.
    effective_at="...",  # optional — The end of the date range over which the schedule is generated.
    tenor="...",  # optional — Tenor, e.g. \&quot;1D\&quot;, \&quot;1M\&quot;, used to generate the date schedule between EffectiveFrom and EffectiveAt.
    roll_convention="...",  # optional — When Tenor is \&quot;1M\&quot; or longer, the rule used to generate the date schedule, e.g. \&quot;EndOfMonth\&quot; or \&quot;1\&quot;.
    holiday_calendars=,  # optional — The holiday calendar(s), by name, used when determining business days for the schedule.
    schedule_dates=,  # optional — If given, the exact set of dates on which to execute. Overrides the generated schedule.
    business_day_convention="...",  # optional — When Tenor is not \&quot;1D\&quot;, the convention (e.g. \&quot;MF\&quot;) used to roll dates that land on non-business days.
    time_zone="...",  # optional — The IANA approved time zone (tzdb id, e.g. \&quot;Europe/London\&quot;) the schedule is expressed in.  Informational for consumers of the schedule: the generated schedule dates are calendar dates  and are not adjusted by this time zone. Optional.
    business_day_offset=0,  # optional — If given, the number of good business days (per the holiday calendars) added to each generated  date. Can be negative. For example, the 10th business day of each month is a \&quot;1M\&quot; tenor with an  \&quot;EndOfMonth\&quot; roll convention and a business day offset of 10. Cannot be combined with ScheduleDates.
    date_exceptions=  # optional — Dates, in yyyy-MM-dd format, on which the Processing Group does not run. These are removed  from the generated schedule after all other conventions and offsets have been applied.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

