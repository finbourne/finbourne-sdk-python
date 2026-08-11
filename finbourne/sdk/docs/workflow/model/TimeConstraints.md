# TimeConstraints

Time constraints for a Recurrence Pattern
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **start_date** | **str** | Required | Start date of the Recurrence Pattern e.g. 2025-12-25 |
| **end_date** | **str** | Optional | Optional end date of the Recurrence Pattern e.g. 2025-12-31 |
| **times_of_day** | [List[TimeOfDay]](TimeOfDay.md) | Required | Times of the day to run the Recurrence Pattern |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.workflow.models.TimeConstraints import TimeConstraints

instance = TimeConstraints(
    start_date="...",  # required — Start date of the Recurrence Pattern e.g. 2025-12-25
    end_date="...",  # optional — Optional end date of the Recurrence Pattern e.g. 2025-12-31
    times_of_day=[]  # required — Times of the day to run the Recurrence Pattern
)
```

- [TimeOfDay](TimeOfDay.md) — used in `times_of_day`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

