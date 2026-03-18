# AuditEntryNote

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **user_id** | **str** | Required | *No description available.* |
| **text** | **str** | Required | *No description available.* |
| **var_date** | **datetime** | Required | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.insights.models.AuditEntryNote import AuditEntryNote

instance = AuditEntryNote(
    user_id="...",  # required
    text="...",  # required
    var_date=datetime.now()  # required
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

