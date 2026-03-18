# EquityCurveDependency

For indicating a dependency on an EquityCurve.  E.g. When pricing an EquitySwap one may want to make predictions about the price of the underlying equity at future dates.  If so, that model would declare an EquityCurve dependency so that it could obtain predictions from the EquityCurve.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **market_identifier** | **str** | Required | Type of the code identifying the corresponding equity, e.g. ISIN or CUSIP |
| **code** | **str** | Required | The code identifying the corresponding equity, e.g. US0378331005 if the MarketIdentifier was set to ISIN |
| **curve_type** | **str** | Required | The curve type of the EquityCurve required. E.g. EquityCurveByPrices |
| **var_date** | **datetime** | Required | The effectiveDate of the entity that this is a dependency for.  Unless there is an obvious date this should be, like for a historic reset, then this is the valuation date. |
| **dependency_type** | **str** | Required | The available values are: OpaqueDependency, CashDependency, DiscountingDependency, EquityCurveDependency, EquityVolDependency, FxDependency, FxForwardsDependency, FxVolDependency, IndexProjectionDependency, IrVolDependency, QuoteDependency, Vendor, CalendarDependency, InflationFixingDependency |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.EquityCurveDependency import EquityCurveDependency

instance = EquityCurveDependency(
    market_identifier="...",  # required — Type of the code identifying the corresponding equity, e.g. ISIN or CUSIP
    code="...",  # required — The code identifying the corresponding equity, e.g. US0378331005 if the MarketIdentifier was set to ISIN
    curve_type="...",  # required — The curve type of the EquityCurve required. E.g. EquityCurveByPrices
    var_date=datetime.now(),  # required — The effectiveDate of the entity that this is a dependency for.  Unless there is an obvious date this should be, like for a historic reset, then this is the valuation date.
    dependency_type="..."  # required — The available values are: OpaqueDependency, CashDependency, DiscountingDependency, EquityCurveDependency, EquityVolDependency, FxDependency, FxForwardsDependency, FxVolDependency, IndexProjectionDependency, IrVolDependency, QuoteDependency, Vendor, CalendarDependency, InflationFixingDependency
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

