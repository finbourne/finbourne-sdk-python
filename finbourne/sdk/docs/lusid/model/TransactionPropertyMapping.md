# TransactionPropertyMapping

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **property_key** | **str** | Required | The key that uniquely identifies the property. It has the format {domain}/{scope}/{code} |
| **map_from** | **str** | Optional | The Property Key of the Property to map from |
| **set_to** | **object** | Optional | A pointer to the Property being mapped from |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.TransactionPropertyMapping import TransactionPropertyMapping

instance = TransactionPropertyMapping(
    property_key="...",  # required — The key that uniquely identifies the property. It has the format {domain}/{scope}/{code}
    map_from="...",  # optional — The Property Key of the Property to map from
    set_to=  # optional — A pointer to the Property being mapped from
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

