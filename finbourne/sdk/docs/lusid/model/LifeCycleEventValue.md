# LifeCycleEventValue

The instrument life cycle event result value type
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **effective_date** | **datetime** | Optional | The effective date of the event |
| **event_values** | [ResultValueDictionary](ResultValueDictionary.md) | Optional | *No description available.* |
| **event_lineage** | [LifeCycleEventLineage](LifeCycleEventLineage.md) | Optional | *No description available.* |
| **result_value_type** | **str** | Required | The available values are: ResultValue, ResultValueDictionary, ResultValue0D, ResultValueDecimal, ResultValueInt, ResultValueString, ResultValueBool, ResultValueCurrency, CashFlowValue, CashFlowValueSet, ResultValueLifeCycleEventValue, ResultValueDateTimeOffset |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.LifeCycleEventValue import LifeCycleEventValue

instance = LifeCycleEventValue(
    effective_date=datetime.now(),  # optional — The effective date of the event
    event_values=ResultValueDictionary(...),  # optional
    event_lineage=LifeCycleEventLineage(...),  # optional
    result_value_type="..."  # required — The available values are: ResultValue, ResultValueDictionary, ResultValue0D, ResultValueDecimal, ResultValueInt, ResultValueString, ResultValueBool, ResultValueCurrency, CashFlowValue, CashFlowValueSet, ResultValueLifeCycleEventValue, ResultValueDateTimeOffset
)
```

- [ResultValueDictionary](ResultValueDictionary.md)
- [LifeCycleEventLineage](LifeCycleEventLineage.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

