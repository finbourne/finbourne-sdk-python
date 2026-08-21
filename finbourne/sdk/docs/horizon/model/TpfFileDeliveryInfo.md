# TpfFileDeliveryInfo

Information about a file delivery
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **file_uuid** | **UUID** | Required | File delivery UUID — the identifier the retry endpoint accepts |
| **file_name** | **str** | Required | File name |
| **file_hash** | **str** | Required | SHA-256 hash of the file content |
| **destination_path** | **str** | Required | SFTP destination path |
| **status** | **str** | Required | Delivery status |
| **generated_at** | **datetime** | Required | Timestamp when the file was originally generated |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.horizon.models.TpfFileDeliveryInfo import TpfFileDeliveryInfo

instance = TpfFileDeliveryInfo(
    file_uuid="...",  # required — File delivery UUID — the identifier the retry endpoint accepts
    file_name="...",  # required — File name
    file_hash="...",  # required — SHA-256 hash of the file content
    destination_path="...",  # required — SFTP destination path
    status="...",  # required — Delivery status
    generated_at=datetime.now()  # required — Timestamp when the file was originally generated
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

