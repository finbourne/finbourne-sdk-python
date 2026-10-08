# FundStructureDriftMateriality

How much ownership drift a Fund Structure member tolerates on the members it holds through an instrument.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **warn_amount** | **float** | Optional | The misallocated P&amp;L, in base currency, above which the valuation point carries a warning naming the holder, the held member and both shares. Optional; unset means never warn. |
| **refuse_amount** | **float** | Optional | The misallocated P&amp;L, in base currency, above which the P&amp;L flow is refused until the sharing percentage is corrected. Must not be less than the warning amount. Optional; unset means never refuse. A share bought from another investor at a premium or a discount shows as drift however correct the sharing percentage. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.FundStructureDriftMateriality import FundStructureDriftMateriality

instance = FundStructureDriftMateriality(
    warn_amount=0.0,  # optional — The misallocated P&amp;L, in base currency, above which the valuation point carries a warning naming the holder, the held member and both shares. Optional; unset means never warn.
    refuse_amount=0.0  # optional — The misallocated P&amp;L, in base currency, above which the P&amp;L flow is refused until the sharing percentage is corrected. Must not be less than the warning amount. Optional; unset means never refuse. A share bought from another investor at a premium or a discount shows as drift however correct the sharing percentage.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

