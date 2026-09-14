# ResultsRecurringConfiguration

Behaviour applied to new child task candidates, and to existing child tasks, when their stacking keys match one another
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **new_tasks** | [NewTasksRecurringConfiguration](NewTasksRecurringConfiguration.md) | Required | *No description available.* |
| **existing_tasks** | [ExistingTasksRecurringConfiguration](ExistingTasksRecurringConfiguration.md) | Required | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.workflow.models.ResultsRecurringConfiguration import ResultsRecurringConfiguration

instance = ResultsRecurringConfiguration(
    new_tasks=NewTasksRecurringConfiguration(...),  # required
    existing_tasks=ExistingTasksRecurringConfiguration(...)  # required
)
```


## Related Models

- [NewTasksRecurringConfiguration](NewTasksRecurringConfiguration.md)
- [ExistingTasksRecurringConfiguration](ExistingTasksRecurringConfiguration.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

