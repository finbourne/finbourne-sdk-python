# FxDependency

For indicating a dependency on an fx rate.  For example domestic-foreign for USD-JPY  means that 1 unit (dollar) of domestic currency will buy you \"X\" units of foreign (Yen) currency; currently somewhere around 100.  This is equivalently denoted as USDJPY and USD/JPY                On the assumption that you wish to convert an amount in the domestic currency to the foreign, you would want the (dom,fgn) dependency; domfgn currency pair.  On the assumption that you wish to convert an amount in the foreign currency to the domestic, you would want the (fgn,dom) dependency; fgndom currency pair.                NB: There alternate descriptions for currency pairs that seem to vary between different banks and sectors of the industry, e.g. base and contract                In pricing we are taking the convention that we will convert from FGN to DOM by DIVIDING through by the DOMFGN spot rate.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **domestic_currency** | **str** | Required | DomesticCurrency is the first currency in a currency pair quote e.g. eur-gbp, eur is the domestic currency. |
| **foreign_currency** | **str** | Required | ForeignCurrency is the second currency in a currency pair quote e.g. eur-gbp, gbp is the foreign currency. |
| **var_date** | **datetime** | Required | The effectiveAt of the fx rate. |
| **dependency_type** | **str** | Required | The available values are: OpaqueDependency, CashDependency, DiscountingDependency, EquityCurveDependency, EquityVolDependency, FxDependency, FxForwardsDependency, FxVolDependency, IndexProjectionDependency, IrVolDependency, QuoteDependency, Vendor, CalendarDependency, InflationFixingDependency |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.FxDependency import FxDependency

instance = FxDependency(
    domestic_currency="...",  # required — DomesticCurrency is the first currency in a currency pair quote e.g. eur-gbp, eur is the domestic currency.
    foreign_currency="...",  # required — ForeignCurrency is the second currency in a currency pair quote e.g. eur-gbp, gbp is the foreign currency.
    var_date=datetime.now(),  # required — The effectiveAt of the fx rate.
    dependency_type="..."  # required — The available values are: OpaqueDependency, CashDependency, DiscountingDependency, EquityCurveDependency, EquityVolDependency, FxDependency, FxForwardsDependency, FxVolDependency, IndexProjectionDependency, IrVolDependency, QuoteDependency, Vendor, CalendarDependency, InflationFixingDependency
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

