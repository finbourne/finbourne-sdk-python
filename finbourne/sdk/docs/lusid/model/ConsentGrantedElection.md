# ConsentGrantedElection

Election to grant consent to the proposed action (CONY), optionally in return for a consent fee.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **election_key** | **str** | Required | Unique key associated to this election. |
| **is_default** | **bool** | Optional | Is this election automatically applied in the absence of an election having been made.  May only be true for one election if multiple are provided. |
| **is_chosen** | **bool** | Optional | Is this the election that has been explicitly chosen from multiple options. |
| **consent_fee_price** | **float** | Optional | The consent fee, quoted per 1,000 of face for bonds (the current notional at the record date for amortising and inflation-linked bonds) and per unit otherwise. |
| **consent_fee_currency** | **str** | Optional | Optional. Currency of the consent fee. Required if a consent fee price is provided. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.ConsentGrantedElection import ConsentGrantedElection

instance = ConsentGrantedElection(
    election_key="...",  # required — Unique key associated to this election.
    is_default=True,  # optional — Is this election automatically applied in the absence of an election having been made.  May only be true for one election if multiple are provided.
    is_chosen=True,  # optional — Is this the election that has been explicitly chosen from multiple options.
    consent_fee_price=0.0,  # optional — The consent fee, quoted per 1,000 of face for bonds (the current notional at the record date for amortising and inflation-linked bonds) and per unit otherwise.
    consent_fee_currency="..."  # optional — Optional. Currency of the consent fee. Required if a consent fee price is provided.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

