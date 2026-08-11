# TransactionReconciliationRequestV2

Specification for the reconciliation request. Left and Right hand sides are constructed. Each consists of transactions from a portfolio  The results of this can then be compared to each other.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **left** | [AggregatedTransactionsRequest](AggregatedTransactionsRequest.md) | Required | *No description available.* |
| **right** | [AggregatedTransactionsRequest](AggregatedTransactionsRequest.md) | Required | *No description available.* |
| **left_to_right_mapping** | [List[ReconciliationLeftRightAddressKeyPair]](ReconciliationLeftRightAddressKeyPair.md) | Optional | The mapping from property keys requested by left aggregation to property keys on right hand side |
| **comparison_rules** | [List[ReconciliationRule]](ReconciliationRule.md) | Optional | The set of rules to be used in comparing values. These are the rules that determine what constitutes a match.  The simplest is obviously an exact one-for-one comparison, but tolerances on numerical or date time values and  case-insensitive string comparison are supported amongst other types. |
| **preserve_keys** | **List[str]** | Optional | List of keys to preserve (from rhs) in the diff. Used in conjunction with filtering/grouping.  If two values are equal, for a given key then the value is elided from the results. Setting it here  will preserve it (takes the values from the RHS and puts it into the line by line results). |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.TransactionReconciliationRequestV2 import TransactionReconciliationRequestV2

instance = TransactionReconciliationRequestV2(
    left=AggregatedTransactionsRequest(...),  # required
    right=AggregatedTransactionsRequest(...),  # required
    left_to_right_mapping=[],  # optional — The mapping from property keys requested by left aggregation to property keys on right hand side
    comparison_rules=[],  # optional — The set of rules to be used in comparing values. These are the rules that determine what constitutes a match.  The simplest is obviously an exact one-for-one comparison, but tolerances on numerical or date time values and  case-insensitive string comparison are supported amongst other types.
    preserve_keys=  # optional — List of keys to preserve (from rhs) in the diff. Used in conjunction with filtering/grouping.  If two values are equal, for a given key then the value is elided from the results. Setting it here  will preserve it (takes the values from the RHS and puts it into the line by line results).
)
```


## Related Models

- [AggregatedTransactionsRequest](AggregatedTransactionsRequest.md)
- [AggregatedTransactionsRequest](AggregatedTransactionsRequest.md)
- [ReconciliationLeftRightAddressKeyPair](ReconciliationLeftRightAddressKeyPair.md) — used in `left_to_right_mapping`
- [ReconciliationRule](ReconciliationRule.md) — used in `comparison_rules`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

