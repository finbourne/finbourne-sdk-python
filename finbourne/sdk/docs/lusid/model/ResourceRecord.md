# ResourceRecord

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **deployment_scope** | **str** | Required | The scope of the deployment this record is part of. |
| **deployment_code** | **str** | Required | The code of the deployment this record is part of. |
| **resource_id** | **str** | Required | The unique identifier of the resource associated with this record. |
| **format** | **str** | Required | A semver format identifier for the resource record. |
| **resource_type** | **str** | Required | The type of resource associated with this record. |
| **resource_state** | **object** | Required | The state of the resource associated with this record. |
| **dependencies** | **List[str]** | Required | A collection of resource identifiers that this resource depends on. |
| **tracking_state** | **object** | Optional | The tracking state of the resource record. |
| **version** | [Version](Version.md) | Optional | *No description available.* |
| **href** | **str** | Optional | The specific Uniform Resource Identifier (URI) for the resource record at the requested effective and asAt datetime. |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.ResourceRecord import ResourceRecord

instance = ResourceRecord(
    deployment_scope="...",  # required — The scope of the deployment this record is part of.
    deployment_code="...",  # required — The code of the deployment this record is part of.
    resource_id="...",  # required — The unique identifier of the resource associated with this record.
    format="...",  # required — A semver format identifier for the resource record.
    resource_type="...",  # required — The type of resource associated with this record.
    resource_state=,  # required — The state of the resource associated with this record.
    dependencies=,  # required — A collection of resource identifiers that this resource depends on.
    tracking_state=,  # optional — The tracking state of the resource record.
    version=Version(...),  # optional
    href="...",  # optional — The specific Uniform Resource Identifier (URI) for the resource record at the requested effective and asAt datetime.
    links=[]  # optional
)
```

- [Version](Version.md)
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

