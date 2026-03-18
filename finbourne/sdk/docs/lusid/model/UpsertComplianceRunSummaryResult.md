# UpsertComplianceRunSummaryResult

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **run_id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **instigated_at** | **datetime** | Required | *No description available.* |
| **completed_at** | **datetime** | Required | *No description available.* |
| **schedule** | **str** | Required | *No description available.* |
| **results** | [List[ComplianceSummaryRuleResult]](ComplianceSummaryRuleResult.md) | Required | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.UpsertComplianceRunSummaryResult import UpsertComplianceRunSummaryResult

instance = UpsertComplianceRunSummaryResult(
    run_id=ResourceId(...),  # required
    instigated_at=datetime.now(),  # required
    completed_at=datetime.now(),  # required
    schedule="...",  # required
    results=[]  # required
)
```


## Related Models

- [ResourceId](ResourceId.md)
- [ComplianceSummaryRuleResult](ComplianceSummaryRuleResult.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

