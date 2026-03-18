# lusid.IdentifierDefinitionsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_identifier_definition**](IdentifierDefinitionsApi.md#create_identifier_definition) | **POST** /api/api/identifierdefinitions | [EXPERIMENTAL] CreateIdentifierDefinition: Create an Identifier Definition
[**delete_identifier_definition**](IdentifierDefinitionsApi.md#delete_identifier_definition) | **DELETE** /api/api/identifierdefinitions/{domain}/{identifierScope}/{identifierType} | [EXPERIMENTAL] DeleteIdentifierDefinition: Delete a particular Identifier Definition
[**get_identifier_definition**](IdentifierDefinitionsApi.md#get_identifier_definition) | **GET** /api/api/identifierdefinitions/{domain}/{identifierScope}/{identifierType} | [EXPERIMENTAL] GetIdentifierDefinition: Get a single Identifier Definition
[**list_identifier_definitions**](IdentifierDefinitionsApi.md#list_identifier_definitions) | **GET** /api/api/identifierdefinitions | [EXPERIMENTAL] ListIdentifierDefinitions: List Identifier Definitions
[**update_identifier_definition**](IdentifierDefinitionsApi.md#update_identifier_definition) | **PUT** /api/api/identifierdefinitions/{domain}/{identifierScope}/{identifierType} | [EXPERIMENTAL] UpdateIdentifierDefinition: Update Identifier Definition defined by domain, identifierScope, and identifierType


### Example

```python
from finbourne.sdk.exceptions import ApiException
from finbourne.sdk.extensions.configuration_options import ConfigurationOptions
from finbourne.sdk.services.lusid.models import *

from finbourne.sdk.extensions import (
  SyncApiClientFactory
)

from finbourne.sdk.services.lusid.api.identifier_definitions_api import IdentifierDefinitionsApi

# opts = ConfigurationOptions()
# opts.total_timeout_ms = 30_000

# uncomment the below to use an api client factory with overrides
# api_client_factory = SyncApiClientFactory(opts=opts)

api_client_factory = SyncApiClientFactory()
api_instance = api_client_factory.build(IdentifierDefinitionsApi)
```

---

# **create_identifier_definition**
> IdentifierDefinition createIdentifierDefinition = create_identifier_definition(create_identifier_definition_request=create_identifier_definition_request)

[EXPERIMENTAL] CreateIdentifierDefinition: Create an Identifier Definition

Define a new Identifier Definition

### Example

```python
api_instance = api_client_factory.build(IdentifierDefinitionsApi)
create_identifier_definition_request = CreateIdentifierDefinitionRequest()
api_response = api_instance.create_identifier_definition(create_identifier_definition_request=create_identifier_definition_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_identifier_definition_request** | [**CreateIdentifierDefinitionRequest**](CreateIdentifierDefinitionRequest.md)| The request defining the new definition | [optional] 

### Return type

[**IdentifierDefinition**](IdentifierDefinition.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The created Identifier Definition |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **delete_identifier_definition**
> DeletedEntityResponse deleteIdentifierDefinition = delete_identifier_definition(domain, identifier_scope, identifier_type)

[EXPERIMENTAL] DeleteIdentifierDefinition: Delete a particular Identifier Definition

The deletion will take effect from the Identifier Definition deletion datetime.  i.e. will no longer exist at any asAt datetime after the asAt datetime of deletion.

### Example

```python
api_instance = api_client_factory.build(IdentifierDefinitionsApi)
domain = 'domain_example' # str
identifier_scope = 'identifier_scope_example' # str
identifier_type = 'identifier_type_example' # str
api_response = api_instance.delete_identifier_definition(domain, identifier_scope, identifier_type)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| The type of entity to which the identifier relates | [required] 
 **identifier_scope** | **str**| The scope that the identifier exists in | [required] 
 **identifier_type** | **str**| What the identifier represents. Together with \&quot;domain\&quot; and \&quot;identifierScope\&quot; this uniquely identifies the identifier definition | [required] 

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

# **get_identifier_definition**
> IdentifierDefinition getIdentifierDefinition = get_identifier_definition(domain, identifier_scope, identifier_type, as_at=as_at, effective_at=effective_at, property_keys=property_keys)

[EXPERIMENTAL] GetIdentifierDefinition: Get a single Identifier Definition

Get a single Identifier Definition using domain, identifierScope, identifierType, and an optional asAt              - defaulting to latest if not specified

### Example

```python
api_instance = api_client_factory.build(IdentifierDefinitionsApi)
domain = 'domain_example' # str
identifier_scope = 'identifier_scope_example' # str
identifier_type = 'identifier_type_example' # str
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
effective_at = 'effective_at_example' # str (optional)
property_keys = ['property_keys_example'] # List[str] (optional)
api_response = api_instance.get_identifier_definition(domain, identifier_scope, identifier_type, as_at=as_at, effective_at=effective_at, property_keys=property_keys)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| The type of entity to which the identifier relates. | [required] 
 **identifier_scope** | **str**| The scope that the identifier exists in | [required] 
 **identifier_type** | **str**| What the identifier represents. Together with \&quot;domain\&quot; and \&quot;identifierScope\&quot; this uniquely identifies the identifier definition | [required] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the Identifier Definition. Defaults to return              the latest version of the definition if not specified. | [optional] 
 **effective_at** | **str**| The effectiveAt datetime at which to retrieve the Identifier Definitions.              Since Identifier Definitions exist for all effective time, this will only apply to properties (if requested)              on the Identifier Definition. | [optional] 
 **property_keys** | [**List[str]**](str.md)| A list of property keys from the &#39;IdentifierDefinition&#39; domain to decorate onto the Identifier Definition.              These must take the format {domain}/{scope}/{code}. If no properties are specified, then no properties will be returned. | [optional] 

### Return type

[**IdentifierDefinition**](IdentifierDefinition.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested Identifier Definition |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **list_identifier_definitions**
> PagedResourceListOfIdentifierDefinition listIdentifierDefinitions = list_identifier_definitions(effective_at=effective_at, as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by, property_keys=property_keys)

[EXPERIMENTAL] ListIdentifierDefinitions: List Identifier Definitions

Retrieves all Identifier Definitions that fit the filter, in a specific order if sortBy is provided  Supports pagination

### Example

```python
api_instance = api_client_factory.build(IdentifierDefinitionsApi)
effective_at = 'effective_at_example' # str (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
page = 'page_example' # str (optional)
limit = 56 # int (optional)
filter = 'filter_example' # str (optional)
sort_by = ['sort_by_example'] # List[str] (optional)
property_keys = ['property_keys_example'] # List[str] (optional)
api_response = api_instance.list_identifier_definitions(effective_at=effective_at, as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by, property_keys=property_keys)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **effective_at** | **str**| The effectiveAt datetime at which to retrieve the Identifier Definitions.              Since Identifier Definitions exist for all effective time, this will only apply to properties (if requested)              on the Identifier Definition. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the Identifier Definitions. Defaults to return the latest              version of the Identifier Definitions if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing Identifier Definitions from a previous call to list              Identifier Definitions. This value is returned from the previous call. If a pagination token is provided the sortBy,              filter, effectiveAt, and asAt fields must not have changed since the original request. | [optional] 
 **limit** | **int**| When paginating, limit the number of returned results to this many per page. | [optional] 
 **filter** | **str**| Expression to filter the result set. Read more about filtering results from LUSID here:              https://support.lusid.com/filtering-results-from-lusid. | [optional] 
 **sort_by** | [**List[str]**](str.md)| A list of field names to sort by, each suffixed by \&quot; ASC\&quot; or \&quot; DESC\&quot; | [optional] 
 **property_keys** | [**List[str]**](str.md)| A list of property keys from the &#39;IdentifierDefinition&#39; domain to decorate onto the Identifier Definition.              These must take the format {domain}/{scope}/{code}. | [optional] 

### Return type

[**PagedResourceListOfIdentifierDefinition**](PagedResourceListOfIdentifierDefinition.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested list of Identifier Definitions |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **update_identifier_definition**
> IdentifierDefinition updateIdentifierDefinition = update_identifier_definition(domain, identifier_scope, identifier_type, update_identifier_definition_request=update_identifier_definition_request)

[EXPERIMENTAL] UpdateIdentifierDefinition: Update Identifier Definition defined by domain, identifierScope, and identifierType

Overwrites an existing Identifier Definition.

### Example

```python
api_instance = api_client_factory.build(IdentifierDefinitionsApi)
domain = 'domain_example' # str
identifier_scope = 'identifier_scope_example' # str
identifier_type = 'identifier_type_example' # str
update_identifier_definition_request = UpdateIdentifierDefinitionRequest()
api_response = api_instance.update_identifier_definition(domain, identifier_scope, identifier_type, update_identifier_definition_request=update_identifier_definition_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| The type of entity to which the identifier relates | [required] 
 **identifier_scope** | **str**| The scope that the identifier exists in | [required] 
 **identifier_type** | **str**| What the identifier represents. Together with \&quot;domain\&quot; and \&quot;identifierScope\&quot; this uniquely identifies the Identifier Definition | [required] 
 **update_identifier_definition_request** | [**UpdateIdentifierDefinitionRequest**](UpdateIdentifierDefinitionRequest.md)| The request containing the updated details of the Identifier Definition. | [optional] 

### Return type

[**IdentifierDefinition**](IdentifierDefinition.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated version of the requested Identifier Definition |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

