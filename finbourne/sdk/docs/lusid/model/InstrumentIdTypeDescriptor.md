# InstrumentIdTypeDescriptor

The description of an allowable instrument identifier.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **identifier_type** | **str** | Required | The name of the identifier type. |
| **property_key** | **str** | Required | The property key that corresponds to the identifier type. |
| **is_unique_identifier_type** | **bool** | Required | Whether or not the identifier type is enforced to be unique. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.InstrumentIdTypeDescriptor import InstrumentIdTypeDescriptor

instance = InstrumentIdTypeDescriptor(
    identifier_type="...",  # required — The name of the identifier type.
    property_key="...",  # required — The property key that corresponds to the identifier type.
    is_unique_identifier_type=True  # required — Whether or not the identifier type is enforced to be unique.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

