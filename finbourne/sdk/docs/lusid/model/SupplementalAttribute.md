# SupplementalAttribute

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **attribute_name** | **str** | Required | The reference name of the supplemental attribute. |
| **left_formula** | **str** | Required | Derivation formula evaluated against the left side of the reconciliation. |
| **right_formula** | **str** | Required | Derivation formula evaluated against the right side of the reconciliation. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.SupplementalAttribute import SupplementalAttribute

instance = SupplementalAttribute(
    attribute_name="...",  # required — The reference name of the supplemental attribute.
    left_formula="...",  # required — Derivation formula evaluated against the left side of the reconciliation.
    right_formula="..."  # required — Derivation formula evaluated against the right side of the reconciliation.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

