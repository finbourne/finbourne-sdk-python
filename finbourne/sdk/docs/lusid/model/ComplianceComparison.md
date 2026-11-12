# ComplianceComparison

A single leaf comparison the check criterion made, re-evaluated for this group. A result of null is a comparison the  group held no data for (the criterion short-circuited past it).
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **predicate** | **str** | Required | *No description available.* |
| **left** | [ComplianceComparisonOperand](ComplianceComparisonOperand.md) | Required | *No description available.* |
| **operator** | **str** | Required | *No description available.* |
| **right** | [ComplianceComparisonOperand](ComplianceComparisonOperand.md) | Required | *No description available.* |
| **passed** | **bool** | Optional | Whether this leaf met its criterion for the group: true where it held, false for a breaching leaf. Absent for a  comparison the group carried no data for (the criterion short-circuited past it). |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.ComplianceComparison import ComplianceComparison

instance = ComplianceComparison(
    predicate="...",  # required
    left=ComplianceComparisonOperand(...),  # required
    operator="...",  # required
    right=ComplianceComparisonOperand(...),  # required
    passed=True  # optional — Whether this leaf met its criterion for the group: true where it held, false for a breaching leaf. Absent for a  comparison the group carried no data for (the criterion short-circuited past it).
)
```

- [ComplianceComparisonOperand](ComplianceComparisonOperand.md)
- [ComplianceComparisonOperand](ComplianceComparisonOperand.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

