# TransactionSettlementInstruction

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **settlement_instruction_id** | **str** | Required | The instruction identifier. Unique within the portfolio. |
| **instruction_type** | **str** | Required | The type of instruction which can be Complete or CancelAutomatic. Complete means that the instruction is intended to completely settle a settlement bucket. CancelAutomatic means that it is intended to cancel Automatic settlement. |
| **actual_settlement_date** | **datetime** | Required | The date that settlement takes place. |
| **units** | **float** | Required | The number of units for the instruction. |
| **transaction_id** | **str** | Required | The ID for the transaction being instructed. |
| **settlement_category** | **str** | Required | A category representing the set of movement types that this instruction applies to. |
| **lusid_instrument_id** | **str** | Required | The LusidInstrumentId of the instrument being settled. |
| **contractual_settlement_date** | **datetime** | Optional | The contractual settlement date. Used to match the instruction to the correct settlement bucket. |
| **sub_holding_key_overrides** | [Dict[str, PerpetualProperty]](PerpetualProperty.md) | Optional | Allows one or more sub-holding keys to be overridden for any movement being settled by an instruction. Providing a key and value will set the sub-holding key to the specified value; Providing a key only will nullify the sub-holding key. Not referenced sub-holding keys will not be impacted.  |
| **custodian_account_override** | [ResourceId](ResourceId.md) | Optional | *No description available.* |
| **instrument_identifiers** | **Dict[str, Optional[str]]** | Required | A set of instrument identifiers that can resolve the settlement instruction to a unique instrument. |
| **status** | **str** | Optional | The status of the settlement instruction - &#39;Invalid&#39;, &#39;Rejected&#39; &#39;Applied&#39; or &#39;Orphan&#39;. |
| **instruction_to_portfolio_rate** | **float** | Optional | The exchange rate between the Settlement Instruction and Portfolio. |
| **settlement_in_lieu** | [SettlementInLieu](SettlementInLieu.md) | Optional | *No description available.* |
| **is_active** | **bool** | Optional | Indicates whether the settlement instruction is active. When false, the instruction has no impact on settlement positions, but remains visible. Defaults to true. |
| **properties** | [Dict[str, PerpetualProperty]](PerpetualProperty.md) | Optional | The properties which have been requested to be decorated onto the settlement instruction. These will be from the &#39;SettlementInstruction&#39;, &#39;Portfolio&#39;, or &#39;Instrument&#39; domains. |
| **version** | [Version](Version.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.TransactionSettlementInstruction import TransactionSettlementInstruction

instance = TransactionSettlementInstruction(
    settlement_instruction_id="...",  # required — The instruction identifier. Unique within the portfolio.
    instruction_type="...",  # required — The type of instruction which can be Complete or CancelAutomatic. Complete means that the instruction is intended to completely settle a settlement bucket. CancelAutomatic means that it is intended to cancel Automatic settlement.
    actual_settlement_date=datetime.now(),  # required — The date that settlement takes place.
    units=0.0,  # required — The number of units for the instruction.
    transaction_id="...",  # required — The ID for the transaction being instructed.
    settlement_category="...",  # required — A category representing the set of movement types that this instruction applies to.
    lusid_instrument_id="...",  # required — The LusidInstrumentId of the instrument being settled.
    contractual_settlement_date=datetime.now(),  # optional — The contractual settlement date. Used to match the instruction to the correct settlement bucket.
    sub_holding_key_overrides=PerpetualProperty(...),  # optional — Allows one or more sub-holding keys to be overridden for any movement being settled by an instruction. Providing a key and value will set the sub-holding key to the specified value; Providing a key only will nullify the sub-holding key. Not referenced sub-holding keys will not be impacted. 
    custodian_account_override=ResourceId(...),  # optional
    instrument_identifiers=,  # required — A set of instrument identifiers that can resolve the settlement instruction to a unique instrument.
    status="...",  # optional — The status of the settlement instruction - &#39;Invalid&#39;, &#39;Rejected&#39; &#39;Applied&#39; or &#39;Orphan&#39;.
    instruction_to_portfolio_rate=0.0,  # optional — The exchange rate between the Settlement Instruction and Portfolio.
    settlement_in_lieu=SettlementInLieu(...),  # optional
    is_active=True,  # optional — Indicates whether the settlement instruction is active. When false, the instruction has no impact on settlement positions, but remains visible. Defaults to true.
    properties=PerpetualProperty(...),  # optional — The properties which have been requested to be decorated onto the settlement instruction. These will be from the &#39;SettlementInstruction&#39;, &#39;Portfolio&#39;, or &#39;Instrument&#39; domains.
    version=Version(...)  # optional
)
```

- [PerpetualProperty](PerpetualProperty.md) — used in `sub_holding_key_overrides`
- [ResourceId](ResourceId.md)
- [SettlementInLieu](SettlementInLieu.md)
- [PerpetualProperty](PerpetualProperty.md) — used in `properties`
- [Version](Version.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

