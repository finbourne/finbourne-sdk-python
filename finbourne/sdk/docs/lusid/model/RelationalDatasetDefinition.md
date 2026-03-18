# RelationalDatasetDefinition

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **display_name** | **str** | Required | A user-friendly display name for the relational dataset definition. |
| **description** | **str** | Optional | A detailed description of the relational dataset definition and its purpose. |
| **applicable_entity_types** | **List[str]** | Required | The types of entities this relational dataset definition can be applied to (e.g. Instrument, Portfolio, etc.). |
| **field_schema** | [List[RelationalDatasetFieldDefinition]](RelationalDatasetFieldDefinition.md) | Required | The schema defining the structure and data types of the relational dataset. |
| **href** | **str** | Optional | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. |
| **version** | [Version](Version.md) | Optional | *No description available.* |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.RelationalDatasetDefinition import RelationalDatasetDefinition

instance = RelationalDatasetDefinition(
    id=ResourceId(...),  # required
    display_name="...",  # required — A user-friendly display name for the relational dataset definition.
    description="...",  # optional — A detailed description of the relational dataset definition and its purpose.
    applicable_entity_types=,  # required — The types of entities this relational dataset definition can be applied to (e.g. Instrument, Portfolio, etc.).
    field_schema=[],  # required — The schema defining the structure and data types of the relational dataset.
    href="...",  # optional — The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.
    version=Version(...),  # optional
    links=[]  # optional
)
```


## Related Models

- [ResourceId](ResourceId.md)
- [RelationalDatasetFieldDefinition](RelationalDatasetFieldDefinition.md) — used in `field_schema`
- [Version](Version.md)
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

