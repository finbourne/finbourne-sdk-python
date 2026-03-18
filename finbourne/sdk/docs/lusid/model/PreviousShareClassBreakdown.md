# PreviousShareClassBreakdown

The data for a Share Class at the previous valuation point.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **nav** | [PreviousNAV](PreviousNAV.md) | Required | *No description available.* |
| **unitisation** | [UnitisationData](UnitisationData.md) | Optional | *No description available.* |
| **share_class_to_fund_fx_rate** | **float** | Required | The fx rate from the Share Class currency to the fund currency at this valuation point. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.PreviousShareClassBreakdown import PreviousShareClassBreakdown

instance = PreviousShareClassBreakdown(
    nav=PreviousNAV(...),  # required
    unitisation=UnitisationData(...),  # optional
    share_class_to_fund_fx_rate=0.0  # required — The fx rate from the Share Class currency to the fund currency at this valuation point.
)
```


## Related Models

- [PreviousNAV](PreviousNAV.md)
- [UnitisationData](UnitisationData.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

