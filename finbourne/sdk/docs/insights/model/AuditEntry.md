# AuditEntry

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **id** | **str** | Required | *No description available.* |
| **var_date** | **datetime** | Required | *No description available.* |
| **process** | [AuditProcess](AuditProcess.md) | Required | *No description available.* |
| **data** | [AuditData](AuditData.md) | Required | *No description available.* |
| **notes** | [List[AuditEntryNote]](AuditEntryNote.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.insights.models.AuditEntry import AuditEntry

instance = AuditEntry(
    id="...",  # required
    var_date=datetime.now(),  # required
    process=AuditProcess(...),  # required
    data=AuditData(...),  # required
    notes=[]  # optional
)
```

- [AuditProcess](AuditProcess.md)
- [AuditData](AuditData.md)
- [AuditEntryNote](AuditEntryNote.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

