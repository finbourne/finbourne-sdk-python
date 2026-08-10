# PolicyUpdateRequest

Update policy request
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **description** | **str** | Optional | Description of what the policy will be used for |
| **applications** | **List[str]** | Optional | Applications this policy is used with |
| **grant** | [../model/Grant](Grant.md) | Required | *No description available.* |
| **selectors** | [../model/List[SelectorDefinition]](SelectorDefinition.md) | Required | Selectors that identify what resources this policy qualifies for |
| **var_for** | [../model/List[ForSpec]](ForSpec.md) | Optional | \&quot;For Specification\&quot; for when the policy is to be applied |
| **var_if** | [../model/List[IfExpression]](IfExpression.md) | Optional | \&quot;If Specification\&quot; for when the policy is to be applied |
| **when** | [../model/WhenSpec](WhenSpec.md) | Required | *No description available.* |
| **how** | [../model/HowSpec](HowSpec.md) | Optional | *No description available.* |
| **template_metadata** | [../model/TemplateMetadata](TemplateMetadata.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.access.models.PolicyUpdateRequest import PolicyUpdateRequest

instance = PolicyUpdateRequest(
    description="...",  # optional — Description of what the policy will be used for
    applications=,  # optional — Applications this policy is used with
    grant=Grant(...),  # required
    selectors=[],  # required — Selectors that identify what resources this policy qualifies for
    var_for=[],  # optional — \&quot;For Specification\&quot; for when the policy is to be applied
    var_if=[],  # optional — \&quot;If Specification\&quot; for when the policy is to be applied
    when=WhenSpec(...),  # required
    how=HowSpec(...),  # optional
    template_metadata=TemplateMetadata(...)  # optional
)
```

- [Grant](Grant.md)
- [SelectorDefinition](SelectorDefinition.md) — used in `selectors`
- [ForSpec](ForSpec.md) — used in `var_for`
- [IfExpression](IfExpression.md) — used in `var_if`
- [WhenSpec](WhenSpec.md)
- [HowSpec](HowSpec.md)
- [TemplateMetadata](TemplateMetadata.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

