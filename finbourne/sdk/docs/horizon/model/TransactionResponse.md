# TransactionResponse

Response containing details of a single transaction for a run. A transaction built twice in one batch appears once per build. FailureStage says whether a failed transaction failed while being built (Build) or while its file was being delivered (Delivery).
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **transaction_id** | **str** | Required | *No description available.* |
| **publication_status** | **str** | Required | The outcome the screens show for this row: Sent, Skipped or Failed. |
| **portfolio_scope** | **str** | Optional | *No description available.* |
| **portfolio_code** | **str** | Optional | *No description available.* |
| **instrument_id** | **str** | Optional | *No description available.* |
| **instrument_type** | **str** | Optional | *No description available.* |
| **instrument_name** | **str** | Optional | *No description available.* |
| **trade_date** | **datetime** | Optional | *No description available.* |
| **settlement_date** | **datetime** | Optional | *No description available.* |
| **status** | **str** | Required | The batch element&#39;s processing state as the worker left it, not the outcome; read PublicationStatus for that. |
| **skip_reason** | **str** | Optional | *No description available.* |
| **failure_reason** | **str** | Optional | *No description available.* |
| **output_file_name** | **str** | Optional | *No description available.* |
| **sent_at** | **datetime** | Optional | *No description available.* |
| **destinations** | [List[DestinationResponse]](DestinationResponse.md) | Required | *No description available.* |
| **failure_stage** | **str** | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.horizon.models.TransactionResponse import TransactionResponse

instance = TransactionResponse(
    transaction_id="...",  # required
    publication_status="...",  # required — The outcome the screens show for this row: Sent, Skipped or Failed.
    portfolio_scope="...",  # optional
    portfolio_code="...",  # optional
    instrument_id="...",  # optional
    instrument_type="...",  # optional
    instrument_name="...",  # optional
    trade_date=datetime.now(),  # optional
    settlement_date=datetime.now(),  # optional
    status="...",  # required — The batch element&#39;s processing state as the worker left it, not the outcome; read PublicationStatus for that.
    skip_reason="...",  # optional
    failure_reason="...",  # optional
    output_file_name="...",  # optional
    sent_at=datetime.now(),  # optional
    destinations=[],  # required
    failure_stage="..."  # optional
)
```

- [DestinationResponse](DestinationResponse.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

