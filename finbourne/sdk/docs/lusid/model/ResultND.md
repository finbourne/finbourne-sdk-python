# ResultND

A single result-value shape whose structure is derived from `dimension`, replacing one  hand-maintained type per rank (Result0D/Result1D/Result2D). Risk measures of dimension 1, 2  or 3 - the ladders, the surfaces and the IR vol cubes - now report this shape rather than  Result1D/Result2D, so their response bytes change: the values arrive nested and dense here  (see `values`), where the legacy types carried a flat \"(row,column)\"-keyed map that  elided unquoted coordinates, and the units arrive as one flat list rather than the doubled  `{ units: { units: [] } }` wrapper. Dimension 0 measures are untouched and stay on the  legacy shapes.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **result_value_type** | **str** | Optional | The discriminator for this result shape. Always \&quot;ResultND\&quot;. *(read-only)* |
| **dimension** | **int** | Optional | The rank of the result, 0..N. Determines which of &#x60;value&#x60; / &#x60;values&#x60; is populated  and how deeply &#x60;values&#x60; is nested. |
| **labels** | **List[List[str]]** | Optional | One ordered array of labels per axis, index to label, in the same axis order as  &#x60;AddressDefinition.Axes&#x60;. Length equals &#x60;dimension&#x60;; empty for a scalar. |
| **value** | **float** | Optional | The scalar value. Present if and only if &#x60;dimension&#x60; is 0. |
| **values** | **object** | Optional | The values, nested exactly &#x60;dimension&#x60; deep (axis 0 outermost) and dense - a coordinate  the legacy format would have elided is null, never a fabricated number. Present if and only  if &#x60;dimension&#x60; is at least 1. |
| **has_annotation** | **bool** | Optional | Unchanged from Result0D/1D/2D. |
| **units** | [List[UnitDimension]](UnitDimension.md) | Optional | A flat list of dimensional-analysis units, replacing the doubled  &#x60;{ units: { units: [] } }&#x60; wrapper on the legacy types. The count reflects the order of  the derivative (e.g. two entries for a ratio such as a rates delta), not the result&#39;s axes. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.ResultND import ResultND

instance = ResultND(
    result_value_type="...",  # optional — The discriminator for this result shape. Always \&quot;ResultND\&quot;.
    dimension=0,  # optional — The rank of the result, 0..N. Determines which of &#x60;value&#x60; / &#x60;values&#x60; is populated  and how deeply &#x60;values&#x60; is nested.
    labels=,  # optional — One ordered array of labels per axis, index to label, in the same axis order as  &#x60;AddressDefinition.Axes&#x60;. Length equals &#x60;dimension&#x60;; empty for a scalar.
    value=0.0,  # optional — The scalar value. Present if and only if &#x60;dimension&#x60; is 0.
    values=,  # optional — The values, nested exactly &#x60;dimension&#x60; deep (axis 0 outermost) and dense - a coordinate  the legacy format would have elided is null, never a fabricated number. Present if and only  if &#x60;dimension&#x60; is at least 1.
    has_annotation=True,  # optional — Unchanged from Result0D/1D/2D.
    units=[]  # optional — A flat list of dimensional-analysis units, replacing the doubled  &#x60;{ units: { units: [] } }&#x60; wrapper on the legacy types. The count reflects the order of  the derivative (e.g. two entries for a ratio such as a rates delta), not the result&#39;s axes.
)
```

- [UnitDimension](UnitDimension.md) — used in `units`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

