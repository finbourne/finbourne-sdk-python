# CreateSeriesIdentifierField

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **field_name** | **str** | Required | The unique identifier for the field within the dataset. |
| **display_name** | **str** | Optional | A user-friendly display name for the field. |
| **description** | **str** | Optional | A detailed description of the field and its purpose. |
| **data_type_id** | [ResourceId](ResourceId.md) | Required | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.CreateSeriesIdentifierField import CreateSeriesIdentifierField

instance = CreateSeriesIdentifierField(
    field_name="...",  # required — The unique identifier for the field within the dataset.
    display_name="...",  # optional — A user-friendly display name for the field.
    description="...",  # optional — A detailed description of the field and its purpose.
    data_type_id=ResourceId(...)  # required
)
```

- [ResourceId](ResourceId.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

