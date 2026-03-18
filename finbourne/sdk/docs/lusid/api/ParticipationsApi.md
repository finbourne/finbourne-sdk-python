# lusid.ParticipationsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_participation**](ParticipationsApi.md#delete_participation) | **DELETE** /api/api/participations/{scope}/{code} | [EARLY ACCESS] DeleteParticipation: Delete participation
[**get_participation**](ParticipationsApi.md#get_participation) | **GET** /api/api/participations/{scope}/{code} | [EARLY ACCESS] GetParticipation: Get Participation
[**list_participations**](ParticipationsApi.md#list_participations) | **GET** /api/api/participations | [EARLY ACCESS] ListParticipations: List Participations
[**upsert_participations**](ParticipationsApi.md#upsert_participations) | **POST** /api/api/participations | [EARLY ACCESS] UpsertParticipations: Upsert Participation


### Example

```python
from finbourne.sdk.exceptions import ApiException
from finbourne.sdk.extensions.configuration_options import ConfigurationOptions
from finbourne.sdk.services.lusid.models import *

from finbourne.sdk.extensions import (
  SyncApiClientFactory
)

from finbourne.sdk.services.lusid.api.participations_api import ParticipationsApi

# opts = ConfigurationOptions()
# opts.total_timeout_ms = 30_000

# uncomment the below to use an api client factory with overrides
# api_client_factory = SyncApiClientFactory(opts=opts)

api_client_factory = SyncApiClientFactory()
api_instance = api_client_factory.build(ParticipationsApi)
```

---

# **delete_participation**
> DeletedEntityResponse deleteParticipation = delete_participation(scope, code)

[EARLY ACCESS] DeleteParticipation: Delete participation

Delete an participation. Deletion will be valid from the participation's creation datetime.  This means that the participation will no longer exist at any effective datetime from the asAt datetime of deletion.

### Example

```python
api_instance = api_client_factory.build(ParticipationsApi)
scope = 'scope_example' # str
code = 'code_example' # str
api_response = api_instance.delete_participation(scope, code)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The participation scope. | [required] 
 **code** | **str**| The participation&#39;s code. This, together with the scope uniquely identifies the participation to delete. | [required] 

### Return type

[**DeletedEntityResponse**](DeletedEntityResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response from deleting an participation. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_participation**
> Participation getParticipation = get_participation(scope, code, as_at=as_at, property_keys=property_keys)

[EARLY ACCESS] GetParticipation: Get Participation

Fetch a Participation that matches the specified identifier

### Example

```python
api_instance = api_client_factory.build(ParticipationsApi)
scope = 'scope_example' # str
code = 'code_example' # str
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
property_keys = ['property_keys_example'] # List[str] (optional)
api_response = api_instance.get_participation(scope, code, as_at=as_at, property_keys=property_keys)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope to which the participation belongs. | [required] 
 **code** | **str**| The participation&#39;s unique identifier. | [required] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the participation. Defaults to return the latest version of the participation if not specified. | [optional] 
 **property_keys** | [**List[str]**](str.md)| A list of property keys from the \&quot;Participation\&quot; domain to decorate onto the participation.              These take the format {domain}/{scope}/{code} e.g. \&quot;Participation/system/Name\&quot;. | [optional] 

### Return type

[**Participation**](Participation.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The participation matching the given identifier. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **list_participations**
> PagedResourceListOfParticipation listParticipations = list_participations(as_at=as_at, page=page, sort_by=sort_by, limit=limit, filter=filter, property_keys=property_keys)

[EARLY ACCESS] ListParticipations: List Participations

Fetch the last pre-AsAt date version of each Participation in scope (does not fetch the entire history).

### Example

```python
api_instance = api_client_factory.build(ParticipationsApi)
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
page = 'page_example' # str (optional)
sort_by = ['sort_by_example'] # List[str] (optional)
limit = 56 # int (optional)
filter = 'filter_example' # str (optional)
property_keys = ['property_keys_example'] # List[str] (optional)
api_response = api_instance.list_participations(as_at=as_at, page=page, sort_by=sort_by, limit=limit, filter=filter, property_keys=property_keys)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **as_at** | **datetime**| The asAt datetime at which to retrieve the participation. Defaults to return the latest version of the participation if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing participations from a previous call to list participations.              This value is returned from the previous call. If a pagination token is provided the sortBy, filter, effectiveAt, and asAt fields              must not have changed since the original request. | [optional] 
 **sort_by** | [**List[str]**](str.md)| A list of field names to sort by, each suffixed by \&quot; ASC\&quot; or \&quot; DESC\&quot; | [optional] 
 **limit** | **int**| When paginating, limit the number of returned results to this many. | [optional] 
 **filter** | **str**| Expression to filter the result set. Read more about filtering results from LUSID here:              https://support.lusid.com/filtering-results-from-lusid. | [optional] 
 **property_keys** | [**List[str]**](str.md)| A list of property keys from the \&quot;Participation\&quot; domain to decorate onto each participation.                  These take the format {domain}/{scope}/{code} e.g. \&quot;Participation/system/Name\&quot;.                  All properties, except derived properties, are returned by default, without specifying here. | [optional] 

### Return type

[**PagedResourceListOfParticipation**](PagedResourceListOfParticipation.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Participations in scope. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **upsert_participations**
> ResourceListOfParticipation upsertParticipations = upsert_participations(participation_set_request=participation_set_request)

[EARLY ACCESS] UpsertParticipations: Upsert Participation

Upsert; update existing participations with given ids, or create new participations otherwise.

### Example

```python
api_instance = api_client_factory.build(ParticipationsApi)
participation_set_request = ParticipationSetRequest()
api_response = api_instance.upsert_participations(participation_set_request=participation_set_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **participation_set_request** | [**ParticipationSetRequest**](ParticipationSetRequest.md)| The collection of participation requests. | [optional] 

### Return type

[**ResourceListOfParticipation**](ResourceListOfParticipation.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | A collection of participations. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

