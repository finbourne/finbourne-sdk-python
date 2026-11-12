# ComplianceComparisonOperand

One side of a comparison: the sub-expression that produced it and, where the group carried the data to evaluate it,  its value. The value is absent for a non-numeric constant, a reference list, or an operand the group held no data for.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **expression** | **str** | Required | *No description available.* |
| **value** | **float** | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.ComplianceComparisonOperand import ComplianceComparisonOperand

instance = ComplianceComparisonOperand(
    expression="...",  # required
    value=0.0  # optional
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

