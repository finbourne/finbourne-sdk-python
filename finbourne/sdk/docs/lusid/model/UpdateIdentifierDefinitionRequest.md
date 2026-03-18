# UpdateIdentifierDefinitionRequest

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **hierarchy_level** | **str** | Optional | Optional metadata associated with the identifier definition. |
| **display_name** | **str** | Optional | A display name for the identifier. E.g. Figi. |
| **description** | **str** | Optional | An optional description for the identifier. |
| **properties** | [Dict[str, ModelProperty]](ModelProperty.md) | Optional | A set of properties for the identifier definition. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.UpdateIdentifierDefinitionRequest import UpdateIdentifierDefinitionRequest

instance = UpdateIdentifierDefinitionRequest(
    hierarchy_level="...",  # optional — Optional metadata associated with the identifier definition.
    display_name="...",  # optional — A display name for the identifier. E.g. Figi.
    description="...",  # optional — An optional description for the identifier.
    properties=ModelProperty(...)  # optional — A set of properties for the identifier definition.
)
```

- [ModelProperty](ModelProperty.md) — used in `properties`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

