# CreateTransferResponse

The transfer that was created, and the transaction legs it booked.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **transfer_id** | [ResourceId](ResourceId.md) | Optional | *No description available.* |
| **transfer_type** | **str** | Optional | *No description available.* |
| **portfolio_id_out** | [ResourceId](ResourceId.md) | Optional | *No description available.* |
| **portfolio_id_in** | [ResourceId](ResourceId.md) | Optional | *No description available.* |
| **transaction_id_out** | **str** | Optional | *No description available.* |
| **transaction_id_in** | **str** | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.CreateTransferResponse import CreateTransferResponse

instance = CreateTransferResponse(
    transfer_id=ResourceId(...),  # optional
    transfer_type="...",  # optional
    portfolio_id_out=ResourceId(...),  # optional
    portfolio_id_in=ResourceId(...),  # optional
    transaction_id_out="...",  # optional
    transaction_id_in="..."  # optional
)
```


## Related Models

- [ResourceId](ResourceId.md)
- [ResourceId](ResourceId.md)
- [ResourceId](ResourceId.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

