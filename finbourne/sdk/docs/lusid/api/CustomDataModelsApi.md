# lusid.CustomDataModelsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**batch_amend**](CustomDataModelsApi.md#batch_amend) | **POST** /api/api/datamodel/$batchamend | [EXPERIMENTAL] BatchAmend: Batch amend entities Custom Data Model membership.
[**create_custom_data_model**](CustomDataModelsApi.md#create_custom_data_model) | **POST** /api/api/datamodel/{entityType} | [EXPERIMENTAL] CreateCustomDataModel: Create a Custom Data Model
[**delete_custom_data_model**](CustomDataModelsApi.md#delete_custom_data_model) | **DELETE** /api/api/datamodel/{entityType}/{scope}/{code} | [EXPERIMENTAL] DeleteCustomDataModel: Delete a Custom Data Model
[**get_custom_data_model**](CustomDataModelsApi.md#get_custom_data_model) | **GET** /api/api/datamodel/{entityType}/{scope}/{code} | [EXPERIMENTAL] GetCustomDataModel: Get a Custom Data Model
[**list_data_model_hierarchies**](CustomDataModelsApi.md#list_data_model_hierarchies) | **GET** /api/api/datamodel/hierarchies | [EXPERIMENTAL] ListDataModelHierarchies: List Custom Data Model hierarchies.
[**list_supported_entity_types**](CustomDataModelsApi.md#list_supported_entity_types) | **GET** /api/api/datamodel/entitytype | [EXPERIMENTAL] ListSupportedEntityTypes: List the currently supported entity types for use in Custom Data Models.
[**update_custom_data_model**](CustomDataModelsApi.md#update_custom_data_model) | **PUT** /api/api/datamodel/{entityType}/{scope}/{code} | [EXPERIMENTAL] UpdateCustomDataModel: Update a Custom Data Model


### Example

```python
from finbourne.sdk.exceptions import ApiException
from finbourne.sdk.extensions.configuration_options import ConfigurationOptions
from finbourne.sdk.services.lusid.models import *

from finbourne.sdk.extensions import (
  SyncApiClientFactory
)

from finbourne.sdk.services.lusid.api.custom_data_models_api import CustomDataModelsApi

# opts = ConfigurationOptions()
# opts.total_timeout_ms = 30_000

# uncomment the below to use an api client factory with overrides
# api_client_factory = SyncApiClientFactory(opts=opts)

api_client_factory = SyncApiClientFactory()
api_instance = api_client_factory.build(CustomDataModelsApi)
```

---

# **batch_amend**
> BatchAmendCustomDataModelMembershipResponse batchAmend = batch_amend(success_mode, request_body)

[EXPERIMENTAL] BatchAmend: Batch amend entities Custom Data Model membership.

Add/Remove entities to/from a Custom Data Model in a single operation.                Each amendment request must be keyed by a unique correlation ID.  This id is ephemeral and is not stored by LUSID.  It serves only as a way to easily identify each amendment in the response.                Note: If using partial failure modes, then it is important to check the response body for failures as any  failures will still return a 200 status code.

### Example

```python
api_instance = api_client_factory.build(CustomDataModelsApi)
success_mode = 'Partial' # str
request_body = {"ephemeral-id-1":{"customDataModelId":{"scope":"MyScope","code":"MyCDMCode"},"entityType":"Instrument","entityUniqueId":"41ad555a-7585-41b7-a057-af27c760e145","operation":"Add"},"ephemeral-id-2":{"customDataModelId":{"scope":"MyScope","code":"MyCDMCode"},"entityType":"Instrument","entityUniqueId":"87lr929k-2937-23j3-j293-ds94n726n204","operation":"Remove"},"ephemeral-id-3":{"customDataModelId":{"scope":"MyScope","code":"MyCDMCode2"},"entityType":"Instrument","entityUniqueId":"61apo865d-8019-41g7-a692-ad97j480c382","operation":"Add"}} # Dict[str, MembershipAmendmentRequest]
api_response = api_instance.batch_amend(success_mode, request_body)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **success_mode** | **str**| Whether the batch request should fail Atomically or in a Partial fashion - Allowed Values: Atomic, Partial. | [required] [default to &#39;Partial&#39;]
 **request_body** | [**Dict[str, MembershipAmendmentRequest]**](MembershipAmendmentRequest.md)| The payload describing the amendments to make for the given Custom Data Model. | [required] 

### Return type

[**BatchAmendCustomDataModelMembershipResponse**](BatchAmendCustomDataModelMembershipResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The batch amendment operation was successful |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **create_custom_data_model**
> CustomDataModel createCustomDataModel = create_custom_data_model(entity_type, create_custom_data_model_request=create_custom_data_model_request)

[EXPERIMENTAL] CreateCustomDataModel: Create a Custom Data Model

Creates a Custom Data Model.

### Example

```python
api_instance = api_client_factory.build(CustomDataModelsApi)
entity_type = 'entity_type_example' # str
create_custom_data_model_request = CreateCustomDataModelRequest()
api_response = api_instance.create_custom_data_model(entity_type, create_custom_data_model_request=create_custom_data_model_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_type** | **str**| The entity type of the Data Model. | [required] 
 **create_custom_data_model_request** | [**CreateCustomDataModelRequest**](CreateCustomDataModelRequest.md)| The request containing the details of the Data Model. | [optional] 

### Return type

[**CustomDataModel**](CustomDataModel.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The created Data Model |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **delete_custom_data_model**
> DeletedEntityResponse deleteCustomDataModel = delete_custom_data_model(entity_type, scope, code)

[EXPERIMENTAL] DeleteCustomDataModel: Delete a Custom Data Model

Delete a Custom Data Model. The data model will remain viewable at previous as at times, but will no longer  be part of any hierarchies.

### Example

```python
api_instance = api_client_factory.build(CustomDataModelsApi)
entity_type = 'entity_type_example' # str
scope = 'scope_example' # str
code = 'code_example' # str
api_response = api_instance.delete_custom_data_model(entity_type, scope, code)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_type** | **str**| The entity type of the Data Model. | [required] 
 **scope** | **str**| The scope of the specified Data Model. | [required] 
 **code** | **str**| The code of the specified Data Model. | [required] 

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

# **get_custom_data_model**
> CustomDataModel getCustomDataModel = get_custom_data_model(entity_type, scope, code, as_at=as_at)

[EXPERIMENTAL] GetCustomDataModel: Get a Custom Data Model

Retrieves a Custom Data Model at a given as at time.

### Example

```python
api_instance = api_client_factory.build(CustomDataModelsApi)
entity_type = 'entity_type_example' # str
scope = 'scope_example' # str
code = 'code_example' # str
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
api_response = api_instance.get_custom_data_model(entity_type, scope, code, as_at=as_at)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_type** | **str**| The entity type of the Data Model. | [required] 
 **scope** | **str**| The scope of the specified Data Model. | [required] 
 **code** | **str**| The code of the specified Data Model. | [required] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the Data Model. Defaults to return              the latest version of the Data Model if not specified. | [optional] 

### Return type

[**CustomDataModel**](CustomDataModel.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested Data Model |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **list_data_model_hierarchies**
> ResourceListOfDataModelSummary listDataModelHierarchies = list_data_model_hierarchies(as_at=as_at, filter=filter, sort_by=sort_by)

[EXPERIMENTAL] ListDataModelHierarchies: List Custom Data Model hierarchies.

Lists the data model summaries within their hierarchical structure.

### Example

```python
api_instance = api_client_factory.build(CustomDataModelsApi)
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
filter = 'filter_example' # str (optional)
sort_by = ['sort_by_example'] # List[str] (optional)
api_response = api_instance.list_data_model_hierarchies(as_at=as_at, filter=filter, sort_by=sort_by)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **as_at** | **datetime**| The asAt datetime at which to retrieve the Data Model. Defaults to return              the latest version of the Data Model if not specified. | [optional] 
 **filter** | **str**| Expression to filter the results. | [optional] 
 **sort_by** | [**List[str]**](str.md)| A list of field names or properties to sort by, each suffixed by \&quot; ASC\&quot; or \&quot; DESC\&quot;. | [optional] 

### Return type

[**ResourceListOfDataModelSummary**](ResourceListOfDataModelSummary.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | All data model hierarchies. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **list_supported_entity_types**
> ResourceListOfString listSupportedEntityTypes = list_supported_entity_types()

[EXPERIMENTAL] ListSupportedEntityTypes: List the currently supported entity types for use in Custom Data Models.

Lists the currently supported entity types available to bind with Custom Data Models.

### Example

```python
api_instance = api_client_factory.build(CustomDataModelsApi)
api_response = api_instance.list_supported_entity_types()
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
**200** | All supported entity types. |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **update_custom_data_model**
> CustomDataModel updateCustomDataModel = update_custom_data_model(entity_type, scope, code, update_custom_data_model_request=update_custom_data_model_request)

[EXPERIMENTAL] UpdateCustomDataModel: Update a Custom Data Model

Updates a Custom Data Model.

### Example

```python
api_instance = api_client_factory.build(CustomDataModelsApi)
entity_type = 'entity_type_example' # str
scope = 'scope_example' # str
code = 'code_example' # str
update_custom_data_model_request = UpdateCustomDataModelRequest()
api_response = api_instance.update_custom_data_model(entity_type, scope, code, update_custom_data_model_request=update_custom_data_model_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_type** | **str**| The entity type of the Data Model. | [required] 
 **scope** | **str**| The scope of the specified Data Model. | [required] 
 **code** | **str**| The code of the specified Data Model. | [required] 
 **update_custom_data_model_request** | [**UpdateCustomDataModelRequest**](UpdateCustomDataModelRequest.md)| The request containing the details of the Data Model. | [optional] 

### Return type

[**CustomDataModel**](CustomDataModel.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated Data Model |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

