# AccessMetadataOperation

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **value** | [List[AccessMetadataValue]](AccessMetadataValue.md) | Required | *No description available.* |
| **path** | **str** | Required | *No description available.* |
| **op** | **str** | Required | The available values are: add, remove |
| **var_from** | **str** | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.AccessMetadataOperation import AccessMetadataOperation

instance = AccessMetadataOperation(
    value=[],  # required
    path="...",  # required
    op="...",  # required — The available values are: add, remove
    var_from="..."  # optional
)
```


## Related Models

- [AccessMetadataValue](AccessMetadataValue.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

