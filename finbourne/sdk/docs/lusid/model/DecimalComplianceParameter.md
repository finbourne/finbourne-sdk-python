# DecimalComplianceParameter

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **value** | **float** | Required | *No description available.* |
| **inclusive_bounds** | **bool** | Optional | Whether the bound is inclusive of the value; when true a candidate landing exactly on the bound satisfies it. Defaults to false (exclusive). |
| **compliance_parameter_type** | **str** | Required | The parameter type. Available values: BoolComplianceParameter, StringComplianceParameter, DecimalComplianceParameter, DateTimeComplianceParameter, PropertyKeyComplianceParameter, AddressKeyComplianceParameter, PortfolioIdComplianceParameter, PortfolioGroupIdComplianceParameter, StringListComplianceParameter, BoolListComplianceParameter, DateTimeListComplianceParameter, DecimalListComplianceParameter, PropertyKeyListComplianceParameter, AddressKeyListComplianceParameter, PortfolioIdListComplianceParameter, PortfolioGroupIdListComplianceParameter, InstrumentListComplianceParameter, FilterPredicateComplianceParameter, GroupFilterPredicateComplianceParameter, GroupBySelectorComplianceParameter, PropertyListComplianceParameter, GroupCalculationComplianceParameter. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.DecimalComplianceParameter import DecimalComplianceParameter

instance = DecimalComplianceParameter(
    value=0.0,  # required
    inclusive_bounds=True,  # optional — Whether the bound is inclusive of the value; when true a candidate landing exactly on the bound satisfies it. Defaults to false (exclusive).
    compliance_parameter_type="..."  # required — The parameter type. Available values: BoolComplianceParameter, StringComplianceParameter, DecimalComplianceParameter, DateTimeComplianceParameter, PropertyKeyComplianceParameter, AddressKeyComplianceParameter, PortfolioIdComplianceParameter, PortfolioGroupIdComplianceParameter, StringListComplianceParameter, BoolListComplianceParameter, DateTimeListComplianceParameter, DecimalListComplianceParameter, PropertyKeyListComplianceParameter, AddressKeyListComplianceParameter, PortfolioIdListComplianceParameter, PortfolioGroupIdListComplianceParameter, InstrumentListComplianceParameter, FilterPredicateComplianceParameter, GroupFilterPredicateComplianceParameter, GroupBySelectorComplianceParameter, PropertyListComplianceParameter, GroupCalculationComplianceParameter.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

