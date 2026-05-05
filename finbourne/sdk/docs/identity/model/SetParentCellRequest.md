# SetParentCellRequest

Request body for setting the parent cell.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **admin_domain_name** | **str** | Required | The name of the admin domain in the parent cell. |
| **confirm** | **bool** | Required | Whether to confirm the parent cell attachment (second invocation). First call with false creates a Proposed state; second call with true transitions to Attaching. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.identity.models.SetParentCellRequest import SetParentCellRequest

instance = SetParentCellRequest(
    admin_domain_name="...",  # required — The name of the admin domain in the parent cell.
    confirm=True  # required — Whether to confirm the parent cell attachment (second invocation). First call with false creates a Proposed state; second call with true transitions to Attaching.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

