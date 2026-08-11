# CashAndSecurityOfferElection

Election for events that result in both cash and equity via a merger or acquisition
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **cash_offer_currency** | **str** | Required | Currency of the cash offer |
| **cash_offer_price** | **float** | Required | Price per share of the cash offer |
| **cost_factor** | **float** | Optional | Optional. The fraction of cost that is transferred from the existing shares to the new shares. |
| **election_key** | **str** | Required | Unique key associated to this election. |
| **is_chosen** | **bool** | Optional | Is this the election that has been explicitly chosen from multiple options. |
| **is_default** | **bool** | Optional | Is this election automatically applied in the absence of an election having been made.  May only be true for one election if multiple are provided. |
| **units_ratio** | [UnitsRatio](UnitsRatio.md) | Required | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.CashAndSecurityOfferElection import CashAndSecurityOfferElection

instance = CashAndSecurityOfferElection(
    cash_offer_currency="...",  # required — Currency of the cash offer
    cash_offer_price=0.0,  # required — Price per share of the cash offer
    cost_factor=0.0,  # optional — Optional. The fraction of cost that is transferred from the existing shares to the new shares.
    election_key="...",  # required — Unique key associated to this election.
    is_chosen=True,  # optional — Is this the election that has been explicitly chosen from multiple options.
    is_default=True,  # optional — Is this election automatically applied in the absence of an election having been made.  May only be true for one election if multiple are provided.
    units_ratio=UnitsRatio(...)  # required
)
```

- [UnitsRatio](UnitsRatio.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

