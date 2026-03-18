# BookTransactionsResponse

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **values** | [Dict[str, Transaction]](Transaction.md) | Optional | *No description available.* |
| **failed** | [Dict[str, ErrorDetail]](ErrorDetail.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.BookTransactionsResponse import BookTransactionsResponse

instance = BookTransactionsResponse(
    values=Transaction(...),  # optional
    failed=ErrorDetail(...)  # optional
)
```


## Related Models

- [Transaction](Transaction.md)
- [ErrorDetail](ErrorDetail.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

