# ResultsNotRecurringConfiguration

Behaviour applied when a new child task candidate's stacking key does not match any existing (non-terminal) child task, and to an existing child task whose stacking key is not matched by any new candidate
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **existing_tasks** | [ExistingTasksNotRecurringConfiguration](ExistingTasksNotRecurringConfiguration.md) | Required | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.workflow.models.ResultsNotRecurringConfiguration import ResultsNotRecurringConfiguration

instance = ResultsNotRecurringConfiguration(
    existing_tasks=ExistingTasksNotRecurringConfiguration(...)  # required
)
```


## Related Models

- [ExistingTasksNotRecurringConfiguration](ExistingTasksNotRecurringConfiguration.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

