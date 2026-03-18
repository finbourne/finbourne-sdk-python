# MappableField

Information about a field that can be designed on (regardless if it currently is) Kind of a \"mini-available catalog entry\"
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **name** | **str** | Optional | Name of the field in need of mapping (The field name from within the Table Parameter itself) |
| **type** | [DataType](DataType.md) | Optional | *No description available.* |
| **description** | **str** | Optional | Description of the field (just for rendering to the user) |
| **display_name** | **str** | Optional | Display Name of the field (just for rendering to the user) |
| **sample_values** | **str** | Optional | Example values for the field (just for rendering to the user) |
| **allowed_values** | **str** | Optional | Any set of exactly allowed values for the field (perhaps just for rendering to the user, if nothing else) |
| **mandatory_for_actions** | **str** | Optional | Which &#x60;Actions&#x60; is this mandatory for? If any (and potentially when), perhaps just for rendering to the user, if nothing else |
| **mapping** | [ExpressionWithAlias](ExpressionWithAlias.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.luminesce.models.MappableField import MappableField

instance = MappableField(
    name="...",  # optional — Name of the field in need of mapping (The field name from within the Table Parameter itself)
    type=DataType(...),  # optional
    description="...",  # optional — Description of the field (just for rendering to the user)
    display_name="...",  # optional — Display Name of the field (just for rendering to the user)
    sample_values="...",  # optional — Example values for the field (just for rendering to the user)
    allowed_values="...",  # optional — Any set of exactly allowed values for the field (perhaps just for rendering to the user, if nothing else)
    mandatory_for_actions="...",  # optional — Which &#x60;Actions&#x60; is this mandatory for? If any (and potentially when), perhaps just for rendering to the user, if nothing else
    mapping=ExpressionWithAlias(...)  # optional
)
```

- [DataType](DataType.md)
- [ExpressionWithAlias](ExpressionWithAlias.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

