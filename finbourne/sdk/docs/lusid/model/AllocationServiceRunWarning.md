# AllocationServiceRunWarning

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **placement_id** | [ResourceId](ResourceId.md) | Optional | *No description available.* |
| **code** | **str** | Optional | The kind of warning. One of: OffMinimumIncrement (an allocation&#39;s quantity is not a multiple of the  instrument&#39;s minimum increment), SkippedBooked (an allocation was not changed because transactions are  already booked against it), ExecutionNotAllocated (an execution was excluded from the run). |
| **message** | **str** | Optional | A description of the warning and, where known, why it arose. |
| **allocation_id** | [ResourceId](ResourceId.md) | Optional | *No description available.* |
| **portfolio_id** | [ResourceId](ResourceId.md) | Optional | *No description available.* |
| **execution_id** | [ResourceId](ResourceId.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.AllocationServiceRunWarning import AllocationServiceRunWarning

instance = AllocationServiceRunWarning(
    placement_id=ResourceId(...),  # optional
    code="...",  # optional — The kind of warning. One of: OffMinimumIncrement (an allocation&#39;s quantity is not a multiple of the  instrument&#39;s minimum increment), SkippedBooked (an allocation was not changed because transactions are  already booked against it), ExecutionNotAllocated (an execution was excluded from the run).
    message="...",  # optional — A description of the warning and, where known, why it arose.
    allocation_id=ResourceId(...),  # optional
    portfolio_id=ResourceId(...),  # optional
    execution_id=ResourceId(...)  # optional
)
```


## Related Models

- [ResourceId](ResourceId.md)
- [ResourceId](ResourceId.md)
- [ResourceId](ResourceId.md)
- [ResourceId](ResourceId.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

