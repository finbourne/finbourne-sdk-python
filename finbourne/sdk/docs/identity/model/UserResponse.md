# UserResponse

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **id** | **str** | Required | The user&#39;s system supplied unique identifier |
| **alternative_user_ids** | **Dict[str, Optional[str]]** | Optional | The user&#39;s alternative IDs |
| **email_address** | **str** | Required | The user&#39;s emailAddress address, which must be unique within the system |
| **second_email_address** | **str** | Optional | The user&#39;s second email address. Only allowed for service users. |
| **login** | **str** | Required | *No description available.* |
| **first_name** | **str** | Required | The user&#39;s first name |
| **last_name** | **str** | Required | The user&#39;s last name |
| **roles** | [List[RoleResponse]](RoleResponse.md) | Optional | The roles that the user has. |
| **type** | **str** | Required | The type of user (e.g. Personal or Service) |
| **status** | **str** | Required | The status of the user |
| **external** | **bool** | Required | Whether or not the user originates from an external identity system |
| **last_login** | **datetime** | Optional | Last time the user logged in |
| **last_updated** | **datetime** | Optional | Last time the user was updated |
| **created** | **datetime** | Optional | Date the user was created |
| **password_changed** | **datetime** | Optional | Last time the password was changed for this user |
| **user_expiry** | **datetime** | Optional | The user&#39;s expiry unix datetime |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.identity.models.UserResponse import UserResponse

instance = UserResponse(
    id="...",  # required — The user&#39;s system supplied unique identifier
    alternative_user_ids=,  # optional — The user&#39;s alternative IDs
    email_address="...",  # required — The user&#39;s emailAddress address, which must be unique within the system
    second_email_address="...",  # optional — The user&#39;s second email address. Only allowed for service users.
    login="...",  # required
    first_name="...",  # required — The user&#39;s first name
    last_name="...",  # required — The user&#39;s last name
    roles=[],  # optional — The roles that the user has.
    type="...",  # required — The type of user (e.g. Personal or Service)
    status="...",  # required — The status of the user
    external=True,  # required — Whether or not the user originates from an external identity system
    last_login=datetime.now(),  # optional — Last time the user logged in
    last_updated=datetime.now(),  # optional — Last time the user was updated
    created=datetime.now(),  # optional — Date the user was created
    password_changed=datetime.now(),  # optional — Last time the password was changed for this user
    user_expiry=datetime.now(),  # optional — The user&#39;s expiry unix datetime
    links=[]  # optional
)
```

- [RoleResponse](RoleResponse.md) — used in `roles`
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

