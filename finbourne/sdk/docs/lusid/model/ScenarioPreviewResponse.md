# ScenarioPreviewResponse

The result of previewing a scenario: every market data target the scenario's shifts changed, with  values before and after, plus warnings for market data that matched a shift but could not honour it.  An empty applied list means the scenario would touch nothing for this portfolio and recipe.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **applied** | [List[ScenarioPreviewAppliedShift]](ScenarioPreviewAppliedShift.md) | Optional | One entry per market data target changed by a shift. |
| **skipped** | **List[str]** | Optional | Market data that matched a shift but was skipped (e.g. an element type that does not support  transformation), with the reason. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.ScenarioPreviewResponse import ScenarioPreviewResponse

instance = ScenarioPreviewResponse(
    applied=[],  # optional — One entry per market data target changed by a shift.
    skipped=  # optional — Market data that matched a shift but was skipped (e.g. an element type that does not support  transformation), with the reason.
)
```


## Related Models

- [ScenarioPreviewAppliedShift](ScenarioPreviewAppliedShift.md) — used in `applied`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

