# GroupReconciliationComparisonRuleTolerance

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **type** | **str** | Required | The type of tolerance to allow. \&quot;Relative\&quot; | \&quot;Absolute\&quot; |
| **value** | **float** | Required | The decimal value of how much tolerance to allow when comparing in relative (i.e percentage) or absolute terms depending on the ToleranceType specified |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.GroupReconciliationComparisonRuleTolerance import GroupReconciliationComparisonRuleTolerance

instance = GroupReconciliationComparisonRuleTolerance(
    type="...",  # required — The type of tolerance to allow. \&quot;Relative\&quot; | \&quot;Absolute\&quot;
    value=0.0  # required — The decimal value of how much tolerance to allow when comparing in relative (i.e percentage) or absolute terms depending on the ToleranceType specified
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

