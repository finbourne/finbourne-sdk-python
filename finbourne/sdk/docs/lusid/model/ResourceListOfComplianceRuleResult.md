# ResourceListOfComplianceRuleResult

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **values** | [List[ComplianceRuleResult]](ComplianceRuleResult.md) | Required | *No description available.* |
| **href** | **str** | Optional | *No description available.* |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |
| **next_page** | **str** | Optional | *No description available.* |
| **previous_page** | **str** | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.ResourceListOfComplianceRuleResult import ResourceListOfComplianceRuleResult

instance = ResourceListOfComplianceRuleResult(
    values=[],  # required
    href="...",  # optional
    links=[],  # optional
    next_page="...",  # optional
    previous_page="..."  # optional
)
```


## Related Models

- [ComplianceRuleResult](ComplianceRuleResult.md)
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

