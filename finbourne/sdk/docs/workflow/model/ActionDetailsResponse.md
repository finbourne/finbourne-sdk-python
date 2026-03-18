# ActionDetailsResponse

Abstracts the kinds of Actions available in a read-only form

## oneOf Type

`ActionDetailsResponse` can be one of the following types:

* [CreateChildTasksActionResponse](./CreateChildTasksActionResponse.md)
* [RunWorkerActionResponse](./RunWorkerActionResponse.md)
* [TriggerParentTaskActionResponse](./TriggerParentTaskActionResponse.md)

## Usage

### Creating from a compatible type

```python
from finbourne.sdk.services.workflow.models.ActionDetailsResponse import ActionDetailsResponse

# Construct using any of the compatible types above
create_child_tasks_action_response_instance = workflow.models.create_child_tasks_action_response.CreateChildTasksActionResponse(
                        type = 'CreateChildTasks', 
                        child_task_configurations = [
                            workflow.models.create_child_task_configuration.CreateChildTaskConfiguration(
                                task_definition_id = workflow.models.resource_id.ResourceId(
                                    scope = '', 
                                    code = '', ), 
                                task_definition_as_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                initial_trigger = 'z', 
                                child_task_fields = {
                                    'key' : workflow.models.field_mapping.FieldMapping(
                                        map_from = '', 
                                        set_to = null, )
                                    }, 
                                map_stacking_key_from = '', )
                            ], )

instance = ActionDetailsResponse(create_child_tasks_action_response_instance)
```

## Related Models

- [CreateChildTasksActionResponse](./CreateChildTasksActionResponse.md)
- [RunWorkerActionResponse](./RunWorkerActionResponse.md)
- [TriggerParentTaskActionResponse](./TriggerParentTaskActionResponse.md)

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

