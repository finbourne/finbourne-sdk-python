# AuditFileDetails

Holds information about Horizon Audit Files
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **file_type** | **str** | Required | The type of the audit file |
| **file_path_and_name** | **str** | Required | The file path and name |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.horizon.models.AuditFileDetails import AuditFileDetails

instance = AuditFileDetails(
    file_type="...",  # required — The type of the audit file
    file_path_and_name="..."  # required — The file path and name
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

