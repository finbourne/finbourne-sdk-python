# SinglePriceDealing

The single dealing price a share class publishes at a valuation point.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **dealing_price** | **float** | Optional | The price subscriptions and redemptions deal at, rounded as the share class unit price is. Absent when the class has no units in issue. |
| **swung** | **bool** | Required | Whether the dealing price moved away from its baseline. |
| **swing_direction** | **str** | Optional | Offer when a net inflow swung the price up, Bid when a net outflow swung it down. Absent when the price did not swing. |
| **swing_from** | **str** | Optional | The baseline the price swung away from. Absent when it did not swing. |
| **per_valuation_source** | **str** | Optional | Bid or Offer when the dealing price is that side&#39;s share class price read as published, from a Bid or Offer baseline or a Market swing. Absent when the price is the mid or a stored spread was applied to it. |
| **spread_bps** | **float** | Optional | The stored spread applied, in basis points. Absent when the price did not swing or swung to a market price. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.SinglePriceDealing import SinglePriceDealing

instance = SinglePriceDealing(
    dealing_price=0.0,  # optional — The price subscriptions and redemptions deal at, rounded as the share class unit price is. Absent when the class has no units in issue.
    swung=True,  # required — Whether the dealing price moved away from its baseline.
    swing_direction="...",  # optional — Offer when a net inflow swung the price up, Bid when a net outflow swung it down. Absent when the price did not swing.
    swing_from="...",  # optional — The baseline the price swung away from. Absent when it did not swing.
    per_valuation_source="...",  # optional — Bid or Offer when the dealing price is that side&#39;s share class price read as published, from a Bid or Offer baseline or a Market swing. Absent when the price is the mid or a stored spread was applied to it.
    spread_bps=0.0  # optional — The stored spread applied, in basis points. Absent when the price did not swing or swung to a market price.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

