# InstrumentEventInstruction

An instruction for an instrument event
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **instrument_event_instruction_id** | **str** | Optional | The unique identifier for this instruction |
| **portfolio_id** | [ResourceId](ResourceId.md) | Optional | *No description available.* |
| **instrument_event_id** | **str** | Optional | The identifier of the instrument event being instructed |
| **instruction_type** | **str** | Optional | The type of instruction (Ignore, ElectForPortfolio, ElectForHolding, ElectForLoanFacilityHolding) |
| **election_key** | **str** | Optional | For elected instructions, the key to be chosen |
| **holding_id** | **int** | Optional | For holding instructions, the id of the holding for which the instruction will apply |
| **version** | [Version](Version.md) | Optional | *No description available.* |
| **href** | **str** | Optional | The uri for this version of this instruction |
| **entitlement_date_instructed** | **datetime** | Optional | The instructed entitlement date for the event (where none is set on the event itself) |
| **quantity_instructed** | [QuantityInstructed](QuantityInstructed.md) | Optional | *No description available.* |
| **tax_lot_id** | **str** | Optional | For loan facility holding instructions, the tax lot id of the holding for which the instruction will apply |
| **ignore_cost_impact** | **bool** | Optional | For loan facility holding instructions, set this flag to &#39;true&#39; if you want the event to not impact cost. If you want to use this option, do not add multiple instructions to the same tax lot or you will get undefined behaviour. |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.InstrumentEventInstruction import InstrumentEventInstruction

instance = InstrumentEventInstruction(
    instrument_event_instruction_id="...",  # optional — The unique identifier for this instruction
    portfolio_id=ResourceId(...),  # optional
    instrument_event_id="...",  # optional — The identifier of the instrument event being instructed
    instruction_type="...",  # optional — The type of instruction (Ignore, ElectForPortfolio, ElectForHolding, ElectForLoanFacilityHolding)
    election_key="...",  # optional — For elected instructions, the key to be chosen
    holding_id=0,  # optional — For holding instructions, the id of the holding for which the instruction will apply
    version=Version(...),  # optional
    href="...",  # optional — The uri for this version of this instruction
    entitlement_date_instructed=datetime.now(),  # optional — The instructed entitlement date for the event (where none is set on the event itself)
    quantity_instructed=QuantityInstructed(...),  # optional
    tax_lot_id="...",  # optional — For loan facility holding instructions, the tax lot id of the holding for which the instruction will apply
    ignore_cost_impact=True,  # optional — For loan facility holding instructions, set this flag to &#39;true&#39; if you want the event to not impact cost. If you want to use this option, do not add multiple instructions to the same tax lot or you will get undefined behaviour.
    links=[]  # optional
)
```

- [ResourceId](ResourceId.md)
- [Version](Version.md)
- [QuantityInstructed](QuantityInstructed.md)
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

