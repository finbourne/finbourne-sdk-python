# UnitisationData

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **shares_in_issue** | **float** | Required | The number of shares in issue at a valuation point. |
| **unit_price** | **float** | Required | The price of one unit of the share class at a valuation point. |
| **net_dealing_units** | **float** | Required | The net dealing in units for the share class at a valuation point. This could be the sum of negative redemptions (in units) and positive subscriptions (in units). |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.UnitisationData import UnitisationData

instance = UnitisationData(
    shares_in_issue=0.0,  # required — The number of shares in issue at a valuation point.
    unit_price=0.0,  # required — The price of one unit of the share class at a valuation point.
    net_dealing_units=0.0  # required — The net dealing in units for the share class at a valuation point. This could be the sum of negative redemptions (in units) and positive subscriptions (in units).
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

