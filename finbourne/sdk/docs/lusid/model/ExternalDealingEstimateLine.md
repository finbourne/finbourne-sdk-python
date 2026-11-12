# ExternalDealingEstimateLine

One order within an external order set: a share class, a direction and either a number of units or an amount.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **instrument_identifier_type** | **str** | Required | *No description available.* |
| **instrument_identifier** | **str** | Required | *No description available.* |
| **instrument_scope** | **str** | Optional | *No description available.* |
| **trade_type** | **str** | Required | Available values: Subscription, Redemption, SwitchOut, SwitchIn, TransferOut, TransferIn. |
| **units** | **float** | Optional | *No description available.* |
| **amount** | [ExternalDealingEstimateAmount](ExternalDealingEstimateAmount.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.ExternalDealingEstimateLine import ExternalDealingEstimateLine

instance = ExternalDealingEstimateLine(
    instrument_identifier_type="...",  # required
    instrument_identifier="...",  # required
    instrument_scope="...",  # optional
    trade_type="...",  # required — Available values: Subscription, Redemption, SwitchOut, SwitchIn, TransferOut, TransferIn.
    units=0.0,  # optional
    amount=ExternalDealingEstimateAmount(...)  # optional
)
```

- [ExternalDealingEstimateAmount](ExternalDealingEstimateAmount.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

