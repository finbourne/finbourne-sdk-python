# CreateCheckDefinitionRequest

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **display_name** | **str** | Required | The name of the Check Definition. |
| **description** | **str** | Required | A description for the Check Definition. |
| **dataset_schema** | [CheckDefinitionDatasetSchema](CheckDefinitionDatasetSchema.md) | Optional | *No description available.* |
| **rule_sets** | [List[UpdateCheckDefinitionRuleSet]](UpdateCheckDefinitionRuleSet.md) | Required | A collection of rule sets for the Check Definition. |
| **properties** | [Dict[str, ModelProperty]](ModelProperty.md) | Optional | A set of properties for the Check Definition. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.CreateCheckDefinitionRequest import CreateCheckDefinitionRequest

instance = CreateCheckDefinitionRequest(
    id=ResourceId(...),  # required
    display_name="...",  # required — The name of the Check Definition.
    description="...",  # required — A description for the Check Definition.
    dataset_schema=CheckDefinitionDatasetSchema(...),  # optional
    rule_sets=[],  # required — A collection of rule sets for the Check Definition.
    properties=ModelProperty(...)  # optional — A set of properties for the Check Definition.
)
```


## Related Models

- [ResourceId](ResourceId.md)
- [CheckDefinitionDatasetSchema](CheckDefinitionDatasetSchema.md)
- [UpdateCheckDefinitionRuleSet](UpdateCheckDefinitionRuleSet.md) — used in `rule_sets`
- [ModelProperty](ModelProperty.md) — used in `properties`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

