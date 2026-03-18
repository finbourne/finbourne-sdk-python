# DeleteRelationRequest

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **source_entity_id** | **Dict[str, Optional[str]]** | Required | The identifier of the source entity of the relation to be deleted. |
| **target_entity_id** | **Dict[str, Optional[str]]** | Required | The identifier of the target entity of the relation to be deleted. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.DeleteRelationRequest import DeleteRelationRequest

instance = DeleteRelationRequest(
    source_entity_id=,  # required — The identifier of the source entity of the relation to be deleted.
    target_entity_id=  # required — The identifier of the target entity of the relation to be deleted.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

