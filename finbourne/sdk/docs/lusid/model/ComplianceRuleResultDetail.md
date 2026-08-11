# ComplianceRuleResultDetail

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **rule_id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **affected_portfolios_details** | [List[ComplianceRuleResultPortfolioDetail]](ComplianceRuleResultPortfolioDetail.md) | Required | *No description available.* |
| **affected_orders** | [List[ResourceId]](ResourceId.md) | Required | *No description available.* |
| **template_id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **template_description** | **str** | Required | *No description available.* |
| **template_variation** | **str** | Required | *No description available.* |
| **status** | **str** | Required | *No description available.* |
| **rule_name** | **str** | Required | *No description available.* |
| **rule_description** | **str** | Required | *No description available.* |
| **outcome** | **str** | Required | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.ComplianceRuleResultDetail import ComplianceRuleResultDetail

instance = ComplianceRuleResultDetail(
    rule_id=ResourceId(...),  # required
    affected_portfolios_details=[],  # required
    affected_orders=[],  # required
    template_id=ResourceId(...),  # required
    template_description="...",  # required
    template_variation="...",  # required
    status="...",  # required
    rule_name="...",  # required
    rule_description="...",  # required
    outcome="..."  # required
)
```


## Related Models

- [ResourceId](ResourceId.md)
- [ComplianceRuleResultPortfolioDetail](ComplianceRuleResultPortfolioDetail.md)
- [ResourceId](ResourceId.md)
- [ResourceId](ResourceId.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

