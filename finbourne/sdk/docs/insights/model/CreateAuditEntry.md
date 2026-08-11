# CreateAuditEntry

Details to create an audit entry
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **process** | [AuditProcess](AuditProcess.md) | Required | *No description available.* |
| **data** | [AuditData](AuditData.md) | Required | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.insights.models.CreateAuditEntry import CreateAuditEntry

instance = CreateAuditEntry(
    process=AuditProcess(...),  # required
    data=AuditData(...)  # required
)
```


## Related Models

- [AuditProcess](AuditProcess.md)
- [AuditData](AuditData.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

