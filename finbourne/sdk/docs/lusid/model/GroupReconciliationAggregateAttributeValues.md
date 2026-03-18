# GroupReconciliationAggregateAttributeValues

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **left_aggregate_attributes** | [List[ComparisonAttributeValuePair]](ComparisonAttributeValuePair.md) | Required | Aggregate attribute names and values for the left hand entity being reconciled. |
| **right_aggregate_attributes** | [List[ComparisonAttributeValuePair]](ComparisonAttributeValuePair.md) | Required | Aggregate attribute names and values for the right hand entity being reconciled. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.GroupReconciliationAggregateAttributeValues import GroupReconciliationAggregateAttributeValues

instance = GroupReconciliationAggregateAttributeValues(
    left_aggregate_attributes=[],  # required — Aggregate attribute names and values for the left hand entity being reconciled.
    right_aggregate_attributes=[]  # required — Aggregate attribute names and values for the right hand entity being reconciled.
)
```


## Related Models

- [ComparisonAttributeValuePair](ComparisonAttributeValuePair.md) — used in `left_aggregate_attributes`
- [ComparisonAttributeValuePair](ComparisonAttributeValuePair.md) — used in `right_aggregate_attributes`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

