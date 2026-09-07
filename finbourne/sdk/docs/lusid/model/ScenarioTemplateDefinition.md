# ScenarioTemplateDefinition

One pre-built scenario template: the name to pass to CreateScenarioFromTemplate, what the  template does, and the parameters it accepts. A parameter not listed here is rejected by  the create call, not ignored.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **name** | **str** | Optional | The template name, as accepted by CreateScenarioFromTemplate. |
| **description** | **str** | Optional | What the template&#39;s scenario does. |
| **parameters** | [List[ScenarioTemplateParameter]](ScenarioTemplateParameter.md) | Optional | The parameters the template accepts, in the order they are documented. Parameter names are  case-sensitive; supplying one not in this list fails the create call. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.ScenarioTemplateDefinition import ScenarioTemplateDefinition

instance = ScenarioTemplateDefinition(
    name="...",  # optional — The template name, as accepted by CreateScenarioFromTemplate.
    description="...",  # optional — What the template&#39;s scenario does.
    parameters=[]  # optional — The parameters the template accepts, in the order they are documented. Parameter names are  case-sensitive; supplying one not in this list fails the create call.
)
```

- [ScenarioTemplateParameter](ScenarioTemplateParameter.md) — used in `parameters`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

