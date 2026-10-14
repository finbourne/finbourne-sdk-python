# PricingMethodologyOverride

The fund manager's override a share class's dealing price follows instead of the pricing methodology's proposal,  and who made it when.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **decision** | **str** | Required | The basis the dealing price is published on: Mid, Bid or Offer. Under a Stored spread source the spread for Bid or Offer is the stored tier the net cashflow matches in that direction, or that direction&#39;s first tier when the flow is below every tier. Under a Market spread source Bid or Offer reads that side&#39;s price including notional dealing costs, which every active NAV type&#39;s valuation recipe must publish. |
| **reason** | **str** | Required | Why the fund manager overrode the methodology&#39;s decision. |
| **user** | **str** | Optional | The user who made the override. |
| **timestamp** | **datetime** | Required | When the override was made. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.PricingMethodologyOverride import PricingMethodologyOverride

instance = PricingMethodologyOverride(
    decision="...",  # required — The basis the dealing price is published on: Mid, Bid or Offer. Under a Stored spread source the spread for Bid or Offer is the stored tier the net cashflow matches in that direction, or that direction&#39;s first tier when the flow is below every tier. Under a Market spread source Bid or Offer reads that side&#39;s price including notional dealing costs, which every active NAV type&#39;s valuation recipe must publish.
    reason="...",  # required — Why the fund manager overrode the methodology&#39;s decision.
    user="...",  # optional — The user who made the override.
    timestamp=datetime.now()  # required — When the override was made.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

