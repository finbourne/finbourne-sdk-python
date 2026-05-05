# CurveOptions

Options for configuring how ComplexMarketData representing a 'curve' is interpreted.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **day_count_convention** | **str** | Optional | Day count convention of the curve. Default value: Act360. Available values: Actual360, Act360, MoneyMarket, Actual365, Act365, Thirty360, ThirtyU360, Bond, ThirtyE360, EuroBond, ActualActual, ActAct, ActActIsda, ActActIsma, ActActIcma, OneOne, Act364, Act365F, Act365L, Act365_25, Act252, Bus252, NL360, NL365, ActActAFB, Act365Cad, ThirtyActIsda, Thirty365Isda, ThirtyEActIsda, ThirtyE360Isda, ThirtyE365Isda, ThirtyU360EOM, Invalid. |
| **front_extrapolation_type** | **str** | Optional | What type of extrapolation is used to build the curve  Imagine that the curve is facing the observer(you), then the \&quot;front\&quot; direction is the closest point on the curve onward.    example: 0D tenor to past  Default value: Flat. Available values: None, Flat, Linear. |
| **back_extrapolation_type** | **str** | Optional | What type of extrapolation is used to build the curve.    Imagine that the curve is facing the observer(you), then the \&quot;back\&quot; direction is the furthest point on the curve onward.  example: 30Y tenor to infinity    Default value: Flat. Available values: None, Flat, Linear. |
| **market_data_options_type** | **str** | Required | Available values: CurveOptions. Available values: CurveOptions. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.CurveOptions import CurveOptions

instance = CurveOptions(
    day_count_convention="...",  # optional — Day count convention of the curve. Default value: Act360. Available values: Actual360, Act360, MoneyMarket, Actual365, Act365, Thirty360, ThirtyU360, Bond, ThirtyE360, EuroBond, ActualActual, ActAct, ActActIsda, ActActIsma, ActActIcma, OneOne, Act364, Act365F, Act365L, Act365_25, Act252, Bus252, NL360, NL365, ActActAFB, Act365Cad, ThirtyActIsda, Thirty365Isda, ThirtyEActIsda, ThirtyE360Isda, ThirtyE365Isda, ThirtyU360EOM, Invalid.
    front_extrapolation_type="...",  # optional — What type of extrapolation is used to build the curve  Imagine that the curve is facing the observer(you), then the \&quot;front\&quot; direction is the closest point on the curve onward.    example: 0D tenor to past  Default value: Flat. Available values: None, Flat, Linear.
    back_extrapolation_type="...",  # optional — What type of extrapolation is used to build the curve.    Imagine that the curve is facing the observer(you), then the \&quot;back\&quot; direction is the furthest point on the curve onward.  example: 30Y tenor to infinity    Default value: Flat. Available values: None, Flat, Linear.
    market_data_options_type="..."  # required — Available values: CurveOptions. Available values: CurveOptions.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

