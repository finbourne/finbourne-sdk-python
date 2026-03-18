# ReconcileNumericRule

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **comparison_type** | **str** | Required | The available values are: Exact, AbsoluteDifference, RelativeDifference |
| **tolerance** | **float** | Optional | For a numeric type only (i.e. decimal, integer, date or datetime offset possibly controversially), this is the quantity used in the comparison.  The units of the tolerance must be set appropriately for the item being compared.  For a number such as a currency or amount that will be a simple quantity, for a DateTime or DateTimeOffset it should be days. If fewer than a single day then this should be  passed as a fraction. |
| **applies_to** | [AggregateSpec](AggregateSpec.md) | Required | *No description available.* |
| **rule_type** | **str** | Required | The available values are: ReconcileNumericRule, ReconcileDateTimeRule, ReconcileStringRule, ReconcileExact |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.ReconcileNumericRule import ReconcileNumericRule

instance = ReconcileNumericRule(
    comparison_type="...",  # required — The available values are: Exact, AbsoluteDifference, RelativeDifference
    tolerance=0.0,  # optional — For a numeric type only (i.e. decimal, integer, date or datetime offset possibly controversially), this is the quantity used in the comparison.  The units of the tolerance must be set appropriately for the item being compared.  For a number such as a currency or amount that will be a simple quantity, for a DateTime or DateTimeOffset it should be days. If fewer than a single day then this should be  passed as a fraction.
    applies_to=AggregateSpec(...),  # required
    rule_type="..."  # required — The available values are: ReconcileNumericRule, ReconcileDateTimeRule, ReconcileStringRule, ReconcileExact
)
```

- [AggregateSpec](AggregateSpec.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

