# SupportAccessRequest

A Request to grant support access to your account
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **duration** | **str** | Required | The duration for which access is requested (in any ISO-8601 format) |
| **description** | **str** | Optional | The description of why the support access has been granted (i.e. support ticket numbers) |
| **permitted_roles** | **List[str]** | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.identity.models.SupportAccessRequest import SupportAccessRequest

instance = SupportAccessRequest(
    duration="...",  # required — The duration for which access is requested (in any ISO-8601 format)
    description="...",  # optional — The description of why the support access has been granted (i.e. support ticket numbers)
    permitted_roles=  # optional
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

