# ComplianceRule

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **scope** | **str** | Required |  |
| **code** | **str** | Required |  |
| **display_name** | **str** | Required |  |
| **type** | **str** | Required | Available values: RangeNumberSecurities, RangePercentSecurityType, RangePercentCash, RangePercentPropertyKey. |
| **property_key** | **str** | Optional |  |
| **value** | **str** | Optional |  |
| **address_key** | **str** | Optional |  |
| **lower_bound** | **float** | Required |  |
| **upper_bound** | **float** | Required |  |
| **schedule** | **str** | Required | Available values: PreTrade, PostTrade, PreAndPostTrade. |
| **hard_requirement** | **bool** | Required |  |
| **target_portfolio_ids** | [List[ResourceId]](ResourceId.md) | Required |  |
| **description** | **str** | Optional |  |
| **version** | [Version](Version.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.ComplianceRule import ComplianceRule

instance = ComplianceRule(
    scope="...",  # required — 
    code="...",  # required — 
    display_name="...",  # required — 
    type="...",  # required — Available values: RangeNumberSecurities, RangePercentSecurityType, RangePercentCash, RangePercentPropertyKey.
    property_key="...",  # optional — 
    value="...",  # optional — 
    address_key="...",  # optional — 
    lower_bound=0.0,  # required — 
    upper_bound=0.0,  # required — 
    schedule="...",  # required — Available values: PreTrade, PostTrade, PreAndPostTrade.
    hard_requirement=True,  # required — 
    target_portfolio_ids=[],  # required — 
    description="...",  # optional — 
    version=Version(...)  # optional
)
```

- [ResourceId](ResourceId.md) — used in `target_portfolio_ids`
- [Version](Version.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

