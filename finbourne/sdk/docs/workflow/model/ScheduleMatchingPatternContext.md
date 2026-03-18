# ScheduleMatchingPatternContext

Context for a Schedule Matching Pattern
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **time_zone** | **str** | Required | The time zone to use. A TZ Identifier e.g. \&quot;Europe/London\&quot; |
| **holiday_calendars** | [List[CalendarReference]](CalendarReference.md) | Optional | References to any Holiday Calendars to use |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.workflow.models.ScheduleMatchingPatternContext import ScheduleMatchingPatternContext

instance = ScheduleMatchingPatternContext(
    time_zone="...",  # required — The time zone to use. A TZ Identifier e.g. \&quot;Europe/London\&quot;
    holiday_calendars=[]  # optional — References to any Holiday Calendars to use
)
```

- [CalendarReference](CalendarReference.md) — used in `holiday_calendars`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

