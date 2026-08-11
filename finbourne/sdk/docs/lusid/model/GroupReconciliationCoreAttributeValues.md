# GroupReconciliationCoreAttributeValues

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **left_core_attributes** | [List[ComparisonAttributeValuePair]](ComparisonAttributeValuePair.md) | Required | Core attribute names and values for the left hand entity being reconciled. |
| **right_core_attributes** | [List[ComparisonAttributeValuePair]](ComparisonAttributeValuePair.md) | Required | Core attribute names and values for the right hand entity being reconciled. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.GroupReconciliationCoreAttributeValues import GroupReconciliationCoreAttributeValues

instance = GroupReconciliationCoreAttributeValues(
    left_core_attributes=[],  # required — Core attribute names and values for the left hand entity being reconciled.
    right_core_attributes=[]  # required — Core attribute names and values for the right hand entity being reconciled.
)
```


## Related Models

- [ComparisonAttributeValuePair](ComparisonAttributeValuePair.md) — used in `left_core_attributes`
- [ComparisonAttributeValuePair](ComparisonAttributeValuePair.md) — used in `right_core_attributes`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

