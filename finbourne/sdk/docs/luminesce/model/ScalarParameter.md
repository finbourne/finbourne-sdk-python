# ScalarParameter

Describes a scalar parameter as defined in the SQL
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **name** | **str** | Required | Name of the scalar parameter |
| **type** | [DataType](DataType.md) | Required | *No description available.* |
| **value** | **object** | Optional | the default value of the parameter |
| **value_options** | **List[object]** | Optional | Values of the parameter listed as being available for choosing from. |
| **value_must_be_from_options** | **bool** | Optional | Must Value be one of ValueOptions (if any)? |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.luminesce.models.ScalarParameter import ScalarParameter

instance = ScalarParameter(
    name="...",  # required — Name of the scalar parameter
    type=DataType(...),  # required
    value=,  # optional — the default value of the parameter
    value_options=,  # optional — Values of the parameter listed as being available for choosing from.
    value_must_be_from_options=True  # optional — Must Value be one of ValueOptions (if any)?
)
```

- [DataType](DataType.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

