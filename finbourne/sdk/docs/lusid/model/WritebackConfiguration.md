# WritebackConfiguration

Base class for the configuration of a writeback a matching ruleset generates suggestions for against its  results. Polymorphic by WritebackType; each supported type has a corresponding inherited class.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **mandatory_rule_names** | [SettleExpectedActivityRuleNames](SettleExpectedActivityRuleNames.md) | Required | *No description available.* |
| **result_patterns** | [List[WritebackResultPattern]](WritebackResultPattern.md) | Required | The combinations of units difference and result cardinality for which writeback is suggested. A combination that is not present never produces a suggestion. Each combination may appear once, and the collection is returned in a canonical order regardless of the order supplied. |
| **writeback_type** | **str** | Required | Polymorphic discriminator, naming the change the writeback makes to LUSID. Supported types: SettleExpectedActivity, which is only valid when recType is SettlementActivity. Available values: SettleExpectedActivity. |
| **target_side** | **str** | Required | The side the writeback changes, the other being the source of truth. As the writeback changes LUSID, this side must draw on a native LUSID dataset rather than relational data. Available values: Left, Right. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.WritebackConfiguration import WritebackConfiguration

instance = WritebackConfiguration(
    mandatory_rule_names=SettleExpectedActivityRuleNames(...),  # required
    result_patterns=[],  # required — The combinations of units difference and result cardinality for which writeback is suggested. A combination that is not present never produces a suggestion. Each combination may appear once, and the collection is returned in a canonical order regardless of the order supplied.
    writeback_type="...",  # required — Polymorphic discriminator, naming the change the writeback makes to LUSID. Supported types: SettleExpectedActivity, which is only valid when recType is SettlementActivity. Available values: SettleExpectedActivity.
    target_side="..."  # required — The side the writeback changes, the other being the source of truth. As the writeback changes LUSID, this side must draw on a native LUSID dataset rather than relational data. Available values: Left, Right.
)
```


## Related Models

- [SettleExpectedActivityRuleNames](SettleExpectedActivityRuleNames.md)
- [WritebackResultPattern](WritebackResultPattern.md) — used in `result_patterns`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

