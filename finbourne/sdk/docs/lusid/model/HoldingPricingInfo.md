# HoldingPricingInfo

Enables price quotes to be created from Holding fields as either overrides or fallbacks to the Market Data  resolution process. For example, we may wish to price an instrument at Cost if Market Data resolution fails.  We may also wish to always price Bonds using the LastTradedPrice on the corresponding Holding.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **fallback_field** | **str** | Optional | The default Holding field to fall back on if the Market Data resolution process fails to find a price quote. |
| **override_field** | **str** | Optional | The default Holding field to be used as an override for instrument price quotes. This cannot be specified  along with a FallbackField or any SpecificFallbacks, since we&#39;ll never attempt Market Data resolution  for price quotes if this field is populated. |
| **specific_fallbacks** | [List[SpecificHoldingPricingInfo]](SpecificHoldingPricingInfo.md) | Optional | Allows a user to specify fallbacks using Holding fields for sources that match a particular DependencySourceFilter. |
| **specific_overrides** | [List[SpecificHoldingPricingInfo]](SpecificHoldingPricingInfo.md) | Optional | Allows a user to specify overrides using Holding fields for sources that match a particular DependencySourceFilter. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.HoldingPricingInfo import HoldingPricingInfo

instance = HoldingPricingInfo(
    fallback_field="...",  # optional — The default Holding field to fall back on if the Market Data resolution process fails to find a price quote.
    override_field="...",  # optional — The default Holding field to be used as an override for instrument price quotes. This cannot be specified  along with a FallbackField or any SpecificFallbacks, since we&#39;ll never attempt Market Data resolution  for price quotes if this field is populated.
    specific_fallbacks=[],  # optional — Allows a user to specify fallbacks using Holding fields for sources that match a particular DependencySourceFilter.
    specific_overrides=[]  # optional — Allows a user to specify overrides using Holding fields for sources that match a particular DependencySourceFilter.
)
```

- [SpecificHoldingPricingInfo](SpecificHoldingPricingInfo.md) — used in `specific_fallbacks`
- [SpecificHoldingPricingInfo](SpecificHoldingPricingInfo.md) — used in `specific_overrides`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

