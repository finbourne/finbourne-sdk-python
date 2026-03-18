# NotificationType

Holds information about a Finbourne.Notifications.WebApi.Dtos.Notifications.Notification that is being created

## oneOf Type

`NotificationType` can be one of the following types:

* [AmazonSqsNotificationType](./AmazonSqsNotificationType.md)
* [AmazonSqsPrincipalAuthNotificationType](./AmazonSqsPrincipalAuthNotificationType.md)
* [AzureServiceBusNotificationType](./AzureServiceBusNotificationType.md)
* [EmailNotificationType](./EmailNotificationType.md)
* [SmsNotificationType](./SmsNotificationType.md)
* [WebhookNotificationType](./WebhookNotificationType.md)

## Usage

### Creating from a compatible type

```python
from finbourne.sdk.services.notifications.models.NotificationType import NotificationType

# Construct using any of the compatible types above
amazon_sqs_notification_type_instance = notifications.models.amazon_sqs_notification_type.AmazonSqsNotificationType(
                        type = 'AmazonSqs', 
                        api_key_ref = '', 
                        api_secret_ref = '', 
                        body = ' Aa6w77ikCX*cKCmv|`K/V', 
                        queue_url_ref = '', )

instance = NotificationType(amazon_sqs_notification_type_instance)
```

## Related Models

- [AmazonSqsNotificationType](./AmazonSqsNotificationType.md)
- [AmazonSqsPrincipalAuthNotificationType](./AmazonSqsPrincipalAuthNotificationType.md)
- [AzureServiceBusNotificationType](./AzureServiceBusNotificationType.md)
- [EmailNotificationType](./EmailNotificationType.md)
- [SmsNotificationType](./SmsNotificationType.md)
- [WebhookNotificationType](./WebhookNotificationType.md)

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

