# TransferAgencyOrderToEstimate

The values of an order to estimate, for an order that has not been saved yet or whose values are being  changed. Carries only what the estimate reads - it is not a whole order and cannot be used to create one.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **portfolio_id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **instrument_identifier_type** | **str** | Required | *No description available.* |
| **instrument_identifier** | **str** | Required | *No description available.* |
| **instrument_scope** | **str** | Optional | *No description available.* |
| **transaction_category** | **str** | Optional | Available values: Subscription, Redemption, SwitchOut, SwitchIn, TransferOut, TransferIn. |
| **currency** | **str** | Required | *No description available.* |
| **quantity** | **float** | Optional | *No description available.* |
| **amount** | **float** | Optional | *No description available.* |
| **weight** | **float** | Optional | *No description available.* |
| **transaction_date** | **datetime** | Optional | *No description available.* |
| **exchange_rate** | **float** | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.TransferAgencyOrderToEstimate import TransferAgencyOrderToEstimate

instance = TransferAgencyOrderToEstimate(
    portfolio_id=ResourceId(...),  # required
    instrument_identifier_type="...",  # required
    instrument_identifier="...",  # required
    instrument_scope="...",  # optional
    transaction_category="...",  # optional — Available values: Subscription, Redemption, SwitchOut, SwitchIn, TransferOut, TransferIn.
    currency="...",  # required
    quantity=0.0,  # optional
    amount=0.0,  # optional
    weight=0.0,  # optional
    transaction_date=datetime.now(),  # optional
    exchange_rate=0.0  # optional
)
```


## Related Models

- [ResourceId](ResourceId.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

