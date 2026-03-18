# CustomEntityFieldDefinition

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **name** | **str** | Required | The name of the field. |
| **lifetime** | **str** | Required | Describes how the field’s values can change over time. The available values are: “Perpetual”, “TimeVariant”. |
| **type** | **str** | Required | The value type for the field. Available values are: “String”, “Boolean”, “DateTime”, “Decimal”. |
| **collection_type** | **str** | Optional | The collection type for the field. Available values are: “Single”, “Array”. Null value defaults to “Single” |
| **required** | **bool** | Required | Whether the field is required or not. |
| **description** | **str** | Optional | An optional description for the field. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.CustomEntityFieldDefinition import CustomEntityFieldDefinition

instance = CustomEntityFieldDefinition(
    name="...",  # required — The name of the field.
    lifetime="...",  # required — Describes how the field’s values can change over time. The available values are: “Perpetual”, “TimeVariant”.
    type="...",  # required — The value type for the field. Available values are: “String”, “Boolean”, “DateTime”, “Decimal”.
    collection_type="...",  # optional — The collection type for the field. Available values are: “Single”, “Array”. Null value defaults to “Single”
    required=True,  # required — Whether the field is required or not.
    description="..."  # optional — An optional description for the field.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

