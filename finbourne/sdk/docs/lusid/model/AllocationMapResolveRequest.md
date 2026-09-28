# AllocationMapResolveRequest

A dry run of an Allocation Map: the event to share, and the basis values to share it by.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **event_type** | **str** | Required | The kind of allocation event to resolve: CapitalCall, Distribution, FeeExpense or ValuationMove. The map must define a basis for it. Available values: CapitalCall, Distribution, FeeExpense, ValuationMove. |
| **amount** | **float** | Required | The amount of the event to share between the participants, in the event currency. |
| **currency** | **str** | Required | The currency of the amount. |
| **basis_values** | [List[AllocationMapBasisValue]](AllocationMapBasisValue.md) | Optional | For a ValueWeighted or PropertyWeighted basis, the basis value of each participating investor record, supplied by the caller until investor records are read from LUSID. Under the AllCommittedToMembers rule these also name the committed investor records. Not needed for a FixedPercentage basis. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.AllocationMapResolveRequest import AllocationMapResolveRequest

instance = AllocationMapResolveRequest(
    event_type="...",  # required — The kind of allocation event to resolve: CapitalCall, Distribution, FeeExpense or ValuationMove. The map must define a basis for it. Available values: CapitalCall, Distribution, FeeExpense, ValuationMove.
    amount=0.0,  # required — The amount of the event to share between the participants, in the event currency.
    currency="...",  # required — The currency of the amount.
    basis_values=[]  # optional — For a ValueWeighted or PropertyWeighted basis, the basis value of each participating investor record, supplied by the caller until investor records are read from LUSID. Under the AllCommittedToMembers rule these also name the committed investor records. Not needed for a FixedPercentage basis.
)
```

- [AllocationMapBasisValue](AllocationMapBasisValue.md) — used in `basis_values`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

