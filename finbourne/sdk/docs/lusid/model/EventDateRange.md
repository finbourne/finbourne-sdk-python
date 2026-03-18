# EventDateRange

A standard representation of the effective date range for the event, used for display, filtering and windowing use cases.  The start and end values for the eventDateRange are mapped from the particular dates contained within the specific  InstrumentEvent schema.  Note that the start and end values may be identical for some types of events.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **start** | **datetime** | Optional | *No description available.* |
| **end** | **datetime** | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.EventDateRange import EventDateRange

instance = EventDateRange(
    start=datetime.now(),  # optional
    end=datetime.now()  # optional
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

