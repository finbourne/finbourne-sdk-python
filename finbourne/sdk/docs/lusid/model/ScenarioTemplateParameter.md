# ScenarioTemplateParameter

One parameter of a scenario template: its name (case-sensitive), whether it must be supplied,  what it means, and - for optional numeric parameters - the default used when omitted and the  unit the value is read in.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **name** | **str** | Optional | The parameter name, as supplied in the create request&#39;s Parameters dictionary. Case-sensitive. |
| **required** | **bool** | Optional | Whether the parameter must be supplied. |
| **description** | **str** | Optional | What the parameter means to this template. |
| **default_value** | **str** | Optional | The value used when the parameter is omitted. Null for required parameters. |
| **unit** | **str** | Optional | The unit a numeric value is read in: &#39;BasisPoints&#39;, &#39;PercentagePoints&#39; or &#39;Fraction&#39;  (0.20 meaning +20%). The templates do NOT share one unit - read this per template.  Null for non-numeric parameters. |
| **exclusive_group** | **str** | Optional | Parameters of a template sharing an ExclusiveGroup are alternatives: exactly one of them must  be supplied. Group members are not individually Required and carry no default. Null for  parameters that stand alone. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.ScenarioTemplateParameter import ScenarioTemplateParameter

instance = ScenarioTemplateParameter(
    name="...",  # optional — The parameter name, as supplied in the create request&#39;s Parameters dictionary. Case-sensitive.
    required=True,  # optional — Whether the parameter must be supplied.
    description="...",  # optional — What the parameter means to this template.
    default_value="...",  # optional — The value used when the parameter is omitted. Null for required parameters.
    unit="...",  # optional — The unit a numeric value is read in: &#39;BasisPoints&#39;, &#39;PercentagePoints&#39; or &#39;Fraction&#39;  (0.20 meaning +20%). The templates do NOT share one unit - read this per template.  Null for non-numeric parameters.
    exclusive_group="..."  # optional — Parameters of a template sharing an ExclusiveGroup are alternatives: exactly one of them must  be supplied. Group members are not individually Required and carry no default. Null for  parameters that stand alone.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

