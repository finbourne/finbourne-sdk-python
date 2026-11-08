# ExportColumn

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **col_id** | **str** | Required | *No description available.* |
| **header** | **str** | Optional | *No description available.* |
| **data_type** | [ExportColumnDataType](ExportColumnDataType.md) | Optional | *No description available.* |
| **hidden** | **bool** | Optional | *No description available.* |
| **wrap_text** | **bool** | Optional | *No description available.* |
| **column_color** | [ExportColumnColor](ExportColumnColor.md) | Optional | *No description available.* |
| **number** | [ExportNumberFormat](ExportNumberFormat.md) | Optional | *No description available.* |
| **var_date** | [ExportDateFormat](ExportDateFormat.md) | Optional | *No description available.* |
| **conditional_rules** | [List[ExportConditionalRule]](ExportConditionalRule.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.luminesce.models.ExportColumn import ExportColumn

instance = ExportColumn(
    col_id="...",  # required
    header="...",  # optional
    data_type=ExportColumnDataType(...),  # optional
    hidden=True,  # optional
    wrap_text=True,  # optional
    column_color=ExportColumnColor(...),  # optional
    number=ExportNumberFormat(...),  # optional
    var_date=ExportDateFormat(...),  # optional
    conditional_rules=[]  # optional
)
```

- [ExportColumnDataType](ExportColumnDataType.md)
- [ExportColumnColor](ExportColumnColor.md)
- [ExportNumberFormat](ExportNumberFormat.md)
- [ExportDateFormat](ExportDateFormat.md)
- [ExportConditionalRule](ExportConditionalRule.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

