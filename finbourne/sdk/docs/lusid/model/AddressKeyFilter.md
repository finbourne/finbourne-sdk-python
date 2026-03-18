# AddressKeyFilter

Class specifying a filtering operation
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **left** | **str** | Optional | Address for the value in the row |
| **operator** | **str** | Optional | What sort of comparison is the filter performing. Can be either \&quot;eq\&quot; for equals or \&quot;neq\&quot; for not equals. |
| **right** | [ResultValue](ResultValue.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.AddressKeyFilter import AddressKeyFilter

instance = AddressKeyFilter(
    left="...",  # optional — Address for the value in the row
    operator="...",  # optional — What sort of comparison is the filter performing. Can be either \&quot;eq\&quot; for equals or \&quot;neq\&quot; for not equals.
    right=ResultValue(...)  # optional
)
```

- [ResultValue](ResultValue.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

