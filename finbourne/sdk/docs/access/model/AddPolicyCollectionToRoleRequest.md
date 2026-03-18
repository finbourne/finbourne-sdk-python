# AddPolicyCollectionToRoleRequest

Request body used to add Policy Collections to a Role
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **policy_collections** | [List[PolicyCollectionId]](PolicyCollectionId.md) | Required | Identifiers of policy collections to add to a role |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.access.models.AddPolicyCollectionToRoleRequest import AddPolicyCollectionToRoleRequest

instance = AddPolicyCollectionToRoleRequest(
    policy_collections=[]  # required — Identifiers of policy collections to add to a role
)
```


## Related Models

- [PolicyCollectionId](PolicyCollectionId.md) — used in `policy_collections`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

