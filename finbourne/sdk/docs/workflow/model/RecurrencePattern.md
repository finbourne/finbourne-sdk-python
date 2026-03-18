# RecurrencePattern

The Recurrence Pattern
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **time_constraints** | [TimeConstraints](TimeConstraints.md) | Required | *No description available.* |
| **date_regularity** | [DateRegularity](DateRegularity.md) | Required | *No description available.* |
| **business_day_adjustment** | **str** | Required | The Business Day Adjustment. One of None, Previous, Following, ModifiedPrevious, ModifiedFollowing, HalfMonthModifiedFollowing, Nearest |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.workflow.models.RecurrencePattern import RecurrencePattern

instance = RecurrencePattern(
    time_constraints=TimeConstraints(...),  # required
    date_regularity=DateRegularity(...),  # required
    business_day_adjustment="..."  # required — The Business Day Adjustment. One of None, Previous, Following, ModifiedPrevious, ModifiedFollowing, HalfMonthModifiedFollowing, Nearest
)
```


## Related Models

- [TimeConstraints](TimeConstraints.md)
- [DateRegularity](DateRegularity.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

