# UpdateCheckDefinitionRuleSet

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **rule_set_key** | **str** | Optional | The Key of the Rule Set. |
| **display_name** | **str** | Optional | The name of the Rule Set. |
| **description** | **str** | Optional | A description for the Rule Set. |
| **rule_set_filter** | **str** | Optional | A filter for the Rule Set to filter entity instances the rule set applies to. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.UpdateCheckDefinitionRuleSet import UpdateCheckDefinitionRuleSet

instance = UpdateCheckDefinitionRuleSet(
    rule_set_key="...",  # optional — The Key of the Rule Set.
    display_name="...",  # optional — The name of the Rule Set.
    description="...",  # optional — A description for the Rule Set.
    rule_set_filter="..."  # optional — A filter for the Rule Set to filter entity instances the rule set applies to.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

