# GetReferencePortfolioConstituentsResponse

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **effective_from** | **datetime** | Required |  |
| **weight_type** | **str** | Required | The available values are: Static, Floating, Periodical |
| **period_type** | **str** | Optional | The available values are: Daily, Weekly, Monthly, Quarterly, Annually |
| **period_count** | **int** | Optional |  |
| **constituents** | [List[ReferencePortfolioConstituent]](ReferencePortfolioConstituent.md) | Required | Set of constituents (instrument/weight pairings) |
| **href** | **str** | Optional | The Uri that returns the same result as the original request,  but may include resolved as at time(s). |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.GetReferencePortfolioConstituentsResponse import GetReferencePortfolioConstituentsResponse

instance = GetReferencePortfolioConstituentsResponse(
    effective_from=datetime.now(),  # required — 
    weight_type="...",  # required — The available values are: Static, Floating, Periodical
    period_type="...",  # optional — The available values are: Daily, Weekly, Monthly, Quarterly, Annually
    period_count=0,  # optional — 
    constituents=[],  # required — Set of constituents (instrument/weight pairings)
    href="...",  # optional — The Uri that returns the same result as the original request,  but may include resolved as at time(s).
    links=[]  # optional
)
```

- [ReferencePortfolioConstituent](ReferencePortfolioConstituent.md) — used in `constituents`
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

