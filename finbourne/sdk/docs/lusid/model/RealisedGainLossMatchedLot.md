# RealisedGainLossMatchedLot

The lot a realised chargeable-gains leg was matched against: its cost in the portfolio currency, the date of the  acquisition that opened it and its chargeable-gains role.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **original_cost** | [CurrencyAndAmount](CurrencyAndAmount.md) | Optional | *No description available.* |
| **purchase_date** | **datetime** | Optional | *No description available.* |
| **role** | **str** | Optional | Available values: DayLot, Section104Pool, Holding1982, Holding1965, FutureAcquisition. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.RealisedGainLossMatchedLot import RealisedGainLossMatchedLot

instance = RealisedGainLossMatchedLot(
    original_cost=CurrencyAndAmount(...),  # optional
    purchase_date=datetime.now(),  # optional
    role="..."  # optional — Available values: DayLot, Section104Pool, Holding1982, Holding1965, FutureAcquisition.
)
```


## Related Models

- [CurrencyAndAmount](CurrencyAndAmount.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

