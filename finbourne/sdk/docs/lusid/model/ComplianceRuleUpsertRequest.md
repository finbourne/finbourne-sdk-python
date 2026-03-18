# ComplianceRuleUpsertRequest

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **scope** | **str** | Required |  |
| **code** | **str** | Optional |  |
| **display_name** | **str** | Optional |  |
| **type** | **str** | Required |  |
| **property_key** | **str** | Optional |  |
| **value** | **str** | Optional |  |
| **lower_bound** | **float** | Required |  |
| **upper_bound** | **float** | Required |  |
| **schedule** | **str** | Required |  |
| **hard_requirement** | **bool** | Required |  |
| **target_portfolio_ids** | [List[ResourceId]](ResourceId.md) | Required |  |
| **description** | **str** | Optional |  |
| **address_key** | **str** | Optional |  |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.ComplianceRuleUpsertRequest import ComplianceRuleUpsertRequest

instance = ComplianceRuleUpsertRequest(
    scope="...",  # required — 
    code="...",  # optional — 
    display_name="...",  # optional — 
    type="...",  # required — 
    property_key="...",  # optional — 
    value="...",  # optional — 
    lower_bound=0.0,  # required — 
    upper_bound=0.0,  # required — 
    schedule="...",  # required — 
    hard_requirement=True,  # required — 
    target_portfolio_ids=[],  # required — 
    description="...",  # optional — 
    address_key="..."  # optional — 
)
```

- [ResourceId](ResourceId.md) — used in `target_portfolio_ids`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

