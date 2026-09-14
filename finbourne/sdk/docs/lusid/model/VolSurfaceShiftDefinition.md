# VolSurfaceShiftDefinition

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **instrument** | **str** | Required | The market-data descriptor of the surfaces to shift, not an instrument identifier such as a LUID.  For an equity vol surface this is the underlier code the surface was mastered against (e.g. &#39;TSLA&#39;  for market asset &#39;TSLA/USD/LN&#39;); for an interest rate vol surface it is the currency (e.g. &#39;USD&#39;);  for an FX vol surface it is the currency pair (e.g. &#39;GBP/USD&#39;). The wildcard &#39;EquityVol.*&#39; widens  the shift to every equity vol surface in the valuation; interest rate and FX vol surfaces cannot  be widened, since neither a currency nor a currency pair names a set of instruments. |
| **amount** | **float** | Optional | *No description available.* |
| **strike** | **float** | Optional | *No description available.* |
| **expiry** | **str** | Optional | The expiry of the surface points the shift applies to, resolved against the valuation  date. A whole number of units, in any case: BD (business day), D, W, M, Q or Qtr, SA  (semi-annual), Y or A - for example \&quot;1BD\&quot;, \&quot;3m\&quot;, \&quot;6M\&quot;, \&quot;1Qtr\&quot;, \&quot;5y\&quot;. Omitted, every  expiry on the surface is shifted. |
| **shift_type** | **str** | Required | Available values: Absolute, Relative. |
| **scenario_shift_type** | **str** | Required | Available values: RateCurveShiftDefinition, FxShiftDefinition, PriceShiftDefinition, VolSurfaceShiftDefinition, MdkrGroupShiftDefinition, InflationCurveShiftDefinition, CreditSpreadShiftDefinition, ModelOptionShiftDefinition. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.VolSurfaceShiftDefinition import VolSurfaceShiftDefinition

instance = VolSurfaceShiftDefinition(
    instrument="...",  # required — The market-data descriptor of the surfaces to shift, not an instrument identifier such as a LUID.  For an equity vol surface this is the underlier code the surface was mastered against (e.g. &#39;TSLA&#39;  for market asset &#39;TSLA/USD/LN&#39;); for an interest rate vol surface it is the currency (e.g. &#39;USD&#39;);  for an FX vol surface it is the currency pair (e.g. &#39;GBP/USD&#39;). The wildcard &#39;EquityVol.*&#39; widens  the shift to every equity vol surface in the valuation; interest rate and FX vol surfaces cannot  be widened, since neither a currency nor a currency pair names a set of instruments.
    amount=0.0,  # optional
    strike=0.0,  # optional
    expiry="...",  # optional — The expiry of the surface points the shift applies to, resolved against the valuation  date. A whole number of units, in any case: BD (business day), D, W, M, Q or Qtr, SA  (semi-annual), Y or A - for example \&quot;1BD\&quot;, \&quot;3m\&quot;, \&quot;6M\&quot;, \&quot;1Qtr\&quot;, \&quot;5y\&quot;. Omitted, every  expiry on the surface is shifted.
    shift_type="...",  # required — Available values: Absolute, Relative.
    scenario_shift_type="..."  # required — Available values: RateCurveShiftDefinition, FxShiftDefinition, PriceShiftDefinition, VolSurfaceShiftDefinition, MdkrGroupShiftDefinition, InflationCurveShiftDefinition, CreditSpreadShiftDefinition, ModelOptionShiftDefinition.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

