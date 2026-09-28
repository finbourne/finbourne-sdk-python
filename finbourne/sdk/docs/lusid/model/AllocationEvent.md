# AllocationEvent

One economic event shared across the participants of an Allocation Map: raised as a draft, computed into  per-investor shares, and finally booked.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **href** | **str** | Optional | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. |
| **id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **description** | **str** | Optional | A description of the Allocation Event. |
| **allocation_map_id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **event_type** | **str** | Required | The type of the event: CapitalCall, Distribution, FeeExpense or ValuationMove. Selects the basis rule from the map. Available values: CapitalCall, Distribution, FeeExpense, ValuationMove. |
| **amount** | **float** | Required | The total amount to be shared across the participants. |
| **currency** | **str** | Required | The ISO 4217 code of the currency of the amount. The amount may not be finer than the currency&#39;s minor unit: two decimal places for most currencies, none for JPY, three for KWD and BHD. A code with no defined minor unit, such as XAU or XAG, is taken to have two decimal places. |
| **event_date** | **datetime** | Required | The date of the event: the point at which the map, its participants and their basis values are read. |
| **status** | **str** | Required | The lifecycle status of the event: Draft until its shares are computed, Computed once they are, and Booked once posted. Available values: Draft, Computed, Booked. |
| **basis_source** | **str** | Optional | Where the basis values came from when the shares were last computed. |
| **allocations** | [List[AllocationMapAllocation]](AllocationMapAllocation.md) | Required | The per-investor shares of the amount, as last computed. |
| **booking_reference** | **str** | Optional | The reference under which the shares were posted. Set only once the event is booked. |
| **booked_at** | **datetime** | Optional | The datetime at which the event was booked. |
| **reallocation_reason** | **str** | Optional | The reason given when the event was last recomputed, if it has been. |
| **version** | [Version](Version.md) | Optional | *No description available.* |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.AllocationEvent import AllocationEvent

instance = AllocationEvent(
    href="...",  # optional — The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.
    id=ResourceId(...),  # required
    description="...",  # optional — A description of the Allocation Event.
    allocation_map_id=ResourceId(...),  # required
    event_type="...",  # required — The type of the event: CapitalCall, Distribution, FeeExpense or ValuationMove. Selects the basis rule from the map. Available values: CapitalCall, Distribution, FeeExpense, ValuationMove.
    amount=0.0,  # required — The total amount to be shared across the participants.
    currency="...",  # required — The ISO 4217 code of the currency of the amount. The amount may not be finer than the currency&#39;s minor unit: two decimal places for most currencies, none for JPY, three for KWD and BHD. A code with no defined minor unit, such as XAU or XAG, is taken to have two decimal places.
    event_date=datetime.now(),  # required — The date of the event: the point at which the map, its participants and their basis values are read.
    status="...",  # required — The lifecycle status of the event: Draft until its shares are computed, Computed once they are, and Booked once posted. Available values: Draft, Computed, Booked.
    basis_source="...",  # optional — Where the basis values came from when the shares were last computed.
    allocations=[],  # required — The per-investor shares of the amount, as last computed.
    booking_reference="...",  # optional — The reference under which the shares were posted. Set only once the event is booked.
    booked_at=datetime.now(),  # optional — The datetime at which the event was booked.
    reallocation_reason="...",  # optional — The reason given when the event was last recomputed, if it has been.
    version=Version(...),  # optional
    links=[]  # optional
)
```

- [ResourceId](ResourceId.md)
- [ResourceId](ResourceId.md)
- [AllocationMapAllocation](AllocationMapAllocation.md) — used in `allocations`
- [Version](Version.md)
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

