# TransactionPayload

record containing the payload for a single transaction. Columns is compiled once from the TPF instance configuration and is identical across every item in the paginated result. PublicationStatus is the row's outcome: Sent, or Failed when the file holding it reached no destination.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **transaction_id** | **str** | Required | *No description available.* |
| **columns** | **List[str]** | Required | *No description available.* |
| **values** | **Dict[str, str]** | Required | *No description available.* |
| **raw_csv_row** | **str** | Required | *No description available.* |
| **publication_status** | **str** | Required | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.horizon.models.TransactionPayload import TransactionPayload

instance = TransactionPayload(
    transaction_id="...",  # required
    columns=,  # required
    values=,  # required
    raw_csv_row="...",  # required
    publication_status="..."  # required
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

