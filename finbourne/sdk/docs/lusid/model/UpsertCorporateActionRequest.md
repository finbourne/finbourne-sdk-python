# UpsertCorporateActionRequest

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **corporate_action_code** | **str** | Required | The unique identifier of this corporate action |
| **description** | **str** | Optional | The description of the corporate action. |
| **announcement_date** | **datetime** | Required | The announcement date of the corporate action |
| **ex_date** | **datetime** | Required | The ex date of the corporate action |
| **record_date** | **datetime** | Required | The record date of the corporate action |
| **payment_date** | **datetime** | Required | The payment date of the corporate action |
| **transitions** | [List[CorporateActionTransitionRequest]](CorporateActionTransitionRequest.md) | Required | The transitions that result from this corporate action |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.UpsertCorporateActionRequest import UpsertCorporateActionRequest

instance = UpsertCorporateActionRequest(
    corporate_action_code="...",  # required — The unique identifier of this corporate action
    description="...",  # optional — The description of the corporate action.
    announcement_date=datetime.now(),  # required — The announcement date of the corporate action
    ex_date=datetime.now(),  # required — The ex date of the corporate action
    record_date=datetime.now(),  # required — The record date of the corporate action
    payment_date=datetime.now(),  # required — The payment date of the corporate action
    transitions=[]  # required — The transitions that result from this corporate action
)
```

- [CorporateActionTransitionRequest](CorporateActionTransitionRequest.md) — used in `transitions`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

