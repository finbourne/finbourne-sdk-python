# ComplianceRuleResultV2

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **run_id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **instigated_at** | **datetime** | Required | *No description available.* |
| **completed_at** | **datetime** | Required | *No description available.* |
| **schedule** | **str** | Required | *No description available.* |
| **rule_result** | [ComplianceSummaryRuleResult](ComplianceSummaryRuleResult.md) | Required | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.ComplianceRuleResultV2 import ComplianceRuleResultV2

instance = ComplianceRuleResultV2(
    run_id=ResourceId(...),  # required
    instigated_at=datetime.now(),  # required
    completed_at=datetime.now(),  # required
    schedule="...",  # required
    rule_result=ComplianceSummaryRuleResult(...)  # required
)
```


## Related Models

- [ResourceId](ResourceId.md)
- [ComplianceSummaryRuleResult](ComplianceSummaryRuleResult.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

