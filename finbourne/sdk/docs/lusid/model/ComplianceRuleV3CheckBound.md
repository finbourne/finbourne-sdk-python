# ComplianceRuleV3CheckBound

A single bound of a check: a hard limit that must hold, plus an optional soft limit that raises a  warning without failing the rule.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **hard** | [ComplianceRuleV3DecimalBound](ComplianceRuleV3DecimalBound.md) | Required | *No description available.* |
| **soft** | [ComplianceRuleV3DecimalBound](ComplianceRuleV3DecimalBound.md) | Optional | *No description available.* |
| **hard_property** | **str** | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.ComplianceRuleV3CheckBound import ComplianceRuleV3CheckBound

instance = ComplianceRuleV3CheckBound(
    hard=ComplianceRuleV3DecimalBound(...),  # required
    soft=ComplianceRuleV3DecimalBound(...),  # optional
    hard_property="..."  # optional
)
```


## Related Models

- [ComplianceRuleV3DecimalBound](ComplianceRuleV3DecimalBound.md)
- [ComplianceRuleV3DecimalBound](ComplianceRuleV3DecimalBound.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

