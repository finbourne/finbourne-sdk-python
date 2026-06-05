# MetadataFieldDefinition

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **field_name** | **str** | Required | The unique identifier for the metadata field. |
| **display_name** | **str** | Optional | A user-friendly display name for the metadata field. |
| **description** | **str** | Optional | A detailed description of the metadata field and its purpose. |
| **data_type_id** | [ResourceId](ResourceId.md) | Required | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.MetadataFieldDefinition import MetadataFieldDefinition

instance = MetadataFieldDefinition(
    field_name="...",  # required — The unique identifier for the metadata field.
    display_name="...",  # optional — A user-friendly display name for the metadata field.
    description="...",  # optional — A detailed description of the metadata field and its purpose.
    data_type_id=ResourceId(...)  # required
)
```

- [ResourceId](ResourceId.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

