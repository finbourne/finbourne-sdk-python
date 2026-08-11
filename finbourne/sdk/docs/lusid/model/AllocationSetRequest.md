# AllocationSetRequest

A request to create or update multiple Allocations.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **allocation_requests** | [List[AllocationRequest]](AllocationRequest.md) | Optional | A collection of AllocationRequests. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.AllocationSetRequest import AllocationSetRequest

instance = AllocationSetRequest(
    allocation_requests=[]  # optional — A collection of AllocationRequests.
)
```


## Related Models

- [AllocationRequest](AllocationRequest.md) — used in `allocation_requests`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

