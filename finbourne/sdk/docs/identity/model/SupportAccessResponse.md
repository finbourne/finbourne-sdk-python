# SupportAccessResponse

Timestamped successful response to grant access to your account
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **id** | **str** | Required | ID of the support access request |
| **duration** | **str** | Required | The duration for which access is requested (in any ISO-8601 format) |
| **description** | **str** | Optional | The description of why the support access has been granted (i.e. support ticket numbers) |
| **created_at** | **datetime** | Required | DateTimeOffset at which the access was granted |
| **expiry** | **datetime** | Required | DateTimeOffset at which the access will be revoked |
| **created_by** | **str** | Required | Obfuscated UserId of the user who granted the support access |
| **terminated** | **bool** | Optional | Whether or not that access has been invalidated |
| **terminated_at** | **datetime** | Optional | DateTimeOffset at which the access was invalidated |
| **terminated_by** | **str** | Optional | Obfuscated UserId of the user who revoked the access |
| **permitted_roles** | **List[str]** | Optional | A list of permitted roles, valid for support staff to assume, for the duration of the access request |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.identity.models.SupportAccessResponse import SupportAccessResponse

instance = SupportAccessResponse(
    id="...",  # required — ID of the support access request
    duration="...",  # required — The duration for which access is requested (in any ISO-8601 format)
    description="...",  # optional — The description of why the support access has been granted (i.e. support ticket numbers)
    created_at=datetime.now(),  # required — DateTimeOffset at which the access was granted
    expiry=datetime.now(),  # required — DateTimeOffset at which the access will be revoked
    created_by="...",  # required — Obfuscated UserId of the user who granted the support access
    terminated=True,  # optional — Whether or not that access has been invalidated
    terminated_at=datetime.now(),  # optional — DateTimeOffset at which the access was invalidated
    terminated_by="...",  # optional — Obfuscated UserId of the user who revoked the access
    permitted_roles=  # optional — A list of permitted roles, valid for support staff to assume, for the duration of the access request
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

