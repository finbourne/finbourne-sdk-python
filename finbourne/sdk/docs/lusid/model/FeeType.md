# FeeType

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **href** | **str** | Optional | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. |
| **id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **display_name** | **str** | Required | The name of the fee type. |
| **description** | **str** | Required | The description of the fee type. |
| **component_transactions** | [List[ComponentTransaction]](ComponentTransaction.md) | Required | A set of component transactions that relate to the fee type to be created. |
| **version** | [Version](Version.md) | Optional | *No description available.* |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.FeeType import FeeType

instance = FeeType(
    href="...",  # optional — The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.
    id=ResourceId(...),  # required
    display_name="...",  # required — The name of the fee type.
    description="...",  # required — The description of the fee type.
    component_transactions=[],  # required — A set of component transactions that relate to the fee type to be created.
    version=Version(...),  # optional
    links=[]  # optional
)
```

- [ResourceId](ResourceId.md)
- [ComponentTransaction](ComponentTransaction.md) — used in `component_transactions`
- [Version](Version.md)
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

