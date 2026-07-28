# VolSurfaceShiftDefinition

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **instrument** | **str** | Required | *No description available.* |
| **amount** | **float** | Required | *No description available.* |
| **strike** | **float** | Optional | *No description available.* |
| **expiry** | **str** | Optional | *No description available.* |
| **shift_type** | **str** | Required | Available values: Absolute, Relative. |
| **scenario_shift_type** | **str** | Required | Available values: RateCurveShiftDefinition, FxShiftDefinition, EquityShiftDefinition, VolSurfaceShiftDefinition. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.VolSurfaceShiftDefinition import VolSurfaceShiftDefinition

instance = VolSurfaceShiftDefinition(
    instrument="...",  # required
    amount=0.0,  # required
    strike=0.0,  # optional
    expiry="...",  # optional
    shift_type="...",  # required — Available values: Absolute, Relative.
    scenario_shift_type="..."  # required — Available values: RateCurveShiftDefinition, FxShiftDefinition, EquityShiftDefinition, VolSurfaceShiftDefinition.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

