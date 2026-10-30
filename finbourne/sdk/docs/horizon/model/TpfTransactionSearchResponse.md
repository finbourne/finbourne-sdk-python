# TpfTransactionSearchResponse

TPF send history record
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **transaction_id** | **str** | Required | Transaction identifier |
| **instance_id** | **UUID** | Required | Integration instance ID where the transaction was processed |
| **instance_name** | **str** | Required | Integration instance name |
| **batch_id** | **UUID** | Required | Unique identifier of the batch |
| **run_id** | **UUID** | Required | The run that processed the transaction for this instance, as shown in run monitoring |
| **run_start_time** | **datetime** | Required | Timestamp when the batch/run started |
| **publication_status** | **str** | Required | Publication status of the transaction (Sent | Skipped | Failed) |
| **instrument_name** | **str** | Required | Instrument name |
| **instrument_type** | **str** | Required | Instrument type |
| **trade_date** | **datetime** | Required | Trade date of the transaction |
| **settlement_date** | **datetime** | Optional | Settlement date of the transaction |
| **skip_reason** | **str** | Optional | Reason the transaction was skipped (if applicable) |
| **file_name** | **str** | Optional | Output file associated with the publication run |
| **destinations** | **List[str]** | Optional | Destinations to which the transaction was published |
| **portfolio_code** | **str** | Optional | PortfolioCode showing portfolio code |
| **portfolio_scope** | **str** | Optional | PortfolioScope displaying portfolio scope |
| **failure_reason** | **str** | Optional | FailureReason to show failure reason |
| **failure_stage** | **str** | Optional | Stage at which a failed transaction failed: Build or Delivery |
| **sent_at** | **datetime** | Optional | When the transaction was sent, which is when its file reached a destination. Empty for Skipped and Failed rows |
| **instrument_id** | **str** | Optional | InstrumentId showing instrument id of transaction |
| **instrument_scope** | **str** | Optional | The scope the build resolved the instrument in; null for rows built before it was recorded |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.horizon.models.TpfTransactionSearchResponse import TpfTransactionSearchResponse

instance = TpfTransactionSearchResponse(
    transaction_id="...",  # required — Transaction identifier
    instance_id="...",  # required — Integration instance ID where the transaction was processed
    instance_name="...",  # required — Integration instance name
    batch_id="...",  # required — Unique identifier of the batch
    run_id="...",  # required — The run that processed the transaction for this instance, as shown in run monitoring
    run_start_time=datetime.now(),  # required — Timestamp when the batch/run started
    publication_status="...",  # required — Publication status of the transaction (Sent | Skipped | Failed)
    instrument_name="...",  # required — Instrument name
    instrument_type="...",  # required — Instrument type
    trade_date=datetime.now(),  # required — Trade date of the transaction
    settlement_date=datetime.now(),  # optional — Settlement date of the transaction
    skip_reason="...",  # optional — Reason the transaction was skipped (if applicable)
    file_name="...",  # optional — Output file associated with the publication run
    destinations=,  # optional — Destinations to which the transaction was published
    portfolio_code="...",  # optional — PortfolioCode showing portfolio code
    portfolio_scope="...",  # optional — PortfolioScope displaying portfolio scope
    failure_reason="...",  # optional — FailureReason to show failure reason
    failure_stage="...",  # optional — Stage at which a failed transaction failed: Build or Delivery
    sent_at=datetime.now(),  # optional — When the transaction was sent, which is when its file reached a destination. Empty for Skipped and Failed rows
    instrument_id="...",  # optional — InstrumentId showing instrument id of transaction
    instrument_scope="..."  # optional — The scope the build resolved the instrument in; null for rows built before it was recorded
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

