# UpsertInvestmentAccountRequest

Request to create or update an investor record
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **scope** | **str** | Required | The scope in which the Investment Account lies. |
| **identifiers** | [Dict[str, ModelProperty]](ModelProperty.md) | Required | Unique client-defined identifiers of the Investment Account. |
| **display_name** | **str** | Required | The display name of the Investment Account |
| **description** | **str** | Optional | The description of the Investment Account |
| **account_type** | **str** | Required | The type of the of the Investment Account. |
| **account_holders** | [List[AccountHolderIdentifier]](AccountHolderIdentifier.md) | Optional | The identification of the account holders associated with this investment account |
| **investment_portfolios** | [List[InvestmentPortfolioIdentifier]](InvestmentPortfolioIdentifier.md) | Optional | The identification of the investment portfolios associated with this investment account |
| **properties** | [Dict[str, ModelProperty]](ModelProperty.md) | Optional | A set of properties associated to the Investment Account. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.UpsertInvestmentAccountRequest import UpsertInvestmentAccountRequest

instance = UpsertInvestmentAccountRequest(
    scope="...",  # required — The scope in which the Investment Account lies.
    identifiers=ModelProperty(...),  # required — Unique client-defined identifiers of the Investment Account.
    display_name="...",  # required — The display name of the Investment Account
    description="...",  # optional — The description of the Investment Account
    account_type="...",  # required — The type of the of the Investment Account.
    account_holders=[],  # optional — The identification of the account holders associated with this investment account
    investment_portfolios=[],  # optional — The identification of the investment portfolios associated with this investment account
    properties=ModelProperty(...)  # optional — A set of properties associated to the Investment Account.
)
```

- [ModelProperty](ModelProperty.md) — used in `identifiers`
- [AccountHolderIdentifier](AccountHolderIdentifier.md) — used in `account_holders`
- [InvestmentPortfolioIdentifier](InvestmentPortfolioIdentifier.md) — used in `investment_portfolios`
- [ModelProperty](ModelProperty.md) — used in `properties`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

