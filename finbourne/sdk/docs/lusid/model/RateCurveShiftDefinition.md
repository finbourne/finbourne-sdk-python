# RateCurveShiftDefinition

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **ccy** | **str** | Required | *No description available.* |
| **amount** | **float** | Required | *No description available.* |
| **start_tenor** | **str** | Optional | *No description available.* |
| **end_tenor** | **str** | Optional | *No description available.* |
| **shift_type** | **str** | Required | Available values: Parallel, Steepen, Flatten, Twist. |
| **scenario_shift_type** | **str** | Required | Available values: RateCurveShiftDefinition, FxShiftDefinition, EquityShiftDefinition, VolSurfaceShiftDefinition. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.RateCurveShiftDefinition import RateCurveShiftDefinition

instance = RateCurveShiftDefinition(
    ccy="...",  # required
    amount=0.0,  # required
    start_tenor="...",  # optional
    end_tenor="...",  # optional
    shift_type="...",  # required — Available values: Parallel, Steepen, Flatten, Twist.
    scenario_shift_type="..."  # required — Available values: RateCurveShiftDefinition, FxShiftDefinition, EquityShiftDefinition, VolSurfaceShiftDefinition.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

