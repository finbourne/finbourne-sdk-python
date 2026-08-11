# UpdateSeriesIdentifierField

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **field_name** | **str** | Required | The unique identifier for the field within the dataset. |
| **display_name** | **str** | Optional | A user-friendly display name for the field. |
| **description** | **str** | Optional | A detailed description of the field and its purpose. |
| **data_type_id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **required** | **bool** | Required | Whether this field is mandatory in the dataset. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.UpdateSeriesIdentifierField import UpdateSeriesIdentifierField

instance = UpdateSeriesIdentifierField(
    field_name="...",  # required — The unique identifier for the field within the dataset.
    display_name="...",  # optional — A user-friendly display name for the field.
    description="...",  # optional — A detailed description of the field and its purpose.
    data_type_id=ResourceId(...),  # required
    required=True  # required — Whether this field is mandatory in the dataset.
)
```

- [ResourceId](ResourceId.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

