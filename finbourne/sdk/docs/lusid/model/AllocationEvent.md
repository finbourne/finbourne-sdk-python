# AllocationEvent

One economic event shared across the participants of an Allocation Map: raised as a draft, computed into  per-investor shares, and finally booked.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **href** | **str** | Optional | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. |
| **id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **description** | **str** | Optional | A description of the Allocation Event. |
| **allocation_map_id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **event_type** | **str** | Required | The type of the event: CapitalCall, Distribution, FeeExpense, ValuationMove, Equalisation, RecallExpiry, Transfer, Default, Commitment or DealFunding. Selects the basis rule from the map. A recall is a CapitalCall with a Recall component. A Commitment event is not shared from a basis: its basis values are the signed commitment amounts per commitment line, and they must sum to the amount. Available values: CapitalCall, Distribution, FeeExpense, ValuationMove, Commitment, Equalisation, RecallExpiry, Transfer, Default, DealFunding. |
| **amount** | **float** | Required | The total amount to be shared across the participants. |
| **currency** | **str** | Required | The ISO 4217 code of the currency of the amount. The amount may not be finer than the currency&#39;s minor unit: two decimal places for most currencies, none for JPY, three for KWD and BHD. A code with no defined minor unit, such as XAU or XAG, is taken to have two decimal places. |
| **event_date** | **datetime** | Required | The date of the event: the point at which the map, its participants and their basis values are read. |
| **status** | **str** | Required | The lifecycle status of the event: Draft until its shares are computed, Computed once they are, Booking while its postings are being written, Booked once they all are, and Reversed once a booked event has been backed out. Available values: Draft, Computed, Booked, Booking, Reversed. |
| **basis_source** | **str** | Optional | Where the basis values came from when the shares were last computed. |
| **allocations** | [List[AllocationMapAllocation]](AllocationMapAllocation.md) | Required | The per-investor shares of the amount, as last computed. |
| **booking_reference** | **str** | Optional | The reference under which the shares were posted. Set only once the event is booked. |
| **booked_at** | **datetime** | Optional | The datetime at which the event was booked. |
| **reallocation_reason** | **str** | Optional | The reason given when the event was last recomputed, if it has been. |
| **components** | [List[AllocationEventComponent]](AllocationEventComponent.md) | Optional | The parts the amount splits into, each shared on its own basis and booked to its own slot. The component amounts must sum to the event amount. Absent means the whole amount is one component: Investment for a CapitalCall, ROC for a Distribution. |
| **residuals** | [List[AllocationEventRoundingResidual]](AllocationEventRoundingResidual.md) | Optional | The minor units left over when each component&#39;s shares were rounded to the currency, and which investor records took them. |
| **basis_diagnostics** | [AllocationEventBasisDiagnostics](AllocationEventBasisDiagnostics.md) | Optional | *No description available.* |
| **written_ids** | **List[str]** | Optional | The identifiers of the postings the booking has written so far, in write order. Complete once the event is Booked. |
| **booking_errors** | [List[AllocationEventBookingError]](AllocationEventBookingError.md) | Optional | The postings the booking could not write. Non-empty leaves the event in Booking; book again under the same reference to resume, or unbook to cancel what was written. |
| **warnings** | [List[AllocationEventBookingWarning]](AllocationEventBookingWarning.md) | Optional | The validation rules the booking was allowed to proceed through under the map&#39;s policy, for instance an OverCall on a map that warns rather than refuses. Kept for the life of the event. |
| **transfers** | [List[AllocationEventTransfer]](AllocationEventTransfer.md) | Optional | For a Transfer event, the legs to book: each moves a fraction of one capital interest line to another. Required for a Transfer event and not allowed on any other type. The fractions out of one line must sum to at most one; the amount of a Transfer event is zero. |
| **equalisation** | [AllocationEventEqualisation](AllocationEventEqualisation.md) | Optional | *No description available.* |
| **use_of_proceeds** | [List[AllocationEventUseOfProceeds]](AllocationEventUseOfProceeds.md) | Optional | For a CapitalCall, what the call pays for: rows of purpose, deal and amount that sum to the call amount. An Investment row names a deal the vehicle has funded and is shared under that deal&#39;s participation, with each investor&#39;s share recorded as paid in for that deal; when the deal was funded from a facility the row repays the draw. Not allowed with components or on any other event type. |
| **deal_funding** | [AllocationEventDealFunding](AllocationEventDealFunding.md) | Optional | *No description available.* |
| **version** | [Version](Version.md) | Optional | *No description available.* |
| **parent_allocation_event_id** | [ResourceId](ResourceId.md) | Optional | *No description available.* |
| **replaces** | [ResourceId](ResourceId.md) | Optional | *No description available.* |
| **reversal** | [AllocationEventReversal](AllocationEventReversal.md) | Optional | *No description available.* |
| **notice_date** | **datetime** | Optional | The date the notice went to investors. |
| **due_date** | **datetime** | Optional | The date the investors&#39; cash is due. |
| **settlement_date** | **datetime** | Optional | The date the postings settle. Defaults to the event date. |
| **receipts** | [List[AllocationEventReceipt]](AllocationEventReceipt.md) | Optional | The cash received against the event, in the order it was recorded. |
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
    event_type="...",  # required — The type of the event: CapitalCall, Distribution, FeeExpense, ValuationMove, Equalisation, RecallExpiry, Transfer, Default, Commitment or DealFunding. Selects the basis rule from the map. A recall is a CapitalCall with a Recall component. A Commitment event is not shared from a basis: its basis values are the signed commitment amounts per commitment line, and they must sum to the amount. Available values: CapitalCall, Distribution, FeeExpense, ValuationMove, Commitment, Equalisation, RecallExpiry, Transfer, Default, DealFunding.
    amount=0.0,  # required — The total amount to be shared across the participants.
    currency="...",  # required — The ISO 4217 code of the currency of the amount. The amount may not be finer than the currency&#39;s minor unit: two decimal places for most currencies, none for JPY, three for KWD and BHD. A code with no defined minor unit, such as XAU or XAG, is taken to have two decimal places.
    event_date=datetime.now(),  # required — The date of the event: the point at which the map, its participants and their basis values are read.
    status="...",  # required — The lifecycle status of the event: Draft until its shares are computed, Computed once they are, Booking while its postings are being written, Booked once they all are, and Reversed once a booked event has been backed out. Available values: Draft, Computed, Booked, Booking, Reversed.
    basis_source="...",  # optional — Where the basis values came from when the shares were last computed.
    allocations=[],  # required — The per-investor shares of the amount, as last computed.
    booking_reference="...",  # optional — The reference under which the shares were posted. Set only once the event is booked.
    booked_at=datetime.now(),  # optional — The datetime at which the event was booked.
    reallocation_reason="...",  # optional — The reason given when the event was last recomputed, if it has been.
    components=[],  # optional — The parts the amount splits into, each shared on its own basis and booked to its own slot. The component amounts must sum to the event amount. Absent means the whole amount is one component: Investment for a CapitalCall, ROC for a Distribution.
    residuals=[],  # optional — The minor units left over when each component&#39;s shares were rounded to the currency, and which investor records took them.
    basis_diagnostics=AllocationEventBasisDiagnostics(...),  # optional
    written_ids=,  # optional — The identifiers of the postings the booking has written so far, in write order. Complete once the event is Booked.
    booking_errors=[],  # optional — The postings the booking could not write. Non-empty leaves the event in Booking; book again under the same reference to resume, or unbook to cancel what was written.
    warnings=[],  # optional — The validation rules the booking was allowed to proceed through under the map&#39;s policy, for instance an OverCall on a map that warns rather than refuses. Kept for the life of the event.
    transfers=[],  # optional — For a Transfer event, the legs to book: each moves a fraction of one capital interest line to another. Required for a Transfer event and not allowed on any other type. The fractions out of one line must sum to at most one; the amount of a Transfer event is zero.
    equalisation=AllocationEventEqualisation(...),  # optional
    use_of_proceeds=[],  # optional — For a CapitalCall, what the call pays for: rows of purpose, deal and amount that sum to the call amount. An Investment row names a deal the vehicle has funded and is shared under that deal&#39;s participation, with each investor&#39;s share recorded as paid in for that deal; when the deal was funded from a facility the row repays the draw. Not allowed with components or on any other event type.
    deal_funding=AllocationEventDealFunding(...),  # optional
    version=Version(...),  # optional
    parent_allocation_event_id=ResourceId(...),  # optional
    replaces=ResourceId(...),  # optional
    reversal=AllocationEventReversal(...),  # optional
    notice_date=datetime.now(),  # optional — The date the notice went to investors.
    due_date=datetime.now(),  # optional — The date the investors&#39; cash is due.
    settlement_date=datetime.now(),  # optional — The date the postings settle. Defaults to the event date.
    receipts=[],  # optional — The cash received against the event, in the order it was recorded.
    links=[]  # optional
)
```

- [ResourceId](ResourceId.md)
- [ResourceId](ResourceId.md)
- [AllocationMapAllocation](AllocationMapAllocation.md) — used in `allocations`
- [AllocationEventComponent](AllocationEventComponent.md) — used in `components`
- [AllocationEventRoundingResidual](AllocationEventRoundingResidual.md) — used in `residuals`
- [AllocationEventBasisDiagnostics](AllocationEventBasisDiagnostics.md)
- [AllocationEventBookingError](AllocationEventBookingError.md) — used in `booking_errors`
- [AllocationEventBookingWarning](AllocationEventBookingWarning.md) — used in `warnings`
- [AllocationEventTransfer](AllocationEventTransfer.md) — used in `transfers`
- [AllocationEventEqualisation](AllocationEventEqualisation.md)
- [AllocationEventUseOfProceeds](AllocationEventUseOfProceeds.md) — used in `use_of_proceeds`
- [AllocationEventDealFunding](AllocationEventDealFunding.md)
- [Version](Version.md)
- [ResourceId](ResourceId.md)
- [ResourceId](ResourceId.md)
- [AllocationEventReversal](AllocationEventReversal.md)
- [AllocationEventReceipt](AllocationEventReceipt.md) — used in `receipts`
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

