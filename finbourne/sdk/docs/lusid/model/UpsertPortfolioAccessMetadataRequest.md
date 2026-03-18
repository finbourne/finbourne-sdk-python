# UpsertPortfolioAccessMetadataRequest

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **metadata** | [List[AccessMetadataValue]](AccessMetadataValue.md) | Required | The access control metadata to assign to portfolios that match the identifier |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.UpsertPortfolioAccessMetadataRequest import UpsertPortfolioAccessMetadataRequest

instance = UpsertPortfolioAccessMetadataRequest(
    metadata=[]  # required — The access control metadata to assign to portfolios that match the identifier
)
```


## Related Models

- [AccessMetadataValue](AccessMetadataValue.md) — used in `metadata`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

