# PricingMethodologyEngineProposal

What the pricing methodology alone publishes for a share class, kept alongside any decision that replaces it.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **swung** | **bool** | Required | Whether the methodology swings the price. |
| **swing_direction** | **str** | Optional | Offer or Bid when the methodology swings the price. Absent when it does not. |
| **spread_source** | **str** | Optional | Where the methodology&#39;s spread came from: Stored or Market. Absent when it does not swing. |
| **spread_bps** | **float** | Optional | The stored spread the methodology applies, in basis points. Absent when it does not swing or swings to a market price. |
| **dealing_price** | **float** | Optional | The dealing price the methodology publishes. Absent when the class has no units in issue. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.PricingMethodologyEngineProposal import PricingMethodologyEngineProposal

instance = PricingMethodologyEngineProposal(
    swung=True,  # required — Whether the methodology swings the price.
    swing_direction="...",  # optional — Offer or Bid when the methodology swings the price. Absent when it does not.
    spread_source="...",  # optional — Where the methodology&#39;s spread came from: Stored or Market. Absent when it does not swing.
    spread_bps=0.0,  # optional — The stored spread the methodology applies, in basis points. Absent when it does not swing or swings to a market price.
    dealing_price=0.0  # optional — The dealing price the methodology publishes. Absent when the class has no units in issue.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

