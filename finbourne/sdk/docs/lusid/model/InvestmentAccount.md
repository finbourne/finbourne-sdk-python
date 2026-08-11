# InvestmentAccount

Representation of an Investment Account on the LUSID API
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **scope** | **str** | Optional | The scope in which the Investment Account lies. |
| **identifiers** | [Dict[str, ModelProperty]](ModelProperty.md) | Optional | Unique client-defined identifiers of the Investment Account. |
| **display_name** | **str** | Optional | The display name of the Investment Account |
| **description** | **str** | Optional | The description of the Investment Account |
| **account_type** | **str** | Optional | The type of the of the Investment Account. |
| **account_holders** | [List[AccountHolder]](AccountHolder.md) | Optional | The Account Holders of the Investment Account. |
| **investment_portfolios** | [List[InvestmentPortfolio]](InvestmentPortfolio.md) | Optional | The Investment Portfolios of the Investment Account. |
| **lusid_investment_account_id** | **str** | Optional | The unique LUSID Investment Account Identifier of the Investment Account. |
| **properties** | [Dict[str, ModelProperty]](ModelProperty.md) | Optional | A set of properties associated to the Investment Account. |
| **relationships** | [List[Relationship]](Relationship.md) | Optional | A set of relationships associated to the Investment Account. |
| **href** | **str** | Optional | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. |
| **version** | [Version](Version.md) | Optional | *No description available.* |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.InvestmentAccount import InvestmentAccount

instance = InvestmentAccount(
    scope="...",  # optional — The scope in which the Investment Account lies.
    identifiers=ModelProperty(...),  # optional — Unique client-defined identifiers of the Investment Account.
    display_name="...",  # optional — The display name of the Investment Account
    description="...",  # optional — The description of the Investment Account
    account_type="...",  # optional — The type of the of the Investment Account.
    account_holders=[],  # optional — The Account Holders of the Investment Account.
    investment_portfolios=[],  # optional — The Investment Portfolios of the Investment Account.
    lusid_investment_account_id="...",  # optional — The unique LUSID Investment Account Identifier of the Investment Account.
    properties=ModelProperty(...),  # optional — A set of properties associated to the Investment Account.
    relationships=[],  # optional — A set of relationships associated to the Investment Account.
    href="...",  # optional — The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.
    version=Version(...),  # optional
    links=[]  # optional
)
```

- [ModelProperty](ModelProperty.md) — used in `identifiers`
- [AccountHolder](AccountHolder.md) — used in `account_holders`
- [InvestmentPortfolio](InvestmentPortfolio.md) — used in `investment_portfolios`
- [ModelProperty](ModelProperty.md) — used in `properties`
- [Relationship](Relationship.md) — used in `relationships`
- [Version](Version.md)
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

