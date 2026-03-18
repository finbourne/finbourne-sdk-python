# lusid.TimelinesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**confirm_closed_period**](TimelinesApi.md#confirm_closed_period) | **POST** /api/api/timelines/{scope}/{code}/closedperiods/{closedPeriodId}/$confirm | [EXPERIMENTAL] ConfirmClosedPeriod: Confirm a Closed Period against a Timeline Entity
[**create_closed_period**](TimelinesApi.md#create_closed_period) | **POST** /api/api/timelines/{scope}/{code}/closedperiods | [EXPERIMENTAL] CreateClosedPeriod: Create a new closed period against a timeline entity
[**create_closed_period_candidate**](TimelinesApi.md#create_closed_period_candidate) | **POST** /api/api/timelines/{scope}/{code}/closedperiods/candidate | [EXPERIMENTAL] CreateClosedPeriodCandidate: Create a new closed period candidate against a timeline entity
[**create_timeline**](TimelinesApi.md#create_timeline) | **POST** /api/api/timelines | [EXPERIMENTAL] CreateTimeline: Create a Timeline
[**delete_timeline**](TimelinesApi.md#delete_timeline) | **DELETE** /api/api/timelines/{scope}/{code} | [EXPERIMENTAL] DeleteTimeline: Deletes a particular Timeline
[**get_closed_period**](TimelinesApi.md#get_closed_period) | **GET** /api/api/timelines/{scope}/{code}/closedperiods/{closedPeriodId} | [EXPERIMENTAL] GetClosedPeriod: Gets a Closed Period entity.
[**get_timeline**](TimelinesApi.md#get_timeline) | **GET** /api/api/timelines/{scope}/{code} | [EXPERIMENTAL] GetTimeline: Get a single Timeline by scope and code.
[**list_closed_periods**](TimelinesApi.md#list_closed_periods) | **GET** /api/api/timelines/{scope}/{code}/closedperiods | [EXPERIMENTAL] ListClosedPeriods: List ClosedPeriods for a specified Timeline.
[**list_timelines**](TimelinesApi.md#list_timelines) | **GET** /api/api/timelines | [EXPERIMENTAL] ListTimelines: List Timelines
[**set_post_close_activity**](TimelinesApi.md#set_post_close_activity) | **POST** /api/api/timelines/{scope}/{code}/closedperiods/{closedPeriodId}/postcloseactivity | [EXPERIMENTAL] SetPostCloseActivity: Sets post-close activities to a Closed Period.
[**unconfirm_closed_period**](TimelinesApi.md#unconfirm_closed_period) | **POST** /api/api/timelines/{scope}/{code}/closedperiods/{closedPeriodId}/$unconfirm | [EXPERIMENTAL] UnconfirmClosedPeriod: Unconfirm the last confirmed Closed Period against a Timeline Entity
[**update_timeline**](TimelinesApi.md#update_timeline) | **PUT** /api/api/timelines/{scope}/{code} | [EXPERIMENTAL] UpdateTimeline: Update Timeline defined by scope and code


### Example

```python
from finbourne.sdk.exceptions import ApiException
from finbourne.sdk.extensions.configuration_options import ConfigurationOptions
from finbourne.sdk.services.lusid.models import *

from finbourne.sdk.extensions import (
  SyncApiClientFactory
)

from finbourne.sdk.services.lusid.api.timelines_api import TimelinesApi

# opts = ConfigurationOptions()
# opts.total_timeout_ms = 30_000

# uncomment the below to use an api client factory with overrides
# api_client_factory = SyncApiClientFactory(opts=opts)

api_client_factory = SyncApiClientFactory()
api_instance = api_client_factory.build(TimelinesApi)
```

---

# **confirm_closed_period**
> ClosedPeriod confirmClosedPeriod = confirm_closed_period(scope, code, closed_period_id, body=body)

[EXPERIMENTAL] ConfirmClosedPeriod: Confirm a Closed Period against a Timeline Entity

Confirms a Closed Period against a Timeline Entity. Deletes any other unconfirmed Closed Periods on the Timeline.

### Example

```python
api_instance = api_client_factory.build(TimelinesApi)
scope = 'scope_example' # str
code = 'code_example' # str
closed_period_id = 'closed_period_id_example' # str
body = {} # object (optional)
api_response = api_instance.confirm_closed_period(scope, code, closed_period_id, body=body)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the specified Timeline. | [required] 
 **code** | **str**| The code of the specified Timeline. Together with the scope this uniquely identifies the Timeline. | [required] 
 **closed_period_id** | **str**| The id of the Closed Period. Together with the scope and code of the Timeline,              this uniquely identifies the ClosedPeriod | [required] 
 **body** | **object**| Not in use at the moment | [optional] 

### Return type

[**ClosedPeriod**](ClosedPeriod.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The confirmed closed period |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **create_closed_period**
> ClosedPeriod createClosedPeriod = create_closed_period(scope, code, create_closed_period_request=create_closed_period_request)

[EXPERIMENTAL] CreateClosedPeriod: Create a new closed period against a timeline entity

Creates a new closed period against a timeline entity  Returns the newly created closed period entity with properties

### Example

```python
api_instance = api_client_factory.build(TimelinesApi)
scope = 'scope_example' # str
code = 'code_example' # str
create_closed_period_request = CreateClosedPeriodRequest()
api_response = api_instance.create_closed_period(scope, code, create_closed_period_request=create_closed_period_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the specified Timeline. | [required] 
 **code** | **str**| The code of the specified Timeline. Together with the domain and scope this uniquely identifies the Timeline. | [required] 
 **create_closed_period_request** | [**CreateClosedPeriodRequest**](CreateClosedPeriodRequest.md)| The request containing the details of the Closed Period | [optional] 

### Return type

[**ClosedPeriod**](ClosedPeriod.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The created closed period |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **create_closed_period_candidate**
> ClosedPeriod createClosedPeriodCandidate = create_closed_period_candidate(scope, code, create_closed_period_request=create_closed_period_request)

[EXPERIMENTAL] CreateClosedPeriodCandidate: Create a new closed period candidate against a timeline entity

Creates a new closed period candidate against a timeline entity  Returns the newly created closed period candidate entity with properties

### Example

```python
api_instance = api_client_factory.build(TimelinesApi)
scope = 'scope_example' # str
code = 'code_example' # str
create_closed_period_request = CreateClosedPeriodRequest()
api_response = api_instance.create_closed_period_candidate(scope, code, create_closed_period_request=create_closed_period_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the specified Timeline. | [required] 
 **code** | **str**| The code of the specified Timeline. Together with the scope this uniquely identifies the Timeline. | [required] 
 **create_closed_period_request** | [**CreateClosedPeriodRequest**](CreateClosedPeriodRequest.md)| The request containing the details of the Closed Period | [optional] 

### Return type

[**ClosedPeriod**](ClosedPeriod.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The created closed period |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **create_timeline**
> Timeline createTimeline = create_timeline(create_timeline_request=create_timeline_request)

[EXPERIMENTAL] CreateTimeline: Create a Timeline

Creates a Timeline. Returns the created Timeline at the current effectiveAt.  Note that Timelines are mono-temporal, however they can have Time-Variant Properties.  Upserted Properties will be returned at the latest AsAt and EffectiveAt

### Example

```python
api_instance = api_client_factory.build(TimelinesApi)
create_timeline_request = CreateTimelineRequest()
api_response = api_instance.create_timeline(create_timeline_request=create_timeline_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_timeline_request** | [**CreateTimelineRequest**](CreateTimelineRequest.md)| The request containing the details of the Timeline | [optional] 

### Return type

[**Timeline**](Timeline.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The created Timeline |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **delete_timeline**
> DeletedEntityResponse deleteTimeline = delete_timeline(scope, code)

[EXPERIMENTAL] DeleteTimeline: Deletes a particular Timeline

The deletion will take effect from the Timeline deletion datetime.  i.e. will no longer exist at any asAt datetime after the asAt datetime of deletion.

### Example

```python
api_instance = api_client_factory.build(TimelinesApi)
scope = 'scope_example' # str
code = 'code_example' # str
api_response = api_instance.delete_timeline(scope, code)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the specified Timeline. | [required] 
 **code** | **str**| The code of the specified Timeline. Together with the domain and scope this uniquely              identifies the Timeline. | [required] 

### Return type

[**DeletedEntityResponse**](DeletedEntityResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The deleted entity metadata |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_closed_period**
> ClosedPeriod getClosedPeriod = get_closed_period(scope, code, closed_period_id, as_at=as_at, property_keys=property_keys)

[EXPERIMENTAL] GetClosedPeriod: Gets a Closed Period entity.

Retrieves one ClosedPeriod uniquely defined by the Timelines Scope/Code and a ClosedPeriodId.

### Example

```python
api_instance = api_client_factory.build(TimelinesApi)
scope = 'scope_example' # str
code = 'code_example' # str
closed_period_id = 'closed_period_id_example' # str
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
property_keys = ['property_keys_example'] # List[str] (optional)
api_response = api_instance.get_closed_period(scope, code, closed_period_id, as_at=as_at, property_keys=property_keys)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Timeline. | [required] 
 **code** | **str**| The code of the Timeline. Together with the scope this uniquely              identifies the Timeline. | [required] 
 **closed_period_id** | **str**| The id of the Closed Period. Together with the scope and code of the Timeline,              this uniquely identifies the ClosedPeriod | [required] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the ClosedPeriod definition. Defaults to return              the latest version of the definition if not specified. | [optional] 
 **property_keys** | [**List[str]**](str.md)| A list of property keys from the &#39;ClosedPeriod&#39; domain to decorate onto              the ClosedPeriod.              These must have the format {domain}/{scope}/{code}, for example &#39;ClosedPeriod/system/Name&#39;. | [optional] 

### Return type

[**ClosedPeriod**](ClosedPeriod.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested closed period |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_timeline**
> Timeline getTimeline = get_timeline(scope, code, as_at=as_at, effective_at=effective_at, property_keys=property_keys)

[EXPERIMENTAL] GetTimeline: Get a single Timeline by scope and code.

Retrieves one Timeline by scope and code.  Timelines are mono-temporal. The EffectiveAt is only applied to Time-Variant Properties.

### Example

```python
api_instance = api_client_factory.build(TimelinesApi)
scope = 'scope_example' # str
code = 'code_example' # str
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
effective_at = 'effective_at_example' # str (optional)
property_keys = ['property_keys_example'] # List[str] (optional)
api_response = api_instance.get_timeline(scope, code, as_at=as_at, effective_at=effective_at, property_keys=property_keys)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the specified Timeline. | [required] 
 **code** | **str**| The code of the specified Timeline. Together with the scope this uniquely              identifies the Timeline. | [required] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the Timeline definition. Defaults to return              the latest version of the definition if not specified. | [optional] 
 **effective_at** | **str**| The effective datetime or cut label at which to retrieve the timeline properties.              Defaults to the current LUSID system datetime if not specified. | [optional] 
 **property_keys** | [**List[str]**](str.md)| A list of property keys from the &#39;Timeline&#39; domain to decorate onto              the Timeline.              These must have the format {domain}/{scope}/{code}, for example &#39;Timeline/system/Name&#39;. | [optional] 

### Return type

[**Timeline**](Timeline.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested Timeline |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **list_closed_periods**
> PagedResourceListOfClosedPeriod listClosedPeriods = list_closed_periods(scope, code, as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by, property_keys=property_keys)

[EXPERIMENTAL] ListClosedPeriods: List ClosedPeriods for a specified Timeline.

List all the ClosedPeriods matching a particular criteria.

### Example

```python
api_instance = api_client_factory.build(TimelinesApi)
scope = 'scope_example' # str
code = 'code_example' # str
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
page = 'page_example' # str (optional)
limit = 56 # int (optional)
filter = 'filter_example' # str (optional)
sort_by = ['sort_by_example'] # List[str] (optional)
property_keys = ['property_keys_example'] # List[str] (optional)
api_response = api_instance.list_closed_periods(scope, code, as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by, property_keys=property_keys)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Timeline. | [required] 
 **code** | **str**| The code of the Timeline. | [required] 
 **as_at** | **datetime**| The asAt datetime at which to list the ClosedPeriods. Defaults to returning the latest version of each ClosedPeriod if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing ClosedPeriods; this              value is returned from the previous call. If a pagination token is provided, the filter, effectiveAt              and asAt fields must not have changed since the original request. | [optional] 
 **limit** | **int**| When paginating, limit the results to this number. Defaults to 100 if not specified. | [optional] 
 **filter** | **str**| Expression to filter the results.              For example, to filter on the effectiveEnd, specify \&quot;effectiveEnd gt 2019-01-15T10:00:00\&quot;. For more information about filtering              results, see https://support.lusid.com/knowledgebase/article/KA-01914. | [optional] 
 **sort_by** | [**List[str]**](str.md)| A list of field names or properties to sort by, each suffixed by \&quot; ASC\&quot; or \&quot; DESC\&quot; | [optional] 
 **property_keys** | [**List[str]**](str.md)| A list of property keys from the &#39;ClosedPeriod&#39; domain to decorate onto each ClosedPeriod.              These must take the format {domain}/{scope}/{code}, for example &#39;ClosedPeriod/Account/id&#39;. | [optional] 

### Return type

[**PagedResourceListOfClosedPeriod**](PagedResourceListOfClosedPeriod.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested ClosedPeriods. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **list_timelines**
> PagedResourceListOfTimeline listTimelines = list_timelines(as_at=as_at, effective_at=effective_at, page=page, limit=limit, filter=filter, sort_by=sort_by, property_keys=property_keys)

[EXPERIMENTAL] ListTimelines: List Timelines

List all the Timelines matching a particular criteria.

### Example

```python
api_instance = api_client_factory.build(TimelinesApi)
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
effective_at = 'effective_at_example' # str (optional)
page = 'page_example' # str (optional)
limit = 56 # int (optional)
filter = 'filter_example' # str (optional)
sort_by = ['sort_by_example'] # List[str] (optional)
property_keys = ['property_keys_example'] # List[str] (optional)
api_response = api_instance.list_timelines(as_at=as_at, effective_at=effective_at, page=page, limit=limit, filter=filter, sort_by=sort_by, property_keys=property_keys)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **as_at** | **datetime**| The asAt datetime at which to list the Timelines. Defaults to returning the latest version of each Timeline if not specified. | [optional] 
 **effective_at** | **str**| The effective datetime or cut label at which to list the Timelines.              Note that Timelines are monotemporal, the effectiveAt is for Timevariant Properties on the Timeline only.              Defaults to the current LUSID system datetime if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing Timelines; this              value is returned from the previous call. If a pagination token is provided, the filter, effectiveAt              and asAt fields must not have changed since the original request. | [optional] 
 **limit** | **int**| When paginating, limit the results to this number. Defaults to 100 if not specified. | [optional] 
 **filter** | **str**| Expression to filter the results.              For example, to filter on the displayName, specify \&quot;displayName eq &#39;AccountingTimeline&#39;\&quot;. For more information about filtering              results, see https://support.lusid.com/knowledgebase/article/KA-01914. | [optional] 
 **sort_by** | [**List[str]**](str.md)| A list of field names or properties to sort by, each suffixed by \&quot; ASC\&quot; or \&quot; DESC\&quot; | [optional] 
 **property_keys** | [**List[str]**](str.md)| A list of property keys from the &#39;Timeline&#39; domain to decorate onto each Timeline.              These must take the format {domain}/{scope}/{code}, for example &#39;Timeline/Account/id&#39;. | [optional] 

### Return type

[**PagedResourceListOfTimeline**](PagedResourceListOfTimeline.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested Timelines. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **set_post_close_activity**
> ClosedPeriod setPostCloseActivity = set_post_close_activity(scope, code, closed_period_id, post_close_activities_request=post_close_activities_request)

[EXPERIMENTAL] SetPostCloseActivity: Sets post-close activities to a Closed Period.

This sets the given post-close activities to the given Closed Period.                **This is an overwriting action!**                The possible types of entity are:  * `PortfolioTransaction`,  * `Instrument`,  * `InstrumentEvent`,  * `InstrumentEventInstruction`,  * `PortfolioSettlementInstruction`, and,  * `Quote`.

### Example

```python
api_instance = api_client_factory.build(TimelinesApi)
scope = 'scope_example' # str
code = 'code_example' # str
closed_period_id = 'closed_period_id_example' # str
post_close_activities_request = PostCloseActivitiesRequest()
api_response = api_instance.set_post_close_activity(scope, code, closed_period_id, post_close_activities_request=post_close_activities_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Timeline. | [required] 
 **code** | **str**| The code of the Timeline. | [required] 
 **closed_period_id** | **str**| The ID of the Closed Period.               This ID together with the scope and code of the Timeline uniquely defines the Closed Period. | [required] 
 **post_close_activities_request** | [**PostCloseActivitiesRequest**](PostCloseActivitiesRequest.md)| This specifies a collection of post-close activities. | [optional] 

### Return type

[**ClosedPeriod**](ClosedPeriod.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated Closed Period. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **unconfirm_closed_period**
> ClosedPeriod unconfirmClosedPeriod = unconfirm_closed_period(scope, code, closed_period_id, body=body)

[EXPERIMENTAL] UnconfirmClosedPeriod: Unconfirm the last confirmed Closed Period against a Timeline Entity

Unconfirm the last confirmed Closed Period against a Timeline Entity

### Example

```python
api_instance = api_client_factory.build(TimelinesApi)
scope = 'scope_example' # str
code = 'code_example' # str
closed_period_id = 'closed_period_id_example' # str
body = {} # object (optional)
api_response = api_instance.unconfirm_closed_period(scope, code, closed_period_id, body=body)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the specified Timeline. | [required] 
 **code** | **str**| The code of the specified Timeline. Together with the scope this uniquely identifies the Timeline. | [required] 
 **closed_period_id** | **str**| The id of the Closed Period. Together with the scope and code of the Timeline,              this uniquely identifies the ClosedPeriod. The closed period must be the last closed period on the Timeline. | [required] 
 **body** | **object**| Not in use at the moment | [optional] 

### Return type

[**ClosedPeriod**](ClosedPeriod.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The unconfirmed closed period |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **update_timeline**
> Timeline updateTimeline = update_timeline(scope, code, update_timeline_request=update_timeline_request)

[EXPERIMENTAL] UpdateTimeline: Update Timeline defined by scope and code

Overwrites an existing Timeline  Update request has the same required fields as Create apart from the id.  Returns the updated Timeline at the current effectiveAt.  Note that Timelines are mono-temporal, however they can have Time-Variant Properties.  Updated Properties will be returned at the latest AsAt and EffectiveAt

### Example

```python
api_instance = api_client_factory.build(TimelinesApi)
scope = 'scope_example' # str
code = 'code_example' # str
update_timeline_request = UpdateTimelineRequest()
api_response = api_instance.update_timeline(scope, code, update_timeline_request=update_timeline_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the specified Timeline. | [required] 
 **code** | **str**| The code of the specified Timeline. Together with the domain and scope this uniquely identifies the Timeline. | [required] 
 **update_timeline_request** | [**UpdateTimelineRequest**](UpdateTimelineRequest.md)| The request containing the updated details of the Timeline | [optional] 

### Return type

[**Timeline**](Timeline.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated version of the requested Timeline |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

