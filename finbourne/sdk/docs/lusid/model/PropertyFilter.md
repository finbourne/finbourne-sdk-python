# PropertyFilter

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **left** | **str** | Optional | The key that uniquely identifies a queryable address in Lusid. |
| **operator** | **str** | Optional | The available values are: Equals, NotEquals, GreaterThan, GreaterThanOrEqualTo, LessThan, LessThanOrEqualTo, In, StartsWith |
| **right** | **object** | Optional | *No description available.* |
| **right_operand_type** | **str** | Optional | The available values are: Absolute, Property |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.PropertyFilter import PropertyFilter

instance = PropertyFilter(
    left="...",  # optional — The key that uniquely identifies a queryable address in Lusid.
    operator="...",  # optional — The available values are: Equals, NotEquals, GreaterThan, GreaterThanOrEqualTo, LessThan, LessThanOrEqualTo, In, StartsWith
    right=,  # optional
    right_operand_type="..."  # optional — The available values are: Absolute, Property
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

