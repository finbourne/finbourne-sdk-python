# AllocationMapEventBasis

The basis an Allocation Map applies to one kind of allocation event.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **event_type** | **str** | Required | The kind of allocation event the basis applies to: CapitalCall, Distribution, FeeExpense or ValuationMove. Available values: CapitalCall, Distribution, FeeExpense, ValuationMove. |
| **basis** | [AllocationMapBasis](AllocationMapBasis.md) | Required | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.AllocationMapEventBasis import AllocationMapEventBasis

instance = AllocationMapEventBasis(
    event_type="...",  # required — The kind of allocation event the basis applies to: CapitalCall, Distribution, FeeExpense or ValuationMove. Available values: CapitalCall, Distribution, FeeExpense, ValuationMove.
    basis=AllocationMapBasis(...)  # required
)
```

- [AllocationMapBasis](AllocationMapBasis.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

