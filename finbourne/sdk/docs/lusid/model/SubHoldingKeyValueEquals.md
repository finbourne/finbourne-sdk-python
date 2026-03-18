# SubHoldingKeyValueEquals

A criterion that checks whether a SubHoldingKey Value is equal to the given string value
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **sub_holding_key** | **str** | Required | The sub holding key whose value will form the left-hand side of the operation |
| **value** | **str** | Required | The value to be compared against |
| **criterion_type** | **str** | Required | The available values are: PropertyValueEquals, PropertyValueIn, SubHoldingKeyValueEquals |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.SubHoldingKeyValueEquals import SubHoldingKeyValueEquals

instance = SubHoldingKeyValueEquals(
    sub_holding_key="...",  # required — The sub holding key whose value will form the left-hand side of the operation
    value="...",  # required — The value to be compared against
    criterion_type="..."  # required — The available values are: PropertyValueEquals, PropertyValueIn, SubHoldingKeyValueEquals
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

