# GetFlowConventionsResponse

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **href** | **str** | Optional | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. |
| **value** | [FlowConventions](FlowConventions.md) | Optional | *No description available.* |
| **failed** | [Dict[str, ErrorDetail]](ErrorDetail.md) | Optional | The identifiers that did not resolve to a conventions along with the nature of the failure. |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.GetFlowConventionsResponse import GetFlowConventionsResponse

instance = GetFlowConventionsResponse(
    href="...",  # optional — The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.
    value=FlowConventions(...),  # optional
    failed=ErrorDetail(...),  # optional — The identifiers that did not resolve to a conventions along with the nature of the failure.
    links=[]  # optional
)
```

- [FlowConventions](FlowConventions.md)
- [ErrorDetail](ErrorDetail.md) — used in `failed`
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

