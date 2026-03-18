# RowDetails

Information about the nuber of rows processed.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **rows_total** | **int** | Optional | The number of rows processed. |
| **rows_succeeded** | **int** | Optional | The number of rows that were successfully processed. |
| **rows_ignored** | **int** | Optional | The number of rows that were not processed. |
| **rows_failed** | **int** | Optional | The number of rows that failed when being processed. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.horizon.models.RowDetails import RowDetails

instance = RowDetails(
    rows_total=0,  # optional — The number of rows processed.
    rows_succeeded=0,  # optional — The number of rows that were successfully processed.
    rows_ignored=0,  # optional — The number of rows that were not processed.
    rows_failed=0  # optional — The number of rows that failed when being processed.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

