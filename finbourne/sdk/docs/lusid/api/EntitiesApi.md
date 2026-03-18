# lusid.EntitiesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_custom_entity_by_entity_unique_id**](EntitiesApi.md#get_custom_entity_by_entity_unique_id) | **GET** /api/api/entities/customentities/{entityUniqueId} | GetCustomEntityByEntityUniqueId: Get a Custom Entity instance by its EntityUniqueId
[**get_data_type_by_entity_unique_id**](EntitiesApi.md#get_data_type_by_entity_unique_id) | **GET** /api/api/entities/datatypes/{entityUniqueId} | GetDataTypeByEntityUniqueId: Get DataType by EntityUniqueId
[**get_entity_history**](EntitiesApi.md#get_entity_history) | **GET** /api/api/entities/{entityType}/{entityUniqueId}/history | GetEntityHistory: List an entity&#39;s history information
[**get_instrument_by_entity_unique_id**](EntitiesApi.md#get_instrument_by_entity_unique_id) | **GET** /api/api/entities/instruments/{entityUniqueId} | GetInstrumentByEntityUniqueId: Get instrument by EntityUniqueId
[**get_portfolio_by_entity_unique_id**](EntitiesApi.md#get_portfolio_by_entity_unique_id) | **GET** /api/api/entities/portfolios/{entityUniqueId} | GetPortfolioByEntityUniqueId: Get portfolio by EntityUniqueId
[**get_portfolio_changes**](EntitiesApi.md#get_portfolio_changes) | **GET** /api/api/entities/changes/portfolios | GetPortfolioChanges: Get the next change to each portfolio in a scope.
[**get_property_definition_by_entity_unique_id**](EntitiesApi.md#get_property_definition_by_entity_unique_id) | **GET** /api/api/entities/propertydefinitions/{entityUniqueId} | GetPropertyDefinitionByEntityUniqueId: Get property definition by EntityUniqueId


### Example

```python
from finbourne.sdk.exceptions import ApiException
from finbourne.sdk.extensions.configuration_options import ConfigurationOptions
from finbourne.sdk.services.lusid.models import *

from finbourne.sdk.extensions import (
  SyncApiClientFactory
)

from finbourne.sdk.services.lusid.api.entities_api import EntitiesApi

# opts = ConfigurationOptions()
# opts.total_timeout_ms = 30_000

# uncomment the below to use an api client factory with overrides
# api_client_factory = SyncApiClientFactory(opts=opts)

api_client_factory = SyncApiClientFactory()
api_instance = api_client_factory.build(EntitiesApi)
```

---

# **get_custom_entity_by_entity_unique_id**
> CustomEntityEntity getCustomEntityByEntityUniqueId = get_custom_entity_by_entity_unique_id(entity_unique_id, effective_at=effective_at, as_at=as_at, previews=previews)

GetCustomEntityByEntityUniqueId: Get a Custom Entity instance by its EntityUniqueId

Retrieve a particular Custom Entity instance.  If the Custom Entity is deleted, this will return the state of the Custom Entity immediately prior to deletion.

### Example

```python
api_instance = api_client_factory.build(EntitiesApi)
entity_unique_id = 'entity_unique_id_example' # str
effective_at = 'effective_at_example' # str (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
previews = ['previews_example'] # List[str] (optional)
api_response = api_instance.get_custom_entity_by_entity_unique_id(entity_unique_id, effective_at=effective_at, as_at=as_at, previews=previews)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_unique_id** | **str**| The universally unique identifier of the Custom Entity. | [required] 
 **effective_at** | **str**| The effective datetime or cut label at which to retrieve the Custom Entity. Defaults to the current LUSID system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the Custom Entity. Defaults to returning the latest version of the Custom Entity if not specified. | [optional] 
 **previews** | [**List[str]**](str.md)| The ids of the staged modifications to be previewed in the response. | [optional] 

### Return type

[**CustomEntityEntity**](CustomEntityEntity.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested CustomEntity |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_data_type_by_entity_unique_id**
> DataTypeEntity getDataTypeByEntityUniqueId = get_data_type_by_entity_unique_id(entity_unique_id, as_at=as_at, previews=previews)

GetDataTypeByEntityUniqueId: Get DataType by EntityUniqueId

Retrieve the definition of a particular DataType.  If the DataType is deleted, this will return the state of the DataType immediately prior to deletion.

### Example

```python
api_instance = api_client_factory.build(EntitiesApi)
entity_unique_id = 'entity_unique_id_example' # str
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
previews = ['previews_example'] # List[str] (optional)
api_response = api_instance.get_data_type_by_entity_unique_id(entity_unique_id, as_at=as_at, previews=previews)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_unique_id** | **str**| The universally unique identifier of the DataType definition. | [required] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the DataType definition. Defaults to returning the latest version of the DataType definition if not specified. | [optional] 
 **previews** | [**List[str]**](str.md)| The ids of the staged modifications to be previewed in the response. | [optional] 

### Return type

[**DataTypeEntity**](DataTypeEntity.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested DataType entity |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_entity_history**
> ResourceListOfChangeInterval getEntityHistory = get_entity_history(entity_type, entity_unique_id, as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by)

GetEntityHistory: List an entity's history information

Retrieve a page of an entity's change history up to a particular point in AsAt time.

### Example

```python
api_instance = api_client_factory.build(EntitiesApi)
entity_type = 'entity_type_example' # str
entity_unique_id = 'entity_unique_id_example' # str
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
page = 'page_example' # str (optional)
limit = 56 # int (optional)
filter = 'filter_example' # str (optional)
sort_by = ['sort_by_example'] # List[str] (optional)
api_response = api_instance.get_entity_history(entity_type, entity_unique_id, as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_type** | **str**| The type of the entity to list the change history for. | [required] 
 **entity_unique_id** | **str**| The universally unique identifier of the entity. | [required] 
 **as_at** | **datetime**| The asAt datetime at which to list change history information. Defaults to return the change history at the latest datetime if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing change history information from a previous call to list change              history information. This value is returned from the previous call. If a pagination token is provided the filter, sortBy              and asAt fields must not have changed since the original request. | [optional] 
 **limit** | **int**| When paginating, limit the number of returned results to this many. Defaults to 100 if not specified. | [optional] 
 **filter** | **str**| Expression to filter the result set.              Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. | [optional] 
 **sort_by** | [**List[str]**](str.md)| A list of field names suffixed by \&quot; ASC\&quot; or \&quot; DESC\&quot; | [optional] 

### Return type

[**ResourceListOfChangeInterval**](ResourceListOfChangeInterval.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The change history of the provided entity. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_instrument_by_entity_unique_id**
> InstrumentEntity getInstrumentByEntityUniqueId = get_instrument_by_entity_unique_id(entity_unique_id, effective_at=effective_at, as_at=as_at, previews=previews, data_model_scope=data_model_scope, data_model_code=data_model_code)

GetInstrumentByEntityUniqueId: Get instrument by EntityUniqueId

Retrieve the definition of a particular instrument.  If the instrument is deleted, this will return the state of the instrument immediately prior to deletion.

### Example

```python
api_instance = api_client_factory.build(EntitiesApi)
entity_unique_id = 'entity_unique_id_example' # str
effective_at = 'effective_at_example' # str (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
previews = ['previews_example'] # List[str] (optional)
data_model_scope = 'data_model_scope_example' # str (optional)
data_model_code = 'data_model_code_example' # str (optional)
api_response = api_instance.get_instrument_by_entity_unique_id(entity_unique_id, effective_at=effective_at, as_at=as_at, previews=previews, data_model_scope=data_model_scope, data_model_code=data_model_code)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_unique_id** | **str**| The universally unique identifier of the instrument definition. | [required] 
 **effective_at** | **str**| The effective datetime or cut label at which to retrieve the Instrument definition. Defaults to the current LUSID system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the instrument definition. Defaults to returning the latest version of the instrument definition if not specified. | [optional] 
 **previews** | [**List[str]**](str.md)| The ids of the staged modifications to be previewed in the response. | [optional] 
 **data_model_scope** | **str**| The optional scope of a Custom Data Model to use. | [optional] 
 **data_model_code** | **str**| The optional code of a Custom Data Model to use. | [optional] 

### Return type

[**InstrumentEntity**](InstrumentEntity.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested instrument entity |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_portfolio_by_entity_unique_id**
> PortfolioEntity getPortfolioByEntityUniqueId = get_portfolio_by_entity_unique_id(entity_unique_id, effective_at=effective_at, as_at=as_at, previews=previews)

GetPortfolioByEntityUniqueId: Get portfolio by EntityUniqueId

Retrieve the definition of a particular portfolio.  If the portfolio is deleted, this will return the state of the portfolio immediately prior to deletion.

### Example

```python
api_instance = api_client_factory.build(EntitiesApi)
entity_unique_id = 'entity_unique_id_example' # str
effective_at = 'effective_at_example' # str (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
previews = ['previews_example'] # List[str] (optional)
api_response = api_instance.get_portfolio_by_entity_unique_id(entity_unique_id, effective_at=effective_at, as_at=as_at, previews=previews)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_unique_id** | **str**| The universally unique identifier of the portfolio definition. | [required] 
 **effective_at** | **str**| The effective datetime or cut label at which to retrieve the portfolio definition. Defaults to the current LUSID system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the portfolio definition. Defaults to returning the latest version of the portfolio definition if not specified. | [optional] 
 **previews** | [**List[str]**](str.md)| The ids of the staged modifications to be previewed in the response. | [optional] 

### Return type

[**PortfolioEntity**](PortfolioEntity.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested portfolio entity |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_portfolio_changes**
> ResourceListOfChange getPortfolioChanges = get_portfolio_changes(scope, effective_at, as_at=as_at)

GetPortfolioChanges: Get the next change to each portfolio in a scope.

Gets the time of the next (earliest effective at) modification (correction and/or amendment) to each portfolio in a scope relative to a point in bitemporal time.  Includes changes from parent portfolios in different scopes.  Excludes changes from subscriptions (e.g corporate actions).

### Example

```python
api_instance = api_client_factory.build(EntitiesApi)
scope = 'scope_example' # str
effective_at = 'effective_at_example' # str
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
api_response = api_instance.get_portfolio_changes(scope, effective_at, as_at=as_at)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope | [required] 
 **effective_at** | **str**| The effective date of the origin. | [required] 
 **as_at** | **datetime**| The as-at date of the origin. | [optional] 

### Return type

[**ResourceListOfChange**](ResourceListOfChange.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | The details of the input related failure |  -  |
**200** | A list of portfolio changes in the requested scope relative to the specified time. |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_property_definition_by_entity_unique_id**
> PropertyDefinitionEntity getPropertyDefinitionByEntityUniqueId = get_property_definition_by_entity_unique_id(entity_unique_id, effective_at=effective_at, as_at=as_at, previews=previews)

GetPropertyDefinitionByEntityUniqueId: Get property definition by EntityUniqueId

Retrieve a particular property definition.  If the property definition is deleted, this will return the state of the property definition immediately prior to deletion.

### Example

```python
api_instance = api_client_factory.build(EntitiesApi)
entity_unique_id = 'entity_unique_id_example' # str
effective_at = 'effective_at_example' # str (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
previews = ['previews_example'] # List[str] (optional)
api_response = api_instance.get_property_definition_by_entity_unique_id(entity_unique_id, effective_at=effective_at, as_at=as_at, previews=previews)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_unique_id** | **str**| The universally unique identifier of the property definition. | [required] 
 **effective_at** | **str**| The effective datetime at which to retrieve the property definition. Defaults to the current LUSID system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the property definition. Defaults to returning the latest version of the property definition if not specified. | [optional] 
 **previews** | [**List[str]**](str.md)| The ids of the staged modifications to be previewed in the response. | [optional] 

### Return type

[**PropertyDefinitionEntity**](PropertyDefinitionEntity.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested property definition entity |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

