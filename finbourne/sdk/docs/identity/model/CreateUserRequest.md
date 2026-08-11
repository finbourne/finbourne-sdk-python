# CreateUserRequest

Details necessary for creating a new user
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **first_name** | **str** | Required | The first name of the user |
| **last_name** | **str** | Required | The last name of the user |
| **email_address** | **str** | Required | The user&#39;s email address - to which the account validation email will be sent. For user accounts this should exactly match the Login. |
| **second_email_address** | **str** | Optional | The user&#39;s second email address. Only allowed for Service users |
| **login** | **str** | Required | The user&#39;s login username, which must be unique within the system. For user accounts this should exactly match the user&#39;s email address. |
| **alternative_user_ids** | **Dict[str, Optional[str]]** | Optional | *No description available.* |
| **roles** | [List[RoleId]](RoleId.md) | Optional | Optional. Any known roles the user should be created with. |
| **type** | **str** | Required | The type of user (e.g. Personal or Service) |
| **user_expiry** | **datetime** | Optional | The user&#39;s expiry unix datetime |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.identity.models.CreateUserRequest import CreateUserRequest

instance = CreateUserRequest(
    first_name="...",  # required — The first name of the user
    last_name="...",  # required — The last name of the user
    email_address="...",  # required — The user&#39;s email address - to which the account validation email will be sent. For user accounts this should exactly match the Login.
    second_email_address="...",  # optional — The user&#39;s second email address. Only allowed for Service users
    login="...",  # required — The user&#39;s login username, which must be unique within the system. For user accounts this should exactly match the user&#39;s email address.
    alternative_user_ids=,  # optional
    roles=[],  # optional — Optional. Any known roles the user should be created with.
    type="...",  # required — The type of user (e.g. Personal or Service)
    user_expiry=datetime.now()  # optional — The user&#39;s expiry unix datetime
)
```

- [RoleId](RoleId.md) — used in `roles`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

