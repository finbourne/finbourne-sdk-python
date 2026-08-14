# AggregateRuleValues

An aggregate matching rule and its values. The difference is the measured magnitude compared against  any applied tolerance.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **rule_name** | **str** | Required | The name of the rule. |
| **left_value** | **str** | Optional | The left-side value. |
| **right_value** | **str** | Optional | The right-side value. |
| **difference** | **str** | Required | The measured magnitude of the difference, ToString(ABS(leftValue - rightValue)). |
| **applied_tolerance** | [AggregateToleranceBase](AggregateToleranceBase.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.AggregateRuleValues import AggregateRuleValues

instance = AggregateRuleValues(
    rule_name="...",  # required — The name of the rule.
    left_value="...",  # optional — The left-side value.
    right_value="...",  # optional — The right-side value.
    difference="...",  # required — The measured magnitude of the difference, ToString(ABS(leftValue - rightValue)).
    applied_tolerance=AggregateToleranceBase(...)  # optional
)
```

- [AggregateToleranceBase](AggregateToleranceBase.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

