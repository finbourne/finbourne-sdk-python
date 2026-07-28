# CreateScenarioFromTemplateRequest

Request to create a scenario from a pre-built parameterised template. The template determines the  shape of the scenario's shifts; the parameters supply the targets (e.g. currency, instrument) and  optionally override the template's default shift size.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **template** | **str** | Required | The template to build the scenario from. Available templates: RatesUp, RatesDown, CurveSteepener,  CurveFlattener, VolSpike, EquityCrash, FxShock, RiskOff. |
| **code** | **str** | Required | The code of the scenario to create. |
| **display_name** | **str** | Optional | The display name of the created scenario. Defaults to a name derived from the template. |
| **description** | **str** | Optional | The description of the created scenario. Defaults to a description derived from the template. |
| **parameters** | **Dict[str, Optional[str]]** | Optional | Template parameters. Which parameters are required depends on the template: &#39;ccy&#39; for rate curve  templates, &#39;instrument&#39; for equity and vol templates, &#39;currencyPair&#39; for FX templates; RiskOff  requires &#39;ccy&#39; and &#39;instrument&#39;. All templates accept an optional &#39;amount&#39; override of the  template&#39;s default shift size. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.CreateScenarioFromTemplateRequest import CreateScenarioFromTemplateRequest

instance = CreateScenarioFromTemplateRequest(
    template="...",  # required — The template to build the scenario from. Available templates: RatesUp, RatesDown, CurveSteepener,  CurveFlattener, VolSpike, EquityCrash, FxShock, RiskOff.
    code="...",  # required — The code of the scenario to create.
    display_name="...",  # optional — The display name of the created scenario. Defaults to a name derived from the template.
    description="...",  # optional — The description of the created scenario. Defaults to a description derived from the template.
    parameters=  # optional — Template parameters. Which parameters are required depends on the template: &#39;ccy&#39; for rate curve  templates, &#39;instrument&#39; for equity and vol templates, &#39;currencyPair&#39; for FX templates; RiskOff  requires &#39;ccy&#39; and &#39;instrument&#39;. All templates accept an optional &#39;amount&#39; override of the  template&#39;s default shift size.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

