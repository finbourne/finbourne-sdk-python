# PropertyValueIn

A criterion that checks whether a Property Value is equal to one of the given string values
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **property_key** | **str** | Required | The property key whose value will form the left-hand side of the operation |
| **value** | **List[str]** | Required | The value to be compared against |
| **criterion_type** | **str** | Required | The available values are: PropertyValueEquals, PropertyValueIn, SubHoldingKeyValueEquals |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.PropertyValueIn import PropertyValueIn

instance = PropertyValueIn(
    property_key="...",  # required — The property key whose value will form the left-hand side of the operation
    value=,  # required — The value to be compared against
    criterion_type="..."  # required — The available values are: PropertyValueEquals, PropertyValueIn, SubHoldingKeyValueEquals
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

