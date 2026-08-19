# AggregateMatchingRule

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **rule_name** | **str** | Required | The reference name of the rule. |
| **left_formula** | **str** | Required | Derivation formula evaluated against the left side of the reconciliation. |
| **left_operation** | **str** | Required | Group-level operation applied to the left side&#39;s per-item values during reconciliation, e.g. Sum, Average, Count. Available values: Sum, Proportion, Average, Count, Min, Max, Value, SumOfPositiveValues, SumOfNegativeValues, SumOfAbsoluteValues, ProportionOfAbsoluteValues, SumCumulativeInAdvance, SumCumulativeInArrears. |
| **right_formula** | **str** | Required | Derivation formula evaluated against the right side of the reconciliation. |
| **right_operation** | **str** | Required | Group-level operation applied to the right side&#39;s per-item values during reconciliation, e.g. Sum, Average, Count. Available values: Sum, Proportion, Average, Count, Min, Max, Value, SumOfPositiveValues, SumOfNegativeValues, SumOfAbsoluteValues, ProportionOfAbsoluteValues, SumCumulativeInAdvance, SumCumulativeInArrears. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.AggregateMatchingRule import AggregateMatchingRule

instance = AggregateMatchingRule(
    rule_name="...",  # required — The reference name of the rule.
    left_formula="...",  # required — Derivation formula evaluated against the left side of the reconciliation.
    left_operation="...",  # required — Group-level operation applied to the left side&#39;s per-item values during reconciliation, e.g. Sum, Average, Count. Available values: Sum, Proportion, Average, Count, Min, Max, Value, SumOfPositiveValues, SumOfNegativeValues, SumOfAbsoluteValues, ProportionOfAbsoluteValues, SumCumulativeInAdvance, SumCumulativeInArrears.
    right_formula="...",  # required — Derivation formula evaluated against the right side of the reconciliation.
    right_operation="..."  # required — Group-level operation applied to the right side&#39;s per-item values during reconciliation, e.g. Sum, Average, Count. Available values: Sum, Proportion, Average, Count, Min, Max, Value, SumOfPositiveValues, SumOfNegativeValues, SumOfAbsoluteValues, ProportionOfAbsoluteValues, SumCumulativeInAdvance, SumCumulativeInArrears.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

