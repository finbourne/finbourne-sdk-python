# DateRegularity

A Date Regularity

## oneOf Type

`DateRegularity` can be one of the following types:

* [DayRegularity](./DayRegularity.md)
* [RelativeMonthRegularity](./RelativeMonthRegularity.md)
* [SpecificMonthRegularity](./SpecificMonthRegularity.md)
* [WeekRegularity](./WeekRegularity.md)
* [YearRegularity](./YearRegularity.md)

## Usage

### Creating from a compatible type

```python
from finbourne.sdk.services.workflow.models.DateRegularity import DateRegularity

# Construct using any of the compatible types above
day_regularity_instance = workflow.models.day_regularity.DayRegularity(
                        frequency = 56, 
                        type = 'Day', )

instance = DateRegularity(day_regularity_instance)
```

## Related Models

- [DayRegularity](./DayRegularity.md)
- [RelativeMonthRegularity](./RelativeMonthRegularity.md)
- [SpecificMonthRegularity](./SpecificMonthRegularity.md)
- [WeekRegularity](./WeekRegularity.md)
- [YearRegularity](./YearRegularity.md)

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

