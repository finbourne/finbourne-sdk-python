# SettlementInstructionWithTransaction

A Settlement Instruction with its Matched Transaction (if any)
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **settlement_instruction** | [TransactionSettlementInstruction](TransactionSettlementInstruction.md) | Optional | *No description available.* |
| **matched_transaction** | [OutputTransaction](OutputTransaction.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.SettlementInstructionWithTransaction import SettlementInstructionWithTransaction

instance = SettlementInstructionWithTransaction(
    settlement_instruction=TransactionSettlementInstruction(...),  # optional
    matched_transaction=OutputTransaction(...)  # optional
)
```


## Related Models

- [TransactionSettlementInstruction](TransactionSettlementInstruction.md)
- [OutputTransaction](OutputTransaction.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

