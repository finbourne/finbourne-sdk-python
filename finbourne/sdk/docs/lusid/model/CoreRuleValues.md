# CoreRuleValues

A core matching rule and the values that pin a rec result to its reconciled position. These values  contribute to the result id.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **rule_name** | **str** | Required | The name of the rule. |
| **left_value** | **str** | Optional | The left-side value. |
| **right_value** | **str** | Optional | The right-side value. |
| **applied_tolerance** | [ToleranceBase](ToleranceBase.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.CoreRuleValues import CoreRuleValues

instance = CoreRuleValues(
    rule_name="...",  # required — The name of the rule.
    left_value="...",  # optional — The left-side value.
    right_value="...",  # optional — The right-side value.
    applied_tolerance=ToleranceBase(...)  # optional
)
```

- [ToleranceBase](ToleranceBase.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

