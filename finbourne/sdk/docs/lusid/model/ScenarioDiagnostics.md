# ScenarioDiagnostics

Diagnostics for the scenario shifts a valuation applied: every market data target changed by a  shift, with values before and after, plus warnings for market data that matched a shift but could  not honour it. Populated whenever the valuation ran with a request-level scenario or  scenario-decorated metrics; null otherwise. The same material is written to the market data  manifest.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **applied** | [List[AppliedScenarioShift]](AppliedScenarioShift.md) | Optional | One entry per market data target changed by a shift. |
| **skipped** | **List[str]** | Optional | Market data that matched a shift but was skipped (e.g. an element type that does not support  transformation), with the reason. Prefixed with the scenario&#39;s \&quot;scope/code\&quot; reference. |
| **omitted_applied** | **int** | Optional | The number of further applied records omitted from this section, when the valuation changed  more targets than the section carries (large portfolios over long schedules). Null when  nothing was omitted. The market data manifest always carries the complete set. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.ScenarioDiagnostics import ScenarioDiagnostics

instance = ScenarioDiagnostics(
    applied=[],  # optional — One entry per market data target changed by a shift.
    skipped=,  # optional — Market data that matched a shift but was skipped (e.g. an element type that does not support  transformation), with the reason. Prefixed with the scenario&#39;s \&quot;scope/code\&quot; reference.
    omitted_applied=0  # optional — The number of further applied records omitted from this section, when the valuation changed  more targets than the section carries (large portfolios over long schedules). Null when  nothing was omitted. The market data manifest always carries the complete set.
)
```


## Related Models

- [AppliedScenarioShift](AppliedScenarioShift.md) — used in `applied`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

