# EquityShiftDefinition

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **instrument** | **str** | Required | *No description available.* |
| **amount** | **float** | Required | *No description available.* |
| **shift_type** | **str** | Required | Available values: Absolute, Relative, Percentage. |
| **scenario_shift_type** | **str** | Required | Available values: RateCurveShiftDefinition, FxShiftDefinition, EquityShiftDefinition, VolSurfaceShiftDefinition, MdkrGroupShiftDefinition. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.EquityShiftDefinition import EquityShiftDefinition

instance = EquityShiftDefinition(
    instrument="...",  # required
    amount=0.0,  # required
    shift_type="...",  # required — Available values: Absolute, Relative, Percentage.
    scenario_shift_type="..."  # required — Available values: RateCurveShiftDefinition, FxShiftDefinition, EquityShiftDefinition, VolSurfaceShiftDefinition, MdkrGroupShiftDefinition.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

