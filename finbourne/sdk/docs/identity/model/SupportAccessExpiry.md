# SupportAccessExpiry

Time at which the support access expires
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **expiry** | **datetime** | Required | DateTimeOffset at which the access will be revoked |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.identity.models.SupportAccessExpiry import SupportAccessExpiry

instance = SupportAccessExpiry(
    expiry=datetime.now()  # required — DateTimeOffset at which the access will be revoked
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

