# lusid.SchemasApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_entity_schema**](SchemasApi.md#get_entity_schema) | **GET** /api/api/schemas/entities/{entity} | [EARLY ACCESS] GetEntitySchema: Get schema
[**get_property_schema**](SchemasApi.md#get_property_schema) | **GET** /api/api/schemas/properties | [EARLY ACCESS] GetPropertySchema: Get property schema
[**get_value_types**](SchemasApi.md#get_value_types) | **GET** /api/api/schemas/types | [EARLY ACCESS] GetValueTypes: Get value types
[**list_entities**](SchemasApi.md#list_entities) | **GET** /api/api/schemas/entities | [EARLY ACCESS] ListEntities: List entities


### Example

```python
from finbourne.sdk.exceptions import ApiException
from finbourne.sdk.extensions.configuration_options import ConfigurationOptions
from finbourne.sdk.services.lusid.models import *

from finbourne.sdk.extensions import (
  SyncApiClientFactory
)

from finbourne.sdk.services.lusid.api.schemas_api import SchemasApi

# opts = ConfigurationOptions()
# opts.total_timeout_ms = 30_000

# uncomment the below to use an api client factory with overrides
# api_client_factory = SyncApiClientFactory(opts=opts)

api_client_factory = SyncApiClientFactory()
api_instance = api_client_factory.build(SchemasApi)
```

---

# **get_entity_schema**
> ModelSchema getEntitySchema = get_entity_schema(entity)

[EARLY ACCESS] GetEntitySchema: Get schema

Gets the schema and meta-data for a given entity

### Example

```python
api_instance = api_client_factory.build(SchemasApi)
entity = 'entity_example' # str
api_response = api_instance.get_entity_schema(entity)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity** | **str**| The name of a valid entity | [required] 

### Return type

[**ModelSchema**](ModelSchema.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_property_schema**
> PropertySchema getPropertySchema = get_property_schema(property_keys=property_keys, as_at=as_at)

[EARLY ACCESS] GetPropertySchema: Get property schema

Get the schemas for the provided list of property keys.

### Example

```python
api_instance = api_client_factory.build(SchemasApi)
property_keys = ['property_keys_example'] # List[str] (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
api_response = api_instance.get_property_schema(property_keys=property_keys, as_at=as_at)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_keys** | [**List[str]**](str.md)| One or more property keys for which the schema is requested | [optional] 
 **as_at** | **datetime**| Optional. The AsAt date of the data | [optional] 

### Return type

[**PropertySchema**](PropertySchema.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_value_types**
> ResourceListOfValueType getValueTypes = get_value_types(sort_by=sort_by, limit=limit)

[EARLY ACCESS] GetValueTypes: Get value types

Gets the available value types for which a schema is available.

### Example

```python
api_instance = api_client_factory.build(SchemasApi)
sort_by = ['sort_by_example'] # List[str] (optional)
limit = 56 # int (optional)
api_response = api_instance.get_value_types(sort_by=sort_by, limit=limit)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sort_by** | [**List[str]**](str.md)| Optional. Order the results by these fields. Use use the &#39;-&#39; sign to denote descending order e.g. -MyFieldName | [optional] 
 **limit** | **int**| Optional. When paginating, limit the number of returned results to this many. | [optional] 

### Return type

[**ResourceListOfValueType**](ResourceListOfValueType.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **list_entities**
> ResourceListOfString listEntities = list_entities()

[EARLY ACCESS] ListEntities: List entities

List all available entities for which schema information is available.

### Example

```python
api_instance = api_client_factory.build(SchemasApi)
api_response = api_instance.list_entities()
pprint(api_response)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ResourceListOfString**](ResourceListOfString.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

