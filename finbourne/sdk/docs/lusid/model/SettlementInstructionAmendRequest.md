# SettlementInstructionAmendRequest

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **settlement_instruction_id** | **str** | Required | *No description available.* |
| **operation** | **str** | Optional | *No description available.* |
| **properties** | [List[PerpetualProperty]](PerpetualProperty.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.SettlementInstructionAmendRequest import SettlementInstructionAmendRequest

instance = SettlementInstructionAmendRequest(
    settlement_instruction_id="...",  # required
    operation="...",  # optional
    properties=[]  # optional
)
```

- [PerpetualProperty](PerpetualProperty.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

