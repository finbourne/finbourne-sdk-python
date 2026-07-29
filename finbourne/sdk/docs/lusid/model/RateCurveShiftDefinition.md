# RateCurveShiftDefinition

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **ccy** | **str** | Required | *No description available.* |
| **amount** | **float** | Required | The size of the shift, in the units given by Scale: basis points by default (50 means +50bps),  or a percentage of each rate when Scale is Percentage (1 means rates scaled by 1.01). |
| **start_tenor** | **str** | Optional | *No description available.* |
| **end_tenor** | **str** | Optional | *No description available.* |
| **shift_type** | **str** | Required | Available values: Parallel, Steepen, Flatten, Twist. |
| **scale** | **str** | Optional | Available values: Bps, Percentage. |
| **scenario_shift_type** | **str** | Required | Available values: RateCurveShiftDefinition, FxShiftDefinition, EquityShiftDefinition, VolSurfaceShiftDefinition. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.RateCurveShiftDefinition import RateCurveShiftDefinition

instance = RateCurveShiftDefinition(
    ccy="...",  # required
    amount=0.0,  # required — The size of the shift, in the units given by Scale: basis points by default (50 means +50bps),  or a percentage of each rate when Scale is Percentage (1 means rates scaled by 1.01).
    start_tenor="...",  # optional
    end_tenor="...",  # optional
    shift_type="...",  # required — Available values: Parallel, Steepen, Flatten, Twist.
    scale="...",  # optional — Available values: Bps, Percentage.
    scenario_shift_type="..."  # required — Available values: RateCurveShiftDefinition, FxShiftDefinition, EquityShiftDefinition, VolSurfaceShiftDefinition.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

