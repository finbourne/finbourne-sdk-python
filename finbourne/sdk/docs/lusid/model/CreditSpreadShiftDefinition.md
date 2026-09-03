# CreditSpreadShiftDefinition

A shift of a credit spread curve, targeted by the ticker of the reference entity and,  optionally, the currency the curve is quoted in. The shift applies to the par spread quotes  the curve carries, so a basis-point amount means basis points of spread - the units a spread  shock is quoted in. Shift shapes, tenor windows, scales and the Tent pivot behave exactly as  they do on a rate curve shift.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **ticker** | **str** | Required | The ticker of the reference entity whose spread curve is shifted. |
| **ccy** | **str** | Optional | The currency the curve is quoted in; disambiguates a ticker quoted in more than one  currency. Omitted, the shift matches the ticker in every currency. |
| **amount** | **float** | Optional | The size of the shift, in the units given by Scale: basis points of spread by default  (50 means +50bps), or a percentage of each spread when Scale is Percentage (1 means  spreads scaled by 1.01). |
| **start_tenor** | **str** | Optional | *No description available.* |
| **end_tenor** | **str** | Optional | *No description available.* |
| **shift_type** | **str** | Required | Available values: Parallel, Steepen, Flatten, Twist, Tent. |
| **scale** | **str** | Optional | Available values: Bps, Percentage. |
| **pivot_tenor** | **str** | Optional | The tenor the Tent shift peaks at. The shift applies with the full Amount at this tenor,  falling linearly to zero at StartTenor and EndTenor - the key-rate triangle shape. Only  valid with ShiftType Tent; omitted, a Tent peaks at the midpoint of the window. Declared  last on purpose: generated SDKs emit their positional constructor in property-declaration  order, and this property must not shift the parameters of the ones before it. |
| **scenario_shift_type** | **str** | Required | Available values: RateCurveShiftDefinition, FxShiftDefinition, PriceShiftDefinition, VolSurfaceShiftDefinition, MdkrGroupShiftDefinition, InflationCurveShiftDefinition, CreditSpreadShiftDefinition. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.CreditSpreadShiftDefinition import CreditSpreadShiftDefinition

instance = CreditSpreadShiftDefinition(
    ticker="...",  # required — The ticker of the reference entity whose spread curve is shifted.
    ccy="...",  # optional — The currency the curve is quoted in; disambiguates a ticker quoted in more than one  currency. Omitted, the shift matches the ticker in every currency.
    amount=0.0,  # optional — The size of the shift, in the units given by Scale: basis points of spread by default  (50 means +50bps), or a percentage of each spread when Scale is Percentage (1 means  spreads scaled by 1.01).
    start_tenor="...",  # optional
    end_tenor="...",  # optional
    shift_type="...",  # required — Available values: Parallel, Steepen, Flatten, Twist, Tent.
    scale="...",  # optional — Available values: Bps, Percentage.
    pivot_tenor="...",  # optional — The tenor the Tent shift peaks at. The shift applies with the full Amount at this tenor,  falling linearly to zero at StartTenor and EndTenor - the key-rate triangle shape. Only  valid with ShiftType Tent; omitted, a Tent peaks at the midpoint of the window. Declared  last on purpose: generated SDKs emit their positional constructor in property-declaration  order, and this property must not shift the parameters of the ones before it.
    scenario_shift_type="..."  # required — Available values: RateCurveShiftDefinition, FxShiftDefinition, PriceShiftDefinition, VolSurfaceShiftDefinition, MdkrGroupShiftDefinition, InflationCurveShiftDefinition, CreditSpreadShiftDefinition.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

