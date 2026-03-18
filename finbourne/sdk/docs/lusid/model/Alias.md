# Alias

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **attribute_name** | **str** | Required | The property key, identifier type, or field to be replaced by an alias. |
| **attribute_alias** | **str** | Required | The alias to replace the property key, identifier type, or field on the bound entity. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.Alias import Alias

instance = Alias(
    attribute_name="...",  # required — The property key, identifier type, or field to be replaced by an alias.
    attribute_alias="..."  # required — The alias to replace the property key, identifier type, or field on the bound entity.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

