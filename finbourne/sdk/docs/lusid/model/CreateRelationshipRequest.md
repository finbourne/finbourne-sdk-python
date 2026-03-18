# CreateRelationshipRequest

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **source_entity_id** | **Dict[str, Optional[str]]** | Required | The identifier of the source entity. |
| **target_entity_id** | **Dict[str, Optional[str]]** | Required | The identifier of the target entity. |
| **effective_from** | **str** | Optional | The effective date of the relationship to be created |
| **effective_until** | **str** | Optional | The effective datetime until which the relationship is valid. If not supplied this will be valid indefinitely. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.CreateRelationshipRequest import CreateRelationshipRequest

instance = CreateRelationshipRequest(
    source_entity_id=,  # required — The identifier of the source entity.
    target_entity_id=,  # required — The identifier of the target entity.
    effective_from="...",  # optional — The effective date of the relationship to be created
    effective_until="..."  # optional — The effective datetime until which the relationship is valid. If not supplied this will be valid indefinitely.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

