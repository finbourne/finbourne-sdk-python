# RankMarginCallRequest

Ranks a margin call's collateral again against the holdings as they stand now, keeping the assets the user chose.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **overrides** | [List[CollateralAllocationOverride]](CollateralAllocationOverride.md) | Optional | The assets and units the user chose, each validated against the agreement&#39;s constraints and kept with its reason when it fails one. Optional. |
| **fill_remainder** | **bool** | Optional | Whether to fill what the overrides leave uncovered from the ranking, cheapest first. Defaults to true. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.RankMarginCallRequest import RankMarginCallRequest

instance = RankMarginCallRequest(
    overrides=[],  # optional — The assets and units the user chose, each validated against the agreement&#39;s constraints and kept with its reason when it fails one. Optional.
    fill_remainder=True  # optional — Whether to fill what the overrides leave uncovered from the ranking, cheapest first. Defaults to true.
)
```


## Related Models

- [CollateralAllocationOverride](CollateralAllocationOverride.md) — used in `overrides`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

