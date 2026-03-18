# lusid.ResourceRecordApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_resource_record**](ResourceRecordApi.md#delete_resource_record) | **DELETE** /api/api/resourcerecords/{scope}/{code}/{resourceId} | [EARLY ACCESS] DeleteResourceRecord: Delete a Resource Record
[**get_resource_record**](ResourceRecordApi.md#get_resource_record) | **GET** /api/api/resourcerecords/{scope}/{code}/{resourceId} | [EARLY ACCESS] GetResourceRecord: Get a Resource Record
[**list_resource_record_codes**](ResourceRecordApi.md#list_resource_record_codes) | **GET** /api/api/resourcerecords/{scope} | [EARLY ACCESS] ListResourceRecordCodes: List Resource Records Codes for Scope
[**list_resource_record_scopes**](ResourceRecordApi.md#list_resource_record_scopes) | **GET** /api/api/resourcerecords | [EARLY ACCESS] ListResourceRecordScopes: List Resource Record Scopes
[**list_resource_records**](ResourceRecordApi.md#list_resource_records) | **GET** /api/api/resourcerecords/{scope}/{code} | [EARLY ACCESS] ListResourceRecords: List Resource Records
[**upsert_resource_record**](ResourceRecordApi.md#upsert_resource_record) | **POST** /api/api/resourcerecords | [EARLY ACCESS] UpsertResourceRecord: Upsert a Resource Record


### Example

```python
from finbourne.sdk.exceptions import ApiException
from finbourne.sdk.extensions.configuration_options import ConfigurationOptions
from finbourne.sdk.services.lusid.models import *

from finbourne.sdk.extensions import (
  SyncApiClientFactory
)

from finbourne.sdk.services.lusid.api.resource_record_api import ResourceRecordApi

# opts = ConfigurationOptions()
# opts.total_timeout_ms = 30_000

# uncomment the below to use an api client factory with overrides
# api_client_factory = SyncApiClientFactory(opts=opts)

api_client_factory = SyncApiClientFactory()
api_instance = api_client_factory.build(ResourceRecordApi)
```

---

# **delete_resource_record**
> DeletedEntityResponse deleteResourceRecord = delete_resource_record(scope, code, resource_id)

[EARLY ACCESS] DeleteResourceRecord: Delete a Resource Record

Delete a resource record.

### Example

```python
api_instance = api_client_factory.build(ResourceRecordApi)
scope = 'scope_example' # str
code = 'code_example' # str
resource_id = 'resource_id_example' # str
api_response = api_instance.delete_resource_record(scope, code, resource_id)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the resource record. | [required] 
 **code** | **str**| The code of the resource record. | [required] 
 **resource_id** | **str**| The resource identifier of the resource record. | [required] 

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

# **get_resource_record**
> ResourceRecord getResourceRecord = get_resource_record(scope, code, resource_id, as_at=as_at)

[EARLY ACCESS] GetResourceRecord: Get a Resource Record

Retrieve a resource record by its identifier.

### Example

```python
api_instance = api_client_factory.build(ResourceRecordApi)
scope = 'scope_example' # str
code = 'code_example' # str
resource_id = 'resource_id_example' # str
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
api_response = api_instance.get_resource_record(scope, code, resource_id, as_at=as_at)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the resource record. | [required] 
 **code** | **str**| The code of the resource record. | [required] 
 **resource_id** | **str**| The resource identifier of the resource record. | [required] 
 **as_at** | **datetime**| The asAt datetime at which to list the resource record. Defaults to return the latest version if not specified. | [optional] 

### Return type

[**ResourceRecord**](ResourceRecord.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested resource record. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **list_resource_record_codes**
> ResourceListOfString listResourceRecordCodes = list_resource_record_codes(scope, as_at=as_at, sort_order=sort_order)

[EARLY ACCESS] ListResourceRecordCodes: List Resource Records Codes for Scope

List all resource records matching particular criteria.

### Example

```python
api_instance = api_client_factory.build(ResourceRecordApi)
scope = 'scope_example' # str
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
sort_order = 'sort_order_example' # str (optional)
api_response = api_instance.list_resource_record_codes(scope, as_at=as_at, sort_order=sort_order)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the resource record. | [required] 
 **as_at** | **datetime**| The asAt datetime at which to list the resource record. Defaults to return the latest version if not specified. | [optional] 
 **sort_order** | **str**| Order of the sort - either \&quot;ASC\&quot; or \&quot;DESC\&quot; | [optional] 

### Return type

[**ResourceListOfString**](ResourceListOfString.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of resource record codes. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **list_resource_record_scopes**
> ResourceListOfScopeDefinition listResourceRecordScopes = list_resource_record_scopes(as_at=as_at, page=page, limit=limit)

[EARLY ACCESS] ListResourceRecordScopes: List Resource Record Scopes

List all resource records matching particular criteria.

### Example

```python
api_instance = api_client_factory.build(ResourceRecordApi)
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
page = 'page_example' # str (optional)
limit = 56 # int (optional)
api_response = api_instance.list_resource_record_scopes(as_at=as_at, page=page, limit=limit)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **as_at** | **datetime**| The asAt datetime at which to list the resource record. Defaults to return the latest version if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing resource records from a previous call. | [optional] 
 **limit** | **int**| When paginating, limit the number of returned results to this many. | [optional] 

### Return type

[**ResourceListOfScopeDefinition**](ResourceListOfScopeDefinition.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of resource records. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **list_resource_records**
> PagedResourceListOfResourceRecord listResourceRecords = list_resource_records(scope, code, as_at=as_at, page=page, sort_by=sort_by, limit=limit, filter=filter)

[EARLY ACCESS] ListResourceRecords: List Resource Records

List all resource records matching particular criteria.

### Example

```python
api_instance = api_client_factory.build(ResourceRecordApi)
scope = 'scope_example' # str
code = 'code_example' # str
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
page = 'page_example' # str (optional)
sort_by = ['sort_by_example'] # List[str] (optional)
limit = 56 # int (optional)
filter = 'filter_example' # str (optional)
api_response = api_instance.list_resource_records(scope, code, as_at=as_at, page=page, sort_by=sort_by, limit=limit, filter=filter)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the resource record. | [required] 
 **code** | **str**| The code of the resource record. | [required] 
 **as_at** | **datetime**| The asAt datetime at which to list the resource record. Defaults to return the latest version if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing resource records from a previous call. | [optional] 
 **sort_by** | [**List[str]**](str.md)| A list of field names to sort by, each suffixed by \&quot; ASC\&quot; or \&quot; DESC\&quot; | [optional] 
 **limit** | **int**| When paginating, limit the number of returned results to this many. | [optional] 
 **filter** | **str**| Expression to filter the result set. | [optional] 

### Return type

[**PagedResourceListOfResourceRecord**](PagedResourceListOfResourceRecord.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of resource records. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **upsert_resource_record**
> ResourceRecord upsertResourceRecord = upsert_resource_record(upsert_resource_record_request)

[EARLY ACCESS] UpsertResourceRecord: Upsert a Resource Record

Create or update a resource record.

### Example

```python
api_instance = api_client_factory.build(ResourceRecordApi)
upsert_resource_record_request = UpsertResourceRecordRequest()
api_response = api_instance.upsert_resource_record(upsert_resource_record_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upsert_resource_record_request** | [**UpsertResourceRecordRequest**](UpsertResourceRecordRequest.md)| The resource record to upsert. | [required] 

### Return type

[**ResourceRecord**](ResourceRecord.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The upserted resource record. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

