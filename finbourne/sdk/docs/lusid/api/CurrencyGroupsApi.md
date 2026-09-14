# lusid.CurrencyGroupsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_currency_group**](CurrencyGroupsApi.md#delete_currency_group) | **DELETE** /api/api/currencies/groups/{code} | [EXPERIMENTAL] DeleteCurrencyGroup: Delete a currency group.
[**get_currency_group**](CurrencyGroupsApi.md#get_currency_group) | **GET** /api/api/currencies/groups/{code} | [EXPERIMENTAL] GetCurrencyGroup: Get a currency group.
[**list_currency_groups**](CurrencyGroupsApi.md#list_currency_groups) | **GET** /api/api/currencies/groups | [EXPERIMENTAL] ListCurrencyGroups: List currency groups.
[**upsert_currency_group**](CurrencyGroupsApi.md#upsert_currency_group) | **POST** /api/api/currencies/groups | [EXPERIMENTAL] UpsertCurrencyGroup: Upsert a currency group.


### Example

```python
from finbourne.sdk.exceptions import ApiException
from finbourne.sdk.extensions.configuration_options import ConfigurationOptions
from finbourne.sdk.services.lusid.models import *

from finbourne.sdk.extensions import (
  SyncApiClientFactory
)

from finbourne.sdk.services.lusid.api.currency_groups_api import CurrencyGroupsApi

# opts = ConfigurationOptions()
# opts.total_timeout_ms = 30_000

# uncomment the below to use an api client factory with overrides
# api_client_factory = SyncApiClientFactory(opts=opts)

api_client_factory = SyncApiClientFactory()
api_instance = api_client_factory.build(CurrencyGroupsApi)
```

---

# **delete_currency_group**
> DeletedEntityResponse deleteCurrencyGroup = delete_currency_group(code)

[EXPERIMENTAL] DeleteCurrencyGroup: Delete a currency group.

Delete the currency group with the given code. The group's currencies are freed to be claimed  by other currency groups.

### Example

```python
api_instance = api_client_factory.build(CurrencyGroupsApi)
code = 'code_example' # str
api_response = api_instance.delete_currency_group(code)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| The code of the currency group to delete. | [required] 

### Return type

[**DeletedEntityResponse**](../model/DeletedEntityResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The deleted entity metadata. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_currency_group**
> CurrencyGroupResponse getCurrencyGroup = get_currency_group(code, as_at=as_at)

[EXPERIMENTAL] GetCurrencyGroup: Get a currency group.

Get the currency group with the given code.

### Example

```python
api_instance = api_client_factory.build(CurrencyGroupsApi)
code = 'code_example' # str
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
api_response = api_instance.get_currency_group(code, as_at=as_at)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| The code of the currency group. | [required] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the currency group. Defaults to returning              the latest version if not specified. | [optional] 

### Return type

[**CurrencyGroupResponse**](../model/CurrencyGroupResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested currency group. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **list_currency_groups**
> PagedResourceListOfCurrencyGroupResponse listCurrencyGroups = list_currency_groups(as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by)

[EXPERIMENTAL] ListCurrencyGroups: List currency groups.

List the currency groups defined in the tenant that the caller is entitled to read.

### Example

```python
api_instance = api_client_factory.build(CurrencyGroupsApi)
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
page = 'page_example' # str (optional)
limit = 56 # int (optional)
filter = 'filter_example' # str (optional)
sort_by = ['sort_by_example'] # List[str] (optional)
api_response = api_instance.list_currency_groups(as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **as_at** | **datetime**| The asAt datetime at which to list the currency groups. Defaults to returning              the latest version of each currency group if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing currency groups from a previous              call to list currency groups. This value is returned from the previous call. If a pagination token              is provided the filter, sortBy and asAt fields must not have changed since the original request. | [optional] 
 **limit** | **int**| When paginating, limit the results to this number. | [optional] 
 **filter** | **str**| Expression to filter the results. Filterable fields are the group&#39;s code,              displayName and majorUnitCurrency. For example, \&quot;majorUnitCurrency eq &#39;GBP&#39;\&quot;. | [optional] 
 **sort_by** | [**List[str]**](../model/str.md)| A list of field names to sort by, each prefixed with \&quot;+\&quot; for ascending or              \&quot;-\&quot; for descending. Sortable fields are the group&#39;s code, displayName and majorUnitCurrency. | [optional] 

### Return type

[**PagedResourceListOfCurrencyGroupResponse**](../model/PagedResourceListOfCurrencyGroupResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested currency groups. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **upsert_currency_group**
> CurrencyGroupResponse upsertCurrencyGroup = upsert_currency_group(upsert_currency_group_request)

[EXPERIMENTAL] UpsertCurrencyGroup: Upsert a currency group.

Create or update a currency group. If a currency group with the same code already exists it is replaced.  A currency may belong to at most one currency group.

### Example

```python
api_instance = api_client_factory.build(CurrencyGroupsApi)
upsert_currency_group_request = UpsertCurrencyGroupRequest()
api_response = api_instance.upsert_currency_group(upsert_currency_group_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upsert_currency_group_request** | [**UpsertCurrencyGroupRequest**](../model/UpsertCurrencyGroupRequest.md)| The currency group to upsert. | [required] 

### Return type

[**CurrencyGroupResponse**](../model/CurrencyGroupResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The upserted currency group. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

