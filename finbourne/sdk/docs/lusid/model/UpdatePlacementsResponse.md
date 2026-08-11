# UpdatePlacementsResponse

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **href** | **str** | Optional | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. |
| **values** | [Dict[str, Placement]](Placement.md) | Optional | The placements which have been successfully updated. |
| **failed** | [Dict[str, ErrorDetail]](ErrorDetail.md) | Optional | The placements that could not be updated, along with a reason for their failure. |
| **metadata** | **Dict[str, Optional[List[ResponseMetaData]]]** | Optional | Meta data associated with the update event. |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.UpdatePlacementsResponse import UpdatePlacementsResponse

instance = UpdatePlacementsResponse(
    href="...",  # optional — The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.
    values=Placement(...),  # optional — The placements which have been successfully updated.
    failed=ErrorDetail(...),  # optional — The placements that could not be updated, along with a reason for their failure.
    metadata=,  # optional — Meta data associated with the update event.
    links=[]  # optional
)
```

- [Placement](Placement.md) — used in `values`
- [ErrorDetail](ErrorDetail.md) — used in `failed`
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

