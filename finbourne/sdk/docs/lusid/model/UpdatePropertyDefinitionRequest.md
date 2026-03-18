# UpdatePropertyDefinitionRequest

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **display_name** | **str** | Required | The display name of the property. |
| **property_description** | **str** | Optional | Describes the property |
| **custom_entity_types** | **List[str]** | Optional | The custom entity types that properties relating to this property definition can be applied to. |
| **value_format** | **str** | Optional | The format in which values for this property definition should be represented. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.UpdatePropertyDefinitionRequest import UpdatePropertyDefinitionRequest

instance = UpdatePropertyDefinitionRequest(
    display_name="...",  # required — The display name of the property.
    property_description="...",  # optional — Describes the property
    custom_entity_types=,  # optional — The custom entity types that properties relating to this property definition can be applied to.
    value_format="..."  # optional — The format in which values for this property definition should be represented.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

