# QueryDesign

Representation of a \"designable Query\" suitable for formatting to SQL or being built from compliant SQL.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **table_name** | **str** | Required | Name of the table being designed |
| **alias** | **str** | Optional | Alias for the table in the generated SQL, if any |
| **fields** | [List[FieldDesign]](FieldDesign.md) | Required | Fields to be selected, aggregated over and/or filtered on |
| **joined_tables** | [List[JoinedTableDesign]](JoinedTableDesign.md) | Optional | Joined in table to the main TableName / Alias |
| **order_by** | [List[OrderByTermDesign]](OrderByTermDesign.md) | Optional | Order By clauses to apply |
| **limit** | **int** | Optional | Row limit to apply, if any |
| **offset** | **int** | Optional | Row offset to apply, if any |
| **warnings** | **List[str]** | Optional | Any warnings to show the user when converting from SQL to this representation |
| **available_fields** | [List[AvailableField]](AvailableField.md) | Optional | Fields that are known to be available for design when parsing SQL |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.luminesce.models.QueryDesign import QueryDesign

instance = QueryDesign(
    table_name="...",  # required — Name of the table being designed
    alias="...",  # optional — Alias for the table in the generated SQL, if any
    fields=[],  # required — Fields to be selected, aggregated over and/or filtered on
    joined_tables=[],  # optional — Joined in table to the main TableName / Alias
    order_by=[],  # optional — Order By clauses to apply
    limit=0,  # optional — Row limit to apply, if any
    offset=0,  # optional — Row offset to apply, if any
    warnings=,  # optional — Any warnings to show the user when converting from SQL to this representation
    available_fields=[]  # optional — Fields that are known to be available for design when parsing SQL
)
```

- [FieldDesign](FieldDesign.md) — used in `fields`
- [JoinedTableDesign](JoinedTableDesign.md) — used in `joined_tables`
- [OrderByTermDesign](OrderByTermDesign.md) — used in `order_by`
- [AvailableField](AvailableField.md) — used in `available_fields`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

