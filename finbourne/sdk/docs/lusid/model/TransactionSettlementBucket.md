# TransactionSettlementBucket

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **settlement_category** | **str** | Required | A category representing the set of movement types that this instruction applies to. |
| **lusid_instrument_id** | **str** | Required | The LusidInstrumentId of the instrument being settled. |
| **instrument_scope** | **str** | Required | The Scope of the instrument being settled. |
| **contractual_settlement_date** | **datetime** | Optional | The contractual settlement date. Used to match the instruction to the correct settlement bucket. |
| **contracted_units** | **float** | Optional | The contracted units. |
| **settled_units** | **float** | Optional | The settled units. |
| **unsettled_units** | **float** | Optional | The unsettled units. |
| **overdue_units** | **float** | Optional | The overdue units. |
| **configured_settlement** | **str** | Optional | The method of settlement for the settlement bucket, as defined in the portfolio&#39;s SettlementConfiguration |
| **status** | **str** | Required | The Status of the settlement bucket - &#39;Settled&#39;, &#39;Part Settled&#39; or &#39;Unsettled&#39;. |
| **settlement_instructions** | [List[TransactionSettlementInstruction]](TransactionSettlementInstruction.md) | Optional | The settlement instructions received for this settlement bucket. |
| **movements** | [List[TransactionSettlementMovement]](TransactionSettlementMovement.md) | Optional | The movements for the settlement bucket. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.TransactionSettlementBucket import TransactionSettlementBucket

instance = TransactionSettlementBucket(
    settlement_category="...",  # required — A category representing the set of movement types that this instruction applies to.
    lusid_instrument_id="...",  # required — The LusidInstrumentId of the instrument being settled.
    instrument_scope="...",  # required — The Scope of the instrument being settled.
    contractual_settlement_date=datetime.now(),  # optional — The contractual settlement date. Used to match the instruction to the correct settlement bucket.
    contracted_units=0.0,  # optional — The contracted units.
    settled_units=0.0,  # optional — The settled units.
    unsettled_units=0.0,  # optional — The unsettled units.
    overdue_units=0.0,  # optional — The overdue units.
    configured_settlement="...",  # optional — The method of settlement for the settlement bucket, as defined in the portfolio&#39;s SettlementConfiguration
    status="...",  # required — The Status of the settlement bucket - &#39;Settled&#39;, &#39;Part Settled&#39; or &#39;Unsettled&#39;.
    settlement_instructions=[],  # optional — The settlement instructions received for this settlement bucket.
    movements=[]  # optional — The movements for the settlement bucket.
)
```

- [TransactionSettlementInstruction](TransactionSettlementInstruction.md) — used in `settlement_instructions`
- [TransactionSettlementMovement](TransactionSettlementMovement.md) — used in `movements`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

