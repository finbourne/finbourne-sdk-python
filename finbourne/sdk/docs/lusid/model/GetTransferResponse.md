# GetTransferResponse

A transfer and both of the transactions it booked.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **transfer_id** | [ResourceId](ResourceId.md) | Optional | *No description available.* |
| **transfer_type** | **str** | Optional | *No description available.* |
| **portfolio_id_out** | [ResourceId](ResourceId.md) | Optional | *No description available.* |
| **portfolio_id_in** | [ResourceId](ResourceId.md) | Optional | *No description available.* |
| **transaction_out** | [Transaction](Transaction.md) | Optional | *No description available.* |
| **transaction_in** | [Transaction](Transaction.md) | Optional | *No description available.* |
| **properties** | [Dict[str, ModelProperty]](ModelProperty.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.GetTransferResponse import GetTransferResponse

instance = GetTransferResponse(
    transfer_id=ResourceId(...),  # optional
    transfer_type="...",  # optional
    portfolio_id_out=ResourceId(...),  # optional
    portfolio_id_in=ResourceId(...),  # optional
    transaction_out=Transaction(...),  # optional
    transaction_in=Transaction(...),  # optional
    properties=ModelProperty(...)  # optional
)
```


## Related Models

- [ResourceId](ResourceId.md)
- [ResourceId](ResourceId.md)
- [ResourceId](ResourceId.md)
- [Transaction](Transaction.md)
- [Transaction](Transaction.md)
- [ModelProperty](ModelProperty.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

