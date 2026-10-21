# RecDefinition

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **display_name** | **str** | Required | The name of the rec definition. |
| **description** | **str** | Optional | A description of the rec definition. |
| **side_names** | [RecDefSideNames](RecDefSideNames.md) | Optional | *No description available.* |
| **details** | [RecDefinitionDetails](RecDefinitionDetails.md) | Required | *No description available.* |
| **review_configuration** | [RecReviewConfiguration](RecReviewConfiguration.md) | Required | *No description available.* |
| **date_policy** | [RecDatePolicy](RecDatePolicy.md) | Required | *No description available.* |
| **properties** | [Dict[str, PerpetualProperty]](PerpetualProperty.md) | Optional | Properties in the RecDefinition domain. On update, a property with a null value is deleted and omitted properties are left unchanged. Filterable and sortable. |
| **href** | **str** | Optional | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. |
| **version** | [Version](Version.md) | Optional | *No description available.* |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.RecDefinition import RecDefinition

instance = RecDefinition(
    id=ResourceId(...),  # required
    display_name="...",  # required — The name of the rec definition.
    description="...",  # optional — A description of the rec definition.
    side_names=RecDefSideNames(...),  # optional
    details=RecDefinitionDetails(...),  # required
    review_configuration=RecReviewConfiguration(...),  # required
    date_policy=RecDatePolicy(...),  # required
    properties=PerpetualProperty(...),  # optional — Properties in the RecDefinition domain. On update, a property with a null value is deleted and omitted properties are left unchanged. Filterable and sortable.
    href="...",  # optional — The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.
    version=Version(...),  # optional
    links=[]  # optional
)
```


## Related Models

- [ResourceId](ResourceId.md)
- [RecDefSideNames](RecDefSideNames.md)
- [RecDefinitionDetails](RecDefinitionDetails.md)
- [RecReviewConfiguration](RecReviewConfiguration.md)
- [RecDatePolicy](RecDatePolicy.md)
- [PerpetualProperty](PerpetualProperty.md) — used in `properties`
- [Version](Version.md)
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

