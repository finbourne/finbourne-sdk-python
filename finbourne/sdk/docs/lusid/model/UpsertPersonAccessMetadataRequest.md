# UpsertPersonAccessMetadataRequest

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **metadata** | [List[AccessMetadataValue]](AccessMetadataValue.md) | Optional | The access control metadata to assign to a Person that matches the identifier |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.UpsertPersonAccessMetadataRequest import UpsertPersonAccessMetadataRequest

instance = UpsertPersonAccessMetadataRequest(
    metadata=[]  # optional — The access control metadata to assign to a Person that matches the identifier
)
```


## Related Models

- [AccessMetadataValue](AccessMetadataValue.md) — used in `metadata`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

