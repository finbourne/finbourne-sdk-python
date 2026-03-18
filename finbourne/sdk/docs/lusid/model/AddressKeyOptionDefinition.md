# AddressKeyOptionDefinition

The definition of an Address Key Option
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **name** | **str** | Required | The name of the option |
| **type** | **str** | Required | The type of the option |
| **description** | **str** | Required | The description of the option |
| **optional** | **bool** | Required | Is this option required or optional? |
| **allowed_value_set** | **List[str]** | Optional | If the option is a string or enum, the allowed set of values it can take. |
| **default_value** | **str** | Optional | If the option is not required, what is the default value? |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.AddressKeyOptionDefinition import AddressKeyOptionDefinition

instance = AddressKeyOptionDefinition(
    name="...",  # required — The name of the option
    type="...",  # required — The type of the option
    description="...",  # required — The description of the option
    optional=True,  # required — Is this option required or optional?
    allowed_value_set=,  # optional — If the option is a string or enum, the allowed set of values it can take.
    default_value="..."  # optional — If the option is not required, what is the default value?
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

