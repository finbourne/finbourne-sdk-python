# PortfoliosReconciliationRequest

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **left** | [PortfolioReconciliationRequest](PortfolioReconciliationRequest.md) | Required | *No description available.* |
| **right** | [PortfolioReconciliationRequest](PortfolioReconciliationRequest.md) | Required | *No description available.* |
| **instrument_property_keys** | **List[str]** | Required | Instrument properties to be included with any identified breaks. These properties will be in the effective and AsAt dates of the left portfolio |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.PortfoliosReconciliationRequest import PortfoliosReconciliationRequest

instance = PortfoliosReconciliationRequest(
    left=PortfolioReconciliationRequest(...),  # required
    right=PortfolioReconciliationRequest(...),  # required
    instrument_property_keys=  # required — Instrument properties to be included with any identified breaks. These properties will be in the effective and AsAt dates of the left portfolio
)
```


## Related Models

- [PortfolioReconciliationRequest](PortfolioReconciliationRequest.md)
- [PortfolioReconciliationRequest](PortfolioReconciliationRequest.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

