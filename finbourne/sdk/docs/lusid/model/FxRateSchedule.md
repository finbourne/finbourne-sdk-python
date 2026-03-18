# FxRateSchedule

Schedule to define fx conversion of cashflows on complex bonds. If an fx schedule is defined then  on payment schedule generation the coupon and principal payoffs will be wrapped in an fx rate payoff method.  Either the fx rate is predefined (fixed) or relies on fx resets (floating).  Used in representation of dual currency bond.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **flow_conventions** | [FlowConventions](FlowConventions.md) | Optional | *No description available.* |
| **fx_conversion_types** | **List[str]** | Optional | List of flags to indicate if coupon payments, principal payments or both are converted |
| **rate** | **float** | Optional | FxRate used to convert payments. Assumed to be in units of the ToCurrency so conversion is paymentAmount x fxRate |
| **to_currency** | **str** | Optional | Currency that payments are converted to |
| **schedule_type** | **str** | Required | The available values are: FixedSchedule, FloatSchedule, OptionalitySchedule, StepSchedule, Exercise, FxRateSchedule, FxLinkedNotionalSchedule, BondConversionSchedule, Invalid |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.FxRateSchedule import FxRateSchedule

instance = FxRateSchedule(
    flow_conventions=FlowConventions(...),  # optional
    fx_conversion_types=,  # optional — List of flags to indicate if coupon payments, principal payments or both are converted
    rate=0.0,  # optional — FxRate used to convert payments. Assumed to be in units of the ToCurrency so conversion is paymentAmount x fxRate
    to_currency="...",  # optional — Currency that payments are converted to
    schedule_type="..."  # required — The available values are: FixedSchedule, FloatSchedule, OptionalitySchedule, StepSchedule, Exercise, FxRateSchedule, FxLinkedNotionalSchedule, BondConversionSchedule, Invalid
)
```


## Related Models

- [FlowConventions](FlowConventions.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

