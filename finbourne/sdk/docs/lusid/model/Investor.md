# Investor

Representation of an Investor on the LUSID API
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **investor_type** | **str** | Optional | The type of the Investor |
| **identifiers** | **Dict[str, Optional[str]]** | Optional | The identifiers of the Investor |
| **entity_unique_id** | **str** | Optional | The unique Investor entity identifier |
| **person** | [Person](Person.md) | Optional | *No description available.* |
| **legal_entity** | [LegalEntity](LegalEntity.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.Investor import Investor

instance = Investor(
    investor_type="...",  # optional — The type of the Investor
    identifiers=,  # optional — The identifiers of the Investor
    entity_unique_id="...",  # optional — The unique Investor entity identifier
    person=Person(...),  # optional
    legal_entity=LegalEntity(...)  # optional
)
```

- [Person](Person.md)
- [LegalEntity](LegalEntity.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

