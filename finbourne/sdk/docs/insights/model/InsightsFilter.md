# InsightsFilter

A single filter applied to a queryable log field. Exactly one comparator (Finbourne.Insights.WebApi.Dtos.Querying.InsightsFilter.Text, Finbourne.Insights.WebApi.Dtos.Querying.InsightsFilter.Numeric, Finbourne.Insights.WebApi.Dtos.Querying.InsightsFilter.Date or Finbourne.Insights.WebApi.Dtos.Querying.InsightsFilter.Boolean) must be populated, and its type must match the data type of the field named by Finbourne.Insights.WebApi.Dtos.Querying.InsightsFilter.Field. The available comparator and operation for a field can be discovered via the queryable-fields metadata endpoint.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **var_field** | **str** | Required | The name of the field to filter on (case-insensitive). Must be a filterable field of the queried log type. |
| **text** | [TextComparator](TextComparator.md) | Optional | *No description available.* |
| **numeric** | [NumericComparator](NumericComparator.md) | Optional | *No description available.* |
| **var_date** | [DateComparator](DateComparator.md) | Optional | *No description available.* |
| **boolean** | [BooleanComparator](BooleanComparator.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.insights.models.InsightsFilter import InsightsFilter

instance = InsightsFilter(
    var_field="...",  # required — The name of the field to filter on (case-insensitive). Must be a filterable field of the queried log type.
    text=TextComparator(...),  # optional
    numeric=NumericComparator(...),  # optional
    var_date=DateComparator(...),  # optional
    boolean=BooleanComparator(...)  # optional
)
```

- [TextComparator](TextComparator.md)
- [NumericComparator](NumericComparator.md)
- [DateComparator](DateComparator.md)
- [BooleanComparator](BooleanComparator.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

