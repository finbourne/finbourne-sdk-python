# ResultValueInt

A simple result type which holds an integer
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **value** | **int** | Optional | The value itself |
| **dimension** | **int** | Optional | The dimension of the result. Can be null if there is no sensible way of defining the dimension. This field should not be  populate by the user on upsertion. |
| **result_value_type** | **str** | Required | The available values are: ResultValue, ResultValueDictionary, ResultValue0D, ResultValueDecimal, ResultValueInt, ResultValueString, ResultValueBool, ResultValueCurrency, CashFlowValue, CashFlowValueSet, ResultValueLifeCycleEventValue, ResultValueDateTimeOffset |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.ResultValueInt import ResultValueInt

instance = ResultValueInt(
    value=0,  # optional — The value itself
    dimension=0,  # optional — The dimension of the result. Can be null if there is no sensible way of defining the dimension. This field should not be  populate by the user on upsertion.
    result_value_type="..."  # required — The available values are: ResultValue, ResultValueDictionary, ResultValue0D, ResultValueDecimal, ResultValueInt, ResultValueString, ResultValueBool, ResultValueCurrency, CashFlowValue, CashFlowValueSet, ResultValueLifeCycleEventValue, ResultValueDateTimeOffset
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

