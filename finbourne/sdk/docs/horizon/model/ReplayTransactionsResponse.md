# ReplayTransactionsResponse

Response from a replay transactions operation containing the CSV output.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **batch_reference_id** | **str** | Required | *No description available.* |
| **mode** | **str** | Required | *No description available.* |
| **transaction_count** | **int** | Required | *No description available.* |
| **csv_output** | **str** | Required | *No description available.* |
| **message** | **str** | Required | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.horizon.models.ReplayTransactionsResponse import ReplayTransactionsResponse

instance = ReplayTransactionsResponse(
    batch_reference_id="...",  # required
    mode="...",  # required
    transaction_count=0,  # required
    csv_output="...",  # required
    message="..."  # required
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

