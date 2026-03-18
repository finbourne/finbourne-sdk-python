# PortfolioSearchResult

A list of portfolios.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **type** | **str** | Required | The type of the portfolio. The available values are: Transaction, Reference, DerivedTransaction, SimplePosition |
| **href** | **str** | Optional | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. |
| **description** | **str** | Optional | The long form description of the portfolio. |
| **display_name** | **str** | Required | The name of the portfolio. |
| **is_derived** | **bool** | Optional | Whether or not this is a derived portfolio. *(read-only)* |
| **created** | **datetime** | Required | The effective datetime at which the portfolio was created. No transactions or constituents can be added to the portfolio before this date. |
| **parent_portfolio_id** | [ResourceId](ResourceId.md) | Optional | *No description available.* |
| **base_currency** | **str** | Optional | The base currency of the portfolio. |
| **properties** | [List[ModelProperty]](ModelProperty.md) | Optional | The requested portfolio properties. These will be from the &#39;Portfolio&#39; domain. |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.PortfolioSearchResult import PortfolioSearchResult

instance = PortfolioSearchResult(
    id=ResourceId(...),  # required
    type="...",  # required — The type of the portfolio. The available values are: Transaction, Reference, DerivedTransaction, SimplePosition
    href="...",  # optional — The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.
    description="...",  # optional — The long form description of the portfolio.
    display_name="...",  # required — The name of the portfolio.
    is_derived=True,  # optional — Whether or not this is a derived portfolio.
    created=datetime.now(),  # required — The effective datetime at which the portfolio was created. No transactions or constituents can be added to the portfolio before this date.
    parent_portfolio_id=ResourceId(...),  # optional
    base_currency="...",  # optional — The base currency of the portfolio.
    properties=[],  # optional — The requested portfolio properties. These will be from the &#39;Portfolio&#39; domain.
    links=[]  # optional
)
```


## Related Models

- [ResourceId](ResourceId.md)
- [ResourceId](ResourceId.md)
- [ModelProperty](ModelProperty.md) — used in `properties`
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

