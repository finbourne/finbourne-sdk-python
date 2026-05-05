# CellParentStatusResponse

Response containing the current cell parent status.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **status** | **str** | Optional | The current attachment status of the cell. |
| **admin_domain_name** | **str** | Optional | The name of the admin domain in the parent cell, if any. |
| **primary_domain_name** | **str** | Optional | The domain designated as the primary domain for this cell, if any. |
| **registration_step** | **str** | Optional | The most recently reached registration checkpoint, or null if no registration has started. One of &#x60;UserEnsured&#x60;, &#x60;PATGenerated&#x60;, &#x60;PATPushed&#x60;. |
| **registration_error** | **str** | Optional | Operator-readable message describing the most recent registration failure, or null on success. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.identity.models.CellParentStatusResponse import CellParentStatusResponse

instance = CellParentStatusResponse(
    status="...",  # optional — The current attachment status of the cell.
    admin_domain_name="...",  # optional — The name of the admin domain in the parent cell, if any.
    primary_domain_name="...",  # optional — The domain designated as the primary domain for this cell, if any.
    registration_step="...",  # optional — The most recently reached registration checkpoint, or null if no registration has started. One of &#x60;UserEnsured&#x60;, &#x60;PATGenerated&#x60;, &#x60;PATPushed&#x60;.
    registration_error="..."  # optional — Operator-readable message describing the most recent registration failure, or null on success.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

