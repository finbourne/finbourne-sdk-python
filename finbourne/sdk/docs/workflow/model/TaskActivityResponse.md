# TaskActivityResponse

Readonly information about how the worker should be executed

## oneOf Type

`TaskActivityResponse` can be one of the following types:

* [CreateNewTaskActivityResponse](./CreateNewTaskActivityResponse.md)
* [UpdateMatchingTasksActivityResponse](./UpdateMatchingTasksActivityResponse.md)

## Usage

### Creating from a compatible type

```python
from finbourne.sdk.services.workflow.models.TaskActivityResponse import TaskActivityResponse

# Construct using any of the compatible types above
create_new_task_activity_response_instance = workflow.models.create_new_task_activity_response.CreateNewTaskActivityResponse(
                        type = 'CreateNewTask', 
                        initial_trigger = '', 
                        correlation_ids = [
                            workflow.models.event_handler_mapping.EventHandlerMapping(
                                map_from = '', 
                                set_to = '', )
                            ], 
                        task_fields = {
                            'key' : workflow.models.field_mapping.FieldMapping(
                                map_from = '', 
                                set_to = null, )
                            }, 
                        schedule_dependent_task_fields = {
                            'key' : workflow.models.scheduled_time_adjustment.ScheduledTimeAdjustment(
                                date_adjustment = workflow.models.date_adjustment.DateAdjustment(
                                    delta_days = 56, 
                                    business_day_adjustment = '', ), 
                                time_adjustment = workflow.models.time_adjustment.TimeAdjustment(
                                    set_to = workflow.models.specified_time.SpecifiedTime(
                                        hours = 56, 
                                        minutes = 56, 
                                        type = 'Specified', ), ), )
                            }, )

instance = TaskActivityResponse(create_new_task_activity_response_instance)
```

## Related Models

- [CreateNewTaskActivityResponse](./CreateNewTaskActivityResponse.md)
- [UpdateMatchingTasksActivityResponse](./UpdateMatchingTasksActivityResponse.md)

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

