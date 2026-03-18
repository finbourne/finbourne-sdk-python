# PortfolioGroupSearchResult

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **href** | **str** | Optional | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. |
| **id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **display_name** | **str** | Required | The name of the portfolio group. |
| **description** | **str** | Optional | The long form description of the portfolio group. |
| **created** | **datetime** | Optional | The effective datetime at which the portfolio group was created. No portfolios or sub groups can be added to the group before this date. |
| **portfolios** | [List[ResourceId]](ResourceId.md) | Optional | The collection of resource identifiers for the portfolios contained in the portfolio group. |
| **sub_groups** | [List[ResourceId]](ResourceId.md) | Optional | The collection of resource identifiers for the portfolio groups contained in the portfolio group as sub groups. |
| **version** | [Version](Version.md) | Optional | *No description available.* |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.PortfolioGroupSearchResult import PortfolioGroupSearchResult

instance = PortfolioGroupSearchResult(
    href="...",  # optional — The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.
    id=ResourceId(...),  # required
    display_name="...",  # required — The name of the portfolio group.
    description="...",  # optional — The long form description of the portfolio group.
    created=datetime.now(),  # optional — The effective datetime at which the portfolio group was created. No portfolios or sub groups can be added to the group before this date.
    portfolios=[],  # optional — The collection of resource identifiers for the portfolios contained in the portfolio group.
    sub_groups=[],  # optional — The collection of resource identifiers for the portfolio groups contained in the portfolio group as sub groups.
    version=Version(...),  # optional
    links=[]  # optional
)
```

- [ResourceId](ResourceId.md)
- [ResourceId](ResourceId.md) — used in `portfolios`
- [ResourceId](ResourceId.md) — used in `sub_groups`
- [Version](Version.md)
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

