# UpdateDerivedPropertyDefinitionRequest

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **display_name** | **str** | Required | The display name of the property. |
| **data_type_id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **property_description** | **str** | Optional | Describes the property |
| **derivation_formula** | **str** | Required | The rule that defines how data is composed for a derived property. |
| **is_filterable** | **bool** | Required | Bool indicating whether the values of this property are fitlerable, this is true for all non-derived property defintions.  For a derived definition this must be set true to enable filtering. |
| **value_format** | **str** | Optional | The format in which values for this property definition should be represented. |
| **custom_entity_type** | **str** | Optional | The custom entity type that this derived property definition can be applied to. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.UpdateDerivedPropertyDefinitionRequest import UpdateDerivedPropertyDefinitionRequest

instance = UpdateDerivedPropertyDefinitionRequest(
    display_name="...",  # required — The display name of the property.
    data_type_id=ResourceId(...),  # required
    property_description="...",  # optional — Describes the property
    derivation_formula="...",  # required — The rule that defines how data is composed for a derived property.
    is_filterable=True,  # required — Bool indicating whether the values of this property are fitlerable, this is true for all non-derived property defintions.  For a derived definition this must be set true to enable filtering.
    value_format="...",  # optional — The format in which values for this property definition should be represented.
    custom_entity_type="..."  # optional — The custom entity type that this derived property definition can be applied to.
)
```

- [ResourceId](ResourceId.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

