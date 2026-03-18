# PortfolioEntityId

Specification of a portfolio or portfolio group id, its scope and which it is.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **scope** | **str** | Required | The scope within which the portfolio or portfolio group lives. |
| **code** | **str** | Required | Portfolio name or code. |
| **portfolio_entity_type** | **str** | Optional | String identifier for portfolio e.g. \&quot;SinglePortfolio\&quot; and \&quot;GroupPortfolio\&quot;. If not specified, it is assumed to be a single portfolio. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.PortfolioEntityId import PortfolioEntityId

instance = PortfolioEntityId(
    scope="...",  # required — The scope within which the portfolio or portfolio group lives.
    code="...",  # required — Portfolio name or code.
    portfolio_entity_type="..."  # optional — String identifier for portfolio e.g. \&quot;SinglePortfolio\&quot; and \&quot;GroupPortfolio\&quot;. If not specified, it is assumed to be a single portfolio.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

