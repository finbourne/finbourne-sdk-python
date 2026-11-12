# EstimateValuationOutcome

Where a net cashflow leads the methodology: whether and which way it swings, the spread and tier it lands in, and the dealing price that results.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **swung** | **bool** | Required | Whether the methodology swings the price on this net cashflow. |
| **swing_direction** | **str** | Optional | &#39;Bid&#39; or &#39;Offer&#39;, the side the price swings to. Absent when it does not swing. |
| **spread_bps** | **float** | Optional | The stored spread applied, in basis points. Absent when the price does not swing or the spread comes from the market. |
| **tier_matched** | [SwingSpreadTierBounds](SwingSpreadTierBounds.md) | Optional | *No description available.* |
| **dealing_price** | **float** | Optional | The dealing price the methodology publishes on this net cashflow. Absent when the baseline price is unavailable. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.EstimateValuationOutcome import EstimateValuationOutcome

instance = EstimateValuationOutcome(
    swung=True,  # required — Whether the methodology swings the price on this net cashflow.
    swing_direction="...",  # optional — &#39;Bid&#39; or &#39;Offer&#39;, the side the price swings to. Absent when it does not swing.
    spread_bps=0.0,  # optional — The stored spread applied, in basis points. Absent when the price does not swing or the spread comes from the market.
    tier_matched=SwingSpreadTierBounds(...),  # optional
    dealing_price=0.0  # optional — The dealing price the methodology publishes on this net cashflow. Absent when the baseline price is unavailable.
)
```

- [SwingSpreadTierBounds](SwingSpreadTierBounds.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

