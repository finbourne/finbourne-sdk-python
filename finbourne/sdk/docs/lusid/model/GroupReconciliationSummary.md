# GroupReconciliationSummary

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **run_details** | [GroupReconciliationRunDetails](GroupReconciliationRunDetails.md) | Optional | *No description available.* |
| **group_reconciliation_definition_id** | [ResourceId](ResourceId.md) | Optional | *No description available.* |
| **reconciliation_type** | **str** | Required | The type of reconciliation to perform. \&quot;Holding\&quot; | \&quot;Transaction\&quot; | \&quot;Valuation\&quot; |
| **instance_id** | [GroupReconciliationInstanceId](GroupReconciliationInstanceId.md) | Required | *No description available.* |
| **dates_reconciled** | [GroupReconciliationDates](GroupReconciliationDates.md) | Required | *No description available.* |
| **reconciliation_run_as_at** | **datetime** | Required | The date and time the reconciliation was run |
| **count_comparison_results** | **int** | Required | The total number of comparison results with this InstanceId and ReconciliationType |
| **link_comparison_results** | [Link](Link.md) | Optional | *No description available.* |
| **result_types** | [GroupReconciliationResultTypes](GroupReconciliationResultTypes.md) | Optional | *No description available.* |
| **result_statuses** | [GroupReconciliationResultStatuses](GroupReconciliationResultStatuses.md) | Optional | *No description available.* |
| **review_statuses** | [GroupReconciliationReviewStatuses](GroupReconciliationReviewStatuses.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.GroupReconciliationSummary import GroupReconciliationSummary

instance = GroupReconciliationSummary(
    run_details=GroupReconciliationRunDetails(...),  # optional
    group_reconciliation_definition_id=ResourceId(...),  # optional
    reconciliation_type="...",  # required — The type of reconciliation to perform. \&quot;Holding\&quot; | \&quot;Transaction\&quot; | \&quot;Valuation\&quot;
    instance_id=GroupReconciliationInstanceId(...),  # required
    dates_reconciled=GroupReconciliationDates(...),  # required
    reconciliation_run_as_at=datetime.now(),  # required — The date and time the reconciliation was run
    count_comparison_results=0,  # required — The total number of comparison results with this InstanceId and ReconciliationType
    link_comparison_results=Link(...),  # optional
    result_types=GroupReconciliationResultTypes(...),  # optional
    result_statuses=GroupReconciliationResultStatuses(...),  # optional
    review_statuses=GroupReconciliationReviewStatuses(...)  # optional
)
```


## Related Models

- [GroupReconciliationRunDetails](GroupReconciliationRunDetails.md)
- [ResourceId](ResourceId.md)
- [GroupReconciliationInstanceId](GroupReconciliationInstanceId.md)
- [GroupReconciliationDates](GroupReconciliationDates.md)
- [Link](Link.md)
- [GroupReconciliationResultTypes](GroupReconciliationResultTypes.md)
- [GroupReconciliationResultStatuses](GroupReconciliationResultStatuses.md)
- [GroupReconciliationReviewStatuses](GroupReconciliationReviewStatuses.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

