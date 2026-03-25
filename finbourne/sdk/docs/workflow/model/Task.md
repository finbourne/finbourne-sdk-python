# Task

Defines a Task created based on a Task Definition
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **id** | **UUID** | Required | The unique id for this Task |
| **task_definition_id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **task_definition_version** | [TaskDefinitionVersion](TaskDefinitionVersion.md) | Required | *No description available.* |
| **task_definition_display_name** | **str** | Required | The display name of the Task Definition used by this Task |
| **state** | **str** | Required | Current State |
| **ultimate_parent_task** | [TaskSummary](TaskSummary.md) | Required | *No description available.* |
| **parent_task** | [TaskSummary](TaskSummary.md) | Optional | *No description available.* |
| **child_tasks** | [List[TaskSummary]](TaskSummary.md) | Optional | This Task&#39;s child tasks |
| **correlation_ids** | **List[str]** | Optional | User-provided ID used to link entities and tasks |
| **version** | [VersionInfo](VersionInfo.md) | Optional | *No description available.* |
| **terminal_state** | **bool** | Required | True if no onward transitions are possible |
| **as_at_last_transition** | **datetime** | Optional | Last Transition timestamp |
| **fields** | [List[TaskInstanceField]](TaskInstanceField.md) | Optional | Fields and their latest values - should correspond with the Task Definition field schema |
| **stacking_key** | **str** | Optional | The key used to determine which stack to add the Task to |
| **stack** | [Stack](Stack.md) | Optional | *No description available.* |
| **action_log_id_created** | **UUID** | Optional | The Id of the Action that created this Task |
| **action_log_id_modified** | **UUID** | Optional | The Id of the Action that last modified this Task |
| **action_log_id_submitted** | **UUID** | Optional | The Id of the last Action submitted by this Task |
| **hierarchical_position** | **str** | Optional | The hierarchical position of this Task: UltimateParent, IntermediateParent, Child, or Standalone |
| **completion_status** | **str** | Optional | The completion status of this Task: NotStarted, InProgress, or Completed |
| **open_duration** | **int** | Optional | Duration in seconds since the Task was created. If the Task is Completed, this is the duration from creation to the last transition. |
| **open_duration_since_last_update** | **int** | Optional | Duration in seconds since the Task was last updated. 0 if the Task is Completed. |
| **open_duration_since_last_transition** | **int** | Optional | Duration in seconds since the Task last transitioned. 0 if the Task is Completed. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.workflow.models.Task import Task

instance = Task(
    id="...",  # required — The unique id for this Task
    task_definition_id=ResourceId(...),  # required
    task_definition_version=TaskDefinitionVersion(...),  # required
    task_definition_display_name="...",  # required — The display name of the Task Definition used by this Task
    state="...",  # required — Current State
    ultimate_parent_task=TaskSummary(...),  # required
    parent_task=TaskSummary(...),  # optional
    child_tasks=[],  # optional — This Task&#39;s child tasks
    correlation_ids=,  # optional — User-provided ID used to link entities and tasks
    version=VersionInfo(...),  # optional
    terminal_state=True,  # required — True if no onward transitions are possible
    as_at_last_transition=datetime.now(),  # optional — Last Transition timestamp
    fields=[],  # optional — Fields and their latest values - should correspond with the Task Definition field schema
    stacking_key="...",  # optional — The key used to determine which stack to add the Task to
    stack=Stack(...),  # optional
    action_log_id_created="...",  # optional — The Id of the Action that created this Task
    action_log_id_modified="...",  # optional — The Id of the Action that last modified this Task
    action_log_id_submitted="...",  # optional — The Id of the last Action submitted by this Task
    hierarchical_position="...",  # optional — The hierarchical position of this Task: UltimateParent, IntermediateParent, Child, or Standalone
    completion_status="...",  # optional — The completion status of this Task: NotStarted, InProgress, or Completed
    open_duration=0,  # optional — Duration in seconds since the Task was created. If the Task is Completed, this is the duration from creation to the last transition.
    open_duration_since_last_update=0,  # optional — Duration in seconds since the Task was last updated. 0 if the Task is Completed.
    open_duration_since_last_transition=0  # optional — Duration in seconds since the Task last transitioned. 0 if the Task is Completed.
)
```

- [ResourceId](ResourceId.md)
- [TaskDefinitionVersion](TaskDefinitionVersion.md)
- [TaskSummary](TaskSummary.md)
- [TaskSummary](TaskSummary.md)
- [TaskSummary](TaskSummary.md) — used in `child_tasks`
- [VersionInfo](VersionInfo.md)
- [TaskInstanceField](TaskInstanceField.md) — used in `fields`
- [Stack](Stack.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

