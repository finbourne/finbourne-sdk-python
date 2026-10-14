# LaunchedBy

The Launcher that started a run of a Workflow
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **launcher_id** | **str** | Required | The ID of the Launcher inside its Workflow |
| **launcher_type** | **str** | Required | The type of Launcher. One of - Schedule, Event |
| **launcher_as_at** | **datetime** | Required | The version.asAtModified of the Launcher definition that fired |
| **fired_at** | **datetime** | Required | When the Launcher fired. For a Schedule Launcher this is the scheduled trigger time, and for an Event Launcher it is the timestamp of the event |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.workflow.models.LaunchedBy import LaunchedBy

instance = LaunchedBy(
    launcher_id="...",  # required — The ID of the Launcher inside its Workflow
    launcher_type="...",  # required — The type of Launcher. One of - Schedule, Event
    launcher_as_at=datetime.now(),  # required — The version.asAtModified of the Launcher definition that fired
    fired_at=datetime.now()  # required — When the Launcher fired. For a Schedule Launcher this is the scheduled trigger time, and for an Event Launcher it is the timestamp of the event
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

