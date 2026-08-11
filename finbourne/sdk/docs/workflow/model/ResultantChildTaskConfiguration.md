# ResultantChildTaskConfiguration

Child Task Configuration
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **result_matching_pattern** | [ResultMatchingPattern](ResultMatchingPattern.md) | Optional | *No description available.* |
| **task_definition_id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **task_definition_as_at** | **datetime** | Optional | TaskDefinition AsAt timestamp |
| **initial_trigger** | **str** | Optional | The Initial Trigger for automatic start |
| **child_task_fields** | [Dict[str, FieldMapping]](FieldMapping.md) | Required | Field Mappings |
| **map_stacking_key_from** | **str** | Optional | The field to be mapped as the ChildTasks Stacking Key |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.workflow.models.ResultantChildTaskConfiguration import ResultantChildTaskConfiguration

instance = ResultantChildTaskConfiguration(
    result_matching_pattern=ResultMatchingPattern(...),  # optional
    task_definition_id=ResourceId(...),  # required
    task_definition_as_at=datetime.now(),  # optional — TaskDefinition AsAt timestamp
    initial_trigger="...",  # optional — The Initial Trigger for automatic start
    child_task_fields=FieldMapping(...),  # required — Field Mappings
    map_stacking_key_from="..."  # optional — The field to be mapped as the ChildTasks Stacking Key
)
```


## Related Models

- [ResultMatchingPattern](ResultMatchingPattern.md)
- [ResourceId](ResourceId.md)
- [FieldMapping](FieldMapping.md) — used in `child_task_fields`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

