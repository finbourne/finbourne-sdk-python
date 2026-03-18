# SecurityElection

Security election for Events that result in equity
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **election_key** | **str** | Required | Unique key associated to this election. |
| **is_chosen** | **bool** | Optional | Is this the election that has been explicitly chosen from multiple options. |
| **is_default** | **bool** | Optional | Is this election automatically applied in the absence of an election having been made.  May only be true for one election if multiple are provided. |
| **price** | **float** | Optional | Price per unit of the security. At least one of UnitsRatio or Price must be provided.  Price must non-zero. |
| **units_ratio** | [UnitsRatio](UnitsRatio.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.SecurityElection import SecurityElection

instance = SecurityElection(
    election_key="...",  # required — Unique key associated to this election.
    is_chosen=True,  # optional — Is this the election that has been explicitly chosen from multiple options.
    is_default=True,  # optional — Is this election automatically applied in the absence of an election having been made.  May only be true for one election if multiple are provided.
    price=0.0,  # optional — Price per unit of the security. At least one of UnitsRatio or Price must be provided.  Price must non-zero.
    units_ratio=UnitsRatio(...)  # optional
)
```

- [UnitsRatio](UnitsRatio.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

