# identity.IdentityLogsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_logs**](IdentityLogsApi.md#list_logs) | **GET** /identity/api/logs | [BETA] ListLogs: Lists system logs for a domain
[**list_user_logs**](IdentityLogsApi.md#list_user_logs) | **GET** /identity/api/logs/me | ListUserLogs: Lists user logs


### Example

```python
from finbourne.sdk.exceptions import ApiException
from finbourne.sdk.extensions.configuration_options import ConfigurationOptions
from finbourne.sdk.services.identity.models import *

from finbourne.sdk.extensions import (
  SyncApiClientFactory
)

from finbourne.sdk.services.identity.api.identity_logs_api import IdentityLogsApi

# opts = ConfigurationOptions()
# opts.total_timeout_ms = 30_000

# uncomment the below to use an api client factory with overrides
# api_client_factory = SyncApiClientFactory(opts=opts)

api_client_factory = SyncApiClientFactory()
api_instance = api_client_factory.build(IdentityLogsApi)
```

---

# **list_logs**
> ResourceListOfSystemLog listLogs = list_logs(okta_since=okta_since, okta_until=okta_until, okta_filter=okta_filter, okta_query=okta_query, okta_limit=okta_limit, okta_sort_order=okta_sort_order, okta_after=okta_after)

[BETA] ListLogs: Lists system logs for a domain

Lists system logs for a domain

### Example

```python
api_instance = api_client_factory.build(IdentityLogsApi)
okta_since = '2013-10-20T19:20:30+01:00' # datetime (optional)
okta_until = '2013-10-20T19:20:30+01:00' # datetime (optional)
okta_filter = 'okta_filter_example' # str (optional)
okta_query = 'okta_query_example' # str (optional)
okta_limit = 56 # int (optional)
okta_sort_order = 'okta_sort_order_example' # str (optional)
okta_after = 'okta_after_example' # str (optional)
api_response = api_instance.list_logs(okta_since=okta_since, okta_until=okta_until, okta_filter=okta_filter, okta_query=okta_query, okta_limit=okta_limit, okta_sort_order=okta_sort_order, okta_after=okta_after)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **okta_since** | **datetime**| Lower bound of log events published property | [optional] 
 **okta_until** | **datetime**| Upper bound of log events published property | [optional] 
 **okta_filter** | **str**| Okta filter expression | [optional] 
 **okta_query** | **str**| Filters log events results by one or more case insensitive keywords | [optional] 
 **okta_limit** | **int**| Max number of results returned | [optional] 
 **okta_sort_order** | **str**| Order of events by published property. Either ASCENDING or DESCENDING | [optional] 
 **okta_after** | **str**| Okta Page token | [optional] 

### Return type

[**ResourceListOfSystemLog**](ResourceListOfSystemLog.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List Logs |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **list_user_logs**
> ResourceListOfSystemLog listUserLogs = list_user_logs(okta_since=okta_since, okta_until=okta_until, okta_limit=okta_limit, okta_sort_order=okta_sort_order, okta_after=okta_after)

ListUserLogs: Lists user logs

Lists account related system logs for the calling user

### Example

```python
api_instance = api_client_factory.build(IdentityLogsApi)
okta_since = '2013-10-20T19:20:30+01:00' # datetime (optional)
okta_until = '2013-10-20T19:20:30+01:00' # datetime (optional)
okta_limit = 56 # int (optional)
okta_sort_order = 'okta_sort_order_example' # str (optional)
okta_after = 'okta_after_example' # str (optional)
api_response = api_instance.list_user_logs(okta_since=okta_since, okta_until=okta_until, okta_limit=okta_limit, okta_sort_order=okta_sort_order, okta_after=okta_after)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **okta_since** | **datetime**| Lower bound of log events published property | [optional] 
 **okta_until** | **datetime**| Upper bound of log events published property | [optional] 
 **okta_limit** | **int**| Max number of results returned | [optional] 
 **okta_sort_order** | **str**| Order of events by published property. Either ASCENDING or DESCENDING | [optional] 
 **okta_after** | **str**| Okta Page token | [optional] 

### Return type

[**ResourceListOfSystemLog**](ResourceListOfSystemLog.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List User Logs |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

