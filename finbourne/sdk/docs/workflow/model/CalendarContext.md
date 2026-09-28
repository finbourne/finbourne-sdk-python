# CalendarContext

A named time zone and set of holiday calendars.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **name** | **str** | Required | The name the schedule and the date and time adjustments use to name this context |
| **time_zone** | **str** | Required | The time zone to use. A TZ identifier, for example \&quot;Europe/London\&quot; |
| **holiday_calendars** | [List[CalendarReference]](CalendarReference.md) | Optional | The holiday calendars that decide which dates are business days in this context |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.workflow.models.CalendarContext import CalendarContext

instance = CalendarContext(
    name="...",  # required — The name the schedule and the date and time adjustments use to name this context
    time_zone="...",  # required — The time zone to use. A TZ identifier, for example \&quot;Europe/London\&quot;
    holiday_calendars=[]  # optional — The holiday calendars that decide which dates are business days in this context
)
```

- [CalendarReference](CalendarReference.md) — used in `holiday_calendars`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

