# InstrumentEventHolder

An instrument event equipped with additional metadata.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **instrument_event_id** | **str** | Required | The unique identifier of this corporate action. |
| **corporate_action_source_id** | [ResourceId](ResourceId.md) | Optional | *No description available.* |
| **instrument_identifiers** | **Dict[str, Optional[str]]** | Required | The set of identifiers which determine the instrument this event relates to. |
| **lusid_instrument_id** | **str** | Required | The LUID for the instrument. |
| **instrument_scope** | **str** | Required | The scope of the instrument. |
| **description** | **str** | Required | The description of the instrument event. |
| **event_date_range** | [EventDateRange](EventDateRange.md) | Required | *No description available.* |
| **completeness** | **str** | Optional | Is the event Economically Complete, or is it missing some DataDependent fields (Incomplete). *(read-only)* |
| **instrument_event** | [InstrumentEvent](InstrumentEvent.md) | Required | *No description available.* |
| **properties** | [List[PerpetualProperty]](PerpetualProperty.md) | Optional | The properties attached to this instrument event. |
| **sequence_number** | **int** | Optional | The order of the instrument event relative others on the same date (0 being processed first). Must be non negative. |
| **participation_type** | **str** | Optional | Is participation in this event Mandatory, MandatoryWithChoices, or Voluntary. Default: `'Mandatory'` |
| **as_at** | **datetime** | Optional | The AsAt time of the instrument event, if available. This is a readonly field and should not be provided on upsert. *(read-only)* |
| **group_code** | **str** | Optional | The group code that determines the processing order of instrument events with the same effective datetime. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.InstrumentEventHolder import InstrumentEventHolder

instance = InstrumentEventHolder(
    instrument_event_id="...",  # required — The unique identifier of this corporate action.
    corporate_action_source_id=ResourceId(...),  # optional
    instrument_identifiers=,  # required — The set of identifiers which determine the instrument this event relates to.
    lusid_instrument_id="...",  # required — The LUID for the instrument.
    instrument_scope="...",  # required — The scope of the instrument.
    description="...",  # required — The description of the instrument event.
    event_date_range=EventDateRange(...),  # required
    completeness="...",  # optional — Is the event Economically Complete, or is it missing some DataDependent fields (Incomplete).
    instrument_event=InstrumentEvent(...),  # required
    properties=[],  # optional — The properties attached to this instrument event.
    sequence_number=0,  # optional — The order of the instrument event relative others on the same date (0 being processed first). Must be non negative.
    participation_type="...",  # optional — Is participation in this event Mandatory, MandatoryWithChoices, or Voluntary.
    as_at=datetime.now(),  # optional — The AsAt time of the instrument event, if available. This is a readonly field and should not be provided on upsert.
    group_code="..."  # optional — The group code that determines the processing order of instrument events with the same effective datetime.
)
```

- [ResourceId](ResourceId.md)
- [EventDateRange](EventDateRange.md)
- [InstrumentEvent](InstrumentEvent.md)
- [PerpetualProperty](PerpetualProperty.md) — used in `properties`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

