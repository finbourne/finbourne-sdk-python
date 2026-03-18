# BatchUpsertPortfolioTransactionsResponse

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **values** | [Dict[str, Transaction]](Transaction.md) | Optional | The transactions which have been successfully upserted. |
| **failed** | [Dict[str, ErrorDetail]](ErrorDetail.md) | Optional | The transactions that could not be upserted along with a reason for their failure. |
| **metadata** | **Dict[str, Optional[List[ResponseMetaData]]]** | Optional | Contains warnings related to unresolved instruments or non-existent transaction types for the upserted trades |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.BatchUpsertPortfolioTransactionsResponse import BatchUpsertPortfolioTransactionsResponse

instance = BatchUpsertPortfolioTransactionsResponse(
    values=Transaction(...),  # optional — The transactions which have been successfully upserted.
    failed=ErrorDetail(...),  # optional — The transactions that could not be upserted along with a reason for their failure.
    metadata=,  # optional — Contains warnings related to unresolved instruments or non-existent transaction types for the upserted trades
    links=[]  # optional
)
```


## Related Models

- [Transaction](Transaction.md) — used in `values`
- [ErrorDetail](ErrorDetail.md) — used in `failed`
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

