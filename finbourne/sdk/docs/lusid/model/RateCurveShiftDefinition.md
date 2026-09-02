# RateCurveShiftDefinition

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **ccy** | **str** | Required | *No description available.* |
| **amount** | **float** | Optional | The size of the shift, in the units given by Scale: basis points by default (50 means +50bps),  or a percentage of each rate when Scale is Percentage (1 means rates scaled by 1.01). |
| **start_tenor** | **str** | Optional | *No description available.* |
| **end_tenor** | **str** | Optional | *No description available.* |
| **shift_type** | **str** | Required | Available values: Parallel, Steepen, Flatten, Twist, Tent. |
| **scale** | **str** | Optional | Available values: Bps, Percentage. |
| **apply_to** | **str** | Optional | A LUSID filter expression over the instrument entity scoping which instruments this shift is  for, e.g. \&quot;properties[Instrument/default/CountryOfIssue] eq &#39;Italy&#39;\&quot;. The shifted market data  is used by the whole valuation run, but when the scenario is requested as a result column the  column is only populated for matching instruments. Only usable when the scenario is applied as  a per-metric column. Note that with a scope set, the base and scenario columns cover different  instrument populations: an aggregate (e.g. Sum) of the scenario column totals only the matching  instruments, so it is not directly comparable to the same aggregate of the base column. |
| **pivot_tenor** | **str** | Optional | The tenor the Tent shift peaks at. The shift applies with the full Amount at this tenor,  falling linearly to zero at StartTenor and EndTenor - the key-rate triangle shape, whose  asymmetry matters because key-rate buckets are rarely evenly spaced. Only valid with  ShiftType Tent; omitted, a Tent peaks at the midpoint of the window. Declared last on  purpose: generated SDKs emit their positional constructor in property-declaration order,  and this property must not shift the parameters of the ones before it.  Over a window containing a single curve point, that point takes the full Amount regardless  of where the pivot lands: a one-point window has no slope to express, and every shift  shape degenerates the same way there. |
| **scenario_shift_type** | **str** | Required | Available values: RateCurveShiftDefinition, FxShiftDefinition, PriceShiftDefinition, VolSurfaceShiftDefinition, MdkrGroupShiftDefinition, InflationCurveShiftDefinition. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.RateCurveShiftDefinition import RateCurveShiftDefinition

instance = RateCurveShiftDefinition(
    ccy="...",  # required
    amount=0.0,  # optional — The size of the shift, in the units given by Scale: basis points by default (50 means +50bps),  or a percentage of each rate when Scale is Percentage (1 means rates scaled by 1.01).
    start_tenor="...",  # optional
    end_tenor="...",  # optional
    shift_type="...",  # required — Available values: Parallel, Steepen, Flatten, Twist, Tent.
    scale="...",  # optional — Available values: Bps, Percentage.
    apply_to="...",  # optional — A LUSID filter expression over the instrument entity scoping which instruments this shift is  for, e.g. \&quot;properties[Instrument/default/CountryOfIssue] eq &#39;Italy&#39;\&quot;. The shifted market data  is used by the whole valuation run, but when the scenario is requested as a result column the  column is only populated for matching instruments. Only usable when the scenario is applied as  a per-metric column. Note that with a scope set, the base and scenario columns cover different  instrument populations: an aggregate (e.g. Sum) of the scenario column totals only the matching  instruments, so it is not directly comparable to the same aggregate of the base column.
    pivot_tenor="...",  # optional — The tenor the Tent shift peaks at. The shift applies with the full Amount at this tenor,  falling linearly to zero at StartTenor and EndTenor - the key-rate triangle shape, whose  asymmetry matters because key-rate buckets are rarely evenly spaced. Only valid with  ShiftType Tent; omitted, a Tent peaks at the midpoint of the window. Declared last on  purpose: generated SDKs emit their positional constructor in property-declaration order,  and this property must not shift the parameters of the ones before it.  Over a window containing a single curve point, that point takes the full Amount regardless  of where the pivot lands: a one-point window has no slope to express, and every shift  shape degenerates the same way there.
    scenario_shift_type="..."  # required — Available values: RateCurveShiftDefinition, FxShiftDefinition, PriceShiftDefinition, VolSurfaceShiftDefinition, MdkrGroupShiftDefinition, InflationCurveShiftDefinition.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

