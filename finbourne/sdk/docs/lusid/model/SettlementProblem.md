# SettlementProblem

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **settlement_instruction_id** | **str** | Required | The id of the problematic settlement instruction. Combined with the portfolio id this uniquely identifies a settlement instruction |
| **category** | **str** | Required | The category this instruction belongs to |
| **status** | **str** | Required | The status of the settlement instruction. Possible values are &#39;Invalid&#39; or &#39;Rejected&#39;. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.SettlementProblem import SettlementProblem

instance = SettlementProblem(
    settlement_instruction_id="...",  # required — The id of the problematic settlement instruction. Combined with the portfolio id this uniquely identifies a settlement instruction
    category="...",  # required — The category this instruction belongs to
    status="..."  # required — The status of the settlement instruction. Possible values are &#39;Invalid&#39; or &#39;Rejected&#39;.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

