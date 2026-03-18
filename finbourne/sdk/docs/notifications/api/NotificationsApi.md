# notifications.NotificationsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_notification**](NotificationsApi.md#create_notification) | **POST** /notifications/api/subscriptions/{scope}/{code}/notifications | CreateNotification: Add a Notification to a Subscription.
[**delete_notification**](NotificationsApi.md#delete_notification) | **DELETE** /notifications/api/subscriptions/{scope}/{code}/notifications/{id} | DeleteNotification: Delete a notification for a given subscription.
[**get_notification**](NotificationsApi.md#get_notification) | **GET** /notifications/api/subscriptions/{scope}/{code}/notifications/{id} | GetNotification: Get a notification on a subscription.
[**list_notifications**](NotificationsApi.md#list_notifications) | **GET** /notifications/api/subscriptions/{scope}/{code}/notifications | ListNotifications: List all notifications on a subscription.
[**update_notification**](NotificationsApi.md#update_notification) | **PUT** /notifications/api/subscriptions/{scope}/{code}/notifications/{id} | UpdateNotification: Update a Notification for a Subscription


### Example

```python
from finbourne.sdk.exceptions import ApiException
from finbourne.sdk.extensions.configuration_options import ConfigurationOptions
from finbourne.sdk.services.notifications.models import *

from finbourne.sdk.extensions import (
  SyncApiClientFactory
)

from finbourne.sdk.services.notifications.api.notifications_api import NotificationsApi

# opts = ConfigurationOptions()
# opts.total_timeout_ms = 30_000

# uncomment the below to use an api client factory with overrides
# api_client_factory = SyncApiClientFactory(opts=opts)

api_client_factory = SyncApiClientFactory()
api_instance = api_client_factory.build(NotificationsApi)
```

---

# **create_notification**
> Notification createNotification = create_notification(scope, code, create_notification_request)

CreateNotification: Add a Notification to a Subscription.

### Example

```python
api_instance = api_client_factory.build(NotificationsApi)
scope = 'scope_example' # str
code = 'code_example' # str
create_notification_request = CreateNotificationRequest()
api_response = api_instance.create_notification(scope, code, create_notification_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope that identifies a subscription | [required] 
 **code** | **str**| The code that identifies a subscription | [required] 
 **create_notification_request** | [**CreateNotificationRequest**](CreateNotificationRequest.md)| The data to create a notification | [required] 

### Return type

[**Notification**](Notification.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **delete_notification**
> deleteNotification = delete_notification(scope, code, id)

DeleteNotification: Delete a notification for a given subscription.

### Example

```python
api_instance = api_client_factory.build(NotificationsApi)
scope = 'scope_example' # str
code = 'code_example' # str
id = 'id_example' # str
api_instance.delete_notification(scope, code, id)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope that identifies a subscription | [required] 
 **code** | **str**| The code that identifies a subscription | [required] 
 **id** | **str**| The unique identifier of the notification | [required] 

### Return type

void (empty response body)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**400** | The details of the input related failure |  -  |
**404** | No notification exists in current scope |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_notification**
> Notification getNotification = get_notification(scope, code, id)

GetNotification: Get a notification on a subscription.

### Example

```python
api_instance = api_client_factory.build(NotificationsApi)
scope = 'scope_example' # str
code = 'code_example' # str
id = 'id_example' # str
api_response = api_instance.get_notification(scope, code, id)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope that identifies a subscription | [required] 
 **code** | **str**| The code that identifies a subscription | [required] 
 **id** | **str**| The unique identifier of the notification | [required] 

### Return type

[**Notification**](Notification.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | The details of the input related failure |  -  |
**404** | No notification exists in current scope |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **list_notifications**
> ResourceListOfNotification listNotifications = list_notifications(scope, code)

ListNotifications: List all notifications on a subscription.

### Example

```python
api_instance = api_client_factory.build(NotificationsApi)
scope = 'scope_example' # str
code = 'code_example' # str
api_response = api_instance.list_notifications(scope, code)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope that identifies a subscription | [required] 
 **code** | **str**| The code that identifies a subscription | [required] 

### Return type

[**ResourceListOfNotification**](ResourceListOfNotification.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | The details of the input related failure |  -  |
**404** | No notifications exists with the provided filter(s) |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **update_notification**
> Notification updateNotification = update_notification(scope, code, id, update_notification_request)

UpdateNotification: Update a Notification for a Subscription

### Example

```python
api_instance = api_client_factory.build(NotificationsApi)
scope = 'scope_example' # str
code = 'code_example' # str
id = 'id_example' # str
update_notification_request = UpdateNotificationRequest()
api_response = api_instance.update_notification(scope, code, id, update_notification_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope that identifies a subscription | [required] 
 **code** | **str**| The code that identifies a subscription | [required] 
 **id** | **str**| The unique identifier of the notification | [required] 
 **update_notification_request** | [**UpdateNotificationRequest**](UpdateNotificationRequest.md)| The data to update a notification | [required] 

### Return type

[**Notification**](Notification.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | The details of the input related failure |  -  |
**404** | No notification exists in current scope |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

