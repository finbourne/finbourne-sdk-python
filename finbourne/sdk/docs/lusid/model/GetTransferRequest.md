# GetTransferRequest

The transfer to read. Every part of its identity is required: a transfer is identified by its scope, its code  and the two portfolios its in and out transaction are booked into.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **transfer_id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **portfolio_id_out** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **portfolio_id_in** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **property_keys** | **List[str]** | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.GetTransferRequest import GetTransferRequest

instance = GetTransferRequest(
    transfer_id=ResourceId(...),  # required
    portfolio_id_out=ResourceId(...),  # required
    portfolio_id_in=ResourceId(...),  # required
    property_keys=  # optional
)
```


## Related Models

- [ResourceId](ResourceId.md)
- [ResourceId](ResourceId.md)
- [ResourceId](ResourceId.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

