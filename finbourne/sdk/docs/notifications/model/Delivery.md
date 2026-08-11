# Delivery

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **id** | **UUID** | Required | The identifier of the delivery. |
| **event_id** | **str** | Required | The identifier of the associated event. |
| **subscription_id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **notification_id** | **str** | Required | The identifier of the associated notification. |
| **delivery_channel** | **str** | Required | The delivery channel of the message. |
| **message_details** | **str** | Required | The Details of the delivery message as JSON string. |
| **attempts** | [List[Attempt]](Attempt.md) | Required | A list of all the delivery attempts made for this message. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.notifications.models.Delivery import Delivery

instance = Delivery(
    id="...",  # required — The identifier of the delivery.
    event_id="...",  # required — The identifier of the associated event.
    subscription_id=ResourceId(...),  # required
    notification_id="...",  # required — The identifier of the associated notification.
    delivery_channel="...",  # required — The delivery channel of the message.
    message_details="...",  # required — The Details of the delivery message as JSON string.
    attempts=[]  # required — A list of all the delivery attempts made for this message.
)
```

- [ResourceId](ResourceId.md)
- [Attempt](Attempt.md) — used in `attempts`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

