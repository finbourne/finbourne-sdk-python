# VendorDependency

For indicating a dependency on some opaque market data requested by an outside vendor
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **vendor_name** | **str** | Required | The name of the outside vendor |
| **vendor_path** | **List[str]** | Required | The specific dependency path |
| **var_date** | **datetime** | Required | The effectiveDate of the entity that this is a dependency for. |
| **dependency_type** | **str** | Required | The available values are: OpaqueDependency, CashDependency, DiscountingDependency, EquityCurveDependency, EquityVolDependency, FxDependency, FxForwardsDependency, FxVolDependency, IndexProjectionDependency, IrVolDependency, QuoteDependency, Vendor, CalendarDependency, InflationFixingDependency |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.VendorDependency import VendorDependency

instance = VendorDependency(
    vendor_name="...",  # required — The name of the outside vendor
    vendor_path=,  # required — The specific dependency path
    var_date=datetime.now(),  # required — The effectiveDate of the entity that this is a dependency for.
    dependency_type="..."  # required — The available values are: OpaqueDependency, CashDependency, DiscountingDependency, EquityCurveDependency, EquityVolDependency, FxDependency, FxForwardsDependency, FxVolDependency, IndexProjectionDependency, IrVolDependency, QuoteDependency, Vendor, CalendarDependency, InflationFixingDependency
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

