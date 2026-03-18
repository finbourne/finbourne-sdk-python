# CheckDefinitionRule

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **rule_key** | **str** | Optional | The key of the Rule. |
| **display_name** | **str** | Optional | The name of the Rule. |
| **description** | **str** | Optional | A description for the Rule. |
| **rule_formula** | **str** | Optional | The formula for the rule. |
| **severity** | **int** | Optional | Severity of the rule if formaula is not satisfied. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.CheckDefinitionRule import CheckDefinitionRule

instance = CheckDefinitionRule(
    rule_key="...",  # optional — The key of the Rule.
    display_name="...",  # optional — The name of the Rule.
    description="...",  # optional — A description for the Rule.
    rule_formula="...",  # optional — The formula for the rule.
    severity=0  # optional — Severity of the rule if formaula is not satisfied.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

