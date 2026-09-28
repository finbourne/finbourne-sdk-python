# TransactionResponse

Response containing details of a single transaction for a run.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **transaction_id** | **str** | Required | *No description available.* |
| **publication_status** | **str** | Required | *No description available.* |
| **portfolio_scope** | **str** | Optional | *No description available.* |
| **portfolio_code** | **str** | Optional | *No description available.* |
| **instrument_id** | **str** | Optional | *No description available.* |
| **instrument_type** | **str** | Optional | *No description available.* |
| **instrument_name** | **str** | Optional | *No description available.* |
| **trade_date** | **datetime** | Optional | *No description available.* |
| **settlement_date** | **datetime** | Optional | *No description available.* |
| **status** | **str** | Required | *No description available.* |
| **skip_reason** | **str** | Optional | *No description available.* |
| **failure_reason** | **str** | Optional | *No description available.* |
| **output_file_name** | **str** | Optional | *No description available.* |
| **sent_at** | **datetime** | Optional | *No description available.* |
| **destinations** | [List[DestinationResponse]](DestinationResponse.md) | Required | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.horizon.models.TransactionResponse import TransactionResponse

instance = TransactionResponse(
    transaction_id="...",  # required
    publication_status="...",  # required
    portfolio_scope="...",  # optional
    portfolio_code="...",  # optional
    instrument_id="...",  # optional
    instrument_type="...",  # optional
    instrument_name="...",  # optional
    trade_date=datetime.now(),  # optional
    settlement_date=datetime.now(),  # optional
    status="...",  # required
    skip_reason="...",  # optional
    failure_reason="...",  # optional
    output_file_name="...",  # optional
    sent_at=datetime.now(),  # optional
    destinations=[]  # required
)
```

- [DestinationResponse](DestinationResponse.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

