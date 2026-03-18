# insights.AuditingApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_entry**](AuditingApi.md#create_entry) | **POST** /insights/api/auditing/entries | [EARLY ACCESS] CreateEntry: Create (persist) and audit entry..
[**get_processes**](AuditingApi.md#get_processes) | **GET** /insights/api/auditing/processes | [EARLY ACCESS] GetProcesses: Get the latest audit entry for each process.
[**list_entries**](AuditingApi.md#list_entries) | **GET** /insights/api/auditing/entries | [EARLY ACCESS] ListEntries: Get the audit entries.


### Example

```python
from finbourne.sdk.exceptions import ApiException
from finbourne.sdk.extensions.configuration_options import ConfigurationOptions
from finbourne.sdk.services.insights.models import *

from finbourne.sdk.extensions import (
  SyncApiClientFactory
)

from finbourne.sdk.services.insights.api.auditing_api import AuditingApi

# opts = ConfigurationOptions()
# opts.total_timeout_ms = 30_000

# uncomment the below to use an api client factory with overrides
# api_client_factory = SyncApiClientFactory(opts=opts)

api_client_factory = SyncApiClientFactory()
api_instance = api_client_factory.build(AuditingApi)
```

---

# **create_entry**
> AuditEntry createEntry = create_entry(create_audit_entry=create_audit_entry)

[EARLY ACCESS] CreateEntry: Create (persist) and audit entry..

### Example

```python
api_instance = api_client_factory.build(AuditingApi)
create_audit_entry = CreateAuditEntry()
api_response = api_instance.create_entry(create_audit_entry=create_audit_entry)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_audit_entry** | [**CreateAuditEntry**](CreateAuditEntry.md)| Information about the entry to be created. | [optional] 

### Return type

[**AuditEntry**](AuditEntry.md)

### HTTP request headers

 - **Content-Type**: application/json, application/json-patch+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**429** | There have been too many recent requests, retry later (using the RETRY-AFTER header value as the delay). |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_processes**
> ResourceListOfAuditProcessSummary getProcesses = get_processes()

[EARLY ACCESS] GetProcesses: Get the latest audit entry for each process.

This will never be `null`, though it may be empty.

### Example

```python
api_instance = api_client_factory.build(AuditingApi)
api_response = api_instance.get_processes()
pprint(api_response)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ResourceListOfAuditProcessSummary**](ResourceListOfAuditProcessSummary.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **list_entries**
> ScrollableCollectionOfAuditEntry listEntries = list_entries(filter=filter, sort_by=sort_by, size=size, state=state)

[EARLY ACCESS] ListEntries: Get the audit entries.

This will never be `null`, though it may be empty.

### Example

```python
api_instance = api_client_factory.build(AuditingApi)
filter = 'filter_example' # str (optional)
sort_by = 'sort_by_example' # str (optional)
size = 1000 # int (optional)
state = 'state_example' # str (optional)
api_response = api_instance.list_entries(filter=filter, sort_by=sort_by, size=size, state=state)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| The filter to be applied to the results. | [optional] 
 **sort_by** | **str**| The order to return the entries in. | [optional] 
 **size** | **int**| The maximum number of entries to return. | [optional] [default to 1000]
 **state** | **str**| The scrolling state, used to iterate through the data set. | [optional] 

### Return type

[**ScrollableCollectionOfAuditEntry**](ScrollableCollectionOfAuditEntry.md)

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

