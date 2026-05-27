# NavSettlementConfigurationCategory

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **calculate_instruction_to_portfolio_rate** | **bool** | Optional | An optional flag that allows for the calculation of the instruction to portfolio rate for instructions with settlement category CashSettlement or DeferredCashReceipt, if it is not provided on the settlement instruction. |
| **calculate_trade_date_to_settlement_fx_pn_l** | **bool** | Optional | An optional flag that allows for the calculation of FxPnL between Trade and Settlement Date. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.NavSettlementConfigurationCategory import NavSettlementConfigurationCategory

instance = NavSettlementConfigurationCategory(
    calculate_instruction_to_portfolio_rate=True,  # optional — An optional flag that allows for the calculation of the instruction to portfolio rate for instructions with settlement category CashSettlement or DeferredCashReceipt, if it is not provided on the settlement instruction.
    calculate_trade_date_to_settlement_fx_pn_l=True  # optional — An optional flag that allows for the calculation of FxPnL between Trade and Settlement Date.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

