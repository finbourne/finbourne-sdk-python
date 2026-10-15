# ProcessingGroupRequest

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **code** | **str** | Required | The code of the Processing Group. Together with the scope this uniquely identifies the Processing Group. |
| **display_name** | **str** | Required | The name of the Processing Group. |
| **description** | **str** | Optional | A description for the Processing Group. |
| **schedule** | [ProcessingGroupSchedule](ProcessingGroupSchedule.md) | Required | *No description available.* |
| **reference_list_id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **workflow_id** | [ResourceId](ResourceId.md) | Optional | *No description available.* |
| **list_exception_filter** | **str** | Optional | A filter selecting reference list items to exclude whenever this Processing Group resolves its reference list. Optional. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.ProcessingGroupRequest import ProcessingGroupRequest

instance = ProcessingGroupRequest(
    code="...",  # required — The code of the Processing Group. Together with the scope this uniquely identifies the Processing Group.
    display_name="...",  # required — The name of the Processing Group.
    description="...",  # optional — A description for the Processing Group.
    schedule=ProcessingGroupSchedule(...),  # required
    reference_list_id=ResourceId(...),  # required
    workflow_id=ResourceId(...),  # optional
    list_exception_filter="..."  # optional — A filter selecting reference list items to exclude whenever this Processing Group resolves its reference list. Optional.
)
```

- [ProcessingGroupSchedule](ProcessingGroupSchedule.md)
- [ResourceId](ResourceId.md)
- [ResourceId](ResourceId.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

