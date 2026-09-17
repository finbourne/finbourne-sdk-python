# ReverseStressResponse

The result of a reverse stress solve: the factor the scenario's shifts must be multiplied by to  reach the target loss, together with the whole evaluated ladder so the answer can be checked  rather than taken on trust.                The ladder is part of the answer, not diagnostics. A reverse stress is only meaningful where the  loss moves in one direction with the factor, and the ladder is what shows that it does.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **scale** | **float** | Optional | The solved factor: the multiple of the scenario&#39;s shifts that reaches the target. Null when no  factor within the evaluated range reaches it, in which case Converged is false and the  warnings say so. |
| **target_pnl** | **float** | Optional | The change in value that was asked for, echoed back. |
| **achieved_pnl** | **float** | Optional | The change in value actually produced at the solved scale, measured by a valuation at that  factor rather than interpolated. The gap to the target is the honest error of the solve. |
| **base_value** | **float** | Optional | The unstressed value of the measure over the filtered holdings. |
| **stressed_value** | **float** | Optional | The value of the measure at the solved scale. |
| **converged** | **bool** | Optional | Whether the achieved change is within the requested tolerance of the target. False means the  reported scale is the best reached, not an answer to rely on. |
| **method** | **str** | Optional | How the bracketing factor was turned into the reported one: \&quot;Interpolation\&quot; on a monotone  ladder, \&quot;Bisection\&quot; where the ladder turned back on itself and interpolating between one  bracketing pair would have hidden the others. |
| **valuations** | **int** | Optional | How many valuations the solve ran, the opening ladder counting as one. |
| **ladder** | [List[ReverseStressRung]](ReverseStressRung.md) | Optional | Every factor evaluated, in increasing order, including the confirming valuations. |
| **warnings** | **List[str]** | Optional | Anything the caller has to know to read the scale correctly: a non-monotone ladder, a target  out of reach, a solve stopped at the iteration limit. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.ReverseStressResponse import ReverseStressResponse

instance = ReverseStressResponse(
    scale=0.0,  # optional — The solved factor: the multiple of the scenario&#39;s shifts that reaches the target. Null when no  factor within the evaluated range reaches it, in which case Converged is false and the  warnings say so.
    target_pnl=0.0,  # optional — The change in value that was asked for, echoed back.
    achieved_pnl=0.0,  # optional — The change in value actually produced at the solved scale, measured by a valuation at that  factor rather than interpolated. The gap to the target is the honest error of the solve.
    base_value=0.0,  # optional — The unstressed value of the measure over the filtered holdings.
    stressed_value=0.0,  # optional — The value of the measure at the solved scale.
    converged=True,  # optional — Whether the achieved change is within the requested tolerance of the target. False means the  reported scale is the best reached, not an answer to rely on.
    method="...",  # optional — How the bracketing factor was turned into the reported one: \&quot;Interpolation\&quot; on a monotone  ladder, \&quot;Bisection\&quot; where the ladder turned back on itself and interpolating between one  bracketing pair would have hidden the others.
    valuations=0,  # optional — How many valuations the solve ran, the opening ladder counting as one.
    ladder=[],  # optional — Every factor evaluated, in increasing order, including the confirming valuations.
    warnings=  # optional — Anything the caller has to know to read the scale correctly: a non-monotone ladder, a target  out of reach, a solve stopped at the iteration limit.
)
```

- [ReverseStressRung](ReverseStressRung.md) — used in `ladder`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

