# PortfolioReconciliationRequest

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **portfolio_id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **effective_at** | **str** | Required | The effective date of the portfolio |
| **as_at** | **datetime** | Optional | Optional. The AsAt date of the portfolio |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.PortfolioReconciliationRequest import PortfolioReconciliationRequest

instance = PortfolioReconciliationRequest(
    portfolio_id=ResourceId(...),  # required
    effective_at="...",  # required — The effective date of the portfolio
    as_at=datetime.now()  # optional — Optional. The AsAt date of the portfolio
)
```


## Related Models

- [ResourceId](ResourceId.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

