# CategorySettlementStatus

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **status** | **str** | Required | The Status of the settlement category - &#39;Settled&#39;, &#39;Part Settled&#39; or &#39;Unsettled&#39;. |
| **is_overdue** | **bool** | Required | Whether the category has any overdue movements |
| **problems** | [List[SettlementProblem]](SettlementProblem.md) | Required | Instruction level detail of rejected or invalid settlement instructions |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.CategorySettlementStatus import CategorySettlementStatus

instance = CategorySettlementStatus(
    status="...",  # required — The Status of the settlement category - &#39;Settled&#39;, &#39;Part Settled&#39; or &#39;Unsettled&#39;.
    is_overdue=True,  # required — Whether the category has any overdue movements
    problems=[]  # required — Instruction level detail of rejected or invalid settlement instructions
)
```

- [SettlementProblem](SettlementProblem.md) — used in `problems`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

