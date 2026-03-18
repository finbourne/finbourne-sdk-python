# NotificationTypeResponse

Holds readonly information about a Finbourne.Notifications.WebApi.Dtos.Notifications.Notification

## oneOf Type

`NotificationTypeResponse` can be one of the following types:

* [AmazonSqsNotificationTypeResponse](./AmazonSqsNotificationTypeResponse.md)
* [AmazonSqsPrincipalAuthNotificationTypeResponse](./AmazonSqsPrincipalAuthNotificationTypeResponse.md)
* [AzureServiceBusTypeResponse](./AzureServiceBusTypeResponse.md)
* [EmailNotificationTypeResponse](./EmailNotificationTypeResponse.md)
* [SmsNotificationTypeResponse](./SmsNotificationTypeResponse.md)
* [WebhookNotificationTypeResponse](./WebhookNotificationTypeResponse.md)

## Usage

### Creating from a compatible type

```python
from finbourne.sdk.services.notifications.models.NotificationTypeResponse import NotificationTypeResponse

# Construct using any of the compatible types above
amazon_sqs_notification_type_response_instance = notifications.models.amazon_sqs_notification_type_response.AmazonSqsNotificationTypeResponse(
                        type = 'AmazonSqs', 
                        api_key_ref = '', 
                        api_secret_ref = '', 
                        body = '', 
                        queue_url_ref = '', )

instance = NotificationTypeResponse(amazon_sqs_notification_type_response_instance)
```

## Related Models

- [AmazonSqsNotificationTypeResponse](./AmazonSqsNotificationTypeResponse.md)
- [AmazonSqsPrincipalAuthNotificationTypeResponse](./AmazonSqsPrincipalAuthNotificationTypeResponse.md)
- [AzureServiceBusTypeResponse](./AzureServiceBusTypeResponse.md)
- [EmailNotificationTypeResponse](./EmailNotificationTypeResponse.md)
- [SmsNotificationTypeResponse](./SmsNotificationTypeResponse.md)
- [WebhookNotificationTypeResponse](./WebhookNotificationTypeResponse.md)

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

