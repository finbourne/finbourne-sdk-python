# ColumnInfo

Information on how to construct a file-read sql query
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **select** | **bool** | Optional | Should the column be used/selected? |
| **type** | [DataType](DataType.md) | Optional | *No description available.* |
| **name** | **str** | Optional | The name of the column |
| **x_path** | **str** | Optional | Xpath for the column (only applicable to XML defined columns) |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.luminesce.models.ColumnInfo import ColumnInfo

instance = ColumnInfo(
    select=True,  # optional — Should the column be used/selected?
    type=DataType(...),  # optional
    name="...",  # optional — The name of the column
    x_path="..."  # optional — Xpath for the column (only applicable to XML defined columns)
)
```

- [DataType](DataType.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

