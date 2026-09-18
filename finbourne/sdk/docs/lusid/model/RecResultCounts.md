# RecResultCounts

Counts of results broken down by the structural categories that align with the review configuration.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **total** | **int** | Required | The total number of results in this result set, across all categories. |
| **open_exceptions** | [RecOpenExceptionCounts](RecOpenExceptionCounts.md) | Required | *No description available.* |
| **closed_exceptions** | [RecClosedExceptionCounts](RecClosedExceptionCounts.md) | Required | *No description available.* |
| **matches** | [RecMatchCounts](RecMatchCounts.md) | Required | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.RecResultCounts import RecResultCounts

instance = RecResultCounts(
    total=0,  # required — The total number of results in this result set, across all categories.
    open_exceptions=RecOpenExceptionCounts(...),  # required
    closed_exceptions=RecClosedExceptionCounts(...),  # required
    matches=RecMatchCounts(...)  # required
)
```

- [RecOpenExceptionCounts](RecOpenExceptionCounts.md)
- [RecClosedExceptionCounts](RecClosedExceptionCounts.md)
- [RecMatchCounts](RecMatchCounts.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

