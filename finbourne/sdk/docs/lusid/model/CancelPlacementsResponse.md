# CancelPlacementsResponse

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **href** | **str** | Optional | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. |
| **values** | [Dict[str, CancelledPlacementResult]](CancelledPlacementResult.md) | Optional | The placements which have been successfully cancelled. |
| **failed** | [Dict[str, ErrorDetail]](ErrorDetail.md) | Optional | The placements that could not be cancelled, along with a reason for their failure. |
| **metadata** | **Dict[str, Optional[List[ResponseMetaData]]]** | Optional | Meta data associated with the cancellation event. |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.CancelPlacementsResponse import CancelPlacementsResponse

instance = CancelPlacementsResponse(
    href="...",  # optional — The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.
    values=CancelledPlacementResult(...),  # optional — The placements which have been successfully cancelled.
    failed=ErrorDetail(...),  # optional — The placements that could not be cancelled, along with a reason for their failure.
    metadata=,  # optional — Meta data associated with the cancellation event.
    links=[]  # optional
)
```

- [CancelledPlacementResult](CancelledPlacementResult.md) — used in `values`
- [ErrorDetail](ErrorDetail.md) — used in `failed`
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

