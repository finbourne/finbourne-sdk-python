# DerivationFormulaExplainRequest

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **entity_type** | **str** | Required | The type of the entity for which the derived property or partial formula is to be resolved against. |
| **scope** | **str** | Optional | (Optional) The scope that entity exists in. If no scope is provided, the default scope for the entity type will be used. |
| **code** | **str** | Optional | (Optional) The code of the entity, to be provided for entities that support scope/code retrieval. If no code or identifier is provided, the logical evaluation tree without resolved values is returned. |
| **subentity_id** | **str** | Optional | (Optional) The id of the sub-entity to explain the derived property for. This must be provided along with the scope/code of the parent entity. |
| **identifier** | **Dict[str, Optional[str]]** | Optional | (Optional). An identifier key/value pair that uniquely identifies the entity to explain the derived property for. This can be either an instrument identifier, or an identifier property. If no code or identifier is provided, the logical evaluation tree without resolved values is returned. |
| **property_key** | **str** | Optional | (Optional) The key of the derived property to get an explanation for. This takes the format {domain}/{scope}/{code}. One of either property key or partial formula must be provided. |
| **partial_formula** | **str** | Optional | (Optional) A partial derivation formula to get an explanation for. Can be provided in lieu of a property key. One of either property key or partial formula must be provided. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.DerivationFormulaExplainRequest import DerivationFormulaExplainRequest

instance = DerivationFormulaExplainRequest(
    entity_type="...",  # required — The type of the entity for which the derived property or partial formula is to be resolved against.
    scope="...",  # optional — (Optional) The scope that entity exists in. If no scope is provided, the default scope for the entity type will be used.
    code="...",  # optional — (Optional) The code of the entity, to be provided for entities that support scope/code retrieval. If no code or identifier is provided, the logical evaluation tree without resolved values is returned.
    subentity_id="...",  # optional — (Optional) The id of the sub-entity to explain the derived property for. This must be provided along with the scope/code of the parent entity.
    identifier=,  # optional — (Optional). An identifier key/value pair that uniquely identifies the entity to explain the derived property for. This can be either an instrument identifier, or an identifier property. If no code or identifier is provided, the logical evaluation tree without resolved values is returned.
    property_key="...",  # optional — (Optional) The key of the derived property to get an explanation for. This takes the format {domain}/{scope}/{code}. One of either property key or partial formula must be provided.
    partial_formula="..."  # optional — (Optional) A partial derivation formula to get an explanation for. Can be provided in lieu of a property key. One of either property key or partial formula must be provided.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

