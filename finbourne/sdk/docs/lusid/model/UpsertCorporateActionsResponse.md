# UpsertCorporateActionsResponse

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **href** | **str** | Optional | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. |
| **values** | [Dict[str, CorporateAction]](CorporateAction.md) | Optional | The corporate actions which have been successfully updated or inserted. |
| **failed** | [Dict[str, ErrorDetail]](ErrorDetail.md) | Optional | The corporate actions that could not be updated or inserted along with a reason for their failure. |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.UpsertCorporateActionsResponse import UpsertCorporateActionsResponse

instance = UpsertCorporateActionsResponse(
    href="...",  # optional — The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.
    values=CorporateAction(...),  # optional — The corporate actions which have been successfully updated or inserted.
    failed=ErrorDetail(...),  # optional — The corporate actions that could not be updated or inserted along with a reason for their failure.
    links=[]  # optional
)
```

- [CorporateAction](CorporateAction.md) — used in `values`
- [ErrorDetail](ErrorDetail.md) — used in `failed`
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

