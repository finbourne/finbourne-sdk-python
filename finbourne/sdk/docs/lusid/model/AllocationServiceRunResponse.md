# AllocationServiceRunResponse

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **values** | [List[ResourceId]](ResourceId.md) | Optional | *No description available.* |
| **failed** | [Dict[str, ErrorDetail]](ErrorDetail.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.AllocationServiceRunResponse import AllocationServiceRunResponse

instance = AllocationServiceRunResponse(
    values=[],  # optional
    failed=ErrorDetail(...)  # optional
)
```


## Related Models

- [ResourceId](ResourceId.md)
- [ErrorDetail](ErrorDetail.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

