# Person

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **display_name** | **str** | Optional | The display name of the Person |
| **description** | **str** | Optional | The description of the Person |
| **href** | **str** | Optional | The specifc Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. |
| **lusid_person_id** | **str** | Optional | The unique LUSID Person Identifier of the Person. |
| **identifiers** | [Dict[str, ModelProperty]](ModelProperty.md) | Optional | Unique client-defined identifiers of the Person. |
| **properties** | [Dict[str, ModelProperty]](ModelProperty.md) | Optional | A set of properties associated to the Person. There can be multiple properties associated with a property key. |
| **relationships** | [List[Relationship]](Relationship.md) | Optional | A set of relationships associated to the Person. |
| **version** | [Version](Version.md) | Optional | *No description available.* |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.Person import Person

instance = Person(
    display_name="...",  # optional — The display name of the Person
    description="...",  # optional — The description of the Person
    href="...",  # optional — The specifc Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.
    lusid_person_id="...",  # optional — The unique LUSID Person Identifier of the Person.
    identifiers=ModelProperty(...),  # optional — Unique client-defined identifiers of the Person.
    properties=ModelProperty(...),  # optional — A set of properties associated to the Person. There can be multiple properties associated with a property key.
    relationships=[],  # optional — A set of relationships associated to the Person.
    version=Version(...),  # optional
    links=[]  # optional
)
```

- [ModelProperty](ModelProperty.md) — used in `identifiers`
- [ModelProperty](ModelProperty.md) — used in `properties`
- [Relationship](Relationship.md) — used in `relationships`
- [Version](Version.md)
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

