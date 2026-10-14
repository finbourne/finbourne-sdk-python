# AllocationEventUnbookRequest

The request used to take a half-booked Allocation Event back to Computed, cancelling what it wrote.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **reason** | **str** | Required | Why the half-booked event is being taken back to Computed. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.AllocationEventUnbookRequest import AllocationEventUnbookRequest

instance = AllocationEventUnbookRequest(
    reason="..."  # required — Why the half-booked event is being taken back to Computed.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

