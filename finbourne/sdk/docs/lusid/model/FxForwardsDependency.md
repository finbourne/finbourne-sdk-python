# FxForwardsDependency

Indicates a dependency on an FxForwardCurve.  Identical to Fx dependencies in the meaning of domestic and foreign currencies, but describes a *set* of fx rates.  These rates are quoted rates for fx forwards, which can be used to interpolate the forward rate at a specific time in the future.  In the case of pips, the absolute rates can be expressed as rate = spotFx + pips / pipsPerUnit
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **domestic_currency** | **str** | Required | DomesticCurrency is the first currency in a currency pair quote e.g. eur-gbp, eur is the domestic currency. |
| **foreign_currency** | **str** | Required | ForeignCurrency is the second currency in a currency pair quote e.g. eur-gbp, gbp is the foreign currency. |
| **curve_type** | **str** | Required | Used to describe the format in which the curve is expressed  e.g. FxFwdCurve (general term to describe any representation), TenorFxFwdCurve, PipsFxFwdCurve. |
| **var_date** | **datetime** | Required | The effectiveDate of the entity that this is a dependency for.  Unless there is an obvious date this should be, like for a historic reset, then this is the valuation date. |
| **dependency_type** | **str** | Required | The available values are: OpaqueDependency, CashDependency, DiscountingDependency, EquityCurveDependency, EquityVolDependency, FxDependency, FxForwardsDependency, FxVolDependency, IndexProjectionDependency, IrVolDependency, QuoteDependency, Vendor, CalendarDependency, InflationFixingDependency |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.FxForwardsDependency import FxForwardsDependency

instance = FxForwardsDependency(
    domestic_currency="...",  # required — DomesticCurrency is the first currency in a currency pair quote e.g. eur-gbp, eur is the domestic currency.
    foreign_currency="...",  # required — ForeignCurrency is the second currency in a currency pair quote e.g. eur-gbp, gbp is the foreign currency.
    curve_type="...",  # required — Used to describe the format in which the curve is expressed  e.g. FxFwdCurve (general term to describe any representation), TenorFxFwdCurve, PipsFxFwdCurve.
    var_date=datetime.now(),  # required — The effectiveDate of the entity that this is a dependency for.  Unless there is an obvious date this should be, like for a historic reset, then this is the valuation date.
    dependency_type="..."  # required — The available values are: OpaqueDependency, CashDependency, DiscountingDependency, EquityCurveDependency, EquityVolDependency, FxDependency, FxForwardsDependency, FxVolDependency, IndexProjectionDependency, IrVolDependency, QuoteDependency, Vendor, CalendarDependency, InflationFixingDependency
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

