# ComplianceRuleV3Check

The limits a measure's result is checked against: an optional upper bound, an optional lower bound, and  the unit both are expressed in.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **unit** | **str** | Required | Available values: Absolute, Percentage. |
| **upper** | [ComplianceRuleV3CheckBound](ComplianceRuleV3CheckBound.md) | Optional | *No description available.* |
| **lower** | [ComplianceRuleV3CheckBound](ComplianceRuleV3CheckBound.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.ComplianceRuleV3Check import ComplianceRuleV3Check

instance = ComplianceRuleV3Check(
    unit="...",  # required — Available values: Absolute, Percentage.
    upper=ComplianceRuleV3CheckBound(...),  # optional
    lower=ComplianceRuleV3CheckBound(...)  # optional
)
```

- [ComplianceRuleV3CheckBound](ComplianceRuleV3CheckBound.md)
- [ComplianceRuleV3CheckBound](ComplianceRuleV3CheckBound.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

