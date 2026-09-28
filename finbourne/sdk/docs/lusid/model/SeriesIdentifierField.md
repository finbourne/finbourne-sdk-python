# SeriesIdentifierField

A series identifier field, carrying the same fields as the CreateSeriesIdentifierField that asks for one, so  that a caller reads back what they wrote. The field category is not among them, because every field of this  shape is a series identifier; nor is a required flag, which is not the caller's to set.
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
from finbourne.sdk.services.lusid.models.SeriesIdentifierField import SeriesIdentifierField

instance = SeriesIdentifierField(
    field_name="...",  # required — The unique identifier for the field within the dataset.
    display_name="...",  # optional — A user-friendly display name for the field.
    description="...",  # optional — A detailed description of the field and its purpose.
    data_type_id=ResourceId(...)  # required
)
```

- [ResourceId](ResourceId.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

