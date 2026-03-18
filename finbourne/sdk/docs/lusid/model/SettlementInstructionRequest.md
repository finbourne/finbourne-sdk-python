# SettlementInstructionRequest

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **settlement_instruction_id** | **str** | Required | *No description available.* |
| **transaction_id** | **str** | Required | *No description available.* |
| **settlement_category** | **str** | Required | *No description available.* |
| **instruction_type** | **str** | Optional | *No description available.* |
| **instrument_identifiers** | **Dict[str, Optional[str]]** | Required | *No description available.* |
| **contractual_settlement_date** | **datetime** | Optional | *No description available.* |
| **actual_settlement_date** | **datetime** | Required | *No description available.* |
| **units** | **float** | Required | *No description available.* |
| **sub_holding_key_overrides** | [Dict[str, PerpetualProperty]](PerpetualProperty.md) | Optional | *No description available.* |
| **custodian_account_override** | [ResourceId](ResourceId.md) | Optional | *No description available.* |
| **instruction_to_portfolio_rate** | **float** | Optional | *No description available.* |
| **settlement_in_lieu** | [SettlementInLieu](SettlementInLieu.md) | Optional | *No description available.* |
| **properties** | [List[PerpetualProperty]](PerpetualProperty.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.SettlementInstructionRequest import SettlementInstructionRequest

instance = SettlementInstructionRequest(
    settlement_instruction_id="...",  # required
    transaction_id="...",  # required
    settlement_category="...",  # required
    instruction_type="...",  # optional
    instrument_identifiers=,  # required
    contractual_settlement_date=datetime.now(),  # optional
    actual_settlement_date=datetime.now(),  # required
    units=0.0,  # required
    sub_holding_key_overrides=PerpetualProperty(...),  # optional
    custodian_account_override=ResourceId(...),  # optional
    instruction_to_portfolio_rate=0.0,  # optional
    settlement_in_lieu=SettlementInLieu(...),  # optional
    properties=[]  # optional
)
```

- [PerpetualProperty](PerpetualProperty.md)
- [ResourceId](ResourceId.md)
- [SettlementInLieu](SettlementInLieu.md)
- [PerpetualProperty](PerpetualProperty.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

