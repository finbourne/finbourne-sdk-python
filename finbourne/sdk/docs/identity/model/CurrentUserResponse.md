# CurrentUserResponse

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **id** | **str** | Required | The user&#39;s system supplied unique identifier |
| **email_address** | **str** | Required | The user&#39;s email address which may be null depending on the authentication method |
| **type** | **str** | Required | The type of user (e.g. Personal or Service) |
| **domain_type** | **str** | Optional | The type of domain in which the user exists |
| **user_expiry** | **datetime** | Optional | The user&#39;s user expiry datetime |
| **groups** | **List[str]** | Optional | The groups this user belongs to |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.identity.models.CurrentUserResponse import CurrentUserResponse

instance = CurrentUserResponse(
    id="...",  # required — The user&#39;s system supplied unique identifier
    email_address="...",  # required — The user&#39;s email address which may be null depending on the authentication method
    type="...",  # required — The type of user (e.g. Personal or Service)
    domain_type="...",  # optional — The type of domain in which the user exists
    user_expiry=datetime.now(),  # optional — The user&#39;s user expiry datetime
    groups=,  # optional — The groups this user belongs to
    links=[]  # optional
)
```

- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

