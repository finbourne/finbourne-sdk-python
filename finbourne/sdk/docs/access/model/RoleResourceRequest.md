# RoleResourceRequest

RoleResourceRequest
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **non_transitive_supervisor_role_resource** | [NonTransitiveSupervisorRoleResource](NonTransitiveSupervisorRoleResource.md) | Optional | *No description available.* |
| **policy_id_role_resource** | [PolicyIdRoleResource](PolicyIdRoleResource.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.access.models.RoleResourceRequest import RoleResourceRequest

instance = RoleResourceRequest(
    non_transitive_supervisor_role_resource=NonTransitiveSupervisorRoleResource(...),  # optional
    policy_id_role_resource=PolicyIdRoleResource(...)  # optional
)
```


## Related Models

- [NonTransitiveSupervisorRoleResource](NonTransitiveSupervisorRoleResource.md)
- [PolicyIdRoleResource](PolicyIdRoleResource.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

