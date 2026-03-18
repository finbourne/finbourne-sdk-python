# CompletePortfolio

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **href** | **str** | Optional | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. |
| **description** | **str** | Optional | The long form description of the portfolio. |
| **display_name** | **str** | Optional | The name of the portfolio. |
| **created** | **datetime** | Optional | The effective datetime at which the portfolio was created. No transactions or constituents can be added to the portfolio before this date. |
| **parent_portfolio_id** | [ResourceId](ResourceId.md) | Optional | *No description available.* |
| **is_derived** | **bool** | Optional | Whether or not this is a derived portfolio. *(read-only)* |
| **type** | **str** | Optional | The type of the portfolio. The available values are: Transaction, Reference, DerivedTransaction, SimplePosition |
| **version** | [Version](Version.md) | Required | *No description available.* |
| **properties** | [List[ModelProperty]](ModelProperty.md) | Optional | The requested portfolio properties. These will be from the &#39;Portfolio&#39; domain. |
| **base_currency** | **str** | Optional | If the portfolio is a transaction portfolio or derived transaction portfolio, this is the base currency of the portfolio. |
| **sub_holding_keys** | **List[str]** | Optional | The sub holding key properties configured for the portfolio |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.CompletePortfolio import CompletePortfolio

instance = CompletePortfolio(
    id=ResourceId(...),  # required
    href="...",  # optional — The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.
    description="...",  # optional — The long form description of the portfolio.
    display_name="...",  # optional — The name of the portfolio.
    created=datetime.now(),  # optional — The effective datetime at which the portfolio was created. No transactions or constituents can be added to the portfolio before this date.
    parent_portfolio_id=ResourceId(...),  # optional
    is_derived=True,  # optional — Whether or not this is a derived portfolio.
    type="...",  # optional — The type of the portfolio. The available values are: Transaction, Reference, DerivedTransaction, SimplePosition
    version=Version(...),  # required
    properties=[],  # optional — The requested portfolio properties. These will be from the &#39;Portfolio&#39; domain.
    base_currency="...",  # optional — If the portfolio is a transaction portfolio or derived transaction portfolio, this is the base currency of the portfolio.
    sub_holding_keys=,  # optional — The sub holding key properties configured for the portfolio
    links=[]  # optional
)
```


## Related Models

- [ResourceId](ResourceId.md)
- [ResourceId](ResourceId.md)
- [Version](Version.md)
- [ModelProperty](ModelProperty.md) — used in `properties`
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

