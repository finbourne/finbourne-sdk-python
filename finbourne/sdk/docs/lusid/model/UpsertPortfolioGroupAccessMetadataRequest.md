# UpsertPortfolioGroupAccessMetadataRequest

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **metadata** | [List[AccessMetadataValue]](AccessMetadataValue.md) | Required | The access control metadata to assign to portfolio groups that match the identifier |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.UpsertPortfolioGroupAccessMetadataRequest import UpsertPortfolioGroupAccessMetadataRequest

instance = UpsertPortfolioGroupAccessMetadataRequest(
    metadata=[]  # required — The access control metadata to assign to portfolio groups that match the identifier
)
```


## Related Models

- [AccessMetadataValue](AccessMetadataValue.md) — used in `metadata`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

