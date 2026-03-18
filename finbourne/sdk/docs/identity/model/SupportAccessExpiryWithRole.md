# SupportAccessExpiryWithRole

Time at which the support access granted for a role expires
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **expiry** | **datetime** | Required | DateTimeOffset at which the access will be revoked |
| **permitted_role** | **str** | Required | Unique identifier for permitted role.  Use GET /identity/api/authentication/support-roles to lookup role label/code from identifier. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.identity.models.SupportAccessExpiryWithRole import SupportAccessExpiryWithRole

instance = SupportAccessExpiryWithRole(
    expiry=datetime.now(),  # required — DateTimeOffset at which the access will be revoked
    permitted_role="..."  # required — Unique identifier for permitted role.  Use GET /identity/api/authentication/support-roles to lookup role label/code from identifier.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

