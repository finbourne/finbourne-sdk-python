# CustomEntityRequest

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **display_name** | **str** | Required | A display label for the custom entity. |
| **description** | **str** | Required | A description of the custom entity. |
| **identifiers** | [List[CustomEntityId]](CustomEntityId.md) | Required | The identifiers the custom entity will be upserted with. |
| **fields** | [List[CustomEntityField]](CustomEntityField.md) | Optional | The fields that decorate the custom entity. |
| **properties** | [Dict[str, ModelProperty]](ModelProperty.md) | Optional | The properties that decorate the custom entity. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.CustomEntityRequest import CustomEntityRequest

instance = CustomEntityRequest(
    display_name="...",  # required — A display label for the custom entity.
    description="...",  # required — A description of the custom entity.
    identifiers=[],  # required — The identifiers the custom entity will be upserted with.
    fields=[],  # optional — The fields that decorate the custom entity.
    properties=ModelProperty(...)  # optional — The properties that decorate the custom entity.
)
```

- [CustomEntityId](CustomEntityId.md) — used in `identifiers`
- [CustomEntityField](CustomEntityField.md) — used in `fields`
- [ModelProperty](ModelProperty.md) — used in `properties`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

