# UpdateUserRequest

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **first_name** | **str** | Required | *No description available.* |
| **last_name** | **str** | Required | *No description available.* |
| **email_address** | **str** | Required | *No description available.* |
| **second_email_address** | **str** | Optional | *No description available.* |
| **login** | **str** | Required | The user&#39;s login username, in the form of an email address, which must be unique within the system. For user accounts this should exactly match the user&#39;s email address. |
| **alternative_user_ids** | **Dict[str, Optional[str]]** | Optional | *No description available.* |
| **roles** | [List[RoleId]](RoleId.md) | Optional | Deprecated. To update a user&#39;s roles use the AddUserToRole and RemoveUserFromRole endpoints |
| **user_expiry** | **datetime** | Optional | The user&#39;s expiry unix datetime |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.identity.models.UpdateUserRequest import UpdateUserRequest

instance = UpdateUserRequest(
    first_name="...",  # required
    last_name="...",  # required
    email_address="...",  # required
    second_email_address="...",  # optional
    login="...",  # required — The user&#39;s login username, in the form of an email address, which must be unique within the system. For user accounts this should exactly match the user&#39;s email address.
    alternative_user_ids=,  # optional
    roles=[],  # optional — Deprecated. To update a user&#39;s roles use the AddUserToRole and RemoveUserFromRole endpoints
    user_expiry=datetime.now()  # optional — The user&#39;s expiry unix datetime
)
```

- [RoleId](RoleId.md) — used in `roles`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

