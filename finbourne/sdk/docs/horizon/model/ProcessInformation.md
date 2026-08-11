# ProcessInformation

Required information for each process
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **domain** | **str** | Required |  |
| **process_name** | **str** | Required |  |
| **run_id** | **str** | Required |  |
| **start_time** | **datetime** | Required |  |
| **data_action** | **str** | Required |  |
| **schema_version** | **str** | Optional |  |
| **user_id** | **str** | Required |  |
| **process_summary** | [ProcessSummary](ProcessSummary.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.horizon.models.ProcessInformation import ProcessInformation

instance = ProcessInformation(
    domain="...",  # required — 
    process_name="...",  # required — 
    run_id="...",  # required — 
    start_time=datetime.now(),  # required — 
    data_action="...",  # required — 
    schema_version="...",  # optional — 
    user_id="...",  # required — 
    process_summary=ProcessSummary(...)  # optional
)
```

- [ProcessSummary](ProcessSummary.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

