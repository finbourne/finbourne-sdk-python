# TableExport

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **table_name** | **str** | Optional | *No description available.* |
| **columns** | [List[ExportColumn]](ExportColumn.md) | Optional | *No description available.* |
| **grouping** | [ExportGrouping](ExportGrouping.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.luminesce.models.TableExport import TableExport

instance = TableExport(
    table_name="...",  # optional
    columns=[],  # optional
    grouping=ExportGrouping(...)  # optional
)
```

- [ExportColumn](ExportColumn.md)
- [ExportGrouping](ExportGrouping.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

