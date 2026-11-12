# ComplianceRuleV3DescribeResponse

A plain-English description of a V3 compliance rule. This is a minimal placeholder shape: the plain-English  generator is delivered separately, so the Lines property is currently empty and only the rule's identity  and subject are populated.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **id** | [ResourceId](ResourceId.md) | Optional | *No description available.* |
| **subject** | **str** | Optional | Available values: Holdings, Orders. |
| **lines** | **List[str]** | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.ComplianceRuleV3DescribeResponse import ComplianceRuleV3DescribeResponse

instance = ComplianceRuleV3DescribeResponse(
    id=ResourceId(...),  # optional
    subject="...",  # optional — Available values: Holdings, Orders.
    lines=  # optional
)
```


## Related Models

- [ResourceId](ResourceId.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

