# PolicyResponse

Response object from the policy API
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **id** | [PolicyId](PolicyId.md) | Optional | *No description available.* |
| **description** | **str** | Optional | Description of what the policy is entitling |
| **applications** | **List[str]** | Optional | Applications to which the policy applies |
| **grant** | [Grant](Grant.md) | Optional | *No description available.* |
| **selectors** | [List[SelectorDefinition]](SelectorDefinition.md) | Optional | Selectors that this policy will be applied to |
| **var_for** | [List[ForSpec]](ForSpec.md) | Optional | \&quot;For Specification\&quot; for when the policy is to be applied |
| **var_if** | [List[IfExpression]](IfExpression.md) | Optional | \&quot;If Specification\&quot; for when the policy is to be applied |
| **when** | [WhenSpec](WhenSpec.md) | Optional | *No description available.* |
| **how** | [HowSpec](HowSpec.md) | Optional | *No description available.* |
| **template_metadata** | [TemplateMetadata](TemplateMetadata.md) | Optional | *No description available.* |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.access.models.PolicyResponse import PolicyResponse

instance = PolicyResponse(
    id=PolicyId(...),  # optional
    description="...",  # optional — Description of what the policy is entitling
    applications=,  # optional — Applications to which the policy applies
    grant=Grant(...),  # optional
    selectors=[],  # optional — Selectors that this policy will be applied to
    var_for=[],  # optional — \&quot;For Specification\&quot; for when the policy is to be applied
    var_if=[],  # optional — \&quot;If Specification\&quot; for when the policy is to be applied
    when=WhenSpec(...),  # optional
    how=HowSpec(...),  # optional
    template_metadata=TemplateMetadata(...),  # optional
    links=[]  # optional
)
```


## Related Models

- [PolicyId](PolicyId.md)
- [Grant](Grant.md)
- [SelectorDefinition](SelectorDefinition.md) — used in `selectors`
- [ForSpec](ForSpec.md) — used in `var_for`
- [IfExpression](IfExpression.md) — used in `var_if`
- [WhenSpec](WhenSpec.md)
- [HowSpec](HowSpec.md)
- [TemplateMetadata](TemplateMetadata.md)
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

