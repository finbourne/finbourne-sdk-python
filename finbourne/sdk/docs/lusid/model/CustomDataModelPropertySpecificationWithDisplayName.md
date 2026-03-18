# CustomDataModelPropertySpecificationWithDisplayName

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **display_name** | **str** | Optional | The display name of the property definition. |
| **property_key** | **str** | Required | The property key that is required/allowed on the bound entity. |
| **required** | **bool** | Optional | Whether property is required or allowed. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.CustomDataModelPropertySpecificationWithDisplayName import CustomDataModelPropertySpecificationWithDisplayName

instance = CustomDataModelPropertySpecificationWithDisplayName(
    display_name="...",  # optional — The display name of the property definition.
    property_key="...",  # required — The property key that is required/allowed on the bound entity.
    required=True  # optional — Whether property is required or allowed.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

