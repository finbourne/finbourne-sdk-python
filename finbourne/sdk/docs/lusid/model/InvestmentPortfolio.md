# InvestmentPortfolio

An Investment Portfolio of an Investment Account.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **key** | **str** | Optional | A client-defined key used to identify the Investment Portfolio, unique within the Investment Account |
| **scope** | **str** | Optional | The scope of the Investment Portfolio |
| **identifiers** | **Dict[str, Optional[str]]** | Optional | The code identifier of the Investment Portfolio |
| **entity_unique_id** | **str** | Optional | The unique Portfolio entity identifier |
| **portfolio** | [Portfolio](Portfolio.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.InvestmentPortfolio import InvestmentPortfolio

instance = InvestmentPortfolio(
    key="...",  # optional — A client-defined key used to identify the Investment Portfolio, unique within the Investment Account
    scope="...",  # optional — The scope of the Investment Portfolio
    identifiers=,  # optional — The code identifier of the Investment Portfolio
    entity_unique_id="...",  # optional — The unique Portfolio entity identifier
    portfolio=Portfolio(...)  # optional
)
```

- [Portfolio](Portfolio.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

