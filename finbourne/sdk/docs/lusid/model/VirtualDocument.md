# VirtualDocument

Virtual document consists of (potentially several) upserted documents.                The documents get parsed according to the provided data map on upsert, the collection of resulting values in  aggregated in a virtual document
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **document_id** | [StructuredResultDataId](StructuredResultDataId.md) | Optional | *No description available.* |
| **data** | [List[VirtualDocumentRow]](VirtualDocumentRow.md) | Optional | The data inside the document |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.VirtualDocument import VirtualDocument

instance = VirtualDocument(
    document_id=StructuredResultDataId(...),  # optional
    data=[]  # optional — The data inside the document
)
```


## Related Models

- [StructuredResultDataId](StructuredResultDataId.md)
- [VirtualDocumentRow](VirtualDocumentRow.md) — used in `data`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

