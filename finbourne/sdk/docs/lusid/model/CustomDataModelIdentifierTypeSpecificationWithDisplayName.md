# CustomDataModelIdentifierTypeSpecificationWithDisplayName

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **display_name** | **str** | Optional | The display name of the property definition. |
| **identifier_key** | **str** | Required | The identifier type that is required/allowed on the bound entity. |
| **required** | **bool** | Optional | Whether identifier type is required or allowed. |
| **identifier_type** | **str** | Optional | The name of the identifier type. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.CustomDataModelIdentifierTypeSpecificationWithDisplayName import CustomDataModelIdentifierTypeSpecificationWithDisplayName

instance = CustomDataModelIdentifierTypeSpecificationWithDisplayName(
    display_name="...",  # optional — The display name of the property definition.
    identifier_key="...",  # required — The identifier type that is required/allowed on the bound entity.
    required=True,  # optional — Whether identifier type is required or allowed.
    identifier_type="..."  # optional — The name of the identifier type.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

