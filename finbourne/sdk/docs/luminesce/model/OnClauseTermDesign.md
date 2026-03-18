# OnClauseTermDesign

A single on clause term (a pair of columns to join or a column to filter on)
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **left_table_field** | **str** | Optional | Name of field in the left table to join to (complex expressions are not supported at this time) |
| **right_table_field** | **str** | Optional | Name of field in the left table to join to (complex expressions are not supported at this time) |
| **operator** | [QueryDesignerBinaryOperator](QueryDesignerBinaryOperator.md) | Required | *No description available.* |
| **filter_value** | **str** | Optional | The value to compare against (always as a string, but will be formatted to the correct type) |
| **filter_value_data_type** | [DataType](DataType.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.luminesce.models.OnClauseTermDesign import OnClauseTermDesign

instance = OnClauseTermDesign(
    left_table_field="...",  # optional — Name of field in the left table to join to (complex expressions are not supported at this time)
    right_table_field="...",  # optional — Name of field in the left table to join to (complex expressions are not supported at this time)
    operator=QueryDesignerBinaryOperator(...),  # required
    filter_value="...",  # optional — The value to compare against (always as a string, but will be formatted to the correct type)
    filter_value_data_type=DataType(...)  # optional
)
```

- [QueryDesignerBinaryOperator](QueryDesignerBinaryOperator.md)
- [DataType](DataType.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

