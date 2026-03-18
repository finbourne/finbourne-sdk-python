# lusid.RelationalDatasetDefinitionApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_relational_dataset_definition**](RelationalDatasetDefinitionApi.md#create_relational_dataset_definition) | **POST** /api/api/relationaldatasetdefinitions | CreateRelationalDatasetDefinition: Create a Relational Dataset Definition
[**delete_relational_dataset_definition**](RelationalDatasetDefinitionApi.md#delete_relational_dataset_definition) | **DELETE** /api/api/relationaldatasetdefinitions/{scope}/{code} | DeleteRelationalDatasetDefinition: Delete a Relational Dataset Definition
[**get_relational_dataset_definition**](RelationalDatasetDefinitionApi.md#get_relational_dataset_definition) | **GET** /api/api/relationaldatasetdefinitions/{scope}/{code} | GetRelationalDatasetDefinition: Get a Relational Dataset Definition
[**list_relational_dataset_definitions**](RelationalDatasetDefinitionApi.md#list_relational_dataset_definitions) | **GET** /api/api/relationaldatasetdefinitions | ListRelationalDatasetDefinitions: List Relational Dataset Definitions
[**update_relational_dataset_definition**](RelationalDatasetDefinitionApi.md#update_relational_dataset_definition) | **PUT** /api/api/relationaldatasetdefinitions/{scope}/{code} | UpdateRelationalDatasetDefinition: Update a Relational Dataset Definition
[**update_relational_dataset_details**](RelationalDatasetDefinitionApi.md#update_relational_dataset_details) | **POST** /api/api/relationaldatasetdefinitions/{scope}/{code}/details/$update | UpdateRelationalDatasetDetails: Update Relational Dataset Details: DisplayName, Description and ApplicableEntityTypes
[**update_relational_dataset_field_schema**](RelationalDatasetDefinitionApi.md#update_relational_dataset_field_schema) | **POST** /api/api/relationaldatasetdefinitions/{scope}/{code}/fieldschema/$update | UpdateRelationalDatasetFieldSchema: Update Relational Dataset Field Schema


### Example

```python
from finbourne.sdk.exceptions import ApiException
from finbourne.sdk.extensions.configuration_options import ConfigurationOptions
from finbourne.sdk.services.lusid.models import *

from finbourne.sdk.extensions import (
  SyncApiClientFactory
)

from finbourne.sdk.services.lusid.api.relational_dataset_definition_api import RelationalDatasetDefinitionApi

# opts = ConfigurationOptions()
# opts.total_timeout_ms = 30_000

# uncomment the below to use an api client factory with overrides
# api_client_factory = SyncApiClientFactory(opts=opts)

api_client_factory = SyncApiClientFactory()
api_instance = api_client_factory.build(RelationalDatasetDefinitionApi)
```

---

# **create_relational_dataset_definition**
> RelationalDatasetDefinition createRelationalDatasetDefinition = create_relational_dataset_definition(create_relational_dataset_definition_request)

CreateRelationalDatasetDefinition: Create a Relational Dataset Definition

Create a new relational dataset definition.

### Example

```python
api_instance = api_client_factory.build(RelationalDatasetDefinitionApi)
create_relational_dataset_definition_request = CreateRelationalDatasetDefinitionRequest()
api_response = api_instance.create_relational_dataset_definition(create_relational_dataset_definition_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_relational_dataset_definition_request** | [**CreateRelationalDatasetDefinitionRequest**](CreateRelationalDatasetDefinitionRequest.md)| The relational dataset definition to create. | [required] 

### Return type

[**RelationalDatasetDefinition**](RelationalDatasetDefinition.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The created relational dataset definition. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **delete_relational_dataset_definition**
> DeletedEntityResponse deleteRelationalDatasetDefinition = delete_relational_dataset_definition(scope, code)

DeleteRelationalDatasetDefinition: Delete a Relational Dataset Definition

Delete a relational dataset definition.  WARNING! This operation is irreversible. Deleting a relational dataset definition will also delete all associated data points.

### Example

```python
api_instance = api_client_factory.build(RelationalDatasetDefinitionApi)
scope = 'scope_example' # str
code = 'code_example' # str
api_response = api_instance.delete_relational_dataset_definition(scope, code)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the relational dataset definition. | [required] 
 **code** | **str**| The code of the relational dataset definition. | [required] 

### Return type

[**DeletedEntityResponse**](DeletedEntityResponse.md)

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

# **get_relational_dataset_definition**
> RelationalDatasetDefinition getRelationalDatasetDefinition = get_relational_dataset_definition(scope, code, as_at=as_at)

GetRelationalDatasetDefinition: Get a Relational Dataset Definition

Retrieve a relational dataset definition by its identifier.

### Example

```python
api_instance = api_client_factory.build(RelationalDatasetDefinitionApi)
scope = 'scope_example' # str
code = 'code_example' # str
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
api_response = api_instance.get_relational_dataset_definition(scope, code, as_at=as_at)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the relational dataset definition. | [required] 
 **code** | **str**| The code of the relational dataset definition. | [required] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the relational dataset definition. Defaults to return the latest version if not specified. | [optional] 

### Return type

[**RelationalDatasetDefinition**](RelationalDatasetDefinition.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested relational dataset definition. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **list_relational_dataset_definitions**
> PagedResourceListOfRelationalDatasetDefinition listRelationalDatasetDefinitions = list_relational_dataset_definitions(as_at=as_at, page=page, sort_by=sort_by, limit=limit, filter=filter)

ListRelationalDatasetDefinitions: List Relational Dataset Definitions

List all relational dataset definitions matching particular criteria.

### Example

```python
api_instance = api_client_factory.build(RelationalDatasetDefinitionApi)
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
page = 'page_example' # str (optional)
sort_by = ['sort_by_example'] # List[str] (optional)
limit = 56 # int (optional)
filter = 'filter_example' # str (optional)
api_response = api_instance.list_relational_dataset_definitions(as_at=as_at, page=page, sort_by=sort_by, limit=limit, filter=filter)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **as_at** | **datetime**| The asAt datetime at which to list the relational dataset definitions. Defaults to return the latest version if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing relational dataset definitions from a previous call to list relational dataset definitions. | [optional] 
 **sort_by** | [**List[str]**](str.md)| A list of field names to sort by, each suffixed by \&quot; ASC\&quot; or \&quot; DESC\&quot; | [optional] 
 **limit** | **int**| When paginating, limit the number of returned results to this many. | [optional] 
 **filter** | **str**| Expression to filter the result set. | [optional] 

### Return type

[**PagedResourceListOfRelationalDatasetDefinition**](PagedResourceListOfRelationalDatasetDefinition.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of relational dataset definitions. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **update_relational_dataset_definition**
> RelationalDatasetDefinition updateRelationalDatasetDefinition = update_relational_dataset_definition(scope, code, update_relational_dataset_definition_request=update_relational_dataset_definition_request)

UpdateRelationalDatasetDefinition: Update a Relational Dataset Definition

Update an existing relational dataset definition.  Applicable only to the definitions that are not yet in use i.e. there are no DataPoints associated with this definition.

### Example

```python
api_instance = api_client_factory.build(RelationalDatasetDefinitionApi)
scope = 'scope_example' # str
code = 'code_example' # str
update_relational_dataset_definition_request = UpdateRelationalDatasetDefinitionRequest()
api_response = api_instance.update_relational_dataset_definition(scope, code, update_relational_dataset_definition_request=update_relational_dataset_definition_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the relational dataset definition. | [required] 
 **code** | **str**| The code of the relational dataset definition. | [required] 
 **update_relational_dataset_definition_request** | [**UpdateRelationalDatasetDefinitionRequest**](UpdateRelationalDatasetDefinitionRequest.md)| The updated relational dataset definition. | [optional] 

### Return type

[**RelationalDatasetDefinition**](RelationalDatasetDefinition.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated relational dataset definition. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **update_relational_dataset_details**
> RelationalDatasetDefinition updateRelationalDatasetDetails = update_relational_dataset_details(scope, code, update_relational_dataset_details=update_relational_dataset_details)

UpdateRelationalDatasetDetails: Update Relational Dataset Details: DisplayName, Description and ApplicableEntityTypes

Update an existing relational dataset definition.  Applicable only to the definitions that are already in use i.e. contain DataPoints associated with this definition.

### Example

```python
api_instance = api_client_factory.build(RelationalDatasetDefinitionApi)
scope = 'scope_example' # str
code = 'code_example' # str
update_relational_dataset_details = UpdateRelationalDatasetDetails()
api_response = api_instance.update_relational_dataset_details(scope, code, update_relational_dataset_details=update_relational_dataset_details)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the relational dataset definition. | [required] 
 **code** | **str**| The code of the relational dataset definition. | [required] 
 **update_relational_dataset_details** | [**UpdateRelationalDatasetDetails**](UpdateRelationalDatasetDetails.md)| The updated details of the relational dataset. | [optional] 

### Return type

[**RelationalDatasetDefinition**](RelationalDatasetDefinition.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated relational dataset definition. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **update_relational_dataset_field_schema**
> RelationalDatasetDefinition updateRelationalDatasetFieldSchema = update_relational_dataset_field_schema(scope, code, update_relational_dataset_field_schema=update_relational_dataset_field_schema)

UpdateRelationalDatasetFieldSchema: Update Relational Dataset Field Schema

Update an existing relational dataset definition with the new field schema.  Applicable only to the definitions that are already in use i.e. contain DataPoints associated with this definition.

### Example

```python
api_instance = api_client_factory.build(RelationalDatasetDefinitionApi)
scope = 'scope_example' # str
code = 'code_example' # str
update_relational_dataset_field_schema = UpdateRelationalDatasetFieldSchema()
api_response = api_instance.update_relational_dataset_field_schema(scope, code, update_relational_dataset_field_schema=update_relational_dataset_field_schema)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the relational dataset definition. | [required] 
 **code** | **str**| The code of the relational dataset definition. | [required] 
 **update_relational_dataset_field_schema** | [**UpdateRelationalDatasetFieldSchema**](UpdateRelationalDatasetFieldSchema.md)| Relational dataset fields to add, update or remove. | [optional] 

### Return type

[**RelationalDatasetDefinition**](RelationalDatasetDefinition.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated relational dataset definition. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

