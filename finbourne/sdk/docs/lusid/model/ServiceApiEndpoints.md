# ServiceApiEndpoints

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **application** | **str** | Required | *No description available.* |
| **endpoints** | [List[ApiEndpoint]](ApiEndpoint.md) | Required | *No description available.* |
| **href** | **str** | Optional | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.ServiceApiEndpoints import ServiceApiEndpoints

instance = ServiceApiEndpoints(
    application="...",  # required
    endpoints=[],  # required
    href="...",  # optional — The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.
    links=[]  # optional
)
```

- [ApiEndpoint](ApiEndpoint.md)
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

