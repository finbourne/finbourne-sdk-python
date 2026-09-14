# ConsentAndExchangeElection

Election to both grant consent and exchange the holding (CEXC), at a given units ratio.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **election_key** | **str** | Required | Unique key associated to this election. |
| **is_default** | **bool** | Optional | Is this election automatically applied in the absence of an election having been made.  May only be true for one election if multiple are provided. |
| **is_chosen** | **bool** | Optional | Is this the election that has been explicitly chosen from multiple options. |
| **units_ratio** | [UnitsRatio](UnitsRatio.md) | Required | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.ConsentAndExchangeElection import ConsentAndExchangeElection

instance = ConsentAndExchangeElection(
    election_key="...",  # required — Unique key associated to this election.
    is_default=True,  # optional — Is this election automatically applied in the absence of an election having been made.  May only be true for one election if multiple are provided.
    is_chosen=True,  # optional — Is this the election that has been explicitly chosen from multiple options.
    units_ratio=UnitsRatio(...)  # required
)
```

- [UnitsRatio](UnitsRatio.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

