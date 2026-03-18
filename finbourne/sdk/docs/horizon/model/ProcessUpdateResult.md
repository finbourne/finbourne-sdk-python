# ProcessUpdateResult

Shows details relevant to update events for a query
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **domain** | **str** | Required |  |
| **entry_id** | **str** | Required |  |
| **process_name** | **str** | Required |  |
| **run_id** | **str** | Required |  |
| **entry_date** | **datetime** | Required |  |
| **status** | **str** | Required |  |
| **message** | **str** | Required |  |
| **schema_version** | **str** | Optional |  |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.horizon.models.ProcessUpdateResult import ProcessUpdateResult

instance = ProcessUpdateResult(
    domain="...",  # required — 
    entry_id="...",  # required — 
    process_name="...",  # required — 
    run_id="...",  # required — 
    entry_date=datetime.now(),  # required — 
    status="...",  # required — 
    message="...",  # required — 
    schema_version="..."  # optional — 
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

