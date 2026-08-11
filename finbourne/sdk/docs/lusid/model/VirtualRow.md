# VirtualRow

Rows identified by the composite id, based on the data maps
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **row_id** | **Dict[str, Optional[str]]** | Optional | The identifier for the row. This is keyed by address keys, and values obtained through applying the data map to the documents. |
| **row_data** | [Dict[str, ResultValue]](ResultValue.md) | Optional | The data for the particular row |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.VirtualRow import VirtualRow

instance = VirtualRow(
    row_id=,  # optional — The identifier for the row. This is keyed by address keys, and values obtained through applying the data map to the documents.
    row_data=ResultValue(...)  # optional — The data for the particular row
)
```

- [ResultValue](ResultValue.md) — used in `row_data`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

