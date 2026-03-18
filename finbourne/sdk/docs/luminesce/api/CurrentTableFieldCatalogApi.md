# luminesce.CurrentTableFieldCatalogApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_catalog**](CurrentTableFieldCatalogApi.md#get_catalog) | **GET** /honeycomb/api/Catalog | GetCatalog: Get a Flattened Table/Field Catalog
[**get_catalog_v1**](CurrentTableFieldCatalogApi.md#get_catalog_v1) | **GET** /honeycomb/api/CatalogV1 | [DEPRECATED] GetCatalogV1: Get a Flattened Table/Field Catalog
[**get_fields**](CurrentTableFieldCatalogApi.md#get_fields) | **GET** /honeycomb/api/Catalog/fields | GetFields: List field and parameters for providers
[**get_fields_v1**](CurrentTableFieldCatalogApi.md#get_fields_v1) | **GET** /honeycomb/api/CatalogV1/fields | [DEPRECATED] GetFieldsV1: List field and parameters for providers
[**get_providers**](CurrentTableFieldCatalogApi.md#get_providers) | **GET** /honeycomb/api/Catalog/providers | GetProviders: List available providers
[**get_providers_v1**](CurrentTableFieldCatalogApi.md#get_providers_v1) | **GET** /honeycomb/api/CatalogV1/providers | [DEPRECATED] GetProvidersV1: List available providers


### Example

```python
from finbourne.sdk.exceptions import ApiException
from finbourne.sdk.extensions.configuration_options import ConfigurationOptions
from finbourne.sdk.services.luminesce.models import *

from finbourne.sdk.extensions import (
  SyncApiClientFactory
)

from finbourne.sdk.services.luminesce.api.current_table_field_catalog_api import CurrentTableFieldCatalogApi

# opts = ConfigurationOptions()
# opts.total_timeout_ms = 30_000

# uncomment the below to use an api client factory with overrides
# api_client_factory = SyncApiClientFactory(opts=opts)

api_client_factory = SyncApiClientFactory()
api_instance = api_client_factory.build(CurrentTableFieldCatalogApi)
```

---

# **get_catalog**
> str getCatalog = get_catalog(free_text_search=free_text_search, json_proper=json_proper)

GetCatalog: Get a Flattened Table/Field Catalog

 Returns the User's full version of the catalog (Providers, their fields and associated information) that are currently running that you have access to (in Json format).  This is the entire catalog flattened, which is often quite large and always a bit repetitive.   The internal results are cached for several minutes.  Consider using `api/Catalog/providers` and `api/Catalog/fields` for a more granular and incremental loading flow.  It is possible to be throttled if you make too many requests in a short period of time, receiving a: - 429 Too Many Requests : Please try your request again soon  The following error codes are to be anticipated with standard Problem Detail reports: - 401 Unauthorized - 403 Forbidden 

### Example

```python
api_instance = api_client_factory.build(CurrentTableFieldCatalogApi)
free_text_search = 'free_text_search_example' # str (optional)
json_proper = False # bool (optional)
api_response = api_instance.get_catalog(free_text_search=free_text_search, json_proper=json_proper)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **free_text_search** | **str**| Limit the catalog to only things in some way dealing with the passed in text string | [optional] 
 **json_proper** | **bool**| Should this be text/json (not json-encoded-as-a-string) | [optional] [default to False]

### Return type

**str**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_catalog_v1**
> str getCatalogV1 = get_catalog_v1(free_text_search=free_text_search, json_proper=json_proper, use_cache=use_cache)

[DEPRECATED] GetCatalogV1: Get a Flattened Table/Field Catalog

 Returns the User's full version of the catalog (Providers, their fields and associated information) that are currently running that you have access to (in Json format).  This is the entire catalog flattened, which is often quite large and always a bit repetitive.   The internal results are cached for several minutes.  Consider using `api/Catalog/providers` and `api/Catalog/fields` for a more granular and incremental loading flow.  The following error codes are to be anticipated with standard Problem Detail reports: - 401 Unauthorized - 403 Forbidden 

### Example

```python
api_instance = api_client_factory.build(CurrentTableFieldCatalogApi)
free_text_search = 'free_text_search_example' # str (optional)
json_proper = False # bool (optional)
use_cache = False # bool (optional)
api_response = api_instance.get_catalog_v1(free_text_search=free_text_search, json_proper=json_proper, use_cache=use_cache)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **free_text_search** | **str**| Limit the catalog to only things in some way dealing with the passed in text string | [optional] 
 **json_proper** | **bool**| Should this be text/json (not json-encoded-as-a-string) | [optional] [default to False]
 **use_cache** | **bool**| Should the available cache be used? false is effectively to pick up a change in the catalog | [optional] [default to False]

### Return type

**str**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_fields**
> str getFields = get_fields(table_like=table_like, add_lineage=add_lineage)

GetFields: List field and parameters for providers

 Returns the User's full version of the catalog but only the field/parameter-level information  (as well as the TableName they refer to, of course) for tables matching the `tableLike` (manually include wildcards if desired).  The internal results are cached for several minutes.  It is possible to be throttled if you make too many requests in a short period of time, receiving a: - 429 Too Many Requests : Please try your request again soon  The following error codes are to be anticipated with standard Problem Detail reports: - 401 Unauthorized - 403 Forbidden 

### Example

```python
api_instance = api_client_factory.build(CurrentTableFieldCatalogApi)
table_like = '%' # str (optional)
add_lineage = False # bool (optional)
api_response = api_instance.get_fields(table_like=table_like, add_lineage=add_lineage)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **table_like** | **str**| Allows for SQL-LIKE style filtering of which Providers you want the fields for. | [optional] [default to &#39;%&#39;]
 **add_lineage** | **bool**| Adds in any column lineage which is registered in the catalog to the results. | [optional] [default to False]

### Return type

**str**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_fields_v1**
> str getFieldsV1 = get_fields_v1(table_like=table_like)

[DEPRECATED] GetFieldsV1: List field and parameters for providers

 Returns the User's full version of the catalog but only the field/parameter-level information  (as well as the TableName they refer to, of course) for tables matching the `tableLike` (manually include wildcards if desired).  The internal results are cached for several minutes.  The following error codes are to be anticipated with standard Problem Detail reports: - 401 Unauthorized - 403 Forbidden 

### Example

```python
api_instance = api_client_factory.build(CurrentTableFieldCatalogApi)
table_like = '%' # str (optional)
api_response = api_instance.get_fields_v1(table_like=table_like)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **table_like** | **str**|  | [optional] [default to &#39;%&#39;]

### Return type

**str**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_providers**
> str getProviders = get_providers(free_text_search=free_text_search, add_lineage=add_lineage)

GetProviders: List available providers

 Returns the User's full version of the catalog but only the table/provider-level information they have access to.  The internal results are cached for several minutes.  It is possible to be throttled if you make too many requests in a short period of time, receiving a: - 429 Too Many Requests : Please try your request again soon  The following error codes are to be anticipated with standard Problem Detail reports: - 401 Unauthorized - 403 Forbidden 

### Example

```python
api_instance = api_client_factory.build(CurrentTableFieldCatalogApi)
free_text_search = 'free_text_search_example' # str (optional)
add_lineage = False # bool (optional)
api_response = api_instance.get_providers(free_text_search=free_text_search, add_lineage=add_lineage)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **free_text_search** | **str**| Limit the catalog to only things in some way dealing with the passed in text string | [optional] 
 **add_lineage** | **bool**| Adds in any column lineage which is registered in the catalog to the results. | [optional] [default to False]

### Return type

**str**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_providers_v1**
> str getProvidersV1 = get_providers_v1(free_text_search=free_text_search, use_cache=use_cache)

[DEPRECATED] GetProvidersV1: List available providers

 Returns the User's full version of the catalog but only the table/provider-level information they have access to.  The internal results are cached for several minutes.  The following error codes are to be anticipated with standard Problem Detail reports: - 401 Unauthorized - 403 Forbidden 

### Example

```python
api_instance = api_client_factory.build(CurrentTableFieldCatalogApi)
free_text_search = 'free_text_search_example' # str (optional)
use_cache = True # bool (optional)
api_response = api_instance.get_providers_v1(free_text_search=free_text_search, use_cache=use_cache)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **free_text_search** | **str**| Limit the catalog to only things in some way dealing with the passed in text string | [optional] 
 **use_cache** | **bool**| Should the available cache be used? false is effectively to pick up a change in the catalog | [optional] [default to True]

### Return type

**str**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

