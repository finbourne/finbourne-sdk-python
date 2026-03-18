# CustomDataModelIdentifierTypeSpecification

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **identifier_key** | **str** | Required | The identifier type that is required/allowed on the bound entity. |
| **required** | **bool** | Optional | Whether identifier type is required or allowed. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.CustomDataModelIdentifierTypeSpecification import CustomDataModelIdentifierTypeSpecification

instance = CustomDataModelIdentifierTypeSpecification(
    identifier_key="...",  # required — The identifier type that is required/allowed on the bound entity.
    required=True  # optional — Whether identifier type is required or allowed.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

