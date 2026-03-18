# CashFlowValue

Result class for a cash flow value
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **payment_date** | **datetime** | Required | The payment date of the cash flow |
| **diagnostics** | [ResultValueDictionary](ResultValueDictionary.md) | Optional | *No description available.* |
| **cash_flow_lineage** | [CashFlowLineage](CashFlowLineage.md) | Optional | *No description available.* |
| **payment_amount** | **float** | Required | The amount paid or received |
| **payment_ccy** | **str** | Required | The currency of the transaction |
| **result_value_type** | **str** | Required | The available values are: ResultValue, ResultValueDictionary, ResultValue0D, ResultValueDecimal, ResultValueInt, ResultValueString, ResultValueBool, ResultValueCurrency, CashFlowValue, CashFlowValueSet, ResultValueLifeCycleEventValue, ResultValueDateTimeOffset |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.CashFlowValue import CashFlowValue

instance = CashFlowValue(
    payment_date=datetime.now(),  # required — The payment date of the cash flow
    diagnostics=ResultValueDictionary(...),  # optional
    cash_flow_lineage=CashFlowLineage(...),  # optional
    payment_amount=0.0,  # required — The amount paid or received
    payment_ccy="...",  # required — The currency of the transaction
    result_value_type="..."  # required — The available values are: ResultValue, ResultValueDictionary, ResultValue0D, ResultValueDecimal, ResultValueInt, ResultValueString, ResultValueBool, ResultValueCurrency, CashFlowValue, CashFlowValueSet, ResultValueLifeCycleEventValue, ResultValueDateTimeOffset
)
```

- [ResultValueDictionary](ResultValueDictionary.md)
- [CashFlowLineage](CashFlowLineage.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

