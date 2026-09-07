# EstimateTransferAgencyOrderRequest

A request to estimate the values of one order. `OrderId` is required whether or not the order has been  saved, because it is the identity the estimate is returned against. Supply `Order` to estimate values  that differ from - or do not yet exist in - the saved order.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **order_id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **order** | [TransferAgencyOrderToEstimate](TransferAgencyOrderToEstimate.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.EstimateTransferAgencyOrderRequest import EstimateTransferAgencyOrderRequest

instance = EstimateTransferAgencyOrderRequest(
    order_id=ResourceId(...),  # required
    order=TransferAgencyOrderToEstimate(...)  # optional
)
```


## Related Models

- [ResourceId](ResourceId.md)
- [TransferAgencyOrderToEstimate](TransferAgencyOrderToEstimate.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

