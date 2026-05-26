# TransactionPayloadResponse

record containing details of a transaction payload.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **columns** | **List[str]** | Required | *No description available.* |
| **values** | **Dict[str, str]** | Required | *No description available.* |
| **raw_csv_row** | **str** | Required | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.horizon.models.TransactionPayloadResponse import TransactionPayloadResponse

instance = TransactionPayloadResponse(
    columns=,  # required
    values=,  # required
    raw_csv_row="..."  # required
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

