# AllocationEventRequest

The request used to raise or replace an Allocation Event. The event is computed against its map straight away.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **code** | **str** | Required | The code of the Allocation Event. Together with the scope this uniquely identifies the event. |
| **allocation_map_id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **event_type** | **str** | Required | The type of the event: CapitalCall, Distribution, FeeExpense or ValuationMove. Selects the basis rule from the map. Available values: CapitalCall, Distribution, FeeExpense, ValuationMove. |
| **amount** | **float** | Required | The total amount to be shared across the participants. |
| **currency** | **str** | Required | The ISO 4217 code of the currency of the amount. The amount may not be finer than the currency&#39;s minor unit: two decimal places for most currencies, none for JPY, three for KWD and BHD. A code with no defined minor unit, such as XAU or XAG, is taken to have two decimal places. |
| **event_date** | **datetime** | Required | The date of the event: the point at which the map, its participants and their basis values are read. |
| **description** | **str** | Optional | A description of the Allocation Event. |
| **basis_values** | [List[AllocationMapBasisValue]](AllocationMapBasisValue.md) | Optional | Optional basis values per investor record, used when the map&#39;s basis is not resolvable from stored data. |
| **effective_at** | **datetime** | Optional | The effective datetime at which the event is created or replaced. Defaults to the earliest effective time on create and the current LUSID system datetime on replace. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.AllocationEventRequest import AllocationEventRequest

instance = AllocationEventRequest(
    code="...",  # required — The code of the Allocation Event. Together with the scope this uniquely identifies the event.
    allocation_map_id=ResourceId(...),  # required
    event_type="...",  # required — The type of the event: CapitalCall, Distribution, FeeExpense or ValuationMove. Selects the basis rule from the map. Available values: CapitalCall, Distribution, FeeExpense, ValuationMove.
    amount=0.0,  # required — The total amount to be shared across the participants.
    currency="...",  # required — The ISO 4217 code of the currency of the amount. The amount may not be finer than the currency&#39;s minor unit: two decimal places for most currencies, none for JPY, three for KWD and BHD. A code with no defined minor unit, such as XAU or XAG, is taken to have two decimal places.
    event_date=datetime.now(),  # required — The date of the event: the point at which the map, its participants and their basis values are read.
    description="...",  # optional — A description of the Allocation Event.
    basis_values=[],  # optional — Optional basis values per investor record, used when the map&#39;s basis is not resolvable from stored data.
    effective_at=datetime.now()  # optional — The effective datetime at which the event is created or replaced. Defaults to the earliest effective time on create and the current LUSID system datetime on replace.
)
```

- [ResourceId](ResourceId.md)
- [AllocationMapBasisValue](AllocationMapBasisValue.md) — used in `basis_values`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

