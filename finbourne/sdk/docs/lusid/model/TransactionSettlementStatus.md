# TransactionSettlementStatus

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **transaction_id** | **str** | Required | The unique identifier for the transaction. |
| **settlement_buckets** | [List[TransactionSettlementBucket]](TransactionSettlementBucket.md) | Optional | The transaction&#39;s external movements (ie: with SettlementMode&#x3D;External) are grouped into buckets with each bucket uniquely defined by the combination of SettlementCategory, LusidInstrumentId, InstrumentScope and ContractualSettlementDate. |
| **invalid_instructions** | [List[TransactionSettlementInstruction]](TransactionSettlementInstruction.md) | Optional | Invalid settlement instructions where the referenced transaction exists but the settlement bucket implied by the settlement instruction does not exist. |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.TransactionSettlementStatus import TransactionSettlementStatus

instance = TransactionSettlementStatus(
    transaction_id="...",  # required — The unique identifier for the transaction.
    settlement_buckets=[],  # optional — The transaction&#39;s external movements (ie: with SettlementMode&#x3D;External) are grouped into buckets with each bucket uniquely defined by the combination of SettlementCategory, LusidInstrumentId, InstrumentScope and ContractualSettlementDate.
    invalid_instructions=[],  # optional — Invalid settlement instructions where the referenced transaction exists but the settlement bucket implied by the settlement instruction does not exist.
    links=[]  # optional
)
```

- [TransactionSettlementBucket](TransactionSettlementBucket.md) — used in `settlement_buckets`
- [TransactionSettlementInstruction](TransactionSettlementInstruction.md) — used in `invalid_instructions`
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

