# RiskBumpOptions

Per-recipe configuration of the bump sizes used by the finite-difference Risk/* measures.  Results are always reported per ResultSensitivity regardless of the shift used to compute  them: the calculators divide by shift/resultSensitivity, so choosing a wider shift (e.g.  10bp for a market element with coarse quote precision) changes the estimator, not the unit.  Every member is optional and an absent member keeps the historical default.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **delta_shift** | **float** | Optional | The shift applied for delta/gamma bumps on any asset type without an explicit override.  Must be strictly positive. Defaults to 0.0001 (1bp) when not supplied. |
| **result_sensitivity** | **float** | Optional | The move the reported sensitivity is normalised to. Must be strictly positive.  Defaults to 0.0001 (results per 1bp move) when not supplied. |
| **delta_shift_overrides** | **Dict[str, float]** | Optional | Per-asset-type overrides of the delta shift, keyed by asset type (e.g. \&quot;Rates\&quot;, \&quot;Credit\&quot;,  \&quot;Fx\&quot;). Values must be strictly positive. Asset types without an override use DeltaShift. |
| **ladder_shift_overrides** | **Dict[str, Optional[List[float]]]** | Optional | Per-asset-type overrides of the shift grid used by ladder measures, keyed by asset type  (e.g. \&quot;Rates\&quot;, \&quot;Fx\&quot;). Each grid must be non-empty and strictly increasing; zero is a  legitimate rung, as the default grids include the base scenario. Asset types without an  override use the standard grids. |
| **parity_relative_tolerance** | **float** | Optional | The relative tolerance for RiskEngine \&quot;Parity\&quot; checks, applied as  |bump - adjoint| &lt;&#x3D; max(absolute floor, |bump| * tolerance). Defaults to 0.001. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.RiskBumpOptions import RiskBumpOptions

instance = RiskBumpOptions(
    delta_shift=0.0,  # optional — The shift applied for delta/gamma bumps on any asset type without an explicit override.  Must be strictly positive. Defaults to 0.0001 (1bp) when not supplied.
    result_sensitivity=0.0,  # optional — The move the reported sensitivity is normalised to. Must be strictly positive.  Defaults to 0.0001 (results per 1bp move) when not supplied.
    delta_shift_overrides=,  # optional — Per-asset-type overrides of the delta shift, keyed by asset type (e.g. \&quot;Rates\&quot;, \&quot;Credit\&quot;,  \&quot;Fx\&quot;). Values must be strictly positive. Asset types without an override use DeltaShift.
    ladder_shift_overrides=,  # optional — Per-asset-type overrides of the shift grid used by ladder measures, keyed by asset type  (e.g. \&quot;Rates\&quot;, \&quot;Fx\&quot;). Each grid must be non-empty and strictly increasing; zero is a  legitimate rung, as the default grids include the base scenario. Asset types without an  override use the standard grids.
    parity_relative_tolerance=0.0  # optional — The relative tolerance for RiskEngine \&quot;Parity\&quot; checks, applied as  |bump - adjoint| &lt;&#x3D; max(absolute floor, |bump| * tolerance). Defaults to 0.001.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

