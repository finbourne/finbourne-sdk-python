# TpfTransactionSearchResponse

TPF send history record
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **transaction_id** | **str** | Required | Transaction identifier |
| **instance_id** | **UUID** | Required | Integration instance ID where the transaction was processed |
| **instance_name** | **str** | Required | Integration instance name |
| **batch_id** | **UUID** | Required | Unique identifier of the batch |
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
| **instrument_id** | **str** | Optional | InstrumentId showing instrument id of transaction |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.horizon.models.TpfTransactionSearchResponse import TpfTransactionSearchResponse

instance = TpfTransactionSearchResponse(
    transaction_id="...",  # required — Transaction identifier
    instance_id="...",  # required — Integration instance ID where the transaction was processed
    instance_name="...",  # required — Integration instance name
    batch_id="...",  # required — Unique identifier of the batch
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
    instrument_id="..."  # optional — InstrumentId showing instrument id of transaction
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

