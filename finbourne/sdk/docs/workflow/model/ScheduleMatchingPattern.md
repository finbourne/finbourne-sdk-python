# ScheduleMatchingPattern

The Schedule Matching Pattern to trigger on
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **context** | [ScheduleMatchingPatternContext](ScheduleMatchingPatternContext.md) | Required | *No description available.* |
| **recurrence_pattern** | [RecurrencePattern](RecurrencePattern.md) | Required | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.workflow.models.ScheduleMatchingPattern import ScheduleMatchingPattern

instance = ScheduleMatchingPattern(
    context=ScheduleMatchingPatternContext(...),  # required
    recurrence_pattern=RecurrencePattern(...)  # required
)
```


## Related Models

- [ScheduleMatchingPatternContext](ScheduleMatchingPatternContext.md)
- [RecurrencePattern](RecurrencePattern.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

