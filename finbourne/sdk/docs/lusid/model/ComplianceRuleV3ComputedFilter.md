# ComplianceRuleV3ComputedFilter

An optional inner test selecting survivors before the measure: an optional grouping, the measure to  compute per group, and the check the group's measure must satisfy.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **group_by** | **List[str]** | Optional | *No description available.* |
| **measure** | [ComplianceRuleV3Measure](ComplianceRuleV3Measure.md) | Required | *No description available.* |
| **check** | [ComplianceRuleV3Check](ComplianceRuleV3Check.md) | Required | *No description available.* |
| **select_outside_bounds** | **bool** | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.ComplianceRuleV3ComputedFilter import ComplianceRuleV3ComputedFilter

instance = ComplianceRuleV3ComputedFilter(
    group_by=,  # optional
    measure=ComplianceRuleV3Measure(...),  # required
    check=ComplianceRuleV3Check(...),  # required
    select_outside_bounds=True  # optional
)
```

- [ComplianceRuleV3Measure](ComplianceRuleV3Measure.md)
- [ComplianceRuleV3Check](ComplianceRuleV3Check.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

