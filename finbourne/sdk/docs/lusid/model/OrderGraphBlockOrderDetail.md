# OrderGraphBlockOrderDetail

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **compliance_state** | **str** | Required | The compliance state of this order. Available values: Pending, Failed, Passed, ManuallyApproved, PartiallyOverridden, Warning. |
| **approval_state** | **str** | Required | The approval state of this order. Available values: Pending, Rejected, Approved. |
| **portfolio_id** | [ResourceId](ResourceId.md) | Optional | *No description available.* |
| **portfolio_name** | **str** | Optional | The name of the order&#39;s referenced Portfolio. |
| **order_approval_task_id** | **str** | Optional | The task id associated with the approval state of the order. |
| **order_approval_task_definition_id** | [ResourceId](ResourceId.md) | Optional | *No description available.* |
| **non_passing_compliance_rule_results** | [List[ContributionToNonPassingRuleDetail]](ContributionToNonPassingRuleDetail.md) | Optional | The details of compliance rules in non-passing states. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.OrderGraphBlockOrderDetail import OrderGraphBlockOrderDetail

instance = OrderGraphBlockOrderDetail(
    id=ResourceId(...),  # required
    compliance_state="...",  # required — The compliance state of this order. Available values: Pending, Failed, Passed, ManuallyApproved, PartiallyOverridden, Warning.
    approval_state="...",  # required — The approval state of this order. Available values: Pending, Rejected, Approved.
    portfolio_id=ResourceId(...),  # optional
    portfolio_name="...",  # optional — The name of the order&#39;s referenced Portfolio.
    order_approval_task_id="...",  # optional — The task id associated with the approval state of the order.
    order_approval_task_definition_id=ResourceId(...),  # optional
    non_passing_compliance_rule_results=[]  # optional — The details of compliance rules in non-passing states.
)
```


## Related Models

- [ResourceId](ResourceId.md)
- [ResourceId](ResourceId.md)
- [ResourceId](ResourceId.md)
- [ContributionToNonPassingRuleDetail](ContributionToNonPassingRuleDetail.md) — used in `non_passing_compliance_rule_results`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

