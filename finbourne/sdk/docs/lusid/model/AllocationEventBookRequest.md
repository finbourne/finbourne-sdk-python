# AllocationEventBookRequest

The request used to book a computed Allocation Event: the reference under which its shares are posted, and  whether to only show what would be posted.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **booking_reference** | **str** | Required | The reference under which the computed shares were posted, for instance a journal entry code. |
| **dry_run** | **bool** | Optional | Whether to only build and return the posting plan without writing anything. Defaults to false. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.AllocationEventBookRequest import AllocationEventBookRequest

instance = AllocationEventBookRequest(
    booking_reference="...",  # required — The reference under which the computed shares were posted, for instance a journal entry code.
    dry_run=True  # optional — Whether to only build and return the posting plan without writing anything. Defaults to false.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

