# ElectionSpecification

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **election_type** | **str** | Required | Available values: CashElection, CashAndSecurityOfferElection, CashOfferElection, EarlyRedemptionElection, LapseElection, OptionExerciseElection, SecurityElection, SecurityOfferElection, TenderOfferElection, MixedLotConstituentsElection. |
| **cardinality** | **Dict[str, Optional[str]]** | Required | *No description available.* |
| **referenced_as** | **List[str]** | Required | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.ElectionSpecification import ElectionSpecification

instance = ElectionSpecification(
    election_type="...",  # required — Available values: CashElection, CashAndSecurityOfferElection, CashOfferElection, EarlyRedemptionElection, LapseElection, OptionExerciseElection, SecurityElection, SecurityOfferElection, TenderOfferElection, MixedLotConstituentsElection.
    cardinality=,  # required
    referenced_as=  # required
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

