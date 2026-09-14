# ExistingTasksNotRecurringConfiguration

Behaviour applied to an existing (non-terminal) child task whose stacking key is not matched by any new child task candidate (i.e. it did not recur on this run)
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **trigger** | **str** | Optional | The existing task receives this trigger |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.workflow.models.ExistingTasksNotRecurringConfiguration import ExistingTasksNotRecurringConfiguration

instance = ExistingTasksNotRecurringConfiguration(
    trigger="..."  # optional — The existing task receives this trigger
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

