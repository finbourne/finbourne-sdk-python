# UpsertRecDefinitionPropertiesResponse

The properties upserted onto a rec definition.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **href** | **str** | Optional | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. |
| **properties** | [Dict[str, PerpetualProperty]](PerpetualProperty.md) | Optional | The rec definition properties that were upserted. These will be from the &#39;RecDefinition&#39; domain. Properties deleted by the request are not included. |
| **version** | [Version](Version.md) | Optional | *No description available.* |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.UpsertRecDefinitionPropertiesResponse import UpsertRecDefinitionPropertiesResponse

instance = UpsertRecDefinitionPropertiesResponse(
    href="...",  # optional — The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.
    properties=PerpetualProperty(...),  # optional — The rec definition properties that were upserted. These will be from the &#39;RecDefinition&#39; domain. Properties deleted by the request are not included.
    version=Version(...),  # optional
    links=[]  # optional
)
```

- [PerpetualProperty](PerpetualProperty.md) — used in `properties`
- [Version](Version.md)
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

