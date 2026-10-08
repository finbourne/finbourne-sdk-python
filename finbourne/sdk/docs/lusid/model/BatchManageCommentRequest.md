# BatchManageCommentRequest

One item of a batch comment request. The operation (add/edit/delete) is inferred from the  combination of commentId and commentText.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **instance_id** | [RecInstanceId](RecInstanceId.md) | Required | *No description available.* |
| **rec_type** | **str** | Required | The rec type whose results this item targets (e.g. Holding). Available values: Holding, CashHolding, Valuation, InputTransaction, OutputTransaction, SettlementActivity. |
| **run_number** | **int** | Required | The run of the instance whose results this item targets. |
| **rec_result_id** | **str** | Required | The rec result the comment operation targets. |
| **comment_id** | **str** | Optional | The comment id. Null with text &#x3D; add; provided with text &#x3D; edit; provided with null text &#x3D; delete. |
| **comment_text** | **str** | Optional | The comment body. See operation inference. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.BatchManageCommentRequest import BatchManageCommentRequest

instance = BatchManageCommentRequest(
    instance_id=RecInstanceId(...),  # required
    rec_type="...",  # required — The rec type whose results this item targets (e.g. Holding). Available values: Holding, CashHolding, Valuation, InputTransaction, OutputTransaction, SettlementActivity.
    run_number=0,  # required — The run of the instance whose results this item targets.
    rec_result_id="...",  # required — The rec result the comment operation targets.
    comment_id="...",  # optional — The comment id. Null with text &#x3D; add; provided with text &#x3D; edit; provided with null text &#x3D; delete.
    comment_text="..."  # optional — The comment body. See operation inference.
)
```


## Related Models

- [RecInstanceId](RecInstanceId.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

