# CancelOrdersAndMoveRemainingResponse

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **href** | **str** | Optional | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. |
| **values** | [Dict[str, CancelOrderAndMoveRemainingResult]](CancelOrderAndMoveRemainingResult.md) | Optional | The orders which have been successfully cancelled, and any remaining quantities moved. |
| **failed** | [Dict[str, ErrorDetail]](ErrorDetail.md) | Optional | The orders that could not be cancelled, along with a reason for their failure. |
| **metadata** | **Dict[str, Optional[List[ResponseMetaData]]]** | Optional | Meta data associated with the cancellation event. |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.CancelOrdersAndMoveRemainingResponse import CancelOrdersAndMoveRemainingResponse

instance = CancelOrdersAndMoveRemainingResponse(
    href="...",  # optional — The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.
    values=CancelOrderAndMoveRemainingResult(...),  # optional — The orders which have been successfully cancelled, and any remaining quantities moved.
    failed=ErrorDetail(...),  # optional — The orders that could not be cancelled, along with a reason for their failure.
    metadata=,  # optional — Meta data associated with the cancellation event.
    links=[]  # optional
)
```

- [CancelOrderAndMoveRemainingResult](CancelOrderAndMoveRemainingResult.md) — used in `values`
- [ErrorDetail](ErrorDetail.md) — used in `failed`
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

