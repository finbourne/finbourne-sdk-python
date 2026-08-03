# MdkrGroupShiftDefinition

A group of keyed market data key rules (e.g. bid/mid/ask). When the scenario is used in a  valuation, each key's rule re-resolves the matching market data dependencies independently and  produces its own result column named scenario:key, alongside the base column - which continues to  resolve through the recipe's own rules in the standard waterfall, whether or not the same rules  appear here.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **rules** | [List[KeyedMarketDataKeyRule]](KeyedMarketDataKeyRule.md) | Required | The keyed rules of the group. Keys must be unique within the group; each key produces one  result column. |
| **scenario_shift_type** | **str** | Required | Available values: RateCurveShiftDefinition, FxShiftDefinition, EquityShiftDefinition, VolSurfaceShiftDefinition, MdkrGroupShiftDefinition. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.MdkrGroupShiftDefinition import MdkrGroupShiftDefinition

instance = MdkrGroupShiftDefinition(
    rules=[],  # required — The keyed rules of the group. Keys must be unique within the group; each key produces one  result column.
    scenario_shift_type="..."  # required — Available values: RateCurveShiftDefinition, FxShiftDefinition, EquityShiftDefinition, VolSurfaceShiftDefinition, MdkrGroupShiftDefinition.
)
```


## Related Models

- [KeyedMarketDataKeyRule](KeyedMarketDataKeyRule.md) — used in `rules`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

