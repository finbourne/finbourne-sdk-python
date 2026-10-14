# UpsertTransferAgencyTransactionFromOrderRequest

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **order_id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **price_date** | **datetime** | Required | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.UpsertTransferAgencyTransactionFromOrderRequest import UpsertTransferAgencyTransactionFromOrderRequest

instance = UpsertTransferAgencyTransactionFromOrderRequest(
    order_id=ResourceId(...),  # required
    price_date=datetime.now()  # required
)
```


## Related Models

- [ResourceId](ResourceId.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

