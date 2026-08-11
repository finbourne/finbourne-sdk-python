# UpdateScheduleRequest

Create a schedule definition
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **job_id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **name** | **str** | Required | The updated name of the schedule |
| **description** | **str** | Required | The updated description of the schedule |
| **author** | **str** | Optional | The updated author of the schedule |
| **owner** | **str** | Optional | The update owner of the schedule |
| **arguments** | **Dict[str, Optional[str]]** | Optional | Updated arguments to be passed to the job Note: The new arguments will completely replace old arguments |
| **trigger** | [Trigger](Trigger.md) | Optional | *No description available.* |
| **notifications** | [List[Notification]](Notification.md) | Optional | Updated notifications for this schedule |
| **enabled** | **bool** | Optional | Specify whether schedule is enabled or not Defaults to true |
| **use_as_auth** | **str** | Optional | Id of user associated with schedule. All calls to FINBOURNE services as part of execution of this schedule will be authenticated as this  user. Can be null, in which case we&#39;ll default to that of the user  making this request |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.scheduler.models.UpdateScheduleRequest import UpdateScheduleRequest

instance = UpdateScheduleRequest(
    job_id=ResourceId(...),  # required
    name="...",  # required — The updated name of the schedule
    description="...",  # required — The updated description of the schedule
    author="...",  # optional — The updated author of the schedule
    owner="...",  # optional — The update owner of the schedule
    arguments=,  # optional — Updated arguments to be passed to the job Note: The new arguments will completely replace old arguments
    trigger=Trigger(...),  # optional
    notifications=[],  # optional — Updated notifications for this schedule
    enabled=True,  # optional — Specify whether schedule is enabled or not Defaults to true
    use_as_auth="..."  # optional — Id of user associated with schedule. All calls to FINBOURNE services as part of execution of this schedule will be authenticated as this  user. Can be null, in which case we&#39;ll default to that of the user  making this request
)
```


## Related Models

- [ResourceId](ResourceId.md)
- [Trigger](Trigger.md)
- [Notification](Notification.md) — used in `notifications`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

