# FundCashStatementLocalCurrency

A single row in the local-currency Fund Cash Statement report. Each row is a settled cash  movement with a running balance in local currency only; base-currency columns are out of  scope for this variant and are not returned.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **group_by_id** | **int** | Optional | The groupBy subHoldings and currency. |
| **sequence_number** | **int** | Optional | Sequence number determining the order of the cash flow records. |
| **sub_holding_keys** | [Dict[str, PerpetualProperty]](PerpetualProperty.md) | Optional | The sub-holding properties which identify the holding. Each property will be from the &#39;Transaction&#39; domain. These are configured on a transaction portfolio. |
| **source_id** | **str** | Optional | The transaction ID that sourced this cash movement. |
| **cash_statement_action_type** | **str** | Optional | The action type: Default, Reversal, TrueUp, SystemCorrection, Opening, or Closing. |
| **entry_type** | **str** | Optional | What drove the row: SystemGenerated (accounting-engine housekeeping such as a reversal/true-up around a backdated transaction) or UserEntered (a real cash movement booked by a user, e.g. a late trade or amendment). |
| **accounting_date** | **datetime** | Optional | The accounting date of the cash movement. |
| **activity_date** | **datetime** | Optional | The activity date (trade/settlement date) of the cash movement. |
| **movement_name** | **str** | Optional | The movement type (e.g. Receivable_Cash_Trade, Payable_Cash_Trade). |
| **portfolio_id** | [ResourceId](ResourceId.md) | Optional | *No description available.* |
| **instruction_type** | **str** | Optional | The settlement instruction type: Automatic, Instructed_Complete, Instructed - Cancel Automatic. |
| **diary_entry_code** | **str** | Optional | The diary entry code of the valuation point this row belongs to. |
| **origin_diary_entry_code** | **str** | Optional | For Reversal/TrueUp rows: the diary entry code of the period the original row belonged to. |
| **cashflow_local** | [CurrencyAndAmount](CurrencyAndAmount.md) | Optional | *No description available.* |
| **balance_local** | [CurrencyAndAmount](CurrencyAndAmount.md) | Optional | *No description available.* |
| **properties** | [Dict[str, ModelProperty]](ModelProperty.md) | Optional | The requested properties decorated onto the cash statement row. |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.FundCashStatementLocalCurrency import FundCashStatementLocalCurrency

instance = FundCashStatementLocalCurrency(
    group_by_id=0,  # optional — The groupBy subHoldings and currency.
    sequence_number=0,  # optional — Sequence number determining the order of the cash flow records.
    sub_holding_keys=PerpetualProperty(...),  # optional — The sub-holding properties which identify the holding. Each property will be from the &#39;Transaction&#39; domain. These are configured on a transaction portfolio.
    source_id="...",  # optional — The transaction ID that sourced this cash movement.
    cash_statement_action_type="...",  # optional — The action type: Default, Reversal, TrueUp, SystemCorrection, Opening, or Closing.
    entry_type="...",  # optional — What drove the row: SystemGenerated (accounting-engine housekeeping such as a reversal/true-up around a backdated transaction) or UserEntered (a real cash movement booked by a user, e.g. a late trade or amendment).
    accounting_date=datetime.now(),  # optional — The accounting date of the cash movement.
    activity_date=datetime.now(),  # optional — The activity date (trade/settlement date) of the cash movement.
    movement_name="...",  # optional — The movement type (e.g. Receivable_Cash_Trade, Payable_Cash_Trade).
    portfolio_id=ResourceId(...),  # optional
    instruction_type="...",  # optional — The settlement instruction type: Automatic, Instructed_Complete, Instructed - Cancel Automatic.
    diary_entry_code="...",  # optional — The diary entry code of the valuation point this row belongs to.
    origin_diary_entry_code="...",  # optional — For Reversal/TrueUp rows: the diary entry code of the period the original row belonged to.
    cashflow_local=CurrencyAndAmount(...),  # optional
    balance_local=CurrencyAndAmount(...),  # optional
    properties=ModelProperty(...),  # optional — The requested properties decorated onto the cash statement row.
    links=[]  # optional
)
```

- [PerpetualProperty](PerpetualProperty.md) — used in `sub_holding_keys`
- [ResourceId](ResourceId.md)
- [CurrencyAndAmount](CurrencyAndAmount.md)
- [CurrencyAndAmount](CurrencyAndAmount.md)
- [ModelProperty](ModelProperty.md) — used in `properties`
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

