# LifeCycleEventLineage

The lineage of the event value
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **event_type** | **str** | Optional | The type of the event |
| **instrument_type** | **str** | Optional | The instrument type of the instrument for the event. |
| **instrument_id** | **str** | Optional | The LUID of the instrument for the event. |
| **leg_id** | **str** | Optional | Leg id for the event. |
| **source_transaction_id** | **str** | Optional | The source transaction of the instrument for the event. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.LifeCycleEventLineage import LifeCycleEventLineage

instance = LifeCycleEventLineage(
    event_type="...",  # optional — The type of the event
    instrument_type="...",  # optional — The instrument type of the instrument for the event.
    instrument_id="...",  # optional — The LUID of the instrument for the event.
    leg_id="...",  # optional — Leg id for the event.
    source_transaction_id="..."  # optional — The source transaction of the instrument for the event.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

