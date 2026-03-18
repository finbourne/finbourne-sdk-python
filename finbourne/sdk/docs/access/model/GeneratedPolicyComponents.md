# GeneratedPolicyComponents

Response object for policy generated from template
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **applications** | **List[str]** | Optional | Applications to which the policy applies |
| **template_metadata** | [TemplateMetadata](TemplateMetadata.md) | Optional | *No description available.* |
| **selectors** | [List[SelectorDefinition]](SelectorDefinition.md) | Optional | Selectors that this policy will be applied to |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.access.models.GeneratedPolicyComponents import GeneratedPolicyComponents

instance = GeneratedPolicyComponents(
    applications=,  # optional — Applications to which the policy applies
    template_metadata=TemplateMetadata(...),  # optional
    selectors=[]  # optional — Selectors that this policy will be applied to
)
```

- [TemplateMetadata](TemplateMetadata.md)
- [SelectorDefinition](SelectorDefinition.md) — used in `selectors`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

