# ComplianceRuleV3GroupResult

The result of one rule for a single evaluated group: its status, the group key identifying it, the  measured value, the unit the value and limits are expressed in, the limits it was checked against, the  portfolios and orders it affects, and, when it could not be assessed, the missing-data details.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **status** | **str** | Optional | Available values: Passed, Failed, Warning, MissingData. |
| **group_key** | **str** | Optional | *No description available.* |
| **measured_value** | **float** | Optional | *No description available.* |
| **hard_limit** | **float** | Optional | *No description available.* |
| **soft_limit** | **float** | Optional | *No description available.* |
| **unit** | **str** | Optional | Available values: Absolute, Percentage. |
| **affected_portfolio_ids** | **List[str]** | Optional | *No description available.* |
| **affected_order_ids** | **List[str]** | Optional | *No description available.* |
| **missing_data_details** | **List[str]** | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.ComplianceRuleV3GroupResult import ComplianceRuleV3GroupResult

instance = ComplianceRuleV3GroupResult(
    status="...",  # optional — Available values: Passed, Failed, Warning, MissingData.
    group_key="...",  # optional
    measured_value=0.0,  # optional
    hard_limit=0.0,  # optional
    soft_limit=0.0,  # optional
    unit="...",  # optional — Available values: Absolute, Percentage.
    affected_portfolio_ids=,  # optional
    affected_order_ids=,  # optional
    missing_data_details=  # optional
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

