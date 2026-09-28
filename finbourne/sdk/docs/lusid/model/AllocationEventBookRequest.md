# AllocationEventBookRequest

The request used to book a computed Allocation Event: the reference under which its shares were posted.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **booking_reference** | **str** | Required | The reference under which the computed shares were posted, for instance a journal entry code. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.AllocationEventBookRequest import AllocationEventBookRequest

instance = AllocationEventBookRequest(
    booking_reference="..."  # required — The reference under which the computed shares were posted, for instance a journal entry code.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

