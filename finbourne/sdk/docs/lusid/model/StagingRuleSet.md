# StagingRuleSet

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **entity_type** | **str** | Required | The entity type the staging rule set applies to. |
| **staging_rule_set_id** | **str** | Required | System generated unique id for the staging rule set. |
| **display_name** | **str** | Required | The name of the staging rule set. |
| **description** | **str** | Optional | A description for the staging rule set. |
| **rules** | [List[StagingRule]](StagingRule.md) | Required | The list of staging rules that apply to a specific entity type. |
| **href** | **str** | Optional | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. |
| **version** | [Version](Version.md) | Optional | *No description available.* |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.StagingRuleSet import StagingRuleSet

instance = StagingRuleSet(
    entity_type="...",  # required — The entity type the staging rule set applies to.
    staging_rule_set_id="...",  # required — System generated unique id for the staging rule set.
    display_name="...",  # required — The name of the staging rule set.
    description="...",  # optional — A description for the staging rule set.
    rules=[],  # required — The list of staging rules that apply to a specific entity type.
    href="...",  # optional — The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.
    version=Version(...),  # optional
    links=[]  # optional
)
```

- [StagingRule](StagingRule.md) — used in `rules`
- [Version](Version.md)
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

