# LusidEntity

Information about the LUSID entity this data can be used with
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **entity_type** | **str** | Required | The entity type |
| **entity_type_display_name** | **str** | Required | The display name for the entity type. |
| **entity_sub_type** | **str** | Optional | The entity sub-type |
| **entity_sub_type_display_name** | **str** | Optional | Display name for the entity sub-type |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.horizon.models.LusidEntity import LusidEntity

instance = LusidEntity(
    entity_type="...",  # required — The entity type
    entity_type_display_name="...",  # required — The display name for the entity type.
    entity_sub_type="...",  # optional — The entity sub-type
    entity_sub_type_display_name="..."  # optional — Display name for the entity sub-type
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

