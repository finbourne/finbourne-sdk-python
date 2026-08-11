# AddPolicyToRoleRequest

Request body used to add Policies to a Role
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **policies** | [List[PolicyId]](PolicyId.md) | Required | Identifiers of policies to add to a role |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.access.models.AddPolicyToRoleRequest import AddPolicyToRoleRequest

instance = AddPolicyToRoleRequest(
    policies=[]  # required — Identifiers of policies to add to a role
)
```


## Related Models

- [PolicyId](PolicyId.md) — used in `policies`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

