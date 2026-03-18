# CreateRelationRequest

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **source_entity_id** | **Dict[str, Optional[str]]** | Required | The identifier of the source entity. |
| **target_entity_id** | **Dict[str, Optional[str]]** | Required | The identifier of the target entity. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.CreateRelationRequest import CreateRelationRequest

instance = CreateRelationRequest(
    source_entity_id=,  # required — The identifier of the source entity.
    target_entity_id=  # required — The identifier of the target entity.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

