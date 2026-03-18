# TemplateSelection

A template selection, identifying a policy template to use for generation
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **scope** | **str** | Required | Scope identifying policy template to use for generation |
| **code** | **str** | Required | Code identifying policy template to use for generation |
| **selector_tags** | **List[str]** | Optional | List of selector tags to optionally filter in the template generation  (Eg: Feature, Data, etc) |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.access.models.TemplateSelection import TemplateSelection

instance = TemplateSelection(
    scope="...",  # required — Scope identifying policy template to use for generation
    code="...",  # required — Code identifying policy template to use for generation
    selector_tags=  # optional — List of selector tags to optionally filter in the template generation  (Eg: Feature, Data, etc)
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

