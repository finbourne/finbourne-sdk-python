# UpsertInstrumentEventRequest

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **instrument_event_id** | **str** | Required | Free string that uniquely identifies the event within the corporate action source |
| **instrument_identifiers** | **Dict[str, Optional[str]]** | Required | The set of identifiers which determine the instrument this event relates to. |
| **description** | **str** | Optional | The description of the instrument event. |
| **instrument_event** | [InstrumentEvent](InstrumentEvent.md) | Required | *No description available.* |
| **properties** | [List[PerpetualProperty]](PerpetualProperty.md) | Optional | The properties attached to this instrument event. |
| **sequence_number** | **int** | Optional | The order of the instrument event relative others on the same date (0 being processed first). Must be non negative. |
| **participation_type** | **str** | Optional | Is participation in this event Mandatory, MandatoryWithChoices, or Voluntary. Default: `'Mandatory'` |
| **event_date_stamps** | [Dict[str, YearMonthDay]](YearMonthDay.md) | Optional | The date stamps corresponding to the relevant date-time fields for the instrument event. The key for each provided date stamp must match the field name of a valid datetime field from the InstrumentEvent DTO. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.UpsertInstrumentEventRequest import UpsertInstrumentEventRequest

instance = UpsertInstrumentEventRequest(
    instrument_event_id="...",  # required — Free string that uniquely identifies the event within the corporate action source
    instrument_identifiers=,  # required — The set of identifiers which determine the instrument this event relates to.
    description="...",  # optional — The description of the instrument event.
    instrument_event=InstrumentEvent(...),  # required
    properties=[],  # optional — The properties attached to this instrument event.
    sequence_number=0,  # optional — The order of the instrument event relative others on the same date (0 being processed first). Must be non negative.
    participation_type="...",  # optional — Is participation in this event Mandatory, MandatoryWithChoices, or Voluntary.
    event_date_stamps=YearMonthDay(...)  # optional — The date stamps corresponding to the relevant date-time fields for the instrument event. The key for each provided date stamp must match the field name of a valid datetime field from the InstrumentEvent DTO.
)
```

- [InstrumentEvent](InstrumentEvent.md)
- [PerpetualProperty](PerpetualProperty.md) — used in `properties`
- [YearMonthDay](YearMonthDay.md) — used in `event_date_stamps`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

