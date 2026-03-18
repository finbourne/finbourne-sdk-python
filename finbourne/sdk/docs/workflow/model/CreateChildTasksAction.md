# CreateChildTasksAction

Defines a Create Child Tasks Action
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **type** | **str** | Required | Type name for this Action |
| **child_task_configurations** | [List[CreateChildTaskConfiguration]](CreateChildTaskConfiguration.md) | Required | The Child Task Configurations |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.workflow.models.CreateChildTasksAction import CreateChildTasksAction

instance = CreateChildTasksAction(
    type="...",  # required — Type name for this Action
    child_task_configurations=[]  # required — The Child Task Configurations
)
```

- [CreateChildTaskConfiguration](CreateChildTaskConfiguration.md) — used in `child_task_configurations`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

