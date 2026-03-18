# ResultValueCurrency

A simple result for a currency value
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **value** | **str** | Optional | The value itself |
| **result_value_type** | **str** | Required | The available values are: ResultValue, ResultValueDictionary, ResultValue0D, ResultValueDecimal, ResultValueInt, ResultValueString, ResultValueBool, ResultValueCurrency, CashFlowValue, CashFlowValueSet, ResultValueLifeCycleEventValue, ResultValueDateTimeOffset |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.ResultValueCurrency import ResultValueCurrency

instance = ResultValueCurrency(
    value="...",  # optional — The value itself
    result_value_type="..."  # required — The available values are: ResultValue, ResultValueDictionary, ResultValue0D, ResultValueDecimal, ResultValueInt, ResultValueString, ResultValueBool, ResultValueCurrency, CashFlowValue, CashFlowValueSet, ResultValueLifeCycleEventValue, ResultValueDateTimeOffset
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

