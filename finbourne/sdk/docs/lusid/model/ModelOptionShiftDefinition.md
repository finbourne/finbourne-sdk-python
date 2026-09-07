# ModelOptionShiftDefinition

A shift of a pricing model option for the duration of the scenario. Unlike every other shift  type, the target is not a piece of market data: it is a field of the model options carried by  the recipe's model rule (for example the short-rate volatility of the Hull-White one-factor  lattice), which no market data shift can reach because a model option is configuration, not a  resolved market element. The shift is scoped to a model rule by the model's name, optionally  narrowed to one instrument type, and applies to every instrument that rule prices.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **model_name** | **str** | Required | The pricing model whose options this shift targets, exactly as named on the recipe&#39;s model  rule, e.g. \&quot;HullWhite1F\&quot;. Only models with shiftable options are accepted; an unknown or  unsupported model name is rejected when the scenario is stored. |
| **instrument_type** | **str** | Optional | The instrument type narrowing which of the model&#39;s rules the shift applies to, matching the  instrument-type addressing of model rules in the recipe, e.g. \&quot;ComplexBond\&quot;. Omitted, the  shift applies to every instrument the named model prices. |
| **option_name** | **str** | Required | The model option field the shift moves, e.g. \&quot;Volatility\&quot; or \&quot;MeanReversion\&quot; for  HullWhite1F. Only a whitelisted set of options per model is shiftable; an unknown option  name is rejected when the scenario is stored. |
| **ccy** | **str** | Optional | For options carrying per-currency overrides (e.g. HullWhite1F&#39;s VolatilityByCurrency): the  ISO currency code whose effective value the shift moves. The shifted entry starts from the  existing override for that currency, or from the scalar option where no override exists.  Omitted, the shift moves the scalar option and every per-currency override together, so the  effective value moves for every instrument regardless of which level supplies it. |
| **amount** | **float** | Optional | The size of the shift, in the units given by ShiftType: the option&#39;s own units for Absolute  (0.0010 on a volatility of 0.008 is ten basis points of annualised volatility), or a  fraction of the configured value for Relative (0.1 raises it by ten percent). |
| **shift_type** | **str** | Required | Available values: Absolute, Relative. |
| **scenario_shift_type** | **str** | Required | Available values: RateCurveShiftDefinition, FxShiftDefinition, PriceShiftDefinition, VolSurfaceShiftDefinition, MdkrGroupShiftDefinition, InflationCurveShiftDefinition, CreditSpreadShiftDefinition, ModelOptionShiftDefinition. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.ModelOptionShiftDefinition import ModelOptionShiftDefinition

instance = ModelOptionShiftDefinition(
    model_name="...",  # required — The pricing model whose options this shift targets, exactly as named on the recipe&#39;s model  rule, e.g. \&quot;HullWhite1F\&quot;. Only models with shiftable options are accepted; an unknown or  unsupported model name is rejected when the scenario is stored.
    instrument_type="...",  # optional — The instrument type narrowing which of the model&#39;s rules the shift applies to, matching the  instrument-type addressing of model rules in the recipe, e.g. \&quot;ComplexBond\&quot;. Omitted, the  shift applies to every instrument the named model prices.
    option_name="...",  # required — The model option field the shift moves, e.g. \&quot;Volatility\&quot; or \&quot;MeanReversion\&quot; for  HullWhite1F. Only a whitelisted set of options per model is shiftable; an unknown option  name is rejected when the scenario is stored.
    ccy="...",  # optional — For options carrying per-currency overrides (e.g. HullWhite1F&#39;s VolatilityByCurrency): the  ISO currency code whose effective value the shift moves. The shifted entry starts from the  existing override for that currency, or from the scalar option where no override exists.  Omitted, the shift moves the scalar option and every per-currency override together, so the  effective value moves for every instrument regardless of which level supplies it.
    amount=0.0,  # optional — The size of the shift, in the units given by ShiftType: the option&#39;s own units for Absolute  (0.0010 on a volatility of 0.008 is ten basis points of annualised volatility), or a  fraction of the configured value for Relative (0.1 raises it by ten percent).
    shift_type="...",  # required — Available values: Absolute, Relative.
    scenario_shift_type="..."  # required — Available values: RateCurveShiftDefinition, FxShiftDefinition, PriceShiftDefinition, VolSurfaceShiftDefinition, MdkrGroupShiftDefinition, InflationCurveShiftDefinition, CreditSpreadShiftDefinition, ModelOptionShiftDefinition.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

