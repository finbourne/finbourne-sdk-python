# IIntegrationLogResponse

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **log_id** | **int** | Required | *No description available.* *(read-only)* |
| **run_id** | **UUID** | Optional | *No description available.* *(read-only)* |
| **parent_log_id** | **int** | Optional | *No description available.* *(read-only)* |
| **log_type** | **str** | Required | *No description available.* *(read-only)* |
| **first_activity** | **datetime** | Optional | *No description available.* *(read-only)* |
| **last_activity** | **datetime** | Optional | *No description available.* *(read-only)* |
| **status** | **str** | Optional | *No description available.* *(read-only)* |
| **source_record** | [IntegrationLogRecord](IntegrationLogRecord.md) | Optional | *No description available.* |
| **target_record** | [IntegrationLogTargetRecord](IntegrationLogTargetRecord.md) | Optional | *No description available.* |
| **activities** | [List[IntegrationLogActivity]](IntegrationLogActivity.md) | Required | *No description available.* *(read-only)* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.horizon.models.IIntegrationLogResponse import IIntegrationLogResponse

instance = IIntegrationLogResponse(
    log_id=0,  # required
    run_id="...",  # optional
    parent_log_id=0,  # optional
    log_type="...",  # required
    first_activity=datetime.now(),  # optional
    last_activity=datetime.now(),  # optional
    status="...",  # optional
    source_record=IntegrationLogRecord(...),  # optional
    target_record=IntegrationLogTargetRecord(...),  # optional
    activities=[]  # required
)
```

- [IntegrationLogRecord](IntegrationLogRecord.md)
- [IntegrationLogTargetRecord](IntegrationLogTargetRecord.md)
- [IntegrationLogActivity](IntegrationLogActivity.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

