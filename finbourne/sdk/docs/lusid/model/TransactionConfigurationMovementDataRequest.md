# TransactionConfigurationMovementDataRequest

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **movement_types** | **str** | Required | . The available values are: Settlement, Traded, StockMovement, FutureCash, Commitment, Receivable, CashSettlement, CashForward, CashCommitment, CashReceivable, Accrual, CashAccrual, ForwardFx, CashFxForward, Carry, CarryAsPnl, VariationMargin, Capital, Fee, LimitAdjustment, BalanceAdjustment, Deferred, CashDeferred |
| **side** | **str** | Required | The movement side |
| **direction** | **int** | Required | The movement direction |
| **properties** | [Dict[str, PerpetualProperty]](PerpetualProperty.md) | Optional | The properties associated with the underlying Movement. |
| **mappings** | [List[TransactionPropertyMappingRequest]](TransactionPropertyMappingRequest.md) | Optional | This allows you to map a transaction property to a property on the underlying holding. |
| **name** | **str** | Optional | The movement name (optional) |
| **movement_options** | **List[str]** | Optional | Allows extra specifications for the movement. The options currently available are &#39;DirectAdjustment&#39;, &#39;IncludesTradedInterest&#39;, &#39;Virtual&#39;, &#39;Income&#39; and &#39;Expense&#39;. A movement type of &#39;StockMovement&#39; with an option of &#39;DirectAdjusment&#39; will allow you to adjust the units of a holding without affecting its cost base. You will, therefore, be able to reflect the impact of a stock split by loading a Transaction. A movement type of &#39;Carry&#39; with the option as &#39;Expense&#39; will not impact the interest accrual for cash-type holdings such loans, loan facilities and deposits. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.TransactionConfigurationMovementDataRequest import TransactionConfigurationMovementDataRequest

instance = TransactionConfigurationMovementDataRequest(
    movement_types="...",  # required — . The available values are: Settlement, Traded, StockMovement, FutureCash, Commitment, Receivable, CashSettlement, CashForward, CashCommitment, CashReceivable, Accrual, CashAccrual, ForwardFx, CashFxForward, Carry, CarryAsPnl, VariationMargin, Capital, Fee, LimitAdjustment, BalanceAdjustment, Deferred, CashDeferred
    side="...",  # required — The movement side
    direction=0,  # required — The movement direction
    properties=PerpetualProperty(...),  # optional — The properties associated with the underlying Movement.
    mappings=[],  # optional — This allows you to map a transaction property to a property on the underlying holding.
    name="...",  # optional — The movement name (optional)
    movement_options=  # optional — Allows extra specifications for the movement. The options currently available are &#39;DirectAdjustment&#39;, &#39;IncludesTradedInterest&#39;, &#39;Virtual&#39;, &#39;Income&#39; and &#39;Expense&#39;. A movement type of &#39;StockMovement&#39; with an option of &#39;DirectAdjusment&#39; will allow you to adjust the units of a holding without affecting its cost base. You will, therefore, be able to reflect the impact of a stock split by loading a Transaction. A movement type of &#39;Carry&#39; with the option as &#39;Expense&#39; will not impact the interest accrual for cash-type holdings such loans, loan facilities and deposits.
)
```

- [PerpetualProperty](PerpetualProperty.md) — used in `properties`
- [TransactionPropertyMappingRequest](TransactionPropertyMappingRequest.md) — used in `mappings`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

