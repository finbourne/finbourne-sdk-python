# PopulateResultProperty

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **property_key** | **str** | Required | The property the formula populates. Must be an existing, single-valued property in the RecResult domain, and may appear only once. |
| **formula** | **str** | Required | The formula gives the value of the property. The value must be of the property&#39;s type. A formula cannot populate an Int property, because its numbers are decimal. A null value means that the property has no value. The formula can read resultType, resultCardinality, resultLifecycle, exception.status, exception.closureType, exception.asAtClosed, exception.asAtClosureInvalidated, review.status, review.decision and review.decisionGroup.groupNumber. It reads rules by name as CoreRules[name] and AggregateRules[name]. Each rule has .leftValue, .rightValue and .appliedTolerance.toleranceType. A numeric aggregate rule also has .difference. You can compare CoreRules[name] with no side by eq, in or startswith. The comparison is true if either side matches. With neq, not in or not startswith, it is true if no side matches. Ordering comparisons must name the side. Comparisons ignore case and accents. |
| **overwrite_manual_edits_on_re_run** | **bool** | Optional | Whether a value edited since the property was last populated is replaced. Defaults to false, so manual edits are kept. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.PopulateResultProperty import PopulateResultProperty

instance = PopulateResultProperty(
    property_key="...",  # required — The property the formula populates. Must be an existing, single-valued property in the RecResult domain, and may appear only once.
    formula="...",  # required — The formula gives the value of the property. The value must be of the property&#39;s type. A formula cannot populate an Int property, because its numbers are decimal. A null value means that the property has no value. The formula can read resultType, resultCardinality, resultLifecycle, exception.status, exception.closureType, exception.asAtClosed, exception.asAtClosureInvalidated, review.status, review.decision and review.decisionGroup.groupNumber. It reads rules by name as CoreRules[name] and AggregateRules[name]. Each rule has .leftValue, .rightValue and .appliedTolerance.toleranceType. A numeric aggregate rule also has .difference. You can compare CoreRules[name] with no side by eq, in or startswith. The comparison is true if either side matches. With neq, not in or not startswith, it is true if no side matches. Ordering comparisons must name the side. Comparisons ignore case and accents.
    overwrite_manual_edits_on_re_run=True  # optional — Whether a value edited since the property was last populated is replaced. Defaults to false, so manual edits are kept.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

