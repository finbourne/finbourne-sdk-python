# CompositeBreakdownResponse

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **href** | **str** | Optional | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. |
| **results** | **Dict[str, Optional[List[CompositeBreakdown]]]** | Required | The Composite calculation with the constituens which were included. |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.CompositeBreakdownResponse import CompositeBreakdownResponse

instance = CompositeBreakdownResponse(
    href="...",  # optional — The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.
    results=,  # required — The Composite calculation with the constituens which were included.
    links=[]  # optional
)
```

- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

