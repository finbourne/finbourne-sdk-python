# AllocationEventRequest

The request used to raise or replace an Allocation Event. The event is computed against its map straight away.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **code** | **str** | Required | The code of the Allocation Event. Together with the scope this uniquely identifies the event. |
| **allocation_map_id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **event_type** | **str** | Required | The type of the event: CapitalCall, Distribution, FeeExpense, ValuationMove, Equalisation, RecallExpiry, Transfer, Default, Commitment or DealFunding. Selects the basis rule from the map. A recall is a CapitalCall with a Recall component. A Commitment event is not shared from a basis: its basis values are the signed commitment amounts per commitment line, and they must sum to the amount. Available values: CapitalCall, Distribution, FeeExpense, ValuationMove, Commitment, Equalisation, RecallExpiry, Transfer, Default, DealFunding. |
| **amount** | **float** | Required | The total amount to be shared across the participants. |
| **currency** | **str** | Required | The ISO 4217 code of the currency of the amount. The amount may not be finer than the currency&#39;s minor unit: two decimal places for most currencies, none for JPY, three for KWD and BHD. A code with no defined minor unit, such as XAU or XAG, is taken to have two decimal places. |
| **event_date** | **datetime** | Required | The date of the event: the point at which the map, its participants and their basis values are read. |
| **description** | **str** | Optional | A description of the Allocation Event. |
| **basis_values** | [List[AllocationMapBasisValue]](AllocationMapBasisValue.md) | Optional | Optional basis values per investor record, used when the map&#39;s basis is not resolvable from stored data. |
| **components** | [List[AllocationEventComponent]](AllocationEventComponent.md) | Optional | The parts the amount splits into, each shared on its own basis and booked to its own slot. The component amounts must sum to the event amount. Absent means the whole amount is one component: Investment for a CapitalCall, ROC for a Distribution. |
| **transfers** | [List[AllocationEventTransfer]](AllocationEventTransfer.md) | Optional | For a Transfer event, the legs to book: each moves a fraction of one capital interest line to another. Required for a Transfer event and not allowed on any other type. The fractions out of one line must sum to at most one; the amount of a Transfer event is zero. |
| **equalisation** | [AllocationEventEqualisation](AllocationEventEqualisation.md) | Optional | *No description available.* |
| **use_of_proceeds** | [List[AllocationEventUseOfProceeds]](AllocationEventUseOfProceeds.md) | Optional | For a CapitalCall, what the call pays for: rows of purpose, deal and amount that sum to the call amount. An Investment row names a deal the vehicle has funded and is shared under that deal&#39;s participation, with each investor&#39;s share recorded as paid in for that deal; when the deal was funded from a facility the row repays the draw. Not allowed with components or on any other event type. |
| **deal_funding** | [AllocationEventDealFunding](AllocationEventDealFunding.md) | Optional | *No description available.* |
| **effective_at** | **datetime** | Optional | The effective datetime at which the event is created or replaced. Defaults to the earliest effective time on create and the current LUSID system datetime on replace. |
| **replaces** | [ResourceId](ResourceId.md) | Optional | *No description available.* |
| **notice_date** | **datetime** | Optional | The date the notice went to investors. |
| **due_date** | **datetime** | Optional | The date the investors&#39; cash is due. |
| **settlement_date** | **datetime** | Optional | The date the postings settle. Defaults to the event date. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.AllocationEventRequest import AllocationEventRequest

instance = AllocationEventRequest(
    code="...",  # required — The code of the Allocation Event. Together with the scope this uniquely identifies the event.
    allocation_map_id=ResourceId(...),  # required
    event_type="...",  # required — The type of the event: CapitalCall, Distribution, FeeExpense, ValuationMove, Equalisation, RecallExpiry, Transfer, Default, Commitment or DealFunding. Selects the basis rule from the map. A recall is a CapitalCall with a Recall component. A Commitment event is not shared from a basis: its basis values are the signed commitment amounts per commitment line, and they must sum to the amount. Available values: CapitalCall, Distribution, FeeExpense, ValuationMove, Commitment, Equalisation, RecallExpiry, Transfer, Default, DealFunding.
    amount=0.0,  # required — The total amount to be shared across the participants.
    currency="...",  # required — The ISO 4217 code of the currency of the amount. The amount may not be finer than the currency&#39;s minor unit: two decimal places for most currencies, none for JPY, three for KWD and BHD. A code with no defined minor unit, such as XAU or XAG, is taken to have two decimal places.
    event_date=datetime.now(),  # required — The date of the event: the point at which the map, its participants and their basis values are read.
    description="...",  # optional — A description of the Allocation Event.
    basis_values=[],  # optional — Optional basis values per investor record, used when the map&#39;s basis is not resolvable from stored data.
    components=[],  # optional — The parts the amount splits into, each shared on its own basis and booked to its own slot. The component amounts must sum to the event amount. Absent means the whole amount is one component: Investment for a CapitalCall, ROC for a Distribution.
    transfers=[],  # optional — For a Transfer event, the legs to book: each moves a fraction of one capital interest line to another. Required for a Transfer event and not allowed on any other type. The fractions out of one line must sum to at most one; the amount of a Transfer event is zero.
    equalisation=AllocationEventEqualisation(...),  # optional
    use_of_proceeds=[],  # optional — For a CapitalCall, what the call pays for: rows of purpose, deal and amount that sum to the call amount. An Investment row names a deal the vehicle has funded and is shared under that deal&#39;s participation, with each investor&#39;s share recorded as paid in for that deal; when the deal was funded from a facility the row repays the draw. Not allowed with components or on any other event type.
    deal_funding=AllocationEventDealFunding(...),  # optional
    effective_at=datetime.now(),  # optional — The effective datetime at which the event is created or replaced. Defaults to the earliest effective time on create and the current LUSID system datetime on replace.
    replaces=ResourceId(...),  # optional
    notice_date=datetime.now(),  # optional — The date the notice went to investors.
    due_date=datetime.now(),  # optional — The date the investors&#39; cash is due.
    settlement_date=datetime.now()  # optional — The date the postings settle. Defaults to the event date.
)
```

- [ResourceId](ResourceId.md)
- [AllocationMapBasisValue](AllocationMapBasisValue.md) — used in `basis_values`
- [AllocationEventComponent](AllocationEventComponent.md) — used in `components`
- [AllocationEventTransfer](AllocationEventTransfer.md) — used in `transfers`
- [AllocationEventEqualisation](AllocationEventEqualisation.md)
- [AllocationEventUseOfProceeds](AllocationEventUseOfProceeds.md) — used in `use_of_proceeds`
- [AllocationEventDealFunding](AllocationEventDealFunding.md)
- [ResourceId](ResourceId.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

