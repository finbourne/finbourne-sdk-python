# CreateCustomEntityTypeRequest

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **entity_type_name** | **str** | Required | A name for the custom entity type. This will be prefixed with “~” and returned as “entityType”, which is the identifier for the custom entity type. |
| **display_name** | **str** | Required | A display label for the custom entity type. |
| **description** | **str** | Required | A description for the custom entity type. |
| **field_schema** | [List[CustomEntityFieldDefinition]](CustomEntityFieldDefinition.md) | Required | The description of the fields on the custom entity type. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.CreateCustomEntityTypeRequest import CreateCustomEntityTypeRequest

instance = CreateCustomEntityTypeRequest(
    entity_type_name="...",  # required — A name for the custom entity type. This will be prefixed with “~” and returned as “entityType”, which is the identifier for the custom entity type.
    display_name="...",  # required — A display label for the custom entity type.
    description="...",  # required — A description for the custom entity type.
    field_schema=[]  # required — The description of the fields on the custom entity type.
)
```

- [CustomEntityFieldDefinition](CustomEntityFieldDefinition.md) — used in `field_schema`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

