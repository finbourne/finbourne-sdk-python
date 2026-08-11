# ProcessSummary

Completed event details
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **end_time** | **datetime** | Optional |  |
| **category** | **str** | Optional |  |
| **status** | **str** | Required |  |
| **message** | **str** | Required |  |
| **rows** | [RowDetails](RowDetails.md) | Required | *No description available.* |
| **file_details** | [List[FileDetails]](FileDetails.md) | Optional |  |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.horizon.models.ProcessSummary import ProcessSummary

instance = ProcessSummary(
    end_time=datetime.now(),  # optional — 
    category="...",  # optional — 
    status="...",  # required — 
    message="...",  # required — 
    rows=RowDetails(...),  # required
    file_details=[]  # optional — 
)
```

- [RowDetails](RowDetails.md)
- [FileDetails](FileDetails.md) — used in `file_details`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

