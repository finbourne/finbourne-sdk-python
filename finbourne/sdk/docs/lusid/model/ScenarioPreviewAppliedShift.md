# ScenarioPreviewAppliedShift

One market data target changed by one scenario shift.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **effective_at** | **datetime** | Optional | The effective date of the market data the shift was applied to. |
| **shift** | **str** | Optional | Description of the shift, e.g. \&quot;EquityShift on &#39;SCENARIO_EQUITY&#39;\&quot;. |
| **target** | **str** | Optional | Description of the market data target the shift changed. |
| **value_before** | **float** | Optional | The target&#39;s value before the shift. Null for multi-point targets (e.g. whole curves) where a  single number is not meaningful. |
| **value_after** | **float** | Optional | The target&#39;s value after the shift. Null for multi-point targets. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.ScenarioPreviewAppliedShift import ScenarioPreviewAppliedShift

instance = ScenarioPreviewAppliedShift(
    effective_at=datetime.now(),  # optional — The effective date of the market data the shift was applied to.
    shift="...",  # optional — Description of the shift, e.g. \&quot;EquityShift on &#39;SCENARIO_EQUITY&#39;\&quot;.
    target="...",  # optional — Description of the market data target the shift changed.
    value_before=0.0,  # optional — The target&#39;s value before the shift. Null for multi-point targets (e.g. whole curves) where a  single number is not meaningful.
    value_after=0.0  # optional — The target&#39;s value after the shift. Null for multi-point targets.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

