# DualPriceDealing

The bid and offer dealing prices a share class of a Dual fund publishes at a valuation point.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **dealing_bid** | **float** | Optional | The price redemptions deal at, rounded as the share class unit price is. Absent when the class has no units in issue or the valuation did not price the side. |
| **dealing_offer** | **float** | Optional | The price subscriptions deal at, rounded as the share class unit price is. Absent when the class has no units in issue or the valuation did not price the side. |
| **bid_per_valuation_source** | **str** | Optional | The share class price the dealing bid was read or derived from: Bid when it is the bid read as published, Offer or Mid when it was derived from that price. Absent when nothing was dealt. |
| **offer_per_valuation_source** | **str** | Optional | The share class price the dealing offer was read or derived from: Offer when it is the offer read as published, Bid or Mid when it was derived from that price. Absent when nothing was dealt. |
| **bid_spread_bps** | **float** | Optional | The spread, in basis points, the dealing bid was set below the price it was derived from by. Absent when the bid was read. |
| **offer_spread_bps** | **float** | Optional | The spread, in basis points, the dealing offer was set above the price it was derived from by. Absent when the offer was read. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.DualPriceDealing import DualPriceDealing

instance = DualPriceDealing(
    dealing_bid=0.0,  # optional — The price redemptions deal at, rounded as the share class unit price is. Absent when the class has no units in issue or the valuation did not price the side.
    dealing_offer=0.0,  # optional — The price subscriptions deal at, rounded as the share class unit price is. Absent when the class has no units in issue or the valuation did not price the side.
    bid_per_valuation_source="...",  # optional — The share class price the dealing bid was read or derived from: Bid when it is the bid read as published, Offer or Mid when it was derived from that price. Absent when nothing was dealt.
    offer_per_valuation_source="...",  # optional — The share class price the dealing offer was read or derived from: Offer when it is the offer read as published, Bid or Mid when it was derived from that price. Absent when nothing was dealt.
    bid_spread_bps=0.0,  # optional — The spread, in basis points, the dealing bid was set below the price it was derived from by. Absent when the bid was read.
    offer_spread_bps=0.0  # optional — The spread, in basis points, the dealing offer was set above the price it was derived from by. Absent when the offer was read.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

