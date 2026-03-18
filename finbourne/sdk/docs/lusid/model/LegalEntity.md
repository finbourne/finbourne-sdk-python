# LegalEntity

Representation of Legal Entity on LUSID API
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **display_name** | **str** | Optional | The display name of the Legal Entity |
| **description** | **str** | Optional | The description of the Legal Entity |
| **href** | **str** | Optional | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. |
| **lusid_legal_entity_id** | **str** | Optional | The unique LUSID Legal Entity Identifier of the Legal Entity. |
| **identifiers** | [Dict[str, ModelProperty]](ModelProperty.md) | Optional | Unique client-defined identifiers of the Legal Entity. |
| **properties** | [Dict[str, ModelProperty]](ModelProperty.md) | Optional | A set of properties associated to the Legal Entity. |
| **relationships** | [List[Relationship]](Relationship.md) | Optional | A set of relationships associated to the Legal Entity. |
| **counterparty_risk_information** | [CounterpartyRiskInformation](CounterpartyRiskInformation.md) | Optional | *No description available.* |
| **version** | [Version](Version.md) | Optional | *No description available.* |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.LegalEntity import LegalEntity

instance = LegalEntity(
    display_name="...",  # optional — The display name of the Legal Entity
    description="...",  # optional — The description of the Legal Entity
    href="...",  # optional — The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.
    lusid_legal_entity_id="...",  # optional — The unique LUSID Legal Entity Identifier of the Legal Entity.
    identifiers=ModelProperty(...),  # optional — Unique client-defined identifiers of the Legal Entity.
    properties=ModelProperty(...),  # optional — A set of properties associated to the Legal Entity.
    relationships=[],  # optional — A set of relationships associated to the Legal Entity.
    counterparty_risk_information=CounterpartyRiskInformation(...),  # optional
    version=Version(...),  # optional
    links=[]  # optional
)
```

- [ModelProperty](ModelProperty.md) — used in `identifiers`
- [ModelProperty](ModelProperty.md) — used in `properties`
- [Relationship](Relationship.md) — used in `relationships`
- [CounterpartyRiskInformation](CounterpartyRiskInformation.md)
- [Version](Version.md)
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

