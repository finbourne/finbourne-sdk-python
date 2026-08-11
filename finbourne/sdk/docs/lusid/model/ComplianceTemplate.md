# ComplianceTemplate

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **description** | **str** | Required | The description of the Compliance Template |
| **tags** | **List[str]** | Optional | Tags for a Compliance Template |
| **variations** | [List[ComplianceTemplateVariation]](ComplianceTemplateVariation.md) | Required | Variation details of a Compliance Template |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.ComplianceTemplate import ComplianceTemplate

instance = ComplianceTemplate(
    id=ResourceId(...),  # required
    description="...",  # required — The description of the Compliance Template
    tags=,  # optional — Tags for a Compliance Template
    variations=[],  # required — Variation details of a Compliance Template
    links=[]  # optional
)
```


## Related Models

- [ResourceId](ResourceId.md)
- [ComplianceTemplateVariation](ComplianceTemplateVariation.md) — used in `variations`
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

