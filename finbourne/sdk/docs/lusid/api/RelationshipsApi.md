# lusid.RelationshipsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_relationship**](RelationshipsApi.md#create_relationship) | **POST** /api/api/relationshipdefinitions/{scope}/{code}/relationships | CreateRelationship: Create Relationship
[**delete_relationship**](RelationshipsApi.md#delete_relationship) | **POST** /api/api/relationshipdefinitions/{scope}/{code}/relationships/$delete | [EARLY ACCESS] DeleteRelationship: Delete Relationship


### Example

```python
from finbourne.sdk.exceptions import ApiException
from finbourne.sdk.extensions.configuration_options import ConfigurationOptions
from finbourne.sdk.services.lusid.models import *

from finbourne.sdk.extensions import (
  SyncApiClientFactory
)

from finbourne.sdk.services.lusid.api.relationships_api import RelationshipsApi

# opts = ConfigurationOptions()
# opts.total_timeout_ms = 30_000

# uncomment the below to use an api client factory with overrides
# api_client_factory = SyncApiClientFactory(opts=opts)

api_client_factory = SyncApiClientFactory()
api_instance = api_client_factory.build(RelationshipsApi)
```

---

# **create_relationship**
> CompleteRelationship createRelationship = create_relationship(scope, code, create_relationship_request)

CreateRelationship: Create Relationship

Create a relationship between two entity objects by their identifiers

### Example

```python
api_instance = api_client_factory.build(RelationshipsApi)
scope = 'scope_example' # str
code = 'code_example' # str
create_relationship_request = CreateRelationshipRequest()
api_response = api_instance.create_relationship(scope, code, create_relationship_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the relationship | [required] 
 **code** | **str**| The code of the relationship | [required] 
 **create_relationship_request** | [**CreateRelationshipRequest**](CreateRelationshipRequest.md)| The details of the relationship to create. | [required] 

### Return type

[**CompleteRelationship**](CompleteRelationship.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The newly created relationship. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **delete_relationship**
> DeletedEntityResponse deleteRelationship = delete_relationship(scope, code, delete_relationship_request)

[EARLY ACCESS] DeleteRelationship: Delete Relationship

Delete a relationship between two entity objects represented by their identifiers

### Example

```python
api_instance = api_client_factory.build(RelationshipsApi)
scope = 'scope_example' # str
code = 'code_example' # str
delete_relationship_request = DeleteRelationshipRequest()
api_response = api_instance.delete_relationship(scope, code, delete_relationship_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the relationship | [required] 
 **code** | **str**| The code of the relationship | [required] 
 **delete_relationship_request** | [**DeleteRelationshipRequest**](DeleteRelationshipRequest.md)| The details of the relationship to delete. | [required] 

### Return type

[**DeletedEntityResponse**](DeletedEntityResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The datetime that the relationship is deleted |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

