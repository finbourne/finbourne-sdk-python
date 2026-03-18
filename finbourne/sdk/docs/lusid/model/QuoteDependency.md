# QuoteDependency

For indicating a dependency on the value of an asset at a point in time.  If the time is omitted, then the dependency is interpreted as the latest value with respect to anything observing it.  E.g. An EquitySwap will declare a dependency on the current price of the underlying equity.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **market_identifier** | **str** | Required | Type of the code identifying the asset, e.g. ISIN or CUSIP |
| **code** | **str** | Required | The code identifying the corresponding equity, e.g. US0378331005 if the MarketIdentifier was set to ISIN |
| **var_date** | **datetime** | Required | The effectiveAt of the quote for the identified entity. |
| **dependency_type** | **str** | Required | The available values are: OpaqueDependency, CashDependency, DiscountingDependency, EquityCurveDependency, EquityVolDependency, FxDependency, FxForwardsDependency, FxVolDependency, IndexProjectionDependency, IrVolDependency, QuoteDependency, Vendor, CalendarDependency, InflationFixingDependency |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.QuoteDependency import QuoteDependency

instance = QuoteDependency(
    market_identifier="...",  # required — Type of the code identifying the asset, e.g. ISIN or CUSIP
    code="...",  # required — The code identifying the corresponding equity, e.g. US0378331005 if the MarketIdentifier was set to ISIN
    var_date=datetime.now(),  # required — The effectiveAt of the quote for the identified entity.
    dependency_type="..."  # required — The available values are: OpaqueDependency, CashDependency, DiscountingDependency, EquityCurveDependency, EquityVolDependency, FxDependency, FxForwardsDependency, FxVolDependency, IndexProjectionDependency, IrVolDependency, QuoteDependency, Vendor, CalendarDependency, InflationFixingDependency
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

