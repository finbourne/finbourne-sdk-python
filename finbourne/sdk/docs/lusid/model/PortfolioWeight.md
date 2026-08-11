# PortfolioWeight

Represents a portfolio and its target allocation weight.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **portfolio_id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **weight** | **float** | Required | The relative weight of the Portfolio compared to the other Portfolios specified, used to determine the allocation split between Portfolios when there are no Orders within the Block to allocate to. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.PortfolioWeight import PortfolioWeight

instance = PortfolioWeight(
    portfolio_id=ResourceId(...),  # required
    weight=0.0  # required — The relative weight of the Portfolio compared to the other Portfolios specified, used to determine the allocation split between Portfolios when there are no Orders within the Block to allocate to.
)
```


## Related Models

- [ResourceId](ResourceId.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

