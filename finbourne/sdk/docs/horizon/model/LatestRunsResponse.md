# LatestRunsResponse

record containing the 24-hour run summary grouped by external status.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **total** | **int** | Required | *No description available.* |
| **status_counts** | [List[RunStatusCount]](RunStatusCount.md) | Required | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.horizon.models.LatestRunsResponse import LatestRunsResponse

instance = LatestRunsResponse(
    total=0,  # required
    status_counts=[]  # required
)
```

- [RunStatusCount](RunStatusCount.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

