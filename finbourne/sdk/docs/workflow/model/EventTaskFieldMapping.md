# EventTaskFieldMapping

How an Event Launcher fills one field of the root task from the event that arrived
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **map_from** | **str** | Required | The path into the event the value is taken from, for example header.timestamp. The path must be in the schema of the event type, and the value must suit the type of the field. A string fills a String or LusidUserId field, a number fills a Decimal field, a boolean fills a Boolean field, and a date and time fills a DateTime field. A path to an identifier collection names a key, for example body.identifiers[Instrument/default/Figi], and fills a String field |
| **date_time_adjustment** | [DateTimeAdjustment](DateTimeAdjustment.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.workflow.models.EventTaskFieldMapping import EventTaskFieldMapping

instance = EventTaskFieldMapping(
    map_from="...",  # required — The path into the event the value is taken from, for example header.timestamp. The path must be in the schema of the event type, and the value must suit the type of the field. A string fills a String or LusidUserId field, a number fills a Decimal field, a boolean fills a Boolean field, and a date and time fills a DateTime field. A path to an identifier collection names a key, for example body.identifiers[Instrument/default/Figi], and fills a String field
    date_time_adjustment=DateTimeAdjustment(...)  # optional
)
```

- [DateTimeAdjustment](DateTimeAdjustment.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

