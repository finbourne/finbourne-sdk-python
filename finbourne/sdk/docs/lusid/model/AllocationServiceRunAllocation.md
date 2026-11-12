# AllocationServiceRunAllocation

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **placement_id** | [ResourceId](ResourceId.md) | Optional | *No description available.* |
| **allocation** | [Allocation](Allocation.md) | Optional | *No description available.* |
| **outcome** | **str** | Optional | What the run did to this allocation. One of: Created (by this run), Updated (an existing allocation  whose fields changed), Unchanged (an existing allocation the run left as it was), Cancelled (moved to a  cancelled state or reduced to zero quantity), Skipped (left alone because transactions are already booked  against it; see the SkippedBooked warning). |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.AllocationServiceRunAllocation import AllocationServiceRunAllocation

instance = AllocationServiceRunAllocation(
    placement_id=ResourceId(...),  # optional
    allocation=Allocation(...),  # optional
    outcome="..."  # optional — What the run did to this allocation. One of: Created (by this run), Updated (an existing allocation  whose fields changed), Unchanged (an existing allocation the run left as it was), Cancelled (moved to a  cancelled state or reduced to zero quantity), Skipped (left alone because transactions are already booked  against it; see the SkippedBooked warning).
)
```


## Related Models

- [ResourceId](ResourceId.md)
- [Allocation](Allocation.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

