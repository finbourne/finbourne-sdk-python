# ListUsersResponse

Users directory query response
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **href** | **str** | Optional | Uri of this response |
| **values** | [Dict[str, UserSummary]](UserSummary.md) | Optional | Successful entities, indexed by their id |
| **failed** | [Dict[str, ErrorDetail]](ErrorDetail.md) | Optional | Failed entities, indexed by their id |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.identity.models.ListUsersResponse import ListUsersResponse

instance = ListUsersResponse(
    href="...",  # optional — Uri of this response
    values=UserSummary(...),  # optional — Successful entities, indexed by their id
    failed=ErrorDetail(...),  # optional — Failed entities, indexed by their id
    links=[]  # optional
)
```

- [UserSummary](UserSummary.md) — used in `values`
- [ErrorDetail](ErrorDetail.md) — used in `failed`
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

