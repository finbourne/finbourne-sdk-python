# SettlementInstructionQuery

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **as_at** | **datetime** | Optional | *No description available.* |
| **start_date** | **str** | Optional | *No description available.* |
| **end_date** | **str** | Optional | *No description available.* |
| **limit** | **int** | Optional | *No description available.* |
| **page** | **str** | Optional | *No description available.* |
| **filter** | **str** | Optional | *No description available.* |
| **settlement_instruction_property_keys** | **List[str]** | Optional | *No description available.* |
| **transaction_property_keys** | **List[str]** | Optional | *No description available.* |
| **timeline_scope** | **str** | Optional | *No description available.* |
| **timeline_code** | **str** | Optional | *No description available.* |
| **closed_period_id** | **str** | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.SettlementInstructionQuery import SettlementInstructionQuery

instance = SettlementInstructionQuery(
    as_at=datetime.now(),  # optional
    start_date="...",  # optional
    end_date="...",  # optional
    limit=0,  # optional
    page="...",  # optional
    filter="...",  # optional
    settlement_instruction_property_keys=,  # optional
    transaction_property_keys=,  # optional
    timeline_scope="...",  # optional
    timeline_code="...",  # optional
    closed_period_id="..."  # optional
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

