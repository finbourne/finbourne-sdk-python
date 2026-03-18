# InflationFixingDependency

For indicating a dependency upon an inflation fixing
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **type** | **str** | Required | The Type of fixing (index, ratio or assumption) |
| **code** | **str** | Required | The Code of the fixing, typically the index name |
| **var_date** | **datetime** | Required | The effectiveAt of the inflation fixing |
| **dependency_type** | **str** | Required | The available values are: OpaqueDependency, CashDependency, DiscountingDependency, EquityCurveDependency, EquityVolDependency, FxDependency, FxForwardsDependency, FxVolDependency, IndexProjectionDependency, IrVolDependency, QuoteDependency, Vendor, CalendarDependency, InflationFixingDependency |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.InflationFixingDependency import InflationFixingDependency

instance = InflationFixingDependency(
    type="...",  # required — The Type of fixing (index, ratio or assumption)
    code="...",  # required — The Code of the fixing, typically the index name
    var_date=datetime.now(),  # required — The effectiveAt of the inflation fixing
    dependency_type="..."  # required — The available values are: OpaqueDependency, CashDependency, DiscountingDependency, EquityCurveDependency, EquityVolDependency, FxDependency, FxForwardsDependency, FxVolDependency, IndexProjectionDependency, IrVolDependency, QuoteDependency, Vendor, CalendarDependency, InflationFixingDependency
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

