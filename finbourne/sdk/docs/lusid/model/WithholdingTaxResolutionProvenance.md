# WithholdingTaxResolutionProvenance

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **match_score** | **float** | Optional | The share of the main dataset&#39;s dimensions that the row matches, from 0 to 1. Null on an anomaly match. |
| **matched_field_count** | **int** | Optional | The number of the main dataset&#39;s dimensions that the row matches. Null on an anomaly match. |
| **source_filter_applied** | **str** | Optional | The rule source level that matched. Null when no source priority applies. |
| **tie_broken** | **bool** | Required | True when another row matched as well as the winner, so the tie-break order chose: the latest effective date, then the rule id. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.WithholdingTaxResolutionProvenance import WithholdingTaxResolutionProvenance

instance = WithholdingTaxResolutionProvenance(
    match_score=0.0,  # optional — The share of the main dataset&#39;s dimensions that the row matches, from 0 to 1. Null on an anomaly match.
    matched_field_count=0,  # optional — The number of the main dataset&#39;s dimensions that the row matches. Null on an anomaly match.
    source_filter_applied="...",  # optional — The rule source level that matched. Null when no source priority applies.
    tie_broken=True  # required — True when another row matched as well as the winner, so the tie-break order chose: the latest effective date, then the rule id.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

