# JoinedTableDesign

Treatment of a joined-to-table a QueryDesign
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **joined_table_name** | **str** | Required | Name of the table on the right side of the join |
| **joined_table_alias** | **str** | Required | Alias for the table on the right side of the join |
| **left_table_alias** | **str** | Required | Alias for the table on the left side of the join |
| **join_type** | [DesignJoinType](DesignJoinType.md) | Required | *No description available.* |
| **on_clause_terms** | [List[OnClauseTermDesign]](OnClauseTermDesign.md) | Required | Filter clauses to apply to this join in the on clause |
| **right_table_available_fields** | [List[AvailableField]](AvailableField.md) | Optional | Fields that are known to be available for design when parsing SQL, of the right hand table |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.luminesce.models.JoinedTableDesign import JoinedTableDesign

instance = JoinedTableDesign(
    joined_table_name="...",  # required — Name of the table on the right side of the join
    joined_table_alias="...",  # required — Alias for the table on the right side of the join
    left_table_alias="...",  # required — Alias for the table on the left side of the join
    join_type=DesignJoinType(...),  # required
    on_clause_terms=[],  # required — Filter clauses to apply to this join in the on clause
    right_table_available_fields=[]  # optional — Fields that are known to be available for design when parsing SQL, of the right hand table
)
```

- [DesignJoinType](DesignJoinType.md)
- [OnClauseTermDesign](OnClauseTermDesign.md) — used in `on_clause_terms`
- [AvailableField](AvailableField.md) — used in `right_table_available_fields`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

