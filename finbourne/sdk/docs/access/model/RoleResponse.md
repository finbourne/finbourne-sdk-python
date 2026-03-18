# RoleResponse

Response object from the role API
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **id** | [RoleId](RoleId.md) | Required | *No description available.* |
| **role_hierarchy_index** | **int** | Required | The hierarchical index of the role |
| **description** | **str** | Optional | The description of the role |
| **resource** | [RoleResourceRequest](RoleResourceRequest.md) | Required | *No description available.* |
| **when** | [WhenSpec](WhenSpec.md) | Required | *No description available.* |
| **permission** | **str** | Required | The action key of the role |
| **limit** | **Dict[str, str]** | Optional | The identifiers of the role with the maximum privileges that this role can have |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.access.models.RoleResponse import RoleResponse

instance = RoleResponse(
    id=RoleId(...),  # required
    role_hierarchy_index=0,  # required — The hierarchical index of the role
    description="...",  # optional — The description of the role
    resource=RoleResourceRequest(...),  # required
    when=WhenSpec(...),  # required
    permission="...",  # required — The action key of the role
    limit=,  # optional — The identifiers of the role with the maximum privileges that this role can have
    links=[]  # optional
)
```


## Related Models

- [RoleId](RoleId.md)
- [RoleResourceRequest](RoleResourceRequest.md)
- [WhenSpec](WhenSpec.md)
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

