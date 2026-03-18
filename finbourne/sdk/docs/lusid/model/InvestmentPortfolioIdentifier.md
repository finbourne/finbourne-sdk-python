# InvestmentPortfolioIdentifier

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **key** | **str** | Required | A client-defined key used to identify the Investment Portfolio, unique within the Investment Account |
| **scope** | **str** | Required | The scope of the Investment Portfolio. |
| **identifiers** | **Dict[str, Optional[str]]** | Required | The code identifier of the Investment Portfolio. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.InvestmentPortfolioIdentifier import InvestmentPortfolioIdentifier

instance = InvestmentPortfolioIdentifier(
    key="...",  # required — A client-defined key used to identify the Investment Portfolio, unique within the Investment Account
    scope="...",  # required — The scope of the Investment Portfolio.
    identifiers=  # required — The code identifier of the Investment Portfolio.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

