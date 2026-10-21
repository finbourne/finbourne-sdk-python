# WithholdingTaxAlternativeMatch

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **if_values** | **Dict[str, Optional[str]]** | Required | The values of the unresolved dimensions that choose this row, one or more. |
| **matched_rule_id** | **str** | Required | The identifier booking would stamp for the row that these values choose. |
| **stop_at_source_rate** | **float** | Required | The rate that this row would withhold at source. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.WithholdingTaxAlternativeMatch import WithholdingTaxAlternativeMatch

instance = WithholdingTaxAlternativeMatch(
    if_values=,  # required — The values of the unresolved dimensions that choose this row, one or more.
    matched_rule_id="...",  # required — The identifier booking would stamp for the row that these values choose.
    stop_at_source_rate=0.0  # required — The rate that this row would withhold at source.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

