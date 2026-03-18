# UserRoleCreationRequest

Dto used to request creating a user's role
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **user_id** | **str** | Required | The Id of the user for whom to create the role. |
| **resource** | [PolicyIdRoleResource](PolicyIdRoleResource.md) | Required | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.access.models.UserRoleCreationRequest import UserRoleCreationRequest

instance = UserRoleCreationRequest(
    user_id="...",  # required — The Id of the user for whom to create the role.
    resource=PolicyIdRoleResource(...)  # required
)
```

- [PolicyIdRoleResource](PolicyIdRoleResource.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

