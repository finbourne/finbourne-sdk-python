# CashFlowValueSet

Result value for a collection of cash flow values
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **cashflows** | [List[CashFlowValue]](CashFlowValue.md) | Optional | The set of cash flows in the result |
| **result_value_type** | **str** | Required | The available values are: ResultValue, ResultValueDictionary, ResultValue0D, ResultValueDecimal, ResultValueInt, ResultValueString, ResultValueBool, ResultValueCurrency, CashFlowValue, CashFlowValueSet, ResultValueLifeCycleEventValue, ResultValueDateTimeOffset |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.CashFlowValueSet import CashFlowValueSet

instance = CashFlowValueSet(
    cashflows=[],  # optional — The set of cash flows in the result
    result_value_type="..."  # required — The available values are: ResultValue, ResultValueDictionary, ResultValue0D, ResultValueDecimal, ResultValueInt, ResultValueString, ResultValueBool, ResultValueCurrency, CashFlowValue, CashFlowValueSet, ResultValueLifeCycleEventValue, ResultValueDateTimeOffset
)
```


## Related Models

- [CashFlowValue](CashFlowValue.md) — used in `cashflows`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

