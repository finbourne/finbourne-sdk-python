# ComplianceRuleV3Measure

How a rule reduces its filtered (and optionally grouped) subject rows to the single number a check is  applied to: a metric field, the aggregate combining its values, and what it is expressed relative to.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **metric** | **str** | Optional | *No description available.* |
| **aggregate** | **str** | Required | Available values: Sum, Min, Max, Average, Count, CountDistinct, WeightedSum, SumAbsolute. |
| **denominator** | **str** | Optional | Available values: None, PortfolioValue, GrossValue, NetValue, FilteredSubsetTotal, GroupNav, GroupGrossExposure, GroupFilteredSubsetTotal. |
| **denominator_metric** | **str** | Optional | *No description available.* |
| **weight_metric** | **str** | Optional | *No description available.* |
| **denominator_property** | **str** | Optional | *No description available.* |
| **filter** | [ComplianceRuleV3FilterNode](ComplianceRuleV3FilterNode.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.ComplianceRuleV3Measure import ComplianceRuleV3Measure

instance = ComplianceRuleV3Measure(
    metric="...",  # optional
    aggregate="...",  # required — Available values: Sum, Min, Max, Average, Count, CountDistinct, WeightedSum, SumAbsolute.
    denominator="...",  # optional — Available values: None, PortfolioValue, GrossValue, NetValue, FilteredSubsetTotal, GroupNav, GroupGrossExposure, GroupFilteredSubsetTotal.
    denominator_metric="...",  # optional
    weight_metric="...",  # optional
    denominator_property="...",  # optional
    filter=ComplianceRuleV3FilterNode(...)  # optional
)
```

- [ComplianceRuleV3FilterNode](ComplianceRuleV3FilterNode.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

