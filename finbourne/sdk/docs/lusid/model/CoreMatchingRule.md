# CoreMatchingRule

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **rule_name** | **str** | Required | The reference name of the rule. |
| **left_formula** | **str** | Required | Derivation formula evaluated against the left side of the reconciliation. |
| **right_formula** | **str** | Required | Derivation formula evaluated against the right side of the reconciliation. |
| **is_case_sensitive** | **bool** | Optional | Whether the core rule comparison is case sensitive. Defaults to false. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.CoreMatchingRule import CoreMatchingRule

instance = CoreMatchingRule(
    rule_name="...",  # required — The reference name of the rule.
    left_formula="...",  # required — Derivation formula evaluated against the left side of the reconciliation.
    right_formula="...",  # required — Derivation formula evaluated against the right side of the reconciliation.
    is_case_sensitive=True  # optional — Whether the core rule comparison is case sensitive. Defaults to false.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

