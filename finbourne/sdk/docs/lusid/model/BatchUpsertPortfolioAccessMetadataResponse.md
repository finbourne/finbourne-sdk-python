# BatchUpsertPortfolioAccessMetadataResponse

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **values** | [Dict[str, BatchUpsertPortfolioAccessMetadataResponseItem]](BatchUpsertPortfolioAccessMetadataResponseItem.md) | Optional | The items have been successfully updated or created. |
| **failed** | [Dict[str, ErrorDetail]](ErrorDetail.md) | Optional | The items that could not be updated or created along with a reason for their failure. |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.BatchUpsertPortfolioAccessMetadataResponse import BatchUpsertPortfolioAccessMetadataResponse

instance = BatchUpsertPortfolioAccessMetadataResponse(
    values=BatchUpsertPortfolioAccessMetadataResponseItem(...),  # optional — The items have been successfully updated or created.
    failed=ErrorDetail(...),  # optional — The items that could not be updated or created along with a reason for their failure.
    links=[]  # optional
)
```


## Related Models

- [BatchUpsertPortfolioAccessMetadataResponseItem](BatchUpsertPortfolioAccessMetadataResponseItem.md) — used in `values`
- [ErrorDetail](ErrorDetail.md) — used in `failed`
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

