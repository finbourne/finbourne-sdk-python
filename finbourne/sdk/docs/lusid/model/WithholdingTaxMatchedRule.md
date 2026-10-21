# WithholdingTaxMatchedRule

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **matched_rule_id** | **str** | Required | The identifier booking stamps for the matched row: its series identifiers and effective date. |
| **matched_dataset** | **str** | Required | The dataset the matched row came from: Main or Anomaly. |
| **rule_source** | **str** | Optional | The rule source of the matched row. Null when the row has none. |
| **effective_at** | **datetime** | Required | The effective date of the matched row version. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.WithholdingTaxMatchedRule import WithholdingTaxMatchedRule

instance = WithholdingTaxMatchedRule(
    matched_rule_id="...",  # required — The identifier booking stamps for the matched row: its series identifiers and effective date.
    matched_dataset="...",  # required — The dataset the matched row came from: Main or Anomaly.
    rule_source="...",  # optional — The rule source of the matched row. Null when the row has none.
    effective_at=datetime.now()  # required — The effective date of the matched row version.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

