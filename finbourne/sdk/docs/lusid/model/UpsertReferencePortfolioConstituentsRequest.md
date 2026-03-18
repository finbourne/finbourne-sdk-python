# UpsertReferencePortfolioConstituentsRequest

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **effective_from** | **str** | Required | The first date from which the weights will apply |
| **weight_type** | **str** | Required | The available values are: Static, Floating, Periodical |
| **period_type** | **str** | Optional | The available values are: Daily, Weekly, Monthly, Quarterly, Annually |
| **period_count** | **int** | Optional |  |
| **constituents** | [List[ReferencePortfolioConstituentRequest]](ReferencePortfolioConstituentRequest.md) | Required | Set of constituents (instrument/weight pairings) |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.UpsertReferencePortfolioConstituentsRequest import UpsertReferencePortfolioConstituentsRequest

instance = UpsertReferencePortfolioConstituentsRequest(
    effective_from="...",  # required — The first date from which the weights will apply
    weight_type="...",  # required — The available values are: Static, Floating, Periodical
    period_type="...",  # optional — The available values are: Daily, Weekly, Monthly, Quarterly, Annually
    period_count=0,  # optional — 
    constituents=[]  # required — Set of constituents (instrument/weight pairings)
)
```

- [ReferencePortfolioConstituentRequest](ReferencePortfolioConstituentRequest.md) — used in `constituents`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

