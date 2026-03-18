# DeleteRelationshipRequest

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **source_entity_id** | **Dict[str, Optional[str]]** | Required | The identifier of the source entity of the relationship to be deleted. |
| **target_entity_id** | **Dict[str, Optional[str]]** | Required | The identifier of the target entity of the relationship to be deleted. |
| **effective_from** | **str** | Optional | The effective date of the relationship to be deleted |
| **effective_until** | **str** | Optional | The effective datetime until which the relationship will be deleted. If not supplied the deletion will be permanent. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.DeleteRelationshipRequest import DeleteRelationshipRequest

instance = DeleteRelationshipRequest(
    source_entity_id=,  # required — The identifier of the source entity of the relationship to be deleted.
    target_entity_id=,  # required — The identifier of the target entity of the relationship to be deleted.
    effective_from="...",  # optional — The effective date of the relationship to be deleted
    effective_until="..."  # optional — The effective datetime until which the relationship will be deleted. If not supplied the deletion will be permanent.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

