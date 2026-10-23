# CreateChildTasksAction

Defines a Create Child Tasks Action
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **type** | **str** | Required | Type name for this Action |
| **child_task_configurations** | [List[CreateChildTaskConfiguration]](CreateChildTaskConfiguration.md) | Required | The Child Task Configurations |
| **ordering** | **str** | Optional | How the created child tasks are ordered for execution: Parallel (default) or Series. In Series the child tasks form a chain and only the first is started; each later one is started by its predecessor&#39;s TriggerNextTask action, or by another trigger such as a TriggerChildTasks filter on previousTask. Without one, the chain stops after the first child. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.workflow.models.CreateChildTasksAction import CreateChildTasksAction

instance = CreateChildTasksAction(
    type="...",  # required — Type name for this Action
    child_task_configurations=[],  # required — The Child Task Configurations
    ordering="..."  # optional — How the created child tasks are ordered for execution: Parallel (default) or Series. In Series the child tasks form a chain and only the first is started; each later one is started by its predecessor&#39;s TriggerNextTask action, or by another trigger such as a TriggerChildTasks filter on previousTask. Without one, the chain stops after the first child.
)
```

- [CreateChildTaskConfiguration](CreateChildTaskConfiguration.md) — used in `child_task_configurations`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

