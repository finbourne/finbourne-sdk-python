# RealisedGainLossChargeableGains

The UK chargeable-gains figures the engine worked for a realised-gain/loss leg: the chargeable gain, the  indexation allowance and the part of it taken, the proceeds the leg was worked on, both sides of the s.35  kink test on a 1982 holding, the basis and identification rule the leg was matched under, the lot it was  matched against, whether its transaction stands reversed, and the treatment applied. All amounts are in  the portfolio currency.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **chargeable_gain** | [CurrencyAndAmount](CurrencyAndAmount.md) | Optional | *No description available.* |
| **indexation_allowance** | [CurrencyAndAmount](CurrencyAndAmount.md) | Optional | *No description available.* |
| **indexation_allowance_taken** | [CurrencyAndAmount](CurrencyAndAmount.md) | Optional | *No description available.* |
| **proceeds** | [CurrencyAndAmount](CurrencyAndAmount.md) | Optional | *No description available.* |
| **gain_on_original_cost** | [CurrencyAndAmount](CurrencyAndAmount.md) | Optional | *No description available.* |
| **gain_on_market_value1982** | [CurrencyAndAmount](CurrencyAndAmount.md) | Optional | *No description available.* |
| **basis** | **str** | Optional | Available values: IndexedCost, MarketValue1982, OriginalCost, NilGain. |
| **match_rule** | **str** | Optional | Available values: SameDay, TenDay, Section210B, Section104Pool, Holding1982, Holding1965. |
| **matched_lot** | [RealisedGainLossMatchedLot](RealisedGainLossMatchedLot.md) | Optional | *No description available.* |
| **market_value1965** | [CurrencyAndAmount](CurrencyAndAmount.md) | Optional | *No description available.* |
| **reversed** | **bool** | Optional | *No description available.* |
| **tax_treatment** | **str** | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.RealisedGainLossChargeableGains import RealisedGainLossChargeableGains

instance = RealisedGainLossChargeableGains(
    chargeable_gain=CurrencyAndAmount(...),  # optional
    indexation_allowance=CurrencyAndAmount(...),  # optional
    indexation_allowance_taken=CurrencyAndAmount(...),  # optional
    proceeds=CurrencyAndAmount(...),  # optional
    gain_on_original_cost=CurrencyAndAmount(...),  # optional
    gain_on_market_value1982=CurrencyAndAmount(...),  # optional
    basis="...",  # optional — Available values: IndexedCost, MarketValue1982, OriginalCost, NilGain.
    match_rule="...",  # optional — Available values: SameDay, TenDay, Section210B, Section104Pool, Holding1982, Holding1965.
    matched_lot=RealisedGainLossMatchedLot(...),  # optional
    market_value1965=CurrencyAndAmount(...),  # optional
    reversed=True,  # optional
    tax_treatment="..."  # optional
)
```


## Related Models

- [CurrencyAndAmount](CurrencyAndAmount.md)
- [CurrencyAndAmount](CurrencyAndAmount.md)
- [CurrencyAndAmount](CurrencyAndAmount.md)
- [CurrencyAndAmount](CurrencyAndAmount.md)
- [CurrencyAndAmount](CurrencyAndAmount.md)
- [CurrencyAndAmount](CurrencyAndAmount.md)
- [RealisedGainLossMatchedLot](RealisedGainLossMatchedLot.md)
- [CurrencyAndAmount](CurrencyAndAmount.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

