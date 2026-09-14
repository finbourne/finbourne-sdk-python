# ReRunConfiguration

Defines how re-run results for a given (child) TaskDefinitionId should be reconciled against existing (non-terminal) child tasks of the same parent Task instance.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **task_definition_id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **results_recurring** | [ResultsRecurringConfiguration](ResultsRecurringConfiguration.md) | Required | *No description available.* |
| **results_not_recurring** | [ResultsNotRecurringConfiguration](ResultsNotRecurringConfiguration.md) | Required | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.workflow.models.ReRunConfiguration import ReRunConfiguration

instance = ReRunConfiguration(
    task_definition_id=ResourceId(...),  # required
    results_recurring=ResultsRecurringConfiguration(...),  # required
    results_not_recurring=ResultsNotRecurringConfiguration(...)  # required
)
```


## Related Models

- [ResourceId](ResourceId.md)
- [ResultsRecurringConfiguration](ResultsRecurringConfiguration.md)
- [ResultsNotRecurringConfiguration](ResultsNotRecurringConfiguration.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

