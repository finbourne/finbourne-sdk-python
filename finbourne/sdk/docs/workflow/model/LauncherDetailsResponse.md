# LauncherDetailsResponse

What makes a Launcher start a run of its Workflow, and what it puts on the root task when it does, in a read only form.              The members here belong to every Launcher. Finbourne.Workflow.WebApi.Common.Dto.Json.Launchers.ScheduleLauncherDetailsResponse and Finbourne.Workflow.WebApi.Common.Dto.Json.Launchers.EventLauncherDetailsResponse add what only a schedule or only an event needs

## oneOf Type

`LauncherDetailsResponse` can be one of the following types:

* [EventLauncherDetailsResponse](./EventLauncherDetailsResponse.md)
* [ScheduleLauncherDetailsResponse](./ScheduleLauncherDetailsResponse.md)

## Usage

### Creating from a compatible type

```python
from finbourne.sdk.services.workflow.models.LauncherDetailsResponse import LauncherDetailsResponse

# Construct using any of the compatible types above
event_launcher_details_response_instance = workflow.models.event_launcher_details_response.EventLauncherDetailsResponse(
                        launcher_type = 'Event', 
                        event_matching_pattern = workflow.models.launcher_event_matching_pattern.LauncherEventMatchingPattern(
                            event_type = 'EiOTgswWMEJTcMoSLlNYUL', 
                            filter = '', ), 
                        map_task_fields = {
                            'key' : workflow.models.event_task_field_mapping.EventTaskFieldMapping(
                                map_from = '', 
                                date_time_adjustment = workflow.models.date_time_adjustment.DateTimeAdjustment(
                                    calendar_context = 'z', 
                                    date_adjustment = workflow.models.date_adjustment.DateAdjustment(
                                        delta_days = 56, 
                                        business_day_adjustment = '', ), 
                                    time_adjustment = workflow.models.time_adjustment.TimeAdjustment(
                                        set_to = workflow.models.specified_time.SpecifiedTime(
                                            hours = 56, 
                                            minutes = 56, 
                                            type = 'Specified', ), ), ), )
                            }, 
                        map_correlation_ids = [
                            workflow.models.correlation_id_mapping.CorrelationIdMapping(
                                map_from = '', )
                            ], 
                        run_as_user_id = workflow.models.launcher_mapping.LauncherMapping(
                            map_from = '', ), 
                        set_task_fields = {
                            'key' : null
                            }, 
                        set_correlation_ids = [
                            ''
                            ], 
                        initial_trigger = '', )

instance = LauncherDetailsResponse(event_launcher_details_response_instance)
```

## Related Models

- [EventLauncherDetailsResponse](./EventLauncherDetailsResponse.md)
- [ScheduleLauncherDetailsResponse](./ScheduleLauncherDetailsResponse.md)

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

