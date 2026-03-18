# ResultValueDictionary

Result value for a collection of key-value pairs. Used for diagnostics associated to a cash flow, etc.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **elements** | [Dict[str, ResultValue]](ResultValue.md) | Optional | The dictionary elements |
| **result_value_type** | **str** | Required | The available values are: ResultValue, ResultValueDictionary, ResultValue0D, ResultValueDecimal, ResultValueInt, ResultValueString, ResultValueBool, ResultValueCurrency, CashFlowValue, CashFlowValueSet, ResultValueLifeCycleEventValue, ResultValueDateTimeOffset |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.ResultValueDictionary import ResultValueDictionary

instance = ResultValueDictionary(
    elements=ResultValue(...),  # optional — The dictionary elements
    result_value_type="..."  # required — The available values are: ResultValue, ResultValueDictionary, ResultValue0D, ResultValueDecimal, ResultValueInt, ResultValueString, ResultValueBool, ResultValueCurrency, CashFlowValue, CashFlowValueSet, ResultValueLifeCycleEventValue, ResultValueDateTimeOffset
)
```


## Related Models

- [ResultValue](ResultValue.md) — used in `elements`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

