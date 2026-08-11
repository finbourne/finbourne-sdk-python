# LusidPropertyDefinition

Defines the information in a LUSID Property Definition
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **key** | **str** | Required | *No description available.* *(read-only)* |
| **product_entity_item_key** | **str** | Required | Property key associated with the mapping |
| **domain** | **str** | Required | The domain of this definition. |
| **scope** | **str** | Required | The scope of this definition. |
| **code** | **str** | Required | The code of this definition. |
| **display_name** | **str** | Required | The name used when this definition is displayed. |
| **data_type_id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **description** | **str** | Required |  |
| **lifetime** | **str** | Required |  |
| **constraint_style** | **str** | Required |  |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.horizon.models.LusidPropertyDefinition import LusidPropertyDefinition

instance = LusidPropertyDefinition(
    key="...",  # required
    product_entity_item_key="...",  # required — Property key associated with the mapping
    domain="...",  # required — The domain of this definition.
    scope="...",  # required — The scope of this definition.
    code="...",  # required — The code of this definition.
    display_name="...",  # required — The name used when this definition is displayed.
    data_type_id=ResourceId(...),  # required
    description="...",  # required — 
    lifetime="...",  # required — 
    constraint_style="..."  # required — 
)
```

- [ResourceId](ResourceId.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

