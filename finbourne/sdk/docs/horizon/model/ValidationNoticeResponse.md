# ValidationNoticeResponse

A non-blocking finding raised when an instance was saved. The save succeeded regardless.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **severity** | **str** | Required | \&quot;Warning\&quot; or \&quot;Information\&quot;. |
| **var_field** | **str** | Required | The configuration field the finding relates to. |
| **message** | **str** | Required | What was found. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.horizon.models.ValidationNoticeResponse import ValidationNoticeResponse

instance = ValidationNoticeResponse(
    severity="...",  # required — \&quot;Warning\&quot; or \&quot;Information\&quot;.
    var_field="...",  # required — The configuration field the finding relates to.
    message="..."  # required — What was found.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

