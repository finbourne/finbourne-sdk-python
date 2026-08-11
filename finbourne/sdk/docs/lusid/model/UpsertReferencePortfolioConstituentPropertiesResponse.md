# UpsertReferencePortfolioConstituentPropertiesResponse

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **href** | **str** | Optional | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. |
| **version** | [Version](Version.md) | Optional | *No description available.* |
| **properties** | [Dict[str, PerpetualProperty]](PerpetualProperty.md) | Optional | The updated collection of properties of the constituent. |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.UpsertReferencePortfolioConstituentPropertiesResponse import UpsertReferencePortfolioConstituentPropertiesResponse

instance = UpsertReferencePortfolioConstituentPropertiesResponse(
    href="...",  # optional — The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.
    version=Version(...),  # optional
    properties=PerpetualProperty(...),  # optional — The updated collection of properties of the constituent.
    links=[]  # optional
)
```

- [Version](Version.md)
- [PerpetualProperty](PerpetualProperty.md) — used in `properties`
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

