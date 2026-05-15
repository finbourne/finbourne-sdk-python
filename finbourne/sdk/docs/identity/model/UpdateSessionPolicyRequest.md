# UpdateSessionPolicyRequest

Session timing settings.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **max_session_idle_minutes** | **int** | Required | Maximum minutes a user&#39;s session can be idle before re-authentication is required. Must be between 5 minutes and 12 hours (720 minutes). |
| **max_session_lifetime_minutes** | **int** | Optional | Maximum minutes a user&#39;s session can live in total. Omit to disable session expiry; otherwise must be between 5 minutes and 24 hours (1440 minutes). |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.identity.models.UpdateSessionPolicyRequest import UpdateSessionPolicyRequest

instance = UpdateSessionPolicyRequest(
    max_session_idle_minutes=0,  # required — Maximum minutes a user&#39;s session can be idle before re-authentication is required. Must be between 5 minutes and 12 hours (720 minutes).
    max_session_lifetime_minutes=0  # optional — Maximum minutes a user&#39;s session can live in total. Omit to disable session expiry; otherwise must be between 5 minutes and 24 hours (1440 minutes).
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

