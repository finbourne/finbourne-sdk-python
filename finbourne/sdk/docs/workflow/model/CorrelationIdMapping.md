# CorrelationIdMapping

How an Event Launcher fills one correlation ID of the root task from the event that arrived.              A mapped correlation ID joins the fixed correlation IDs of the Launcher
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **map_from** | **str** | Required | The path into the event the correlation ID is taken from, for example body.fileId. The path must be in the schema of the event type, and a value of any type is written as a string |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.workflow.models.CorrelationIdMapping import CorrelationIdMapping

instance = CorrelationIdMapping(
    map_from="..."  # required — The path into the event the correlation ID is taken from, for example body.fileId. The path must be in the schema of the event type, and a value of any type is written as a string
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

