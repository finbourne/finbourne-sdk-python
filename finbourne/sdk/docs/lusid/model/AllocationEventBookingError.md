# AllocationEventBookingError

One posting a booking could not write.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **code** | **str** | Optional | The rule or write step that failed, for instance WriteFailed. |
| **id** | **str** | Optional | The identifier of the posting that could not be written. |
| **message** | **str** | Optional | What went wrong. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.AllocationEventBookingError import AllocationEventBookingError

instance = AllocationEventBookingError(
    code="...",  # optional — The rule or write step that failed, for instance WriteFailed.
    id="...",  # optional — The identifier of the posting that could not be written.
    message="..."  # optional — What went wrong.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

