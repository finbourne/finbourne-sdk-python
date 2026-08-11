# WeightedAllocationServiceRunRequest

The request body for the RunAllocationServiceWithWeights endpoint.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **placement_ids** | [List[ResourceId]](ResourceId.md) | Required | The set of Placement IDs to allocate. |
| **portfolio_weights** | [List[PortfolioWeight]](PortfolioWeight.md) | Optional | The set of Portfolios and their associated weights to use for allocation. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.WeightedAllocationServiceRunRequest import WeightedAllocationServiceRunRequest

instance = WeightedAllocationServiceRunRequest(
    placement_ids=[],  # required — The set of Placement IDs to allocate.
    portfolio_weights=[]  # optional — The set of Portfolios and their associated weights to use for allocation.
)
```


## Related Models

- [ResourceId](ResourceId.md) — used in `placement_ids`
- [PortfolioWeight](PortfolioWeight.md) — used in `portfolio_weights`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

