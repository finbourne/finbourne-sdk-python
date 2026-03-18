# OrderFlowConfiguration

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **include_entity_types** | **str** | Required | Controls whether Orders and Allocations orders are included in the Portfolio valuation.  Valid values are  None (to account for Transactions only), Allocations (to include Allocations and Transactions) and  OrdersAndAllocations (to include Orders, Allocations and Transactions). |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.OrderFlowConfiguration import OrderFlowConfiguration

instance = OrderFlowConfiguration(
    include_entity_types="..."  # required — Controls whether Orders and Allocations orders are included in the Portfolio valuation.  Valid values are  None (to account for Transactions only), Allocations (to include Allocations and Transactions) and  OrdersAndAllocations (to include Orders, Allocations and Transactions).
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

