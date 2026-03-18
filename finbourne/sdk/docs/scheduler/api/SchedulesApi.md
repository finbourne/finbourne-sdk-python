# scheduler.SchedulesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_schedule**](SchedulesApi.md#create_schedule) | **POST** /scheduler2/api/schedules | CreateSchedule: Create a Schedule for a job
[**delete_schedule**](SchedulesApi.md#delete_schedule) | **DELETE** /scheduler2/api/schedules/{scope}/{code} | DeleteSchedule: Delete a schedule
[**enabled_schedule**](SchedulesApi.md#enabled_schedule) | **PUT** /scheduler2/api/schedules/{scope}/{code}/enabled | EnabledSchedule: Enable/disable a schedule
[**get_schedule**](SchedulesApi.md#get_schedule) | **GET** /scheduler2/api/schedules/{scope}/{code} | GetSchedule: Get a single Schedule
[**get_valid_timezones**](SchedulesApi.md#get_valid_timezones) | **GET** /scheduler2/api/schedules/timezones | GetValidTimezones: Get a list of valid timezones
[**list_schedules**](SchedulesApi.md#list_schedules) | **GET** /scheduler2/api/schedules | ListSchedules: List the available Schedules
[**run_schedule**](SchedulesApi.md#run_schedule) | **POST** /scheduler2/api/schedules/{scope}/{code}/$run | RunSchedule: Run a schedule immediately
[**update_schedule**](SchedulesApi.md#update_schedule) | **PUT** /scheduler2/api/schedules/{scope}/{code} | UpdateSchedule: Update a schedule.


### Example

```python
from finbourne.sdk.exceptions import ApiException
from finbourne.sdk.extensions.configuration_options import ConfigurationOptions
from finbourne.sdk.services.scheduler.models import *

from finbourne.sdk.extensions import (
  SyncApiClientFactory
)

from finbourne.sdk.services.scheduler.api.schedules_api import SchedulesApi

# opts = ConfigurationOptions()
# opts.total_timeout_ms = 30_000

# uncomment the below to use an api client factory with overrides
# api_client_factory = SyncApiClientFactory(opts=opts)

api_client_factory = SyncApiClientFactory()
api_instance = api_client_factory.build(SchedulesApi)
```

---

# **create_schedule**
> ScheduleDefinition createSchedule = create_schedule(create_schedule_request)

CreateSchedule: Create a Schedule for a job

### Example

```python
api_instance = api_client_factory.build(SchedulesApi)
create_schedule_request = CreateScheduleRequest()
api_response = api_instance.create_schedule(create_schedule_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_schedule_request** | [**CreateScheduleRequest**](CreateScheduleRequest.md)|  | [required] 

### Return type

[**ScheduleDefinition**](ScheduleDefinition.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The newly created schedule |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **delete_schedule**
> deleteSchedule = delete_schedule(scope, code)

DeleteSchedule: Delete a schedule

### Example

```python
api_instance = api_client_factory.build(SchedulesApi)
scope = 'scope_example' # str
code = 'code_example' # str
api_instance.delete_schedule(scope, code)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| Scope of the schedule to be deleted | [required] 
 **code** | **str**| Code of the schedule to be deleted | [required] 

### Return type

void (empty response body)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **enabled_schedule**
> ScheduleDefinition enabledSchedule = enabled_schedule(scope, code, enable)

EnabledSchedule: Enable/disable a schedule

### Example

```python
api_instance = api_client_factory.build(SchedulesApi)
scope = 'scope_example' # str
code = 'code_example' # str
enable = True # bool
api_response = api_instance.enabled_schedule(scope, code, enable)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| Scope of the schedule to be enabled/disabled | [required] 
 **code** | **str**| Code of the schedule to be enabled/disabled | [required] 
 **enable** | **bool**| Specify whether to enable or disable the schedule | [required] 

### Return type

[**ScheduleDefinition**](ScheduleDefinition.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_schedule**
> ScheduleDefinition getSchedule = get_schedule(scope, code)

GetSchedule: Get a single Schedule

### Example

```python
api_instance = api_client_factory.build(SchedulesApi)
scope = 'scope_example' # str
code = 'code_example' # str
api_response = api_instance.get_schedule(scope, code)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of Schedule | [required] 
 **code** | **str**| The code of the Schedule | [required] 

### Return type

[**ScheduleDefinition**](ScheduleDefinition.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_valid_timezones**
> ResourceListOfString getValidTimezones = get_valid_timezones()

GetValidTimezones: Get a list of valid timezones

### Example

```python
api_instance = api_client_factory.build(SchedulesApi)
api_response = api_instance.get_valid_timezones()
pprint(api_response)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ResourceListOfString**](ResourceListOfString.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **list_schedules**
> ResourceListOfScheduleDefinition listSchedules = list_schedules(page=page, sort_by=sort_by, start=start, limit=limit, filter=filter)

ListSchedules: List the available Schedules

### Example

```python
api_instance = api_client_factory.build(SchedulesApi)
page = 'page_example' # str (optional)
sort_by = ['sort_by_example'] # List[str] (optional)
start = 56 # int (optional)
limit = 2000 # int (optional)
filter = 'filter_example' # str (optional)
api_response = api_instance.list_schedules(page=page, sort_by=sort_by, start=start, limit=limit, filter=filter)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **str**| The pagination token to use to continue listing instruments from a previous call to list instruments.             This value is returned from the previous call. If a pagination token is provided the sortBy and filter fields             must not have changed since the original request. Also, if set, a start value cannot be provided. | [optional] 
 **sort_by** | [**List[str]**](str.md)| Order the results by these fields. Use use the &#39;-&#39; sign to denote descending order e.g. -MyFieldName. | [optional] 
 **start** | **int**| When paginating, skip this number of results. | [optional] 
 **limit** | **int**| When paginating, limit the number of returned results to this many. Defaults to 2000 if not specified. Maximum is 5000. | [optional] [default to 2000]
 **filter** | **str**| Expression to filter the result set. | [optional] 

### Return type

[**ResourceListOfScheduleDefinition**](ResourceListOfScheduleDefinition.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **run_schedule**
> StartScheduleResponse runSchedule = run_schedule(scope, code)

RunSchedule: Run a schedule immediately

### Example

```python
api_instance = api_client_factory.build(SchedulesApi)
scope = 'scope_example' # str
code = 'code_example' # str
api_response = api_instance.run_schedule(scope, code)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The schedule scope | [required] 
 **code** | **str**| The schedule cde | [required] 

### Return type

[**StartScheduleResponse**](StartScheduleResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **update_schedule**
> ScheduleDefinition updateSchedule = update_schedule(scope, code, update_schedule_request)

UpdateSchedule: Update a schedule.

### Example

```python
api_instance = api_client_factory.build(SchedulesApi)
scope = 'scope_example' # str
code = 'code_example' # str
update_schedule_request = UpdateScheduleRequest()
api_response = api_instance.update_schedule(scope, code, update_schedule_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| Scope of the schedule to be updated | [required] 
 **code** | **str**| Code of the schedule to be updated | [required] 
 **update_schedule_request** | [**UpdateScheduleRequest**](UpdateScheduleRequest.md)| The updated schedule | [required] 

### Return type

[**ScheduleDefinition**](ScheduleDefinition.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

