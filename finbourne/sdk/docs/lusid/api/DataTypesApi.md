# lusid.DataTypesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_data_type**](DataTypesApi.md#create_data_type) | **POST** /api/api/datatypes | [EARLY ACCESS] CreateDataType: Create data type definition
[**delete_data_type**](DataTypesApi.md#delete_data_type) | **DELETE** /api/api/datatypes/{scope}/{code} | DeleteDataType: Delete a data type definition.
[**get_data_type**](DataTypesApi.md#get_data_type) | **GET** /api/api/datatypes/{scope}/{code} | GetDataType: Get data type definition
[**get_units_from_data_type**](DataTypesApi.md#get_units_from_data_type) | **GET** /api/api/datatypes/{scope}/{code}/units | [EARLY ACCESS] GetUnitsFromDataType: Get units from data type
[**list_data_type_summaries**](DataTypesApi.md#list_data_type_summaries) | **GET** /api/api/datatypes | [EARLY ACCESS] ListDataTypeSummaries: List all data type summaries, without the reference data
[**list_data_types**](DataTypesApi.md#list_data_types) | **GET** /api/api/datatypes/{scope} | ListDataTypes: List data types
[**update_data_type**](DataTypesApi.md#update_data_type) | **PUT** /api/api/datatypes/{scope}/{code} | [EARLY ACCESS] UpdateDataType: Update data type definition
[**update_reference_data**](DataTypesApi.md#update_reference_data) | **PUT** /api/api/datatypes/{scope}/{code}/referencedata | [EARLY ACCESS] UpdateReferenceData: Update all reference data on a data type, includes the reference values, the field definitions, field values
[**update_reference_values**](DataTypesApi.md#update_reference_values) | **PUT** /api/api/datatypes/{scope}/{code}/referencedatavalues | [EARLY ACCESS] UpdateReferenceValues: Update reference data on a data type


### Example

```python
from finbourne.sdk.exceptions import ApiException
from finbourne.sdk.extensions.configuration_options import ConfigurationOptions
from finbourne.sdk.services.lusid.models import *

from finbourne.sdk.extensions import (
  SyncApiClientFactory
)

from finbourne.sdk.services.lusid.api.data_types_api import DataTypesApi

# opts = ConfigurationOptions()
# opts.total_timeout_ms = 30_000

# uncomment the below to use an api client factory with overrides
# api_client_factory = SyncApiClientFactory(opts=opts)

api_client_factory = SyncApiClientFactory()
api_instance = api_client_factory.build(DataTypesApi)
```

---

# **create_data_type**
> DataType createDataType = create_data_type(create_data_type_request=create_data_type_request)

[EARLY ACCESS] CreateDataType: Create data type definition

Create a new data type definition    Data types cannot be created in either the \"default\" or \"system\" scopes.

### Example

```python
api_instance = api_client_factory.build(DataTypesApi)
create_data_type_request = CreateDataTypeRequest()
api_response = api_instance.create_data_type(create_data_type_request=create_data_type_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_data_type_request** | [**CreateDataTypeRequest**](CreateDataTypeRequest.md)| The definition of the new data type | [optional] 

### Return type

[**DataType**](DataType.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **delete_data_type**
> DeletedEntityResponse deleteDataType = delete_data_type(scope, code)

DeleteDataType: Delete a data type definition.

Delete an existing data type definition.    Data types cannot be deleted in either the \"default\" or \"system\" scopes, scopes beginning with \"LUSID-\",  or data types that are in use on a property definition.

### Example

```python
api_instance = api_client_factory.build(DataTypesApi)
scope = 'scope_example' # str
code = 'code_example' # str
api_response = api_instance.delete_data_type(scope, code)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the data type | [required] 
 **code** | **str**| The code of the data type | [required] 

### Return type

[**DeletedEntityResponse**](DeletedEntityResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_data_type**
> DataType getDataType = get_data_type(scope, code, as_at=as_at)

GetDataType: Get data type definition

Get the definition of a specified data type

### Example

```python
api_instance = api_client_factory.build(DataTypesApi)
scope = 'scope_example' # str
code = 'code_example' # str
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
api_response = api_instance.get_data_type(scope, code, as_at=as_at)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the data type | [required] 
 **code** | **str**| The code of the data type | [required] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the data type definition. Defaults to              return the latest version of the instrument definition if not specified. | [optional] 

### Return type

[**DataType**](DataType.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_units_from_data_type**
> ResourceListOfIUnitDefinitionDto getUnitsFromDataType = get_units_from_data_type(scope, code, units=units, filter=filter, as_at=as_at)

[EARLY ACCESS] GetUnitsFromDataType: Get units from data type

Get the definitions of the specified units associated bound to a specific data type

### Example

```python
api_instance = api_client_factory.build(DataTypesApi)
scope = 'scope_example' # str
code = 'code_example' # str
units = ['units_example'] # List[str] (optional)
filter = 'filter_example' # str (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
api_response = api_instance.get_units_from_data_type(scope, code, units=units, filter=filter, as_at=as_at)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the data type | [required] 
 **code** | **str**| The code of the data type | [required] 
 **units** | [**List[str]**](str.md)| One or more unit identifiers for which the definition is being requested | [optional] 
 **filter** | **str**| Optional. Expression to filter the result set.               For example, to filter on the Schema, use \&quot;schema eq &#39;string&#39;\&quot;              Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. | [optional] 
 **as_at** | **datetime**| Optional. The as at of the requested data type | [optional] 

### Return type

[**ResourceListOfIUnitDefinitionDto**](ResourceListOfIUnitDefinitionDto.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **list_data_type_summaries**
> PagedResourceListOfDataTypeSummary listDataTypeSummaries = list_data_type_summaries(as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by)

[EARLY ACCESS] ListDataTypeSummaries: List all data type summaries, without the reference data

List all data type summaries

### Example

```python
api_instance = api_client_factory.build(DataTypesApi)
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
page = 'page_example' # str (optional)
limit = 56 # int (optional)
filter = 'filter_example' # str (optional)
sort_by = ['sort_by_example'] # List[str] (optional)
api_response = api_instance.list_data_type_summaries(as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **as_at** | **datetime**| The asAt datetime at which to list the data type summaries. Defaults to returning the latest version               of each summary if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing data type summaries. This  value is returned from the previous call. If a pagination token is provided, the filter, sortBy  and asAt fields must not have changed since the original request. | [optional] 
 **limit** | **int**| When paginating, limit the results to this number. Defaults to 100 if not specified. | [optional] 
 **filter** | **str**| Optional. Expression to filter the result set.                For example, to filter on the Scope, use \&quot;id.scope eq &#39;myscope&#39;\&quot;, to filter on Schema, use \&quot;schema eq &#39;string&#39;\&quot;,               to filter on AcceptableValues use \&quot;acceptableValues any (~ eq &#39;value&#39;)\&quot;               Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. | [optional] 
 **sort_by** | [**List[str]**](str.md)| A list of field names to sort by, each suffixed by \&quot; ASC\&quot; or \&quot; DESC\&quot; | [optional] 

### Return type

[**PagedResourceListOfDataTypeSummary**](PagedResourceListOfDataTypeSummary.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **list_data_types**
> ResourceListOfDataType listDataTypes = list_data_types(scope, as_at=as_at, include_system=include_system, sort_by=sort_by, limit=limit, filter=filter)

ListDataTypes: List data types

List all data types in a specified scope

### Example

```python
api_instance = api_client_factory.build(DataTypesApi)
scope = 'scope_example' # str
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
include_system = True # bool (optional)
sort_by = ['sort_by_example'] # List[str] (optional)
limit = 56 # int (optional)
filter = 'filter_example' # str (optional)
api_response = api_instance.list_data_types(scope, as_at=as_at, include_system=include_system, sort_by=sort_by, limit=limit, filter=filter)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The requested scope of the data types | [required] 
 **as_at** | **datetime**| The as at of the requested data types | [optional] 
 **include_system** | **bool**| Whether to additionally include those data types in the \&quot;system\&quot; scope | [optional] 
 **sort_by** | [**List[str]**](str.md)| Optional. Order the results by these fields. Use use the &#39;-&#39; sign to denote descending order e.g. -MyFieldName | [optional] 
 **limit** | **int**| Optional. When paginating, limit the number of returned results to this many. | [optional] 
 **filter** | **str**| Optional. Expression to filter the result set.              For example, to filter on the Display Name, use \&quot;displayName eq &#39;string&#39;\&quot;              Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. | [optional] 

### Return type

[**ResourceListOfDataType**](ResourceListOfDataType.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **update_data_type**
> DataType updateDataType = update_data_type(scope, code, update_data_type_request)

[EARLY ACCESS] UpdateDataType: Update data type definition

Update the definition of the specified existing data type    Not all elements within a data type definition are modifiable due to the potential implications for data  already stored against the types

### Example

```python
api_instance = api_client_factory.build(DataTypesApi)
scope = 'scope_example' # str
code = 'code_example' # str
update_data_type_request = UpdateDataTypeRequest()
api_response = api_instance.update_data_type(scope, code, update_data_type_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the data type | [required] 
 **code** | **str**| The code of the data type | [required] 
 **update_data_type_request** | [**UpdateDataTypeRequest**](UpdateDataTypeRequest.md)| The updated definition of the data type | [required] 

### Return type

[**DataType**](DataType.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **update_reference_data**
> DataType updateReferenceData = update_reference_data(scope, code, update_reference_data_request)

[EARLY ACCESS] UpdateReferenceData: Update all reference data on a data type, includes the reference values, the field definitions, field values

Replaces the whole set of reference data

### Example

```python
api_instance = api_client_factory.build(DataTypesApi)
scope = 'scope_example' # str
code = 'code_example' # str
update_reference_data_request = UpdateReferenceDataRequest()
api_response = api_instance.update_reference_data(scope, code, update_reference_data_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the data type | [required] 
 **code** | **str**| The code of the data type | [required] 
 **update_reference_data_request** | [**UpdateReferenceDataRequest**](UpdateReferenceDataRequest.md)| The updated reference data | [required] 

### Return type

[**DataType**](DataType.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **update_reference_values**
> DataType updateReferenceValues = update_reference_values(scope, code, field_value)

[EARLY ACCESS] UpdateReferenceValues: Update reference data on a data type

Replaces the whole set of reference values

### Example

```python
api_instance = api_client_factory.build(DataTypesApi)
scope = 'scope_example' # str
code = 'code_example' # str
field_value = [{"value":"FRA","fields":{"english_short_name":"France","continent":"Europe"},"numericFields":{"population_in_millions":68.0}},{"value":"DEU","fields":{"english_short_name":"Germany","continent":"Europe"},"numericFields":{"population_in_millions":84.0}}] # List[FieldValue]
api_response = api_instance.update_reference_values(scope, code, field_value)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the data type | [required] 
 **code** | **str**| The code of the data type | [required] 
 **field_value** | [**List[FieldValue]**](FieldValue.md)| The updated reference values | [required] 

### Return type

[**DataType**](DataType.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

