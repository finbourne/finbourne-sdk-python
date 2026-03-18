# CreateRoleRequest

Specifies the information required to create a new role.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **name** | **str** | Required | The role name, which must be unique within the system. |
| **description** | **str** | Optional | The description for this role |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.identity.models.CreateRoleRequest import CreateRoleRequest

instance = CreateRoleRequest(
    name="...",  # required — The role name, which must be unique within the system.
    description="..."  # optional — The description for this role
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

