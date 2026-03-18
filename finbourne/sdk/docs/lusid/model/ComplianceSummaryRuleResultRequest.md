# ComplianceSummaryRuleResultRequest

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **rule_id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **template_id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **variation** | **str** | Required | *No description available.* |
| **rule_status** | **str** | Required | *No description available.* |
| **affected_portfolios** | [List[ResourceId]](ResourceId.md) | Required | *No description available.* |
| **affected_orders** | [List[ResourceId]](ResourceId.md) | Required | *No description available.* |
| **parameters_used** | **Dict[str, Optional[str]]** | Required | *No description available.* |
| **rule_breakdown** | [List[ComplianceRuleBreakdownRequest]](ComplianceRuleBreakdownRequest.md) | Required | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.ComplianceSummaryRuleResultRequest import ComplianceSummaryRuleResultRequest

instance = ComplianceSummaryRuleResultRequest(
    rule_id=ResourceId(...),  # required
    template_id=ResourceId(...),  # required
    variation="...",  # required
    rule_status="...",  # required
    affected_portfolios=[],  # required
    affected_orders=[],  # required
    parameters_used=,  # required
    rule_breakdown=[]  # required
)
```


## Related Models

- [ResourceId](ResourceId.md)
- [ResourceId](ResourceId.md)
- [ResourceId](ResourceId.md)
- [ResourceId](ResourceId.md)
- [ComplianceRuleBreakdownRequest](ComplianceRuleBreakdownRequest.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

