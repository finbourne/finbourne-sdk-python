# SessionPolicyResponse

Session timing settings.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **max_session_idle_minutes** | **int** | Optional | Maximum minutes a user&#39;s session can be idle before re-authentication is required. |
| **max_session_lifetime_minutes** | **int** | Optional | Maximum minutes a user&#39;s session can live in total. When absent, sessions do not expire. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.identity.models.SessionPolicyResponse import SessionPolicyResponse

instance = SessionPolicyResponse(
    max_session_idle_minutes=0,  # optional — Maximum minutes a user&#39;s session can be idle before re-authentication is required.
    max_session_lifetime_minutes=0  # optional — Maximum minutes a user&#39;s session can live in total. When absent, sessions do not expire.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

