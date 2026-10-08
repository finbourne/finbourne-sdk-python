# SettleExpectedActivityWritebackSuggestion

Suggests a settlement instruction that settles the expected activity of the target item, using the  settlement confirmed by the origin item on the other side of the result. The request is upsertable as-is.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **result_pattern** | [WritebackResultPattern](WritebackResultPattern.md) | Required | *No description available.* |
| **portfolio_id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **settlement_instruction_request** | [SettlementInstructionRequest](SettlementInstructionRequest.md) | Required | *No description available.* |
| **writeback_type** | **str** | Required | Polymorphic discriminator, carrying the same values as writebackType on the matching ruleset&#39;s writeback configuration. Supported types: SettleExpectedActivity. Available values: SettleExpectedActivity. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.SettleExpectedActivityWritebackSuggestion import SettleExpectedActivityWritebackSuggestion

instance = SettleExpectedActivityWritebackSuggestion(
    result_pattern=WritebackResultPattern(...),  # required
    portfolio_id=ResourceId(...),  # required
    settlement_instruction_request=SettlementInstructionRequest(...),  # required
    writeback_type="..."  # required — Polymorphic discriminator, carrying the same values as writebackType on the matching ruleset&#39;s writeback configuration. Supported types: SettleExpectedActivity. Available values: SettleExpectedActivity.
)
```


## Related Models

- [WritebackResultPattern](WritebackResultPattern.md)
- [ResourceId](ResourceId.md)
- [SettlementInstructionRequest](SettlementInstructionRequest.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

