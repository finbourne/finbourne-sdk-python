# CreateSubscription

The information required to create a subscription
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **display_name** | **str** | Required | The name of the subscription |
| **description** | **str** | Optional | The summary of the services provided by the subscription |
| **status** | **str** | Required | The current status of the subscription. Possible values are: Active, Inactive |
| **matching_pattern** | [MatchingPattern](MatchingPattern.md) | Required | *No description available.* |
| **use_as_auth** | **str** | Optional | Id of user associated with subscription. All events associated with  the subscription will use this user to check entitlements against  the resource to send a notification. Can be null, in which case  we&#39;ll default to that of the user making this request |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.notifications.models.CreateSubscription import CreateSubscription

instance = CreateSubscription(
    id=ResourceId(...),  # required
    display_name="...",  # required — The name of the subscription
    description="...",  # optional — The summary of the services provided by the subscription
    status="...",  # required — The current status of the subscription. Possible values are: Active, Inactive
    matching_pattern=MatchingPattern(...),  # required
    use_as_auth="..."  # optional — Id of user associated with subscription. All events associated with  the subscription will use this user to check entitlements against  the resource to send a notification. Can be null, in which case  we&#39;ll default to that of the user making this request
)
```


## Related Models

- [ResourceId](ResourceId.md)
- [MatchingPattern](MatchingPattern.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

