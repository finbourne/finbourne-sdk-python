# TargetTaxLotRequest

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **units** | **float** | Required | The number of units of the instrument in this tax-lot. |
| **cost** | [CurrencyAndAmount](CurrencyAndAmount.md) | Optional | *No description available.* |
| **portfolio_cost** | **float** | Optional | The total cost of the tax-lot in the transaction portfolio&#39;s base currency. |
| **price** | **float** | Optional | The purchase price of each unit of the instrument held in this tax-lot. This forms part of the unique key required for multiple tax-lots. |
| **purchase_date** | **datetime** | Optional | The purchase date of this tax-lot. This forms part of the unique key required for multiple tax-lots. |
| **settlement_date** | **datetime** | Optional | The settlement date of the tax-lot&#39;s opening transaction. |
| **notional_cost** | **float** | Optional | The notional cost of the tax-lot&#39;s opening transaction. |
| **variation_margin** | **float** | Optional | The variation margin of the tax-lot&#39;s opening transaction. |
| **variation_margin_portfolio_ccy** | **float** | Optional | The variation margin in portfolio currency of the tax-lot&#39;s opening transaction. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.TargetTaxLotRequest import TargetTaxLotRequest

instance = TargetTaxLotRequest(
    units=0.0,  # required — The number of units of the instrument in this tax-lot.
    cost=CurrencyAndAmount(...),  # optional
    portfolio_cost=0.0,  # optional — The total cost of the tax-lot in the transaction portfolio&#39;s base currency.
    price=0.0,  # optional — The purchase price of each unit of the instrument held in this tax-lot. This forms part of the unique key required for multiple tax-lots.
    purchase_date=datetime.now(),  # optional — The purchase date of this tax-lot. This forms part of the unique key required for multiple tax-lots.
    settlement_date=datetime.now(),  # optional — The settlement date of the tax-lot&#39;s opening transaction.
    notional_cost=0.0,  # optional — The notional cost of the tax-lot&#39;s opening transaction.
    variation_margin=0.0,  # optional — The variation margin of the tax-lot&#39;s opening transaction.
    variation_margin_portfolio_ccy=0.0  # optional — The variation margin in portfolio currency of the tax-lot&#39;s opening transaction.
)
```

- [CurrencyAndAmount](CurrencyAndAmount.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

