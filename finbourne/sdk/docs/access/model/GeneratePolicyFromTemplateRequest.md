# GeneratePolicyFromTemplateRequest

Generate policy from template
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **template_selection** | [List[TemplateSelection]](TemplateSelection.md) | Required | List of template selection, identifying policy templates to use for generation |
| **selectors** | [List[SelectorDefinition]](SelectorDefinition.md) | Optional | List of additional selectors to be included in the policy |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.access.models.GeneratePolicyFromTemplateRequest import GeneratePolicyFromTemplateRequest

instance = GeneratePolicyFromTemplateRequest(
    template_selection=[],  # required — List of template selection, identifying policy templates to use for generation
    selectors=[]  # optional — List of additional selectors to be included in the policy
)
```


## Related Models

- [TemplateSelection](TemplateSelection.md) — used in `template_selection`
- [SelectorDefinition](SelectorDefinition.md) — used in `selectors`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

