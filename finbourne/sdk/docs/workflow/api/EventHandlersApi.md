# workflow.EventHandlersApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_event_handler**](EventHandlersApi.md#create_event_handler) | **POST** /workflow/api/eventhandlers | CreateEventHandler: Create a new Event Handler
[**delete_event_handler**](EventHandlersApi.md#delete_event_handler) | **DELETE** /workflow/api/eventhandlers/{scope}/{code} | DeleteEventHandler: Delete an Event Handler
[**get_event_handler**](EventHandlersApi.md#get_event_handler) | **GET** /workflow/api/eventhandlers/{scope}/{code} | GetEventHandler: Get an Event Handler
[**list_event_handlers**](EventHandlersApi.md#list_event_handlers) | **GET** /workflow/api/eventhandlers | ListEventHandlers: List Event Handlers
[**update_event_handler**](EventHandlersApi.md#update_event_handler) | **PUT** /workflow/api/eventhandlers/{scope}/{code} | UpdateEventHandler: Update an existing Event handler


### Example

```python
from finbourne.sdk.exceptions import ApiException
from finbourne.sdk.extensions.configuration_options import ConfigurationOptions
from finbourne.sdk.services.workflow.models import *

from finbourne.sdk.extensions import (
  SyncApiClientFactory
)

from finbourne.sdk.services.workflow.api.event_handlers_api import EventHandlersApi

# opts = ConfigurationOptions()
# opts.total_timeout_ms = 30_000

# uncomment the below to use an api client factory with overrides
# api_client_factory = SyncApiClientFactory(opts=opts)

api_client_factory = SyncApiClientFactory()
api_instance = api_client_factory.build(EventHandlersApi)
```

---

# **create_event_handler**
> EventHandler createEventHandler = create_event_handler(create_event_handler_request)

CreateEventHandler: Create a new Event Handler

### Example

```python
api_instance = api_client_factory.build(EventHandlersApi)
create_event_handler_request = CreateEventHandlerRequest()
api_response = api_instance.create_event_handler(create_event_handler_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_event_handler_request** | [**CreateEventHandlerRequest**](CreateEventHandlerRequest.md)| The data to create an Event Handler | [required] 

### Return type

[**EventHandler**](EventHandler.md)

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

# **delete_event_handler**
> DeletedEntityResponse deleteEventHandler = delete_event_handler(scope, code)

DeleteEventHandler: Delete an Event Handler

If the Event Handler does not exist a failure will be returned

### Example

```python
api_instance = api_client_factory.build(EventHandlersApi)
scope = 'scope_example' # str
code = 'code_example' # str
api_response = api_instance.delete_event_handler(scope, code)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| Scope of the event handler to be deleted | [required] 
 **code** | **str**| Code of the event handler to be deleted | [required] 

### Return type

[**DeletedEntityResponse**](DeletedEntityResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | The details of the input related failure |  -  |
**404** | Event Handler not found. |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_event_handler**
> EventHandler getEventHandler = get_event_handler(scope, code, as_at=as_at)

GetEventHandler: Get an Event Handler

Will return a NotFound failure if the event handler does not exist

### Example

```python
api_instance = api_client_factory.build(EventHandlersApi)
scope = 'scope_example' # str
code = 'code_example' # str
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
api_response = api_instance.get_event_handler(scope, code, as_at=as_at)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| Scope of the event handler | [required] 
 **code** | **str**| Code of the event handler | [required] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the event handler. Defaults to returning the latest version of the event handler if not specified. | [optional] 

### Return type

[**EventHandler**](EventHandler.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **list_event_handlers**
> PagedResourceListOfEventHandler listEventHandlers = list_event_handlers(as_at=as_at, filter=filter, limit=limit, page=page)

ListEventHandlers: List Event Handlers

### Example

```python
api_instance = api_client_factory.build(EventHandlersApi)
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
filter = 'filter_example' # str (optional)
limit = 10 # int (optional)
page = 'page_example' # str (optional)
api_response = api_instance.list_event_handlers(as_at=as_at, filter=filter, limit=limit, page=page)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **as_at** | **datetime**| The asAt datetime at which to list the Event Handlers. Defaults to return the latest version of each Event Handler if not specified. | [optional] 
 **filter** | **str**| Expression to filter the result set. Read more about filtering results from LUSID here: https://support.lusid.com/filtering-results-from-lusid. | [optional] 
 **limit** | **int**| When paginating, limit the number of returned results to this many. | [optional] [default to 10]
 **page** | **str**| The pagination token to use to continue listing event handlers from a previous call to list event handlers. This value is returned from the previous call. If a pagination token is provided the sortBy, filter, effectiveAt, and asAt fields must not have changed since the original request. | [optional] 

### Return type

[**PagedResourceListOfEventHandler**](PagedResourceListOfEventHandler.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of Event Handlers |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **update_event_handler**
> EventHandler updateEventHandler = update_event_handler(scope, code, update_event_handler_request)

UpdateEventHandler: Update an existing Event handler

### Example

```python
api_instance = api_client_factory.build(EventHandlersApi)
scope = 'scope_example' # str
code = 'code_example' # str
update_event_handler_request = UpdateEventHandlerRequest()
api_response = api_instance.update_event_handler(scope, code, update_event_handler_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope that identifies an Event Handler | [required] 
 **code** | **str**| The code that identifies an Event Handler | [required] 
 **update_event_handler_request** | [**UpdateEventHandlerRequest**](UpdateEventHandlerRequest.md)| The data to update an Event Handler | [required] 

### Return type

[**EventHandler**](EventHandler.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | The details of the input related failure |  -  |
**404** | Event Handler not found. |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

