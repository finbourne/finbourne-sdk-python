# VolCubeOptions

Options for configuring how an IrVolCubeData is interpreted.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **day_count_convention** | **str** | Optional | Day count convention the vols are quoted on. The cube places its expiry pillars on it, and a swaption priced off  the cube measures its time to expiry on it. Supported values: Actual360, Actual365, Act365F, Act365_25 and  ActualActual, or their aliases Act360, MoneyMarket, Act365, ActAct and ActActIsda. Default value: ActualActual. Available values: Actual360, Act360, MoneyMarket, Actual365, Act365, Thirty360, ThirtyU360, Bond, ThirtyE360, EuroBond, ActualActual, ActAct, ActActIsda, ActActIcma, ActActIsma, OneOne, Act364, Act365F, Act365L, Act365_25, Act252, Bus252, NL360, NL365, ActActAFB, Act365Cad, ThirtyActIsda, Thirty365Isda, ThirtyEActIsda, ThirtyE360Isda, ThirtyE365Isda, ThirtyU360EOM, Invalid. |
| **market_data_options_type** | **str** | Required | Available values: CurveOptions, VolCubeOptions. Available values: CurveOptions, VolCubeOptions. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.VolCubeOptions import VolCubeOptions

instance = VolCubeOptions(
    day_count_convention="...",  # optional — Day count convention the vols are quoted on. The cube places its expiry pillars on it, and a swaption priced off  the cube measures its time to expiry on it. Supported values: Actual360, Actual365, Act365F, Act365_25 and  ActualActual, or their aliases Act360, MoneyMarket, Act365, ActAct and ActActIsda. Default value: ActualActual. Available values: Actual360, Act360, MoneyMarket, Actual365, Act365, Thirty360, ThirtyU360, Bond, ThirtyE360, EuroBond, ActualActual, ActAct, ActActIsda, ActActIcma, ActActIsma, OneOne, Act364, Act365F, Act365L, Act365_25, Act252, Bus252, NL360, NL365, ActActAFB, Act365Cad, ThirtyActIsda, Thirty365Isda, ThirtyEActIsda, ThirtyE360Isda, ThirtyE365Isda, ThirtyU360EOM, Invalid.
    market_data_options_type="..."  # required — Available values: CurveOptions, VolCubeOptions. Available values: CurveOptions, VolCubeOptions.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

