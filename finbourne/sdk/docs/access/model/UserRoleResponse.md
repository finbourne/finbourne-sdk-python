# UserRoleResponse

Response object from the user role API
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **resource** | [RoleResourceRequest](RoleResourceRequest.md) | Required | *No description available.* |
| **id** | [RoleId](RoleId.md) | Required | *No description available.* |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.access.models.UserRoleResponse import UserRoleResponse

instance = UserRoleResponse(
    resource=RoleResourceRequest(...),  # required
    id=RoleId(...),  # required
    links=[]  # optional
)
```


## Related Models

- [RoleResourceRequest](RoleResourceRequest.md)
- [RoleId](RoleId.md)
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

