# GroupReconciliationComparisonResult

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **reconciliation_type** | **str** | Required | The type of reconciliation to perform. \&quot;Holding\&quot; | \&quot;Transaction\&quot; | \&quot;Valuation\&quot; |
| **group_reconciliation_definition_id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **instance_id** | [GroupReconciliationInstanceId](GroupReconciliationInstanceId.md) | Required | *No description available.* |
| **comparison_result_id** | **str** | Required | Comparison result identifier, encoded value for core attribute results, aggregate attribute results, reconciliation type and run instanceId. |
| **reconciliation_run_as_at** | **datetime** | Required | The timestamp when the run occurred. |
| **result_type** | **str** | Required | Reconciliation run general result. \&quot;Break\&quot; | \&quot;Match\&quot; | \&quot;PartialMatch\&quot; | \&quot;NotFound |
| **result_status** | **str** | Required | Indicates how a particular result evolves from one run to the next. \&quot;New\&quot; | \&quot;Confirmed\&quot; | \&quot;Changed\&quot; |
| **review_status** | **str** | Required | Status of whether user has provided any input (comments, manual matches, break codes). \&quot;Pending\&quot; | \&quot;Reviewed\&quot; | \&quot;Matched\&quot; | \&quot;Invalid\&quot; |
| **dates_reconciled** | [GroupReconciliationDates](GroupReconciliationDates.md) | Required | *No description available.* |
| **core_attributes** | [GroupReconciliationCoreAttributeValues](GroupReconciliationCoreAttributeValues.md) | Required | *No description available.* |
| **aggregate_attributes** | [GroupReconciliationAggregateAttributeValues](GroupReconciliationAggregateAttributeValues.md) | Required | *No description available.* |
| **user_review** | [GroupReconciliationUserReview](GroupReconciliationUserReview.md) | Optional | *No description available.* |
| **href** | **str** | Optional | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. |
| **version** | [Version](Version.md) | Optional | *No description available.* |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.GroupReconciliationComparisonResult import GroupReconciliationComparisonResult

instance = GroupReconciliationComparisonResult(
    id=ResourceId(...),  # required
    reconciliation_type="...",  # required — The type of reconciliation to perform. \&quot;Holding\&quot; | \&quot;Transaction\&quot; | \&quot;Valuation\&quot;
    group_reconciliation_definition_id=ResourceId(...),  # required
    instance_id=GroupReconciliationInstanceId(...),  # required
    comparison_result_id="...",  # required — Comparison result identifier, encoded value for core attribute results, aggregate attribute results, reconciliation type and run instanceId.
    reconciliation_run_as_at=datetime.now(),  # required — The timestamp when the run occurred.
    result_type="...",  # required — Reconciliation run general result. \&quot;Break\&quot; | \&quot;Match\&quot; | \&quot;PartialMatch\&quot; | \&quot;NotFound
    result_status="...",  # required — Indicates how a particular result evolves from one run to the next. \&quot;New\&quot; | \&quot;Confirmed\&quot; | \&quot;Changed\&quot;
    review_status="...",  # required — Status of whether user has provided any input (comments, manual matches, break codes). \&quot;Pending\&quot; | \&quot;Reviewed\&quot; | \&quot;Matched\&quot; | \&quot;Invalid\&quot;
    dates_reconciled=GroupReconciliationDates(...),  # required
    core_attributes=GroupReconciliationCoreAttributeValues(...),  # required
    aggregate_attributes=GroupReconciliationAggregateAttributeValues(...),  # required
    user_review=GroupReconciliationUserReview(...),  # optional
    href="...",  # optional — The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.
    version=Version(...),  # optional
    links=[]  # optional
)
```


## Related Models

- [ResourceId](ResourceId.md)
- [ResourceId](ResourceId.md)
- [GroupReconciliationInstanceId](GroupReconciliationInstanceId.md)
- [GroupReconciliationDates](GroupReconciliationDates.md)
- [GroupReconciliationCoreAttributeValues](GroupReconciliationCoreAttributeValues.md)
- [GroupReconciliationAggregateAttributeValues](GroupReconciliationAggregateAttributeValues.md)
- [GroupReconciliationUserReview](GroupReconciliationUserReview.md)
- [Version](Version.md)
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

