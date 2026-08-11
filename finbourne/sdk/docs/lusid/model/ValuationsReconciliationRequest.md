# ValuationsReconciliationRequest

Specification for the reconciliation request. Left and Right hand sides are constructed. Each consists of a valuation of a portfolio  using an aggregation request. The results of this can then be compared to each other. The difference, which is effectively a risk based  difference allows comparison of the effects of changing a recipe, valuation date, or (though it may or may not make logical sense) a portfolio.  For instance, one might look at the difference in risk caused by the addition of transaction to a portfolio, or through changing the valuation  methodology or system.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **left** | [ValuationRequest](ValuationRequest.md) | Required | *No description available.* |
| **right** | [ValuationRequest](ValuationRequest.md) | Required | *No description available.* |
| **left_to_right_mapping** | [List[ReconciliationLeftRightAddressKeyPair]](ReconciliationLeftRightAddressKeyPair.md) | Optional | The mapping from property keys requested by left aggregation to property keys on right hand side |
| **preserve_keys** | **List[str]** | Optional | List of keys to preserve (from rhs) in the diff. Used in conjunction with filtering/grouping.  If two values are equal, for a given key then the value is elided from the results. Setting it here  will preserve it (takes the values from the RHS and puts it into the line by line results). |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.ValuationsReconciliationRequest import ValuationsReconciliationRequest

instance = ValuationsReconciliationRequest(
    left=ValuationRequest(...),  # required
    right=ValuationRequest(...),  # required
    left_to_right_mapping=[],  # optional — The mapping from property keys requested by left aggregation to property keys on right hand side
    preserve_keys=  # optional — List of keys to preserve (from rhs) in the diff. Used in conjunction with filtering/grouping.  If two values are equal, for a given key then the value is elided from the results. Setting it here  will preserve it (takes the values from the RHS and puts it into the line by line results).
)
```


## Related Models

- [ValuationRequest](ValuationRequest.md)
- [ValuationRequest](ValuationRequest.md)
- [ReconciliationLeftRightAddressKeyPair](ReconciliationLeftRightAddressKeyPair.md) — used in `left_to_right_mapping`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

