# ResultValueBool

A simple result for a boolean value
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **value** | **bool** | Optional | The value itself |
| **result_value_type** | **str** | Required | The available values are: ResultValue, ResultValueDictionary, ResultValue0D, ResultValueDecimal, ResultValueInt, ResultValueString, ResultValueBool, ResultValueCurrency, CashFlowValue, CashFlowValueSet, ResultValueLifeCycleEventValue, ResultValueDateTimeOffset |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.ResultValueBool import ResultValueBool

instance = ResultValueBool(
    value=True,  # optional — The value itself
    result_value_type="..."  # required — The available values are: ResultValue, ResultValueDictionary, ResultValue0D, ResultValueDecimal, ResultValueInt, ResultValueString, ResultValueBool, ResultValueCurrency, CashFlowValue, CashFlowValueSet, ResultValueLifeCycleEventValue, ResultValueDateTimeOffset
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

