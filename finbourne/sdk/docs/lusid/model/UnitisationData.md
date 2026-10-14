# UnitisationData

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **shares_in_issue** | **float** | Required | The number of shares in issue at a valuation point. |
| **unit_price** | **float** | Required | The price of one unit of the share class at a valuation point. |
| **net_dealing_units** | **float** | Required | The net dealing in units for the share class at a valuation point. This could be the sum of negative redemptions (in units) and positive subscriptions (in units). |
| **bid_price** | **float** | Optional | The price of one unit of the share class on the bid side at a valuation point: the class&#39;s NAV with the fund&#39;s holdings marked at their bid prices. Equal to the unit price when the fund is struck on the bid. Absent when a holding&#39;s bid could not be priced. |
| **offer_price** | **float** | Optional | The price of one unit of the share class on the offer side at a valuation point: the class&#39;s NAV with the fund&#39;s holdings marked at their ask prices. Equal to the unit price when the fund is struck on the ask. Absent when a holding&#39;s ask could not be priced. |
| **bid_price_inc_ndc** | **float** | Optional | The bid price of one unit of the share class less the class&#39;s share of the notional dealing costs of selling the fund&#39;s holdings, at a valuation point. Absent when the NAV type has no notional dealing cost table. |
| **offer_price_inc_ndc** | **float** | Optional | The offer price of one unit of the share class plus the class&#39;s share of the notional dealing costs of buying the fund&#39;s holdings, at a valuation point. Absent when the NAV type has no notional dealing cost table. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.UnitisationData import UnitisationData

instance = UnitisationData(
    shares_in_issue=0.0,  # required — The number of shares in issue at a valuation point.
    unit_price=0.0,  # required — The price of one unit of the share class at a valuation point.
    net_dealing_units=0.0,  # required — The net dealing in units for the share class at a valuation point. This could be the sum of negative redemptions (in units) and positive subscriptions (in units).
    bid_price=0.0,  # optional — The price of one unit of the share class on the bid side at a valuation point: the class&#39;s NAV with the fund&#39;s holdings marked at their bid prices. Equal to the unit price when the fund is struck on the bid. Absent when a holding&#39;s bid could not be priced.
    offer_price=0.0,  # optional — The price of one unit of the share class on the offer side at a valuation point: the class&#39;s NAV with the fund&#39;s holdings marked at their ask prices. Equal to the unit price when the fund is struck on the ask. Absent when a holding&#39;s ask could not be priced.
    bid_price_inc_ndc=0.0,  # optional — The bid price of one unit of the share class less the class&#39;s share of the notional dealing costs of selling the fund&#39;s holdings, at a valuation point. Absent when the NAV type has no notional dealing cost table.
    offer_price_inc_ndc=0.0  # optional — The offer price of one unit of the share class plus the class&#39;s share of the notional dealing costs of buying the fund&#39;s holdings, at a valuation point. Absent when the NAV type has no notional dealing cost table.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

