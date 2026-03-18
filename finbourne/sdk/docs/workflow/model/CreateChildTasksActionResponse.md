# CreateChildTasksActionResponse

Defines a read-only Create Child Tasks Action
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **type** | **str** | Optional | Type name for this Action |
| **child_task_configurations** | [List[CreateChildTaskConfiguration]](CreateChildTaskConfiguration.md) | Optional | The Child Task Configurations |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.workflow.models.CreateChildTasksActionResponse import CreateChildTasksActionResponse

instance = CreateChildTasksActionResponse(
    type="...",  # optional — Type name for this Action
    child_task_configurations=[]  # optional — The Child Task Configurations
)
```

- [CreateChildTaskConfiguration](CreateChildTaskConfiguration.md) — used in `child_task_configurations`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

