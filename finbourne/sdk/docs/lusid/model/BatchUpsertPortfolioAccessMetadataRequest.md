# BatchUpsertPortfolioAccessMetadataRequest

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **portfolio_id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **metadata** | **Dict[str, Optional[List[AccessMetadataValue]]]** | Required | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.BatchUpsertPortfolioAccessMetadataRequest import BatchUpsertPortfolioAccessMetadataRequest

instance = BatchUpsertPortfolioAccessMetadataRequest(
    portfolio_id=ResourceId(...),  # required
    metadata=  # required
)
```


## Related Models

- [ResourceId](ResourceId.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

