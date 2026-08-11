# ReconciledTransaction

Information about reconciled transactions.  At least one of Left and Right will be populated.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **left** | [Transaction](Transaction.md) | Optional | *No description available.* |
| **right** | [Transaction](Transaction.md) | Optional | *No description available.* |
| **percentage_match** | **float** | Optional | How good a match this is considered to be. |
| **mapping_rule_set_results** | **List[bool]** | Optional | The result of each individual mapping rule result.  Will only be present if both Left and Right are populated. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.ReconciledTransaction import ReconciledTransaction

instance = ReconciledTransaction(
    left=Transaction(...),  # optional
    right=Transaction(...),  # optional
    percentage_match=0.0,  # optional — How good a match this is considered to be.
    mapping_rule_set_results=  # optional — The result of each individual mapping rule result.  Will only be present if both Left and Right are populated.
)
```


## Related Models

- [Transaction](Transaction.md)
- [Transaction](Transaction.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

