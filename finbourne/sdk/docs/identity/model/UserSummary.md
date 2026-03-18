# UserSummary

Lightweight view of an user details
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **id** | **str** | Optional | The user id |
| **login** | **str** | Optional | The user login |
| **email** | **str** | Optional | The email address registered for that user |
| **second_email** | **str** | Optional | *No description available.* |
| **first_name** | **str** | Optional | User&#39;s first name |
| **last_name** | **str** | Optional | User&#39;s last name |
| **type** | **str** | Optional | User&#39;s type (Personal, Service...) |
| **alternative_user_ids** | **Dict[str, Optional[str]]** | Optional | User&#39;s alternative user IDs. Only returned for the current user |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.identity.models.UserSummary import UserSummary

instance = UserSummary(
    id="...",  # optional — The user id
    login="...",  # optional — The user login
    email="...",  # optional — The email address registered for that user
    second_email="...",  # optional
    first_name="...",  # optional — User&#39;s first name
    last_name="...",  # optional — User&#39;s last name
    type="...",  # optional — User&#39;s type (Personal, Service...)
    alternative_user_ids=,  # optional — User&#39;s alternative user IDs. Only returned for the current user
    links=[]  # optional
)
```

- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

