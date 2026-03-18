# FxVolDependency

Economic dependency required to price FX derivative products that contain optionality.  FX Vol surface is a grid of implied volatilities for an array of strikes and tenors,  derived from vanilla option prices in the market.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **domestic_currency** | **str** | Required | DomesticCurrency is the first currency in a currency pair quote e.g. eur-gbp, eur is the domestic currency. |
| **foreign_currency** | **str** | Required | ForeignCurrency is the second currency in a currency pair quote e.g. eur-gbp, gbp is the foreign currency. |
| **vol_type** | **str** | Required | Volatility type e.g. \&quot;LN\&quot; and \&quot;N\&quot; for log-normal and normal volatility. |
| **var_date** | **datetime** | Required | The effectiveDate of the entity that this is a dependency for.  Unless there is an obvious date this should be, like for a historic reset, then this is the valuation date. |
| **dependency_type** | **str** | Required | The available values are: OpaqueDependency, CashDependency, DiscountingDependency, EquityCurveDependency, EquityVolDependency, FxDependency, FxForwardsDependency, FxVolDependency, IndexProjectionDependency, IrVolDependency, QuoteDependency, Vendor, CalendarDependency, InflationFixingDependency |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.FxVolDependency import FxVolDependency

instance = FxVolDependency(
    domestic_currency="...",  # required — DomesticCurrency is the first currency in a currency pair quote e.g. eur-gbp, eur is the domestic currency.
    foreign_currency="...",  # required — ForeignCurrency is the second currency in a currency pair quote e.g. eur-gbp, gbp is the foreign currency.
    vol_type="...",  # required — Volatility type e.g. \&quot;LN\&quot; and \&quot;N\&quot; for log-normal and normal volatility.
    var_date=datetime.now(),  # required — The effectiveDate of the entity that this is a dependency for.  Unless there is an obvious date this should be, like for a historic reset, then this is the valuation date.
    dependency_type="..."  # required — The available values are: OpaqueDependency, CashDependency, DiscountingDependency, EquityCurveDependency, EquityVolDependency, FxDependency, FxForwardsDependency, FxVolDependency, IndexProjectionDependency, IrVolDependency, QuoteDependency, Vendor, CalendarDependency, InflationFixingDependency
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

