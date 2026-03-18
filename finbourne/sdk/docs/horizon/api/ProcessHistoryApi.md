# horizon.ProcessHistoryApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_complete_event**](ProcessHistoryApi.md#create_complete_event) | **POST** /horizon/api/process-history/event/complete | [EARLY ACCESS] CreateCompleteEvent: Write a completed event to the Horizon Dashboard
[**create_update_event**](ProcessHistoryApi.md#create_update_event) | **POST** /horizon/api/process-history/event/update | [EARLY ACCESS] CreateUpdateEvent: Write an update event to the Horizon Dashboard
[**get_latest_runs**](ProcessHistoryApi.md#get_latest_runs) | **GET** /horizon/api/process-history/$latestRuns | [EARLY ACCESS] GetLatestRuns: Get latest run for each process
[**process_entry_updates**](ProcessHistoryApi.md#process_entry_updates) | **POST** /horizon/api/process-history/entries/$query | [EARLY ACCESS] ProcessEntryUpdates: Get process entry updates for a query
[**process_history_entries**](ProcessHistoryApi.md#process_history_entries) | **POST** /horizon/api/process-history/$query | [EARLY ACCESS] ProcessHistoryEntries: Get process history entries


### Example

```python
from finbourne.sdk.exceptions import ApiException
from finbourne.sdk.extensions.configuration_options import ConfigurationOptions
from finbourne.sdk.services.horizon.models import *

from finbourne.sdk.extensions import (
  SyncApiClientFactory
)

from finbourne.sdk.services.horizon.api.process_history_api import ProcessHistoryApi

# opts = ConfigurationOptions()
# opts.total_timeout_ms = 30_000

# uncomment the below to use an api client factory with overrides
# api_client_factory = SyncApiClientFactory(opts=opts)

api_client_factory = SyncApiClientFactory()
api_instance = api_client_factory.build(ProcessHistoryApi)
```

---

# **create_complete_event**
> AuditCompleteResponse createCompleteEvent = create_complete_event(audit_complete_request)

[EARLY ACCESS] CreateCompleteEvent: Write a completed event to the Horizon Dashboard

### Example

```python
api_instance = api_client_factory.build(ProcessHistoryApi)
audit_complete_request = AuditCompleteRequest()
api_response = api_instance.create_complete_event(audit_complete_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **audit_complete_request** | [**AuditCompleteRequest**](AuditCompleteRequest.md)|  | [required] 

### Return type

[**AuditCompleteResponse**](AuditCompleteResponse.md)

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

# **create_update_event**
> AuditUpdateResponse createUpdateEvent = create_update_event(audit_update_request)

[EARLY ACCESS] CreateUpdateEvent: Write an update event to the Horizon Dashboard

### Example

```python
api_instance = api_client_factory.build(ProcessHistoryApi)
audit_update_request = AuditUpdateRequest()
api_response = api_instance.create_update_event(audit_update_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **audit_update_request** | [**AuditUpdateRequest**](AuditUpdateRequest.md)|  | [required] 

### Return type

[**AuditUpdateResponse**](AuditUpdateResponse.md)

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

# **get_latest_runs**
> List[ProcessInformation] getLatestRuns = get_latest_runs()

[EARLY ACCESS] GetLatestRuns: Get latest run for each process

### Example

```python
api_instance = api_client_factory.build(ProcessHistoryApi)
api_response = api_instance.get_latest_runs()
pprint(api_response)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**List[ProcessInformation]**](ProcessInformation.md)

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

# **process_entry_updates**
> PagedResourceListOfProcessUpdateResult processEntryUpdates = process_entry_updates(run_id, query_request)

[EARLY ACCESS] ProcessEntryUpdates: Get process entry updates for a query

### Example

```python
api_instance = api_client_factory.build(ProcessHistoryApi)
run_id = 'run_id_example' # str
query_request = QueryRequest()
api_response = api_instance.process_entry_updates(run_id, query_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_id** | **str**|  | [required] 
 **query_request** | [**QueryRequest**](QueryRequest.md)|  | [required] 

### Return type

[**PagedResourceListOfProcessUpdateResult**](PagedResourceListOfProcessUpdateResult.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **process_history_entries**
> PagedResourceListOfProcessInformation processHistoryEntries = process_history_entries(query_request, process_name=process_name)

[EARLY ACCESS] ProcessHistoryEntries: Get process history entries

### Example

```python
api_instance = api_client_factory.build(ProcessHistoryApi)
query_request = QueryRequest()
process_name = 'process_name_example' # str (optional)
api_response = api_instance.process_history_entries(query_request, process_name=process_name)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query_request** | [**QueryRequest**](QueryRequest.md)|  | [required] 
 **process_name** | **str**|  | [optional] 

### Return type

[**PagedResourceListOfProcessInformation**](PagedResourceListOfProcessInformation.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

