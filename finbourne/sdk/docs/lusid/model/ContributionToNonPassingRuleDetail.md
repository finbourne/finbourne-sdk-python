# ContributionToNonPassingRuleDetail

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **rule_id** | [ResourceId](ResourceId.md) | Optional | *No description available.* |
| **rule_status** | **str** | Optional | The status of the non-passing rule. |
| **breach_task_ids** | **List[str]** | Optional | The task ids associated with the compliance breach for this order&#39;s groups (if failing). |
| **likely_responsible_for_status** | **bool** | Optional | Whether this order is deemed as a likely contributor to the non-passing rule for this group. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.ContributionToNonPassingRuleDetail import ContributionToNonPassingRuleDetail

instance = ContributionToNonPassingRuleDetail(
    rule_id=ResourceId(...),  # optional
    rule_status="...",  # optional — The status of the non-passing rule.
    breach_task_ids=,  # optional — The task ids associated with the compliance breach for this order&#39;s groups (if failing).
    likely_responsible_for_status=True  # optional — Whether this order is deemed as a likely contributor to the non-passing rule for this group.
)
```


## Related Models

- [ResourceId](ResourceId.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

