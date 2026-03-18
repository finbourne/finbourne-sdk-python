# IrVolDependency

Economic dependency required to price interest rate products that contain optionality, for example swaptions.  For example, can indicate a dependency on an IrVolCubeData.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **currency** | **str** | Required | The domestic currency of the instrument declaring this dependency. |
| **vol_type** | **str** | Required | Volatility type e.g. \&quot;LN\&quot; and \&quot;N\&quot; for log-normal and normal volatility. |
| **var_date** | **datetime** | Required | The effectiveDate of the entity that this is a dependency for.  Unless there is an obvious date this should be, like for a historic reset, then this is the valuation date. |
| **dependency_type** | **str** | Required | The available values are: OpaqueDependency, CashDependency, DiscountingDependency, EquityCurveDependency, EquityVolDependency, FxDependency, FxForwardsDependency, FxVolDependency, IndexProjectionDependency, IrVolDependency, QuoteDependency, Vendor, CalendarDependency, InflationFixingDependency |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.IrVolDependency import IrVolDependency

instance = IrVolDependency(
    currency="...",  # required — The domestic currency of the instrument declaring this dependency.
    vol_type="...",  # required — Volatility type e.g. \&quot;LN\&quot; and \&quot;N\&quot; for log-normal and normal volatility.
    var_date=datetime.now(),  # required — The effectiveDate of the entity that this is a dependency for.  Unless there is an obvious date this should be, like for a historic reset, then this is the valuation date.
    dependency_type="..."  # required — The available values are: OpaqueDependency, CashDependency, DiscountingDependency, EquityCurveDependency, EquityVolDependency, FxDependency, FxForwardsDependency, FxVolDependency, IndexProjectionDependency, IrVolDependency, QuoteDependency, Vendor, CalendarDependency, InflationFixingDependency
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

