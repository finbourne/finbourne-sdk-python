# CreateStagingRuleSetRequest

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **display_name** | **str** | Required | The name of the staging rule set. |
| **description** | **str** | Optional | A description for the staging rule set. |
| **rules** | [List[StagingRule]](StagingRule.md) | Required | The list of staging rules that apply to a specific entity type. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.CreateStagingRuleSetRequest import CreateStagingRuleSetRequest

instance = CreateStagingRuleSetRequest(
    display_name="...",  # required — The name of the staging rule set.
    description="...",  # optional — A description for the staging rule set.
    rules=[]  # required — The list of staging rules that apply to a specific entity type.
)
```

- [StagingRule](StagingRule.md) — used in `rules`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

