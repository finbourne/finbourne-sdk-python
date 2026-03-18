# lusid.AborApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_diary_entry**](AborApi.md#add_diary_entry) | **POST** /api/api/abor/{scope}/{code}/accountingdiary | [EXPERIMENTAL] AddDiaryEntry: Add a diary entry to the specified Abor. This would be type &#39;Other&#39;.
[**close_period**](AborApi.md#close_period) | **POST** /api/api/abor/{scope}/{code}/accountingdiary/$closeperiod | [EXPERIMENTAL] ClosePeriod: Closes or locks the current period for the given Abor.
[**create_abor**](AborApi.md#create_abor) | **POST** /api/api/abor/{scope} | [EXPERIMENTAL] CreateAbor: Create an Abor.
[**delete_abor**](AborApi.md#delete_abor) | **DELETE** /api/api/abor/{scope}/{code} | [EXPERIMENTAL] DeleteAbor: Delete an Abor.
[**delete_diary_entry**](AborApi.md#delete_diary_entry) | **DELETE** /api/api/abor/{scope}/{code}/accountingdiary/{diaryEntryCode} | [EXPERIMENTAL] DeleteDiaryEntry: Delete a diary entry type &#39;Other&#39; from the specified Abor.
[**get_abor**](AborApi.md#get_abor) | **GET** /api/api/abor/{scope}/{code} | [EXPERIMENTAL] GetAbor: Get Abor.
[**get_abor_properties**](AborApi.md#get_abor_properties) | **GET** /api/api/abor/{scope}/{code}/properties | [EXPERIMENTAL] GetAborProperties: Get Abor properties
[**get_journal_entry_lines**](AborApi.md#get_journal_entry_lines) | **POST** /api/api/abor/{scope}/{code}/journalentrylines/$query | [EXPERIMENTAL] GetJournalEntryLines: Get the Journal Entry lines for the given Abor.
[**get_trial_balance**](AborApi.md#get_trial_balance) | **POST** /api/api/abor/{scope}/{code}/trialbalance/$query | [EXPERIMENTAL] GetTrialBalance: Get the Trial Balance for the given Abor.
[**list_abors**](AborApi.md#list_abors) | **GET** /api/api/abor | [EXPERIMENTAL] ListAbors: List Abors.
[**list_diary_entries**](AborApi.md#list_diary_entries) | **GET** /api/api/abor/{scope}/{code}/accountingdiary | [EXPERIMENTAL] ListDiaryEntries: List diary entries.
[**lock_period**](AborApi.md#lock_period) | **POST** /api/api/abor/{scope}/{code}/accountingdiary/$lockperiod | [EXPERIMENTAL] LockPeriod: Locks the last Closed or given Closed Period.
[**patch_abor**](AborApi.md#patch_abor) | **PATCH** /api/api/abor/{scope}/{code} | [EXPERIMENTAL] PatchAbor: Patch Abor.
[**re_open_periods**](AborApi.md#re_open_periods) | **POST** /api/api/abor/{scope}/{code}/accountingdiary/$reopenperiods | [EXPERIMENTAL] ReOpenPeriods: Reopen periods from a seed Diary Entry Code or when not specified, the last Closed Period for the given Abor.
[**upsert_abor_properties**](AborApi.md#upsert_abor_properties) | **POST** /api/api/abor/{scope}/{code}/properties/$upsert | [EXPERIMENTAL] UpsertAborProperties: Upsert Abor properties


### Example

```python
from finbourne.sdk.exceptions import ApiException
from finbourne.sdk.extensions.configuration_options import ConfigurationOptions
from finbourne.sdk.services.lusid.models import *

from finbourne.sdk.extensions import (
  SyncApiClientFactory
)

from finbourne.sdk.services.lusid.api.abor_api import AborApi

# opts = ConfigurationOptions()
# opts.total_timeout_ms = 30_000

# uncomment the below to use an api client factory with overrides
# api_client_factory = SyncApiClientFactory(opts=opts)

api_client_factory = SyncApiClientFactory()
api_instance = api_client_factory.build(AborApi)
```

---

# **add_diary_entry**
> DiaryEntry addDiaryEntry = add_diary_entry(scope, code, diary_entry_request)

[EXPERIMENTAL] AddDiaryEntry: Add a diary entry to the specified Abor. This would be type 'Other'.

Adds a new diary entry to the specified Abor

### Example

```python
api_instance = api_client_factory.build(AborApi)
scope = 'scope_example' # str
code = 'code_example' # str
diary_entry_request = DiaryEntryRequest()
api_response = api_instance.add_diary_entry(scope, code, diary_entry_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Abor. | [required] 
 **code** | **str**| The code of the Abor. | [required] 
 **diary_entry_request** | [**DiaryEntryRequest**](DiaryEntryRequest.md)| The diary entry to add. | [required] 

### Return type

[**DiaryEntry**](DiaryEntry.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The newly added diary entry. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **close_period**
> DiaryEntry closePeriod = close_period(scope, code, close_period_diary_entry_request)

[EXPERIMENTAL] ClosePeriod: Closes or locks the current period for the given Abor.

Closes or Locks the current open period for the given Abor.

### Example

```python
api_instance = api_client_factory.build(AborApi)
scope = 'scope_example' # str
code = 'code_example' # str
close_period_diary_entry_request = ClosePeriodDiaryEntryRequest()
api_response = api_instance.close_period(scope, code, close_period_diary_entry_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Abor. | [required] 
 **code** | **str**| The code of the Abor. | [required] 
 **close_period_diary_entry_request** | [**ClosePeriodDiaryEntryRequest**](ClosePeriodDiaryEntryRequest.md)| The request body, containing details to apply to the closing/locking period. | [required] 

### Return type

[**DiaryEntry**](DiaryEntry.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The DiaryEntry created as a result of the closing of the Period. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **create_abor**
> Abor createAbor = create_abor(scope, abor_request)

[EXPERIMENTAL] CreateAbor: Create an Abor.

Create the given Abor.

### Example

```python
api_instance = api_client_factory.build(AborApi)
scope = 'scope_example' # str
abor_request = AborRequest()
api_response = api_instance.create_abor(scope, abor_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Abor. | [required] 
 **abor_request** | [**AborRequest**](AborRequest.md)| The definition of the Abor. | [required] 

### Return type

[**Abor**](Abor.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The newly created abor. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **delete_abor**
> DeletedEntityResponse deleteAbor = delete_abor(scope, code)

[EXPERIMENTAL] DeleteAbor: Delete an Abor.

Delete the given Abor.

### Example

```python
api_instance = api_client_factory.build(AborApi)
scope = 'scope_example' # str
code = 'code_example' # str
api_response = api_instance.delete_abor(scope, code)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Abor to be deleted. | [required] 
 **code** | **str**| The code of the Abor to be deleted. Together with the scope this uniquely identifies the Abor. | [required] 

### Return type

[**DeletedEntityResponse**](DeletedEntityResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The datetime that the Abor was deleted |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **delete_diary_entry**
> DeletedEntityResponse deleteDiaryEntry = delete_diary_entry(scope, code, diary_entry_code)

[EXPERIMENTAL] DeleteDiaryEntry: Delete a diary entry type 'Other' from the specified Abor.

Delete a diary entry type 'Other' from the specified Abor.

### Example

```python
api_instance = api_client_factory.build(AborApi)
scope = 'scope_example' # str
code = 'code_example' # str
diary_entry_code = 'diary_entry_code_example' # str
api_response = api_instance.delete_diary_entry(scope, code, diary_entry_code)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Abor. | [required] 
 **code** | **str**| The code of the Abor. | [required] 
 **diary_entry_code** | **str**| The diary entry code to be deleted. | [required] 

### Return type

[**DeletedEntityResponse**](DeletedEntityResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The datetime that the Cleardown Module was deleted. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_abor**
> Abor getAbor = get_abor(scope, code, effective_at=effective_at, as_at=as_at, property_keys=property_keys)

[EXPERIMENTAL] GetAbor: Get Abor.

Retrieve the definition of a particular Abor.

### Example

```python
api_instance = api_client_factory.build(AborApi)
scope = 'scope_example' # str
code = 'code_example' # str
effective_at = 'effective_at_example' # str (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
property_keys = ['property_keys_example'] # List[str] (optional)
api_response = api_instance.get_abor(scope, code, effective_at=effective_at, as_at=as_at, property_keys=property_keys)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Abor. | [required] 
 **code** | **str**| The code of the Abor. Together with the scope this uniquely identifies the Abor. | [required] 
 **effective_at** | **str**| The effective datetime or cut label at which to retrieve the Abor properties. Defaults to the current LUSID system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the Abor definition. Defaults to returning the latest version of the Abor definition if not specified. | [optional] 
 **property_keys** | [**List[str]**](str.md)| A list of property keys from the &#39;Abor&#39; domain to decorate onto the Abor.              These must take the format {domain}/{scope}/{code}, for example &#39;Abor/Manager/Id&#39;. If no properties are specified, then no properties will be returned. | [optional] 

### Return type

[**Abor**](Abor.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested Abor definition. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_abor_properties**
> AborProperties getAborProperties = get_abor_properties(scope, code, effective_at=effective_at, as_at=as_at)

[EXPERIMENTAL] GetAborProperties: Get Abor properties

Get all the properties of a single abor.

### Example

```python
api_instance = api_client_factory.build(AborApi)
scope = 'scope_example' # str
code = 'code_example' # str
effective_at = 'effective_at_example' # str (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
api_response = api_instance.get_abor_properties(scope, code, effective_at=effective_at, as_at=as_at)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Abor to list the properties for. | [required] 
 **code** | **str**| The code of the Abor to list the properties for. Together with the scope this uniquely identifies the Abor. | [required] 
 **effective_at** | **str**| The effective datetime or cut label at which to list the Abor&#39;s properties. Defaults to the current LUSID system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to list the Abor&#39;s properties. Defaults to return the latest version of each property if not specified. | [optional] 

### Return type

[**AborProperties**](AborProperties.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The properties of the specified abor |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_journal_entry_lines**
> VersionedResourceListOfJournalEntryLine getJournalEntryLines = get_journal_entry_lines(scope, code, journal_entry_lines_query_parameters, as_at=as_at, filter=filter, limit=limit, page=page)

[EXPERIMENTAL] GetJournalEntryLines: Get the Journal Entry lines for the given Abor.

Gets the Journal Entry lines for the given Abor                The Journal Entry lines have been generated from transactions and translated via posting rules

### Example

```python
api_instance = api_client_factory.build(AborApi)
scope = 'scope_example' # str
code = 'code_example' # str
journal_entry_lines_query_parameters = JournalEntryLinesQueryParameters()
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
filter = 'filter_example' # str (optional)
limit = 56 # int (optional)
page = 'page_example' # str (optional)
api_response = api_instance.get_journal_entry_lines(scope, code, journal_entry_lines_query_parameters, as_at=as_at, filter=filter, limit=limit, page=page)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Abor. | [required] 
 **code** | **str**| The code of the Abor. Together with the scope is creating the unique identifier for the given Abor. | [required] 
 **journal_entry_lines_query_parameters** | [**JournalEntryLinesQueryParameters**](JournalEntryLinesQueryParameters.md)| The query parameters used in running the generation of the Journal Entry lines. | [required] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve Journal Entry lines. Defaults to returning the latest version               of each transaction if not specified. | [optional] 
 **filter** | **str**| \&quot;Expression to filter the result set.\&quot; | [optional] 
 **limit** | **int**| When paginating, limit the number of returned results to this many. Defaults to 100 if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing Journal Entry lines from a previous call to GetJournalEntryLines. | [optional] 

### Return type

[**VersionedResourceListOfJournalEntryLine**](VersionedResourceListOfJournalEntryLine.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested Journal Entry lines for the specified Abor. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_trial_balance**
> VersionedResourceListOfTrialBalance getTrialBalance = get_trial_balance(scope, code, trial_balance_query_parameters, as_at=as_at, filter=filter, limit=limit, page=page)

[EXPERIMENTAL] GetTrialBalance: Get the Trial Balance for the given Abor.

Gets the Trial Balance for the given Abor.    The Trial Balance has been generated from transactions, translated via Posting Rules  and aggregated based on a General Ledger Profile (where specified).

### Example

```python
api_instance = api_client_factory.build(AborApi)
scope = 'scope_example' # str
code = 'code_example' # str
trial_balance_query_parameters = TrialBalanceQueryParameters()
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
filter = 'filter_example' # str (optional)
limit = 56 # int (optional)
page = 'page_example' # str (optional)
api_response = api_instance.get_trial_balance(scope, code, trial_balance_query_parameters, as_at=as_at, filter=filter, limit=limit, page=page)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Abor. | [required] 
 **code** | **str**| The code of the Abor. Together with the scope this uniquely identifies the Abor. | [required] 
 **trial_balance_query_parameters** | [**TrialBalanceQueryParameters**](TrialBalanceQueryParameters.md)| The query parameters used in running the generation of the Trial Balance. | [required] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the Trial Balance.              Defaults to returning the latest version if not specified. | [optional] 
 **filter** | **str**| Expression to filter the results by.              For more information about filtering results, see https://support.lusid.com/knowledgebase/article/KA-01914. | [optional] 
 **limit** | **int**| When paginating, limit the number of returned results to this many.              Defaults to 100 if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing Trial Balances.              This token is returned from the previous call.              If a pagination token is provided, the filter, effectiveAt and asAt fields              must not have changed since the original request. | [optional] 

### Return type

[**VersionedResourceListOfTrialBalance**](VersionedResourceListOfTrialBalance.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested Trial Balance for the specified Abor. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **list_abors**
> PagedResourceListOfAbor listAbors = list_abors(effective_at=effective_at, as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by, property_keys=property_keys)

[EXPERIMENTAL] ListAbors: List Abors.

List all the Abors matching particular criteria.

### Example

```python
api_instance = api_client_factory.build(AborApi)
effective_at = 'effective_at_example' # str (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
page = 'page_example' # str (optional)
limit = 56 # int (optional)
filter = 'filter_example' # str (optional)
sort_by = ['sort_by_example'] # List[str] (optional)
property_keys = ['property_keys_example'] # List[str] (optional)
api_response = api_instance.list_abors(effective_at=effective_at, as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by, property_keys=property_keys)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **effective_at** | **str**| The effective datetime or cut label at which to list the TimeVariant properties for the Abor. Defaults to the current LUSID              system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to list the Abor. Defaults to returning the latest version of each Abor if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing Abor; this              value is returned from the previous call. If a pagination token is provided, the filter, effectiveAt              and asAt fields must not have changed since the original request. | [optional] 
 **limit** | **int**| When paginating, limit the results to this number. Defaults to 100 if not specified. | [optional] 
 **filter** | **str**| Expression to filter the results.              For example, to filter on the Abor type, specify \&quot;id.Code eq &#39;Abor1&#39;\&quot;. For more information about filtering              results, see https://support.lusid.com/knowledgebase/article/KA-01914. | [optional] 
 **sort_by** | [**List[str]**](str.md)| A list of field names or properties to sort by, each suffixed by \&quot; ASC\&quot; or \&quot; DESC\&quot;. | [optional] 
 **property_keys** | [**List[str]**](str.md)| A list of property keys from the &#39;Abor&#39; domain to decorate onto each Abor.              These must take the format {domain}/{scope}/{code}, for example &#39;Abor/Manager/Id&#39;. | [optional] 

### Return type

[**PagedResourceListOfAbor**](PagedResourceListOfAbor.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested abors. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **list_diary_entries**
> PagedResourceListOfDiaryEntry listDiaryEntries = list_diary_entries(scope, code, effective_at=effective_at, as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by, property_keys=property_keys)

[EXPERIMENTAL] ListDiaryEntries: List diary entries.

List all the diary entries matching particular criteria.

### Example

```python
api_instance = api_client_factory.build(AborApi)
scope = 'scope_example' # str
code = 'code_example' # str
effective_at = 'effective_at_example' # str (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
page = 'page_example' # str (optional)
limit = 56 # int (optional)
filter = 'filter_example' # str (optional)
sort_by = ['sort_by_example'] # List[str] (optional)
property_keys = ['property_keys_example'] # List[str] (optional)
api_response = api_instance.list_diary_entries(scope, code, effective_at=effective_at, as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by, property_keys=property_keys)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Abor. | [required] 
 **code** | **str**| The code of the Abor. | [required] 
 **effective_at** | **str**| The effective datetime or cut label at which to list the TimeVariant properties for the Diary Entries. Defaults to the current LUSID              system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to list the DiaryEntry. Defaults to returning the latest version of each DiaryEntry if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing diary entries; this              value is returned from the previous call. If a pagination token is provided, the filter, effectiveAt              and asAt fields must not have changed since the original request. | [optional] 
 **limit** | **int**| When paginating, limit the results to this number. Defaults to 100 if not specified. | [optional] 
 **filter** | **str**| Expression to filter the results.              For example, to filter on the DiaryEntry type, specify \&quot;type eq &#39;PeriodBoundary&#39;\&quot;. For more information about filtering              results, see https://support.lusid.com/knowledgebase/article/KA-01914. | [optional] 
 **sort_by** | [**List[str]**](str.md)| A list of field names or properties to sort by, each suffixed by \&quot; ASC\&quot; or \&quot; DESC\&quot;. | [optional] 
 **property_keys** | [**List[str]**](str.md)| A list of property keys from the &#39;DiaryEntry&#39; domain to decorate onto each DiaryEntry.              These must take the format {domain}/{scope}/{code}, for example &#39;DiaryEntry/Report/Id&#39;. | [optional] 

### Return type

[**PagedResourceListOfDiaryEntry**](PagedResourceListOfDiaryEntry.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested diary entries. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **lock_period**
> DiaryEntry lockPeriod = lock_period(scope, code, lock_period_diary_entry_request=lock_period_diary_entry_request)

[EXPERIMENTAL] LockPeriod: Locks the last Closed or given Closed Period.

Locks the specified or last locked period for the given Abor.

### Example

```python
api_instance = api_client_factory.build(AborApi)
scope = 'scope_example' # str
code = 'code_example' # str
lock_period_diary_entry_request = LockPeriodDiaryEntryRequest()
api_response = api_instance.lock_period(scope, code, lock_period_diary_entry_request=lock_period_diary_entry_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Abor. | [required] 
 **code** | **str**| The code of the Abor. | [required] 
 **lock_period_diary_entry_request** | [**LockPeriodDiaryEntryRequest**](LockPeriodDiaryEntryRequest.md)| The request body, detailing lock details | [optional] 

### Return type

[**DiaryEntry**](DiaryEntry.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated DiaryEntry as a result of the locking of the Period. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **patch_abor**
> Abor patchAbor = patch_abor(scope, code, operation)

[EXPERIMENTAL] PatchAbor: Patch Abor.

Create or update certain fields for a particular Abor.  The behaviour is defined by the JSON Patch specification.    Currently supported fields are: PortfolioIds.

### Example

```python
api_instance = api_client_factory.build(AborApi)
scope = 'scope_example' # str
code = 'code_example' # str
operation = [{"value":[{"scope":"UKScope","code":"Portfolio1","portfolioEntityType":"SinglePortfolio"},{"scope":"UKScope","code":"Portfolio2","portfolioEntityType":"SinglePortfolio"}],"path":"/portfolioids","op":"add"}] # List[Operation]
api_response = api_instance.patch_abor(scope, code, operation)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Abor. | [required] 
 **code** | **str**| The code of the Abor. Together with the              scope this uniquely identifies the Abor. | [required] 
 **operation** | [**List[Operation]**](Operation.md)| The json patch document. For more information see: https://datatracker.ietf.org/doc/html/rfc6902. | [required] 

### Return type

[**Abor**](Abor.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The newly patched Abor |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **re_open_periods**
> PeriodDiaryEntriesReopenedResponse reOpenPeriods = re_open_periods(scope, code, re_open_period_diary_entry_request=re_open_period_diary_entry_request)

[EXPERIMENTAL] ReOpenPeriods: Reopen periods from a seed Diary Entry Code or when not specified, the last Closed Period for the given Abor.

Reopens one or more periods.

### Example

```python
api_instance = api_client_factory.build(AborApi)
scope = 'scope_example' # str
code = 'code_example' # str
re_open_period_diary_entry_request = ReOpenPeriodDiaryEntryRequest()
api_response = api_instance.re_open_periods(scope, code, re_open_period_diary_entry_request=re_open_period_diary_entry_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Abor. | [required] 
 **code** | **str**| The code of the Abor. Together with the scope this uniquely identifies the Abor. | [required] 
 **re_open_period_diary_entry_request** | [**ReOpenPeriodDiaryEntryRequest**](ReOpenPeriodDiaryEntryRequest.md)| The request body, containing details about the period to be re-opened. | [optional] 

### Return type

[**PeriodDiaryEntriesReopenedResponse**](PeriodDiaryEntriesReopenedResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The datetime that the DiaryEntryCodes were deleted |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **upsert_abor_properties**
> AborProperties upsertAborProperties = upsert_abor_properties(scope, code, request_body=request_body)

[EXPERIMENTAL] UpsertAborProperties: Upsert Abor properties

Update or insert one or more properties onto a single Abor. A property will be updated if it  already exists and inserted if it does not. All properties must be of the domain 'Abor'.                Upserting a property that exists for an Abor, with a null value, will delete the instance of the property for that group.                Properties have an <i>effectiveFrom</i> datetime for which the property is valid, and an <i>effectiveUntil</i>  datetime until which the property is valid. Not supplying an <i>effectiveUntil</i> datetime results in the property being  valid indefinitely, or until the next <i>effectiveFrom</i> datetime of the property.

### Example

```python
api_instance = api_client_factory.build(AborApi)
scope = 'scope_example' # str
code = 'code_example' # str
request_body = {"Abor/MyScope/FundManagerName":{"key":"Abor/MyScope/FundManagerName","value":{"labelValue":"Smith"},"effectiveFrom":"2018-03-05T00:00:00.0000000+00:00"},"Abor/MyScope/SomeProperty":{"key":"Abor/MyScope/SomeProperty","value":{"labelValue":"SomeValue"},"effectiveFrom":"2016-01-01T00:00:00.0000000+00:00"},"Abor/MyScope/AnotherProperty":{"key":"Abor/MyScope/AnotherProperty","value":{"labelValue":"AnotherValue"},"effectiveFrom":"2018-03-05T00:00:00.0000000+00:00","effectiveUntil":"2020-01-01T00:00:00.0000000+00:00"},"Abor/MyScope/ReBalanceInterval":{"key":"Abor/MyScope/ReBalanceInterval","value":{"metricValue":{"value":30.0,"unit":"Days"}}}} # Dict[str, ModelProperty] (optional)
api_response = api_instance.upsert_abor_properties(scope, code, request_body=request_body)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Abor to update or insert the properties onto. | [required] 
 **code** | **str**| The code of the Abor to update or insert the properties onto. Together with the scope this uniquely identifies the Abor. | [required] 
 **request_body** | [**Dict[str, ModelProperty]**](ModelProperty.md)| The properties to be updated or inserted onto the Abor. Each property in               the request must be keyed by its unique property key. This has the format {domain}/{scope}/{code} e.g. \&quot;Abor/Manager/Id\&quot;. | [optional] 

### Return type

[**AborProperties**](AborProperties.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated or inserted properties |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

