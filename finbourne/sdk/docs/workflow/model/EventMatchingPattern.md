# EventMatchingPattern

The matching event pattern object
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **event_type** | **str** | Required | The type of event to subscribe to. The list of available event types can be discovered by calling the ListEventTypes API endpoint in the Notifications service. Note that event types published by the Workflow service itself (such as TaskCreated, TaskUpdated, TaskDeleted, TaskDefinitionCreated, TaskDefinitionUpdated and TaskDefinitionDeleted) are not supported as Event Handler triggers, and specifying one will be rejected. |
| **filter** | **str** | Optional | A filter on the event. See https://support.lusid.com/filtering-results-from-lusid for more information. If not provided, all events will be matched. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.workflow.models.EventMatchingPattern import EventMatchingPattern

instance = EventMatchingPattern(
    event_type="...",  # required — The type of event to subscribe to. The list of available event types can be discovered by calling the ListEventTypes API endpoint in the Notifications service. Note that event types published by the Workflow service itself (such as TaskCreated, TaskUpdated, TaskDeleted, TaskDefinitionCreated, TaskDefinitionUpdated and TaskDefinitionDeleted) are not supported as Event Handler triggers, and specifying one will be rejected.
    filter="..."  # optional — A filter on the event. See https://support.lusid.com/filtering-results-from-lusid for more information. If not provided, all events will be matched.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

