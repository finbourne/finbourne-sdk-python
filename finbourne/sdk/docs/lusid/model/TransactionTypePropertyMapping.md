# TransactionTypePropertyMapping

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **property_key** | **str** | Required | The key that uniquely identifies the property. It has the format {domain}/{scope}/{code} |
| **map_from** | **str** | Optional | The Property Key of the Property to map from |
| **set_to** | **str** | Optional | A pointer to the Property being mapped from |
| **template_from** | **str** | Optional | The template that defines how the property value is constructed from transaction, instrument and portfolio details. |
| **nullify** | **bool** | Optional | Flag to unset the Property Key for the mapping |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.TransactionTypePropertyMapping import TransactionTypePropertyMapping

instance = TransactionTypePropertyMapping(
    property_key="...",  # required — The key that uniquely identifies the property. It has the format {domain}/{scope}/{code}
    map_from="...",  # optional — The Property Key of the Property to map from
    set_to="...",  # optional — A pointer to the Property being mapped from
    template_from="...",  # optional — The template that defines how the property value is constructed from transaction, instrument and portfolio details.
    nullify=True  # optional — Flag to unset the Property Key for the mapping
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

