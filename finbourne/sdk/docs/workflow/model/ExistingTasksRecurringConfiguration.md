# ExistingTasksRecurringConfiguration

Behaviour applied to an existing (non-terminal) child task whose stacking key matches one or more new child task candidates
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **increment_as_at_modified** | **bool** | Optional | When true, the existing task&#39;s asAtModified is incremented even if no other change (Trigger or MergeFields) is applied |
| **trigger** | **str** | Optional | The existing task receives this trigger |
| **merge_fields** | **List[str]** | Optional | The named fields on the existing task are updated with the values from the latest run. Only applies where the new-to-existing stacking key cardinality is one-to-one or one-to-many; unspecified fields are untouched. Data will be merged in even if these fields are in a read-only state. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.workflow.models.ExistingTasksRecurringConfiguration import ExistingTasksRecurringConfiguration

instance = ExistingTasksRecurringConfiguration(
    increment_as_at_modified=True,  # optional — When true, the existing task&#39;s asAtModified is incremented even if no other change (Trigger or MergeFields) is applied
    trigger="...",  # optional — The existing task receives this trigger
    merge_fields=  # optional — The named fields on the existing task are updated with the values from the latest run. Only applies where the new-to-existing stacking key cardinality is one-to-one or one-to-many; unspecified fields are untouched. Data will be merged in even if these fields are in a read-only state.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

