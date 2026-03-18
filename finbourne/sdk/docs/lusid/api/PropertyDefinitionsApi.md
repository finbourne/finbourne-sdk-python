# lusid.PropertyDefinitionsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_derived_property_definition**](PropertyDefinitionsApi.md#create_derived_property_definition) | **POST** /api/api/propertydefinitions/derived | [EARLY ACCESS] CreateDerivedPropertyDefinition: Create derived property definition
[**create_property_definition**](PropertyDefinitionsApi.md#create_property_definition) | **POST** /api/api/propertydefinitions | CreatePropertyDefinition: Create property definition
[**delete_property_definition**](PropertyDefinitionsApi.md#delete_property_definition) | **DELETE** /api/api/propertydefinitions/{domain}/{scope}/{code} | DeletePropertyDefinition: Delete property definition
[**delete_property_definition_properties**](PropertyDefinitionsApi.md#delete_property_definition_properties) | **POST** /api/api/propertydefinitions/{domain}/{scope}/{code}/properties/$delete | [EARLY ACCESS] DeletePropertyDefinitionProperties: Delete property definition properties
[**get_derived_formula_explanation**](PropertyDefinitionsApi.md#get_derived_formula_explanation) | **POST** /api/api/propertydefinitions/derived/$formulaExplanation | GetDerivedFormulaExplanation: Get explanation of a derived property formula
[**get_multiple_property_definitions**](PropertyDefinitionsApi.md#get_multiple_property_definitions) | **GET** /api/api/propertydefinitions | GetMultiplePropertyDefinitions: Get multiple property definitions
[**get_property_definition**](PropertyDefinitionsApi.md#get_property_definition) | **GET** /api/api/propertydefinitions/{domain}/{scope}/{code} | GetPropertyDefinition: Get property definition
[**get_property_definition_property_time_series**](PropertyDefinitionsApi.md#get_property_definition_property_time_series) | **GET** /api/api/propertydefinitions/{domain}/{scope}/{code}/properties/time-series | [EARLY ACCESS] GetPropertyDefinitionPropertyTimeSeries: Get Property Definition Property Time Series
[**list_property_definitions**](PropertyDefinitionsApi.md#list_property_definitions) | **GET** /api/api/propertydefinitions/$list | ListPropertyDefinitions: List property definitions
[**update_derived_property_definition**](PropertyDefinitionsApi.md#update_derived_property_definition) | **PUT** /api/api/propertydefinitions/derived/{domain}/{scope}/{code} | [EARLY ACCESS] UpdateDerivedPropertyDefinition: Update a pre-existing derived property definition
[**update_property_definition**](PropertyDefinitionsApi.md#update_property_definition) | **PUT** /api/api/propertydefinitions/{domain}/{scope}/{code} | UpdatePropertyDefinition: Update property definition
[**upsert_property_definition_properties**](PropertyDefinitionsApi.md#upsert_property_definition_properties) | **POST** /api/api/propertydefinitions/{domain}/{scope}/{code}/properties | UpsertPropertyDefinitionProperties: Upsert properties to a property definition


### Example

```python
from finbourne.sdk.exceptions import ApiException
from finbourne.sdk.extensions.configuration_options import ConfigurationOptions
from finbourne.sdk.services.lusid.models import *

from finbourne.sdk.extensions import (
  SyncApiClientFactory
)

from finbourne.sdk.services.lusid.api.property_definitions_api import PropertyDefinitionsApi

# opts = ConfigurationOptions()
# opts.total_timeout_ms = 30_000

# uncomment the below to use an api client factory with overrides
# api_client_factory = SyncApiClientFactory(opts=opts)

api_client_factory = SyncApiClientFactory()
api_instance = api_client_factory.build(PropertyDefinitionsApi)
```

---

# **create_derived_property_definition**
> PropertyDefinition createDerivedPropertyDefinition = create_derived_property_definition(create_derived_property_definition_request)

[EARLY ACCESS] CreateDerivedPropertyDefinition: Create derived property definition

Define a new derived property.

### Example

```python
api_instance = api_client_factory.build(PropertyDefinitionsApi)
create_derived_property_definition_request = CreateDerivedPropertyDefinitionRequest()
api_response = api_instance.create_derived_property_definition(create_derived_property_definition_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_derived_property_definition_request** | [**CreateDerivedPropertyDefinitionRequest**](CreateDerivedPropertyDefinitionRequest.md)| The definition of the new derived property. | [required] 

### Return type

[**PropertyDefinition**](PropertyDefinition.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The newly created derived property definition |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **create_property_definition**
> PropertyDefinition createPropertyDefinition = create_property_definition(create_property_definition_request)

CreatePropertyDefinition: Create property definition

Define a new property.

### Example

```python
api_instance = api_client_factory.build(PropertyDefinitionsApi)
create_property_definition_request = CreatePropertyDefinitionRequest()
api_response = api_instance.create_property_definition(create_property_definition_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_property_definition_request** | [**CreatePropertyDefinitionRequest**](CreatePropertyDefinitionRequest.md)| The definition of the new property. | [required] 

### Return type

[**PropertyDefinition**](PropertyDefinition.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The newly created property definition |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **delete_property_definition**
> DeletedEntityResponse deletePropertyDefinition = delete_property_definition(domain, scope, code)

DeletePropertyDefinition: Delete property definition

Delete the definition of the specified property.

### Example

```python
api_instance = api_client_factory.build(PropertyDefinitionsApi)
domain = 'domain_example' # str
scope = 'scope_example' # str
code = 'code_example' # str
api_response = api_instance.delete_property_definition(domain, scope, code)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| The domain of the property to be deleted. | [required] 
 **scope** | **str**| The scope of the property to be deleted. | [required] 
 **code** | **str**| The code of the property to be deleted. Together with the domain and scope this uniquely              identifies the property. | [required] 

### Return type

[**DeletedEntityResponse**](DeletedEntityResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The time that the property definition was deleted |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **delete_property_definition_properties**
> DeletedEntityResponse deletePropertyDefinitionProperties = delete_property_definition_properties(domain, scope, code, request_body, effective_at=effective_at)

[EARLY ACCESS] DeletePropertyDefinitionProperties: Delete property definition properties

Delete one or more properties from a single property definition. If the properties are time-variant then an effective date time from which the  properties will be deleted must be specified. If the properties are perpetual then it is invalid to specify an effective date time for deletion.

### Example

```python
api_instance = api_client_factory.build(PropertyDefinitionsApi)
domain = 'domain_example' # str
scope = 'scope_example' # str
code = 'code_example' # str
request_body = ["PropertyDefinition/MyScope/MyPropertyName","PropertyDefinition/MyScope/MyPropertyName2"] # List[str]
effective_at = 'effective_at_example' # str (optional)
api_response = api_instance.delete_property_definition_properties(domain, scope, code, request_body, effective_at=effective_at)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| The domain of the property definition to delete properties from. | [required] 
 **scope** | **str**| The scope of the property definition to delete properties from. | [required] 
 **code** | **str**| The code of the property definition to delete properties from. | [required] 
 **request_body** | [**List[str]**](str.md)| The property keys of the properties to delete. These must take the format              {domain}/{scope}/{code} e.g \&quot;PropertyDefinition/myScope/someAttributeKey\&quot;. Each property must be from the \&quot;PropertyDefinition\&quot; domain. | [required] 
 **effective_at** | **str**| The effective datetime or cut label at which to delete time-variant properties from.              The property must exist at the specified &#39;effectiveAt&#39; datetime. If the &#39;effectiveAt&#39; is not provided or is before              the time-variant property exists then a failure is returned. Do not specify this parameter if an of the properties to delete are perpetual. | [optional] 

### Return type

[**DeletedEntityResponse**](DeletedEntityResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The datetime that the properties were deleted from the specified definition |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_derived_formula_explanation**
> DerivedPropertyComponent getDerivedFormulaExplanation = get_derived_formula_explanation(derivation_formula_explain_request, as_at=as_at, effective_at=effective_at)

GetDerivedFormulaExplanation: Get explanation of a derived property formula

Produces a manifest that shows the nested hierarchy of any source properties and the actions taken upon them to create the derived property.  This can either be done against an existing entity, which will produce a manifest that includes the values of the source properties  at the specified effective date time, or it can be done without providing an entity which will produce a manifest without values.

### Example

```python
api_instance = api_client_factory.build(PropertyDefinitionsApi)
derivation_formula_explain_request = DerivationFormulaExplainRequest()
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
effective_at = 'effective_at_example' # str (optional)
api_response = api_instance.get_derived_formula_explanation(derivation_formula_explain_request, as_at=as_at, effective_at=effective_at)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **derivation_formula_explain_request** | [**DerivationFormulaExplainRequest**](DerivationFormulaExplainRequest.md)| Information about the derivation formula to explain, and optionally, the entity to resolve the formula against. | [required] 
 **as_at** | **datetime**| The asAt datetime at which to resolve the entity. Defaults to returning the latest asAt in LUSID              if not specified. | [optional] 
 **effective_at** | **str**| The effective datetime or cut label at which to resolve the entity. Defaults to the current LUSID              system datetime if not specified. | [optional] 

### Return type

[**DerivedPropertyComponent**](DerivedPropertyComponent.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested derived property formula components. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_multiple_property_definitions**
> ResourceListOfPropertyDefinition getMultiplePropertyDefinitions = get_multiple_property_definitions(property_keys, as_at=as_at, filter=filter, effective_at=effective_at)

GetMultiplePropertyDefinitions: Get multiple property definitions

Retrieve the definition of one or more specified properties.

### Example

```python
api_instance = api_client_factory.build(PropertyDefinitionsApi)
property_keys = ['property_keys_example'] # List[str]
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
filter = 'filter_example' # str (optional)
effective_at = 'effective_at_example' # str (optional)
api_response = api_instance.get_multiple_property_definitions(property_keys, as_at=as_at, filter=filter, effective_at=effective_at)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_keys** | [**List[str]**](str.md)| One or more property keys which identify each property that a definition should              be retrieved for. The format for each property key is {domain}/{scope}/{code}, e.g. &#39;Portfolio/Manager/Id&#39;. | [required] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the property definitions. Defaults to return              the latest version of each definition if not specified. | [optional] 
 **filter** | **str**| Expression to filter the result set.               For example, to filter on the Lifetime, use \&quot;lifeTime eq &#39;Perpetual&#39;\&quot;              Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. | [optional] 
 **effective_at** | **str**| The effective datetime or cut label at which to list properties attached to the Property Definition.              Defaults to the current LUSID system datetime if not specified. | [optional] 

### Return type

[**ResourceListOfPropertyDefinition**](ResourceListOfPropertyDefinition.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested property definitions |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_property_definition**
> PropertyDefinition getPropertyDefinition = get_property_definition(domain, scope, code, as_at=as_at, effective_at=effective_at)

GetPropertyDefinition: Get property definition

Retrieve the definition of a specified property.

### Example

```python
api_instance = api_client_factory.build(PropertyDefinitionsApi)
domain = 'domain_example' # str
scope = 'scope_example' # str
code = 'code_example' # str
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
effective_at = 'effective_at_example' # str (optional)
api_response = api_instance.get_property_definition(domain, scope, code, as_at=as_at, effective_at=effective_at)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| The domain of the specified property. | [required] 
 **scope** | **str**| The scope of the specified property. | [required] 
 **code** | **str**| The code of the specified property. Together with the domain and scope this uniquely              identifies the property. | [required] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the property definition. Defaults to return              the latest version of the definition if not specified. | [optional] 
 **effective_at** | **str**| The effective datetime or cut label at which to list properties attached to the Property Definition.              Defaults to the current LUSID system datetime if not specified. | [optional] 

### Return type

[**PropertyDefinition**](PropertyDefinition.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested property definition |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_property_definition_property_time_series**
> ResourceListOfPropertyInterval getPropertyDefinitionPropertyTimeSeries = get_property_definition_property_time_series(domain, scope, code, property_key, as_at=as_at, filter=filter, page=page, limit=limit)

[EARLY ACCESS] GetPropertyDefinitionPropertyTimeSeries: Get Property Definition Property Time Series

List the complete time series of a property definition property.

### Example

```python
api_instance = api_client_factory.build(PropertyDefinitionsApi)
domain = 'domain_example' # str
scope = 'scope_example' # str
code = 'code_example' # str
property_key = 'property_key_example' # str
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
filter = 'filter_example' # str (optional)
page = 'page_example' # str (optional)
limit = 56 # int (optional)
api_response = api_instance.get_property_definition_property_time_series(domain, scope, code, property_key, as_at=as_at, filter=filter, page=page, limit=limit)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| The domain of the property definition to which the property is attached | [required] 
 **scope** | **str**| The scope of the property definition to which the property is attached | [required] 
 **code** | **str**| The code of the property definition to which the property is attached | [required] 
 **property_key** | **str**| The property key of the property whose history to show. This must be from the \&quot;Property Definition\&quot; domain and in the format              {domain}/{scope}/{code}, for example \&quot;PropertyDefinition/myScope/someAttributeKey\&quot;. | [required] 
 **as_at** | **datetime**| The asAt datetime at which to show the history. Defaults to the current datetime if not specified. | [optional] 
 **filter** | **str**| Expression to filter the results. Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. | [optional] 
 **page** | **str**| The pagination token to use to continue listing properties from a previous call to get property time series.              This value is returned from the previous call. If a pagination token is provided the filter and asAt fields              must not have changed since the original request. | [optional] 
 **limit** | **int**| When paginating, limit the number of returned results to this many. | [optional] 

### Return type

[**ResourceListOfPropertyInterval**](ResourceListOfPropertyInterval.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The time series of the property |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **list_property_definitions**
> PagedResourceListOfPropertyDefinition listPropertyDefinitions = list_property_definitions(effective_at=effective_at, as_at=as_at, property_keys=property_keys, page=page, limit=limit, filter=filter, sort_by=sort_by)

ListPropertyDefinitions: List property definitions

List all the property definitions matching particular criteria.

### Example

```python
api_instance = api_client_factory.build(PropertyDefinitionsApi)
effective_at = 'effective_at_example' # str (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
property_keys = ['property_keys_example'] # List[str] (optional)
page = 'page_example' # str (optional)
limit = 56 # int (optional)
filter = 'filter_example' # str (optional)
sort_by = ['sort_by_example'] # List[str] (optional)
api_response = api_instance.list_property_definitions(effective_at=effective_at, as_at=as_at, property_keys=property_keys, page=page, limit=limit, filter=filter, sort_by=sort_by)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **effective_at** | **str**| The effective datetime or cut label at which to list the property definitions. Defaults to the current LUSID              system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to list the property definitions. Defaults to returning the latest version              of each property definition if not specified. | [optional] 
 **property_keys** | [**List[str]**](str.md)| A list of property keys from the &#39;Property Definition&#39; domain to decorate onto              property definitions. These must take the format              {domain}/{scope}/{code} e.g \&quot;PropertyDefinition/myScope/someAttributeKey\&quot;. Each property must be from the \&quot;PropertyDefinition\&quot; domain. | [optional] 
 **page** | **str**| The pagination token to use to continue listing property definitions; this              value is returned from the previous call. If a pagination token is provided, the filter, effectiveAt              and asAt fields must not have changed since the original request. | [optional] 
 **limit** | **int**| When paginating, limit the results to this number. Defaults to 100 if not specified. | [optional] 
 **filter** | **str**| Expression to filter the results.              For example, to filter on the display name, specify \&quot;DisplayName eq &#39;DisplayName&#39;\&quot;. For more information about filtering              results, see https://support.lusid.com/knowledgebase/article/KA-01914. | [optional] 
 **sort_by** | [**List[str]**](str.md)| A list of field names or properties to sort by, each suffixed by \&quot; ASC\&quot; or \&quot; DESC\&quot; | [optional] 

### Return type

[**PagedResourceListOfPropertyDefinition**](PagedResourceListOfPropertyDefinition.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested property definitions |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **update_derived_property_definition**
> PropertyDefinition updateDerivedPropertyDefinition = update_derived_property_definition(domain, scope, code, update_derived_property_definition_request)

[EARLY ACCESS] UpdateDerivedPropertyDefinition: Update a pre-existing derived property definition

This will fail if the property definition does not exist

### Example

```python
api_instance = api_client_factory.build(PropertyDefinitionsApi)
domain = 'domain_example' # str
scope = 'scope_example' # str
code = 'code_example' # str
update_derived_property_definition_request = UpdateDerivedPropertyDefinitionRequest()
api_response = api_instance.update_derived_property_definition(domain, scope, code, update_derived_property_definition_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| Domain of the property definition | [required] 
 **scope** | **str**| Scope of the property definition | [required] 
 **code** | **str**| Code of the property definition | [required] 
 **update_derived_property_definition_request** | [**UpdateDerivedPropertyDefinitionRequest**](UpdateDerivedPropertyDefinitionRequest.md)| Information about the derived property definition being updated | [required] 

### Return type

[**PropertyDefinition**](PropertyDefinition.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated derived property definition |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **update_property_definition**
> PropertyDefinition updatePropertyDefinition = update_property_definition(domain, scope, code, update_property_definition_request)

UpdatePropertyDefinition: Update property definition

Update the definition of a specified existing property. Not all elements within a property definition  are modifiable due to the potential implications for values already stored against the property.

### Example

```python
api_instance = api_client_factory.build(PropertyDefinitionsApi)
domain = 'domain_example' # str
scope = 'scope_example' # str
code = 'code_example' # str
update_property_definition_request = UpdatePropertyDefinitionRequest()
api_response = api_instance.update_property_definition(domain, scope, code, update_property_definition_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| The domain of the property being updated. | [required] 
 **scope** | **str**| The scope of the property being updated. | [required] 
 **code** | **str**| The code of the property being updated. Together with the domain and scope this uniquely              identifies the property. | [required] 
 **update_property_definition_request** | [**UpdatePropertyDefinitionRequest**](UpdatePropertyDefinitionRequest.md)| The updated definition of the property. | [required] 

### Return type

[**PropertyDefinition**](PropertyDefinition.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated property definition |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **upsert_property_definition_properties**
> BatchUpsertPropertyDefinitionPropertiesResponse upsertPropertyDefinitionProperties = upsert_property_definition_properties(domain, scope, code, request_body, success_mode=success_mode)

UpsertPropertyDefinitionProperties: Upsert properties to a property definition

Create or update properties for a particular property definition

### Example

```python
api_instance = api_client_factory.build(PropertyDefinitionsApi)
domain = 'domain_example' # str
scope = 'scope_example' # str
code = 'code_example' # str
request_body = {"PropertyDefinition/MyScope/FundManagerName":{"key":"PropertyDefinition/MyScope/FundManagerName","value":{"labelValue":"Smith"},"effectiveFrom":"2018-03-05T00:00:00.0000000+00:00"},"PropertyDefinition/MyScope/SomeProperty":{"key":"PropertyDefinition/MyScope/SomeProperty","value":{"labelValue":"SomeValue"},"effectiveFrom":"2016-01-01T00:00:00.0000000+00:00"},"PropertyDefinition/MyScope/AnotherProperty":{"key":"PropertyDefinition/MyScope/AnotherProperty","value":{"labelValue":"AnotherValue"},"effectiveFrom":"2018-03-05T00:00:00.0000000+00:00","effectiveUntil":"2020-01-01T00:00:00.0000000+00:00"},"PropertyDefinition/MyScope/ReBalanceInterval":{"key":"PropertyDefinition/MyScope/ReBalanceInterval","value":{"metricValue":{"value":30.0,"unit":"Days"}}}} # Dict[str, ModelProperty]
success_mode = 'Partial' # str (optional)
api_response = api_instance.upsert_property_definition_properties(domain, scope, code, request_body, success_mode=success_mode)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| The domain of the specified property. | [required] 
 **scope** | **str**| The scope of the specified property. | [required] 
 **code** | **str**| The code of the specified property. Together with the domain and scope this uniquely | [required] 
 **request_body** | [**Dict[str, ModelProperty]**](ModelProperty.md)| The properties to be created or updated. Each property in              the request must be keyed by its unique property key. This has the format {domain}/{scope}/{code}, for example              &#39;PropertyDefinition/Manager/Id&#39;. | [required] 
 **success_mode** | **str**| Whether the batch request should fail Atomically or in a Partial fashion - Allowed Values: Atomic, Partial. | [optional] [default to &#39;Partial&#39;]

### Return type

[**BatchUpsertPropertyDefinitionPropertiesResponse**](BatchUpsertPropertyDefinitionPropertiesResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The asAt datetime at which the properties were updated or created. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

