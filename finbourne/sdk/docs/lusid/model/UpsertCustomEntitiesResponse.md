# UpsertCustomEntitiesResponse

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **href** | **str** | Optional | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. |
| **values** | [Dict[str, CustomEntityResponse]](CustomEntityResponse.md) | Optional | The custom-entities which have been successfully updated or created. |
| **staged** | [Dict[str, CustomEntityResponse]](CustomEntityResponse.md) | Optional | The custom-entities that have been staged for update or creation. |
| **failed** | [Dict[str, ErrorDetail]](ErrorDetail.md) | Optional | The custom-entities that could not be updated or created or were left unchanged without error along with a reason for their failure. |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.UpsertCustomEntitiesResponse import UpsertCustomEntitiesResponse

instance = UpsertCustomEntitiesResponse(
    href="...",  # optional — The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.
    values=CustomEntityResponse(...),  # optional — The custom-entities which have been successfully updated or created.
    staged=CustomEntityResponse(...),  # optional — The custom-entities that have been staged for update or creation.
    failed=ErrorDetail(...),  # optional — The custom-entities that could not be updated or created or were left unchanged without error along with a reason for their failure.
    links=[]  # optional
)
```

- [CustomEntityResponse](CustomEntityResponse.md) — used in `values`
- [CustomEntityResponse](CustomEntityResponse.md) — used in `staged`
- [ErrorDetail](ErrorDetail.md) — used in `failed`
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

