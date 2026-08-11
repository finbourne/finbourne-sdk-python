# Abor

An Abor entity.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **href** | **str** | Optional | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. |
| **id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **display_name** | **str** | Optional | The name of the Abor. |
| **description** | **str** | Optional | The description for the Abor. |
| **portfolio_ids** | [List[PortfolioEntityId]](PortfolioEntityId.md) | Required | The list with the portfolio ids which are part of the Abor. Note: These must all have the same base currency. |
| **abor_configuration_id** | [ResourceId](ResourceId.md) | Optional | *No description available.* |
| **properties** | [Dict[str, ModelProperty]](ModelProperty.md) | Optional | A set of properties for the Abor. |
| **version** | [Version](Version.md) | Optional | *No description available.* |
| **base_currency** | **str** | Optional | The base currency of the abor based on contained portfolio base currencies. |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.Abor import Abor

instance = Abor(
    href="...",  # optional — The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.
    id=ResourceId(...),  # required
    display_name="...",  # optional — The name of the Abor.
    description="...",  # optional — The description for the Abor.
    portfolio_ids=[],  # required — The list with the portfolio ids which are part of the Abor. Note: These must all have the same base currency.
    abor_configuration_id=ResourceId(...),  # optional
    properties=ModelProperty(...),  # optional — A set of properties for the Abor.
    version=Version(...),  # optional
    base_currency="...",  # optional — The base currency of the abor based on contained portfolio base currencies.
    links=[]  # optional
)
```

- [ResourceId](ResourceId.md)
- [PortfolioEntityId](PortfolioEntityId.md) — used in `portfolio_ids`
- [ResourceId](ResourceId.md)
- [ModelProperty](ModelProperty.md) — used in `properties`
- [Version](Version.md)
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

