# TpfRetrySftpResponse

Response from retrying SFTP file delivery
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **success** | **bool** | Required | Whether the retry was successful |
| **message** | **str** | Required | Status message describing the result |
| **new_file_delivery_id** | **int** | Optional | ID of the new file delivery record created for this retry (if successful) |
| **retried_at** | **datetime** | Optional | Timestamp when the retry was executed |
| **original_file** | [TpfFileDeliveryInfo](TpfFileDeliveryInfo.md) | Optional | *No description available.* |
| **duplicate_file** | [TpfFileDeliveryInfo](TpfFileDeliveryInfo.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.horizon.models.TpfRetrySftpResponse import TpfRetrySftpResponse

instance = TpfRetrySftpResponse(
    success=True,  # required — Whether the retry was successful
    message="...",  # required — Status message describing the result
    new_file_delivery_id=0,  # optional — ID of the new file delivery record created for this retry (if successful)
    retried_at=datetime.now(),  # optional — Timestamp when the retry was executed
    original_file=TpfFileDeliveryInfo(...),  # optional
    duplicate_file=TpfFileDeliveryInfo(...)  # optional
)
```

- [TpfFileDeliveryInfo](TpfFileDeliveryInfo.md)
- [TpfFileDeliveryInfo](TpfFileDeliveryInfo.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

