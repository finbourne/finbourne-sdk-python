# UpdateRelationshipDefinitionRequest

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **display_name** | **str** | Required | The display name of the relation. |
| **outward_description** | **str** | Required | The description to relate source entity object and target entity object. |
| **inward_description** | **str** | Required | The description to relate target entity object and source entity object. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.UpdateRelationshipDefinitionRequest import UpdateRelationshipDefinitionRequest

instance = UpdateRelationshipDefinitionRequest(
    display_name="...",  # required — The display name of the relation.
    outward_description="...",  # required — The description to relate source entity object and target entity object.
    inward_description="..."  # required — The description to relate target entity object and source entity object.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

