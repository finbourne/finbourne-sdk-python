# AuditProcessSummary

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **process** | [AuditProcess](AuditProcess.md) | Optional | *No description available.* |
| **latest_entry** | [AuditData](AuditData.md) | Optional | *No description available.* |
| **summary** | [AuditDataSummary](AuditDataSummary.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.insights.models.AuditProcessSummary import AuditProcessSummary

instance = AuditProcessSummary(
    process=AuditProcess(...),  # optional
    latest_entry=AuditData(...),  # optional
    summary=AuditDataSummary(...)  # optional
)
```


## Related Models

- [AuditProcess](AuditProcess.md)
- [AuditData](AuditData.md)
- [AuditDataSummary](AuditDataSummary.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

