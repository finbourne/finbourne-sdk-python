# notifications.EventTypesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_event_type**](EventTypesApi.md#get_event_type) | **GET** /notifications/api/eventtypes/{eventType} | GetEventType: Gets the specified event type schema.
[**list_event_types**](EventTypesApi.md#list_event_types) | **GET** /notifications/api/eventtypes | ListEventTypes: Lists all of the available event types.


### Example

```python
from finbourne.sdk.exceptions import ApiException
from finbourne.sdk.extensions.configuration_options import ConfigurationOptions
from finbourne.sdk.services.notifications.models import *

from finbourne.sdk.extensions import (
  SyncApiClientFactory
)

from finbourne.sdk.services.notifications.api.event_types_api import EventTypesApi

# opts = ConfigurationOptions()
# opts.total_timeout_ms = 30_000

# uncomment the below to use an api client factory with overrides
# api_client_factory = SyncApiClientFactory(opts=opts)

api_client_factory = SyncApiClientFactory()
api_instance = api_client_factory.build(EventTypesApi)
```

---

# **get_event_type**
> EventTypeSchema getEventType = get_event_type(event_type)

GetEventType: Gets the specified event type schema.

### Example

```python
api_instance = api_client_factory.build(EventTypesApi)
event_type = 'event_type_example' # str
api_response = api_instance.get_event_type(event_type)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_type** | **str**| The event type to retrieve schema for. | [required] 

### Return type

[**EventTypeSchema**](EventTypeSchema.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | The details of the input related failure |  -  |
**404** | No event type exists with the specified type |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **list_event_types**
> ResourceListOfEventTypeSchema listEventTypes = list_event_types()

ListEventTypes: Lists all of the available event types.

### Example

```python
api_instance = api_client_factory.build(EventTypesApi)
api_response = api_instance.list_event_types()
pprint(api_response)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ResourceListOfEventTypeSchema**](ResourceListOfEventTypeSchema.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | No event types found |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

