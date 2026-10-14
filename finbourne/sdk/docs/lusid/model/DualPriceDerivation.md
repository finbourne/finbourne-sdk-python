# DualPriceDerivation

How a Dual fund derives its dealing prices from one real price by fixed spreads.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **real_side** | **str** | Required | The price read from the valuation: Bid or Offer, from which the other side is derived, or Mid, the share class unit price, from which both sides are derived, for a fund whose market data has no bid or offer. Available values: Bid, Offer, Mid. |
| **include_ndc** | **bool** | Required | Whether the real side is read including notional dealing costs, which needs the NAV type to have a notional dealing cost table. Must be false for Mid. |
| **bid_spread_bps** | **float** | Optional | How far below the real price the bid is set, in basis points of the real price. Zero or more. Required when the bid is derived, for an Offer or Mid real side, and absent for a Bid one. |
| **offer_spread_bps** | **float** | Optional | How far above the real price the offer is set, in basis points of the real price. Zero or more. Required when the offer is derived, for a Bid or Mid real side, and absent for an Offer one. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.DualPriceDerivation import DualPriceDerivation

instance = DualPriceDerivation(
    real_side="...",  # required — The price read from the valuation: Bid or Offer, from which the other side is derived, or Mid, the share class unit price, from which both sides are derived, for a fund whose market data has no bid or offer. Available values: Bid, Offer, Mid.
    include_ndc=True,  # required — Whether the real side is read including notional dealing costs, which needs the NAV type to have a notional dealing cost table. Must be false for Mid.
    bid_spread_bps=0.0,  # optional — How far below the real price the bid is set, in basis points of the real price. Zero or more. Required when the bid is derived, for an Offer or Mid real side, and absent for a Bid one.
    offer_spread_bps=0.0  # optional — How far above the real price the offer is set, in basis points of the real price. Zero or more. Required when the offer is derived, for a Bid or Mid real side, and absent for an Offer one.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

