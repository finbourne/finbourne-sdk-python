# ProcessingGroupNextScheduledDetails

The next scheduled occurrence of a Processing Group: the next execution date after the requested date,  together with the executed (resolved) contents of the reference list the Processing Group operates over.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **next_schedule_date** | **datetime** | Optional | The next execution date strictly after the requested date. |
| **resolved_reference_list** | [ReferenceList](ReferenceList.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.ProcessingGroupNextScheduledDetails import ProcessingGroupNextScheduledDetails

instance = ProcessingGroupNextScheduledDetails(
    next_schedule_date=datetime.now(),  # optional — The next execution date strictly after the requested date.
    resolved_reference_list=ReferenceList(...)  # optional
)
```

- [ReferenceList](ReferenceList.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

