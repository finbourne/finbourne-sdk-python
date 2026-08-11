# FieldDesign

Treatment of a single field within a QueryDesign
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **name** | **str** | Required | Name of the Field (column name, constant, complex expression, etc.) |
| **table_alias** | **str** | Optional | Alias of the Table the field belongs to |
| **alias** | **str** | Optional | Alias if any (if none the Name is used) |
| **data_type** | [DataType](DataType.md) | Optional | *No description available.* |
| **should_select** | **bool** | Optional | Should this be selected? False would imply it is only being filtered on. Ignored when Aggregations are present |
| **filters** | [List[FilterTermDesign]](FilterTermDesign.md) | Optional | Filter clauses to apply to this field (And&#39;ed together) |
| **aggregations** | [List[Aggregation]](Aggregation.md) | Optional | Aggregations to apply (as opposed to simply selecting) |
| **is_expression** | **bool** | Optional | Is this field an expression |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.luminesce.models.FieldDesign import FieldDesign

instance = FieldDesign(
    name="...",  # required — Name of the Field (column name, constant, complex expression, etc.)
    table_alias="...",  # optional — Alias of the Table the field belongs to
    alias="...",  # optional — Alias if any (if none the Name is used)
    data_type=DataType(...),  # optional
    should_select=True,  # optional — Should this be selected? False would imply it is only being filtered on. Ignored when Aggregations are present
    filters=[],  # optional — Filter clauses to apply to this field (And&#39;ed together)
    aggregations=[],  # optional — Aggregations to apply (as opposed to simply selecting)
    is_expression=True  # optional — Is this field an expression
)
```

- [DataType](DataType.md)
- [FilterTermDesign](FilterTermDesign.md) — used in `filters`
- [Aggregation](Aggregation.md) — used in `aggregations`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

