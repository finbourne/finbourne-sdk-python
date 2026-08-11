# BookTransactionsResponse

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **values** | [Dict[str, Transaction]](Transaction.md) | Optional | *No description available.* |
| **failed** | [Dict[str, ErrorDetail]](ErrorDetail.md) | Optional | *No description available.* |
| **fx_orders** | [List[BlockAndOrders]](BlockAndOrders.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.BookTransactionsResponse import BookTransactionsResponse

instance = BookTransactionsResponse(
    values=Transaction(...),  # optional
    failed=ErrorDetail(...),  # optional
    fx_orders=[]  # optional
)
```


## Related Models

- [Transaction](Transaction.md)
- [ErrorDetail](ErrorDetail.md)
- [BlockAndOrders](BlockAndOrders.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

