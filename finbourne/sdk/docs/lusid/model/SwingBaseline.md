# SwingBaseline

The price a Single fund's dealing price starts from before any swing.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **source** | **str** | Required | The price the dealing price starts from: Mid, the share class unit price, or Bid or Offer, the share class price that the valuation recipe of each active NAV type publishes on that side. Available values: Mid, Bid, Offer. |
| **include_ndc** | **bool** | Optional | Whether a Bid or Offer baseline reads the price including notional dealing costs, which needs the NAV type to have a notional dealing cost table. Required for a Bid or Offer baseline and must be omitted for a Mid baseline. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.SwingBaseline import SwingBaseline

instance = SwingBaseline(
    source="...",  # required — The price the dealing price starts from: Mid, the share class unit price, or Bid or Offer, the share class price that the valuation recipe of each active NAV type publishes on that side. Available values: Mid, Bid, Offer.
    include_ndc=True  # optional — Whether a Bid or Offer baseline reads the price including notional dealing costs, which needs the NAV type to have a notional dealing cost table. Required for a Bid or Offer baseline and must be omitted for a Mid baseline.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

