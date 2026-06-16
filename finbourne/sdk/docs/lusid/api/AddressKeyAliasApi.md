# lusid.AddressKeyAliasApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_address_key_alias**](AddressKeyAliasApi.md#delete_address_key_alias) | **DELETE** /api/api/addresskeyaliases/{scope}/{code} | [EXPERIMENTAL] DeleteAddressKeyAlias: Delete an Address Key Alias, assuming that it is present.
[**get_address_key_alias**](AddressKeyAliasApi.md#get_address_key_alias) | **GET** /api/api/addresskeyaliases/{scope}/{code} | [EXPERIMENTAL] GetAddressKeyAlias: Get Address Key Alias
[**list_address_key_aliases**](AddressKeyAliasApi.md#list_address_key_aliases) | **GET** /api/api/addresskeyaliases/{scope} | [EXPERIMENTAL] ListAddressKeyAliases: List the set of Address Key Aliases
[**upsert_address_key_alias**](AddressKeyAliasApi.md#upsert_address_key_alias) | **POST** /api/api/addresskeyaliases | [EXPERIMENTAL] UpsertAddressKeyAlias: Upsert an Address Key Alias. This creates or updates the alias in LUSID.


### Example

```python
from finbourne.sdk.exceptions import ApiException
from finbourne.sdk.extensions.configuration_options import ConfigurationOptions
from finbourne.sdk.services.lusid.models import *

from finbourne.sdk.extensions import (
  SyncApiClientFactory
)

from finbourne.sdk.services.lusid.api.address_key_alias_api import AddressKeyAliasApi

# opts = ConfigurationOptions()
# opts.total_timeout_ms = 30_000

# uncomment the below to use an api client factory with overrides
# api_client_factory = SyncApiClientFactory(opts=opts)

api_client_factory = SyncApiClientFactory()
api_instance = api_client_factory.build(AddressKeyAliasApi)
```

---

# **delete_address_key_alias**
> AnnulSingleStructuredDataResponse deleteAddressKeyAlias = delete_address_key_alias(scope, code)

[EXPERIMENTAL] DeleteAddressKeyAlias: Delete an Address Key Alias, assuming that it is present.

Delete the specified Address Key Alias from a single scope.                The response will return either detail of the deleted item, or an explanation (failure) as to why this did not succeed.

### Example

```python
api_instance = api_client_factory.build(AddressKeyAliasApi)
scope = 'scope_example' # str
code = 'code_example' # str
api_response = api_instance.delete_address_key_alias(scope, code)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Address Key Alias to delete. | [required] 
 **code** | **str**| The Address Key Alias to delete. | [required] 

### Return type

[**AnnulSingleStructuredDataResponse**](AnnulSingleStructuredDataResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The AsAt of deletion or failure |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_address_key_alias**
> GetAddressKeyAliasResponse getAddressKeyAlias = get_address_key_alias(scope, code, as_at=as_at)

[EXPERIMENTAL] GetAddressKeyAlias: Get Address Key Alias

Get an Address Key Alias from a single scope.                The response will return either the alias that has been stored, or a failure explaining why the request was unsuccessful.

### Example

```python
api_instance = api_client_factory.build(AddressKeyAliasApi)
scope = 'scope_example' # str
code = 'code_example' # str
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
api_response = api_instance.get_address_key_alias(scope, code, as_at=as_at)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Address Key Alias to retrieve. | [required] 
 **code** | **str**| The code of the alias to retrieve. | [required] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the alias. Defaults to return the latest version if not specified. | [optional] 

### Return type

[**GetAddressKeyAliasResponse**](GetAddressKeyAliasResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The successfully retrieved Address Key Alias or any failure |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **list_address_key_aliases**
> PagedResourceListOfGetAddressKeyAliasResponse listAddressKeyAliases = list_address_key_aliases(scope, as_at=as_at, filter=filter, limit=limit, page=page)

[EXPERIMENTAL] ListAddressKeyAliases: List the set of Address Key Aliases

List the set of address key aliases at the specified date/time and scope.

### Example

```python
api_instance = api_client_factory.build(AddressKeyAliasApi)
scope = 'scope_example' # str
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
filter = 'filter_example' # str (optional)
limit = 56 # int (optional)
page = 'page_example' # str (optional)
api_response = api_instance.list_address_key_aliases(scope, as_at=as_at, filter=filter, limit=limit, page=page)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope to list aliases for. | [required] 
 **as_at** | **datetime**| The asAt datetime at which to list the aliases. Defaults to latest if not specified. | [optional] 
 **filter** | **str**| Expression to filter the result set. | [optional] 
 **limit** | **int**| Maximum number of results to return. Defaults to 100. | [optional] 
 **page** | **str**| Pagination token from a previous result to fetch the next page. | [optional] 

### Return type

[**PagedResourceListOfGetAddressKeyAliasResponse**](PagedResourceListOfGetAddressKeyAliasResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested address key aliases |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **upsert_address_key_alias**
> UpsertSingleStructuredDataResponse upsertAddressKeyAlias = upsert_address_key_alias(upsert_address_key_alias_request)

[EXPERIMENTAL] UpsertAddressKeyAlias: Upsert an Address Key Alias. This creates or updates the alias in LUSID.

Update or insert one Address Key Alias. An item will be updated if it already exists  and inserted if it does not.                The response will return the successfully updated or inserted alias or failure message if unsuccessful.

### Example

```python
api_instance = api_client_factory.build(AddressKeyAliasApi)
upsert_address_key_alias_request = UpsertAddressKeyAliasRequest()
api_response = api_instance.upsert_address_key_alias(upsert_address_key_alias_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upsert_address_key_alias_request** | [**UpsertAddressKeyAliasRequest**](UpsertAddressKeyAliasRequest.md)| The Address Key Alias to update or insert | [required] 

### Return type

[**UpsertSingleStructuredDataResponse**](UpsertSingleStructuredDataResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The successfully updated or inserted item or any failure |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

