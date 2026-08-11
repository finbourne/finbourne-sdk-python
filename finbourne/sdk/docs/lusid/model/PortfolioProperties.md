# PortfolioProperties

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **href** | **str** | Optional | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. |
| **properties** | [Dict[str, ModelProperty]](ModelProperty.md) | Optional | The portfolio properties. These will be from the &#39;Portfolio&#39; domain. |
| **version** | [Version](Version.md) | Optional | *No description available.* |
| **staged_modifications** | [StagedModificationsInfo](StagedModificationsInfo.md) | Optional | *No description available.* |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.PortfolioProperties import PortfolioProperties

instance = PortfolioProperties(
    href="...",  # optional — The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.
    properties=ModelProperty(...),  # optional — The portfolio properties. These will be from the &#39;Portfolio&#39; domain.
    version=Version(...),  # optional
    staged_modifications=StagedModificationsInfo(...),  # optional
    links=[]  # optional
)
```

- [ModelProperty](ModelProperty.md) — used in `properties`
- [Version](Version.md)
- [StagedModificationsInfo](StagedModificationsInfo.md)
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

