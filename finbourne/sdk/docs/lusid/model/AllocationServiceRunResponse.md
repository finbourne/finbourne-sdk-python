# AllocationServiceRunResponse

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **values** | [List[ResourceId]](ResourceId.md) | Optional | The placements that were allocated successfully. |
| **failed** | [Dict[str, ErrorDetail]](ErrorDetail.md) | Optional | The placements that could not be allocated, keyed by placement, with the reason. |
| **allocations** | [List[AllocationServiceRunAllocation]](AllocationServiceRunAllocation.md) | Optional | Every allocation the run touched across the successful placements, each with its outcome. |
| **warnings** | [List[AllocationServiceRunWarning]](AllocationServiceRunWarning.md) | Optional | Warnings raised while allocating the successful placements. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.AllocationServiceRunResponse import AllocationServiceRunResponse

instance = AllocationServiceRunResponse(
    values=[],  # optional — The placements that were allocated successfully.
    failed=ErrorDetail(...),  # optional — The placements that could not be allocated, keyed by placement, with the reason.
    allocations=[],  # optional — Every allocation the run touched across the successful placements, each with its outcome.
    warnings=[]  # optional — Warnings raised while allocating the successful placements.
)
```


## Related Models

- [ResourceId](ResourceId.md) — used in `values`
- [ErrorDetail](ErrorDetail.md) — used in `failed`
- [AllocationServiceRunAllocation](AllocationServiceRunAllocation.md) — used in `allocations`
- [AllocationServiceRunWarning](AllocationServiceRunWarning.md) — used in `warnings`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

