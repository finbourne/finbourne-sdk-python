# lusid.RelationsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_relation**](RelationsApi.md#create_relation) | **POST** /api/api/relations/{scope}/{code} | [EXPERIMENTAL] CreateRelation: Create Relation
[**delete_relation**](RelationsApi.md#delete_relation) | **POST** /api/api/relations/{scope}/{code}/$delete | [EXPERIMENTAL] DeleteRelation: Delete a relation


### Example

```python
from finbourne.sdk.exceptions import ApiException
from finbourne.sdk.extensions.configuration_options import ConfigurationOptions
from finbourne.sdk.services.lusid.models import *

from finbourne.sdk.extensions import (
  SyncApiClientFactory
)

from finbourne.sdk.services.lusid.api.relations_api import RelationsApi

# opts = ConfigurationOptions()
# opts.total_timeout_ms = 30_000

# uncomment the below to use an api client factory with overrides
# api_client_factory = SyncApiClientFactory(opts=opts)

api_client_factory = SyncApiClientFactory()
api_instance = api_client_factory.build(RelationsApi)
```

---

# **create_relation**
> CompleteRelation createRelation = create_relation(scope, code, create_relation_request, effective_at=effective_at)

[EXPERIMENTAL] CreateRelation: Create Relation

Create a relation between two entity objects by their identifiers

### Example

```python
api_instance = api_client_factory.build(RelationsApi)
scope = 'scope_example' # str
code = 'code_example' # str
create_relation_request = CreateRelationRequest()
effective_at = 'effective_at_example' # str (optional)
api_response = api_instance.create_relation(scope, code, create_relation_request, effective_at=effective_at)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the relation definition | [required] 
 **code** | **str**| The code of the relation definition | [required] 
 **create_relation_request** | [**CreateRelationRequest**](CreateRelationRequest.md)| The details of the relation to create. | [required] 
 **effective_at** | **str**| The effective datetime or cut label at which the relation should be effective from. Defaults to the current LUSID system datetime if not specified. | [optional] 

### Return type

[**CompleteRelation**](CompleteRelation.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The newly created relation. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **delete_relation**
> DeletedEntityResponse deleteRelation = delete_relation(scope, code, delete_relation_request, effective_at=effective_at)

[EXPERIMENTAL] DeleteRelation: Delete a relation

Delete a relation between two entity objects represented by their identifiers

### Example

```python
api_instance = api_client_factory.build(RelationsApi)
scope = 'scope_example' # str
code = 'code_example' # str
delete_relation_request = DeleteRelationRequest()
effective_at = 'effective_at_example' # str (optional)
api_response = api_instance.delete_relation(scope, code, delete_relation_request, effective_at=effective_at)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the relation definition | [required] 
 **code** | **str**| The code of the relation definition | [required] 
 **delete_relation_request** | [**DeleteRelationRequest**](DeleteRelationRequest.md)| The details of the relation to delete. | [required] 
 **effective_at** | **str**| The effective datetime or cut label at which the relation should the deletion be effective from. Defaults to the current LUSID system datetime if not specified. | [optional] 

### Return type

[**DeletedEntityResponse**](DeletedEntityResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The datetime that the relation is deleted |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

