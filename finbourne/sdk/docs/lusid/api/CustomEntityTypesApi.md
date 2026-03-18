# lusid.CustomEntityTypesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_custom_entity_type**](CustomEntityTypesApi.md#create_custom_entity_type) | **POST** /api/api/customentitytypes | [EARLY ACCESS] CreateCustomEntityType: Define a new Custom Entity Type.
[**get_custom_entity_type**](CustomEntityTypesApi.md#get_custom_entity_type) | **GET** /api/api/customentitytypes/{entityType} | [EARLY ACCESS] GetCustomEntityType: Get a Custom Entity Type.
[**list_custom_entity_types**](CustomEntityTypesApi.md#list_custom_entity_types) | **GET** /api/api/customentitytypes | [EARLY ACCESS] ListCustomEntityTypes: List Custom Entity Types.
[**update_custom_entity_type**](CustomEntityTypesApi.md#update_custom_entity_type) | **PUT** /api/api/customentitytypes/{entityType} | [EARLY ACCESS] UpdateCustomEntityType: Modify an existing Custom Entity Type.


### Example

```python
from finbourne.sdk.exceptions import ApiException
from finbourne.sdk.extensions.configuration_options import ConfigurationOptions
from finbourne.sdk.services.lusid.models import *

from finbourne.sdk.extensions import (
  SyncApiClientFactory
)

from finbourne.sdk.services.lusid.api.custom_entity_types_api import CustomEntityTypesApi

# opts = ConfigurationOptions()
# opts.total_timeout_ms = 30_000

# uncomment the below to use an api client factory with overrides
# api_client_factory = SyncApiClientFactory(opts=opts)

api_client_factory = SyncApiClientFactory()
api_instance = api_client_factory.build(CustomEntityTypesApi)
```

---

# **create_custom_entity_type**
> CustomEntityType createCustomEntityType = create_custom_entity_type(create_custom_entity_type_request)

[EARLY ACCESS] CreateCustomEntityType: Define a new Custom Entity Type.

The API will return a Bad Request if the Custom Entity Type already exists.

### Example

```python
api_instance = api_client_factory.build(CustomEntityTypesApi)
create_custom_entity_type_request = CreateCustomEntityTypeRequest()
api_response = api_instance.create_custom_entity_type(create_custom_entity_type_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_custom_entity_type_request** | [**CreateCustomEntityTypeRequest**](CreateCustomEntityTypeRequest.md)| The payload containing the description of the Custom Entity Type. | [required] 

### Return type

[**CustomEntityType**](CustomEntityType.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The created Custom Entity Type. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_custom_entity_type**
> CustomEntityType getCustomEntityType = get_custom_entity_type(entity_type, as_at=as_at)

[EARLY ACCESS] GetCustomEntityType: Get a Custom Entity Type.

Retrieve a specific Custom Entity Type at a point in AsAt time.

### Example

```python
api_instance = api_client_factory.build(CustomEntityTypesApi)
entity_type = 'entity_type_example' # str
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
api_response = api_instance.get_custom_entity_type(entity_type, as_at=as_at)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_type** | **str**| The identifier for the Custom Entity Type, derived from the \&quot;entityTypeName\&quot; provided on creation. | [required] 
 **as_at** | **datetime**| The AsAt datetime at which to retrieve the definition. | [optional] 

### Return type

[**CustomEntityType**](CustomEntityType.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested Custom Entity Type. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **list_custom_entity_types**
> PagedResourceListOfCustomEntityType listCustomEntityTypes = list_custom_entity_types(as_at=as_at, limit=limit, filter=filter, sort_by=sort_by, page=page)

[EARLY ACCESS] ListCustomEntityTypes: List Custom Entity Types.

List all Custom Entity Types matching particular criteria.

### Example

```python
api_instance = api_client_factory.build(CustomEntityTypesApi)
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
limit = 56 # int (optional)
filter = 'filter_example' # str (optional)
sort_by = ['sort_by_example'] # List[str] (optional)
page = 'page_example' # str (optional)
api_response = api_instance.list_custom_entity_types(as_at=as_at, limit=limit, filter=filter, sort_by=sort_by, page=page)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **as_at** | **datetime**| The asAt datetime at which to list the entities. Defaults to returning the latest version              of each Custom Entity Type if not specified. | [optional] 
 **limit** | **int**| When paginating, limit the results to this number. Defaults to 100 if not specified. | [optional] 
 **filter** | **str**| Expression to filter the results. For more information about filtering              results, see https://support.lusid.com/knowledgebase/article/KA-01914. | [optional] 
 **sort_by** | [**List[str]**](str.md)| A list of field names to sort by, each suffixed by \&quot; ASC\&quot; or \&quot; DESC\&quot; | [optional] 
 **page** | **str**| The pagination token to use to continue listing entities; this              value is returned from the previous call. If a pagination token is provided, the filter, limit, sortBy,              and asAt fields must not have changed since the original request. | [optional] 

### Return type

[**PagedResourceListOfCustomEntityType**](PagedResourceListOfCustomEntityType.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List Custom Entity Types. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **update_custom_entity_type**
> CustomEntityType updateCustomEntityType = update_custom_entity_type(entity_type, update_custom_entity_type_request)

[EARLY ACCESS] UpdateCustomEntityType: Modify an existing Custom Entity Type.

The API will return a Bad Request if the Custom Entity Type does not exist.

### Example

```python
api_instance = api_client_factory.build(CustomEntityTypesApi)
entity_type = 'entity_type_example' # str
update_custom_entity_type_request = UpdateCustomEntityTypeRequest()
api_response = api_instance.update_custom_entity_type(entity_type, update_custom_entity_type_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_type** | **str**| The identifier for the Custom Entity Type, derived from the \&quot;entityTypeName\&quot; provided on creation. | [required] 
 **update_custom_entity_type_request** | [**UpdateCustomEntityTypeRequest**](UpdateCustomEntityTypeRequest.md)| The payload containing the description of the Custom Entity Type. | [required] 

### Return type

[**CustomEntityType**](CustomEntityType.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated Custom Entity Type. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

