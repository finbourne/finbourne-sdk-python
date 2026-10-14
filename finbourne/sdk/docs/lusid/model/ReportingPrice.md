# ReportingPrice

A share class price a fund publishes at each valuation point under a label of its own, alongside the dealing price.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **source** | **str** | Required | The share class price published: Mid, the unit price, or Bid, Offer, BidIncNdc or OfferIncNdc, as the valuation recipe of each active NAV type publishes it. Available values: Mid, Bid, Offer, BidIncNdc, OfferIncNdc, Creation, Cancellation. |
| **label** | **str** | Required | The name the price is published under in the share class&#39;s reporting prices. Unique within the fund. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.ReportingPrice import ReportingPrice

instance = ReportingPrice(
    source="...",  # required — The share class price published: Mid, the unit price, or Bid, Offer, BidIncNdc or OfferIncNdc, as the valuation recipe of each active NAV type publishes it. Available values: Mid, Bid, Offer, BidIncNdc, OfferIncNdc, Creation, Cancellation.
    label="..."  # required — The name the price is published under in the share class&#39;s reporting prices. Unique within the fund.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

