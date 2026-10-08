# LauncherEdge

Represents the relationship between a Launcher of a Workflow and the Task Definition it starts a run of
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **launcher_id** | **str** | Optional | The identifier of the Launcher inside its Workflow |
| **target_task_definition** | [VersionedTaskDefinitionId](VersionedTaskDefinitionId.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.workflow.models.LauncherEdge import LauncherEdge

instance = LauncherEdge(
    launcher_id="...",  # optional — The identifier of the Launcher inside its Workflow
    target_task_definition=VersionedTaskDefinitionId(...)  # optional
)
```

- [VersionedTaskDefinitionId](VersionedTaskDefinitionId.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

