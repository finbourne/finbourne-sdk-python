# AbstainElection

Election to abstain from voting on the proposed action (ABST).
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **election_key** | **str** | Required | Unique key associated to this election. |
| **is_default** | **bool** | Optional | Is this election automatically applied in the absence of an election having been made.  May only be true for one election if multiple are provided. |
| **is_chosen** | **bool** | Optional | Is this the election that has been explicitly chosen from multiple options. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.AbstainElection import AbstainElection

instance = AbstainElection(
    election_key="...",  # required — Unique key associated to this election.
    is_default=True,  # optional — Is this election automatically applied in the absence of an election having been made.  May only be true for one election if multiple are provided.
    is_chosen=True  # optional — Is this the election that has been explicitly chosen from multiple options.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

