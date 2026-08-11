# UpsertPortfolioTransactionsResponse

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **version** | [Version](Version.md) | Required | *No description available.* |
| **href** | **str** | Optional | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. |
| **metadata** | **Dict[str, Optional[List[ResponseMetaData]]]** | Optional | Contains warnings related to unresolved instruments or non-existent transaction types for the upserted trades |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.UpsertPortfolioTransactionsResponse import UpsertPortfolioTransactionsResponse

instance = UpsertPortfolioTransactionsResponse(
    version=Version(...),  # required
    href="...",  # optional — The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.
    metadata=,  # optional — Contains warnings related to unresolved instruments or non-existent transaction types for the upserted trades
    links=[]  # optional
)
```


## Related Models

- [Version](Version.md)
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

