# SettlementConfigurationCategory

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **method** | **str** | Optional | The method of settlement for the movements of the relevant type(s). Allowed values: &#39;Automatic&#39; and &#39;Instructed&#39;. A value of &#39;Instructed&#39; means that such movements can only be settled with a SettlementInstruction. A value of &#39;Automatic&#39; means that such movements will settle automatically but a SettlementInstruction will still override automatic settlement. |
| **calculate_instruction_to_portfolio_rate** | **bool** | Optional | An optional flag that allows for the calculation of the instruction to portfolio rate for instructions with settlement category CashSettlement or DeferredCashReceipt, if it is not provided on the settlement instruction. Defaults to false if not specified. |
| **calculate_in_lieu_settlement_amount** | **bool** | Optional | An optional flag that allows for the calculation of the in lieu amount for instructions with settlement category CashSettlement or DeferredCashReceipt, if it is not provided on the settlement instruction. Defaults to false if not specified. |
| **method_override** | [SettlementConfigurationMethodOverride](SettlementConfigurationMethodOverride.md) | Optional | *No description available.* |
| **calculate_trade_date_to_settlement_fx_pn_l** | **bool** | Optional | An optional flag that allows for the calculation of the in lieu amount for instructions with settlement category CashSettlement or DeferredCashReceipt, if it is not provided on the settlement instruction. Defaults to false if not specified. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.SettlementConfigurationCategory import SettlementConfigurationCategory

instance = SettlementConfigurationCategory(
    method="...",  # optional — The method of settlement for the movements of the relevant type(s). Allowed values: &#39;Automatic&#39; and &#39;Instructed&#39;. A value of &#39;Instructed&#39; means that such movements can only be settled with a SettlementInstruction. A value of &#39;Automatic&#39; means that such movements will settle automatically but a SettlementInstruction will still override automatic settlement.
    calculate_instruction_to_portfolio_rate=True,  # optional — An optional flag that allows for the calculation of the instruction to portfolio rate for instructions with settlement category CashSettlement or DeferredCashReceipt, if it is not provided on the settlement instruction. Defaults to false if not specified.
    calculate_in_lieu_settlement_amount=True,  # optional — An optional flag that allows for the calculation of the in lieu amount for instructions with settlement category CashSettlement or DeferredCashReceipt, if it is not provided on the settlement instruction. Defaults to false if not specified.
    method_override=SettlementConfigurationMethodOverride(...),  # optional
    calculate_trade_date_to_settlement_fx_pn_l=True  # optional — An optional flag that allows for the calculation of the in lieu amount for instructions with settlement category CashSettlement or DeferredCashReceipt, if it is not provided on the settlement instruction. Defaults to false if not specified.
)
```

- [SettlementConfigurationMethodOverride](SettlementConfigurationMethodOverride.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

