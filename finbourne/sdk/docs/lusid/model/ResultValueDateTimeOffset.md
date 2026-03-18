# ResultValueDateTimeOffset

A simple result for a date time value
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **value** | **datetime** | Optional | The value itself |
| **dimension** | **int** | Optional | The dimension of the result. Can be null if there is no sensible way of defining the dimension. This field should not be  populate by the user on upsertion. |
| **result_value_type** | **str** | Required | The available values are: ResultValue, ResultValueDictionary, ResultValue0D, ResultValueDecimal, ResultValueInt, ResultValueString, ResultValueBool, ResultValueCurrency, CashFlowValue, CashFlowValueSet, ResultValueLifeCycleEventValue, ResultValueDateTimeOffset |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.ResultValueDateTimeOffset import ResultValueDateTimeOffset

instance = ResultValueDateTimeOffset(
    value=datetime.now(),  # optional — The value itself
    dimension=0,  # optional — The dimension of the result. Can be null if there is no sensible way of defining the dimension. This field should not be  populate by the user on upsertion.
    result_value_type="..."  # required — The available values are: ResultValue, ResultValueDictionary, ResultValue0D, ResultValueDecimal, ResultValueInt, ResultValueString, ResultValueBool, ResultValueCurrency, CashFlowValue, CashFlowValueSet, ResultValueLifeCycleEventValue, ResultValueDateTimeOffset
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

