# lusid.StructuredResultDataApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_data_map**](StructuredResultDataApi.md#create_data_map) | **POST** /api/api/unitresults/datamap/{scope} | CreateDataMap: Create data map
[**delete_structured_result_data**](StructuredResultDataApi.md#delete_structured_result_data) | **POST** /api/api/unitresults/{scope}/$delete | DeleteStructuredResultData: Delete structured result data
[**get_address_key_definitions_for_document**](StructuredResultDataApi.md#get_address_key_definitions_for_document) | **GET** /api/api/unitresults/virtualdocument/{scope}/{code}/{source}/{resultType}/addresskeydefinitions | GetAddressKeyDefinitionsForDocument: Get AddressKeyDefinitions for a virtual document.
[**get_data_map**](StructuredResultDataApi.md#get_data_map) | **POST** /api/api/unitresults/datamap/{scope}/$get | GetDataMap: Get data map
[**get_structured_result_data**](StructuredResultDataApi.md#get_structured_result_data) | **POST** /api/api/unitresults/{scope}/$get | GetStructuredResultData: Get structured result data
[**get_virtual_document**](StructuredResultDataApi.md#get_virtual_document) | **POST** /api/api/unitresults/virtualdocument/{scope}/$get | GetVirtualDocument: Get Virtual Documents
[**get_virtual_document_rows**](StructuredResultDataApi.md#get_virtual_document_rows) | **GET** /api/api/unitresults/virtualdocument/{scope}/{code}/{source}/{resultType} | GetVirtualDocumentRows: Get Virtual Document Rows
[**upsert_result_value**](StructuredResultDataApi.md#upsert_result_value) | **POST** /api/api/unitresults/resultvalue/{scope} | UpsertResultValue: Upsert result value
[**upsert_structured_result_data**](StructuredResultDataApi.md#upsert_structured_result_data) | **POST** /api/api/unitresults/{scope} | UpsertStructuredResultData: Upsert structured result data


### Example

```python
from finbourne.sdk.exceptions import ApiException
from finbourne.sdk.extensions.configuration_options import ConfigurationOptions
from finbourne.sdk.services.lusid.models import *

from finbourne.sdk.extensions import (
  SyncApiClientFactory
)

from finbourne.sdk.services.lusid.api.structured_result_data_api import StructuredResultDataApi

# opts = ConfigurationOptions()
# opts.total_timeout_ms = 30_000

# uncomment the below to use an api client factory with overrides
# api_client_factory = SyncApiClientFactory(opts=opts)

api_client_factory = SyncApiClientFactory()
api_instance = api_client_factory.build(StructuredResultDataApi)
```

---

# **create_data_map**
> UpsertStructuredDataResponse createDataMap = create_data_map(scope, request_body)

CreateDataMap: Create data map

Create or update one or more structured result store address definition data maps in a particular scope. Note these are immutable and cannot be changed once created.                In the request, each data map must be keyed by a unique correlation ID. This ID is ephemeral and not stored by LUSID.  It serves only to easily identify each data map object in the response.                The response returns both the collection of successfully created or updated data maps, as well as those that failed.  For each failure, a reason is provided.                It is important to check the failed set for any unsuccessful results.

### Example

```python
api_instance = api_client_factory.build(StructuredResultDataApi)
scope = 'scope_example' # str
request_body = {"id1":{"id":{"version":"1.0.0","code":"dataMapCode"},"data":{"dataDefinitions":[{"address":"Instrument/default/LusidInstrumentId","name":"luid","dataType":"String","keyType":"Unique","allowNull":false,"allowMissing":false},{"address":"Valuation/PV","dataType":"Result0D","keyType":"Leaf","allowNull":false,"allowMissing":false},{"address":"Valuation/PV/Amount","name":"pv","dataType":"Decimal","keyType":"Leaf","allowNull":false,"allowMissing":false},{"address":"Valuation/PV/Ccy","name":"pv-ccy","dataType":"String","keyType":"Leaf","allowNull":false,"allowMissing":false},{"address":"Instrument/default/Name","name":"instrument-name","dataType":"String","keyType":"Leaf","allowNull":false,"allowMissing":false}]}}} # Dict[str, CreateDataMapRequest]
api_response = api_instance.create_data_map(scope, request_body)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope in which to create or update data maps. | [required] 
 **request_body** | [**Dict[str, CreateDataMapRequest]**](CreateDataMapRequest.md)| Individual data map creation requests. | [required] 

### Return type

[**UpsertStructuredDataResponse**](UpsertStructuredDataResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The successfully created or updated data maps along with any failures. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **delete_structured_result_data**
> AnnulStructuredDataResponse deleteStructuredResultData = delete_structured_result_data(scope, request_body)

DeleteStructuredResultData: Delete structured result data

Delete one or more structured result data items from a particular scope. Each item is identified by a unique ID which includes  information about its type as well as the exact effective datetime (to the microsecond) at which it entered the system (became valid).                In the request, each data item must be keyed by a unique correlation ID. This ID is ephemeral and not stored by LUSID.  It serves only to easily identify each data item in the response.                The response returns both the collection of successfully deleted data items, as well as those that failed.  For each failure, a reason is provided.                It is important to check the failed set for any unsuccessful results.

### Example

```python
api_instance = api_client_factory.build(StructuredResultDataApi)
scope = 'scope_example' # str
request_body = {"SomeCorrelationId1":{"source":"MiddleOffice","code":"MyUploadedRiskResults","effectiveAt":"2018-03-05T00:00:00.0000000+00:00","resultType":"Risk"}} # Dict[str, StructuredResultDataId]
api_response = api_instance.delete_structured_result_data(scope, request_body)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope from which to delete data items. | [required] 
 **request_body** | [**Dict[str, StructuredResultDataId]**](StructuredResultDataId.md)| The data IDs to delete, each keyed by a unique, ephemeral correlation ID. | [required] 

### Return type

[**AnnulStructuredDataResponse**](AnnulStructuredDataResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The successfully deleted data items along with any failures. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_address_key_definitions_for_document**
> ResourceListOfAddressKeyDefinition getAddressKeyDefinitionsForDocument = get_address_key_definitions_for_document(scope, code, source, result_type, effective_at=effective_at, as_at=as_at)

GetAddressKeyDefinitionsForDocument: Get AddressKeyDefinitions for a virtual document.

For a given virtual document retrieve all the address key definitions that are in use.

### Example

```python
api_instance = api_client_factory.build(StructuredResultDataApi)
scope = 'scope_example' # str
code = 'code_example' # str
source = 'source_example' # str
result_type = 'result_type_example' # str
effective_at = 'effective_at_example' # str (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
api_response = api_instance.get_address_key_definitions_for_document(scope, code, source, result_type, effective_at=effective_at, as_at=as_at)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the document for which address key definitions are retrieved. | [required] 
 **code** | **str**| The code of the document for which address key definitions are retrieved. | [required] 
 **source** | **str**| The source of the document for which address key definitions are retrieved. | [required] 
 **result_type** | **str**| The result type of the document for which address key definitions are retrieved. | [required] 
 **effective_at** | **str**| The effective datetime to query the document for which the address key definitions are retrieved.              Defaults to querying the latest version if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime to query the document for which the address key definitions are retrieved.              Defaults to querying the latest version if not specified. | [optional] 

### Return type

[**ResourceListOfAddressKeyDefinition**](ResourceListOfAddressKeyDefinition.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A collection of address key definitions. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_data_map**
> GetDataMapResponse getDataMap = get_data_map(scope, request_body)

GetDataMap: Get data map

Retrieve one or more structured result store address definition data maps from a particular scope.                Each data map can be identified by its invariant key, which can be thought of as a permanent URL.  For each ID, LUSID returns the most recently matched item.                In the request, each data map must be keyed by a unique correlation ID. This ID is ephemeral and not stored by LUSID.  It serves only to easily identify each data map in the response.                The response returns three collections. The first contains successfully retrieved data maps. The second contains those with a  valid identifier but that could not be found. The third contains those that failed because LUSID could not construct a valid identifier from the request.                For the IDs that failed to resolve or could not be found, a reason is provided.                It is important to check the failed sets for any unsuccessful results.

### Example

```python
api_instance = api_client_factory.build(StructuredResultDataApi)
scope = 'scope_example' # str
request_body = {"id1":{"version":"1.0.0","code":"dataMapCode"}} # Dict[str, DataMapKey]
api_response = api_instance.get_data_map(scope, request_body)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope from which to retrieve data maps. | [required] 
 **request_body** | [**Dict[str, DataMapKey]**](DataMapKey.md)| The data map keys to look up, each keyed by a unique, ephemeral correlation ID. | [required] 

### Return type

[**GetDataMapResponse**](GetDataMapResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The successfully retrieved data maps along with any failures. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_structured_result_data**
> GetStructuredResultDataResponse getStructuredResultData = get_structured_result_data(scope, request_body, as_at=as_at, max_age=max_age)

GetStructuredResultData: Get structured result data

Retrieve one or more structured result data items from a particular scope.                Each item can be identified by its time invariant structured result data identifier. For each ID, LUSID  returns the most recently matched item with respect to the provided (or default) effective datetime.                 An optional maximum age range window can be specified to control how far back to look from the specified  effective datetime. LUSID returns the most recent item within this window.                In the request, each data item must be keyed by a unique correlation ID. This ID is ephemeral and not stored by LUSID.  It serves only to easily identify each data item in the response.    The response returns three collections. The first contains successfully retrieved data items. The second contains those with a  valid identifier but that could not be found. The third contains those that failed because LUSID could not construct a valid identifier from the request.    For the IDs that failed to resolve or could not be found, a reason is provided.                It is important to check the failed sets for any unsuccessful results.

### Example

```python
api_instance = api_client_factory.build(StructuredResultDataApi)
scope = 'scope_example' # str
request_body = {"SomeCorrelationId1":{"source":"MiddleOffice","code":"MyUploadedRiskResults","effectiveAt":"2018-03-05T00:00:00.0000000+00:00","resultType":"Risk"}} # Dict[str, StructuredResultDataId]
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
max_age = 'max_age_example' # str (optional)
api_response = api_instance.get_structured_result_data(scope, request_body, as_at=as_at, max_age=max_age)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope from which to retrieve data items. | [required] 
 **request_body** | [**Dict[str, StructuredResultDataId]**](StructuredResultDataId.md)| The time invariant set of structured data identifiers to retrieve, keyed by a unique, ephemeral correlation ID. | [required] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the structured result data. Defaults to returning the latest version if not specified. | [optional] 
 **max_age** | **str**| The duration of the look-back window in ISO8601 time interval format, for example &#39;P1Y2M3DT4H30M&#39; (1 year, 2 months, 3 days, 4 hours and 30 minutes).               This is subtracted from the provided effectiveAt datetime to generate a effective datetime window inside which a data item must exist to be retrieved. | [optional] 

### Return type

[**GetStructuredResultDataResponse**](GetStructuredResultDataResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The successfully retrieved data items along with any failures. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_virtual_document**
> GetVirtualDocumentResponse getVirtualDocument = get_virtual_document(scope, request_body, as_at=as_at)

GetVirtualDocument: Get Virtual Documents

Retrieve one or more virtual documents from a particular scope.                Each item can be identified by its time invariant structured result data identifier. For each ID, LUSID  returns the most recently matched item with respect to the provided effective datetime.                In the request, each data item must be keyed by a unique correlation ID. This ID is ephemeral and not stored by LUSID.  It serves only to easily identify each data item in the response.                The response returns two collections. The first contains successfully retrieved data items. The second contains those with a  valid identifier but that could not be found, or those that failed because LUSID could not construct a valid identifier from the request.                For the IDs that failed to resolve or could not be found, a reason is provided.                It is important to check the failed sets for any unsuccessful results.

### Example

```python
api_instance = api_client_factory.build(StructuredResultDataApi)
scope = 'scope_example' # str
request_body = {"SomeCorrelationId1":{"source":"MiddleOffice","code":"MyUploadedRiskResults","effectiveAt":"2018-03-05T00:00:00.0000000+00:00","resultType":"Risk"}} # Dict[str, StructuredResultDataId]
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
api_response = api_instance.get_virtual_document(scope, request_body, as_at=as_at)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope in which to construct the virtual documents. | [required] 
 **request_body** | [**Dict[str, StructuredResultDataId]**](StructuredResultDataId.md)| The time invariant set of structured data identifiers to retrieve, keyed by a unique, ephemeral correlation ID. | [required] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the structured result data. Defaults to returning the latest version if not specified. | [optional] 

### Return type

[**GetVirtualDocumentResponse**](GetVirtualDocumentResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The successfully retrieved virtual documents along with any failures. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_virtual_document_rows**
> PagedResourceListOfVirtualRow getVirtualDocumentRows = get_virtual_document_rows(scope, code, source, result_type, effective_at, as_at=as_at, page=page, limit=limit, filter=filter)

GetVirtualDocumentRows: Get Virtual Document Rows

Retrieve the rows of the virtual document with the specified identifiers and the given effectiveAt date time.    Get virtual document rows merges multiple StructuredResultData items upserted with UpsertStructuredResultData  for a single StructuredResultDataId.                Since an item of StructuredResultData is always upserted with a StructuredResultDataId, of which  effectiveAt is a part, then merging across the asAt dimension is supported but not merging across the  effectiveAt dimension.

### Example

```python
api_instance = api_client_factory.build(StructuredResultDataApi)
scope = 'scope_example' # str
code = 'code_example' # str
source = 'source_example' # str
result_type = 'result_type_example' # str
effective_at = 'effective_at_example' # str
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
page = 'page_example' # str (optional)
limit = 56 # int (optional)
filter = 'filter_example' # str (optional)
api_response = api_instance.get_virtual_document_rows(scope, code, source, result_type, effective_at, as_at=as_at, page=page, limit=limit, filter=filter)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope in which to retrieve the virtual document. | [required] 
 **code** | **str**| The code of the virtual document to retrieve. | [required] 
 **source** | **str**| The source of the virtual document to retrieve. | [required] 
 **result_type** | **str**| The result type of the virtual document to retrieve. | [required] 
 **effective_at** | **str**| The effectiveAt datetime at which to retrieve the virtual document. | [required] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the virtual document. Defaults to returning the latest version if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing virtual document rows from a previous               call to list virtual document rows. This value is returned from the previous call. If a pagination token is               provided the filter, effectiveAt, and asAt fields must not have changed since the original request. | [optional] 
 **limit** | **int**| When paginating, limit the number of returned results to this many. | [optional] 
 **filter** | **str**| Expression to filter the result set. Read more about filtering results from LUSID here:               https://support.lusid.com/filtering-results-from-lusid. | [optional] 

### Return type

[**PagedResourceListOfVirtualRow**](PagedResourceListOfVirtualRow.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The rows of the virtual document. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **upsert_result_value**
> UpsertStructuredDataResponse upsertResultValue = upsert_result_value(scope, request_body)

UpsertResultValue: Upsert result value

Create or update one or more Upsert one or more result values in a particular scope. An item is updated if it already exists  and created if it does not.                In the request, each data item must be keyed by a unique correlation ID. This ID is ephemeral and not stored by LUSID.  It serves only to easily identify each data item in the response.                The response returns both the collection of successfully created or updated data items, as well as those that failed.  For each failure, a reason is provided.                It is important to check the failed set for any unsuccessful results.

### Example

```python
api_instance = api_client_factory.build(StructuredResultDataApi)
scope = 'scope_example' # str
request_body = {"SomeCorrelationId1":{"documentId":{"source":"MiddleOffice","code":"MyUploadedRiskResults","effectiveAt":"2018-03-05T00:00:00.0000000+00:00","resultType":"UnitResult/Analytic"},"key":{"UnitResult/LusidInstrumentId":"LUID_0000ABCD"},"dataAddress":"UnitResult/Valuation/InstrumentAccrued","resultValue":{"units":"USD","value":0.0102,"dimension":0,"resultValueType":"ResultValue0D"}}} # Dict[str, UpsertResultValuesDataRequest]
api_response = api_instance.upsert_result_value(scope, request_body)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope in which to construct the virtual documents. | [required] 
 **request_body** | [**Dict[str, UpsertResultValuesDataRequest]**](UpsertResultValuesDataRequest.md)| The time invariant set of structured data identifiers to retrieve, keyed by a unique, ephemeral correlation ID. | [required] 

### Return type

[**UpsertStructuredDataResponse**](UpsertStructuredDataResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The successfully retrieved virtual documents along with any failures. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **upsert_structured_result_data**
> UpsertStructuredDataResponse upsertStructuredResultData = upsert_structured_result_data(scope, request_body)

UpsertStructuredResultData: Upsert structured result data

Create or update one or more structured result data items in a particular scope. An item is updated if it already exists  and created if it does not.                In the request, each data item must be keyed by a unique correlation ID. This ID is ephemeral and not stored by LUSID.  It serves only to easily identify each data item in the response.                The response returns both the collection of successfully created or updated data items, as well as those that failed.  For each failure, a reason is provided.                It is important to check the failed set for any unsuccessful results.

### Example

```python
api_instance = api_client_factory.build(StructuredResultDataApi)
scope = 'scope_example' # str
request_body = {"first-item":{"id":{"source":"Client","code":"MyCustomDocument","effectiveAt":"2020-01-01T00:00:00.0000000+00:00","resultType":"UnitResult/Custom"},"data":{"documentFormat":"Csv","version":"1.0.0","name":"my document identifier","document":"luid,pv,pv-ccy,instrument-name\nLUID_11111111,1,GBP,instr1\nLUID_22222222,2,USD,instr2","dataMapKey":{"version":"1.0.0","code":"dataMapCode"}}},"second-item":{"id":{"source":"Client","code":"MyUploadedRiskResults-1","effectiveAt":"2018-03-05T00:00:00.0000000+00:00","resultType":"Risk"},"data":{"documentFormat":"Xml","version":"1.0.0","name":"free text identifier of document 1","document":"<xml>data</xml>"}},"third-item":{"id":{"source":"Client","code":"MyUploadedRiskResults-2","effectiveAt":"2018-03-05T00:00:00.0000000+00:00","resultType":"Risk"},"data":{"documentFormat":"Json","version":"1.0.0","name":"free text identifier of document 2","document":"{ \"some\":\"valid json\"}"}}} # Dict[str, UpsertStructuredResultDataRequest]
api_response = api_instance.upsert_structured_result_data(scope, request_body)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope in which to create or update data items. | [required] 
 **request_body** | [**Dict[str, UpsertStructuredResultDataRequest]**](UpsertStructuredResultDataRequest.md)| The set of data items to create or update, keyed by a unique, ephemeral correlation ID. | [required] 

### Return type

[**UpsertStructuredDataResponse**](UpsertStructuredDataResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The successfully created or updated data items along with any failures. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

