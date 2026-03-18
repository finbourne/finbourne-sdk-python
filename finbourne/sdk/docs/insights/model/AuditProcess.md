# AuditProcess

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **name** | **str** | Required | *No description available.* |
| **run_id** | **str** | Required | *No description available.* |
| **start_time** | **datetime** | Required | *No description available.* |
| **end_time** | **datetime** | Optional | *No description available.* |
| **succeeded** | **bool** | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.insights.models.AuditProcess import AuditProcess

instance = AuditProcess(
    name="...",  # required
    run_id="...",  # required
    start_time=datetime.now(),  # required
    end_time=datetime.now(),  # optional
    succeeded=True  # optional
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

