# CreateRecDefinitionRequest

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **display_name** | **str** | Required | The name of the rec definition. |
| **description** | **str** | Optional | A description of the rec definition. |
| **side_names** | [RecDefSideNames](RecDefSideNames.md) | Optional | *No description available.* |
| **details** | [RecDefinitionDetails](RecDefinitionDetails.md) | Required | *No description available.* |
| **review_configuration** | [RecReviewConfiguration](RecReviewConfiguration.md) | Optional | *No description available.* |
| **date_policy** | [RecDatePolicy](RecDatePolicy.md) | Optional | *No description available.* |
| **properties** | [Dict[str, PerpetualProperty]](PerpetualProperty.md) | Optional | Properties in the RecDefinition domain. On update, a property with a null value is deleted and omitted properties are left unchanged. Filterable and sortable. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.CreateRecDefinitionRequest import CreateRecDefinitionRequest

instance = CreateRecDefinitionRequest(
    id=ResourceId(...),  # required
    display_name="...",  # required — The name of the rec definition.
    description="...",  # optional — A description of the rec definition.
    side_names=RecDefSideNames(...),  # optional
    details=RecDefinitionDetails(...),  # required
    review_configuration=RecReviewConfiguration(...),  # optional
    date_policy=RecDatePolicy(...),  # optional
    properties=PerpetualProperty(...)  # optional — Properties in the RecDefinition domain. On update, a property with a null value is deleted and omitted properties are left unchanged. Filterable and sortable.
)
```


## Related Models

- [ResourceId](ResourceId.md)
- [RecDefSideNames](RecDefSideNames.md)
- [RecDefinitionDetails](RecDefinitionDetails.md)
- [RecReviewConfiguration](RecReviewConfiguration.md)
- [RecDatePolicy](RecDatePolicy.md)
- [PerpetualProperty](PerpetualProperty.md) — used in `properties`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

