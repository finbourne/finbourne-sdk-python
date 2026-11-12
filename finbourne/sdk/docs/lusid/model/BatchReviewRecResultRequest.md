# BatchReviewRecResultRequest

One item of a batch review request: applies review content to its targeted rec result(s). Exactly  one target, except FixAsGroup/ForceMatch which require two or more. A result id is unique within one  instance. Every item names the rec type of its targets, so a group decision covers results of one rec type  only.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **instance_id** | [RecInstanceId](RecInstanceId.md) | Required | *No description available.* |
| **rec_type** | **str** | Required | The rec type whose results this item targets (e.g. Holding). Available values: Holding, CashHolding, Valuation, InputTransaction, OutputTransaction, SettlementActivity, External, Instrument, LegalEntity, Portfolio. |
| **rec_result_ids** | **List[str]** | Required | The rec results targeted by this batch item. Exactly one, except FixAsGroup/ForceMatch which require two or more. |
| **decision** | [RecResultDecisionUpdate](RecResultDecisionUpdate.md) | Optional | *No description available.* |
| **assigned_user** | [RecResultAssignmentUpdate](RecResultAssignmentUpdate.md) | Optional | *No description available.* |
| **assigned_role** | [RecResultAssignmentUpdate](RecResultAssignmentUpdate.md) | Optional | *No description available.* |
| **add_comment_text** | **str** | Optional | Optional comment text to add to each targeted result. |
| **properties** | [List[PerpetualProperty]](PerpetualProperty.md) | Optional | Properties in the RecResult domain to set on each result. A property with a null value is deleted and omitted properties are left unchanged. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.BatchReviewRecResultRequest import BatchReviewRecResultRequest

instance = BatchReviewRecResultRequest(
    instance_id=RecInstanceId(...),  # required
    rec_type="...",  # required — The rec type whose results this item targets (e.g. Holding). Available values: Holding, CashHolding, Valuation, InputTransaction, OutputTransaction, SettlementActivity, External, Instrument, LegalEntity, Portfolio.
    rec_result_ids=,  # required — The rec results targeted by this batch item. Exactly one, except FixAsGroup/ForceMatch which require two or more.
    decision=RecResultDecisionUpdate(...),  # optional
    assigned_user=RecResultAssignmentUpdate(...),  # optional
    assigned_role=RecResultAssignmentUpdate(...),  # optional
    add_comment_text="...",  # optional — Optional comment text to add to each targeted result.
    properties=[]  # optional — Properties in the RecResult domain to set on each result. A property with a null value is deleted and omitted properties are left unchanged.
)
```


## Related Models

- [RecInstanceId](RecInstanceId.md)
- [RecResultDecisionUpdate](RecResultDecisionUpdate.md)
- [RecResultAssignmentUpdate](RecResultAssignmentUpdate.md)
- [RecResultAssignmentUpdate](RecResultAssignmentUpdate.md)
- [PerpetualProperty](PerpetualProperty.md) — used in `properties`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

