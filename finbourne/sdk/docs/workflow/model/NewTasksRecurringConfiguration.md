# NewTasksRecurringConfiguration

Behaviour applied to a new child task candidate whose stacking key matches an existing (non-terminal) child task
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **do_not_create** | **bool** | Optional | When true, the new child task will not be created |
| **initial_trigger_override** | **str** | Optional | When DoNotCreate is false, the new child task will be created with this trigger instead of the ChildTaskConfiguration&#39;s InitialTrigger |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.workflow.models.NewTasksRecurringConfiguration import NewTasksRecurringConfiguration

instance = NewTasksRecurringConfiguration(
    do_not_create=True,  # optional — When true, the new child task will not be created
    initial_trigger_override="..."  # optional — When DoNotCreate is false, the new child task will be created with this trigger instead of the ChildTaskConfiguration&#39;s InitialTrigger
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

