# PricingMethodology

How a fund prices its share classes for dealing. A Single fund deals at one price per class, which starts at a  baseline and may swing with the fund's net cashflow. A Dual fund deals at a bid and an offer per class.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **output_shape** | **str** | Required | How many dealing prices each share class publishes: Single, one price that subscriptions and redemptions both deal at, or Dual, a bid that redemptions deal at and an offer that subscriptions deal at. Available values: Single, Dual. |
| **swing_policy** | [SwingPolicy](SwingPolicy.md) | Optional | *No description available.* |
| **price_labels** | **str** | Optional | What a Dual fund&#39;s two prices are. BidOffer is the only label available: the bid and the offer, including notional dealing costs, that the valuation recipe of each active NAV type publishes. Required for a Dual fund and must be omitted for a Single fund. Available values: BidOffer, CreationCancellation. |
| **derivation** | [DualPriceDerivation](DualPriceDerivation.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.PricingMethodology import PricingMethodology

instance = PricingMethodology(
    output_shape="...",  # required — How many dealing prices each share class publishes: Single, one price that subscriptions and redemptions both deal at, or Dual, a bid that redemptions deal at and an offer that subscriptions deal at. Available values: Single, Dual.
    swing_policy=SwingPolicy(...),  # optional
    price_labels="...",  # optional — What a Dual fund&#39;s two prices are. BidOffer is the only label available: the bid and the offer, including notional dealing costs, that the valuation recipe of each active NAV type publishes. Required for a Dual fund and must be omitted for a Single fund. Available values: BidOffer, CreationCancellation.
    derivation=DualPriceDerivation(...)  # optional
)
```

- [SwingPolicy](SwingPolicy.md)
- [DualPriceDerivation](DualPriceDerivation.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

