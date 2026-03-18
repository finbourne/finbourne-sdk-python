# AttemptStatus

Status of the delivery attempt.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **result** | **str** | Required | Result of the delivery. |
| **detailed_message** | **str** | Optional | The detailed message from attempting to deliver the message. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.notifications.models.AttemptStatus import AttemptStatus

instance = AttemptStatus(
    result="...",  # required — Result of the delivery.
    detailed_message="..."  # optional — The detailed message from attempting to deliver the message.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

