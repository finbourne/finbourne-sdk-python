# lusid.EntityResolversApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_entity_resolver**](EntityResolversApi.md#create_entity_resolver) | **POST** /api/api/entityresolvers | [EXPERIMENTAL] CreateEntityResolver: Create an Entity Resolver
[**delete_entity_resolver**](EntityResolversApi.md#delete_entity_resolver) | **DELETE** /api/api/entityresolvers/{scope}/{code} | [EXPERIMENTAL] DeleteEntityResolver: Delete an Entity Resolver
[**get_entity_resolver**](EntityResolversApi.md#get_entity_resolver) | **GET** /api/api/entityresolvers/{scope}/{code} | [EXPERIMENTAL] GetEntityResolver: Get a single Entity Resolver
[**update_entity_resolver**](EntityResolversApi.md#update_entity_resolver) | **PUT** /api/api/entityresolvers/{scope}/{code} | [EXPERIMENTAL] UpdateEntityResolver: Update an Entity Resolver


### Example

```python
from finbourne.sdk.exceptions import ApiException
from finbourne.sdk.extensions.configuration_options import ConfigurationOptions
from finbourne.sdk.services.lusid.models import *

from finbourne.sdk.extensions import (
  SyncApiClientFactory
)

from finbourne.sdk.services.lusid.api.entity_resolvers_api import EntityResolversApi

# opts = ConfigurationOptions()
# opts.total_timeout_ms = 30_000

# uncomment the below to use an api client factory with overrides
# api_client_factory = SyncApiClientFactory(opts=opts)

api_client_factory = SyncApiClientFactory()
api_instance = api_client_factory.build(EntityResolversApi)
```

---

# **create_entity_resolver**
> EntityResolver createEntityResolver = create_entity_resolver(create_entity_resolver_request=create_entity_resolver_request)

[EXPERIMENTAL] CreateEntityResolver: Create an Entity Resolver

Define a new Entity Resolver. The resolver's identifier matching order is the sequence of identifier  property keys that will be tried, in turn, when resolving an entity of the given type in the resolver's scope.

### Example

```python
api_instance = api_client_factory.build(EntityResolversApi)
create_entity_resolver_request = CreateEntityResolverRequest()
api_response = api_instance.create_entity_resolver(create_entity_resolver_request=create_entity_resolver_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_entity_resolver_request** | [**CreateEntityResolverRequest**](../model/CreateEntityResolverRequest.md)| The request defining the new Entity Resolver | [optional] 

### Return type

[**EntityResolver**](../model/EntityResolver.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The created Entity Resolver |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **delete_entity_resolver**
> DeletedEntityResponse deleteEntityResolver = delete_entity_resolver(scope, code)

[EXPERIMENTAL] DeleteEntityResolver: Delete an Entity Resolver

The deletion will take effect from the deletion datetime, i.e. the Entity Resolver will no longer exist  at any asAt datetime after the asAt datetime of deletion. Resolution in the affected scope reverts to  the default matching order.

### Example

```python
api_instance = api_client_factory.build(EntityResolversApi)
scope = 'scope_example' # str
code = 'code_example' # str
api_response = api_instance.delete_entity_resolver(scope, code)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Entity Resolver | [required] 
 **code** | **str**| The code of the Entity Resolver. Together with the scope this uniquely identifies the Entity Resolver | [required] 

### Return type

[**DeletedEntityResponse**](../model/DeletedEntityResponse.md)

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

# **get_entity_resolver**
> EntityResolver getEntityResolver = get_entity_resolver(scope, code, as_at=as_at)

[EXPERIMENTAL] GetEntityResolver: Get a single Entity Resolver

Get a single Entity Resolver by scope and code at an optional asAt, defaulting to latest if not specified.

### Example

```python
api_instance = api_client_factory.build(EntityResolversApi)
scope = 'scope_example' # str
code = 'code_example' # str
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
api_response = api_instance.get_entity_resolver(scope, code, as_at=as_at)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Entity Resolver | [required] 
 **code** | **str**| The code of the Entity Resolver. Together with the scope this uniquely identifies the Entity Resolver | [required] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the Entity Resolver. Defaults to return              the latest version if not specified. | [optional] 

### Return type

[**EntityResolver**](../model/EntityResolver.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested Entity Resolver |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **update_entity_resolver**
> EntityResolver updateEntityResolver = update_entity_resolver(scope, code, upsert_entity_resolver_request=upsert_entity_resolver_request)

[EXPERIMENTAL] UpdateEntityResolver: Update an Entity Resolver

Overwrites the description and identifier matching order of an existing Entity Resolver.

### Example

```python
api_instance = api_client_factory.build(EntityResolversApi)
scope = 'scope_example' # str
code = 'code_example' # str
upsert_entity_resolver_request = UpsertEntityResolverRequest()
api_response = api_instance.update_entity_resolver(scope, code, upsert_entity_resolver_request=upsert_entity_resolver_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Entity Resolver | [required] 
 **code** | **str**| The code of the Entity Resolver. Together with the scope this uniquely identifies the Entity Resolver | [required] 
 **upsert_entity_resolver_request** | [**UpsertEntityResolverRequest**](../model/UpsertEntityResolverRequest.md)| The request containing the updated details of the Entity Resolver | [optional] 

### Return type

[**EntityResolver**](../model/EntityResolver.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated Entity Resolver |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

