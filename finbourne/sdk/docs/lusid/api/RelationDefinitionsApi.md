# lusid.RelationDefinitionsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_relation_definition**](RelationDefinitionsApi.md#create_relation_definition) | **POST** /api/api/relationdefinitions | [EXPERIMENTAL] CreateRelationDefinition: Create a relation definition
[**delete_relation_definition**](RelationDefinitionsApi.md#delete_relation_definition) | **DELETE** /api/api/relationdefinitions/{scope}/{code} | [EXPERIMENTAL] DeleteRelationDefinition: Delete relation definition
[**get_relation_definition**](RelationDefinitionsApi.md#get_relation_definition) | **GET** /api/api/relationdefinitions/{scope}/{code} | [EXPERIMENTAL] GetRelationDefinition: Get relation definition


### Example

```python
from finbourne.sdk.exceptions import ApiException
from finbourne.sdk.extensions.configuration_options import ConfigurationOptions
from finbourne.sdk.services.lusid.models import *

from finbourne.sdk.extensions import (
  SyncApiClientFactory
)

from finbourne.sdk.services.lusid.api.relation_definitions_api import RelationDefinitionsApi

# opts = ConfigurationOptions()
# opts.total_timeout_ms = 30_000

# uncomment the below to use an api client factory with overrides
# api_client_factory = SyncApiClientFactory(opts=opts)

api_client_factory = SyncApiClientFactory()
api_instance = api_client_factory.build(RelationDefinitionsApi)
```

---

# **create_relation_definition**
> RelationDefinition createRelationDefinition = create_relation_definition(create_relation_definition_request)

[EXPERIMENTAL] CreateRelationDefinition: Create a relation definition

Define a new relation.

### Example

```python
api_instance = api_client_factory.build(RelationDefinitionsApi)
create_relation_definition_request = CreateRelationDefinitionRequest()
api_response = api_instance.create_relation_definition(create_relation_definition_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_relation_definition_request** | [**CreateRelationDefinitionRequest**](CreateRelationDefinitionRequest.md)| The definition of the new relation. | [required] 

### Return type

[**RelationDefinition**](RelationDefinition.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The newly created relation definition |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **delete_relation_definition**
> DeletedEntityResponse deleteRelationDefinition = delete_relation_definition(scope, code)

[EXPERIMENTAL] DeleteRelationDefinition: Delete relation definition

Delete the definition of the specified relation.

### Example

```python
api_instance = api_client_factory.build(RelationDefinitionsApi)
scope = 'scope_example' # str
code = 'code_example' # str
api_response = api_instance.delete_relation_definition(scope, code)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the relation to be deleted. | [required] 
 **code** | **str**| The code of the relation to be deleted. Together with the domain and scope this uniquely              identifies the relation. | [required] 

### Return type

[**DeletedEntityResponse**](DeletedEntityResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The time that the relation definition was deleted |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_relation_definition**
> RelationDefinition getRelationDefinition = get_relation_definition(scope, code, as_at=as_at)

[EXPERIMENTAL] GetRelationDefinition: Get relation definition

Retrieve the definition of a specified relation.

### Example

```python
api_instance = api_client_factory.build(RelationDefinitionsApi)
scope = 'scope_example' # str
code = 'code_example' # str
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
api_response = api_instance.get_relation_definition(scope, code, as_at=as_at)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the specified relation. | [required] 
 **code** | **str**| The code of the specified relation. Together with the domain and scope this uniquely              identifies the relation. | [required] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the relation definition. Defaults to return              the latest version of the definition if not specified. | [optional] 

### Return type

[**RelationDefinition**](RelationDefinition.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested relation definition |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

