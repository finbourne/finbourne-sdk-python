# CompositeDispersion

A list of Dispersion calculations for the given years.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **effective_at** | **datetime** | Required | The date for which dipsersion calculation has been done. This should be 31 Dec for each given year. |
| **dispersion_calculation** | **float** | Optional | The result for the dispersion calculation on the given effectiveAt. |
| **variance** | **float** | Optional | The variance on the given effectiveAt. |
| **first_quartile** | **float** | Optional | First Quartile (Q1) &#x3D;  (lower quartile) &#x3D; the middle of the bottom half of the returns. |
| **third_quartile** | **float** | Optional | Third Quartile (Q3) &#x3D;  (higher quartile) &#x3D; the middle of the top half of the returns. |
| **range** | **float** | Optional | Highest return - Lowest return. |
| **constituents_in_scope** | [List[ResourceId]](ResourceId.md) | Optional | List containing Composite members which are part of the dispersion calcualtion. |
| **constituents_excluded** | [List[ResourceId]](ResourceId.md) | Optional | List containing the Composite members which are not part of the dispersion calculation |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.CompositeDispersion import CompositeDispersion

instance = CompositeDispersion(
    effective_at=datetime.now(),  # required — The date for which dipsersion calculation has been done. This should be 31 Dec for each given year.
    dispersion_calculation=0.0,  # optional — The result for the dispersion calculation on the given effectiveAt.
    variance=0.0,  # optional — The variance on the given effectiveAt.
    first_quartile=0.0,  # optional — First Quartile (Q1) &#x3D;  (lower quartile) &#x3D; the middle of the bottom half of the returns.
    third_quartile=0.0,  # optional — Third Quartile (Q3) &#x3D;  (higher quartile) &#x3D; the middle of the top half of the returns.
    range=0.0,  # optional — Highest return - Lowest return.
    constituents_in_scope=[],  # optional — List containing Composite members which are part of the dispersion calcualtion.
    constituents_excluded=[]  # optional — List containing the Composite members which are not part of the dispersion calculation
)
```

- [ResourceId](ResourceId.md) — used in `constituents_in_scope`
- [ResourceId](ResourceId.md) — used in `constituents_excluded`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

