# ReconciliationBreak

A reconciliation break
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **instrument_scope** | **str** | Optional | The scope in which the instrument lies. |
| **instrument_uid** | **str** | Required | Unique instrument identifier |
| **sub_holding_keys** | [Dict[str, PerpetualProperty]](PerpetualProperty.md) | Required | Any other properties that comprise the Sub-Holding Key |
| **left_units** | **float** | Required | Units from the left hand side |
| **right_units** | **float** | Required | Units from the right hand side |
| **difference_units** | **float** | Required | Difference in units |
| **left_cost** | [CurrencyAndAmount](CurrencyAndAmount.md) | Required | *No description available.* |
| **right_cost** | [CurrencyAndAmount](CurrencyAndAmount.md) | Required | *No description available.* |
| **difference_cost** | [CurrencyAndAmount](CurrencyAndAmount.md) | Required | *No description available.* |
| **instrument_properties** | [List[ModelProperty]](ModelProperty.md) | Required | Additional features relating to the instrument |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.ReconciliationBreak import ReconciliationBreak

instance = ReconciliationBreak(
    instrument_scope="...",  # optional — The scope in which the instrument lies.
    instrument_uid="...",  # required — Unique instrument identifier
    sub_holding_keys=PerpetualProperty(...),  # required — Any other properties that comprise the Sub-Holding Key
    left_units=0.0,  # required — Units from the left hand side
    right_units=0.0,  # required — Units from the right hand side
    difference_units=0.0,  # required — Difference in units
    left_cost=CurrencyAndAmount(...),  # required
    right_cost=CurrencyAndAmount(...),  # required
    difference_cost=CurrencyAndAmount(...),  # required
    instrument_properties=[]  # required — Additional features relating to the instrument
)
```

- [PerpetualProperty](PerpetualProperty.md) — used in `sub_holding_keys`
- [CurrencyAndAmount](CurrencyAndAmount.md)
- [CurrencyAndAmount](CurrencyAndAmount.md)
- [CurrencyAndAmount](CurrencyAndAmount.md)
- [ModelProperty](ModelProperty.md) — used in `instrument_properties`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

