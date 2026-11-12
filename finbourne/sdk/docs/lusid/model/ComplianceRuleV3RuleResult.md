# ComplianceRuleV3RuleResult

The aggregate result of one rule across every group it was evaluated over: the rule's overall status  (its worst group outcome) and the per-group results partitioned by outcome.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **rule_id** | [ResourceId](ResourceId.md) | Optional | *No description available.* |
| **status** | **str** | Optional | Available values: Passed, Failed, Warning, MissingData. |
| **results** | [List[ComplianceRuleV3GroupResult]](ComplianceRuleV3GroupResult.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.ComplianceRuleV3RuleResult import ComplianceRuleV3RuleResult

instance = ComplianceRuleV3RuleResult(
    rule_id=ResourceId(...),  # optional
    status="...",  # optional — Available values: Passed, Failed, Warning, MissingData.
    results=[]  # optional
)
```


## Related Models

- [ResourceId](ResourceId.md)
- [ComplianceRuleV3GroupResult](ComplianceRuleV3GroupResult.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

