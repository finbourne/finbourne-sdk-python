# StagingRule

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **rule_id** | **str** | Required | The ID of the staging rule. |
| **description** | **str** | Optional | A description for the staging rule. |
| **status** | **str** | Required | Whether the rule is &#39;Active&#39; or &#39;Inactive&#39;. |
| **match_criteria** | [StagingRuleMatchCriteria](StagingRuleMatchCriteria.md) | Required | *No description available.* |
| **approval_criteria** | [StagingRuleApprovalCriteria](StagingRuleApprovalCriteria.md) | Required | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.StagingRule import StagingRule

instance = StagingRule(
    rule_id="...",  # required — The ID of the staging rule.
    description="...",  # optional — A description for the staging rule.
    status="...",  # required — Whether the rule is &#39;Active&#39; or &#39;Inactive&#39;.
    match_criteria=StagingRuleMatchCriteria(...),  # required
    approval_criteria=StagingRuleApprovalCriteria(...)  # required
)
```

- [StagingRuleMatchCriteria](StagingRuleMatchCriteria.md)
- [StagingRuleApprovalCriteria](StagingRuleApprovalCriteria.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

