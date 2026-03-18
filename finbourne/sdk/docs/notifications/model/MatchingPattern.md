# MatchingPattern

A matching pattern object
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **event_type** | **str** | Required | The type of event to subscribe to. The list of available event types can be discovered by calling the ‘List available EventTypes’ API endpoint. |
| **filter** | **str** | Optional | A filter on the event. See https://support.lusid.com/filtering-results-from-lusid for more information. If not provided, all events will be matched |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.notifications.models.MatchingPattern import MatchingPattern

instance = MatchingPattern(
    event_type="...",  # required — The type of event to subscribe to. The list of available event types can be discovered by calling the ‘List available EventTypes’ API endpoint.
    filter="..."  # optional — A filter on the event. See https://support.lusid.com/filtering-results-from-lusid for more information. If not provided, all events will be matched
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

