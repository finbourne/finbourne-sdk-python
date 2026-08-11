# ComplianceTemplateVariation

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **label** | **str** | Required | Label of a Compliance Template Variation |
| **description** | **str** | Required | The description of the Compliance Template Variation |
| **required_parameters** | [List[ComplianceTemplateParameter]](ComplianceTemplateParameter.md) | Required | A parameter required by a Compliance Template Variation |
| **properties** | [Dict[str, PerpetualProperty]](PerpetualProperty.md) | Required | Properties associated with the Compliance Template Variation |
| **accepted_address_keys** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **steps** | [List[ComplianceStep]](ComplianceStep.md) | Required | The steps expressed in this template, with their required parameters |
| **referenced_group_label** | **str** | Optional | The label of a given referenced group in a Compliance Rule Template Variation |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.ComplianceTemplateVariation import ComplianceTemplateVariation

instance = ComplianceTemplateVariation(
    label="...",  # required — Label of a Compliance Template Variation
    description="...",  # required — The description of the Compliance Template Variation
    required_parameters=[],  # required — A parameter required by a Compliance Template Variation
    properties=PerpetualProperty(...),  # required — Properties associated with the Compliance Template Variation
    accepted_address_keys=ResourceId(...),  # required
    steps=[],  # required — The steps expressed in this template, with their required parameters
    referenced_group_label="..."  # optional — The label of a given referenced group in a Compliance Rule Template Variation
)
```

- [ComplianceTemplateParameter](ComplianceTemplateParameter.md) — used in `required_parameters`
- [PerpetualProperty](PerpetualProperty.md) — used in `properties`
- [ResourceId](ResourceId.md)
- [ComplianceStep](ComplianceStep.md) — used in `steps`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

