# ComplianceRuleTemplate

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **id** | [ResourceId](ResourceId.md) | Optional | *No description available.* |
| **description** | **str** | Optional | The description of the Compliance Template |
| **properties** | [Dict[str, ModelProperty]](ModelProperty.md) | Optional | Properties associated with the Compliance Template Variation |
| **variations** | [List[ComplianceTemplateVariationDto]](ComplianceTemplateVariationDto.md) | Optional | Variation details of a Compliance Template |
| **href** | **str** | Optional | The specific Uniform Resource Identifier (URI) for this resource at the requested asAt datetime. |
| **version** | [Version](Version.md) | Optional | *No description available.* |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.ComplianceRuleTemplate import ComplianceRuleTemplate

instance = ComplianceRuleTemplate(
    id=ResourceId(...),  # optional
    description="...",  # optional — The description of the Compliance Template
    properties=ModelProperty(...),  # optional — Properties associated with the Compliance Template Variation
    variations=[],  # optional — Variation details of a Compliance Template
    href="...",  # optional — The specific Uniform Resource Identifier (URI) for this resource at the requested asAt datetime.
    version=Version(...),  # optional
    links=[]  # optional
)
```


## Related Models

- [ResourceId](ResourceId.md)
- [ModelProperty](ModelProperty.md) — used in `properties`
- [ComplianceTemplateVariationDto](ComplianceTemplateVariationDto.md) — used in `variations`
- [Version](Version.md)
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

