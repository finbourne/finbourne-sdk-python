# MixedLotConstituentsElection

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **election_key** | **str** | Required | *No description available.* |
| **is_default** | **bool** | Optional | *No description available.* |
| **is_chosen** | **bool** | Optional | *No description available.* |
| **securities_constituents** | [List[SecurityOfferConstituent]](SecurityOfferConstituent.md) | Optional | *No description available.* |
| **cash_constituents** | [List[CashOfferConstituent]](CashOfferConstituent.md) | Optional | *No description available.* |
| **cost_factor** | **float** | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.MixedLotConstituentsElection import MixedLotConstituentsElection

instance = MixedLotConstituentsElection(
    election_key="...",  # required
    is_default=True,  # optional
    is_chosen=True,  # optional
    securities_constituents=[],  # optional
    cash_constituents=[],  # optional
    cost_factor=0.0  # optional
)
```

- [SecurityOfferConstituent](SecurityOfferConstituent.md)
- [CashOfferConstituent](CashOfferConstituent.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

