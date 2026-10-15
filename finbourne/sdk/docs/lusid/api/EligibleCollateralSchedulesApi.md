# lusid.EligibleCollateralSchedulesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_eligible_collateral_schedule**](EligibleCollateralSchedulesApi.md#create_eligible_collateral_schedule) | **POST** /api/api/eligiblecollateralschedules/{scope} | [EXPERIMENTAL] CreateEligibleCollateralSchedule: Create an Eligible Collateral Schedule.
[**delete_eligible_collateral_schedule**](EligibleCollateralSchedulesApi.md#delete_eligible_collateral_schedule) | **DELETE** /api/api/eligiblecollateralschedules/{scope}/{code} | [EXPERIMENTAL] DeleteEligibleCollateralSchedule: Delete an Eligible Collateral Schedule.
[**get_eligible_collateral_schedule**](EligibleCollateralSchedulesApi.md#get_eligible_collateral_schedule) | **GET** /api/api/eligiblecollateralschedules/{scope}/{code} | [EXPERIMENTAL] GetEligibleCollateralSchedule: Get an Eligible Collateral Schedule.
[**list_eligible_collateral_schedules**](EligibleCollateralSchedulesApi.md#list_eligible_collateral_schedules) | **GET** /api/api/eligiblecollateralschedules | [EXPERIMENTAL] ListEligibleCollateralSchedules: List Eligible Collateral Schedules.
[**upsert_eligible_collateral_schedule**](EligibleCollateralSchedulesApi.md#upsert_eligible_collateral_schedule) | **PUT** /api/api/eligiblecollateralschedules/{scope}/{code} | [EXPERIMENTAL] UpsertEligibleCollateralSchedule: Upsert an Eligible Collateral Schedule.


### Example

```python
from finbourne.sdk.exceptions import ApiException
from finbourne.sdk.extensions.configuration_options import ConfigurationOptions
from finbourne.sdk.services.lusid.models import *

from finbourne.sdk.extensions import (
  SyncApiClientFactory
)

from finbourne.sdk.services.lusid.api.eligible_collateral_schedules_api import EligibleCollateralSchedulesApi

# opts = ConfigurationOptions()
# opts.total_timeout_ms = 30_000

# uncomment the below to use an api client factory with overrides
# api_client_factory = SyncApiClientFactory(opts=opts)

api_client_factory = SyncApiClientFactory()
api_instance = api_client_factory.build(EligibleCollateralSchedulesApi)
```

---

# **create_eligible_collateral_schedule**
> EligibleCollateralSchedule createEligibleCollateralSchedule = create_eligible_collateral_schedule(scope, eligible_collateral_schedule_request)

[EXPERIMENTAL] CreateEligibleCollateralSchedule: Create an Eligible Collateral Schedule.

Create a new Eligible Collateral Schedule. The scope of the schedule is in the route and its code is in the request body.

### Example

```python
api_instance = api_client_factory.build(EligibleCollateralSchedulesApi)
scope = 'scope_example' # str
eligible_collateral_schedule_request = EligibleCollateralScheduleRequest()
api_response = api_instance.create_eligible_collateral_schedule(scope, eligible_collateral_schedule_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Eligible Collateral Schedule. | [required] 
 **eligible_collateral_schedule_request** | [**EligibleCollateralScheduleRequest**](../model/EligibleCollateralScheduleRequest.md)| The definition of the Eligible Collateral Schedule. | [required] 

### Return type

[**EligibleCollateralSchedule**](../model/EligibleCollateralSchedule.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The newly created Eligible Collateral Schedule. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **delete_eligible_collateral_schedule**
> DeletedEntityResponse deleteEligibleCollateralSchedule = delete_eligible_collateral_schedule(scope, code, effective_at=effective_at)

[EXPERIMENTAL] DeleteEligibleCollateralSchedule: Delete an Eligible Collateral Schedule.

Delete an Eligible Collateral Schedule from the given effective datetime. It remains retrievable at earlier effective datetimes.

### Example

```python
api_instance = api_client_factory.build(EligibleCollateralSchedulesApi)
scope = 'scope_example' # str
code = 'code_example' # str
effective_at = 'effective_at_example' # str (optional)
api_response = api_instance.delete_eligible_collateral_schedule(scope, code, effective_at=effective_at)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Eligible Collateral Schedule to be deleted. | [required] 
 **code** | **str**| The code of the Eligible Collateral Schedule to be deleted. Together with the scope this uniquely identifies the Eligible Collateral Schedule. | [required] 
 **effective_at** | **str**| The effective datetime or cut label from which the Eligible Collateral Schedule is deleted. Defaults to the current LUSID system datetime if not specified. | [optional] 

### Return type

[**DeletedEntityResponse**](../model/DeletedEntityResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The datetime that the Eligible Collateral Schedule was deleted. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_eligible_collateral_schedule**
> EligibleCollateralSchedule getEligibleCollateralSchedule = get_eligible_collateral_schedule(scope, code, effective_at=effective_at, as_at=as_at, property_keys=property_keys)

[EXPERIMENTAL] GetEligibleCollateralSchedule: Get an Eligible Collateral Schedule.

Retrieve the definition of a particular Eligible Collateral Schedule at an effective and asAt datetime.

### Example

```python
api_instance = api_client_factory.build(EligibleCollateralSchedulesApi)
scope = 'scope_example' # str
code = 'code_example' # str
effective_at = 'effective_at_example' # str (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
property_keys = ['property_keys_example'] # List[str] (optional)
api_response = api_instance.get_eligible_collateral_schedule(scope, code, effective_at=effective_at, as_at=as_at, property_keys=property_keys)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Eligible Collateral Schedule. | [required] 
 **code** | **str**| The code of the Eligible Collateral Schedule. Together with the scope this uniquely identifies the Eligible Collateral Schedule. | [required] 
 **effective_at** | **str**| The effective datetime or cut label at which to retrieve the Eligible Collateral Schedule. Defaults to the current LUSID system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the Eligible Collateral Schedule. Defaults to returning the latest version if not specified. | [optional] 
 **property_keys** | [**List[str]**](../model/str.md)| A list of property keys from the &#39;EligibleCollateralSchedule&#39; domain to decorate onto the Eligible Collateral Schedule.              These must take the format {domain}/{scope}/{code}, for example &#39;EligibleCollateralSchedule/Manager/Id&#39;. If no properties are specified, then no properties will be returned. | [optional] 

### Return type

[**EligibleCollateralSchedule**](../model/EligibleCollateralSchedule.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested Eligible Collateral Schedule. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **list_eligible_collateral_schedules**
> PagedResourceListOfEligibleCollateralSchedule listEligibleCollateralSchedules = list_eligible_collateral_schedules(effective_at=effective_at, as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by, property_keys=property_keys)

[EXPERIMENTAL] ListEligibleCollateralSchedules: List Eligible Collateral Schedules.

List all the Eligible Collateral Schedules matching the given criteria.

### Example

```python
api_instance = api_client_factory.build(EligibleCollateralSchedulesApi)
effective_at = 'effective_at_example' # str (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
page = 'page_example' # str (optional)
limit = 56 # int (optional)
filter = 'filter_example' # str (optional)
sort_by = ['sort_by_example'] # List[str] (optional)
property_keys = ['property_keys_example'] # List[str] (optional)
api_response = api_instance.list_eligible_collateral_schedules(effective_at=effective_at, as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by, property_keys=property_keys)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **effective_at** | **str**| The effective datetime or cut label at which to list the Eligible Collateral Schedules. Defaults to the current LUSID system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to list Eligible Collateral Schedules. Defaults to returning the latest version of each Eligible Collateral Schedule if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing Eligible Collateral Schedules; this value is returned from the previous call. If a pagination token is provided, the filter and asAt fields must not have changed since the original request. | [optional] 
 **limit** | **int**| When paginating, limit the results to this number. Defaults to 100 if not specified. | [optional] 
 **filter** | **str**| Expression to filter the results. The filterable fields are Id.Scope, Id.Code, Description, Properties and Version. The rows can be filtered with a single-condition any expression on Rows over Code, Description, Selector.Kind, Selector.Currency, Selector.InstrumentFilter, ValuationPercentage, FxHaircut, MinResidualMaturityYears or MaxResidualMaturityYears. For example, to filter on the schedule code, specify \&quot;Id.Code eq &#39;UsdCashAndGovies&#39;\&quot;, and to find schedules with a row for a given asset kind, specify \&quot;Rows any (Selector.Kind eq &#39;Cash&#39;)\&quot;. For more information about filtering results, see https://support.lusid.com/docs/filtering-information-retrieved-from-lusid. | [optional] 
 **sort_by** | [**List[str]**](../model/str.md)| A list of field names to sort by, each suffixed by \&quot; ASC\&quot; or \&quot; DESC\&quot;. | [optional] 
 **property_keys** | [**List[str]**](../model/str.md)| A list of property keys from the &#39;EligibleCollateralSchedule&#39; domain to decorate onto each Eligible Collateral Schedule.              These must take the format {domain}/{scope}/{code}, for example &#39;EligibleCollateralSchedule/Manager/Id&#39;. | [optional] 

### Return type

[**PagedResourceListOfEligibleCollateralSchedule**](../model/PagedResourceListOfEligibleCollateralSchedule.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested Eligible Collateral Schedules. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **upsert_eligible_collateral_schedule**
> EligibleCollateralSchedule upsertEligibleCollateralSchedule = upsert_eligible_collateral_schedule(scope, code, upsert_eligible_collateral_schedule_request)

[EXPERIMENTAL] UpsertEligibleCollateralSchedule: Upsert an Eligible Collateral Schedule.

Create or replace the full definition of an Eligible Collateral Schedule from an effective datetime. A change to the  definition becomes a new bitemporal version: the schedule as it was declared at earlier effective datetimes,  and as of earlier asAt datetimes, remains retrievable.

### Example

```python
api_instance = api_client_factory.build(EligibleCollateralSchedulesApi)
scope = 'scope_example' # str
code = 'code_example' # str
upsert_eligible_collateral_schedule_request = UpsertEligibleCollateralScheduleRequest()
api_response = api_instance.upsert_eligible_collateral_schedule(scope, code, upsert_eligible_collateral_schedule_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Eligible Collateral Schedule. | [required] 
 **code** | **str**| The code of the Eligible Collateral Schedule. Together with the scope this uniquely identifies the Eligible Collateral Schedule. | [required] 
 **upsert_eligible_collateral_schedule_request** | [**UpsertEligibleCollateralScheduleRequest**](../model/UpsertEligibleCollateralScheduleRequest.md)| The full definition of the Eligible Collateral Schedule from the effective datetime in the request, or the current LUSID system datetime if not specified. | [required] 

### Return type

[**EligibleCollateralSchedule**](../model/EligibleCollateralSchedule.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The Eligible Collateral Schedule as it stands from the effective datetime. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

