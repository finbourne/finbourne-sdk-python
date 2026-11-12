# UpsertComplianceRuleV3Request

A request to create or update a V3 compliance rule. A V3 rule's own record fully describes what it  checks: the subject it runs over, the filter selecting rows, the grouping and measure reducing them to a  number, and the check that number must satisfy. Shares no type with ComplianceV1/V2.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **name** | **str** | Optional | *No description available.* |
| **description** | **str** | Optional | *No description available.* |
| **active** | **bool** | Required | *No description available.* |
| **subject** | **str** | Required | Available values: Holdings, Orders. |
| **filter** | [ComplianceRuleV3FilterNode](ComplianceRuleV3FilterNode.md) | Optional | *No description available.* |
| **group_by** | **List[str]** | Optional | *No description available.* |
| **measure** | [ComplianceRuleV3Measure](ComplianceRuleV3Measure.md) | Required | *No description available.* |
| **check** | [ComplianceRuleV3Check](ComplianceRuleV3Check.md) | Required | *No description available.* |
| **computed_filter** | [ComplianceRuleV3ComputedFilter](ComplianceRuleV3ComputedFilter.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.UpsertComplianceRuleV3Request import UpsertComplianceRuleV3Request

instance = UpsertComplianceRuleV3Request(
    id=ResourceId(...),  # required
    name="...",  # optional
    description="...",  # optional
    active=True,  # required
    subject="...",  # required — Available values: Holdings, Orders.
    filter=ComplianceRuleV3FilterNode(...),  # optional
    group_by=,  # optional
    measure=ComplianceRuleV3Measure(...),  # required
    check=ComplianceRuleV3Check(...),  # required
    computed_filter=ComplianceRuleV3ComputedFilter(...)  # optional
)
```


## Related Models

- [ResourceId](ResourceId.md)
- [ComplianceRuleV3FilterNode](ComplianceRuleV3FilterNode.md)
- [ComplianceRuleV3Measure](ComplianceRuleV3Measure.md)
- [ComplianceRuleV3Check](ComplianceRuleV3Check.md)
- [ComplianceRuleV3ComputedFilter](ComplianceRuleV3ComputedFilter.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

