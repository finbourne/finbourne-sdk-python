# ComplianceRuleV3Response

A V3 compliance rule as returned by the API: its identity and administrative fields, its full  definition, and its version.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **id** | [ResourceId](ResourceId.md) | Optional | *No description available.* |
| **name** | **str** | Optional | *No description available.* |
| **description** | **str** | Optional | *No description available.* |
| **active** | **bool** | Optional | *No description available.* |
| **subject** | **str** | Optional | Available values: Holdings, Orders. |
| **filter** | [ComplianceRuleV3FilterNode](ComplianceRuleV3FilterNode.md) | Optional | *No description available.* |
| **group_by** | **List[str]** | Optional | *No description available.* |
| **measure** | [ComplianceRuleV3Measure](ComplianceRuleV3Measure.md) | Optional | *No description available.* |
| **check** | [ComplianceRuleV3Check](ComplianceRuleV3Check.md) | Optional | *No description available.* |
| **computed_filter** | [ComplianceRuleV3ComputedFilter](ComplianceRuleV3ComputedFilter.md) | Optional | *No description available.* |
| **version** | [Version](Version.md) | Optional | *No description available.* |
| **plain_english** | **str** | Optional | *No description available.* |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.ComplianceRuleV3Response import ComplianceRuleV3Response

instance = ComplianceRuleV3Response(
    id=ResourceId(...),  # optional
    name="...",  # optional
    description="...",  # optional
    active=True,  # optional
    subject="...",  # optional — Available values: Holdings, Orders.
    filter=ComplianceRuleV3FilterNode(...),  # optional
    group_by=,  # optional
    measure=ComplianceRuleV3Measure(...),  # optional
    check=ComplianceRuleV3Check(...),  # optional
    computed_filter=ComplianceRuleV3ComputedFilter(...),  # optional
    version=Version(...),  # optional
    plain_english="...",  # optional
    links=[]  # optional
)
```


## Related Models

- [ResourceId](ResourceId.md)
- [ComplianceRuleV3FilterNode](ComplianceRuleV3FilterNode.md)
- [ComplianceRuleV3Measure](ComplianceRuleV3Measure.md)
- [ComplianceRuleV3Check](ComplianceRuleV3Check.md)
- [ComplianceRuleV3ComputedFilter](ComplianceRuleV3ComputedFilter.md)
- [Version](Version.md)
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

