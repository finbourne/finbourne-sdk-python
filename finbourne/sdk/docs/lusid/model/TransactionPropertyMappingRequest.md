# TransactionPropertyMappingRequest

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **property_key** | **str** | Required | Uniquely identifies the property definition and consists of a Domain, Scope and Code. |
| **map_from** | **str** | Optional | The Property Key of the Property to map from. |
| **set_to** | **object** | Optional | A pointer to the Property being mapped from. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.TransactionPropertyMappingRequest import TransactionPropertyMappingRequest

instance = TransactionPropertyMappingRequest(
    property_key="...",  # required — Uniquely identifies the property definition and consists of a Domain, Scope and Code.
    map_from="...",  # optional — The Property Key of the Property to map from.
    set_to=  # optional — A pointer to the Property being mapped from.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

