# InflationCurveShiftDefinition

A shift of an inflation curve, targeted by inflation index name. The shift applies to the  zero-coupon inflation swap quotes the curve was solved from and the curve re-solves with  the same seasonal factors and resolved fixings, so seasonality and the historic index path  survive the shift. Shift shapes, tenor windows, scales and the Tent pivot behave exactly  as they do on a rate curve shift.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **index** | **str** | Required | The inflation index name the curve is keyed by, e.g. UKRPI or EUHICPXT. |
| **amount** | **float** | Optional | The size of the shift, in the units given by Scale: basis points on the zero-coupon  rates by default (50 means +50bps), or a percentage of each rate when Scale is  Percentage (1 means rates scaled by 1.01). |
| **start_tenor** | **str** | Optional | *No description available.* |
| **end_tenor** | **str** | Optional | *No description available.* |
| **shift_type** | **str** | Required | Available values: Parallel, Steepen, Flatten, Twist, Tent. |
| **scale** | **str** | Optional | Available values: Bps, Percentage. |
| **pivot_tenor** | **str** | Optional | The tenor the Tent shift peaks at. The shift applies with the full Amount at this tenor,  falling linearly to zero at StartTenor and EndTenor - the key-rate triangle shape. Only  valid with ShiftType Tent; omitted, a Tent peaks at the midpoint of the window. Declared  last on purpose: generated SDKs emit their positional constructor in property-declaration  order, and this property must not shift the parameters of the ones before it. |
| **scenario_shift_type** | **str** | Required | Available values: RateCurveShiftDefinition, FxShiftDefinition, PriceShiftDefinition, VolSurfaceShiftDefinition, MdkrGroupShiftDefinition, InflationCurveShiftDefinition. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.InflationCurveShiftDefinition import InflationCurveShiftDefinition

instance = InflationCurveShiftDefinition(
    index="...",  # required — The inflation index name the curve is keyed by, e.g. UKRPI or EUHICPXT.
    amount=0.0,  # optional — The size of the shift, in the units given by Scale: basis points on the zero-coupon  rates by default (50 means +50bps), or a percentage of each rate when Scale is  Percentage (1 means rates scaled by 1.01).
    start_tenor="...",  # optional
    end_tenor="...",  # optional
    shift_type="...",  # required — Available values: Parallel, Steepen, Flatten, Twist, Tent.
    scale="...",  # optional — Available values: Bps, Percentage.
    pivot_tenor="...",  # optional — The tenor the Tent shift peaks at. The shift applies with the full Amount at this tenor,  falling linearly to zero at StartTenor and EndTenor - the key-rate triangle shape. Only  valid with ShiftType Tent; omitted, a Tent peaks at the midpoint of the window. Declared  last on purpose: generated SDKs emit their positional constructor in property-declaration  order, and this property must not shift the parameters of the ones before it.
    scenario_shift_type="..."  # required — Available values: RateCurveShiftDefinition, FxShiftDefinition, PriceShiftDefinition, VolSurfaceShiftDefinition, MdkrGroupShiftDefinition, InflationCurveShiftDefinition.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

