# VersionedResourceListWithWarningsOfPortfolioHolding

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **version** | [Version](Version.md) | Required | *No description available.* |
| **values** | [List[PortfolioHolding]](PortfolioHolding.md) | Required | The resources to list. |
| **href** | **str** | Optional | The URI of the resource list. |
| **next_page** | **str** | Optional | The next page of results. |
| **previous_page** | **str** | Optional | The previous page of results. |
| **warnings** | [List[Warning]](Warning.md) | Optional | *No description available.* |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.VersionedResourceListWithWarningsOfPortfolioHolding import VersionedResourceListWithWarningsOfPortfolioHolding

instance = VersionedResourceListWithWarningsOfPortfolioHolding(
    version=Version(...),  # required
    values=[],  # required — The resources to list.
    href="...",  # optional — The URI of the resource list.
    next_page="...",  # optional — The next page of results.
    previous_page="...",  # optional — The previous page of results.
    warnings=[],  # optional
    links=[]  # optional
)
```


## Related Models

- [Version](Version.md)
- [PortfolioHolding](PortfolioHolding.md) — used in `values`
- [Warning](Warning.md)
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

