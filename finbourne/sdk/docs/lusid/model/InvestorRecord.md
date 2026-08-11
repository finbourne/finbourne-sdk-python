# InvestorRecord

Representation of an Investor Record on the LUSID API
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **scope** | **str** | Optional | The scope in which the Investor Record lies. |
| **identifiers** | [Dict[str, ModelProperty]](ModelProperty.md) | Optional | Unique client-defined identifiers of the Investor Record. |
| **display_name** | **str** | Optional | The display name of the Investor Record |
| **description** | **str** | Optional | The description of the Investor Record |
| **investor** | [Investor](Investor.md) | Optional | *No description available.* |
| **lusid_investor_record_id** | **str** | Optional | The unique LUSID Investor Record Identifier of the Investor Record. |
| **properties** | [Dict[str, ModelProperty]](ModelProperty.md) | Optional | A set of properties associated to the Investor Record. |
| **relationships** | [List[Relationship]](Relationship.md) | Optional | A set of relationships associated to the Investor Record. |
| **href** | **str** | Optional | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. |
| **version** | [Version](Version.md) | Optional | *No description available.* |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.InvestorRecord import InvestorRecord

instance = InvestorRecord(
    scope="...",  # optional — The scope in which the Investor Record lies.
    identifiers=ModelProperty(...),  # optional — Unique client-defined identifiers of the Investor Record.
    display_name="...",  # optional — The display name of the Investor Record
    description="...",  # optional — The description of the Investor Record
    investor=Investor(...),  # optional
    lusid_investor_record_id="...",  # optional — The unique LUSID Investor Record Identifier of the Investor Record.
    properties=ModelProperty(...),  # optional — A set of properties associated to the Investor Record.
    relationships=[],  # optional — A set of relationships associated to the Investor Record.
    href="...",  # optional — The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.
    version=Version(...),  # optional
    links=[]  # optional
)
```

- [ModelProperty](ModelProperty.md) — used in `identifiers`
- [Investor](Investor.md)
- [ModelProperty](ModelProperty.md) — used in `properties`
- [Relationship](Relationship.md) — used in `relationships`
- [Version](Version.md)
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

