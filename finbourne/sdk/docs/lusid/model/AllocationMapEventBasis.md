# AllocationMapEventBasis

The basis an Allocation Map applies to one kind of allocation event.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **event_type** | **str** | Required | The kind of allocation event the basis applies to: CapitalCall, Distribution, FeeExpense, ValuationMove, Equalisation, RecallExpiry, Transfer, Default, Commitment or DealFunding. Available values: CapitalCall, Distribution, FeeExpense, ValuationMove, Commitment, Equalisation, RecallExpiry, Transfer, Default, DealFunding. |
| **basis** | [AllocationMapBasis](AllocationMapBasis.md) | Required | *No description available.* |
| **component** | **str** | Optional | The component of the event the basis applies to, for example MgmtFee or OrgCost. Absent means the entry is the default for every component of the event type without an entry of its own. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.AllocationMapEventBasis import AllocationMapEventBasis

instance = AllocationMapEventBasis(
    event_type="...",  # required — The kind of allocation event the basis applies to: CapitalCall, Distribution, FeeExpense, ValuationMove, Equalisation, RecallExpiry, Transfer, Default, Commitment or DealFunding. Available values: CapitalCall, Distribution, FeeExpense, ValuationMove, Commitment, Equalisation, RecallExpiry, Transfer, Default, DealFunding.
    basis=AllocationMapBasis(...),  # required
    component="..."  # optional — The component of the event the basis applies to, for example MgmtFee or OrgCost. Absent means the entry is the default for every component of the event type without an entry of its own.
)
```

- [AllocationMapBasis](AllocationMapBasis.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

