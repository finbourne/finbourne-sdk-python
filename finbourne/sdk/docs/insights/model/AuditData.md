# AuditData

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **action** | **str** | Required | *No description available.* |
| **category** | **str** | Required | *No description available.* |
| **user_id** | **str** | Optional | *No description available.* |
| **message** | **str** | Optional | *No description available.* |
| **resource** | [Resource](Resource.md) | Optional | *No description available.* |
| **details_type** | **str** | Optional | *No description available.* |
| **details** | **object** | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.insights.models.AuditData import AuditData

instance = AuditData(
    action="...",  # required
    category="...",  # required
    user_id="...",  # optional
    message="...",  # optional
    resource=Resource(...),  # optional
    details_type="...",  # optional
    details=  # optional
)
```

- [Resource](Resource.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

