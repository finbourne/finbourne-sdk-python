# ExportConditionalRule

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **operator** | [ExportRuleOperator](ExportRuleOperator.md) | Required | *No description available.* |
| **value** | **str** | Optional | *No description available.* |
| **value_to** | **str** | Optional | *No description available.* |
| **value_column** | **str** | Optional | *No description available.* |
| **value_to_column** | **str** | Optional | *No description available.* |
| **source_column** | **str** | Optional | *No description available.* |
| **effect** | [ExportRuleEffect](ExportRuleEffect.md) | Required | *No description available.* |
| **color** | [ExportRuleColor](ExportRuleColor.md) | Optional | *No description available.* |
| **hex** | **str** | Optional | *No description available.* |
| **text** | **str** | Optional | *No description available.* |
| **format** | **str** | Optional | *No description available.* |
| **include_aggregates** | **bool** | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.luminesce.models.ExportConditionalRule import ExportConditionalRule

instance = ExportConditionalRule(
    operator=ExportRuleOperator(...),  # required
    value="...",  # optional
    value_to="...",  # optional
    value_column="...",  # optional
    value_to_column="...",  # optional
    source_column="...",  # optional
    effect=ExportRuleEffect(...),  # required
    color=ExportRuleColor(...),  # optional
    hex="...",  # optional
    text="...",  # optional
    format="...",  # optional
    include_aggregates=True  # optional
)
```


## Related Models

- [ExportRuleOperator](ExportRuleOperator.md)
- [ExportRuleEffect](ExportRuleEffect.md)
- [ExportRuleColor](ExportRuleColor.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

