# AdjustHolding

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **href** | **str** | Optional | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. |
| **version** | [Version](Version.md) | Required | *No description available.* |
| **metadata** | **Dict[str, Optional[List[ResponseMetaData]]]** | Optional | Contains warnings related to unresolved instruments |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.AdjustHolding import AdjustHolding

instance = AdjustHolding(
    href="...",  # optional — The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.
    version=Version(...),  # required
    metadata=,  # optional — Contains warnings related to unresolved instruments
    links=[]  # optional
)
```

- [Version](Version.md)
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

