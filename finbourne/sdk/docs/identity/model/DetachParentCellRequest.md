# DetachParentCellRequest

Request body for `DetachParentCell`. The endpoint uses a double-invoke pattern: the first call (Finbourne.Lydia.WebApi.Dtos.CellManagement.DetachParentCellRequest.Confirm=false) transitions the cell into Finbourne.Lydia.Postgres.Database.DTO.AttachmentStatus.Detaching; the second call (Finbourne.Lydia.WebApi.Dtos.CellManagement.DetachParentCellRequest.Confirm=true) performs the actual detach.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **confirm** | **bool** | Optional | False to mark the cell as &#x60;Detaching&#x60;; true to execute the detach. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.identity.models.DetachParentCellRequest import DetachParentCellRequest

instance = DetachParentCellRequest(
    confirm=True  # optional — False to mark the cell as &#x60;Detaching&#x60;; true to execute the detach.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

