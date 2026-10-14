# TransferAgencyTransactionFromOrderResult

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **order_id** | [ResourceId](ResourceId.md) | Optional | *No description available.* |
| **security_transaction_id** | **str** | Optional | *No description available.* |
| **amended_cash_transaction_id** | **str** | Optional | *No description available.* |
| **price** | **float** | Optional | *No description available.* |
| **units** | **float** | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.TransferAgencyTransactionFromOrderResult import TransferAgencyTransactionFromOrderResult

instance = TransferAgencyTransactionFromOrderResult(
    order_id=ResourceId(...),  # optional
    security_transaction_id="...",  # optional
    amended_cash_transaction_id="...",  # optional
    price=0.0,  # optional
    units=0.0  # optional
)
```


## Related Models

- [ResourceId](ResourceId.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

