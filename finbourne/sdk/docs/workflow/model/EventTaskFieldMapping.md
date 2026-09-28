# EventTaskFieldMapping

How an Event Launcher fills one field of the root task from the event that arrived
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **map_from** | **str** | Required | The path into the event the value is taken from, for example header.timestamp |
| **date_time_adjustment** | [DateTimeAdjustment](DateTimeAdjustment.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.workflow.models.EventTaskFieldMapping import EventTaskFieldMapping

instance = EventTaskFieldMapping(
    map_from="...",  # required — The path into the event the value is taken from, for example header.timestamp
    date_time_adjustment=DateTimeAdjustment(...)  # optional
)
```

- [DateTimeAdjustment](DateTimeAdjustment.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

