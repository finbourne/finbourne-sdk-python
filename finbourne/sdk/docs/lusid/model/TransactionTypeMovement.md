# TransactionTypeMovement

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **movement_types** | **str** | Required | Movement types determine the impact of the movement on the holdings. The available values are: Settlement, Traded, StockMovement, FutureCash,  Commitment, Receivable, CashSettlement, CashForward, CashCommitment, CashReceivable, Accrual, CashAccrual, ForwardFx, CashFxForward, Carry, CarryAsPnl, VariationMargin, Capital, Fee, Deferred, CashDeferred. |
| **side** | **str** | Required | The Side determines which of the fields from our transaction are used to generate the Movement. Side1 means the &#39;security&#39; side of the transaction, ie the Instrument and Units; Side2 means the &#39;cash&#39; side, ie the Total Consideration |
| **direction** | **int** | Required |  A multiplier to apply to Transaction amounts; the values are -1 to indicate to reverse the signs and 1 to indicate to use the signed values from the Transaction directly. For a typical Transaction with unsigned values, 1 means increase, -1 means decrease |
| **properties** | [Dict[str, PerpetualProperty]](PerpetualProperty.md) | Optional | The properties associated with the underlying Movement |
| **mappings** | [List[TransactionTypePropertyMapping]](TransactionTypePropertyMapping.md) | Optional | This allows you to map a transaction property to a property on the underlying holding |
| **name** | **str** | Optional | The movement name (optional) |
| **movement_options** | **List[str]** | Optional | Allows extra specifications for the movement. The options currently available are &#39;DirectAdjustment&#39;, &#39;IncludesTradedInterest&#39;, &#39;Virtual&#39;, &#39;Income&#39; and &#39;Expense&#39;. A movement type of &#39;StockMovement&#39; with an option of &#39;DirectAdjusment&#39; will allow you to adjust the units of a holding without affecting its cost base. You will, therefore, be able to reflect the impact of a stock split by loading a Transaction. A movement type of &#39;Carry&#39; with the option as &#39;Expense&#39; will not impact the interest accrual for cash-type holdings such loans, loan facilities and deposits. |
| **settlement_date_override** | **str** | Optional | Optional property key that must be in the Transaction domain when specified. When the movement is processed and the transaction has this property set to a valid date, then the property value will override the SettlementDate of the transaction. |
| **condition** | **str** | Optional | The condition that the transaction must satisfy to generate the movement, such as: Portfolio.BaseCurrency eq &#39;GBP&#39;. The condition can contain fields and properties from transactions and portfolios. If no condition is provided, the movement will apply for all transactions of this type. |
| **settlement_mode** | **str** | Optional | Configures how movements should settle. Allowed values: &#39;Internal&#39; and &#39;External&#39;. A movement with &#39;Internal&#39; settlement mode will settle automatically on the contractual settlement date regardlesss of portfolio configuration or settlement instruction. An &#39;External&#39; movement can be settled automatically or by a settlement instruction. |
| **calculate_trade_date_to_settlement_fx_pn_l** | **bool** | Optional | Configures whether Trade To Settlement Date Realised Gain Loss should be calculated. This overrides the value set at the Portfolio level.If null, then the Portfolio Settlement Configuration TradeToSettlementDateRealisedFxPnl setting will be used.If false, then no TradeToSettlementDateRealisedFxPnl will apply for this movement and if true, then TradeToSettlementDateRealisedFxPnlwill be calculated for this movement. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.TransactionTypeMovement import TransactionTypeMovement

instance = TransactionTypeMovement(
    movement_types="...",  # required — Movement types determine the impact of the movement on the holdings. The available values are: Settlement, Traded, StockMovement, FutureCash,  Commitment, Receivable, CashSettlement, CashForward, CashCommitment, CashReceivable, Accrual, CashAccrual, ForwardFx, CashFxForward, Carry, CarryAsPnl, VariationMargin, Capital, Fee, Deferred, CashDeferred.
    side="...",  # required — The Side determines which of the fields from our transaction are used to generate the Movement. Side1 means the &#39;security&#39; side of the transaction, ie the Instrument and Units; Side2 means the &#39;cash&#39; side, ie the Total Consideration
    direction=0,  # required —  A multiplier to apply to Transaction amounts; the values are -1 to indicate to reverse the signs and 1 to indicate to use the signed values from the Transaction directly. For a typical Transaction with unsigned values, 1 means increase, -1 means decrease
    properties=PerpetualProperty(...),  # optional — The properties associated with the underlying Movement
    mappings=[],  # optional — This allows you to map a transaction property to a property on the underlying holding
    name="...",  # optional — The movement name (optional)
    movement_options=,  # optional — Allows extra specifications for the movement. The options currently available are &#39;DirectAdjustment&#39;, &#39;IncludesTradedInterest&#39;, &#39;Virtual&#39;, &#39;Income&#39; and &#39;Expense&#39;. A movement type of &#39;StockMovement&#39; with an option of &#39;DirectAdjusment&#39; will allow you to adjust the units of a holding without affecting its cost base. You will, therefore, be able to reflect the impact of a stock split by loading a Transaction. A movement type of &#39;Carry&#39; with the option as &#39;Expense&#39; will not impact the interest accrual for cash-type holdings such loans, loan facilities and deposits.
    settlement_date_override="...",  # optional — Optional property key that must be in the Transaction domain when specified. When the movement is processed and the transaction has this property set to a valid date, then the property value will override the SettlementDate of the transaction.
    condition="...",  # optional — The condition that the transaction must satisfy to generate the movement, such as: Portfolio.BaseCurrency eq &#39;GBP&#39;. The condition can contain fields and properties from transactions and portfolios. If no condition is provided, the movement will apply for all transactions of this type.
    settlement_mode="...",  # optional — Configures how movements should settle. Allowed values: &#39;Internal&#39; and &#39;External&#39;. A movement with &#39;Internal&#39; settlement mode will settle automatically on the contractual settlement date regardlesss of portfolio configuration or settlement instruction. An &#39;External&#39; movement can be settled automatically or by a settlement instruction.
    calculate_trade_date_to_settlement_fx_pn_l=True  # optional — Configures whether Trade To Settlement Date Realised Gain Loss should be calculated. This overrides the value set at the Portfolio level.If null, then the Portfolio Settlement Configuration TradeToSettlementDateRealisedFxPnl setting will be used.If false, then no TradeToSettlementDateRealisedFxPnl will apply for this movement and if true, then TradeToSettlementDateRealisedFxPnlwill be calculated for this movement.
)
```

- [PerpetualProperty](PerpetualProperty.md) — used in `properties`
- [TransactionTypePropertyMapping](TransactionTypePropertyMapping.md) — used in `mappings`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

