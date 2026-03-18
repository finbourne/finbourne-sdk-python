# Subscription

A subscription object
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **display_name** | **str** | Required | The name of the subscription |
| **description** | **str** | Optional | The summary of the services provided by the subscription |
| **status** | **str** | Required | The current status of the subscription |
| **matching_pattern** | [MatchingPattern](MatchingPattern.md) | Required | *No description available.* |
| **created_at** | **datetime** | Required | The time at which the subscription was made |
| **user_id_created** | **str** | Required | The user who made the subscription |
| **modified_at** | **datetime** | Required | The time at which the subscription was last modified |
| **user_id_modified** | **str** | Required | The user who last modified the subscription |
| **use_as_auth** | **str** | Required | The user to use as auth for the subscription |
| **href** | **str** | Optional | A URI for retrieving this subscription |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.notifications.models.Subscription import Subscription

instance = Subscription(
    id=ResourceId(...),  # required
    display_name="...",  # required — The name of the subscription
    description="...",  # optional — The summary of the services provided by the subscription
    status="...",  # required — The current status of the subscription
    matching_pattern=MatchingPattern(...),  # required
    created_at=datetime.now(),  # required — The time at which the subscription was made
    user_id_created="...",  # required — The user who made the subscription
    modified_at=datetime.now(),  # required — The time at which the subscription was last modified
    user_id_modified="...",  # required — The user who last modified the subscription
    use_as_auth="...",  # required — The user to use as auth for the subscription
    href="..."  # optional — A URI for retrieving this subscription
)
```


## Related Models

- [ResourceId](ResourceId.md)
- [MatchingPattern](MatchingPattern.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

