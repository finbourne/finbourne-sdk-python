# UpdateCustomEntityDefinitionRequest

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **display_name** | **str** | Required | A display label for the custom entity type. |
| **description** | **str** | Required | A description for the custom entity type. |
| **field_schema** | [List[CustomEntityFieldDefinition]](CustomEntityFieldDefinition.md) | Required | The description of the fields on the custom entity type. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.UpdateCustomEntityDefinitionRequest import UpdateCustomEntityDefinitionRequest

instance = UpdateCustomEntityDefinitionRequest(
    display_name="...",  # required — A display label for the custom entity type.
    description="...",  # required — A description for the custom entity type.
    field_schema=[]  # required — The description of the fields on the custom entity type.
)
```

- [CustomEntityFieldDefinition](CustomEntityFieldDefinition.md) — used in `field_schema`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

