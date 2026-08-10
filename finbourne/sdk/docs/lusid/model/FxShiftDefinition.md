# FxShiftDefinition

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **currency_pair** | **str** | Required | *No description available.* |
| **amount** | **float** | Optional | *No description available.* |
| **shift_type** | **str** | Required | Available values: Absolute, Relative, Percentage. |
| **scenario_shift_type** | **str** | Required | Available values: RateCurveShiftDefinition, FxShiftDefinition, PriceShiftDefinition, VolSurfaceShiftDefinition, MdkrGroupShiftDefinition. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.FxShiftDefinition import FxShiftDefinition

instance = FxShiftDefinition(
    currency_pair="...",  # required
    amount=0.0,  # optional
    shift_type="...",  # required — Available values: Absolute, Relative, Percentage.
    scenario_shift_type="..."  # required — Available values: RateCurveShiftDefinition, FxShiftDefinition, PriceShiftDefinition, VolSurfaceShiftDefinition, MdkrGroupShiftDefinition.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

