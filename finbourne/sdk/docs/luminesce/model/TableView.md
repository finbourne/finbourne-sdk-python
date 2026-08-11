# TableView

Representation of the table structure
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **header_names** | **Dict[str, Optional[str]]** | Required | Mapping of column ids to aliases |
| **column_state** | [List[ColumnStateType]](ColumnStateType.md) | Required | Array of all columns in the dashboard |
| **filters** | [Dict[str, FilterModel]](FilterModel.md) | Optional | Filters applied to columns in the dashboard |
| **meta** | [TableMeta](TableMeta.md) | Required | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.luminesce.models.TableView import TableView

instance = TableView(
    header_names=,  # required — Mapping of column ids to aliases
    column_state=[],  # required — Array of all columns in the dashboard
    filters=FilterModel(...),  # optional — Filters applied to columns in the dashboard
    meta=TableMeta(...)  # required
)
```

- [ColumnStateType](ColumnStateType.md) — used in `column_state`
- [FilterModel](FilterModel.md) — used in `filters`
- [TableMeta](TableMeta.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

