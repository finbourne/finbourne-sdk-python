# CheckDefinitionRuleSet

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **rule_set_key** | **str** | Optional | The Key of the Rule Set. |
| **display_name** | **str** | Optional | The name of the Rule Set. |
| **description** | **str** | Optional | A description for the Rule Set. |
| **rule_set_filter** | **str** | Optional | A filter for the Rule Set to filter entity instances the rule set applies to. |
| **rules** | [List[CheckDefinitionRule]](CheckDefinitionRule.md) | Optional | A collection of rules for the Rule Set. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.CheckDefinitionRuleSet import CheckDefinitionRuleSet

instance = CheckDefinitionRuleSet(
    rule_set_key="...",  # optional — The Key of the Rule Set.
    display_name="...",  # optional — The name of the Rule Set.
    description="...",  # optional — A description for the Rule Set.
    rule_set_filter="...",  # optional — A filter for the Rule Set to filter entity instances the rule set applies to.
    rules=[]  # optional — A collection of rules for the Rule Set.
)
```

- [CheckDefinitionRule](CheckDefinitionRule.md) — used in `rules`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

