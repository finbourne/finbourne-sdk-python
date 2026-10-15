# AllocationEventNoticeEvent

The allocation event a notice is issued for.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **type** | **str** | Required | The type of the allocation event. |
| **event_date** | **datetime** | Required | The effective date of the allocation event. |
| **notice_date** | **datetime** | Optional | The date the notice is issued. |
| **due_date** | **datetime** | Optional | The date the payment is due. |
| **status** | **str** | Required | The status of the allocation event. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.AllocationEventNoticeEvent import AllocationEventNoticeEvent

instance = AllocationEventNoticeEvent(
    id=ResourceId(...),  # required
    type="...",  # required — The type of the allocation event.
    event_date=datetime.now(),  # required — The effective date of the allocation event.
    notice_date=datetime.now(),  # optional — The date the notice is issued.
    due_date=datetime.now(),  # optional — The date the payment is due.
    status="..."  # required — The status of the allocation event.
)
```


## Related Models

- [ResourceId](ResourceId.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

