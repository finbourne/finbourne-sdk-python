# RoleResponse

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **id** | **str** | Required | The role&#39;s system supplied unique identifier |
| **role_id** | [RoleId](RoleId.md) | Required | *No description available.* |
| **source** | **str** | Required | The source of the role |
| **name** | **str** | Required | The role name, which must be unique within the system. |
| **description** | **str** | Optional | The description for this role |
| **saml_name** | **str** | Optional | The name to use on the SAML request if assigning this role via SAML Just in Time (JIT) |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.identity.models.RoleResponse import RoleResponse

instance = RoleResponse(
    id="...",  # required — The role&#39;s system supplied unique identifier
    role_id=RoleId(...),  # required
    source="...",  # required — The source of the role
    name="...",  # required — The role name, which must be unique within the system.
    description="...",  # optional — The description for this role
    saml_name="..."  # optional — The name to use on the SAML request if assigning this role via SAML Just in Time (JIT)
)
```

- [RoleId](RoleId.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

