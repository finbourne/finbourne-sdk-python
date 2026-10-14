# DirectionSpreads

The tiers of spread for one direction of net cashflow and what their bounds measure.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **basis** | **str** | Required | What the tier bounds measure: Amount, the size of the net cashflow in the fund currency, or PctOfNav, the net cashflow as a percentage of the previous valuation point&#39;s NAV. Available values: Amount, PctOfNav. |
| **tiers** | [List[SwingSpreadTier]](SwingSpreadTier.md) | Required | The tiers, in ascending order. Each starts where the previous one ends, and only the last is unbounded above. The first tier&#39;s lower bound is the threshold: a flow at or below it does not swing. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.DirectionSpreads import DirectionSpreads

instance = DirectionSpreads(
    basis="...",  # required — What the tier bounds measure: Amount, the size of the net cashflow in the fund currency, or PctOfNav, the net cashflow as a percentage of the previous valuation point&#39;s NAV. Available values: Amount, PctOfNav.
    tiers=[]  # required — The tiers, in ascending order. Each starts where the previous one ends, and only the last is unbounded above. The first tier&#39;s lower bound is the threshold: a flow at or below it does not swing.
)
```

- [SwingSpreadTier](SwingSpreadTier.md) — used in `tiers`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

