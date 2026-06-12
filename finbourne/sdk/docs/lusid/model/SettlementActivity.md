# SettlementActivity

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **activity_id** | **str** | Required | A unique identifier for the settlement activity row, composed from the portfolio, activity type and the underlying transaction or settlement instruction. |
| **portfolio_id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **activity_type** | **str** | Required | The type of settlement activity: Expected for outstanding units that are due or overdue, or Settled for units that have settled. Available values: Expected, Settled. |
| **activity_basis** | **str** | Required | The basis on which the settlement activity arose: Inferred for outstanding units, Automatic for units settled per the portfolio&#39;s settlement configuration, or Instruction for units settled by a settlement instruction. Available values: Inferred, Automatic, Instruction. |
| **activity_date** | **datetime** | Required | The date of the settlement activity. For Expected activity this is the query&#39;s end activity date; for Automatic settlement it is the contractual settlement date; for Instruction settlement it is the instruction&#39;s actual settlement date. |
| **settlement_category** | **str** | Required | The settlement category of the underlying movements. Available values: StockSettlement, CashSettlement, DeferredCashReceipt, NotApplicable. |
| **transaction_id** | **str** | Optional | The identifier of the transaction that gave rise to this settlement activity. Always populated for Expected and Settled activity. |
| **settlement_instruction_id** | **str** | Optional | The identifier of the settlement instruction that settled the activity. Populated only for Instruction settlement; null for Inferred and Automatic activity. |
| **holding_ids** | **List[int]** | Optional | The identifiers of the holdings whose movements contributed to this settlement activity. |
| **lusid_instrument_id** | **str** | Required | The LUSID instrument identifier (LUID) of the instrument being settled. |
| **instrument_scope** | **str** | Required | The scope in which the instrument is defined. |
| **contractual_settlement_date** | **datetime** | Required | The contractual settlement date of the underlying movements. |
| **custodian_account_id** | [ResourceId](ResourceId.md) | Optional | *No description available.* |
| **custodian_account_number** | **str** | Optional | The account number of the associated custodian account, if any. |
| **custodian_account_name** | **str** | Optional | The name of the associated custodian account, if any. |
| **units** | **float** | Required | The signed number of units settled or expected to settle for this activity. |
| **direction** | **str** | Required | The direction of the settlement from the portfolio&#39;s perspective. Available values: Debit, Credit. |
| **days_overdue** | **float** | Optional | The number of days the activity is overdue, calculated as the activity date minus the contractual settlement date. Zero for settled activity. |
| **transaction** | [OutputTransaction](OutputTransaction.md) | Optional | *No description available.* |
| **settlement_instruction** | [TransactionSettlementInstruction](TransactionSettlementInstruction.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.SettlementActivity import SettlementActivity

instance = SettlementActivity(
    activity_id="...",  # required — A unique identifier for the settlement activity row, composed from the portfolio, activity type and the underlying transaction or settlement instruction.
    portfolio_id=ResourceId(...),  # required
    activity_type="...",  # required — The type of settlement activity: Expected for outstanding units that are due or overdue, or Settled for units that have settled. Available values: Expected, Settled.
    activity_basis="...",  # required — The basis on which the settlement activity arose: Inferred for outstanding units, Automatic for units settled per the portfolio&#39;s settlement configuration, or Instruction for units settled by a settlement instruction. Available values: Inferred, Automatic, Instruction.
    activity_date=datetime.now(),  # required — The date of the settlement activity. For Expected activity this is the query&#39;s end activity date; for Automatic settlement it is the contractual settlement date; for Instruction settlement it is the instruction&#39;s actual settlement date.
    settlement_category="...",  # required — The settlement category of the underlying movements. Available values: StockSettlement, CashSettlement, DeferredCashReceipt, NotApplicable.
    transaction_id="...",  # optional — The identifier of the transaction that gave rise to this settlement activity. Always populated for Expected and Settled activity.
    settlement_instruction_id="...",  # optional — The identifier of the settlement instruction that settled the activity. Populated only for Instruction settlement; null for Inferred and Automatic activity.
    holding_ids=,  # optional — The identifiers of the holdings whose movements contributed to this settlement activity.
    lusid_instrument_id="...",  # required — The LUSID instrument identifier (LUID) of the instrument being settled.
    instrument_scope="...",  # required — The scope in which the instrument is defined.
    contractual_settlement_date=datetime.now(),  # required — The contractual settlement date of the underlying movements.
    custodian_account_id=ResourceId(...),  # optional
    custodian_account_number="...",  # optional — The account number of the associated custodian account, if any.
    custodian_account_name="...",  # optional — The name of the associated custodian account, if any.
    units=0.0,  # required — The signed number of units settled or expected to settle for this activity.
    direction="...",  # required — The direction of the settlement from the portfolio&#39;s perspective. Available values: Debit, Credit.
    days_overdue=0.0,  # optional — The number of days the activity is overdue, calculated as the activity date minus the contractual settlement date. Zero for settled activity.
    transaction=OutputTransaction(...),  # optional
    settlement_instruction=TransactionSettlementInstruction(...)  # optional
)
```

- [ResourceId](ResourceId.md)
- [ResourceId](ResourceId.md)
- [OutputTransaction](OutputTransaction.md)
- [TransactionSettlementInstruction](TransactionSettlementInstruction.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

