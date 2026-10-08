# WritebackSuggestion

A writeback suggested against a target-side item of a rec result. Polymorphic by WritebackType; each  supported type has a corresponding inherited class carrying the upsertable request it proposes.
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
from finbourne.sdk.services.lusid.models.WritebackSuggestion import WritebackSuggestion

instance = WritebackSuggestion(
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

