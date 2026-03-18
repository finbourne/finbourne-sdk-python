# CorporateAction

A corporate action
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **corporate_action_code** | **str** | Required | The unique identifier of this corporate action |
| **description** | **str** | Optional | The description of the corporate action. |
| **announcement_date** | **datetime** | Optional | The announcement date of the corporate action |
| **ex_date** | **datetime** | Optional | The ex date of the corporate action |
| **record_date** | **datetime** | Optional | The record date of the corporate action |
| **payment_date** | **datetime** | Optional | The payment date of the corporate action |
| **transitions** | [List[CorporateActionTransition]](CorporateActionTransition.md) | Optional | The transitions that result from this corporate action |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.CorporateAction import CorporateAction

instance = CorporateAction(
    corporate_action_code="...",  # required — The unique identifier of this corporate action
    description="...",  # optional — The description of the corporate action.
    announcement_date=datetime.now(),  # optional — The announcement date of the corporate action
    ex_date=datetime.now(),  # optional — The ex date of the corporate action
    record_date=datetime.now(),  # optional — The record date of the corporate action
    payment_date=datetime.now(),  # optional — The payment date of the corporate action
    transitions=[]  # optional — The transitions that result from this corporate action
)
```

- [CorporateActionTransition](CorporateActionTransition.md) — used in `transitions`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

