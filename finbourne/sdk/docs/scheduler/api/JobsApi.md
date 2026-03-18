# scheduler.JobsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_job**](JobsApi.md#create_job) | **POST** /scheduler2/api/jobs | CreateJob: Create a new job
[**delete_job**](JobsApi.md#delete_job) | **DELETE** /scheduler2/api/jobs/{scope}/{code} | DeleteJob: Delete a job
[**get_history**](JobsApi.md#get_history) | **GET** /scheduler2/api/jobs/history | GetHistory: Get the history of job runs
[**get_job_console_output**](JobsApi.md#get_job_console_output) | **GET** /scheduler2/api/jobs/history/{runId}/console | GetJobConsoleOutput: Gets the console output of a specific job run
[**get_run_history**](JobsApi.md#get_run_history) | **GET** /scheduler2/api/jobs/history/{runId} | GetRunHistory: Get the history for a single job run
[**get_schedules_for_a_job**](JobsApi.md#get_schedules_for_a_job) | **GET** /scheduler2/api/jobs/{scope}/{code}/schedules | GetSchedulesForAJob: Get all the schedules for a single job
[**list_jobs**](JobsApi.md#list_jobs) | **GET** /scheduler2/api/jobs | ListJobs: List the available jobs
[**run_job**](JobsApi.md#run_job) | **POST** /scheduler2/api/jobs/{scope}/{code}/$run | RunJob: Run a job immediately
[**update_job**](JobsApi.md#update_job) | **PUT** /scheduler2/api/jobs/{scope}/{code} | UpdateJob: Update a JobDefinition


### Example

```python
from finbourne.sdk.exceptions import ApiException
from finbourne.sdk.extensions.configuration_options import ConfigurationOptions
from finbourne.sdk.services.scheduler.models import *

from finbourne.sdk.extensions import (
  SyncApiClientFactory
)

from finbourne.sdk.services.scheduler.api.jobs_api import JobsApi

# opts = ConfigurationOptions()
# opts.total_timeout_ms = 30_000

# uncomment the below to use an api client factory with overrides
# api_client_factory = SyncApiClientFactory(opts=opts)

api_client_factory = SyncApiClientFactory()
api_instance = api_client_factory.build(JobsApi)
```

---

# **create_job**
> JobDefinition createJob = create_job(create_job_request)

CreateJob: Create a new job

### Example

```python
api_instance = api_client_factory.build(JobsApi)
create_job_request = CreateJobRequest()
api_response = api_instance.create_job(create_job_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_job_request** | [**CreateJobRequest**](CreateJobRequest.md)| The request to create a new job | [required] 

### Return type

[**JobDefinition**](JobDefinition.md)

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

# **delete_job**
> ResourceListOfScheduleDefinition deleteJob = delete_job(scope, code)

DeleteJob: Delete a job

### Example

```python
api_instance = api_client_factory.build(JobsApi)
scope = 'scope_example' # str
code = 'code_example' # str
api_response = api_instance.delete_job(scope, code)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the job | [required] 
 **code** | **str**| The code of the job | [required] 

### Return type

[**ResourceListOfScheduleDefinition**](ResourceListOfScheduleDefinition.md)

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

# **get_history**
> ResourceListOfJobHistory getHistory = get_history(page=page, sort_by=sort_by, start=start, limit=limit, filter=filter)

GetHistory: Get the history of job runs

### Example

```python
api_instance = api_client_factory.build(JobsApi)
page = 'page_example' # str (optional)
sort_by = ['sort_by_example'] # List[str] (optional)
start = 56 # int (optional)
limit = 56 # int (optional)
filter = 'filter_example' # str (optional)
api_response = api_instance.get_history(page=page, sort_by=sort_by, start=start, limit=limit, filter=filter)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **str**| The pagination token to use to continue listing instruments from a previous call to list instruments.             This value is returned from the previous call. If a pagination token is provided the sortBy and filter fields             must not have changed since the original request. Also, if set, a start value cannot be provided. | [optional] 
 **sort_by** | [**List[str]**](str.md)| Order the results by these fields. Use use the &#39;-&#39; sign to denote descending order e.g. -MyFieldName. | [optional] 
 **start** | **int**| This field is obsolete, the value of this field would not be considered. | [optional] 
 **limit** | **int**| When paginating, limit the number of returned results to this many. Defaults to 2000 if not specified. Maximum is 5000. | [optional] 
 **filter** | **str**| Expression to filter the result set. | [optional] 

### Return type

[**ResourceListOfJobHistory**](ResourceListOfJobHistory.md)

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

# **get_job_console_output**
> str getJobConsoleOutput = get_job_console_output(run_id)

GetJobConsoleOutput: Gets the console output of a specific job run

### Example

```python
api_instance = api_client_factory.build(JobsApi)
run_id = 'run_id_example' # str
api_response = api_instance.get_job_console_output(run_id)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_id** | **str**| The RunId of the job run | [required] 

### Return type

**str**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_run_history**
> JobRunResult getRunHistory = get_run_history(run_id)

GetRunHistory: Get the history for a single job run

### Example

```python
api_instance = api_client_factory.build(JobsApi)
run_id = 'run_id_example' # str
api_response = api_instance.get_run_history(run_id)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_id** | **str**| The unique ID of the run | [required] 

### Return type

[**JobRunResult**](JobRunResult.md)

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

# **get_schedules_for_a_job**
> ResourceListOfScheduleDefinition getSchedulesForAJob = get_schedules_for_a_job(scope, code)

GetSchedulesForAJob: Get all the schedules for a single job

### Example

```python
api_instance = api_client_factory.build(JobsApi)
scope = 'scope_example' # str
code = 'code_example' # str
api_response = api_instance.get_schedules_for_a_job(scope, code)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the job | [required] 
 **code** | **str**| The code of the job | [required] 

### Return type

[**ResourceListOfScheduleDefinition**](ResourceListOfScheduleDefinition.md)

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

# **list_jobs**
> ResourceListOfJobDefinition listJobs = list_jobs(page=page, sort_by=sort_by, start=start, limit=limit, filter=filter)

ListJobs: List the available jobs

### Example

```python
api_instance = api_client_factory.build(JobsApi)
page = 'page_example' # str (optional)
sort_by = ['sort_by_example'] # List[str] (optional)
start = 56 # int (optional)
limit = 2000 # int (optional)
filter = 'filter_example' # str (optional)
api_response = api_instance.list_jobs(page=page, sort_by=sort_by, start=start, limit=limit, filter=filter)
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

[**ResourceListOfJobDefinition**](ResourceListOfJobDefinition.md)

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

# **run_job**
> StartJobResponse runJob = run_job(scope, code, start_job_request)

RunJob: Run a job immediately

### Example

```python
api_instance = api_client_factory.build(JobsApi)
scope = 'scope_example' # str
code = 'code_example' # str
start_job_request = StartJobRequest()
api_response = api_instance.run_job(scope, code, start_job_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the job | [required] 
 **code** | **str**| The code of the job | [required] 
 **start_job_request** | [**StartJobRequest**](StartJobRequest.md)| The request for starting job | [required] 

### Return type

[**StartJobResponse**](StartJobResponse.md)

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

# **update_job**
> JobDefinition updateJob = update_job(scope, code, update_job_request)

UpdateJob: Update a JobDefinition

### Example

```python
api_instance = api_client_factory.build(JobsApi)
scope = 'scope_example' # str
code = 'code_example' # str
update_job_request = UpdateJobRequest()
api_response = api_instance.update_job(scope, code, update_job_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**|  | [required] 
 **code** | **str**|  | [required] 
 **update_job_request** | [**UpdateJobRequest**](UpdateJobRequest.md)|  | [required] 

### Return type

[**JobDefinition**](JobDefinition.md)

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

