# ReconciliationLine

In evaluating a left and right hand side holding or valuation set, two data records result. These are then compared based on a set of  rules. This results in either a match or failure to match. If there is a match both left and right will be present, otherwise one will not.  A difference will be present if a match was calculated.  The options used in comparison may result in elision of results where an exact or tolerable match is made.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **left** | **Dict[str, Optional[object]]** | Optional | Left hand side of the comparison |
| **right** | **Dict[str, Optional[object]]** | Optional | Right hand side of the comparison |
| **difference** | **Dict[str, Optional[object]]** | Optional | Difference between LHS and RHS of comparison |
| **result_comparison** | **Dict[str, Optional[object]]** | Optional | The logical or semantic description of the difference, e.g. \&quot;Matches\&quot; or \&quot;MatchesWithTolerance\&quot; or \&quot;Failed\&quot;. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.ReconciliationLine import ReconciliationLine

instance = ReconciliationLine(
    left=,  # optional — Left hand side of the comparison
    right=,  # optional — Right hand side of the comparison
    difference=,  # optional — Difference between LHS and RHS of comparison
    result_comparison=  # optional — The logical or semantic description of the difference, e.g. \&quot;Matches\&quot; or \&quot;MatchesWithTolerance\&quot; or \&quot;Failed\&quot;.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

