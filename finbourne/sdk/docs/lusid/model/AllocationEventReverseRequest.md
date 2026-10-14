# AllocationEventReverseRequest

The request used to reverse a booked Allocation Event: why, and when the mirror postings are dated.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **reason** | **str** | Required | Why the booked event is being reversed. |
| **effective_at** | **datetime** | Optional | The date to post the mirror entries at. Defaults to the original event date unless that period is closed, when it defaults to the current date. |
| **backdated** | **bool** | Optional | Whether to post the mirror entries at the original event date even when that period is closed. Defaults to false. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.AllocationEventReverseRequest import AllocationEventReverseRequest

instance = AllocationEventReverseRequest(
    reason="...",  # required — Why the booked event is being reversed.
    effective_at=datetime.now(),  # optional — The date to post the mirror entries at. Defaults to the original event date unless that period is closed, when it defaults to the current date.
    backdated=True  # optional — Whether to post the mirror entries at the original event date even when that period is closed. Defaults to false.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

