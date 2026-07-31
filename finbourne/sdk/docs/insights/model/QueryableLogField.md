# QueryableLogField

Describes a field of a log type that can be selected and (where Finbourne.Insights.WebApi.Dtos.Querying.QueryableLogField.Filterable is set) filtered when querying logs, including the comparator operations available for it. Returned by the queryable-fields metadata endpoint so a UI can advertise the correct comparators for each field.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **name** | **str** | Required | The name of the field, as used when requesting it or filtering on it (case-insensitive). |
| **data_type** | **str** | Required | The data type of the field: Text, Numeric, Date or Boolean. |
| **supported_operations** | **List[str]** | Required | The comparator operations available for this field. Empty when the field is not filterable. |
| **filterable** | **bool** | Optional | Whether the field can be used in a filter. |
| **always_returned** | **bool** | Optional | Whether the field is always returned (and therefore need not be requested). |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.insights.models.QueryableLogField import QueryableLogField

instance = QueryableLogField(
    name="...",  # required — The name of the field, as used when requesting it or filtering on it (case-insensitive).
    data_type="...",  # required — The data type of the field: Text, Numeric, Date or Boolean.
    supported_operations=,  # required — The comparator operations available for this field. Empty when the field is not filterable.
    filterable=True,  # optional — Whether the field can be used in a filter.
    always_returned=True  # optional — Whether the field is always returned (and therefore need not be requested).
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

