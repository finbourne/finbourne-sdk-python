# VirtualDocumentRow

Rows identified by the composite id, based on the data maps
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **row_id** | **Dict[str, Optional[str]]** | Optional | The identifier for the row. This is keyed by address keys, and values obtained through applying the data map to the documents. |
| **row_data** | [GroupedResultOfAddressKey](GroupedResultOfAddressKey.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.VirtualDocumentRow import VirtualDocumentRow

instance = VirtualDocumentRow(
    row_id=,  # optional — The identifier for the row. This is keyed by address keys, and values obtained through applying the data map to the documents.
    row_data=GroupedResultOfAddressKey(...)  # optional
)
```

- [GroupedResultOfAddressKey](GroupedResultOfAddressKey.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

