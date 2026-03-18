# lusid.AggregatedReturnsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_returns_entity**](AggregatedReturnsApi.md#delete_returns_entity) | **DELETE** /api/api/returns/{scope}/{code} | [EXPERIMENTAL] DeleteReturnsEntity: Delete returns entity.
[**get_returns_entity**](AggregatedReturnsApi.md#get_returns_entity) | **GET** /api/api/returns/{scope}/{code} | [EXPERIMENTAL] GetReturnsEntity: Get returns entity.
[**list_returns_entities**](AggregatedReturnsApi.md#list_returns_entities) | **GET** /api/api/returns | [EXPERIMENTAL] ListReturnsEntities: List returns entities.
[**upsert_returns_entity**](AggregatedReturnsApi.md#upsert_returns_entity) | **POST** /api/api/returns | [EXPERIMENTAL] UpsertReturnsEntity: Upsert returns entity.


### Example

```python
from finbourne.sdk.exceptions import ApiException
from finbourne.sdk.extensions.configuration_options import ConfigurationOptions
from finbourne.sdk.services.lusid.models import *

from finbourne.sdk.extensions import (
  SyncApiClientFactory
)

from finbourne.sdk.services.lusid.api.aggregated_returns_api import AggregatedReturnsApi

# opts = ConfigurationOptions()
# opts.total_timeout_ms = 30_000

# uncomment the below to use an api client factory with overrides
# api_client_factory = SyncApiClientFactory(opts=opts)

api_client_factory = SyncApiClientFactory()
api_instance = api_client_factory.build(AggregatedReturnsApi)
```

---

# **delete_returns_entity**
> DeletedEntityResponse deleteReturnsEntity = delete_returns_entity(scope, code)

[EXPERIMENTAL] DeleteReturnsEntity: Delete returns entity.

Delete returns entity.

### Example

```python
api_instance = api_client_factory.build(AggregatedReturnsApi)
scope = 'scope_example' # str
code = 'code_example' # str
api_response = api_instance.delete_returns_entity(scope, code)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| Returns entity scope. | [required] 
 **code** | **str**| Returns entity code. | [required] 

### Return type

[**DeletedEntityResponse**](DeletedEntityResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The time that the returns entity was deleted |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_returns_entity**
> ReturnsEntity getReturnsEntity = get_returns_entity(scope, code, as_at=as_at)

[EXPERIMENTAL] GetReturnsEntity: Get returns entity.

Get returns entity.

### Example

```python
api_instance = api_client_factory.build(AggregatedReturnsApi)
scope = 'scope_example' # str
code = 'code_example' # str
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
api_response = api_instance.get_returns_entity(scope, code, as_at=as_at)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| Returns entity scope. | [required] 
 **code** | **str**| Returns entity code. | [required] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the returns entity. Defaults to return              the latest version of the definition if not specified. | [optional] 

### Return type

[**ReturnsEntity**](ReturnsEntity.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested returns entity |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **list_returns_entities**
> ResourceListOfReturnsEntity listReturnsEntities = list_returns_entities(as_at=as_at)

[EXPERIMENTAL] ListReturnsEntities: List returns entities.

List returns entities.

### Example

```python
api_instance = api_client_factory.build(AggregatedReturnsApi)
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
api_response = api_instance.list_returns_entities(as_at=as_at)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **as_at** | **datetime**| The asAt datetime at which to retrieve the relation definitions. Defaults to return              the latest version of each definition if not specified. | [optional] 

### Return type

[**ResourceListOfReturnsEntity**](ResourceListOfReturnsEntity.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested returns entities |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **upsert_returns_entity**
> ReturnsEntity upsertReturnsEntity = upsert_returns_entity(returns_entity)

[EXPERIMENTAL] UpsertReturnsEntity: Upsert returns entity.

Upsert returns entity.

### Example

```python
api_instance = api_client_factory.build(AggregatedReturnsApi)
returns_entity = ReturnsEntity()
api_response = api_instance.upsert_returns_entity(returns_entity)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **returns_entity** | [**ReturnsEntity**](ReturnsEntity.md)| Definition of the returns entity. | [required] 

### Return type

[**ReturnsEntity**](ReturnsEntity.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The upserted returns entity |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

