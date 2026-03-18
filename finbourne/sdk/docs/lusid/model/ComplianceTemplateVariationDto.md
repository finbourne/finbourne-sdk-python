# ComplianceTemplateVariationDto

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **label** | **str** | Required | *No description available.* |
| **description** | **str** | Required | *No description available.* |
| **outcome_description** | **str** | Optional | *No description available.* |
| **referenced_group_label** | **str** | Optional | *No description available.* |
| **steps** | [List[ComplianceStep]](ComplianceStep.md) | Required | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.ComplianceTemplateVariationDto import ComplianceTemplateVariationDto

instance = ComplianceTemplateVariationDto(
    label="...",  # required
    description="...",  # required
    outcome_description="...",  # optional
    referenced_group_label="...",  # optional
    steps=[]  # required
)
```

- [ComplianceStep](ComplianceStep.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

