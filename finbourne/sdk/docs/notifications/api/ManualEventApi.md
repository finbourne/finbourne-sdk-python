# notifications.ManualEventApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**trigger_manual_event**](ManualEventApi.md#trigger_manual_event) | **POST** /notification/api/manualevent | TriggerManualEvent: Trigger a manual event.


### Example

```python
from finbourne.sdk.exceptions import ApiException
from finbourne.sdk.extensions.configuration_options import ConfigurationOptions
from finbourne.sdk.services.notifications.models import *

from finbourne.sdk.extensions import (
  SyncApiClientFactory
)

from finbourne.sdk.services.notifications.api.manual_event_api import ManualEventApi

# opts = ConfigurationOptions()
# opts.total_timeout_ms = 30_000

# uncomment the below to use an api client factory with overrides
# api_client_factory = SyncApiClientFactory(opts=opts)

api_client_factory = SyncApiClientFactory()
api_instance = api_client_factory.build(ManualEventApi)
```

---

# **trigger_manual_event**
> ManualEvent triggerManualEvent = trigger_manual_event(manual_event_request)

TriggerManualEvent: Trigger a manual event.

### Example

```python
api_instance = api_client_factory.build(ManualEventApi)
manual_event_request = ManualEventRequest()
api_response = api_instance.trigger_manual_event(manual_event_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **manual_event_request** | [**ManualEventRequest**](ManualEventRequest.md)| The data required to trigger a manual event. | [required] 

### Return type

[**ManualEvent**](ManualEvent.md)

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

