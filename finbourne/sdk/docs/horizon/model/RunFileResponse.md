# RunFileResponse

record containing details of a single file for a run.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **file_name** | **str** | Required | *No description available.* |
| **generated_at** | **datetime** | Required | *No description available.* |
| **row_count** | **int** | Required | *No description available.* |
| **file_hash** | **str** | Required | *No description available.* |
| **encrypted** | **bool** | Required | *No description available.* |
| **destinations** | [List[FileDestinationResponse]](FileDestinationResponse.md) | Required | *No description available.* |
| **transaction_ids** | **List[UUID]** | Required | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.horizon.models.RunFileResponse import RunFileResponse

instance = RunFileResponse(
    file_name="...",  # required
    generated_at=datetime.now(),  # required
    row_count=0,  # required
    file_hash="...",  # required
    encrypted=True,  # required
    destinations=[],  # required
    transaction_ids=  # required
)
```

- [FileDestinationResponse](FileDestinationResponse.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

