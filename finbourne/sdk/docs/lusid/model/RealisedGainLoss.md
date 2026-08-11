# RealisedGainLoss

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **instrument_scope** | **str** | Optional | The scope in which the instrument lies. |
| **instrument_uid** | **str** | Required | The unique Lusid Instrument Id (LUID) of the instrument that this gain or loss is associated with. |
| **units** | **float** | Required | The number of units of the associated instrument against which the gain or loss has been realised. |
| **purchase_trade_date** | **datetime** | Optional | The effective datetime at which the units associated with this gain or loss were originally purchased. *(read-only)* |
| **purchase_settlement_date** | **datetime** | Optional | The effective datetime at which the units associated with this gain or loss were originally settled. *(read-only)* |
| **purchase_price** | **float** | Optional | The purchase price of each unit associated with this gain or loss. |
| **cost_trade_ccy** | [CurrencyAndAmount](CurrencyAndAmount.md) | Required | *No description available.* |
| **cost_portfolio_ccy** | [CurrencyAndAmount](CurrencyAndAmount.md) | Required | *No description available.* |
| **realised_trade_ccy** | [CurrencyAndAmount](CurrencyAndAmount.md) | Required | *No description available.* |
| **realised_total** | [CurrencyAndAmount](CurrencyAndAmount.md) | Required | *No description available.* |
| **realised_market** | [CurrencyAndAmount](CurrencyAndAmount.md) | Optional | *No description available.* |
| **realised_currency** | [CurrencyAndAmount](CurrencyAndAmount.md) | Optional | *No description available.* |
| **tax_lot_id** | **str** | Optional | The identifier of the tax lot with which this gain or loss is associated. |
| **realised_amortisation** | [CurrencyAndAmount](CurrencyAndAmount.md) | Optional | *No description available.* |
| **trade_date_to_settlement_date_realised_currency** | [CurrencyAndAmount](CurrencyAndAmount.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.RealisedGainLoss import RealisedGainLoss

instance = RealisedGainLoss(
    instrument_scope="...",  # optional — The scope in which the instrument lies.
    instrument_uid="...",  # required — The unique Lusid Instrument Id (LUID) of the instrument that this gain or loss is associated with.
    units=0.0,  # required — The number of units of the associated instrument against which the gain or loss has been realised.
    purchase_trade_date=datetime.now(),  # optional — The effective datetime at which the units associated with this gain or loss were originally purchased.
    purchase_settlement_date=datetime.now(),  # optional — The effective datetime at which the units associated with this gain or loss were originally settled.
    purchase_price=0.0,  # optional — The purchase price of each unit associated with this gain or loss.
    cost_trade_ccy=CurrencyAndAmount(...),  # required
    cost_portfolio_ccy=CurrencyAndAmount(...),  # required
    realised_trade_ccy=CurrencyAndAmount(...),  # required
    realised_total=CurrencyAndAmount(...),  # required
    realised_market=CurrencyAndAmount(...),  # optional
    realised_currency=CurrencyAndAmount(...),  # optional
    tax_lot_id="...",  # optional — The identifier of the tax lot with which this gain or loss is associated.
    realised_amortisation=CurrencyAndAmount(...),  # optional
    trade_date_to_settlement_date_realised_currency=CurrencyAndAmount(...)  # optional
)
```

- [CurrencyAndAmount](CurrencyAndAmount.md)
- [CurrencyAndAmount](CurrencyAndAmount.md)
- [CurrencyAndAmount](CurrencyAndAmount.md)
- [CurrencyAndAmount](CurrencyAndAmount.md)
- [CurrencyAndAmount](CurrencyAndAmount.md)
- [CurrencyAndAmount](CurrencyAndAmount.md)
- [CurrencyAndAmount](CurrencyAndAmount.md)
- [CurrencyAndAmount](CurrencyAndAmount.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

