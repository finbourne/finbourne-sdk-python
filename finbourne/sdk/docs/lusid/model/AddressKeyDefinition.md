# AddressKeyDefinition

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **address_key** | **str** | Required | The address key of the address key definition. |
| **type** | **str** | Required | The type of the address key definition |
| **version** | [Version](Version.md) | Optional | *No description available.* |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.AddressKeyDefinition import AddressKeyDefinition

instance = AddressKeyDefinition(
    address_key="...",  # required — The address key of the address key definition.
    type="...",  # required — The type of the address key definition
    version=Version(...),  # optional
    links=[]  # optional
)
```

- [Version](Version.md)
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

