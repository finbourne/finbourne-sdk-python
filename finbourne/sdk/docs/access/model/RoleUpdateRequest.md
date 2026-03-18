# RoleUpdateRequest

Role update does not allow the changing of the id
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **description** | **str** | Optional | The description of the role |
| **resource** | [RoleResourceRequest](RoleResourceRequest.md) | Required | *No description available.* |
| **when** | [WhenSpec](WhenSpec.md) | Required | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.access.models.RoleUpdateRequest import RoleUpdateRequest

instance = RoleUpdateRequest(
    description="...",  # optional — The description of the role
    resource=RoleResourceRequest(...),  # required
    when=WhenSpec(...)  # required
)
```

- [RoleResourceRequest](RoleResourceRequest.md)
- [WhenSpec](WhenSpec.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

