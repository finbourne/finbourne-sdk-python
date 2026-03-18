# RunWorkerAction

Defines a Run Worker Action
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **type** | **str** | Required | Type name for this Action |
| **worker_id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **worker_as_at** | **datetime** | Optional | Worker AsAt |
| **worker_parameters** | [Dict[str, FieldMapping]](FieldMapping.md) | Optional | Parameters for this Worker |
| **worker_status_triggers** | [WorkerStatusTriggers](WorkerStatusTriggers.md) | Optional | *No description available.* |
| **child_task_configurations** | [List[ResultantChildTaskConfiguration]](ResultantChildTaskConfiguration.md) | Optional | Tasks can be generated from run worker results; this is the configuration |
| **worker_timeout** | **int** | Optional | Worker WorkerTimeout in seconds |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.workflow.models.RunWorkerAction import RunWorkerAction

instance = RunWorkerAction(
    type="...",  # required — Type name for this Action
    worker_id=ResourceId(...),  # required
    worker_as_at=datetime.now(),  # optional — Worker AsAt
    worker_parameters=FieldMapping(...),  # optional — Parameters for this Worker
    worker_status_triggers=WorkerStatusTriggers(...),  # optional
    child_task_configurations=[],  # optional — Tasks can be generated from run worker results; this is the configuration
    worker_timeout=0  # optional — Worker WorkerTimeout in seconds
)
```

- [ResourceId](ResourceId.md)
- [FieldMapping](FieldMapping.md) — used in `worker_parameters`
- [WorkerStatusTriggers](WorkerStatusTriggers.md)
- [ResultantChildTaskConfiguration](ResultantChildTaskConfiguration.md) — used in `child_task_configurations`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

