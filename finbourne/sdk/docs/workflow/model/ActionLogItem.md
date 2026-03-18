# ActionLogItem

A log item for a given Action Log
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **timestamp** | **datetime** | Required | The timestamp of the log item |
| **log_type** | **str** | Required | The type of log item |
| **details** | **str** | Optional | The details of the log item |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.workflow.models.ActionLogItem import ActionLogItem

instance = ActionLogItem(
    timestamp=datetime.now(),  # required — The timestamp of the log item
    log_type="...",  # required — The type of log item
    details="..."  # optional — The details of the log item
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

