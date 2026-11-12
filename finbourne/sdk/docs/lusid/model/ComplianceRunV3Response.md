# ComplianceRunV3Response

The outcome of a V3 compliance run: the result of each rule that was run.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **rule_results** | [List[ComplianceRuleV3RuleResult]](ComplianceRuleV3RuleResult.md) | Optional | *No description available.* |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.ComplianceRunV3Response import ComplianceRunV3Response

instance = ComplianceRunV3Response(
    rule_results=[],  # optional
    links=[]  # optional
)
```


## Related Models

- [ComplianceRuleV3RuleResult](ComplianceRuleV3RuleResult.md)
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

