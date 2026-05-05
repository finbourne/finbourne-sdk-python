# FundCashStatementRow

A single row in a Fund Cash Statement report.  Each row represents a settled cash movement with running balance, cost basis,  average rate, and realised FX PnL.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **group_by_id** | **int** | Optional | The groupBy subHoldings and currency. |
| **sequence_number** | **int** | Optional | Sequence number determining the order of the cash flow records. |
| **sub_holding_keys** | [Dict[str, PerpetualProperty]](PerpetualProperty.md) | Optional | The sub-holding properties which identify the holding. Each property will be from the &#39;Transaction&#39; domain. These are configured on a transaction portfolio. |
| **source_id** | **str** | Optional | The transaction ID that sourced this cash movement. |
| **cash_statement_action_type** | **str** | Optional | The action type: Default, Reversal, TrueUp, AvgRateCorrection, Opening, or Closing. |
| **accounting_date** | **datetime** | Optional | The accounting date of the cash movement. |
| **activity_date** | **datetime** | Optional | The activity date (trade/settlement date) of the cash movement. |
| **movement_name** | **str** | Optional | The movement type (e.g. Receivable_Cash_Trade, Payable_Cash_Trade). |
| **portfolio_id** | [ResourceId](ResourceId.md) | Optional | *No description available.* |
| **instruction_type** | **str** | Optional | The settlement instruction type: Automatic, Instructed_Complete, Instructed - Cancel Automatic. |
| **diary_entry_code** | **str** | Optional | The diary entry code of the valuation point this row belongs to. |
| **origin_diary_entry_code** | **str** | Optional | For Reversal/TrueUp rows: the diary entry code of the period the original row belonged to. |
| **cashflow_local** | [CurrencyAndAmount](CurrencyAndAmount.md) | Optional | *No description available.* |
| **balance_local** | [CurrencyAndAmount](CurrencyAndAmount.md) | Optional | *No description available.* |
| **cashflow_base** | [CurrencyAndAmount](CurrencyAndAmount.md) | Optional | *No description available.* |
| **realised_fx_pnl** | [CurrencyAndAmount](CurrencyAndAmount.md) | Optional | *No description available.* |
| **cost_basis_base** | [CurrencyAndAmount](CurrencyAndAmount.md) | Optional | *No description available.* |
| **avg_rate** | **float** | Optional | Weighted average FX rate (costBasisBase / balanceLocal). Null when balance is zero. |
| **fx_rate_movement** | **float** | Optional | FX rate for this specific movement (CashflowBase / CashFlowLocal). Null when localAmount is zero. |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.FundCashStatementRow import FundCashStatementRow

instance = FundCashStatementRow(
    group_by_id=0,  # optional — The groupBy subHoldings and currency.
    sequence_number=0,  # optional — Sequence number determining the order of the cash flow records.
    sub_holding_keys=PerpetualProperty(...),  # optional — The sub-holding properties which identify the holding. Each property will be from the &#39;Transaction&#39; domain. These are configured on a transaction portfolio.
    source_id="...",  # optional — The transaction ID that sourced this cash movement.
    cash_statement_action_type="...",  # optional — The action type: Default, Reversal, TrueUp, AvgRateCorrection, Opening, or Closing.
    accounting_date=datetime.now(),  # optional — The accounting date of the cash movement.
    activity_date=datetime.now(),  # optional — The activity date (trade/settlement date) of the cash movement.
    movement_name="...",  # optional — The movement type (e.g. Receivable_Cash_Trade, Payable_Cash_Trade).
    portfolio_id=ResourceId(...),  # optional
    instruction_type="...",  # optional — The settlement instruction type: Automatic, Instructed_Complete, Instructed - Cancel Automatic.
    diary_entry_code="...",  # optional — The diary entry code of the valuation point this row belongs to.
    origin_diary_entry_code="...",  # optional — For Reversal/TrueUp rows: the diary entry code of the period the original row belonged to.
    cashflow_local=CurrencyAndAmount(...),  # optional
    balance_local=CurrencyAndAmount(...),  # optional
    cashflow_base=CurrencyAndAmount(...),  # optional
    realised_fx_pnl=CurrencyAndAmount(...),  # optional
    cost_basis_base=CurrencyAndAmount(...),  # optional
    avg_rate=0.0,  # optional — Weighted average FX rate (costBasisBase / balanceLocal). Null when balance is zero.
    fx_rate_movement=0.0,  # optional — FX rate for this specific movement (CashflowBase / CashFlowLocal). Null when localAmount is zero.
    links=[]  # optional
)
```

- [PerpetualProperty](PerpetualProperty.md) — used in `sub_holding_keys`
- [ResourceId](ResourceId.md)
- [CurrencyAndAmount](CurrencyAndAmount.md)
- [CurrencyAndAmount](CurrencyAndAmount.md)
- [CurrencyAndAmount](CurrencyAndAmount.md)
- [CurrencyAndAmount](CurrencyAndAmount.md)
- [CurrencyAndAmount](CurrencyAndAmount.md)
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

