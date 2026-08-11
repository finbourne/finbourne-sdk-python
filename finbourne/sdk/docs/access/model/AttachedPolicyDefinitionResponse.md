# AttachedPolicyDefinitionResponse

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **source_role** | [RoleId](RoleId.md) | Optional | *No description available.* |
| **role_hierarchy_index** | **int** | Optional | *No description available.* |
| **description** | **str** | Optional | *No description available.* |
| **applications** | **List[str]** | Optional | *No description available.* |
| **policy_type** | [PolicyType](PolicyType.md) | Optional | *No description available.* |
| **id** | [PolicyId](PolicyId.md) | Optional | *No description available.* |
| **grant** | [Grant](Grant.md) | Optional | *No description available.* |
| **selectors** | [List[SelectorDefinition]](SelectorDefinition.md) | Optional | *No description available.* |
| **var_for** | [List[ForSpec]](ForSpec.md) | Optional | *No description available.* |
| **var_if** | [List[IfExpression]](IfExpression.md) | Optional | *No description available.* |
| **when** | [WhenSpec](WhenSpec.md) | Optional | *No description available.* |
| **how** | [HowSpec](HowSpec.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.access.models.AttachedPolicyDefinitionResponse import AttachedPolicyDefinitionResponse

instance = AttachedPolicyDefinitionResponse(
    source_role=RoleId(...),  # optional
    role_hierarchy_index=0,  # optional
    description="...",  # optional
    applications=,  # optional
    policy_type=PolicyType(...),  # optional
    id=PolicyId(...),  # optional
    grant=Grant(...),  # optional
    selectors=[],  # optional
    var_for=[],  # optional
    var_if=[],  # optional
    when=WhenSpec(...),  # optional
    how=HowSpec(...)  # optional
)
```


## Related Models

- [RoleId](RoleId.md)
- [PolicyType](PolicyType.md)
- [PolicyId](PolicyId.md)
- [Grant](Grant.md)
- [SelectorDefinition](SelectorDefinition.md)
- [ForSpec](ForSpec.md)
- [IfExpression](IfExpression.md)
- [WhenSpec](WhenSpec.md)
- [HowSpec](HowSpec.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

