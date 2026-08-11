# CompositeBreakdown

A list of Composite Breakdowns.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **effective_at** | **datetime** | Required | The effectiveAt for the calculation. |
| **composite** | [PortfolioReturnBreakdown](PortfolioReturnBreakdown.md) | Optional | *No description available.* |
| **constituents** | [List[PortfolioReturnBreakdown]](PortfolioReturnBreakdown.md) | Optional | The constituents with their information which are part of the composite. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.CompositeBreakdown import CompositeBreakdown

instance = CompositeBreakdown(
    effective_at=datetime.now(),  # required — The effectiveAt for the calculation.
    composite=PortfolioReturnBreakdown(...),  # optional
    constituents=[]  # optional — The constituents with their information which are part of the composite.
)
```

- [PortfolioReturnBreakdown](PortfolioReturnBreakdown.md)
- [PortfolioReturnBreakdown](PortfolioReturnBreakdown.md) — used in `constituents`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

