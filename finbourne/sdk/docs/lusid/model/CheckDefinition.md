# CheckDefinition

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **display_name** | **str** | Optional | The name of the Check Definition. |
| **description** | **str** | Optional | A description for the Check Definition. |
| **dataset_schema** | [CheckDefinitionDatasetSchema](CheckDefinitionDatasetSchema.md) | Optional | *No description available.* |
| **rule_sets** | [List[CheckDefinitionRuleSet]](CheckDefinitionRuleSet.md) | Optional | A collection of rule sets for the Check Definition. |
| **href** | **str** | Optional | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. |
| **version** | [Version](Version.md) | Optional | *No description available.* |
| **properties** | [Dict[str, ModelProperty]](ModelProperty.md) | Optional | A set of properties for the Check Definition. |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.CheckDefinition import CheckDefinition

instance = CheckDefinition(
    id=ResourceId(...),  # required
    display_name="...",  # optional — The name of the Check Definition.
    description="...",  # optional — A description for the Check Definition.
    dataset_schema=CheckDefinitionDatasetSchema(...),  # optional
    rule_sets=[],  # optional — A collection of rule sets for the Check Definition.
    href="...",  # optional — The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.
    version=Version(...),  # optional
    properties=ModelProperty(...),  # optional — A set of properties for the Check Definition.
    links=[]  # optional
)
```


## Related Models

- [ResourceId](ResourceId.md)
- [CheckDefinitionDatasetSchema](CheckDefinitionDatasetSchema.md)
- [CheckDefinitionRuleSet](CheckDefinitionRuleSet.md) — used in `rule_sets`
- [Version](Version.md)
- [ModelProperty](ModelProperty.md) — used in `properties`
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

