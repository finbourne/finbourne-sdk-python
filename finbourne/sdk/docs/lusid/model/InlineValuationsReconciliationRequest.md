# InlineValuationsReconciliationRequest

Specification for the reconciliation request. Left and Right hand sides are constructed. Each consists of a valuation of a inline set of instruments  using an inline aggregation request. The results of this can then be compared to each other. The difference, which is effectively a risk based  difference allows comparison of the effects of changing a recipe, valuation date, or (though it may or may not make logical sense) a set of instruments.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **left** | [InlineValuationRequest](InlineValuationRequest.md) | Required | *No description available.* |
| **right** | [InlineValuationRequest](InlineValuationRequest.md) | Required | *No description available.* |
| **left_to_right_mapping** | [List[ReconciliationLeftRightAddressKeyPair]](ReconciliationLeftRightAddressKeyPair.md) | Optional | The mapping from property keys requested by left aggregation to property keys on right hand side |
| **preserve_keys** | **List[str]** | Optional | List of keys to preserve (from rhs) in the diff. Used in conjunction with filtering/grouping |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.InlineValuationsReconciliationRequest import InlineValuationsReconciliationRequest

instance = InlineValuationsReconciliationRequest(
    left=InlineValuationRequest(...),  # required
    right=InlineValuationRequest(...),  # required
    left_to_right_mapping=[],  # optional — The mapping from property keys requested by left aggregation to property keys on right hand side
    preserve_keys=  # optional — List of keys to preserve (from rhs) in the diff. Used in conjunction with filtering/grouping
)
```


## Related Models

- [InlineValuationRequest](InlineValuationRequest.md)
- [InlineValuationRequest](InlineValuationRequest.md)
- [ReconciliationLeftRightAddressKeyPair](ReconciliationLeftRightAddressKeyPair.md) — used in `left_to_right_mapping`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

